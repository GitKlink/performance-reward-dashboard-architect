# Cursor Architecture Research Programme

This directory stores the durable research evidence used to resolve Wayfinder #5 and related architecture decisions for the Power BI / Fabric Architect ecosystem.

Research artifacts are **evidence and analysis, not normative standards**. Architecture decisions and standards should cite or consume this research rather than treating the research files themselves as binding policy.

## Research tickets

| Research | GitHub issue | Wave | Durable artifact | Status |
|---|---:|---:|---|---|
| R1 — Cursor native architecture primitives | #10 | 1 | `01-cursor-primitives.md` | Planned |
| R2 — Harness vs agent vs skill vs plugin architecture | #12 | 2 | `02-harness-agent-skill-plugin.md` | Planned |
| R3 — Reference implementation benchmark | #11 | 1 | `03-reference-repo-benchmark.md` | Planned |
| R4 — Cross-repository composition | #13 | 2 | `04-cross-repo-composition.md` | Planned |
| R5 — Installation and bootstrap architecture | #15 | 3 | `05-installation-bootstrap.md` | Planned |
| R6 — Standards and reusable library packaging | #16 | 3 | `06-standards-library-packaging.md` | Planned |
| R7 — Cross-agent portability | #14 | 2 | `07-cross-agent-portability.md` | Planned |
| R8 — Target architecture synthesis | #17 | 4 | `08-target-architecture.md` | Planned |

## Execution order

### Wave 1
- R1 — establish Cursor-native primitives and boundaries.
- R3 — benchmark six reference implementations.

### Wave 2
- R2 — classify the architecture using R1/R3 evidence.
- R4 — decide how multiple repositories compose during development and consumption.
- R7 — define the Cursor-first / cross-agent portability boundary.

### Wave 3
- R5 — determine installer/bootstrap architecture.
- R6 — determine standards and reusable-library packaging and loading.

### Wave 4
- R8 — synthesize R1–R7 into an implementable target architecture and feed the result back into Wayfinder #5.

## Research discipline

Each research artifact should contain:

1. Research question and scope
2. Sources and evidence
3. Observed patterns
4. Pros / cons and trade-offs
5. Implications for this project
6. Recommendation
7. Unresolved questions

Where later research depends on earlier work, it should read the stored artifact from this directory rather than relying on chat history.

## Primary decision consumers

- Wayfinder #5 — canonical home for analytics engineering standards
- Future implementation tickets for the Architect harness/plugin/skills
- Standards packaging and distribution decisions
- Cross-repository composition and installer/bootstrap decisions

## R3 fixed reference corpus

R3 must review these six repositories:

1. `cursor/plugins`
2. `cursor/plugin-template`
3. `microsoft/skills-for-fabric`
4. `mattpocock/skills`
5. `addyosmani/agent-skills`
6. `github/spec-kit`

Additional repositories are optional follow-up references only when one of the six leaves a specific research question unresolved.
