---
artifact_id: CTRL-CORE-002
status: DRAFT
phase: 0
priority: critical
depends_on:
  - artifact_id: CTRL-CORE-001
    path: BUILD-ORDER.md
blocks:
  - all dependent artifacts
  - dependency validation
content_version: 0.5.0
last_reviewed: 2026-07-31
next_review: 2026-08-31
---

# Artifact dependency map

## Purpose

This file defines dependency semantics, source-of-truth boundaries, development maturity, approval rules, and change-impact handling. `ARTIFACT-REGISTER.yaml` is the machine-readable authority for artifact IDs, paths, statuses, and direct dependencies.

## Dependency chain

```text
Minimum repository controls, architecture, standards, schemas, and validation
        ↓
Performance & Reward ontology and shared definitions
        ↓
Priority specialist domain packs
        ↓
Domain workflows and product archetypes
        ↓
Performance & Reward audience and decision treatment
        ↓
Microsoft Power BI skill integration and gap handling
        ↓
Performance & Reward-specific implementation knowledge
        ↓
Domain communication and visual patterns
        ↓
Active skills, orchestrator rules, subagents, and comprehensive evaluation
        ↓
Approval, packaging, and release
```

The chain controls order and ownership. It does not require formal approval of every upstream draft before downstream authoring begins.

Generic Power BI implementation knowledge is no longer an automatic upstream dependency for domain authoring. Domain artifacts may begin once their minimum structural, evidence, and schema dependencies are substantive drafts.

## Required metadata

Every governed Markdown or MDC artifact declares:

```yaml
artifact_id:
depends_on:
blocks:
```

Canonical dependencies use immutable IDs and repository-relative paths:

```yaml
depends_on:
  - artifact_id: STD-CORE-001
    path: docs/standards/naming-standard.md
```

The ID is authoritative. The path supports navigation and must agree with the artifact register.

`blocks` may name artifact IDs or bounded capabilities. It is informative; `depends_on` is authoritative for validation.

## Dependency types

| Type | Meaning | Example |
|---|---|---|
| Structural | Defines format or component boundaries | skill depends on skill-authoring standard |
| Semantic | Defines concepts or terminology | domain skill depends on domain ontology |
| Data contract | Defines fields or machine-readable structure | KPI catalogue depends on KPI schema |
| Evidence | Defines research required for claims | knowledge depends on research standards |
| Behavioural | Defines invocation or orchestration | main rule depends on routing model |
| Validation | Defines tests or acceptance criteria | release depends on evaluation standard |
| Implementation | Defines platform feasibility | domain workflow depends on verified implementation constraints |
| External capability | Defines delegated platform behaviour | local integration rule depends on a verified Microsoft skill capability |

## Lifecycle semantics

### `PLACEHOLDER`

Planned scope only. It does not provide substantive authority and cannot be activated or released.

### `RESEARCH IN PROGRESS`

Evidence collection is active and unsettled.

### `DRAFT`

Substantive content exists. It may support controlled downstream authoring, prototyping, and testing when assumptions and limitations remain visible.

### `IN REVIEW`

The artifact is a formal review candidate. It may support release-candidate evaluation but is not yet authoritative for public release.

### `APPROVED`

The artifact is authoritative for the release package until superseded.

### `SUPERSEDED`

The artifact cannot satisfy new dependencies and must identify its replacement.

## Minimum maturity by activity

| Activity | Default minimum prerequisite status |
|---|---|
| Scope planning | `PLACEHOLDER` |
| Controlled development | `DRAFT` |
| Formal review | `IN REVIEW` |
| Runtime activation for release | `APPROVED` mandatory dependencies |
| Public release | `APPROVED` mandatory dependencies |

A draft dependency does not prevent downstream draft work. It does prevent a downstream artifact from claiming final authority or release readiness.

## Draft dependency obligations

When an artifact depends on a draft:

1. inherit the draft status or remain below formal approval;
2. identify material assumptions that could change;
3. link to the owning artifact instead of copying its definitions;
4. revisit the dependent artifact when the dependency changes materially;
5. avoid activating runtime behaviour that presents the draft as approved policy.

## Phase-boundary rule

