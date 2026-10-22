# Set up the Power BI / Fabric Architect with an AI agent

**Entry point for Cursor Agent (local).** This is an *instruction-driven* setup, modelled on the approach of Matt Pocock's `setup-matt-pocock-skills`. You do **not** need to install a new CLI or run a remote script.

## Copy into Cursor Agent (local clones folder)

**Start from your local clone, not the GitHub page.** Open the directory containing your cloned repositories (for example, a folder named `clones`) in **local Cursor**. Locate the actual Architect checkout at `<LOCAL_CLONES_FOLDER>/performance-reward-dashboard-architect/`.

Paste this prompt into Cursor Agent when the **clones folder** is open:

```text
Read the LOCAL file performance-reward-dashboard-architect/SETUP.md
from my open clones folder and follow the LOCAL instructions in
performance-reward-dashboard-architect/.agents/skills/setup-power-bi-architect/SKILL.md.

Set up the Power BI / Fabric Architect for a read-only DAX Measure Standards Review.
Inspect the local repositories first. Show proposed changes and obtain my approval
before applying them. Reuse existing clones, verify the pinned standards revision,
confirm skill discovery, and run synthetic tests. Do not modify Power BI models or
publish my measure inventory.
```

If you opened the **Architect repository itself** as the Cursor workspace root instead of its parent `clones` folder, the paths above are `SETUP.md` and `.agents/skills/setup-power-bi-architect/SKILL.md`.

Cursor can also reference the file as `@SETUP.md` when the Architect repository is the open workspace and the file mention resolves correctly. If your clones live somewhere else, point the agent at the **actual local absolute path**; do not assume a particular drive or home directory.

**Canonical agent procedure:** [`.agents/skills/setup-power-bi-architect/SKILL.md`](.agents/skills/setup-power-bi-architect/SKILL.md). Read it fully from the same local checkout before making changes. If the Architect repository is **not cloned yet**, only then use the [public GitHub source](https://github.com/GitKlink/performance-reward-dashboard-architect) to obtain it, open the local clone in Cursor, and continue from these local instructions.

## What the AI should do

1. **Inspect** existing Cursor workspace, Git/Python availability, project folder and relevant clones; do not assume a blank machine.
2. **Propose** local paths and the minimum changes needed; ask for approval before cloning repositories, switching revisions, creating workspace files or touching project folders.
3. **Resolve sources** without overwriting anything:
   - Architect (this repository): `https://github.com/GitKlink/performance-reward-dashboard-architect`, containing the skill and checker.
   - Canonical engineering standards: `https://github.com/GitKlink/power-bi-fabric-standards`. The current DAX reviewer requires Git commit **`2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`**. Use a **separate pinned clone** if an existing checkout is on a newer revision.
   - DAX/M Library: `https://github.com/GitKlink/dax-m-query-library`, **not needed for the first measure review**.
4. **Verify** the Git revision and committed standards files using the checker's existing source-verification logic. Make the Architect skill visible by opening the Architect repository in Cursor; for a real Power BI project, a **local multi-root workspace** can include Architect, standards and the PBIP folder. Verify skill discovery in Cursor rather than assuming it.
5. **Test** the checker using existing synthetic CSV and Python unit tests. Produce reports only in a private/local directory outside public repositories.
6. **Pilot** real measures only after the synthetic test: run `EVALUATE INFO.VIEW.MEASURES()` in Power BI DAX Query View, export CSV privately and run the **read-only** reviewer. An approval table may be proposed, but *no model edits* are permitted by this setup.

## Scope

- **Works toward:** local Cursor + Python 3.10+ + Git, a public Architect repository, public canonical standards pinned to the verified revision and an optional PBIP project.
- **Does not install:** a global CLI, package/plugin marketplace, Fabric environment, Microsoft tools, enterprise data access or cloud/CI integration.
- **Privacy:** Power BI measure metadata, exported expressions and generated reports can contain proprietary business logic. Never commit them to any public repository.
- **Status:** the setup instructions are source-controlled and testable for consistency. Only your local execution can prove that Cursor discovered the skill and that your actual Power BI export works.

See also [DAX Measure Reviewer quick start](.agents/skills/dax-measure-standards-review/README.md), [check coverage](.agents/skills/dax-measure-standards-review/references/check-coverage.md), and the official [Cursor skills documentation](https://cursor.com/docs/skills).

**Naming:** Power BI / Fabric Architect is the product. "Wayfinder" means Matt Pocock's historical planning skill, not our product.
