"""Static guardrails for an instruction-driven setup; no AI runtime is simulated."""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PIN = "2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9"
SETUP = ROOT / "SETUP.md"
SETUP_SKILL = ROOT / ".agents/skills/setup-power-bi-architect/SKILL.md"
REVIEW_SKILL = ROOT / ".agents/skills/dax-measure-standards-review/SKILL.md"
REVIEW_SCRIPT = ROOT / ".agents/skills/dax-measure-standards-review/scripts/review_measures.py"


class SetupContractTests(unittest.TestCase):
    def test_files_and_install_entrypoint_exist(self):
        for p in (SETUP, SETUP_SKILL, REVIEW_SKILL, REVIEW_SCRIPT):
            self.assertTrue(p.is_file(), str(p))
        self.assertIn("[AI-readable setup instructions](SETUP.md)", (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_user_invoked_skill_has_valid_identity(self):
        skill = SETUP_SKILL.read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertIn("name: setup-power-bi-architect", skill)
        self.assertIn("disable-model-invocation: true", skill)
        self.assertIn("Power BI / Fabric Architect", skill)

    def test_pin_consistency_and_no_legacy_product_name(self):
        script = REVIEW_SCRIPT.read_text(encoding="utf-8")
        self.assertIn('BASELINE_SHA = "' + PIN + '"', script)
        for f in (SETUP, SETUP_SKILL):
            contents = f.read_text(encoding="utf-8")
            self.assertIn(PIN, contents)
            self.assertNotIn("setup-wayfinder", contents)
            self.assertNotIn("Wayfinder Architect", contents)
            self.assertIn("dax-measure-standards-review", contents)

    def test_approval_safety_and_distinct_validation_gates(self):
        skill = SETUP_SKILL.read_text(encoding="utf-8").lower()
        for fragment in (
            "explore", "propose", "approval", "no model", "standards",
            "private", "python -m unittest", "py_compile",
            "schema_version", "partial_review_only", "local cursor",
            "not verified",
        ):
            self.assertIn(fragment, skill)

    def test_review_export_and_private_output_instructions(self):
        setup = SETUP.read_text(encoding="utf-8")
        self.assertIn("EVALUATE INFO.VIEW.MEASURES()", setup)
        self.assertIn("outside public repositories", setup)
        self.assertIn("DAX/M Library", setup)


if __name__ == "__main__":
    unittest.main()
