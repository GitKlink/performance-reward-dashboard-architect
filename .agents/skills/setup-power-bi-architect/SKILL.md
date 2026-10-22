---
name: setup-power-bi-architect
description: Set up a local Cursor workspace to use the Power BI / Fabric Architect's read-only DAX Measure Standards Reviewer with a pinned canonical standards checkout. Run once before first use. Inspect, propose, confirm, apply and verify.
disable-model-invocation: true
---

# Setup Power BI / Fabric Architect

This is a **prompt-driven setup skill**, not an installation executable. It uses the coding agent's ordinary local file/Git/terminal tools. Model the flow on Matt Pocock's `setup-matt-pocock-skills`: **explore → propose → confirm → make minimal changes → verify**.

Only install the **first usable DAX measure-review vertical slice**, not a hypothetical full agent ecosystem or a plugin marketplace. Do not rename this product Wayfinder. Do **not** edit Power BI/PBIP/DAX/TMDL files.

## 0. Source, scope and prerequisites

Read these files from the **existing local Architect checkout**, typically inside the user's `clones` directory, before making changes. Resolve paths relative to the open workspace: `performance-reward-dashboard-architect/SETUP.md` if Cursor opened the parent `clones` folder, or `SETUP.md` if it opened the Architect repository itself. Do not fetch the hosted GitHub copy when a local version exists; GitHub is only a bootstrap fallback for a missing clone. Confirm the local checkout/branch state and do not update it without approval.

Read these files from the **Architect repository** before making changes:
1. [`SETUP.md`](../../../SETUP.md) (root relative to this skill).
2. [DAX reviewer instructions](../dax-measure-standards-review/SKILL.md).
3. [DAX reviewer quick start](../dax-measure-standards-review/README.md).
4. [Rule coverage and omissions](../dax-measure-standards-review/references/check-coverage.md).

The two required repositories:
- **Architect**: `GitKlink/performance-reward-dashboard-architect`, owns this setup skill, read-only checker and architecture workflows.
- **Standards**: `GitKlink/power-bi-fabric-standards`, the public **canonical engineering-policy authority**.
- **DAX/M Library**: optional and **not required** for this first DAX review.

Pinned compatible Standards revision: `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`. This is the revision enforced by `dax-measure-standards-review/scripts/review_measures.py`. Never silently replace the pin with `main`.

In scope: **local Cursor Agent** with Git and Python 3.10+; use a synthetic fixture before any real private measure inventory. Do not claim remote Cursor Cloud Agent/multi-root/CI support was established. Cursor should discover the reviewer from the Architect repository's `.agents/skills/`.

## 1. Explore existing environment (no writes)

- Identify the workspace/project folder and whether the user wants **first synthetic review only** (default) or integration into a real Power BI/PBIP project (optional).
- Check the host: local Cursor Agent vs remote/cloud; stop or give supported alternatives if remote/cloud cannot access required local files.
- Inspect available `git`, `python` (`py -3` on Windows if relevant), permissions and usable local storage.
- Find an existing Architect clone, Standards clone and optional PBIP project. Inspect each repository's **remote origin**, `HEAD`, working tree cleanliness and `git status`. Do not change branches, stash, reset, clean, force-pull or remove directories.
- Check whether skill `dax-measure-standards-review` is already installed/discovered or conflicts with another same-named skill. Cursor supports project skills under `.agents/skills/<name>/SKILL.md` and `.cursor/skills/<name>/SKILL.md`; don't create duplicate copies.
- Check for a **read-only, private report destination** outside the source repositories. If the chosen path exists, inspect it and avoid overwriting `review.md` or `review.json`.

## 2. Propose a minimal setup plan (human confirmation gate)

Present a concise plan with:
1. Host, Python/Git results, and what already exists.
2. Exact chosen folder for the Architect checkout, and Standards clone at the **pinned** revision.
3. Whether any Git clone, new directory or workspace file is proposed.
4. How Cursor will discover the skill (preferred: open Architect as a local workspace root, including the optional PBIP folder as a second root). **Do not copy the reviewer skill or create a global installation by default.**
5. Expected test commands and private report output path.
6. Any unresolved permissions or model data sensitivity.

**Pause for approval** before writes, including Git clones, generated workspace files, or changes to existing project instructions. Do not ask questions already answered by local inspection. If a good checkout exists, reuse it. If not, propose a **new, distinct local path**, never overwrite the existing folder.

## 3. Apply *only* approved setup changes

