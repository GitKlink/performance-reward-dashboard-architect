---
artifact_id: CTRL-CORE-001
status: DRAFT
phase: 0
priority: critical
depends_on: []
blocks:
  - all repository implementation work
content_version: 0.4.0
last_reviewed: 2026-07-31
next_review: 2026-08-31
---

# Authoritative build order

This file defines the development sequence for the Performance & Reward Dashboard Architect.

The repository's durable differentiation is Performance & Reward decision, process, metric, control, and data-model knowledge. Generic Power BI capability should be integrated from maintained Microsoft skills where suitable rather than recreated without a domain-specific reason.

The sequence protects architectural dependencies without requiring every phase to complete a formal approval ceremony before useful development can continue. Comprehensive independent testing and approval occur before the first release.

## Development model

### During development

- `PLACEHOLDER` records planned scope only.
- `DRAFT` may be used by downstream development when its assumptions and limitations are visible.
- Automated validation runs continuously.
- Each phase performs only the checks needed to avoid building on an obviously broken foundation.
- Findings discovered through later implementation may revise earlier drafts.
- Domain-first vertical slices may proceed once the minimum schema, routing, and authoring controls they need are available.
- Generic Power BI guidance is expanded only where Microsoft skills do not provide adequate capability or where Performance & Reward constraints materially alter the answer.

### Before release

- Runtime components and their mandatory dependencies must reach `APPROVED`.
- Independent architecture, evidence, security, privacy, accessibility, and release reviews must be complete.
- The complete benchmark and regression suite must pass.

## Gate rules

1. `PLACEHOLDER` does not provide substantive authority.
2. `DRAFT` is sufficient for controlled downstream authoring and prototyping.
3. A downstream artifact must identify material assumptions inherited from a draft dependency.
4. Automated repository validation must remain green while development continues.
5. No `PLACEHOLDER` may be activated as a Cursor rule, skill, subagent, command, or release dependency.
6. `APPROVED` is required for the release package, not for every intermediate development step.
7. Critical defects return to the owning upstream artifact rather than being hidden in local workarounds.
8. `ARTIFACT-REGISTER.yaml`, `DEPENDENCIES.md`, and `STATUS.md` must remain consistent.
9. Microsoft Power BI skills are treated as external implementation capabilities, not as authority for Performance & Reward business definitions.
10. Domain definitions, calculations, grain rules, governance constraints, and decision logic remain repository-owned even when implementation is delegated.

## Phase 0 — Minimum operating foundation

### Deliverables

1. Build order, dependency model, and status register
2. Naming, research, citation, skill-authoring, example-authoring, and evaluation standards
3. Artifact and source registers
4. Agent architecture, context-management strategy, and skill-routing model
5. Minimum schemas and templates required for domain authoring
6. Repository validation scripts, tests, and CI
7. Safe non-operational scaffold for later components

### Development gate

Phase 0 is provisionally complete when:

- the scaffold and control artifacts exist;
- core standards and architecture are substantive drafts;
- KPI, audience, research, dashboard-brief, and implementation-handoff contracts can support domain work;
- representative trials have exercised the standards;
- known internal critical and major defects are resolved;
- dependency, source, link, and schema validation pass;
- placeholders cannot activate accidentally.

Phase 0 is intentionally narrower than the previous architecture-first programme. Repository information architecture, release detail, and secondary templates may continue in parallel when they do not block domain authoring.

## Phase 1 — Performance & Reward ontology and shared foundation

Complete in this order:

1. Domain boundaries and shared terminology
2. Business-process and decision map
3. Holistic value-driver tree
4. KPI classification framework
5. Grain, effective-dating, population, and time conventions
6. Cross-domain relationship map
7. Sensitivity, privacy, governance, and control classification
8. BAU and non-BAU scenario catalogue
9. Holistic Performance & Reward value-driver skill

### Development gate

The shared ontology must be coherent enough to prevent specialist packs from creating materially overlapping or contradictory definitions.

Minimum checks:

- every core concept has an owner and definition;
- decision points connect to processes, measures, audiences, and data grain;
- point-in-time, period, event, and lifecycle concepts are distinguishable;
- sensitive remuneration and performance concepts have explicit handling rules;
- three representative workflows can trace from business question to data and decision.

## Phase 2 — Core specialist Performance & Reward domains

Develop in priority order:

1. fixed reward;
2. variable reward;
3. performance management;
4. job architecture;
5. market competitiveness;
6. governance and controls;
7. pay equity;
8. talent and retention;
9. benefits and recognition.

Each domain pack includes:

- domain purpose and boundaries;
- business-process and decision map;
- value-driver branch;
- business-question catalogue;
- KPI catalogue and calculation definitions;
- canonical entities, grain, and dimensional-model patterns;
- effective-dating and point-in-time implications;
- diagnostic patterns;
- audience-specific interpretation;
- BAU and non-BAU use cases;
- cross-domain dependencies;
- Power BI implementation implications;
- governance risks, contradiction rules, and anti-patterns.

### Development gate

Each pack passes local evidence and metric-definition checks, identifies its data and governance requirements, and works in at least one representative decision scenario. Full cross-domain contradiction testing occurs in Phase 8.

## Phase 3 — Domain workflows and product archetypes

Build end-to-end vertical slices for:

1. pre-EOY salary and bonus planning;
2. manager salary review;
3. performance outcome reporting;
4. fixed-reward budget allocation;
5. variable-reward calibration;
6. market-data and benchmark-cycle analysis;
7. job-architecture diagnostics;
8. executive remuneration reporting;
9. pay-equity investigation;
10. reward governance and control monitoring.

Each vertical slice should exercise:

