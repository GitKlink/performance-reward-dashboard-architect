#!/usr/bin/env python3
"""Validate repository-local Markdown links.

External URLs, mail links, and anchor-only links are ignored. The checker is
read-only and skips fenced code blocks to reduce false positives.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:")
IGNORED_DIRECTORIES = {".git", ".venv", "venv", "build", "dist"}


@dataclass(frozen=True)
class LinkFinding:
    source: Path
    line_number: int
    target: str

    def render(self, root: Path) -> str:
        source = self.source.relative_to(root)
        return f"ERROR: {source}:{self.line_number} missing local target {self.target!r}"


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".mdc"}:
            continue
        if any(part in IGNORED_DIRECTORIES for part in path.relative_to(root).parts):
            continue
        files.append(path)
    return sorted(files)


def clean_target(raw_target: str) -> str:
    target = raw_target.strip()

    # Markdown allows an optional title after the URL.
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " \"" in target:
        target = target.split(" \"", 1)[0]
    elif " '" in target:
        target = target.split(" '", 1)[0]

    return unquote(target.strip())


def is_external_or_anchor(target: str) -> bool:
    lowered = target.lower()
    return (
        not target
        or target.startswith("#")
        or lowered.startswith(IGNORED_PREFIXES)
    )


def resolve_local_target(source: Path, root: Path, target: str) -> Path:
    path_part = target.split("#", 1)[0].split("?", 1)[0]
    if path_part.startswith("/"):
        return root / path_part.lstrip("/")
    return source.parent / path_part


def check_file(path: Path, root: Path) -> list[LinkFinding]:
    findings: list[LinkFinding] = []
    in_fence = False
    fence_marker = ""

    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue

        if in_fence:
            continue

        for match in LINK_PATTERN.finditer(line):
            target = clean_target(match.group(1))
            if is_external_or_anchor(target):
                continue

            resolved = resolve_local_target(path, root, target)
            if not resolved.exists():
                findings.append(
                    LinkFinding(
                        source=path,
                        line_number=line_number,
                        target=target,
                    )
                )

    return findings


def check_repository(root: Path) -> list[LinkFinding]:
    findings: list[LinkFinding] = []
    for path in markdown_files(root):
        findings.extend(check_file(path, root))
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root to scan",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = args.root.resolve()
    findings = check_repository(root)

    for finding in findings:
        print(finding.render(root))

    if findings:
        print(f"\nInternal-link validation failed with {len(findings)} error(s).")
        return 1

    print("Internal-link validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
