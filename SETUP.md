# Install Power BI / Fabric Architect into the current Power BI project

This file instructs **local Cursor Agent** to install *copies* of approved
Architect skills and canonical standards into the Power BI project that is open
in Cursor. It is not an executable script and does not install a global plugin.

## Paste into Cursor Agent

```text
My open Cursor workspace contains the target Power BI project.
Read the LOCAL clones/performance-reward-dashboard-architect/SETUP.md
and its .agents/skills/setup-power-bi-architect/SKILL.md.
Resolve the true clone paths rather than assuming their location.
Inspect my existing project folders. Put Architect skills under the project's
EXISTING skills folder in a power-bi-architect provider subfolder, with each
skill beneath it. Copy approved pinned standards into the project docs folder.
Show me the exact dry-run plan and ask my approval before writing anything.
Preserve matt-pocock, skills-for-fabric, all other skills, rules, and PBIP files.
Verify the installed DAX reviewer using only its copied local files.
Never edit a Power BI model or publish real measure inventory data.
```

If your Architect clone is missing, the AI may propose cloning
`https://github.com/GitKlink/performance-reward-dashboard-architect`
and then follow these instructions **locally**. If the workspace contains
several projects, verify the actual target before installing.

**Procedure:** [`setup-power-bi-architect/SKILL.md`](.agents/skills/setup-power-bi-architect/SKILL.md).

## What the current installer creates

For a project already using `.cursor/skills`, such as EOY-REWARD-DASHBOARD:

```text
EOY-REWARD-DASHBOARD/
├── .cursor/
│   ├── rules/                                    # unchanged
│   └── skills/
│       ├── matt-pocock/                          # unchanged
│       ├── skills-for-fabric/                    # unchanged
│       └── power-bi-architect/                   # source/provider folder
│           └── dax-measure-standards-review/     # specific skill
│               ├── SKILL.md
│               ├── README.md
│               ├── scripts/review_measures.py
│               ├── references/
│               └── examples/measure-inventory.synthetic.csv
├── docs/
│   └── power-bi-architect/
│       ├── README.md
│       ├── installation.json                     # provenance and copied-file hashes
│       └── standards/
│           ├── source-manifest.json              # pinned standards hashes
│           └── semantic-model/                   # all 11 copied standards files
├── AGENTS.md                                     # unchanged
└── <existing Power BI files>                     # unchanged
```

For a project already using `.agents/skills`, the same
`power-bi-architect/dax-measure-standards-review/` hierarchy goes underneath
`.agents/skills/`. If both skill roots exist, **ask** which should receive
the new provider. If neither exists, the current default is `.agents/skills/`.
Do not move other providers or merge their files into ours.

Cursor walks its skills roots recursively, so its documented skill identity
remains `dax-measure-standards-review` (not `power-bi-architect`).
Future Architect skills must be separate sibling folders under
`skills/power-bi-architect/`.

## Updating a project after changing the local clones

**No automatic syncing.** Once your Architect changes have been reviewed and
committed in your local Git clone, open the existing Power BI project in Cursor.
The updater reads the current `docs/power-bi-architect/installation.json`,
compares your installed assets with the latest committed local source snapshot,
and presents **add / replace / remove** actions plus source commit revisions.

Copy into Cursor Agent:

```text
My current Power BI project already has Power BI / Fabric Architect installed.
Read the LOCAL clones/performance-reward-dashboard-architect/SETUP.md
and its setup-power-bi-architect/SKILL.md. Inspect the source clones and my
current project's docs/power-bi-architect/installation.json.
Run the project update plan; list changed files, old/new source Git SHAs and
conflicts. Do not change anything until I approve the exact update plan ID.
Once approved, apply the same plan, then run the installed synthetic reviewer.
Preserve other provider skills, project rules, AGENTS.md and PBIP/model files.
```

From the updated local Architect repository root, after identifying actual
paths, run a read-only plan:

```powershell
python scripts/update_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>"
```

Review the output, including its **64-character plan ID**. Only after your
explicit approval, run:

