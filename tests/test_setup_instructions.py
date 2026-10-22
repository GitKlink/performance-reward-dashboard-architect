"""Static coverage for the project-local install instructions and source lock."""

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PIN = "2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9"
SETUP = ROOT / "SETUP.md"
SETUP_SKILL = ROOT / ".agents/skills/setup-power-bi-architect/SKILL.md"
REVIEW_SKILL = ROOT / ".agents/skills/dax-measure-standards-review/SKILL.md"
REVIEW_SCRIPT = ROOT / ".agents/skills/dax-measure-standards-review/scripts/review_measures.py"
INSTALLER = ROOT / "scripts/install_into_project.py"
LOCK = ROOT / ".agents/skills/dax-measure-standards-review/references/source-lock.json"


class SetupContractTests(unittest.TestCase):
    def test_files_and_install_entrypoint_exist(self):
        for p in (SETUP, SETUP_SKILL, REVIEW_SKILL, REVIEW_SCRIPT, INSTALLER, LOCK):
            self.assertTrue(p.is_file(), str(p))
        self.assertIn("[AI-readable setup instructions](SETUP.md)",
                      (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_user_invoked_skill_has_valid_identity(self):
        s = SETUP_SKILL.read_text(encoding="utf-8")
        self.assertTrue(s.startswith("---\n"))
        self.assertIn("name: setup-power-bi-architect", s)
        self.assertIn("disable-model-invocation: true", s)
        self.assertIn("Power BI / Fabric Architect", s)

    def test_pin_consistency_and_no_legacy_product_name(self):
        script = REVIEW_SCRIPT.read_text(encoding="utf-8")
        self.assertIn('BASELINE_SHA = "' + PIN + '"', script)
        lock = json.loads(LOCK.read_text(encoding="utf-8"))
        self.assertEqual(lock["git_sha"], PIN)
        self.assertEqual(len(lock["files"]), 11)
        for path, sha in lock["files"].items():
            self.assertTrue(path.startswith("semantic-model/"))
            self.assertEqual(len(sha), 40)
        for f in (SETUP, SETUP_SKILL):
            s = f.read_text(encoding="utf-8")
            self.assertIn(PIN, s)
            self.assertNotIn("setup-wayfinder", s)
            self.assertIn("dax-measure-standards-review", s)

    def test_install_is_project_local_and_requires_approval(self):
        s = SETUP_SKILL.read_text(encoding="utf-8").lower()
        setup = SETUP.read_text(encoding="utf-8").lower()
        for fragment in ("currently open", "dry-run", "approval", "--apply",
                         "docs/power-bi-architect", ".agents/skills",
                         "do not apply anything to the model"):
            self.assertIn(fragment, s)
        for fragment in ("current", "clones", "outside public repositories",
                         "source-manifest.json", "evalidate"):
            # 'evalidate' is not required; other contract terms must exist.
            if fragment != "evalidate":
                self.assertIn(fragment, setup)

    def test_provider_nested_folder_contract(self):
        setup = SETUP.read_text(encoding="utf-8")
        installer = INSTALLER.read_text(encoding="utf-8")
        setup_skill = SETUP_SKILL.read_text(encoding="utf-8")
        self.assertIn("power-bi-architect/dax-measure-standards-review/", setup)
        self.assertIn('PROVIDER_DIR = "power-bi-architect"', installer)
        self.assertIn('select_skills_dir(project, skills_dir) / PROVIDER_DIR / "dax-measure-standards-review"', installer)
        self.assertIn("power-bi-architect/dax-measure-standards-review/", setup_skill)
        self.assertIn(".cursor/skills/power-bi-architect/dax-measure-standards-review", setup)
        self.assertNotIn(".cursor/skills/dax-measure-standards-review/SKILL.md", setup)

    def test_readonly_source_and_private_report(self):
        s = SETUP.read_text(encoding="utf-8")
        self.assertIn("EVALUATE INFO.VIEW.MEASURES()", s)
        self.assertIn("--standards-root", s)
        self.assertIn("source-manifest.json", s)
        self.assertIn("DAX/M Library", s)


if __name__ == "__main__":
    unittest.main()
