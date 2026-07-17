---
artifact_id: CTRL-CORE-001
status: DRAFT
phase: 0
priority: critical
depends_on: []
blocks:
  - all repository implementation work
content_version: 0.3.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Authoritative build order

This file defines the development sequence for the Performance & Reward Dashboard Architect.

The sequence protects architectural dependencies without requiring every phase to complete a formal approval ceremony before useful development can continue. Comprehensive independent testing and approval occur before the first release.

## Development model

### During development

- `PLACEHOLDER` records planned scope only.
- `DRAFT` may be used by downstream development when its assumptions and limitations are visible.
- Automated validation runs continuously.
- Each phase performs only the checks needed to avoid building on an obviously broken foundation.
- Findings discovered through later implementation may revise earlier drafts.

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

## Phase 0 — Repository foundation

### Deliverables

1. Build order, dependency model, and status register
2. Naming, research, and citation standards
3. Artifact and source registers
4. Representative evidence and decision trials
5. Repository validation scripts, tests, and CI
6. Safe non-operational scaffold for later components

### Development gate

Phase 0 is provisionally complete when:

- the scaffold and control artifacts exist;
- standards are substantive drafts;
- representative trials have exercised the standards;
- known internal critical and major defects are resolved;
- dependency, source, link, and unit-test validation pass;
- placeholders cannot activate accidentally.

An independent Phase 0-only review is not required to begin Phase 1. The Phase 0 artifacts remain `DRAFT` and are included in the comprehensive pre-release review.

## Phase 1 — Architecture and authoring standards

Complete in this order:

1. `ARCH-CORE-001` — agent architecture
2. `ARCH-CORE-002` — context-management strategy
3. `ARCH-CORE-003` — skill-routing model
4. `ARCH-CORE-004` — repository information architecture
5. `ARCH-CORE-005` — release architecture
6. `STD-CORE-004` — skill-authoring standard
7. `STD-CORE-005` — example-authoring standard
8. `STD-CORE-006` — evaluation standard
9. `PLAN-CORE-001` — research program
10. `PLAN-CORE-002` — implementation roadmap
11. `PLAN-CORE-003` — release plan

### Development gate

The draft architecture must define component boundaries, context strategy, routing logic, source-of-truth ownership, skill format, evaluation approach, and release boundary clearly enough to support schemas and foundational skills.

Minimum checks:

- no obvious authority overlap or circular dependency;
- current Cursor claims use official evidence;
- three representative dashboard workflows can be traced through the architecture;
- placeholder runtime components remain disabled.

## Phase 2 — Schemas and templates

Create schemas before their templates:

1. Research record
2. Audience and decision profile
3. KPI definition
4. Dashboard brief
5. Page specification
6. Visual specification
7. Design review
8. Implementation handoff

### Development gate

- Schemas parse and validate representative records.
- Templates map to schema fields.
- Versioning and migration rules are explicit.
- At least one end-to-end draft workflow uses the contracts.

## Phase 3 — Audience and decision foundation

1. Audience archetypes
2. Decision modes
3. Consumption modes
4. Audience-specific knowledge
5. `audience-decision-framing`
6. `dashboard-discovery`
7. `grill-dashboard-requirements`

### Development gate

The agent can distinguish executive, Business Partner, people-manager, Reward Partner, and specialist needs and can select interactive, static, or hybrid consumption appropriately.

## Phase 4 — Holistic Performance & Reward foundation

1. Holistic value-driver tree
2. BAU scenarios
3. Non-BAU scenarios
4. Domain boundaries and shared terminology
5. KPI classification framework
6. Holistic Performance & Reward value-driver skill

### Development gate

The cross-domain value-driver model is coherent enough to prevent specialist packs from creating materially overlapping or contradictory definitions.

## Phase 5 — Specialist Performance & Reward domains

Develop:

- performance management;
- fixed reward;
- variable reward;
- market competitiveness;
- job architecture;
- pay equity;
- talent and retention;
- benefits and recognition;
- governance and controls.

Each domain pack includes:

- value-driver branch;
- business-question catalogue;
- KPI catalogue and calculation definitions;
- diagnostic patterns;
- audience-specific treatment;
- BAU and non-BAU use cases;
- governance risks and anti-patterns.

