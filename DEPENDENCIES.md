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
content_version: 0.4.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Artifact dependency map

## Purpose

This file defines dependency semantics, source-of-truth boundaries, development maturity, approval rules, and change-impact handling. `ARTIFACT-REGISTER.yaml` is the machine-readable authority for artifact IDs, paths, statuses, and direct dependencies.

## Dependency chain

```text
Repository controls and evidence standards
        ↓
Agent architecture and context strategy
        ↓
Schemas and output contracts
        ↓
Audience and decision framework
        ↓
Holistic Performance & Reward foundation
        ↓
Specialist domain packs
        ↓
Consulting, visual-design, and visualisation knowledge
        ↓
Dashboard experience patterns
        ↓
Power BI implementation patterns
        ↓
Active skills, orchestrator rules, and subagents
        ↓
Comprehensive evaluation, approval, packaging, and release
```

The chain controls order and ownership. It does not require formal approval of every upstream draft before downstream authoring begins.

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
| Semantic | Defines concepts or terminology | domain skill depends on domain knowledge |
| Data contract | Defines fields or machine-readable structure | template depends on schema |
| Evidence | Defines research required for claims | knowledge depends on research standards |
| Behavioural | Defines invocation or orchestration | main rule depends on routing model |
| Validation | Defines tests or acceptance criteria | release depends on evaluation standard |
| Implementation | Defines platform feasibility | interaction pattern depends on Power BI evidence |

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

Formal independent review is concentrated in Phase 12 and approval in Phase 13, except where an earlier decision is high-risk, legally sensitive, security-sensitive, or difficult to reverse.

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

## Circular dependencies

Formal dependencies must remain acyclic.

Evaluation can trigger revision of an upstream artifact without creating a formal reverse dependency.

When a cycle appears:

1. identify the owner of the shared definition;
2. move the definition to that artifact or a new upstream artifact;
3. replace copied content with references;
4. update frontmatter and the register;
5. rerun validation.

## Phase 0 and Phase 1 graph

```text
CTRL-CORE-001  BUILD ORDER
        ↓
CTRL-CORE-002  DEPENDENCIES
        ↓
STD-CORE-001   NAMING
        ↓
STD-CORE-002   RESEARCH
        ↓
STD-CORE-003   CITATION
        ↓
CTRL-CORE-004  ARTIFACT REGISTER
        ↓
Phase 0 trials and automated validation
        ↓
ARCH-CORE-001  AGENT ARCHITECTURE
        ├──→ ARCH-CORE-002  CONTEXT STRATEGY
        ├──→ ARCH-CORE-004  INFORMATION ARCHITECTURE
        └──→ ARCH-CORE-005  RELEASE ARCHITECTURE

ARCH-CORE-001 + ARCH-CORE-002
        ↓
ARCH-CORE-003  SKILL ROUTING
        ↓
STD-CORE-004   SKILL AUTHORING
        ↓
STD-CORE-005   EXAMPLE AUTHORING
        ↓
STD-CORE-006   EVALUATION STANDARD
```

All artifacts may remain drafts during development. Phase 12 tests the integrated system; Phase 13 approves release dependencies.

## Group dependencies

| Group | Upstream draft foundation | Main consumers |
|---|---|---|
| Repository controls | Build order, dependency model, artifact register | all governed artifacts |
| Research governance | naming, research, and citation standards | knowledge and evidence-based skills |
| Architecture | Phase 0 controls and trials | rules, agents, skills, schemas, release packaging |
| Schemas | architecture and naming | templates, skills, evaluations, validators |
| Audience knowledge | architecture, schemas, research governance | discovery, KPI, UX, storyline |
| Performance & Reward foundation | audience framework and research governance | specialist packs and diagnostics |
| Consulting and visual knowledge | research and citation standards | communication, UX, and design skills |
| Power BI knowledge | design patterns and current product evidence | implementation skills and verifier |
| Orchestrator | routing model and foundational skills | final Cursor runtime |
| Evaluation | schemas, skills, examples, and evaluation standard | release approval |

## Change impact

When a draft or approved artifact changes materially:

1. increment `content_version`;
2. identify direct and transitive dependants;
3. classify the change as compatible or breaking;
4. update affected artifacts or mark them for review;
5. run dependency, source, link, and unit-test validation;
6. update `CHANGELOG.md` when the change is notable;
7. block release until breaking impacts are resolved.

A major content-version change is presumed breaking unless demonstrated otherwise.

## Exceptions

A dependency exception requires:

- the missing dependency to be named;
- the work to be explicitly exploratory;
- a rework trigger;
- no runtime activation or public release;
- no bypass of privacy, security, regulation, citation, or public-repository safety.

## Validation requirements

The dependency validator must confirm:

- registered paths exist;
- IDs and paths are unique;
- frontmatter and register metadata agree;
- dependencies resolve;
- no formal dependency cycle exists;
- no artifact is approved while a mandatory dependency remains below its required release status;
- superseded artifacts identify replacements;
- path changes preserve IDs;
- canonical dependency syntax is used.

## Acceptance criteria

This control is suitable for continued development when:

- artifact and frontmatter validation passes;
- the graph is acyclic;
- draft and release maturity are clearly distinguished;
- representative architecture, skill-to-knowledge, schema-to-template, and validation relationships are modelled;
- automated validation runs in CI.

It becomes `APPROVED` during the Phase 12–13 review and release process after critical and major findings are resolved.
