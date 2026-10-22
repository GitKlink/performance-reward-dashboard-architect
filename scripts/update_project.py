#!/usr/bin/env python3
"""Plan or safely apply updates to an existing project-local Architect installation.

This is an explicit opt-in update, never an unattended sync. The checked source
files come from reviewed, committed Architect and Standards local clones.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

from install_into_project import (
    DOC, INSTALL_SCHEMA, PROVIDER_DIR, InstallError,
    build_files, sha256,
)

MANIFEST = DOC / "installation.json"
PLAN_SCHEMA = "power-bi-fabric-architect-update-plan-v1"
SKILL = "dax-measure-standards-review"
ROOTS = (".agents/skills", ".cursor/skills")


def safe_relative(key: str, root: Path, skills_root: str) -> Path:
    if not isinstance(key, str) or not key or "\\" in key:
        raise InstallError("Invalid managed asset path in existing manifest.")
    rel = Path(key)
    if rel.is_absolute() or "." in rel.parts or ".." in rel.parts or rel.as_posix() != key:
        raise InstallError("Unsafe managed asset path in existing manifest: " + key)
    skills_prefix = Path(skills_root) / PROVIDER_DIR / SKILL
    if not (rel.is_relative_to(skills_prefix) or rel.is_relative_to(DOC)):
        raise InstallError("Manifest claims ownership outside installed Architect assets: " + key)
    path = root / rel
    if not path.is_relative_to(root):
        raise InstallError("Managed path escapes the Power BI project: " + key)
    part = root
    for component in rel.parts:
        part = part / component
        if part.is_symlink():
            raise InstallError("Managed path is symlinked: " + key)
    return rel


def load_previous(project: Path) -> tuple[dict, bytes, dict[Path, bytes]]:
    manifest_path = project / MANIFEST
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise InstallError("An existing Architect installation.json is required; use install for first-time setup.")
    manifest_bytes = manifest_path.read_bytes()
    try:
        prior = json.loads(manifest_bytes.decode("utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise InstallError("Existing installation manifest is unreadable.") from exc
    if prior.get("schema_version") != INSTALL_SCHEMA:
        raise InstallError("Unknown existing installation schema; manual migration needed.")
    skills_root = prior.get("skills_dir")
    if skills_root not in ROOTS or prior.get("skills_provider") != PROVIDER_DIR:
        raise InstallError("Existing installation has incompatible skills root/provider metadata.")
    if prior.get("architect_repo") != "GitKlink/performance-reward-dashboard-architect" or prior.get("standards_repo") != "GitKlink/power-bi-fabric-standards":
        raise InstallError("Unexpected source repository metadata in installation manifest.")
    if prior.get("capabilities") != [SKILL]:
        raise InstallError("Unsupported installed capability set; do not update blindly.")
    old_records = prior.get("installed_assets_sha256")
    if not isinstance(old_records, dict) or not old_records:
        raise InstallError("Existing installation has no reliable owned-file hashes.")
    if MANIFEST.as_posix() in old_records:
        raise InstallError("The installation manifest must not list itself as an owned asset.")
    old_bytes = {}
    for key, digest in old_records.items():
        rel = safe_relative(key, project, skills_root)
        if (not isinstance(digest, str) or len(digest) != 64 or
                any(c not in "0123456789abcdef" for c in digest)):
            raise InstallError("Invalid prior SHA-256 for: " + key)
        p = project / rel
        if not p.is_file() or p.is_symlink():
            raise InstallError("An installed managed file is missing or replaced: " + key)
        data = p.read_bytes()
        if sha256(data) != digest:
            raise InstallError("Project-local modifications detected; refuse to overwrite: " + key)
        old_bytes[rel] = data
    return prior, manifest_bytes, old_bytes


def validate_target(project: Path, paths: list[Path], old_skills_root: str):
    for rel in paths:
        safe_relative(rel.as_posix(), project, old_skills_root)
        target = project / rel
        for parent in (target, *target.parents):
            if parent == project:
                break
            if parent.is_symlink():
                raise InstallError("Symlink in target path: " + rel.as_posix())
            if parent.exists() and parent != target and not parent.is_dir():
                raise InstallError("Non-directory in target path: " + rel.as_posix())


def make_plan(project: Path, standards_repo: Path, skills_dir: str | None = None) -> tuple[dict, dict[Path, bytes], dict[Path, bytes]]:
    project, standards_repo = project.resolve(), standards_repo.resolve()
    prior, manifest_bytes, old_bytes = load_previous(project)
    previously_used = prior["skills_dir"]
    if skills_dir is not None and skills_dir != previously_used:
        raise InstallError("Cannot silently relocate an existing installation from " + previously_used)
    payload, new_record = build_files(project, standards_repo, previously_used)
    expected = set(old_bytes)
    next_keys = set(payload) - {MANIFEST}
    if not next_keys:
        raise InstallError("Empty new capability package; refusing to remove existing installation.")
    validate_target(project, list(expected | next_keys | {MANIFEST}), previously_used)
    # New additions must not collide with files not previously owned by this installation.
    for rel in sorted(next_keys - expected):
        p = project / rel
        if p.exists() or p.is_symlink():
            raise InstallError("New installer asset would overwrite a project-owned file: " + rel.as_posix())
    if (project / MANIFEST).read_bytes() != manifest_bytes:
        raise InstallError("Installation manifest changed during planning.")

    changes = []
    for rel in sorted(expected | next_keys):
        old = old_bytes.get(rel)
        new = payload.get(rel)
        if old == new:
            continue
        changes.append({
            "action": "add" if old is None else "remove" if new is None else "replace",
            "path": rel.as_posix(),
            "previous_sha256": sha256(old) if old is not None else None,
            "next_sha256": sha256(new) if new is not None else None,
        })
    new_manifest = payload[MANIFEST]
    manifest_action = (new_manifest != manifest_bytes)
    canonical = {
        "schema_version": PLAN_SCHEMA,
        "old_architect_sha": prior["architect_git_sha"],
        "new_architect_sha": new_record["architect_git_sha"],
        "old_standards_sha": prior["standards_git_sha"],
        "new_standards_sha": new_record["standards_git_sha"],
        "skills_dir": previously_used,
        "skills_provider": PROVIDER_DIR,
        "manifest_old_sha256": sha256(manifest_bytes),
        "manifest_new_sha256": sha256(new_manifest),
        "changes": changes,
    }
    plan_id = sha256(json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    canonical["plan_id"] = plan_id
    canonical["count"] = {
        action: sum(c["action"] == action for c in changes) for action in ("add", "replace", "remove")
    }
    canonical["manifest_update"] = manifest_action
    return canonical, payload, {**old_bytes, MANIFEST: manifest_bytes}


def apply_plan(project: Path, plan: dict, payload: dict[Path, bytes], old_bytes: dict[Path, bytes]):
    project = project.resolve()
    changes = plan["changes"]
    if not changes and not plan["manifest_update"]:
        return "UP TO DATE: no source or installed assets changed."

    # Stage all write bytes on the target filesystem before any managed file is touched.
    writes = {Path(c["path"]): payload[Path(c["path"])] for c in changes if c["action"] != "remove"}
    if plan["manifest_update"]:
        writes[MANIFEST] = payload[MANIFEST]
    removals = [Path(c["path"]) for c in changes if c["action"] == "remove"]

    dirs_created, staged, changed = [], {}, []
    try:
        for rel in sorted(writes):
            dst = project / rel
            missing = []
            parent = dst.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for d in reversed(missing):
                d.mkdir()
                dirs_created.append(d)
            with tempfile.NamedTemporaryFile(prefix=".architect-update-", dir=dst.parent, delete=False) as stream:
                stream.write(writes[rel])
                staged[rel] = Path(stream.name)
        # Complete each atomic per-file replace. Manifest is ALWAYS the last write.
        for rel in sorted(set(writes) - {MANIFEST}):
            os.replace(staged[rel], project / rel)
            del staged[rel]
            changed.append(rel)
        for rel in removals:
            (project / rel).unlink()
            changed.append(rel)
        if MANIFEST in staged:
            os.replace(staged[MANIFEST], project / MANIFEST)
            del staged[MANIFEST]
            changed.append(MANIFEST)
    except Exception:
        # Restore only bytes known to have been owned by us before starting;
        # never overwrite or delete unrelated pre-existing files.
        rollback_errors = []
        for rel in reversed(changed):
            dst = project / rel
            try:
                if rel not in old_bytes:
                    dst.unlink(missing_ok=True)
                else:
                    with tempfile.NamedTemporaryFile(prefix=".architect-rollback-", dir=dst.parent, delete=False) as stream:
                        stream.write(old_bytes[rel])
                        recovery = Path(stream.name)
                    os.replace(recovery, dst)
            except Exception as ex:
                rollback_errors.append(str(rel) + ": " + str(ex))
        if rollback_errors:
            raise InstallError("Update failed; rollback incomplete: " + "; ".join(rollback_errors))
        raise
    finally:
        for leftover in staged.values():
            leftover.unlink(missing_ok=True)
        for d in reversed(dirs_created):
            try:
                d.rmdir()
            except OSError:
                pass
    return ("UPDATED: " + str(len(changes)) + " managed asset changes; " +
            ("manifest updated." if plan["manifest_update"] else "manifest unchanged.") +
            " Plan " + plan["plan_id"])


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True, help="Existing target Power BI project")
    parser.add_argument("--standards-repo", type=Path, required=True,
                        help="Local pinned canonical Standards checkout")
    parser.add_argument("--skills-dir", choices=ROOTS,
                        help="Optional assertion of the existing project skills root; never relocates it")
    parser.add_argument("--apply", action="store_true", help="Apply a reviewed plan after approval")
    parser.add_argument("--expected-plan-id", help="Exact 64-character plan ID approved during dry run")
    args = parser.parse_args(argv)
    try:
        if args.apply and not args.expected_plan_id:
            raise InstallError("Updates require --expected-plan-id from the reviewed dry-run.")
        if args.expected_plan_id and not args.apply:
            raise InstallError("--expected-plan-id is for approved --apply executions only.")
        plan, new_files, prior = make_plan(args.project, args.standards_repo, args.skills_dir)
        if args.apply:
            if args.expected_plan_id != plan["plan_id"]:
                raise InstallError("Update plan changed since approval; run a new dry-run and re-approve.")
            print(apply_plan(args.project, plan, new_files, prior))
        else:
            print(json.dumps(plan, indent=2))
            print("\nPLAN ONLY — no files modified. Confirm the plan ID and request approval before --apply.")
    except (InstallError, OSError, ValueError, KeyError, UnicodeError, json.JSONDecodeError) as exc:
        print("UPDATE BLOCKED: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
