# Install Power BI / Fabric Architect into the current Power BI project

This file is **instructions for a local Cursor Agent**, not an executable installer.
Open your **Power BI / PBIP project** as the current Cursor project first.
The AI reads this file from your local Architect clone, then proposes and executes a
**project-local copy** of the approved capabilities and standards. It does not need
the Architect and Standards repositories open in Cursor after installation.

## Copy into Cursor Agent

```text
My currently open Cursor workspace is the TARGET Power BI project.
Find my local clones/performance-reward-dashboard-architect/SETUP.md
and follow its local setup-power-bi-architect/SKILL.md.
Inspect the project and upstream clones. Show the proposed project-local files
and exact dry-run plan. Ask for my approval before writing any files.
Install the reviewer into this project's existing .agents/skills/ folder,
and copy the pinned standards into its docs/power-bi-architect/standards/ folder.
Verify the installed reviewer can run using only those installed project files.
Do not overwrite existing files or modify a Power BI model.
```

Paths to the local `clones` folder vary by machine: **discover the actual path**.
If the current Cursor workspace is a parent multi-root workspace, identify the **specific
Power BI project** and confirm the target rather than installing into `clones`
or the Architect repository. If the Architect is not yet cloned, propose cloning
`https://github.com/GitKlink/performance-reward-dashboard-architect` first.

**Procedure:** [`.agents/skills/setup-power-bi-architect/SKILL.md`](.agents/skills/setup-power-bi-architect/SKILL.md).
Read the local file fully before proceeding.

## Expected project result

```text
<YOUR-OPEN-POWER-BI-PROJECT>/
├── .agents/
│   └── skills/
│       ├── <your existing skills>/              # untouched
│       └── dax-measure-standards-review/         # copied from Architect
│           ├── SKILL.md
│           ├── README.md
│           ├── scripts/review_measures.py
│           ├── references/
│           └── examples/measure-inventory.synthetic.csv
├── docs/
│   └── power-bi-architect/
│       ├── README.md
│       ├── installation.json                     # source SHA + file hashes
│       └── standards/
│           ├── source-manifest.json              # pinned standards file hashes
│           └── semantic-model/                   # copied canonical documents
└── <your existing PBIP/model/report files>      # untouched
```

The copied standards include the core, glossary, improvement backlog and **all seven
current domain documents**, keeping their original relative paths. The authoritative
standards repository remains
[GitKlink/power-bi-fabric-standards](https://github.com/GitKlink/power-bi-fabric-standards);
the project copy is an **installed, versioned snapshot**, not a second authoring home.

## Installation contract

- Use the **local Architect** checkout as installer source; do **not** fetch
  random GitHub content and paste it into project instructions.
- Use the **local Standards** repository at reviewed Git commit
  `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9` as standards source.
  A newer existing clone must be left intact; propose a separate pinned clone.
- Run the deterministic installer's **dry-run first**, show its output, then
  obtain approval before `--apply`.
- Copies are **new, additive files only**; existing project skills, docs,
  `AGENTS.md`, `.cursor/rules`, PBIP/TMDL, and model assets are preserved.
  Rerunning on an identical installation is a no-op. A changed or partial
  installation blocks instead of silently overwriting anything.
- The installer has no remote dependency beyond initially obtaining the
  two upstream clones with Git. No separate plugin or global CLI is installed.
- The DAX reviewer validates **all copied standards files against immutable
  Git blob hashes** pinned with the installed skill, plus the local manifest.
  No independent standards Git checkout is needed **after installation**.
- No confidential Power BI/DAX inventory or analysis report is committed
  to a public repository. Keep reports in a private folder.

Run these commands from the **local Architect checkout** after Cursor identifies
the real `<TARGET_PROJECT>` and `<PINNED_STANDARDS_CLONE>`:

```powershell
python scripts/install_into_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>"
# Review the displayed plan; ask for user approval before running:
python scripts/install_into_project.py --project "<TARGET_PROJECT>" --standards-repo "<PINNED_STANDARDS_CLONE>" --apply
```

## Verify the copied reviewer

Run from the **target Power BI project root**, using the harmless copied fixture
and a **new private report directory outside public repositories**:

```powershell
python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input ".agents/skills/dax-measure-standards-review/examples/measure-inventory.synthetic.csv" --standards-root "docs/power-bi-architect/standards" --domain variable_reward --out-dir "<PRIVATE_REPORTS_FOLDER>"
```

Confirm `review.json`, `review.md`, `status=partial_review_only`,
`schema_version=power-bi-fabric-architect-dax-measure-review-v1` and
`standards.verification=pinned_project_copy`. Check that Cursor's skills view
sees `dax-measure-standards-review` **when only the target project is open**.

After the synthetic test, Power BI Desktop's DAX Query View can export real measures:

```dax
EVALUATE INFO.VIEW.MEASURES()
```

Keep that CSV and any generated reports private. **Do not change the model**;
this capability only suggests human-reviewed measure improvements.

**Not yet installed by this procedure:** other Architect capabilities, the full
DAX/M Library, Microsoft Fabric skills, a plugin marketplace or a global CLI.
