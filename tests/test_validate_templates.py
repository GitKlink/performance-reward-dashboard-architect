from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-templates.py"
SPEC = importlib.util.spec_from_file_location("validate_templates", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TemplateValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "templates").mkdir(parents=True)
        (self.root / "schemas").mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_schema(self, subject: str, version: str = "0.1.0") -> Path:
        target = self.root / "schemas" / f"{subject}.schema.yaml"
        target.write_text(
            yaml.safe_dump(
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "$id": (
                        "urn:performance-reward-dashboard-architect:schema:"
                        f"{subject}:{version}"
                    ),
                    "title": subject,
                    "type": "object",
                    "additionalProperties": False,
                    "x-repository": {
                        "artifact_id": "SCHEMA-CORE-001",
                        "status": "DRAFT",
                        "phase": 2,
                        "schema_version": version,
                        "content_version": version,
                        "owner": "docs/standard.md",
                    },
                    "required": ["name"],
                    "properties": {"name": {"type": "string"}},
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        return target

    def write_template(
        self,
        subject: str,
        *,
        template_id: str = "TPL-CORE-001",
        schema_reference: str | None = None,
        schema_version: str = "0.1.0",
        status: str = "DRAFT",
        body: str = "# Example template\n",
    ) -> Path:
        target = self.root / "templates" / f"{subject}.md"
        if status == "PLACEHOLDER":
            metadata = {
                "status": status,
                "phase": 2,
                "priority": "medium",
            }
        else:
            metadata = {
                "template_id": template_id,
                "status": status,
                "content_version": "0.1.0",
                "schema": schema_reference or f"../schemas/{subject}.schema.yaml",
                "schema_version": schema_version,
                "last_reviewed": "2026-07-17",
            }
        target.write_text(
            "---\n"
            + yaml.safe_dump(metadata, sort_keys=False)
            + "---\n\n"
            + body,
            encoding="utf-8",
        )
        return target

    def messages(self) -> list[str]:
        return [finding.message for finding in MODULE.validate_repository(self.root)]

    def test_valid_template_passes(self) -> None:
        self.write_schema("example")
        self.write_template("example")
        self.assertEqual([], self.messages())

    def test_missing_schema_fails(self) -> None:
        self.write_template("example")
        self.assertTrue(any("missing schema" in message for message in self.messages()))

    def test_schema_version_mismatch_fails(self) -> None:
        self.write_schema("example", version="0.2.0")
        self.write_template("example", schema_version="0.1.0")
        self.assertTrue(any("does not match schema" in message for message in self.messages()))

    def test_duplicate_template_id_fails(self) -> None:
        self.write_schema("one")
        self.write_schema("two")
        self.write_template("one", template_id="TPL-CORE-001")
        self.write_template("two", template_id="TPL-CORE-001")
        self.assertTrue(any("duplicate template_id" in message for message in self.messages()))

    def test_filename_schema_mismatch_fails(self) -> None:
        self.write_schema("other")
        self.write_template(
            "example",
            schema_reference="../schemas/other.schema.yaml",
        )
        self.assertTrue(any("should map to" in message for message in self.messages()))

    def test_placeholder_requires_explanation(self) -> None:
        self.write_template(
            "wireframe",
            status="PLACEHOLDER",
            body="# Wireframe\n\nFuture work remains.\n",
        )
        findings = MODULE.validate_repository(self.root)
        self.assertTrue(
            any("does not explain placeholder status" in finding.message for finding in findings)
        )

    def test_schema_without_active_template_fails(self) -> None:
        self.write_schema("example")
        self.write_template(
            "example",
            status="PLACEHOLDER",
            body="# Example\n\nThis is a placeholder.\n",
        )
        self.assertTrue(
            any("schemas without active matching templates" in message for message in self.messages())
        )


if __name__ == "__main__":
    unittest.main()
