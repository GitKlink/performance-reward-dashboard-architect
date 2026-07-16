---
status: DRAFT
phase: 0
priority: critical
depends_on: []
blocks:
  - all repository implementation work
last_reviewed: 2026-07-17
---

# Authoritative Build Order

This file defines the sequence for researching, authoring, validating, and releasing the Performance & Reward Dashboard Architect. Work must not begin on a dependent artifact until its prerequisite has reached the minimum required status.

## Phase 0 — Repository controls

Complete first:

1. `BUILD-ORDER.md`
2. `DEPENDENCIES.md`
3. `STATUS.md`
4. `docs/standards/naming-standard.md`
5. `docs/standards/research-standard.md`
6. `docs/standards/citation-standard.md`

**Gate:** repository controls reviewed and dependency identifiers stable.

## Phase 1 — Architecture and authoring standards

1. `docs/architecture/agent-architecture.md`
2. `docs/architecture/context-management-strategy.md`
3. `docs/architecture/skill-routing-model.md`
4. `docs/architecture/information-architecture.md`
5. `docs/standards/skill-authoring-standard.md`
6. `docs/standards/example-authoring-standard.md`
7. `docs/standards/evaluation-standard.md`

**Gate:** component boundaries, source-of-truth rules, and skill format approved.

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

**Gate:** schemas validate and templates map one-to-one to schema fields.

## Phase 3 — Audience and decision foundation

1. Audience archetypes
2. Decision modes
3. Consumption modes
4. Audience-specific knowledge files
5. `audience-decision-framing`
6. `dashboard-discovery`
7. `grill-dashboard-requirements`

## Phase 4 — Holistic Performance & Reward foundation

1. Holistic value-driver tree
2. BAU scenarios
3. Non-BAU scenarios
4. Domain boundaries and shared terminology
5. KPI classification framework
6. Holistic P&R value-driver skill

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

Each pack must include value drivers, business questions, KPIs, calculations, diagnostics, audience treatment, BAU uses, non-BAU uses, risks, and anti-patterns.

## Phase 6 — Consulting communication

1. Technique catalogue
2. Pyramid Principle
3. SCQA
4. Issue trees
5. Action titles
6. Executive storytelling
7. Technique-selection matrix
8. Corresponding skills

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

## Phase 8 — Visualisation patterns

1. Analytical-relationship map
2. Chart-pattern catalogue
3. Executive exhibit patterns
4. IBCS standard
5. Anti-patterns
6. Chart-selection and exhibit skills

## Phase 9 — Dashboard experience

1. Information architecture
2. Guided versus exploratory design
3. Interactive UX
4. Static deck-style design
5. Executive, Business Partner, and manager patterns

## Phase 10 — Power BI implementation

1. Feasibility rules
2. Interaction patterns
3. Static export patterns
4. Semantic model patterns
5. DAX patterns
6. Performance patterns
7. Security
8. Accessibility
9. Theme design

## Phase 11 — Orchestrator and subagents

1. Main Cursor project rule
2. Repository-wide `AGENTS.md`
3. Research synthesiser
4. Dashboard design critic
5. Power BI verifier
6. Evidence and authoring rules
7. Quality gates

## Phase 12 — Evaluation and validation

1. Evaluation rubric
2. Benchmark scenarios
3. Expected results
4. Validation scripts
5. Regression process
6. Release criteria

## Phase 13 — Integration and release

- Remove or resolve placeholders required for the release
- Validate dependencies and internal links
- Test automatic skill discovery
- Test explicit skill invocation
- Run benchmark scenarios
- Resolve material gaps
- Prepare `v0.1.0`

## Minimum status required to unblock dependants

- Standards and schemas: `APPROVED`
- Knowledge packs: `IN REVIEW` for prototyping; `APPROVED` for release
- Skills: `DRAFT` for internal testing; `APPROVED` for release
- Examples: `DRAFT` for evaluation development; `APPROVED` for release examples
