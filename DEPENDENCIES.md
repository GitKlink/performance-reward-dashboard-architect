---
artifact_id: CTRL-CORE-002
status: DRAFT
phase: 0
priority: critical
depends_on:
  - CTRL-CORE-001: BUILD-ORDER.md
blocks:
  - all dependent artifacts
  - dependency validation
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Artifact Dependency Map

## Purpose

This file defines dependency semantics, approval rules, and the authoritative high-level dependency graph. File-level identifiers and lifecycle states are recorded in `ARTIFACT-REGISTER.yaml`.

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
Specialist P&R domain packs
        ↓
Consulting, visual-design, and visualisation knowledge
        ↓
Dashboard experience patterns
        ↓
Power BI implementation patterns
        ↓
Active skills, orchestrator rules, and subagents
        ↓
Evaluation, regression, and release
```

## Dependency fields

Every governed artifact must declare:

```yaml
artifact_id:
depends_on:
blocks:
```

### `depends_on`

Lists the immutable artifact IDs required to author, interpret, validate, or approve the current artifact.

Use the form:

```yaml
depends_on:
  - STD-CORE-001: docs/standards/naming-standard.md
  - ARCH-CORE-001: docs/architecture/agent-architecture.md
```

The path is included for human readability. Validation resolves the identifier through `ARTIFACT-REGISTER.yaml`.

### `blocks`

Lists downstream artifact IDs, groups, or named capabilities that cannot progress to the required status until this artifact meets its gate.

`blocks` is informative and may be broader than the reverse of `depends_on`. `depends_on` remains authoritative for machine validation.

## Dependency types

| Type | Meaning | Example |
|---|---|---|
| Structural | Defines required location, format, or component boundary | skill depends on skill-authoring standard |
| Semantic | Defines concepts or terminology used downstream | fixed-reward skill depends on fixed-reward knowledge pack |
| Data contract | Defines required fields or machine-readable structure | template depends on corresponding schema |
| Evidence | Defines research or sources required for factual claims | knowledge pack depends on research and citation standards |
| Behavioural | Defines orchestration or invocation behaviour | main rule depends on routing model |
| Validation | Defines tests or acceptance criteria | release depends on approved evaluation standard |
| Implementation | Defines platform feasibility or technical constraints | interactive UX pattern depends on Power BI feasibility knowledge |

A dependency may have more than one type. The detailed register may add a `dependency_type` field when the schema is implemented.

## Status semantics

### Placeholder

`PLACEHOLDER` identifies planned scope only. It never satisfies a dependency.

### Research in progress

`RESEARCH IN PROGRESS` may inform exploration but cannot be treated as settled knowledge.

### Draft

`DRAFT` may support explicitly authorised prototyping. A dependent artifact must state that it is using draft input and must be revisited after the dependency changes.

### In review

`IN REVIEW` may support controlled evaluation. It is not sufficient for public release unless `BUILD-ORDER.md` explicitly permits it.

### Approved

`APPROVED` is authoritative for downstream release work until superseded.

### Superseded

`SUPERSEDED` cannot satisfy new dependencies. The artifact must declare `superseded_by`.

## Minimum dependency status

The default minimum prerequisite status is:

| Downstream activity | Minimum prerequisite status |
|---|---|
| Scope planning | `PLACEHOLDER` |
| Research planning | `DRAFT` standard or architecture with explicit risk note |
| Prototype authoring | `DRAFT` where authorised by `BUILD-ORDER.md` |
| Controlled evaluation | `IN REVIEW` |
| Approval | `APPROVED` prerequisites |
| Public release | `APPROVED` prerequisites |

An artifact cannot move to a higher status than its least mature mandatory dependency unless a documented exception is approved in a decision record.

## Source-of-truth rules

1. One concept must have one authoritative artifact.
2. Dependent files link to the authority instead of reproducing its full content.
3. Skills contain procedures and selection logic; knowledge files contain governed subject matter.
4. Templates mirror schemas; they do not redefine field semantics.
5. Examples demonstrate approved methods; they do not create new rules silently.
6. Rules orchestrate and constrain behaviour; they do not duplicate full skills or knowledge packs.
7. Subagents return bounded results; they do not become independent sources of truth.
8. The artifact register identifies authority by immutable ID and current path.

## Circular-dependency rules

Circular dependencies are prohibited among approval dependencies.

Permitted feedback does not create a formal cycle. For example, evaluation may reveal that an architecture artifact needs revision, but architecture does not formally depend on the evaluation artifact used to test it.

When a cycle is detected:

1. identify which artifact owns the definition;
2. move the shared definition to that authority or a new upstream artifact;
3. replace copied content with links;
4. update the register and frontmatter;
5. rerun validation.

## Phase 0 and Phase 1 dependency graph

```text
CTRL-CORE-001  BUILD-ORDER
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