- discovery and business framing;
- audience and decision requirements;
- ontology and specialist-domain routing;
- KPI definitions;
- canonical data grain and semantic model;
- page and visual specification;
- implementation handoff;
- control, privacy, and validation rules.

### Development gate

At least three priority workflows produce coherent end-to-end outputs and expose any missing schema, routing, or domain-definition requirements.

## Phase 4 — Performance & Reward audiences and decision treatment

Develop role-specific knowledge for:

- Group Executives and executives;
- People Leaders;
- HR Business Partners;
- Reward Partners;
- Performance Partners;
- Executive Reward;
- People Analytics and reporting specialists;
- Governance, Risk, and Control;
- Payroll and HRIS operational users.

Retain only the generic audience concepts required to support these roles:

- decision modes;
- consumption modes;
- interactive, static, and hybrid delivery;
- audience-decision framing;
- dashboard discovery;
- requirements challenge and validation.

### Development gate

The agent produces materially different decision framing, measures, explanations, controls, and delivery patterns for Performance & Reward roles rather than reskinning one generic report.

## Phase 5 — Microsoft Power BI skill integration

Develop:

1. Microsoft skill inventory and capability map;
2. overlap assessment against repository placeholders and planned skills;
3. delegation and fallback rules;
4. domain-context injection contract;
5. domain-constraint override rules;
6. output verification rules;
7. version and change-monitoring approach;
8. explicit gap register.

### Development gate

For each generic Power BI capability, the repository can identify whether to delegate, supplement, override, or retain locally. Delegation must not transfer ownership of business definitions, calculations, controls, or domain semantics.

## Phase 6 — Performance & Reward-specific Power BI implementation

Develop only the implementation knowledge where domain requirements materially change the design:

- employee, employment, position, job, organisation, and remuneration history;
- effective dating and slowly changing dimensions;
- position-of-record and point-in-time modelling;
- pre-outcome versus outcome models;
- remuneration review and pay-element facts;
- budget, allocation, recommendation, and outcome facts;
- local-currency and reporting-currency treatment;
- management, HR-partner, and specialist security hierarchies;
- sensitive remuneration and performance data controls;
- snapshot, movement, event, and lifecycle analysis;
- reconciliation, auditability, export, and offline-distribution risks;
- non-technical consumer semantic-model design.

Generic DAX, visual selection, accessibility, performance optimisation, theme design, and ordinary interactions should normally use Microsoft skills unless a documented gap or domain constraint requires local guidance.

### Development gate

Implementation guidance can realise the priority domain workflows without obvious grain, history, security, privacy, reconciliation, performance, accessibility, or export failures.

## Phase 7 — Domain communication and visual patterns

Consolidate the previous consulting, visual-design, visualisation, and dashboard-experience phases into a domain-focused layer.

Develop only what materially improves Performance & Reward decisions:

- issue trees and value-driver communication;
- Pyramid Principle, SCQA, action titles, and executive storytelling;
- high-data-to-ink executive exhibits;
- comparison, distribution, movement, exception, and allocation patterns;
- executive, Business Partner, Reward Partner, and manager page patterns;
- static versus interactive decision products;
- domain-specific visual and interpretation anti-patterns;
- accessibility and disclosure controls for sensitive data.

### Development gate

Recommendations are evidence-grounded, decision-specific, accessible, and materially different by audience and domain. Generic chart catalogues or aesthetic guidance do not block progress.

## Phase 8 — Orchestration, comprehensive evaluation, and correction

Develop and test:

1. Main Cursor project rule
2. Repository-wide `AGENTS.md` only where it does not duplicate the project rule
3. Research synthesiser
4. Dashboard design critic
5. Power BI verifier
6. Evidence and authoring rules
7. Runtime quality gates
8. Complete benchmark suite
9. Automatic and explicit skill-routing tests
10. Context-load and handoff tests
11. Cross-skill contradiction and duplication analysis
12. Executive, Business Partner, manager, specialist, interactive, and static scenarios
13. Metric and calculation review
14. Power BI feasibility, security, accessibility, performance, and export review
15. Evidence, citation, privacy, licensing, and public-repository review
16. Regression testing after corrections

### Gate

No critical failure remains. Major failures are resolved or explicitly accepted by the release authority. Runtime components and mandatory release dependencies are ready to move to `APPROVED`.

## Phase 9 — Integration and release

- Resolve release-blocking placeholders.
- Approve runtime components and mandatory dependencies.
- Validate artifact IDs, dependencies, schemas, sources, and links.
- Verify skill discovery and explicit invocation in current Cursor.
- Verify Microsoft Power BI skill delegation and fallback behaviour.
- Run the final benchmark and regression suite.
- Review package contents for confidential or licensed material.
- Produce the release manifest and migration notes.
- Prepare and tag `v0.1.0`.

## Deprioritised generic content

The following may remain placeholders, thin reference layers, or integration notes until a documented domain need exists:

- generic executive archetypes;
- broad consulting-method summaries;
- generic visual-perception explainers;
- broad chart catalogues;
- generic Power BI feasibility guidance;
- generic DAX and semantic-model guidance;
- ordinary dashboard UX patterns;
- generic accessibility, performance, and theme guidance already covered by maintained Microsoft skills.

## Status requirements

| Activity | Minimum status |
|---|---|
| Planning scope | `PLACEHOLDER` |
| Controlled authoring and prototyping | `DRAFT` |
| Formal review candidate | `IN REVIEW` |
| Runtime or mandatory release dependency | `APPROVED` |
| Public release | All included runtime artifacts and mandatory dependencies `APPROVED` |

## Review timing

Independent review is concentrated in Phase 8 and final release approval in Phase 9. Earlier independent review remains optional when a decision is high-risk, legally sensitive, security-sensitive, or difficult to reverse.
