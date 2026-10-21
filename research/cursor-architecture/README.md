# Cursor Architecture Research Programme

This directory stores durable research evidence for Wayfinder's Power BI / Fabric Architect ecosystem. Canonical engineering-standard ownership was already settled by [ADR-0001](../../docs/decisions/0001-canonical-standards-home.md) and closed [Issue #5](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/5). This programme now supports review of the **implementation architecture**, not reopening the standards-home decision.

Research artifacts are **evidence and analysis, not normative standards**. Architecture decisions and standards should cite or consume this research rather than treating the research files themselves as binding policy.

## Research tickets — checked 2026-10-22

Research status below distinguishes a document present on `main` from its tracking issue's state. Source snapshots and merge dates are not the same thing. A draft PR is **not** an approved architecture decision.

| Research | Issue | Wave | Durable artifact | Evidence date | Status at this snapshot | Decision consumer |
|---|---|---:|---|---|---|---|
| R1 — Cursor native primitives | [#10](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/10) | 1 | [01-cursor-primitives.md](01-cursor-primitives.md) | 2026-09-16 | Artifact on `main`; tracking issue open | R2, R4, R7, R8 |
| R2 — Harness/agent/skill/plugin | [#12](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/12) | 2 | [02-harness-agent-skill-plugin.md](02-harness-agent-skill-plugin.md) | 2026-09 | Artifact on `main`; tracking issue open | R5, R8 |
| R3 — Reference benchmark | [#11](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/11) | 1 | [03-reference-repo-benchmark.md](03-reference-repo-benchmark.md) | 2026-09-16 | Artifact on `main`; tracking issue open | R2, R4, R5, R6, R7, R8 |
| R4 — Cross-repository composition | [#13](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/13) | 2 | [04-cross-repo-composition.md](04-cross-repo-composition.md) | 2026-10-19 | Merged PR #23; issue closed | R5, R6, R8, implementation |
| R5 — Installation/bootstrap | [#15](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/15) | 3 | [05-installation-bootstrap.md](05-installation-bootstrap.md) | 2026-10-19 | Merged PR #25; issue closed | R8, bootstrap design |
| R6 — Standards/library packaging | [#16](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/16) | 3 | [06-standards-library-packaging.md](06-standards-library-packaging.md) | 2026-09; corrected 2026-10-22 | Merged PR #19; issue closed; **§20 native asset correction controls** | R8, catalogue/release design |
| R7 — Cross-agent portability | [#14](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/14) | 2 | [07-cross-agent-portability.md](07-cross-agent-portability.md) | 2026-10-19 | Merged PR #24; issue closed | R5, R8, host adapters |
| R8 — Target architecture synthesis | [#17](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/17) | 4 | [08-target-architecture.md](08-target-architecture.md) | 2026-10-22 | **Proposed in review branch; not approved or implemented** | New target-architecture ADR and pilot backlog |

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
- R8 — synthesise R1–R7 into a reviewable proposed target architecture for a **new implementation ADR**. The repository home is already settled in ADR-0001 and #5 remains closed.

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

- **Settled foundation:** [ADR-0001](../../docs/decisions/0001-canonical-standards-home.md) / [Issue #5](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/5) — repository authority; not reopened by R8.
- **Current synthesis:** [R8 / Issue #17](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/17) — proposed composed Cursor-first implementation architecture.
- **Next decision:** a separate target-architecture ADR to accept/revise R8's proposed choices (new approval; not issued by the research merge).
- **Related scope:** [#6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6) business meaning vs semantic representation; [#7](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/7) semantic taxonomy; [#8](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/8) M standards.
- **Implementation:** future PBIP pilot, independent QA, bootstrap/dependency-manifest and cross-agent adapter tickets. None is implemented by research alone.

## R3 fixed reference corpus

R3 must review these six repositories:

1. `cursor/plugins`
2. `cursor/plugin-template`
3. `microsoft/skills-for-fabric`
4. `mattpocock/skills`
5. `addyosmani/agent-skills`
6. `github/spec-kit`

Additional repositories are optional follow-up references only when one of the six leaves a specific research question unresolved.
