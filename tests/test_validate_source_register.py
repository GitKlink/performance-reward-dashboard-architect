from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-source-register.py"
SPEC = importlib.util.spec_from_file_location("validate_source_register", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SourceRegisterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "knowledge/research-register/trials").mkdir(parents=True)
        self.write_artifact_register()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_artifact_register(self) -> None:
        payload = {
            "artifacts": [
                {
                    "artifact_id": "STD-CORE-001",
                    "path": "docs/standard.md",
                    "type": "STD",
                    "domain": "CORE",
                    "phase": 0,
                    "status": "DRAFT",
                    "depends_on": [],
                    "blocks": [],
                }
            ]
        }
        (self.root / "ARTIFACT-REGISTER.yaml").write_text(
            yaml.safe_dump(payload, sort_keys=False),
            encoding="utf-8",
        )

    @staticmethod
    def valid_source(source_id: str = "example-source") -> dict[str, object]:
        return {
            "source_id": source_id,
            "title": "Example source",
            "author_or_organisation": "Example Organisation",
            "source_type": "official-product-documentation",
            "evidence_level": "primary-authoritative",
            "url_or_doi": f"https://example.com/{source_id}",
            "publication_date": "2026-01-01",
            "updated_date": None,
            "retrieved_date": "2026-07-01",
            "version": "current",
            "jurisdiction": "global",
            "lifecycle_state": "accepted",
            "licence_or_usage_notes": "Cite and paraphrase.",
            "relevant_artifacts": ["STD-CORE-001"],
            "relevant_claims": ["Example supported claim."],
            "review_notes": "Reverify before release.",
        }

    def write_sources(self, sources: list[dict[str, object]]) -> None:
        payload = {"register": {"artifact_id": "KNOW-CORE-002"}, "sources": sources}
        (self.root / "knowledge/research-register/sources.yaml").write_text(
            yaml.safe_dump(payload, sort_keys=False),
            encoding="utf-8",
        )

    def messages(self) -> list[str]:
        return [
            finding.message
            for finding in MODULE.validate_source_register(
                self.root,
                today=date(2026, 7, 17),
            )
        ]

    def test_valid_source_passes(self) -> None:
        self.write_sources([self.valid_source()])
        self.assertEqual([], self.messages())

    def test_duplicate_source_id_fails(self) -> None:
        self.write_sources([self.valid_source(), self.valid_source()])
        self.assertTrue(any("duplicate source_id" in message for message in self.messages()))

    def test_invalid_evidence_level_fails(self) -> None:
        source = self.valid_source()
        source["evidence_level"] = "best-source"
        self.write_sources([source])
        self.assertTrue(any("unsupported evidence_level" in message for message in self.messages()))

    def test_unknown_artifact_id_fails(self) -> None:
        source = self.valid_source()
        source["relevant_artifacts"] = ["STD-CORE-999"]
        self.write_sources([source])
        self.assertTrue(any("unregistered artifact" in message for message in self.messages()))

    def test_unknown_central_source_reference_fails(self) -> None:
        self.write_sources([self.valid_source()])
        (self.root / "knowledge/research-register/trials/trial.md").write_text(
            "Central source ID: `missing-source`.\n",
            encoding="utf-8",
        )
        self.assertTrue(any("unknown central source ID" in message for message in self.messages()))

    def test_legacy_descriptive_artifact_reference_warns(self) -> None:
        source = self.valid_source()
        source["relevant_artifacts"] = ["future skill"]
        self.write_sources([source])
        findings = MODULE.validate_source_register(
            self.root,
            today=date(2026, 7, 17),
        )
        self.assertTrue(any(finding.level == "WARNING" for finding in findings))


if __name__ == "__main__":
    unittest.main()
