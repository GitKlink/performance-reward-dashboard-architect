---
name: setup-power-bi-architect
description: Install version-pinned copies of approved Power BI / Fabric Architect skills and canonical standards into the currently open Power BI project. Inspect, plan, approve, install and verify.
disable-model-invocation: true
---

# Install Power BI / Fabric Architect into this project

This is the **user-invoked setup procedure**, not a custom global CLI.
Unlike the first environment-only pilot, this installs a **self-contained
project-local copy** so the Power BI project can be reopened independently.
Only the first capability, `dax-measure-standards-review`, is supported today.

**Read `../../../SETUP.md` from the LOCAL Architect clone in full** before acting,
then read `../dax-measure-standards-review/SKILL.md`.
The Architect clone may be in a folder called `clones`, but find its true path
rather than assuming a drive or home location.

## 1. Explore without writing anything

- Determine **which currently open folder is the target Power BI project**.
  If Cursor has opened a parent `clones` folder or several roots, confirm the
  specific PBIP/project directory, not a source repository.
- Locate the local Architect checkout containing `scripts/install_into_project.py`.
- Locate a local `GitKlink/power-bi-fabric-standards` checkout at approved SHA
  `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`. If the user's checkout is
  newer, propose a separate pinned clone; **never** detach/reset their existing one.
- Identify existing `.agents/skills/`, `.cursor/skills/`, `docs/`, `AGENTS.md`, `.cursor/` and any
  `docs/power-bi-architect/installation.json`; preserve all existing contents.
- Confirm Git and Python 3.10+ are available. Do not assume Power BI tools or a
  Python environment is already installed inside the target project.
- Check for directory and file collisions; verify target is not Architect/Standards.
- Never upload proprietary CSV, DAX formulas, PBIP files or report outputs to GitHub.

## 2. Plan and request approval

From the **local Architect repository root**, use the deterministic installer
in **dry-run** mode:

```sh
python scripts/install_into_project.py --project "<OPEN_POWER_BI_PROJECT_ABSOLUTE_PATH>" --standards-repo "<PINNED_STANDARDS_REPO_ABSOLUTE_PATH>"
```

Show the user exactly what the installer will create, why, and whether their
project has pre-existing files. The installer adds only:
- `.agents/skills/dax-measure-standards-review/` including SKILL.md, the Python
  checker, references, source lock and small synthetic example;
- `docs/power-bi-architect/standards/semantic-model/` with copied core standards,
  glossary, domain extensions and non-normative backlog;
- provenance manifests and a short `docs/power-bi-architect/README.md`.

The user should be able to continue using unrelated skills in the existing
`.agents/skills/` folder. No new `AGENTS.md` or `.cursor/rules` are needed.

**Get approval before creating clones, files or project configuration.** Do not
silently install globally, update the Architect clone or modify any PBIP model.

## 3. Apply only the approved project-local copy

After approval, run the **same command** with `--apply`:

```sh
python scripts/install_into_project.py --project "<OPEN_POWER_BI_PROJECT_ABSOLUTE_PATH>" --standards-repo "<PINNED_STANDARDS_REPO_ABSOLUTE_PATH>" --apply
```

The installer fails on overwritten, changed or partial managed files. Never
work around a conflict by deleting project-owned files. On identical re-run
it reports `ALREADY INSTALLED` without changing bytes.

**Do not copy the setup skill itself by default.** The user's project receives
the functional DAX-review capability. Installation/update instructions remain
in the source Architect repository. The project gets a manifest recording
which source Architect and Standards Git revisions produced its copy.

## 4. Verify independent project usability

- Inspect the installed files and `docs/power-bi-architect/installation.json`
  for the correct source revisions and installed asset SHA-256 checksums.
- Verify the standards lock + installed `source-manifest.json`; no Git checkout
  must be needed to **run** the installed reviewer.
- Close other source roots or open **only the target project** in local Cursor,
  and confirm `dax-measure-standards-review` appears in Cursor Skills. If that
  cannot be inspected, state **not verified**.
- Run the synthetic checker from the **target project root**. The example\n  uses `.agents/skills`; substitute `.cursor/skills` when the installer selected it:

```sh
python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input ".agents/skills/dax-measure-standards-review/examples/measure-inventory.synthetic.csv" --standards-root "docs/power-bi-architect/standards" --domain variable_reward --out-dir "<NEW_PRIVATE_REPORT_DIR>"
```

- Inspect `review.json` and `review.md`: `schema_version` equals
  `power-bi-fabric-architect-dax-measure-review-v1`;
  `status` equals `partial_review_only`;
  `standards.verification` equals `pinned_project_copy`;
  Git SHA is `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`;
  fixture measure `M_VR Payout%` must produce a naming finding.
- **Unit tests**: if the source Architect checkout is available, run
  `python -m unittest discover -s tests -p 'test_*.py' -v`
  from the source repo. The unit suite is separate from the installed smoke test.
- A successful run is **partial metadata validation**, not full DAX conformance
  or compilation, nor proof that a user's real Power BI model was checked.

## 5. Hand off to a real DAX measure inventory

Give user the Desktop DAX Query View export command:

```dax
EVALUATE INFO.VIEW.MEASURES()
```

Keep exported measure metadata **private** (it may contain proprietary DAX).
Run the installed Python checker against the private CSV with a fresh report
directory and selected domain. Read the local copied standards and propose
human-approved DAX refactor suggestions, **do not apply anything to the model**.

Report three gates separately:
- **A**: source Python unit tests (if available).
- **B**: local copied skill installed, discoverable and synthetic CLI verified.
- **C**: real Power BI inventory reviewed (not part of automatic installation).

List exact installed folders, source SHAs and any blockers. Do not claim B/C
unless you observed the corresponding results. Never overwrite existing skills,
standards, reports, project instructions or Power BI files.

## Updating

The current installer is **additive and fail-closed**; it does not implement
an automatic updater. Keep the installed manifest, compare versions against
the upstream Git sources and plan a separately approved migration if versions
change. Do not replace modified project-owned files or relax source locks.
