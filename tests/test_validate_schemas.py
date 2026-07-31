from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-schemas.py"
SPEC = importlib.util.spec_from_file_location("validate_schemas", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SchemaValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "schemas").mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    @staticmethod
    def valid_schema(subject: str = "example") -> dict[str, object]:
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": (
                "urn:performance-reward-dashboard-architect:schema:"
                f"{subject}:0.1.0"
            ),
            "title": "Example schema",
            "type": "object",
            "additionalProperties": False,
            "x-repository": {
                "artifact_id": "SCHEMA-CORE-001",
                "status": "DRAFT",
                "phase": 2,
                "schema_version": "0.1.0",
                "content_version": "0.1.0",
                "owner": "docs/standard.md",
            },
            "required": ["name"],
            "properties": {"name": {"type": "string", "minLength": 1}},
        }

    def write_schema(
        self,
        subject: str = "example",
        schema: dict[str, object] | None = None,
    ) -> Path:
        target = self.root / "schemas" / f"{subject}.schema.yaml"
        target.write_text(
            yaml.safe_dump(schema or self.valid_schema(subject), sort_keys=False),
            encoding="utf-8",
        )
        return target

    def messages(self) -> list[str]:
        return [finding.message for finding in MODULE.validate_repository(self.root)]

    def test_valid_schema_passes(self) -> None:
        self.write_schema()
        self.assertEqual([], self.messages())

    def test_wrong_dialect_fails(self) -> None:
        schema = self.valid_schema()
        schema["$schema"] = "https://json-schema.org/draft/2019-09/schema"
        self.write_schema(schema=schema)
        self.assertTrue(any("Draft 2020-12" in message for message in self.messages()))

    def test_undeclared_required_field_fails(self) -> None:
        schema = self.valid_schema()
        schema["required"] = ["name", "missing"]
        self.write_schema(schema=schema)
        self.assertTrue(
            any("not declared in properties" in message for message in self.messages())
        )

    def test_duplicate_schema_id_fails(self) -> None:
        first = self.valid_schema("one")
        second = self.valid_schema("two")
        second["$id"] = first["$id"]
        second["x-repository"] = dict(second["x-repository"])
        second["x-repository"]["artifact_id"] = "SCHEMA-CORE-002"
        self.write_schema("one", first)
        self.write_schema("two", second)
        self.assertTrue(any("duplicate schema $id" in message for message in self.messages()))

    def test_valid_fixture_passes(self) -> None:
        self.write_schema()
        fixture_root = self.root / "schemas" / "examples"
        fixture_root.mkdir()
        (fixture_root / "example.valid.yaml").write_text(
            yaml.safe_dump({"name": "valid"}),
            encoding="utf-8",
        )
        self.assertEqual([], self.messages())

    def test_valid_fixture_with_invalid_content_fails(self) -> None:
        self.write_schema()
        fixture_root = self.root / "schemas" / "examples"
        fixture_root.mkdir()
        (fixture_root / "example.valid.yaml").write_text(
            yaml.safe_dump({"name": ""}),
            encoding="utf-8",
        )
        self.assertTrue(any("expected valid" in message for message in self.messages()))

    def test_invalid_fixture_that_passes_fails(self) -> None:
        self.write_schema()
        fixture_root = self.root / "schemas" / "examples"
        fixture_root.mkdir()
        (fixture_root / "example.invalid.yaml").write_text(
            yaml.safe_dump({"name": "valid"}),
            encoding="utf-8",
        )
        self.assertTrue(any("expected invalid" in message for message in self.messages()))


if __name__ == "__main__":
    unittest.main()
