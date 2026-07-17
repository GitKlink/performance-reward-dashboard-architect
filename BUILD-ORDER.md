---
artifact_id: CTRL-CORE-001
status: DRAFT
phase: 0
priority: critical
depends_on: []
blocks:
  - all repository implementation work
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Authoritative Build Order

This file defines the mandatory sequence for researching, authoring, validating, and releasing the Performance & Reward Dashboard Architect.

A later phase may be explored for planning, but no dependent artifact may be treated as authoritative or activated in Cursor until its prerequisite gate is satisfied.

## Gate rules

1. `PLACEHOLDER` never satisfies a dependency.
2. `DRAFT` may support prototyping only where this file explicitly permits it.
3. `IN REVIEW` may support controlled evaluation but not release.
4. `APPROVED` is required for release dependencies.
5. A dependent artifact must use the current approved version of each prerequisite.
6. Work that reveals a flawed prerequisite returns to the earlier phase rather than adding local workarounds.
7. Status and dependencies must agree with `ARTIFACT-REGISTER.yaml` and `DEPENDENCIES.md`.

## Phase 0 — Repository controls

Complete in this order:

1. `CTRL-CORE-001` — `BUILD-ORDER.md`
2. `CTRL-CORE-002` — `DEPENDENCIES.md`
3. `CTRL-CORE-003` — `STATUS.md`
4. `STD-CORE-001` — `docs/standards/naming-standard.md`
5. `STD-CORE-002` — `docs/standards/research-standard.md`
6. `STD-CORE-003` — `docs/standards/citation-standard.md`
7. `CTRL-CORE-004` — `ARTIFACT-REGISTER.yaml`

### Current Phase 0 state

- Initial scaffold: complete on `scaffold/repository-foundation`
- Naming standard: `DRAFT`
- Research standard: `DRAFT`
- Citation standard: `DRAFT`
- Artifact register: `DRAFT`

### Phase 0 gate

Phase 0 is complete when:

- control files and standards have immutable artifact IDs;
- status and dependency records agree;
- naming, research, and citation standards pass representative trials;
- identified scaffold naming migrations are recorded;
- internal-link and dependency validation requirements are implementable;
- the control artifacts are independently reviewed and marked `APPROVED`.

## Phase 1 — Architecture and authoring standards

Complete in this order:

1. `ARCH-CORE-001` — agent architecture
2. `ARCH-CORE-002` — context-management strategy
3. `ARCH-CORE-003` — skill-routing model
4. `ARCH-CORE-004` — information architecture
5. `ARCH-CORE-005` — release architecture
6. `STD-CORE-004` — skill-authoring standard
7. `STD-CORE-005` — example-authoring standard
8. `STD-CORE-006` — evaluation standard
9. `PLAN-CORE-001` — research program
10. `PLAN-CORE-002` — implementation roadmap
11. `PLAN-CORE-003` — release plan

### Phase 1 gate

Component boundaries, context strategy, source-of-truth rules, routing logic, skill format, evaluation principles, and release boundaries are approved.

## Phase 2 — Schemas and templates

Complete schemas before templates:

1. Research record
2. Audience and decision profile
3. KPI definition
4. Dashboard brief
5. Page specification
6. Visual specification
7. Design review
8. Implementation handoff

Complete the corresponding template only after its schema reaches `IN REVIEW`.

### Phase 2 gate

Schemas validate, templates map one-to-one to schema fields, and migration/version rules are defined.

## Phase 3 — Audience and decision foundation

1. Audience archetypes
2. Decision modes
3. Consumption modes
4. Audience-specific knowledge files
5. `audience-decision-framing`
6. `dashboard-discovery`
7. `grill-dashboard-requirements`

### Phase 3 gate

The agent can distinguish executive, Business Partner, people-manager, Reward Partner, and specialist needs; identify the decision mode; and select interactive, static, or hybrid consumption appropriately.

## Phase 4 — Holistic Performance & Reward foundation

1. Holistic value-driver tree
2. BAU scenarios
3. Non-BAU scenarios
4. Domain boundaries and shared terminology
5. KPI classification framework
6. Holistic Performance & Reward value-driver skill

### Phase 4 gate

The cross-domain value-driver architecture is approved and specialist domain boundaries do not materially overlap or conflict.