The machine-readable register contains the complete initial mapping and takes precedence if this diagram becomes stale.

## Group dependencies

| Group | Mandatory upstream authorities | Primary consumers |
|---|---|---|
| Repository controls | `CTRL-CORE-001` to `CTRL-CORE-004` | all governed artifacts |
| Research governance | `STD-CORE-001` to `STD-CORE-003` | knowledge, current-product claims, domain skills |
| Architecture | Phase 0 approved standards | rules, agents, skills, schemas, release packaging |
| Schemas | architecture and naming standard | templates, skills, evaluations, scripts |
| Audience knowledge | architecture, schemas, research governance | discovery, KPI, UX, storyline skills |
| P&R foundation | audience framework and research governance | specialist domains, KPI catalogue, diagnostics |
| Consulting knowledge | research and citation standards | storyline, static-design, executive communication |
| Visual-design knowledge | research and citation standards | visualisation, UX, accessibility, QA |
| Power BI knowledge | approved design patterns and current official product evidence | implementation skills and verifier |
| Orchestrator | stable routing model and foundational skills | final Cursor agent |
| Evaluation | approved schemas, skills, examples, and evaluation standard | release decisions |

## Change-impact procedure

When an approved artifact changes:

1. increment its `content_version`;
2. identify all direct and transitive dependants;
3. classify the change as compatible or breaking;
4. update affected dependants or mark them for review;
5. run dependency and link validation;
6. record the impact in `CHANGELOG.md`;
7. do not release until breaking impacts are resolved.

A major content-version change is presumed breaking unless demonstrated otherwise.

## Dependency exceptions

Exceptions are allowed only when:

- the missing dependency is explicitly identified;
- the work is clearly labelled exploratory;
- no active Cursor rule, skill, or subagent is released from it;
- the owner records the rework trigger;
- the exception does not concern privacy, security, regulatory, citation, or public-repository safety.

Exceptions must not be used to bypass evidence or governance standards.

## Validation requirements

The future dependency validator must confirm:

- every substantive artifact has an immutable `artifact_id`;
- every registered path exists;
- file frontmatter and the register agree;
- every `depends_on` ID resolves;
- no duplicate IDs exist;
- no approval cycle exists;
- no artifact is approved while a mandatory dependency is below its required status;
- superseded artifacts identify their replacement;
- renamed paths preserve artifact IDs;
- templates and schemas have one-to-one declared relationships.

## Current limitations

- Only repository controls and Phase 0/1 artifacts have received final IDs.
- Group-level placeholders will receive IDs when they enter active work.
- Automated graph validation has not yet been implemented.
- The scaffold contains generic frontmatter that must be replaced before each artifact becomes active.

## Acceptance criteria

This dependency map can move to `IN REVIEW` when:

- the initial artifact register passes uniqueness and path checks;
- Phase 0 and Phase 1 frontmatter agrees with the register;
- one representative skill-to-knowledge dependency is modelled;
- one schema-to-template dependency is modelled;
- one breaking-change impact path is tested;
- the validator design has no unresolved semantics.

It can move to `APPROVED` with the other Phase 0 controls after independent review.
