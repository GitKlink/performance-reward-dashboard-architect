#!/usr/bin/env python3
"""Read-only CSV measure metadata review; partial checks pinned to a standards revision."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASELINE_SHA = "2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9"
SOURCE_REPO = "GitKlink/power-bi-fabric-standards"
SOURCE_FILES = [
    "semantic-model/README.md",
    "semantic-model/semantic_measure_standard.md",
    "semantic-model/business_glossary.md",
]
DOMAIN_FILES = {
    "workforce": "semantic_measure_standard_workforce.md",
    "organisation": "semantic_measure_standard_organisation.md",
    "performance": "semantic_measure_standard_performance.md",
    "fixed_reward": "semantic_measure_standard_fixed_reward.md",
    "variable_reward": "semantic_measure_standard_variable_reward.md",
    "equity": "semantic_measure_standard_equity.md",
    "international_assignments": "semantic_measure_standard_international_assignments.md",
}
ALIASES = {
    "name": ("name", "measurename", "measure"),
    "table": ("table", "hometable", "tablename"),
    "description": ("description",),
    "format": ("formatstring", "format"),
    "dynamic_format": ("formatstringdefinition", "dynamicformatstring"),
    "folder": ("displayfolder", "folder"),
    "hidden": ("ishidden", "hidden"),
    "expression": ("expression", "daxformula", "dax"),
    "state": ("state",),
}


class ReviewError(Exception):
    """Invalid input or unverified source."""


def git(root: Path, *args: str) -> str:
    try:
        result = subprocess.run(["git", "-C", str(root), *args],
                                capture_output=True, text=True, check=False)
    except FileNotFoundError as exc:
        raise ReviewError("Git is not installed or not available on PATH.") from exc
    if result.returncode:
        raise ReviewError("Cannot verify local standards Git checkout and revisions.")
    return result.stdout.strip()


def verify_source(root: Path, domain: str | None) -> dict:
    root = root.resolve()
    if not root.is_dir():
        raise ReviewError("Standards directory does not exist. Clone the private repository.")
    if Path(git(root, "rev-parse", "--show-toplevel")).resolve() != root:
        raise ReviewError("Provide the standards repository root, not a nested folder.")
    actual = git(root, "rev-parse", "HEAD")
    if actual != BASELINE_SHA:
        raise ReviewError("Standards SHA mismatch: expected " + BASELINE_SHA + ", got " + actual)
    origin = git(root, "remote", "get-url", "origin").lower()
    if not re.search(r"(^|[:/])gitklink/power-bi-fabric-standards(?:\.git)?$", origin):
        raise ReviewError("Git origin does not match the canonical standards repository.")
    if git(root, "status", "--porcelain", "--", "semantic-model"):
        raise ReviewError("Standards checkout has modified or untracked semantic-model files.")
    paths = list(SOURCE_FILES)
    if domain:
        paths.append("semantic-model/domains/" + DOMAIN_FILES[domain])
    digests = {}
    for rel in paths:
        source = root / rel
        if not source.is_file() or source.is_symlink():
            raise ReviewError("Canonical standard missing or symlinked: " + rel)
        if git(root, "hash-object", "--", rel) != git(root, "rev-parse", "HEAD:" + rel):
            raise ReviewError("Canonical document does not match the pinned Git blob: " + rel)
        digests[rel] = hashlib.sha256(source.read_bytes()).hexdigest()
    return {"repo": SOURCE_REPO, "git_sha": actual, "files_sha256": digests}


def column_key(s: str) -> str:
    s = s.lstrip("\ufeff").strip()
    m = re.search(r"\[([^\]]+)\]$", s)
    if m:
        s = m.group(1)
    return re.sub(r"[^a-z0-9]", "", s.casefold())


def read_csv(path: Path) -> tuple[list[dict], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ReviewError("The CSV has no header.")
        keys = [column_key(s) for s in reader.fieldnames]
        found = {}
        for field, variants in ALIASES.items():
            hits = [i for i, value in enumerate(keys) if value in variants]
            if len(hits) > 1:
                raise ReviewError("Duplicate or ambiguous column: " + field)
            if hits:
                found[field] = reader.fieldnames[hits[0]]
        if "name" not in found:
            raise ReviewError("A Name column is required (INFO.VIEW.MEASURES export).")
        rows = []
        for n, original in enumerate(reader, 2):
            if None in original:
                raise ReviewError("Unexpected extra CSV fields at row " + str(n))
            row = {k: original.get(v) or "" for k, v in found.items()}
            row["csv_row"] = n
            if not row["name"].strip():
                raise ReviewError("Missing Name at CSV row " + str(n))
            rows.append(row)
        if not rows:
            raise ReviewError("CSV has no measure rows.")
    return rows, sorted(set(ALIASES) - set(found))


def hidden_value(s: str) -> bool | None:
    s = s.strip().casefold()
    if s in ("true", "1", "yes"):
        return True
    if s in ("false", "0", "no"):
        return False
    return None


def review(rows: list[dict], missing: list[str]) -> dict:
    findings = []
    missing = set(missing)

    def add(row: dict, rule: str, level: str, reason: str, action: str):
        findings.append({
            "csv_row": row["csv_row"], "table": row.get("table", ""),
            "name": row["name"], "rule_id": rule, "severity": level,
            "finding": reason, "review_action": action,
        })

    for row in rows:
        name = row["name"]
        hidden = hidden_value(row.get("hidden", "")) if "hidden" not in missing else None
        visible = hidden is False
        if len(name) > 50:
            add(row, "SM-NAME-050", "error", "Exceeds hard maximum of 50 characters.",
                "Find shorter unambiguous name; exception requires approval.")
        elif len(name) > 40:
            add(row, "SM-NAME-040", "warning", "Exceeds 40-character soft maximum.",
                "Review discoverability and record justification or shorten.")
        elif len(name) > 30:
            add(row, "SM-NAME-030", "info", "Exceeds the 30-character naming target.",
                "Review only; 30 characters is a target, not a hard rule.")
        if name != name.strip():
            add(row, "SM-NAME-SPACE", "warning", "Leading/trailing whitespace.",
                "Review a whitespace-only rename.")
        if visible and re.match(r"^(M_|Calc_|KPI_|Helper_)", name, flags=re.I):
            add(row, "SM-NAME-PREFIX", "warning", "Visible business measure has developer prefix.",
                "Check intended measure class; choose business-first name.")
        if visible and "_" in name:
            add(row, "SM-NAME-UNDERSCORE", "warning", "Visible measure name has underscore.",
                "Prefer readable approved business wording.")
        if "%" in name and not name.endswith(" %"):
            add(row, "SM-NAME-PERCENT", "warning", "Percent sign is not terminal ' %'.",
                "Confirm percentage semantics; review suffix.")
        if "hidden" not in missing and hidden is None:
            add(row, "EXP-HIDDEN-UNKNOWN", "info", "Unrecognised IsHidden value.",
                "Export True/False; visibility-sensitive checks skipped.")
        if visible:
            if "description" not in missing and not row.get("description", "").strip():
                add(row, "SM-DESC-MISSING", "error", "Visible measure has no description.",
                    "Document definition, population, calculation and relevant context.")
            if ("format" not in missing or "dynamic_format" not in missing) and (
                not row.get("format", "").strip() and
                not row.get("dynamic_format", "").strip()
            ):
                add(row, "SM-FORMAT-MISSING", "error", "No format or dynamic-format metadata.",
                    "Verify intentional static/dynamic formatting in model.")
        if visible and (name.casefold().startswith("deprecated ") or
                        row.get("description", "").strip().upper().startswith("DEPRECATED.")):
            add(row, "SM-DEPRECATED-VISIBLE", "warning", "Deprecated measure is visible.",
                "Review hidden state, replacement and technical folder.")
        if "folder" not in missing:
            for group in row.get("folder", "").split(";"):
                levels = [x.strip() for x in re.split(r"[/\\]", group) if x.strip()]
                if len(levels) > 2 and levels[0].casefold() != "_technical":
                    add(row, "SM-FOLDER-DEPTH", "warning",
                        "Business display folder is deeper than two levels.",
                        "Review whether hierarchy is necessary.")
                    break

    counts = Counter(row["name"].strip().casefold() for row in rows)
    for row in rows:
        if counts[row["name"].strip().casefold()] > 1:
            add(row, "SM-DUPLICATE-NAME", "error", "Duplicate measure name in CSV.",
                "Investigate collision and dependencies; no automated rename.")

    findings.sort(key=lambda f: (f["csv_row"], f["rule_id"]))
    severity = Counter(f["severity"] for f in findings)
    omitted = [
        "Business glossary approval, root-first concept clustering, Change vs Variance and domain semantics require human review.",
        "DAX parsing, dependency analysis, semantic model compilation and numeric reconciliation not performed.",
        "Fact-table grain/row-count coverage, synonyms and remaining standard clauses not checked.",
    ]
    if "hidden" in missing:
        omitted.append("IsHidden absent: visibility-dependent checks skipped.")
    if "description" in missing:
        omitted.append("Description absent: description completeness skipped.")
    if "format" in missing and "dynamic_format" in missing:
        omitted.append("Format columns absent: formatting completeness skipped.")
    if "folder" in missing:
        omitted.append("DisplayFolder absent: folder hierarchy checks skipped.")
    return {
        "measures": len(rows), "findings": findings,
        "severity": {k: severity.get(k, 0) for k in ("error", "warning", "info")},
        "missing_columns": sorted(missing), "not_evaluated": omitted,
    }


def markdown(result: dict) -> str:
    def cell(s):
        return str(s).replace("|", "\\|").replace("\r", " ").replace("\n", " ")
    lines = [
        "# Read-only DAX Measure Standards Review",
        "",
        "**PARTIAL REVIEW ONLY — not a full conformance certification.**",
        "",
        "- Measures: " + str(result["measures"]),
        "- Findings: " + ", ".join(k + "=" + str(v) for k, v in result["severity"].items()),
        "- Standards revision: " + result["standards"]["git_sha"],
        "- Domain: " + (result["domain"] or "none"),
        "- Input SHA-256: " + result["input_sha256"],
        "",
        "## Findings", "",
        "| Row | Table | Measure | Rule | Severity | Finding | Review action |",
        "|---:|---|---|---|---|---|---|",
    ]
    for f in result["findings"]:
        lines.append("| " + " | ".join(cell(f[k]) for k in (
            "csv_row", "table", "name", "rule_id", "severity",
            "finding", "review_action")) + " |")
    if not result["findings"]:
        lines.append("| — | — | — | — | — | No findings for implemented rules | — |")
    lines += ["", "## Not evaluated", ""]
    lines += ["- " + x for x in result["not_evaluated"]]
    lines += ["", "## Canonical source file hashes", "",
              "| File | SHA-256 |", "|---|---|"]
    lines += ["| " + k + " | " + v + " |"
              for k, v in result["standards"]["files_sha256"].items()]
    lines += ["", "No model, input export or canonical standard was modified.", ""]
    return "\n".join(lines)


def run(args: argparse.Namespace) -> dict:
    source = args.input.resolve(strict=True)
    out = args.out_dir.resolve()
    root = args.standards_root.resolve()
    if not source.is_file():
        raise ReviewError("Input must be a file.")
    if out == root or root in out.parents:
        raise ReviewError("Do not write reports inside the canonical standards repository.")
    if out == source.parent or out in source.parents:
        raise ReviewError("Use a separate output directory outside the CSV input parent.")
    standards = verify_source(root, args.domain)
    rows, missing = read_csv(source)
    result = review(rows, missing)
    result.update({
        "schema_version": "wayfinder-dax-measure-review-v0",
        "status": "partial_review_only",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "domain": args.domain, "input_filename": source.name,
        "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "standards": standards,
    })
    out.mkdir(parents=True, exist_ok=True)
    (out / "review.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "review.md").write_text(markdown(result), encoding="utf-8")
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="UTF-8 CSV measure inventory")
    parser.add_argument("--standards-root", type=Path, required=True, help="Private standards Git clone")
    parser.add_argument("--domain", choices=sorted(DOMAIN_FILES))
    parser.add_argument("--out-dir", type=Path, required=True, help="Private/local report directory")
    args = parser.parse_args(argv)
    try:
        result = run(args)
    except (ReviewError, OSError, UnicodeError) as error:
        print("REVIEW BLOCKED: " + str(error), file=sys.stderr)
        return 2
    print("Partial review: " + str(result["measures"]) + " measures, " +
          str(len(result["findings"])) + " findings. No source/model edits.")
    print("Reports in " + str(args.out_dir.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
