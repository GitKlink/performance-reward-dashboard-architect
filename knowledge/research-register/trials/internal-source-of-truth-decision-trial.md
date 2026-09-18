---
artifact_id: EX-CORE-002
status: DRAFT
phase: 0
priority: high
depends_on:
  - artifact_id: CTRL-CORE-001
    path: ../../../BUILD-ORDER.md
  - artifact_id: CTRL-CORE-002
    path: ../../../DEPENDENCIES.md
  - artifact_id: STD-CORE-001
    path: ../../../docs/standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../../../docs/standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../../../docs/standards/citation-standard.md
blocks:
  - Phase 0 internal-decision review
  - ARCH-CORE-001
  - ARCH-CORE-005
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-10-17
---

# Trial: Internal source-of-truth decision

## Purpose

Test how the repository records a deliberate architecture decision that is informed by project needs but is not an externally established fact.

## Decision question

Should this repository contain only the final installable Cursor agent, or should it remain the maintained source repository for research, development, evaluation, and releases of that agent?

## Project decision

**This repository is the maintained source of truth for creating, testing, releasing, and maintaining the Performance & Reward Dashboard Architect.**

The installable Cursor agent is a governed subset of the repository rather than a separate authority.

The intended runtime surface is:

```text
.cursor/
├── rules/
├── agents/
└── skills/
```

Supporting knowledge, schemas, templates, examples, evaluations, scripts, and documentation remain versioned beside the runtime components because they explain, test, and govern behaviour.

## Rationale

A single maintained source repository provides:

- one history for agent behaviour and supporting knowledge;
- traceability from research to skills and evaluations;
- coordinated dependency and version management;
- one pull request for a change and its downstream impacts;
- release packaging without synchronising competing repositories;
- separation between development artifacts and the distributed package through release architecture rather than repository duplication.

This is a project judgement, not a universal Cursor requirement.

## Boundaries

The decision does not mean every file must ship in every release.

The release architecture may package only approved runtime and support files, for example:

```text
.cursor/
knowledge/
templates/
schemas/
README.md
LICENSE
```

Development-only research trails, incomplete evaluations, working notes, and validation fixtures may remain in the source repository but be excluded from the release package.

A separate distribution repository may be reconsidered where a material need emerges, such as:

- package-manager constraints;
- materially different licensing;
- security separation;
- generated artifacts requiring independent history;
- a consumer repository with a genuinely separate lifecycle.

A future split requires an approved architecture decision and migration plan.

## Authority

This decision is governed by:

- [CTRL-CORE-001 — Build order](../../../BUILD-ORDER.md);
- [CTRL-CORE-002 — Dependency map](../../../DEPENDENCIES.md);
- [CTRL-CORE-004 — Artifact register](../../../ARTIFACT-REGISTER.yaml);
- the future `ARCH-CORE-005` release architecture.

No external citation is required because the statement is explicitly a project decision and does not claim that Cursor mandates this model.

## Alternative considered

### Separate builder and final-agent repositories

Potential benefits:

- cleaner consumer-facing repository;
- stronger separation of research and runtime;
- potentially smaller clone and review surface.

Reasons not selected initially:

- duplicate release and dependency management;
- risk of drift between source knowledge and distributed skills;
- more complex contribution and regression workflows;
- no current product, security, or licensing requirement for separation.

## Revisit triggers

Reassess this decision when:

- release packaging becomes materially complex;
- licensing differs between source and distribution;
- a security boundary is required;
- generated releases require a separate lifecycle;
- consumers need a stable repository that cannot include development history.

## Decision-record prototype

Future architecture decisions should capture:

```yaml
artifact_id:
decision:
status:
date:
context:
options_considered:
decision_drivers:
selected_option:
consequences:
revisit_triggers:
depends_on:
blocks:
```

## Acceptance result

**Trial result: PASS**

The standards support a clear internal decision without citation theatre. The decision remains subject to the future release architecture and independent review.
