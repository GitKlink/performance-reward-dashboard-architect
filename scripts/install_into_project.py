#!/usr/bin/env python3
"""Install an immutable, read-only Architect capability snapshot into a local project.

Default is plan-only. --apply creates *new* files; it never overwrites existing
project files or model artifacts. Source is the local Architect + pinned Standards
checkouts, not a network-dependent installer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path(".agents/skills/dax-measure-standards-review")
DOC = Path("docs/power-bi-architect")
STD = DOC / "standards"
PIN_FILE = ROOT / SKILL / "references/source-lock.json"
SKILL_FILES = (
    "SKILL.md",
    "README.md",
    "scripts/review_measures.py",
    "references/check-coverage.md",
    "references/source-lock.json",
)
ARCHITECT_REPO = "GitKlink/performance-reward-dashboard-architect"
INSTALL_SCHEMA = "power-bi-fabric-architect-install-v1"


class InstallError(Exception):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def git(folder: Path, *args: str) -> str:
    try:
        p = subprocess.run(("git", "-C", str(folder), *args),
                           capture_output=True, text=True, check=False)
    except FileNotFoundError as exc:
        raise InstallError("Git is required.") from exc
    if p.returncode:
        raise InstallError("Git verification failed in " + str(folder) + ": " +
                           " ".join(args))
    return p.stdout.strip()


def git_checkout(folder: Path, expected_repo: str, expected_sha: str | None = None) -> str:
    if Path(git(folder, "rev-parse", "--show-toplevel")).resolve() != folder.resolve():
        raise InstallError("Expected Git repository root: " + str(folder))
    origin = git(folder, "remote", "get-url", "origin").lower()
    if not re.search(r"(^|[:/])" + re.escape(expected_repo.lower()) + r"(?:\.git)?$", origin):
        raise InstallError("Unexpected repository origin: " + expected_repo)
    actual = git(folder, "rev-parse", "HEAD")
    if expected_sha and actual != expected_sha:
        raise InstallError("Pinned standards revision required: " + expected_sha +
                           " (checkout is " + actual + "). Use a separate pinned clone.")
    return actual


def checked_file(root: Path, rel: Path) -> bytes:
    p = root / rel
    if not p.is_file() or p.is_symlink():
        raise InstallError("Missing or symlinked source file: " + str(rel))
    return p.read_bytes()


def build_files(project: Path, standards_repo: Path) -> tuple[dict[Path, bytes], dict]:
    if not project.is_dir():
        raise InstallError("The target project directory must already exist.")
    for forbidden in (ROOT, standards_repo):
        if project == forbidden or forbidden in project.parents or project in forbidden.parents:
            raise InstallError("Target must be an independent Power BI project, not a source checkout.")

    lock = json.loads(PIN_FILE.read_text(encoding="utf-8"))
    if lock.get("schema_version") != "power-bi-fabric-standards-source-lock-v1":
        raise InstallError("Unknown standards lock schema.")
    if lock.get("repo") != "GitKlink/power-bi-fabric-standards":
        raise InstallError("Unexpected source lock repository.")
    pin = lock["git_sha"]
    architect_sha = git_checkout(ROOT, ARCHITECT_REPO)
    git_checkout(standards_repo, lock["repo"], pin)
    if git(ROOT, "status", "--porcelain", "--untracked-files=no", "--", str(SKILL)):
        raise InstallError("Architect skill source has uncommitted changes.")
    if git(standards_repo, "status", "--porcelain", "--", "semantic-model"):
        raise InstallError("Canonical standards contain uncommitted changes.")

    payload = {}
    for name in SKILL_FILES:
        rel = SKILL / name
        raw = checked_file(ROOT, rel)
        if git(ROOT, "hash-object", "--", str(rel)) != git(ROOT, "rev-parse", "HEAD:" + rel.as_posix()):
            raise InstallError("Architect skill source differs from committed bytes: " + str(rel))
        payload[rel] = raw

    # Ship a harmless test input with the skill so it can be verified again
    # when the Architect source repository is no longer part of the workspace.
    fixture_source = Path("examples/dax-measure-review/measure-inventory.synthetic.csv")
    fixture = checked_file(ROOT, fixture_source)
    if git(ROOT, "hash-object", "--", fixture_source.as_posix()) != git(
        ROOT, "rev-parse", "HEAD:" + fixture_source.as_posix()
    ):
        raise InstallError("Synthetic fixture differs from committed Architect source.")
    payload[SKILL / "examples/measure-inventory.synthetic.csv"] = fixture

    std_sha256 = {}
    for path, expected_blob in sorted(lock["files"].items()):
        rel = Path(path)
        if rel.is_absolute() or ".." in rel.parts or rel.parts[0] != "semantic-model":
            raise InstallError("Unsafe standards lock entry: " + path)
        raw = checked_file(standards_repo, rel)
        if blob_sha(raw) != expected_blob:
            raise InstallError("Pinned standards contents differ from approved Git blob: " + path)
        std_sha256[path] = sha256(raw)
        payload[STD / rel] = raw

    source_manifest = {
        "schema_version": "power-bi-fabric-standards-snapshot-v1",
        "repo": lock["repo"],
        "git_sha": pin,
        "files_sha256": std_sha256,
    }
    payload[STD / "source-manifest.json"] = (
        json.dumps(source_manifest, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    guidance = (
        "# Power BI / Fabric Architect: installed project assets\n\n"
        "This is a **project-local installed snapshot**; the source repositories "
        "remain authoritative. Do not edit the copied standards.\n\n"
        "- Skill: `.agents/skills/dax-measure-standards-review/SKILL.md`\n"
        "- Source provenance: `docs/power-bi-architect/installation.json`\n"
        "- Standards manifest: `standards/source-manifest.json`\n"
        "- Standards read order: `standards/semantic-model/README.md`, "
        "`semantic_measure_standard.md`, `business_glossary.md`, "
        "then the relevant `domains/` extension. "
        "The improvement backlog is proposed work, not approved policy.\n\n"
        "Run the reviewer's Python checker against a **private measure metadata CSV** "
        "with `--standards-root docs/power-bi-architect/standards`; keep reports "
        "outside public repositories. Reinstall from reviewed source revisions "
        "rather than manually editing installed files.\n"
    )
    payload[DOC / "README.md"] = guidance.encode("utf-8")

    records = {p.as_posix(): sha256(contents) for p, contents in sorted(payload.items())}
    install_record = {
        "schema_version": INSTALL_SCHEMA,
        "architect_repo": ARCHITECT_REPO,
        "architect_git_sha": architect_sha,
        "standards_repo": lock["repo"],
        "standards_git_sha": pin,
        "capabilities": ["dax-measure-standards-review"],
        "installed_assets_sha256": records,
    }
    payload[DOC / "installation.json"] = (
        json.dumps(install_record, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    return payload, install_record


def install(project: Path, standards_repo: Path, *, apply: bool = False) -> str:
    project, standards_repo = project.resolve(), standards_repo.resolve()
    payload, record = build_files(project, standards_repo)
    existing = [(path, project / path) for path in payload if (project / path).exists() or
                (project / path).is_symlink()]
    if existing:
        # All managed bytes match: no-op on identical re-run, and no modified files.
        if len(existing) == len(payload) and all(
            actual.is_file() and not actual.is_symlink() and
            actual.read_bytes() == payload[relative]
            for relative, actual in existing
        ):
            return "ALREADY INSTALLED (identical snapshot; no files changed)."
        conflicts = [str(relative) for relative, actual in existing
                     if not actual.is_file() or actual.is_symlink() or
                     actual.read_bytes() != payload[relative]]
        raise InstallError("Existing managed path(s) must not be overwritten: " +
                           ", ".join(conflicts or [str(p) for p, _ in existing]) +
                           ". Review local changes and update through a separate approved process.")

    # Refuse to traverse project-owned symlink directories.
    for relative in payload:
        parent = project
        for part in relative.parts[:-1]:
            parent = parent / part
            if parent.is_symlink():
                raise InstallError("Refusing symlink parent: " + str(parent))
            if parent.exists() and not parent.is_dir():
                raise InstallError("Path is not a directory: " + str(parent))

    if not apply:
        return ("PLAN ONLY: create " + str(len(payload)) + " files inside " + str(project) +
                "; skill=.agents/skills/dax-measure-standards-review; "
                "standards=docs/power-bi-architect/standards; architect_sha=" +
                record["architect_git_sha"] + "; standards_sha=" + record["standards_git_sha"] +
                ". No files changed. Re-run with --apply only after approving the plan.")

    created_files = []
    created_dirs = []
    try:
        for relative, contents in sorted(payload.items(), key=lambda x: x[0].as_posix()):
            dest = project / relative
            missing = []
            parent = dest.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for d in reversed(missing):
                d.mkdir()
                created_dirs.append(d)
            # 'xb' refuses all existing files, including a collision arising after preflight.
            with dest.open("xb") as fp:
                created_files.append(dest)
                fp.write(contents)
    except (OSError, ValueError):
        for p in reversed(created_files):
            p.unlink(missing_ok=True)
        for p in reversed(created_dirs):
            try:
                p.rmdir()
            except OSError:
                pass
        raise
    return ("INSTALLED " + str(len(payload)) + " files into " + str(project) +
            ". Run a synthetic review with the installed skill and standards.")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", required=True, type=Path, help="Existing target Power BI project root")
    ap.add_argument("--standards-repo", required=True, type=Path,
                    help="Local canonical Standards Git checkout at the reviewer pinned revision")
    ap.add_argument("--apply", action="store_true",
                    help="Create project-local files after reviewing a default dry-run plan")
    args = ap.parse_args(argv)
    try:
        print(install(args.project, args.standards_repo, apply=args.apply))
    except (InstallError, OSError, ValueError, json.JSONDecodeError, KeyError) as exc:
        print("INSTALL BLOCKED: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
