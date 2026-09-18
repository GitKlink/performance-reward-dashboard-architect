#!/usr/bin/env python3
"""Validate the central source register and local central-source references."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Run `python -m pip install -r requirements-dev.txt`."
    ) from exc


SOURCE_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ARTIFACT_ID_PATTERN = re.compile(r"^[A-Z]+-[A-Z]+-[0-9]{3}$")
CENTRAL_SOURCE_REFERENCE = re.compile(r"Central source ID:\s*`([^`]+)`")

REQUIRED_FIELDS = {
    "source_id",
    "title",
    "author_or_organisation",
    "source_type",
    "evidence_level",
    "url_or_doi",
    "publication_date",
    "updated_date",
    "retrieved_date",
    "version",
    "jurisdiction",
    "lifecycle_state",
    "licence_or_usage_notes",
    "relevant_artifacts",
    "relevant_claims",
    "review_notes",
}

EVIDENCE_LEVELS = {
    "primary-authoritative",
    "authoritative-synthesis",
    "practitioner-evidence",
    "discovery-only",
}
LIFECYCLE_STATES = {"candidate", "accepted", "restricted", "stale", "rejected"}
CURRENT_PRODUCT_TYPES = {
    "official-product-documentation",
    "official-release-note",
    "official-product-guidance",
}


@dataclass(frozen=True)
class Finding:
    level: str
    message: str

    def render(self) -> str:
        return f"{self.level}: {self.message}"


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML in {path}: {exc}") from exc


def parse_date(value: Any, *, full: bool) -> date | None:
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, int):
        value = str(value)
    if not isinstance(value, str):
        raise ValueError(f"date value must be a string, year, or null: {value!r}")

    formats = ["%Y-%m-%d"] if full else ["%Y-%m-%d", "%Y-%m", "%Y"]
    for format_string in formats:
        try:
            return datetime.strptime(value, format_string).date()
        except ValueError:
            continue
    requirement = "YYYY-MM-DD" if full else "YYYY, YYYY-MM, or YYYY-MM-DD"
    raise ValueError(f"invalid date {value!r}; expected {requirement}")


def validate_url(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def artifact_ids(root: Path) -> set[str]:
    register_path = root / "ARTIFACT-REGISTER.yaml"
    payload = load_yaml(register_path)
    artifacts = payload.get("artifacts", []) if isinstance(payload, dict) else []
    return {
        artifact["artifact_id"]
        for artifact in artifacts
        if isinstance(artifact, dict) and isinstance(artifact.get("artifact_id"), str)
    }


def validate_source_register(root: Path, today: date | None = None) -> list[Finding]:
    findings: list[Finding] = []
    today = today or date.today()
    path = root / "knowledge/research-register/sources.yaml"
    if not path.exists():
        return [Finding("ERROR", f"missing source register: {path}")]

    try:
        payload = load_yaml(path)
    except ValueError as exc:
        return [Finding("ERROR", str(exc))]

    sources = payload.get("sources") if isinstance(payload, dict) else None
    if not isinstance(sources, list):
        return [Finding("ERROR", "source register must contain a `sources` list")]

    known_artifacts = artifact_ids(root)
    by_id: dict[str, dict[str, Any]] = {}
    urls: dict[str, str] = {}

    for index, source in enumerate(sources, start=1):
        prefix = f"source entry {index}"
        if not isinstance(source, dict):
            findings.append(Finding("ERROR", f"{prefix} must be a mapping"))
            continue

        missing = sorted(REQUIRED_FIELDS - source.keys())
        if missing:
            findings.append(
                Finding("ERROR", f"{prefix} missing fields: {', '.join(missing)}")
            )
            continue

        source_id = source["source_id"]
        if not isinstance(source_id, str) or not SOURCE_ID_PATTERN.fullmatch(source_id):
            findings.append(Finding("ERROR", f"{prefix} has invalid source_id"))
            continue
        if source_id in by_id:
            findings.append(Finding("ERROR", f"duplicate source_id {source_id}"))
        else:
            by_id[source_id] = source

        url = source["url_or_doi"]
        if not validate_url(url):
            findings.append(Finding("ERROR", f"{source_id} has invalid HTTPS URL"))
        elif url in urls:
            findings.append(
                Finding(
                    "WARNING",
                    f"{source_id} and {urls[url]} share the same URL; confirm that "
                    "separate version records are required",
                )
            )
        else:
            urls[url] = source_id

        evidence_level = source["evidence_level"]
        if evidence_level not in EVIDENCE_LEVELS:
            findings.append(
                Finding(
                    "ERROR",
                    f"{source_id} has unsupported evidence_level {evidence_level!r}",
                )
            )

        lifecycle_state = source["lifecycle_state"]
        if lifecycle_state not in LIFECYCLE_STATES:
            findings.append(
                Finding(
                    "ERROR",
                    f"{source_id} has unsupported lifecycle_state {lifecycle_state!r}",
                )
            )

        try:
            parse_date(source["publication_date"], full=False)
            parse_date(source["updated_date"], full=False)
            retrieved = parse_date(source["retrieved_date"], full=True)
        except ValueError as exc:
            findings.append(Finding("ERROR", f"{source_id}: {exc}"))
            retrieved = None

        if retrieved and retrieved > today:
            findings.append(
                Finding("ERROR", f"{source_id} retrieved_date is in the future")
            )

        if (
            retrieved
            and source["source_type"] in CURRENT_PRODUCT_TYPES
            and (today - retrieved).days > 30
            and lifecycle_state == "accepted"
        ):
            findings.append(
                Finding(
                    "WARNING",
                    f"{source_id} is current-product evidence retrieved more than "
                    "30 days ago",
                )
            )

        for field in (
            "title",
            "author_or_organisation",
            "source_type",
            "version",
            "jurisdiction",
            "licence_or_usage_notes",
            "review_notes",
        ):
            if not isinstance(source[field], str) or not source[field].strip():
                findings.append(
                    Finding("ERROR", f"{source_id} field {field} must be non-empty")
                )

        relevant_claims = source["relevant_claims"]
        if not isinstance(relevant_claims, list) or not relevant_claims:
            findings.append(
                Finding("ERROR", f"{source_id} must contain relevant_claims")
            )
        elif any(not isinstance(claim, str) or not claim.strip() for claim in relevant_claims):
            findings.append(
                Finding("ERROR", f"{source_id} contains an invalid relevant claim")
            )

        relevant_artifacts = source["relevant_artifacts"]
        if not isinstance(relevant_artifacts, list) or not relevant_artifacts:
            findings.append(
                Finding("ERROR", f"{source_id} must contain relevant_artifacts")
            )
        else:
            for reference in relevant_artifacts:
                if not isinstance(reference, str) or not reference.strip():
                    findings.append(
                        Finding(
                            "ERROR",
                            f"{source_id} contains an invalid relevant artifact",
                        )
                    )
                elif ARTIFACT_ID_PATTERN.fullmatch(reference):
                    if reference not in known_artifacts:
                        findings.append(
                            Finding(
                                "ERROR",
                                f"{source_id} references unregistered artifact {reference}",
                            )
                        )
                else:
                    findings.append(
                        Finding(
                            "WARNING",
                            f"{source_id} uses a legacy descriptive relevant_artifact "
                            f"reference: {reference!r}",
                        )
                    )

    trial_root = root / "knowledge/research-register"
    for markdown_path in trial_root.rglob("*.md"):
        text = markdown_path.read_text(encoding="utf-8")
        for match in CENTRAL_SOURCE_REFERENCE.finditer(text):
            source_id = match.group(1)
            if source_id not in by_id:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{markdown_path.relative_to(root)} references unknown central "
                        f"source ID {source_id}",
                    )
                )

    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root containing the source register",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="return exit code 2 when warnings are present",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    findings = validate_source_register(args.root.resolve())
    errors = [finding for finding in findings if finding.level == "ERROR"]
    warnings = [finding for finding in findings if finding.level == "WARNING"]

    for finding in findings:
        print(finding.render())

    if errors:
        print(f"\nSource-register validation failed with {len(errors)} error(s).")
        return 1
    if warnings and args.warnings_as_errors:
        print(f"\nSource-register validation failed with {len(warnings)} warning(s).")
        return 2

    if warnings:
        print(f"\nSource-register validation passed with {len(warnings)} warning(s).")
    else:
        print("Source-register validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