```powershell
python scripts/update_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>" --apply --expected-plan-id "<APPROVED_PLAN_ID>"
```

The updater **rechecks** all source and installed files before writing. If any
managed file was edited inside the Power BI project, any unknown project-owned
file would be overwritten, or the plan ID differs from what you approved,
the update **blocks**. It retains the originally selected `.cursor/skills` or
`.agents/skills` root and `power-bi-architect/<skill-name>` hierarchy.

Existing project files outside Architect's recorded install assets are never
modified. Files previously installed by Architect may be removed **only if
their bytes still match the original installation manifest**, and only when
the approved plan explicitly lists the removal. Writes are staged, with
attempted rollback on an ordinary execution failure. As with any multi-file
update, ensure important projects have version-control or filesystem backups;
a system crash or disk failure cannot be guaranteed recoverable.

**Version policy:** updates use **committed source changes**, not uncommitted
working-tree edits. Changes to the Standards repository require a separate
reviewed update of the Architect's `source-lock.json`, DAX reviewer's
`BASELINE_SHA` and corresponding verification tests; the installer deliberately
refuses a different Standards revision until that compatibility update exists.
The source Standards clone can be separate from your active latest checkout.
This avoids silently changing approved business and engineering policy.

The installer/updater does not push changes to the project Git repository,
edit DAX/TMDL/PBIP or update Matt Pocock/Microsoft skills.

## Approval-based project copy

Prerequisites: local Git, Python 3.10+, and the locally cloned
[Architect repository](https://github.com/GitKlink/performance-reward-dashboard-architect).
Canonical standards come from the local
[Standards repository](https://github.com/GitKlink/power-bi-fabric-standards)
at immutable commit `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`.
If the user's Standards clone is newer, leave it untouched and propose
a **second pinned clone**.

From the local **Architect repository root**, run the read-only installation
plan and show it to the user:

```powershell
python scripts/install_into_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>"
```

Only **after the user approves**, apply the same plan:

```powershell
python scripts/install_into_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>" --apply
```

The installer detects the existing skills root; if both are present, add
`--skills-dir .cursor/skills` or `--skills-dir .agents/skills` with user
approval. It creates only new files; existing skill folders, project instructions,
standards or model files are never overwritten. Identical reruns are no-ops.
Changed or incomplete previous installs **block** rather than silently update.

The standards copy is a read-only **consumer snapshot**. Core, glossary,
improvement backlog and all seven domain files retain their original folder
layout. The authoritative source stays in the Standards Git repository.
The DAX reviewer checks immutable source Git-blob IDs from its bundled
`references/source-lock.json` against every copied standard, as well as
the SHA-256 values recorded in the installation manifest. **No Git checkout
needs to remain open after installation.**

## Verify the installed capability

Run the following from the **target Power BI project root**, with a new
private reports folder. The example assumes an existing `.cursor/skills`
root; substitute `.agents/skills` if that was selected:

```powershell
python .cursor/skills/power-bi-architect/dax-measure-standards-review/scripts/review_measures.py --input ".cursor/skills/power-bi-architect/dax-measure-standards-review/examples/measure-inventory.synthetic.csv" --standards-root "docs/power-bi-architect/standards" --domain variable_reward --out-dir "<PRIVATE_REPORTS_FOLDER>"
```

Check `review.json` and `review.md` were created with
`status=partial_review_only`,
`schema_version=power-bi-fabric-architect-dax-measure-review-v1`, and
`standards.verification=pinned_project_copy`. Cursor should discover the skill
with **only the Power BI project open**; if this cannot be checked, mark it
*unverified*, not installed successfully by assumption.

When ready for a **separate real-model pilot**, use Power BI Desktop's
DAX Query View:

```dax
EVALUATE INFO.VIEW.MEASURES()
```

Keep its CSV and the resulting reports **private**, outside public repositories. The reviewer does not
rename DAX, modify PBIP/TMDL, compile expressions, or certify all standards.

Only the DAX reviewer capability is packaged today. The reusable DAX/M Library,
Microsoft Fabric upstream skills, other Architect skills and automatic update
management are not part of this installation.
