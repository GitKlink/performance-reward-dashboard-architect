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
content_version: 0.3.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Artifact dependency map

## Purpose

This file defines dependency semantics, approval rules, source-of-truth boundaries, and change-impact handling. `ARTIFACT-REGISTER.yaml` is the machine-readable authority for artifact IDs, paths, statuses, and direct dependencies.

## Core dependency chain

```text
Repository controls and evidence standards
        ↓
Agent architecture and context strategy
        ↓
Schemas and output contracts
        ↓
Audience and decision framework
        ↓
Holistic Performance & Reward value-driver architecture
        ↓
Specialist Performance & Reward domain packs
        ↓
Consulting, visual-design, and visualisation knowledge
        ↓
Dashboard experience patterns
        ↓
Power BI implementation patterns
        ↓
Active skills, orchestrator rules, and subagents
        ↓
Evaluation, regression, packaging, and release
```

## Required dependency metadata

Every governed Markdown or MDC artifact declares:

```yaml
artifact_id:
depends_on:
blocks:
```

Canonical dependencies use immutable IDs plus repository-relative paths:

```yaml
depends_on:
  - artifact_id: STD-CORE-001
    path: docs/standards/naming-standard.md
  - artifact_id: ARCH-CORE-001
    path: docs/architecture/agent-architecture.md
```

The ID is authoritative. The path supports human navigation and must agree with the artifact register.

`blocks` may name artifact IDs or bounded capabilities. It is informative; `depends_on` is authoritative for validation.

## Dependency types

| Type | Meaning | Example |
|---|---|---|
| Structural | Defines required format or component boundary | skill depends on skill-authoring standard |
| Semantic | Defines concepts or terminology | domain skill depends on domain knowledge pack |
| Data contract | Defines required fields or structure | template depends on schema |
| Evidence | Defines research needed for claims | knowledge pack depends on research and citation standards |
| Behavioural | Defines invocation or orchestration | main rule depends on routing model |
| Validation | Defines tests or acceptance criteria | release depends on evaluation standard |
| Implementation | Defines platform feasibility | interaction pattern depends on Power BI evidence |

A dependency may satisfy more than one type.

## Lifecycle semantics

### `PLACEHOLDER`

Scope exists, but the artifact does not provide substantive authority. It never satisfies a release dependency.

### `RESEARCH IN PROGRESS`

Evidence collection is active. The artifact may inform exploration but remains unsettled.

### `DRAFT`

Substantive content exists. It may support explicitly authorised prototyping and internal pre-review.

### `IN REVIEW`

Acceptance criteria are being assessed. It may support controlled evaluation but not public release.

### `APPROVED`

The artifact is authoritative for dependent work until superseded.

### `SUPERSEDED`

The artifact cannot satisfy new dependencies and must declare `superseded_by`.

## Minimum dependency maturity

| Downstream activity | Default minimum prerequisite status |
|---|---|
| Scope planning | `PLACEHOLDER` |
| Evidence or implementation prototyping | `DRAFT`, where authorised by `BUILD-ORDER.md` |
| Controlled evaluation | `IN REVIEW` |
| Artifact approval | `APPROVED` mandatory prerequisites |
| Public release | `APPROVED` mandatory prerequisites |

An artifact cannot move above the maturity of a mandatory dependency unless a documented exception is approved.

## Phase-boundary rule

`BUILD-ORDER.md` defines the phase gate. A later phase may be explored for planning or controlled trials, but it cannot become authoritative while its mandatory earlier-phase dependencies remain below the required status.

A trial used to validate an earlier standard does not create a circular approval dependency when:

- it is explicitly labelled as a controlled trial;
- it does not become an active Cursor capability;
- the earlier standard remains authoritative for the trial's scope;
- the trial result is used to approve or revise the earlier standard.

## Source-of-truth rules

1. One concept has one authoritative artifact.
2. Dependent files link to the authority instead of reproducing it.
3. Skills contain procedures and selection logic; knowledge files contain governed subject matter.
4. Templates implement schemas and do not redefine field semantics.
5. Examples demonstrate approved methods and do not create hidden rules.
6. Rules orchestrate and constrain behaviour without duplicating full skills or knowledge packs.
7. Subagents return bounded results and do not become independent authorities.
8. Generated indexes never replace the artifact register.
9. Source records identify evidence; they do not replace claim-level citations.
10. A review performed by the authoring workflow does not replace an independent approval review.

