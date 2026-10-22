# Power BI / Fabric Architect

A Cursor-first, composed analytics-engineering capability for building and reviewing Power BI/Fabric analytical products. The project coordinates engineering policy, Performance & Reward domain meaning, reusable native implementations, and Microsoft-maintained platform skills without copying their canonical sources.

## First implementation: DAX Measure Standards Reviewer (MVP)

**Status: first reviewer merged / local pilot pending**, not a complete Architect implementation or a certified DAX conformance tool.

- [Skill and usage guide](.agents/skills/dax-measure-standards-review/README.md)
- [Agent Skill instructions](.agents/skills/dax-measure-standards-review/SKILL.md)
- [Coverage and limitations](.agents/skills/dax-measure-standards-review/references/check-coverage.md)
- [Synthetic example inventory](examples/dax-measure-review/measure-inventory.synthetic.csv)

This first read-only workflow checks a **CSV measure inventory** (exported with `EVALUATE INFO.VIEW.MEASURES()`) for a limited set of naming/metadata findings, then produces Markdown/JSON reports for a human-reviewed refactor proposal. It does **not** edit the model, compile DAX, understand all business metrics, or prove full standards conformance. Real model and private Git access tests remain to be completed.

## Repository authorities

- **[Engineering Standards](https://github.com/GitKlink/power-bi-fabric-standards)** — public canonical Power BI/Fabric engineering-policy repository. Access is permission-controlled.
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
