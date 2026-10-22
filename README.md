# Power BI / Fabric Architect

A Cursor-first, composed analytics-engineering capability for building and reviewing Power BI/Fabric analytical products. The project coordinates engineering policy, Performance & Reward domain meaning, reusable native implementations, and Microsoft-maintained platform skills without copying their canonical sources.

## Install into an existing Power BI project

The Architect is **installed as version-pinned copies inside your current project**:
the DAX reviewer goes under whichever project skill root already exists,
`.agents/skills/` or `.cursor/skills/`, in the `dax-measure-standards-review/` subfolder. Copied canonical
documents go under `docs/power-bi-architect/standards/semantic-model/`.
The source repositories do **not** need to remain open in Cursor afterwards.

**[AI-readable setup instructions](SETUP.md)** explain the safe
**inspect → dry-run → user approval → project-local copy → verify** flow.
The [`setup-power-bi-architect` skill](.agents/skills/setup-power-bi-architect/SKILL.md)
and deterministic [project installer](scripts/install_into_project.py) implement it.

Paste into **Cursor Agent**, with the actual Power BI project open:
`Read the LOCAL clones/performance-reward-dashboard-architect/SETUP.md, inspect my current Power BI project, propose a project-local installation, and ask my approval before copying any skills or standards.`
Cursor must discover the real `clones` directory rather than assume a
drive/path. Existing skills, docs, AGENTS.md and model files remain untouched.

The first packaged capability is the read-only DAX measure reviewer.
No global CLI, plugin marketplace, Microsoft Fabric skill bundle or automatic
updater is installed. Source documents stay authoritative upstream; the
installed copies are pinned snapshots with integrity/provenance manifests.

## First implementation: DAX Measure Standards Reviewer (MVP)

**Status: first reviewer merged / local pilot pending**, not a complete Architect implementation or a certified DAX conformance tool.

- [Skill and usage guide](.agents/skills/dax-measure-standards-review/README.md)
- [Agent Skill instructions](.agents/skills/dax-measure-standards-review/SKILL.md)
- [Coverage and limitations](.agents/skills/dax-measure-standards-review/references/check-coverage.md)
- [Synthetic example inventory](examples/dax-measure-review/measure-inventory.synthetic.csv)

This first read-only workflow checks a **CSV measure inventory** (exported with `EVALUATE INFO.VIEW.MEASURES()`) for a limited set of naming/metadata findings, then produces Markdown/JSON reports for a human-reviewed refactor proposal. It does **not** edit the model, compile DAX, understand all business metrics, or prove full standards conformance. Local Cursor discovery and real-model integration still require a user pilot; source checkout and installed-copy synthetic verification are CI-tested.

## Repository authorities

- **[Engineering Standards](https://github.com/GitKlink/power-bi-fabric-standards)** — public canonical Power BI/Fabric engineering-policy repository. Reviewers pin a checked commit.
- **[DAX/M Query Library](https://github.com/GitKlink/dax-m-query-library)** — reusable native DAX, Power Query M, Python and Deneb implementations, distinct from normative standards.
- **Architect (this repo)** — integration, orchestration, skills, proposed architecture, future validators.
- **Domain authority** — Performance & Reward business definitions, eligibility, grain, interpretation and reconciliation. Business/content boundary issue [#6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6) remains distinct from generic semantic formatting.

## Architecture research

- [R1–R8 evidence index](research/cursor-architecture/README.md)
- [R8 proposed target architecture](research/cursor-architecture/08-target-architecture.md)
- [ADR-0001 — canonical standards home](docs/decisions/0001-canonical-standards-home.md)

Research and architecture proposals are not themselves enforcement or deployed agents. Development follows small, validated Power BI slices rather than building an installer/plugin ecosystem first.

## Naming and historical research

This project is the **Power BI / Fabric Architect** (repository: `performance-reward-dashboard-architect`). **Wayfinder** refers only to Matt Pocock's planning skill used in the architecture research. It is not the name of this product, installer, agent or report schema. The `research/cursor-architecture/` files include a dated terminology correction to preserve the original research trail.