### Development gate

Each pack passes local evidence and metric-definition checks and works in at least one representative audience scenario. Full cross-domain contradiction testing occurs in Phase 12.

## Phase 6 — Consulting communication

Develop:

- technique catalogue;
- Pyramid Principle;
- SCQA;
- issue trees;
- action titles;
- executive storytelling;
- technique-selection matrix;
- corresponding skills.

### Development gate

The agent distinguishes published methodology, published examples, observed conventions, general practice, and project synthesis and selects techniques based on audience and decision.

## Phase 7 — Visual-design foundation

Develop:

- visual perception and hierarchy;
- Gestalt principles;
- preattentive processing;
- typography;
- colour;
- layout and grids;
- data-ink ratio;
- accessibility;
- corresponding skills.

### Development gate

Recommendations are evidence-grounded, accessible, audience-appropriate, and expressed as selection rules rather than universal aesthetic preferences.

## Phase 8 — Visualisation patterns

Develop:

- analytical-relationship map;
- chart-pattern catalogue;
- executive exhibit patterns;
- current IBCS guidance;
- visualisation anti-patterns;
- chart-selection and exhibit skills.

### Development gate

Each visual pattern identifies the analytical relationship, required data, audience, comparison logic, Power BI feasibility, and misuse conditions.

## Phase 9 — Dashboard experience

Develop:

- dashboard information architecture;
- guided versus exploratory design;
- interactive dashboard UX;
- static deck-style design;
- executive decision patterns;
- Business Partner diagnostic patterns;
- manager action patterns.

### Development gate

The agent produces materially different designs for executives, Business Partners, and managers rather than reskinning one report.

## Phase 10 — Power BI implementation

Develop:

- feasibility rules;
- interaction and export patterns;
- semantic-model and DAX patterns;
- performance guidance;
- security;
- accessibility;
- theme design.

### Development gate

Implementation guidance can realise the draft design architecture without obvious security, accessibility, performance, or export failures.

## Phase 11 — Orchestrator and subagents

Develop:

1. Main Cursor project rule
2. Repository-wide `AGENTS.md` only where it does not duplicate the project rule
3. Research synthesiser
4. Dashboard design critic
5. Power BI verifier
6. Evidence and authoring rules
7. Runtime quality gates

### Development gate

- Persistent instructions remain concise.
- Skill routing works across benchmark prompts.
- Subagent handoffs are bounded.
- No placeholder can be invoked accidentally.
- The source repository can generate the intended release package.

## Phase 12 — Comprehensive evaluation and correction

This is the main testing phase.

Run:

- independent architecture review;
- complete benchmark suite;
- automatic and explicit skill-routing tests;
- context-load and handoff tests;
- cross-skill contradiction and duplication analysis;
- executive, Business Partner, manager, specialist, interactive, and static scenarios;
- metric and calculation review;
- Power BI feasibility, security, accessibility, performance, and export review;
- evidence, citation, privacy, licensing, and public-repository review;
- regression testing after corrections.

### Gate

No critical failure remains. Major failures are resolved or explicitly accepted by the release authority. Runtime components and mandatory release dependencies are ready to move to `APPROVED`.

## Phase 13 — Integration and release

- Resolve release-blocking placeholders.
- Approve runtime components and mandatory dependencies.
- Validate artifact IDs, dependencies, schemas, sources, and links.
- Verify skill discovery and explicit invocation in current Cursor.
- Run the final benchmark and regression suite.
- Review package contents for confidential or licensed material.
- Produce the release manifest and migration notes.
- Prepare and tag `v0.1.0`.

## Status requirements

| Activity | Minimum status |
|---|---|
| Planning scope | `PLACEHOLDER` |
| Controlled authoring and prototyping | `DRAFT` |
| Formal review candidate | `IN REVIEW` |
| Runtime or mandatory release dependency | `APPROVED` |
| Public release | All included runtime artifacts and mandatory dependencies `APPROVED` |

## Review timing

Independent review is concentrated in Phase 12 and final release approval in Phase 13. Earlier independent review remains optional when a decision is high-risk, legally sensitive, security-sensitive, or difficult to reverse.