- Clone missing repositories from the public GitHub sources **after approval**. Never execute a remote script via `curl | bash` or equivalent.
- If an **existing** Standards checkout is at a different SHA, **do not detach or reset it**. Create a *separate* pinned checkout, preferably a fresh clone with its own distinct folder. If the existing checkout is exactly at the pin with clean `semantic-model/`, reuse it.
- For a **newly cloned and clean** Standards checkout only, run `git switch --detach 2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9` and verify `git rev-parse HEAD`. If the historical commit is unavailable, **stop** and report why; don't bypass the checker.
- Verify the origin is `GitKlink/power-bi-fabric-standards` and the required committed standard documents exist. The checker performs strict source validation at review time.
- Open the Architect folder in local Cursor, or create a user-approved local multi-root `.code-workspace` file **outside public repositories** if a PBIP project is included. Do not assume that merely linking to GitHub grants local filesystem access. Cursor's Skills view is the authority on actual skill discovery.
- No automatic project-local skill copy, user-global installation, `AGENTS.md` overwrite, `MCP` setup, plugin installation or installer CLI is needed for this pilot.
- The real input inventory remains in an explicitly private folder. Never upload it to a public repo, issue, PR or log; don't copy confidential DAX into synthetic test fixtures.

## 4. Verify the synthetic slice (safe, no PBIP edits)

Use local commands appropriate for Windows, macOS or Linux. The agent should resolve paths from its actual inspected environment; examples below assume shell working directory at the **Architect repo root** and three real paths selected in step 2.

1. Assert Architect working tree and Python/Git availability. Confirm pinned Standards path is a valid clone with the required commit and expected remote.
2. Run standard-library unit tests:

   ```sh
   python -m unittest discover -s tests -p 'test_dax_measure_reviewer.py' -v
   ```

3. Compile the checker:

   ```sh
   python -m py_compile .agents/skills/dax-measure-standards-review/scripts/review_measures.py
   ```

4. Run a real **read-only checker execution** against synthetic metadata using the resolved paths (substitute shell quoting and absolute locations):

   ```sh
   python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input "examples/dax-measure-review/measure-inventory.synthetic.csv" --standards-root "<PINNED_STANDARDS_ABSOLUTE_PATH>" --domain variable_reward --out-dir "<NEW_EMPTY_PRIVATE_OUTPUT_FOLDER_OUTSIDE_REPOS>"
   ```

5. Inspect `review.md` and `review.json`. Verify `schema_version == "power-bi-fabric-architect-dax-measure-review-v1"`, `status == "partial_review_only"`, the standards Git SHA equals the pinned commit, and the **synthetic deliberately nonstandard** `M_VR Payout%` row produces findings. Do not claim that the synthetic fixture's business semantics were verified.
6. Check in Cursor's **Customize → Skills** (or equivalent available settings) that `dax-measure-standards-review` is discoverable. If discovery cannot be inspected directly, report it as **not verified** and give the user the manual check.
7. If anything fails, report the actual failure and the smallest safe repair suggestion. Do not claim successful installation based solely on a file existing.

Distinguish three independent gates:
- **A: unit tests** passed (source-code correctness on synthetic/mocks).
- **B: local source/skill + synthetic CLI smoke test** passed.
- **C: actual Power BI semantic-model measure inventory** reviewed (requires a separate real export).

## 5. Hand off to the first real model pilot

Only after gates A/B, guide the user through Power BI Desktop **DAX Query View**:

```dax
EVALUATE
    INFO.VIEW.MEASURES()
```

Export the result as UTF-8 CSV to a **private** location. Retain `Name`, `Table`, `Description`, `FormatString`, `FormatStringDefinition`, `IsHidden` and `DisplayFolder` when available. The checker requires only `Name`, but other missing fields must be reported **not evaluated**, not treated as zero violations.

Execute the same CLI against that CSV with a **new private output folder** and relevant `--domain` (e.g. `variable_reward`). Have the reviewer skill read the authoritative documents and produce a **review proposal**, not a rename or model change. A return code of 0 means only that the partial review ran; it does not certify conformance.

For human review, present **old name, proposed name, explanation, canonical rule, folder/description suggestions, semantics/denominator questions, dependency concerns and approval status**. Do not apply anything to the model.

## 6. End-of-run handoff

Summarise:
- What existed, what was added with the user's approval, and where it is located.
- Exact Architect SHA, Standards SHA and source Git remotes (no authentication tokens).
- Test outcomes for A/B/C separately and report paths, without copying confidential contents into chat when prohibited.
- Any unverified capabilities or blockers, and the next user action (Power BI export or open Cursor Skills).

Do not present "setup complete" until B has been genuinely verified. Never imply that a documentation-only PR established local installation or PBIP model testing.

**Update rules:** no silent upstream updates, no automatic rewrite of a product repository, no version drift. Future reviewer baseline changes require reviewed tests and a new source pin.
