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
- Verify the project expects skills grouped by **provider folder**, then by skill name. Never place a DAX reviewer directly under the root skills directory.
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
- `<existing-skills-root>/power-bi-architect/dax-measure-standards-review/` including SKILL.md, the Python
  checker, references, source lock and small synthetic example;
- `docs/power-bi-architect/standards/semantic-model/` with copied core standards,
  glossary, domain extensions and non-normative backlog;
- provenance manifests and a short `docs/power-bi-architect/README.md`.

The user must be able to continue using unrelated skills under the existing
`.agents/skills/` or `.cursor/skills/` root. Keep any `matt-pocock`, `skills-for-fabric` and other provider folders untouched.\nThe `power-bi-architect` parent is a provider label, not a skill itself;\nsubsequent Architect capabilities receive sibling folders beneath it. No new `AGENTS.md` or `.cursor/rules` are needed.

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
- Run the synthetic checker from the **target project root**. The example
  uses `.cursor/skills` as in EOY-REWARD-DASHBOARD; substitute `.agents/skills` if that is the project's existing root:

```sh
python .cursor/skills/power-bi-architect/dax-measure-standards-review/scripts/review_measures.py --input ".cursor/skills/power-bi-architect/dax-measure-standards-review/examples/measure-inventory.synthetic.csv" --standards-root "docs/power-bi-architect/standards" --domain variable_reward --out-dir "<NEW_PRIVATE_REPORT_DIR>"
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

## Updating an existing project-local installation

If `docs/power-bi-architect/installation.json` already exists, **do not
run the first-time installer**. Follow the project-local update procedure:

1. Inspect the *actual currently open Power BI project*, its installation
   manifest and its local modifications. Preserve `matt-pocock`,
   `skills-for-fabric`, other provider skills and all project-owned files.
2. Confirm the local Architect source changes are **committed**, with clean
   tracked skill files, and locate the compatible pinned Standards checkout.
   The source lock must remain consistent with the reviewer's `BASELINE_SHA`.
   Standards revisions may advance only through a separately reviewed
   source-lock and checker update.
3. **Plan without writing** from the Architect source root:

   ```sh
   python scripts/update_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>"
   ```

4. Summarise each `add`, `replace` or `remove`, both source SHAs,
   manifest change, and the complete **64-character plan ID**. Clearly
   identify removals. If the command blocks because the user edited an
   installed file or a project-owned path conflicts, do **not** delete or
   overwrite it automatically. Stop and request a reviewed resolution.
5. **Ask for user approval**. Do not treat a previous project's approval
   as approval for this plan, even if the same source revisions are used.
6. After explicit approval, apply **only that exact plan**:

   ```sh
   python scripts/update_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>" --apply --expected-plan-id "<APPROVED_PLAN_ID>"
   ```

   The command recomputes the plan and blocks if files or source revisions
   changed. It refuses relocation of the existing skill root and never
   modifies unrelated skills, rules, project instructions or model assets.
   Source-based removals only apply to unchanged, previously managed files.
7. Verify the installed `docs/power-bi-architect/installation.json` now
   records the new Architect/Standards SHA. Reopen **only the project** in
   Cursor; run the installed synthetic DAX review command from section 4.
   Confirm `review.json` was produced from
   `standards.verification=pinned_project_copy`. The installed skills must
   still work independently of the source clones.
8. Report the update result, managed file changes, local Cursor discovery
   and actual Power BI inventory results as *separate* validations.

Updates are **opt-in per Power BI project**, not automatic. Do not invent
an auto-updater or claim that the current installer updates every project
which once received a skill. The source repositories remain authoritative.