## Phase 5 — Specialist P&R domain packs

Research and complete:

- Performance management
- Fixed reward
- Variable reward
- Market competitiveness
- Job architecture
- Pay equity
- Talent and retention
- Benefits and recognition
- Governance and controls

Each pack must include:

- value-driver branch;
- business-question catalogue;
- KPI catalogue;
- calculation definitions;
- diagnostic patterns;
- audience-specific treatment;
- BAU use cases;
- non-BAU use cases;
- governance risks and anti-patterns.

### Phase 5 gate

Each domain pack passes evidence review, metric-definition review, overlap review, and at least two audience-specific benchmark tests.

## Phase 6 — Consulting communication

1. Technique catalogue
2. Pyramid Principle
3. SCQA
4. Issue trees
5. Action titles
6. Executive storytelling
7. Technique-selection matrix
8. Corresponding Cursor skills

### Phase 6 gate

The agent can distinguish published methodology, published examples, observed conventions, general consulting practice, and project synthesis, then select techniques based on audience and decision rather than aesthetics.

## Phase 7 — Visual-design foundation

1. Visual perception and hierarchy
2. Gestalt principles
3. Preattentive processing
4. Typography
5. Colour
6. Layout and grids
7. Data-ink ratio
8. Accessibility
9. Corresponding skills

### Phase 7 gate

Visual recommendations are evidence-grounded, accessible, audience-appropriate, and expressed as selection rules rather than universal style preferences.

## Phase 8 — Visualisation patterns

1. Analytical-relationship map
2. Chart-pattern catalogue
3. Executive exhibit patterns
4. IBCS standard
5. Visualisation anti-patterns
6. Chart-selection and exhibit skills

### Phase 8 gate

Every visual pattern identifies the analytical relationship, required data, appropriate audience, comparison logic, Power BI feasibility, and misuse conditions.

## Phase 9 — Dashboard experience

1. Information architecture
2. Guided versus exploratory design
3. Interactive dashboard UX
4. Static deck-style design
5. Executive decision patterns
6. Business Partner diagnostic patterns
7. Manager action patterns

### Phase 9 gate

The agent can design distinct information architectures for executives, Business Partners, and managers rather than reskinning one report.

## Phase 10 — Power BI implementation

1. Feasibility rules
2. Interaction patterns
3. Static export patterns
4. Semantic-model patterns
5. DAX patterns
6. Performance patterns
7. Security
8. Accessibility
9. Theme design

### Phase 10 gate

Implementation guidance supports the approved design architecture and passes feasibility, security, accessibility, performance, and export review.

## Phase 11 — Orchestrator and subagents

1. Main Cursor project rule
2. Repository-wide `AGENTS.md`
3. Research synthesiser
4. Dashboard design critic
5. Power BI verifier
6. Evidence and authoring rules
7. Quality gates

### Phase 11 gate

Persistent rules are concise, skill routing is reliable, subagent handoffs are bounded, and no placeholder component can be invoked accidentally.

## Phase 12 — Evaluation and validation

1. Evaluation rubric
2. Benchmark scenarios
3. Expected results
4. Validation scripts
5. Regression process
6. Release criteria

### Phase 12 gate

The agent passes the agreed benchmark suite with no critical audience, metric, evidence, visual, accessibility, or implementation failures.

## Phase 13 — Integration and release

- Resolve release-blocking placeholders.
- Validate artifact IDs, dependencies, schemas, and internal links.
- Verify skill discovery and explicit invocation.
- Run benchmark scenarios and regression tests.
- Review the public package for confidential or licensed material.
- Prepare and tag `v0.1.0`.

## Minimum status required to unblock dependants

| Artifact class | Prototyping | Release dependency |
|---|---|---|
| Controls and standards | `IN REVIEW` | `APPROVED` |
| Architecture | `IN REVIEW` | `APPROVED` |
| Schemas | `IN REVIEW` | `APPROVED` |
| Knowledge packs | `DRAFT` where explicitly authorised | `APPROVED` |
| Skills | `DRAFT` in controlled testing | `APPROVED` |
| Examples | `DRAFT` | `APPROVED` when shipped publicly |
| Evaluations | `DRAFT` for test development | `APPROVED` for release gates |