## Circular dependencies

Approval dependencies must be acyclic.

Evaluation may reveal that an upstream artifact needs revision, but that feedback does not become a formal reverse dependency.

When a cycle is detected:

1. identify which artifact owns the shared definition;
2. move the definition to that authority or a new upstream artifact;
3. replace copied content with links;
4. update frontmatter and the artifact register;
5. rerun validation.

## Phase 0 and Phase 1 dependency graph

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
Phase 0 trials, validators, tests, and independent review
        ↓
ARCH-CORE-001  AGENT ARCHITECTURE
        ├──→ ARCH-CORE-002  CONTEXT STRATEGY
        ├──→ ARCH-CORE-004  INFORMATION ARCHITECTURE
        └──→ STD-CORE-005   EXAMPLE STANDARD

ARCH-CORE-001 + ARCH-CORE-002
        ↓
ARCH-CORE-003  SKILL ROUTING
        ↓
STD-CORE-004   SKILL AUTHORING
        ↓
STD-CORE-006   EVALUATION STANDARD
```

The artifact register takes precedence if this diagram becomes stale.

## Group dependencies

| Group | Mandatory upstream authorities | Main consumers |
|---|---|---|
| Repository controls | `CTRL-CORE-001` to `CTRL-CORE-004` | all governed artifacts |
| Research governance | `STD-CORE-001` to `STD-CORE-003` | knowledge, research-dependent skills, current-product claims |
| Architecture | approved Phase 0 controls | rules, agents, skills, schemas, release packaging |
| Schemas | architecture and naming standards | templates, skills, evaluations, validators |
| Audience knowledge | architecture, schemas, research governance | discovery, KPI, UX, and storyline skills |
| Performance & Reward foundation | audience framework and research governance | specialist packs, KPI catalogue, diagnostics |
| Consulting knowledge | research and citation standards | storyline, static design, executive communication |
| Visual-design knowledge | research and citation standards | visualisation, UX, accessibility, quality assurance |
| Power BI knowledge | approved design patterns and current product evidence | implementation skills and verifier |
| Orchestrator | routing model and foundational skills | final Cursor agent |
| Evaluation | approved schemas, skills, examples, and evaluation standard | release decisions |

## Change impact

When an approved artifact changes:

1. increment `content_version`;
2. identify direct and transitive dependants;
3. classify the change as compatible or breaking;
4. update affected artifacts or mark them for review;
5. run dependency, source, and link validation;
6. record the impact in `CHANGELOG.md`;
7. block release until breaking impacts are resolved.

A major content-version change is presumed breaking unless demonstrated otherwise.

## Exceptions

A dependency exception is allowed only when:

- the missing dependency is named;
- the work is explicitly exploratory;
- no active rule, skill, or subagent is released from it;
- a rework trigger is recorded;
- the exception does not concern privacy, security, regulation, citation, or public-repository safety.

Exceptions cannot bypass evidence or governance requirements.

## Validation requirements

The dependency validator must confirm:

- registered paths exist;
- IDs and paths are unique;
- frontmatter and register metadata agree;
- every dependency resolves;
- no approval cycle exists;
- no artifact is approved while a mandatory prerequisite is below the required status;
- superseded artifacts name their replacement;
- path changes preserve IDs;
- templates and schemas declare their relationships;
- canonical dependency syntax is used before Phase 0 approval.

## Acceptance criteria

This control can move to `IN REVIEW` when:

- the artifact register passes uniqueness, path, and cycle validation;
- registered Markdown and MDC frontmatter agrees with the register;
- representative skill-to-knowledge, schema-to-template, and validation dependencies are modelled;
- one breaking-change path has been tested;
- legacy dependency syntax has been removed from active Phase 0 artifacts;
- the internal pre-review's critical and major findings are resolved.

It can move to `APPROVED` after independent review and correction of all critical and major findings.