`BUILD-ORDER.md` defines the development sequence and the comprehensive pre-release gate.

A later phase may begin substantive draft work when:

- its required upstream artifacts contain enough draft content to guide it;
- automated repository validation passes;
- no unresolved critical defect makes the downstream work predictably invalid;
- runtime placeholders remain disabled.

Domain-first vertical slices may cross nominal phase boundaries when they are used to validate the ontology, schemas, routing, and implementation constraints together.

Formal independent review is concentrated in Phase 8 and approval in Phase 9, except where an earlier decision is high-risk, legally sensitive, security-sensitive, or difficult to reverse.

## Source-of-truth rules

1. One concept has one authoritative owning artifact.
2. Dependent files link to the owner instead of reproducing it.
3. Skills contain procedures and selection logic; knowledge files contain subject matter.
4. Templates implement schemas and do not redefine field semantics.
5. Examples demonstrate methods and do not create hidden rules.
6. Rules orchestrate behaviour without duplicating full skills or knowledge packs.
7. Subagents return bounded outputs and do not become independent authorities.
8. Generated indexes never replace the artifact register.
9. Source records identify evidence; they do not replace claim-level citations.
10. A draft may guide development without becoming release authority.
11. Performance & Reward ontology owns business terminology, calculations, process semantics, grain rules, and control meanings.
12. Microsoft Power BI skills may own delegated platform procedures but do not become authority for domain definitions.
13. Local integration artifacts own delegate, supplement, override, fallback, and verification decisions.

## Circular dependencies

Formal dependencies must remain acyclic.

Evaluation can trigger revision of an upstream artifact without creating a formal reverse dependency.

When a cycle appears:

1. identify the owner of the shared definition;
2. move the definition to that artifact or a new upstream artifact;
3. replace copied content with references;
4. update frontmatter and the register;
5. rerun validation.

## Domain-first graph

```text
CTRL-CORE-001  BUILD ORDER
        ↓
CTRL-CORE-002  DEPENDENCIES
        ↓
Core standards + architecture + minimum schemas
        ↓
P&R ONTOLOGY
        ├──→ FIXED REWARD
        ├──→ VARIABLE REWARD
        ├──→ PERFORMANCE MANAGEMENT
        ├──→ JOB ARCHITECTURE
        ├──→ MARKET COMPETITIVENESS
        └──→ GOVERNANCE AND CONTROLS

P&R ONTOLOGY + PRIORITY DOMAIN PACKS
        ↓
DOMAIN WORKFLOWS
        ├──→ PRE-EOY SALARY AND BONUS PLANNING
        ├──→ MANAGER SALARY REVIEW
        └──→ FIXED-REWARD BUDGET ALLOCATION

DOMAIN WORKFLOWS + MICROSOFT SKILL INTEGRATION
        ↓
P&R-SPECIFIC IMPLEMENTATION + RUNTIME ORCHESTRATION
        ↓
COMPREHENSIVE EVALUATION AND RELEASE
```

## Group dependencies

| Group | Upstream draft foundation | Main consumers |
|---|---|---|
| Repository controls | Build order, dependency model, artifact register | all governed artifacts |
| Research governance | naming, research, and citation standards | knowledge and evidence-based skills |
| Minimum architecture | controls, context strategy, routing, authoring standards | ontology, schemas, skills, release packaging |
| Minimum schemas | architecture and naming | domain catalogues, workflows, templates, evaluations |
| P&R ontology | research governance and minimum schemas | all specialist packs and domain workflows |
| Specialist domains | ontology and relevant evidence | workflows, diagnostics, audience treatment, implementation |
| Domain workflows | ontology, specialist packs, schemas | runtime routes, evaluations, product archetypes |
| P&R audiences | ontology and workflows | discovery, explanation, UX, storyline |
| Microsoft skill integration | routing model and verified external capability evidence | delegated implementation routes and verifier |
| P&R implementation | domain workflows and verified platform capability | implementation skills and handoffs |
| Domain communication | audiences, workflows, and evidence standards | page, visual, and narrative skills |
| Orchestrator | routing model, domain skills, integration rules, and evaluations | final Cursor runtime |
