"""Project-local update tests using synthetic installed files and mock source packages."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/update_project.py"
spec = importlib.util.spec_from_file_location("architect_update", SCRIPT)
import sys
sys.path.insert(0, str(SCRIPT.parent))
updater = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updater)

SKILL_ROOT = Path(".cursor/skills/power-bi-architect/dax-measure-standards-review")
DOCS = Path("docs/power-bi-architect")
STANDARDS = DOCS / "standards/semantic-model/README.md"
README = SKILL_ROOT / "README.md"
OLD = SKILL_ROOT / "references/obsolete.md"
NEW = SKILL_ROOT / "references/new-guide.md"
MANIFEST = DOCS / "installation.json"


def manifest(assets, architect_sha):
    return {
        "schema_version": updater.INSTALL_SCHEMA,
        "architect_repo": "GitKlink/performance-reward-dashboard-architect",
        "architect_git_sha": architect_sha,
        "standards_repo": "GitKlink/power-bi-fabric-standards",
        "standards_git_sha": "2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9",
        "capabilities": ["dax-measure-standards-review"],
        "skills_dir": ".cursor/skills",
        "skills_provider": "power-bi-architect",
        "installed_assets_sha256": {
            p.as_posix(): updater.sha256(data) for p, data in assets.items()
        },
    }


def dump(value):
    return (json.dumps(value, indent=2) + "\n").encode()


class ProjectUpdateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project = Path(self.tmp.name) / "eoy-dashboard"
        self.project.mkdir()
        self.previous = {README: b"old README\n", OLD: b"old guide\n",
                         STANDARDS: b"approved standards\n"}
        self.next = {README: b"updated README\n", NEW: b"new guide\n",
                     STANDARDS: b"approved standards\n"}
        old_manifest = manifest(self.previous, "a" * 40)
        next_manifest = manifest(self.next, "b" * 40)
        for p, data in self.previous.items():
            dest = self.project / p
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
        (self.project / MANIFEST).parent.mkdir(parents=True, exist_ok=True)
        (self.project / MANIFEST).write_bytes(dump(old_manifest))
        self.new_payload = {**self.next, MANIFEST: dump(next_manifest)}
        self.new_record = next_manifest
        unrelated = self.project / ".cursor/skills/matt-pocock/research/SKILL.md"
        unrelated.parent.mkdir(parents=True)
        unrelated.write_text("untouched", encoding="utf-8")
        (self.project / "AGENTS.md").write_text("unchanged", encoding="utf-8")
        self.source = Path(self.tmp.name) / "standards-clone"

    def plan(self):
        with patch.object(updater, "build_files", return_value=(self.new_payload, self.new_record)):
            return updater.make_plan(self.project, self.source)

    def test_plan_lists_changes_without_touching_project(self):
        p, payload, prior = self.plan()
        self.assertEqual(p["count"], {"add": 1, "replace": 1, "remove": 1})
        self.assertTrue(p["manifest_update"])
        self.assertEqual(len(p["plan_id"]), 64)
        self.assertEqual(p["old_architect_sha"], "a" * 40)
        self.assertEqual(p["new_architect_sha"], "b" * 40)
        self.assertEqual((self.project / README).read_bytes(), b"old README\n")
        self.assertFalse((self.project / NEW).exists())

    def test_apply_changes_only_owned_files_and_restores_idempotence(self):
        p, payload, previous = self.plan()
        result = updater.apply_plan(self.project, p, payload, previous)
        self.assertIn("UPDATED", result)
        self.assertEqual((self.project / README).read_bytes(), b"updated README\n")
        self.assertEqual((self.project / NEW).read_bytes(), b"new guide\n")
        self.assertFalse((self.project / OLD).exists())
        self.assertEqual((self.project / ".cursor/skills/matt-pocock/research/SKILL.md").read_text(), "untouched")
        self.assertEqual((self.project / "AGENTS.md").read_text(), "unchanged")
        p2, files2, prev2 = self.plan()
        self.assertEqual(p2["count"], {"add": 0, "replace": 0, "remove": 0})
        self.assertFalse(p2["manifest_update"])
        self.assertIn("UP TO DATE", updater.apply_plan(self.project, p2, files2, prev2))

    def test_edited_managed_file_blocks_before_writes(self):
        (self.project / README).write_bytes(b"local modification")
        with self.assertRaisesRegex(updater.InstallError, "Project-local modifications"):
            self.plan()
        self.assertFalse((self.project / NEW).exists())

    def test_new_path_collision_blocks(self):
        f = self.project / NEW
        f.write_text("project-owned custom documentation", encoding="utf-8")
        with self.assertRaisesRegex(updater.InstallError, "project-owned file"):
            self.plan()
        self.assertEqual(f.read_text(), "project-owned custom documentation")

    def test_plan_drift_changes_id(self):
        before, _, _ = self.plan()
        self.new_payload[README] = b"newer README than first approved plan"
        after, _, _ = self.plan()
        self.assertNotEqual(before["plan_id"], after["plan_id"])

    def test_malicious_manifest_path_blocked(self):
        m = json.loads((self.project / MANIFEST).read_text())
        m["installed_assets_sha256"]["../../escape"] = "0" * 64
        (self.project / MANIFEST).write_bytes(dump(m))
        with self.assertRaisesRegex(updater.InstallError, "Unsafe|ownership"):
            self.plan()

    def test_provider_root_cannot_be_switched(self):
        with patch.object(updater, "build_files", return_value=(self.new_payload, self.new_record)):
            with self.assertRaisesRegex(updater.InstallError, "Cannot silently relocate"):
                updater.make_plan(self.project, self.source, ".agents/skills")

    def test_rollback_after_mid_apply_failure(self):
        p, payload, previous = self.plan()
        real_replace = updater.os.replace
        calls = [0]

        def fail_once(src, dst):
            calls[0] += 1
            if calls[0] == 2:
                raise OSError("simulated write failure")
            return real_replace(src, dst)

        with patch.object(updater.os, "replace", side_effect=fail_once):
            with self.assertRaisesRegex(OSError, "simulated"):
                updater.apply_plan(self.project, p, payload, previous)
        self.assertEqual((self.project / README).read_bytes(), b"old README\n")
        self.assertTrue((self.project / OLD).is_file())
        self.assertFalse((self.project / NEW).exists())
        self.assertEqual(json.loads((self.project / MANIFEST).read_text())["architect_git_sha"], "a" * 40)
        self.assertFalse(list(self.project.rglob(".architect-update-*")))
        self.assertFalse(list(self.project.rglob(".architect-rollback-*")))

    def test_missing_manifest_blocks(self):
        (self.project / MANIFEST).unlink()
        with self.assertRaisesRegex(updater.InstallError, "required"):
            self.plan()

    def test_noop_source_version_only_records_source_commit(self):
        same = self.previous.copy()
        manifest_only = manifest(same, "b" * 40)
        with patch.object(updater, "build_files", return_value=(
            {**same, MANIFEST: dump(manifest_only)}, manifest_only
        )):
            p, files, previous = updater.make_plan(self.project, self.source)
        self.assertEqual(p["count"], {"add": 0, "replace": 0, "remove": 0})
        self.assertTrue(p["manifest_update"])
        updater.apply_plan(self.project, p, files, previous)
        self.assertEqual(json.loads((self.project / MANIFEST).read_text())["architect_git_sha"], "b" * 40)


if __name__ == "__main__":
    unittest.main()
