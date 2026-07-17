#!/usr/bin/env python3
"""Validate Markdown templates and their schema declarations.

The validator checks frontmatter, template IDs, schema links and versions,
filename alignment, duplicate IDs, placeholder safety, and schema coverage. It is
read-only.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Run `python3 -m pip install -r requirements-dev.txt`."
    ) from exc


TEMPLATE_ID_PATTERN = re.compile(r"^TPL-[A-Z]+-[0-9]{3}$")
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
ACTIVE_STATUSES = {"DRAFT", "IN REVIEW", "APPROVED", "SUPERSEDED"}


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


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    try:
        closing = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError(f"unterminated YAML frontmatter in {path}") from exc

    try:
        result = yaml.safe_load("\n".join(lines[1:closing])) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter in {path}: {exc}") from exc

    if not isinstance(result, dict):
        raise ValueError(f"frontmatter in {path} must be a mapping")
    return result


def template_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in (root / "templates").glob("*.md")
        if path.name != "README.md"
    )


def schema_version(path: Path) -> str | None:
    payload = load_yaml(path)
    if not isinstance(payload, dict):
        return None
    repository = payload.get("x-repository")
    if not isinstance(repository, dict):
        return None
    value = repository.get("schema_version")
    return value if isinstance(value, str) else None


def validate_repository(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    paths = template_files(root)
    if not paths:
        return [Finding("ERROR", "no Markdown templates found under templates/")]

    ids: dict[str, Path] = {}
    active_subjects: set[str] = set()

    for path in paths:
        relative = path.relative_to(root)
        try:
            frontmatter = parse_frontmatter(path)
        except ValueError as exc:
            findings.append(Finding("ERROR", str(exc)))
            continue

        if frontmatter is None:
            findings.append(Finding("ERROR", f"{relative} has no YAML frontmatter"))
            continue

        status = frontmatter.get("status")
        if status == "PLACEHOLDER":
            text = path.read_text(encoding="utf-8").lower()
            if "placeholder" not in text:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{relative} is PLACEHOLDER but does not explain placeholder status",
                    )
                )
            continue

        if status not in ACTIVE_STATUSES:
            findings.append(
                Finding("ERROR", f"{relative} has unsupported status {status!r}")
            )
            continue

        required = {
            "template_id",
            "status",
            "content_version",
            "schema",
            "schema_version",
            "last_reviewed",
        }
        missing = sorted(required - frontmatter.keys())
        if missing:
            findings.append(
                Finding(
                    "ERROR",
                    f"{relative} frontmatter missing: {', '.join(missing)}",
                )
            )
            continue

        template_id = frontmatter["template_id"]
        if not isinstance(template_id, str) or not TEMPLATE_ID_PATTERN.fullmatch(
            template_id
        ):
            findings.append(Finding("ERROR", f"{relative} has invalid template_id"))
        elif template_id in ids:
            findings.append(
                Finding(
                    "ERROR",
                    f"duplicate template_id {template_id} in {relative} and "
                    f"{ids[template_id].relative_to(root)}",
                )
            )
        else:
            ids[template_id] = path

        for field in ("content_version", "schema_version"):
            value = frontmatter[field]
            if not isinstance(value, str) or not VERSION_PATTERN.fullmatch(value):
                findings.append(
                    Finding("ERROR", f"{relative} has invalid {field} {value!r}")
                )

        schema_reference = frontmatter["schema"]
        if not isinstance(schema_reference, str) or not schema_reference:
            findings.append(Finding("ERROR", f"{relative} has invalid schema path"))
            continue

        resolved_schema = (path.parent / schema_reference).resolve()
        try:
            resolved_schema.relative_to(root.resolve())
        except ValueError:
            findings.append(
                Finding("ERROR", f"{relative} schema path escapes repository root")
            )
            continue

        if not resolved_schema.exists():
            findings.append(
                Finding(
                    "ERROR",
                    f"{relative} references missing schema {schema_reference}",
                )
            )
            continue

        subject = path.name.removesuffix(".md")
        expected_schema_name = f"{subject}.schema.yaml"
        if resolved_schema.name != expected_schema_name:
            findings.append(
                Finding(
                    "ERROR",
                    f"{relative} should map to {expected_schema_name}, not "
                    f"{resolved_schema.name}",
                )
            )
        else:
            active_subjects.add(subject)

        try:
            declared_schema_version = schema_version(resolved_schema)
        except ValueError as exc:
            findings.append(Finding("ERROR", str(exc)))
            continue

        if declared_schema_version != frontmatter["schema_version"]:
            findings.append(
                Finding(
                    "ERROR",
                    f"{relative} schema_version {frontmatter['schema_version']!r} "
                    f"does not match schema {declared_schema_version!r}",
                )
            )

        text = path.read_text(encoding="utf-8")
        if not re.search(r"^#\s+\S", text, re.MULTILINE):
            findings.append(Finding("ERROR", f"{relative} has no level-one heading"))

    schema_subjects = {
        path.name.removesuffix(".schema.yaml")
        for path in (root / "schemas").glob("*.schema.yaml")
    }
    missing_templates = sorted(schema_subjects - active_subjects)
    if missing_templates:
        findings.append(
            Finding(
                "ERROR",
                "schemas without active matching templates: "
                + ", ".join(missing_templates),
            )
        )

    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root containing templates/ and schemas/",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="return exit code 2 when warnings are present",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    findings = validate_repository(args.root.resolve())
    errors = [finding for finding in findings if finding.level == "ERROR"]
    warnings = [finding for finding in findings if finding.level == "WARNING"]

    for finding in findings:
        print(finding.render())

    if errors:
        print(f"\nTemplate validation failed with {len(errors)} error(s).")
        return 1
    if warnings and args.warnings_as_errors:
        print(f"\nTemplate validation failed with {len(warnings)} warning(s).")
        return 2

    if warnings:
        print(f"\nTemplate validation passed with {len(warnings)} warning(s).")
    else:
        print("Template validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
