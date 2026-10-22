"""Stdlib-only tests; use synthetic metadata, never a private standards checkout."""
import argparse
import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / ".agents/skills/dax-measure-standards-review/scripts/review_measures.py"
)
spec = importlib.util.spec_from_file_location("measure_review", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def record(name="Headcount", table="Workforce Measures", description="Count of employees",
           fmt="#,##0", hidden="False", folder="Workforce", dynamic=""):
    return {
        "csv_row": 2, "name": name, "table": table, "description": description,
        "format": fmt, "hidden": hidden, "folder": folder,
        "dynamic_format": dynamic, "expression": "COUNTROWS ( 'Employees' )",
    }


class RulesTests(unittest.TestCase):
    def rules(self, rows, missing=None):
        return mod.review(rows, missing or [])

    def ids(self, report):
        return [f["rule_id"] for f in report["findings"]]

    def test_clean_visible_record(self):
        result = self.rules([record()])
        self.assertEqual(result["measures"], 1)
        self.assertEqual(result["findings"], [])

    def test_explicit_violations(self):
        r = record("M_Reward%", description="", fmt="",
                   folder="Reward\\Outcomes\\By Team")
        ids = self.ids(self.rules([r]))
        for wanted in ["SM-NAME-PREFIX", "SM-NAME-UNDERSCORE",
                       "SM-NAME-PERCENT", "SM-DESC-MISSING",
                       "SM-FORMAT-MISSING", "SM-FOLDER-DEPTH"]:
            self.assertIn(wanted, ids)

    def test_static_or_dynamic_format(self):
        r = record(fmt="", dynamic="SELECTEDMEASUREFORMATSTRING()")
        self.assertNotIn("SM-FORMAT-MISSING", self.ids(self.rules([r])))

    def test_hidden_measure_not_business_visible(self):
        r = record(name="M_Private", description="", fmt="", hidden="True")
        ids = self.ids(self.rules([r]))
        self.assertNotIn("SM-DESC-MISSING", ids)
        self.assertNotIn("SM-NAME-PREFIX", ids)
        self.assertNotIn("SM-FORMAT-MISSING", ids)

    def test_incomplete_csv_does_not_invent_metadata(self):
        r = {"csv_row": 2, "name": "M_Unknown"}
        result = self.rules([r], list(mod.ALIASES.keys() - {"name"}))
        self.assertEqual(result["findings"], [])
        self.assertIn("hidden", result["missing_columns"])
        self.assertTrue(any("skipped" in s for s in result["not_evaluated"]))

    def test_unknown_hidden_does_not_assume_visible(self):
        r = record("M_Unknown", hidden="maybe", description="", fmt="")
        ids = self.ids(self.rules([r]))
        self.assertIn("EXP-HIDDEN-UNKNOWN", ids)
        self.assertNotIn("SM-DESC-MISSING", ids)

    def test_duplicate_names_case_insensitive(self):
        a, b = record(name="Headcount"), record(name="HEADCOUNT")
        b["csv_row"] = 3
        result = self.rules([a, b])
        self.assertEqual(self.ids(result).count("SM-DUPLICATE-NAME"), 2)

    def test_tiers_name_length(self):
        for n, target in [(31, "SM-NAME-030"), (41, "SM-NAME-040"), (51, "SM-NAME-050")]:
            self.assertIn(target, self.ids(self.rules([record(name="X" * n)])))

    def test_deprecated_visible(self):
        r = record(name="Previous Metric", description="DEPRECATED. Use Headcount.")
        self.assertIn("SM-DEPRECATED-VISIBLE", self.ids(self.rules([r])))

    def test_technical_folder_exempt_depth(self):
        r = record(folder="_Technical\\QA\\Deep\\Diagnostics")
        self.assertNotIn("SM-FOLDER-DEPTH", self.ids(self.rules([r])))

    def test_markdown_no_conformance_claim(self):
        result = self.rules([record()])
        result.update({
            "standards": {"git_sha": mod.BASELINE_SHA, "files_sha256": {}},
            "domain": None, "input_sha256": "a" * 64,
        })
        report = mod.markdown(result)
        self.assertIn("PARTIAL REVIEW ONLY", report)
        self.assertIn("Not evaluated", report)


class CsvAndIntegrationTests(unittest.TestCase):
    def test_read_bracket_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "inventory.csv"
            p.write_text("[Name],[IsHidden],[Description],[FormatString]\n"
                         "Headcount,False,Counts employees,\"#,##0\"\n", encoding="utf-8")
            rows, missing = mod.read_csv(p)
            self.assertEqual(rows[0]["name"], "Headcount")
            self.assertNotIn("description", missing)

    def test_reject_ambiguous_name_header(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "bad.csv"
            p.write_text("Name,[Name]\nA,B\n", encoding="utf-8")
            with self.assertRaises(mod.ReviewError):
                mod.read_csv(p)

    def test_reject_blank_name(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "bad.csv"
            p.write_text("Name,Description\n,Blank\n", encoding="utf-8")
            with self.assertRaises(mod.ReviewError):
                mod.read_csv(p)

    def test_missing_standard_revision_is_blocking(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(mod, "git", side_effect=[str(root), "0000000000000000000000000000000000000000"]):
                with self.assertRaisesRegex(mod.ReviewError, "SHA mismatch"):
                    mod.verify_source(root, None)

    def test_wrong_origin_is_blocking(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(mod, "git", side_effect=[
                str(root), mod.BASELINE_SHA, "https://github.com/other/incorrect.git"
            ]):
                with self.assertRaisesRegex(mod.ReviewError, "origin"):
                    mod.verify_source(root, None)

    def test_run_creates_reports_without_editing_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            inp = base / "inventory.csv"
            out = base / "private-out"
            inp.write_text("Name,Table,IsHidden,Description,FormatString,DisplayFolder\n"
                           "Headcount,Workforce,False,Counts employees,\"#,##0\",Workforce\n",
                           encoding="utf-8")
            original = inp.read_bytes()
            args = argparse.Namespace(input=inp, out_dir=out,
                                      standards_root=base / "standards", domain=None)
            fake_source = {"repo": mod.SOURCE_REPO, "git_sha": mod.BASELINE_SHA,
                           "files_sha256": {"semantic-model/README.md": "abc"}}
            with patch.object(mod, "verify_source", return_value=fake_source):
                result = mod.run(args)
            self.assertEqual(inp.read_bytes(), original)
            self.assertEqual(result["findings"], [])
            self.assertTrue((out / "review.md").exists())
            report = json.loads((out / "review.json").read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "partial_review_only")
            self.assertEqual(report["schema_version"], "power-bi-fabric-architect-dax-measure-review-v1")
            self.assertEqual(report["measures"], 1)

    def test_report_cannot_be_written_in_standards(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            inp = base / "input.csv"
            inp.write_text("Name\nHeadcount\n", encoding="utf-8")
            root = base / "standards"
            args = argparse.Namespace(input=inp, out_dir=root / "output",
                                      standards_root=root, domain=None)
            with self.assertRaisesRegex(mod.ReviewError, "canonical standards"):
                mod.run(args)


if __name__ == "__main__":
    unittest.main()
