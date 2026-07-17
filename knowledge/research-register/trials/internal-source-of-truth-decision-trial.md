---
artifact_id: EX-CORE-002
status: DRAFT
phase: 0
priority: high
depends_on:
  - CTRL-CORE-001: ../../../BUILD-ORDER.md
  - CTRL-CORE-002: ../../../DEPENDENCIES.md
  - STD-CORE-001: ../../../docs/standards/naming-standard.md
  - STD-CORE-002: ../../../docs/standards/research-standard.md
  - STD-CORE-003: ../../../docs/standards/citation-standard.md
blocks:
  - Phase 0 internal-decision review
  - ARCH-CORE-001: ../../../docs/architecture/agent-architecture.md
  - ARCH-CORE-005: ../../../docs/architecture/release-architecture.md
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-10-17
---

# Trial: Internal source-of-truth decision

## Purpose

Test how the repository records a deliberate architectural decision that is informed by project needs but is not an externally established fact.

## Decision question

Should this repository contain only the final installable Cursor agent, or should it remain the maintained source repository for research, development, evaluation, and releases of that agent?

## Project decision

**This repository is the maintained source of truth for creating, testing, releasing, and maintaining the Performance & Reward Dashboard Architect.**

The installable Cursor agent is a governed subset of the repository rather than a separate authority.

The final agent surface is expected to include:

```text
.cursor/
├── rules/
├── agents/
└── skills/
```

Supporting knowledge, schemas, templates, examples, evaluation cases, scripts, and documentation remain versioned beside the agent because they explain, test, and govern its behaviour.

## Rationale

A single maintained source repository provides:

- one authoritative history for agent behaviour and supporting knowledge;
- traceability from research to skill instructions and evaluation results;
- coordinated versioning of dependencies;
- the ability to review a change and its downstream effects in one pull request;
- release packaging without synchronising two competing repositories;
- clear separation between development artifacts and the packaged release through release architecture rather than repository duplication.

This rationale is a project judgement. It is not presented as a universal Cursor requirement.

## Boundaries

The decision does not mean every repository file must ship in every release.

The release architecture may package only approved runtime and support files, for example:

```text
.cursor/
knowledge/
templates/
schemas/
README.md
LICENSE
```

Development-only research trails, incomplete evaluations, working notes, or validation fixtures may remain in the source repository but be excluded from a public release package.

The decision also does not prevent a future distribution repository if a documented need emerges, such as:

- package-manager requirements;
- materially different licensing;
- security separation;
- a generated artifact that should not share source history;
- a stable consumer repository with a distinct maintenance lifecycle.

A future split would require an approved architecture decision and migration plan.

## Authority and references

This decision is governed by:

- [CTRL-CORE-001 — Build order](../../../BUILD-ORDER.md), which separates architecture, implementation, evaluation, and release stages;
- [CTRL-CORE-002 — Dependencies](../../../DEPENDENCIES.md), which requires one authoritative artifact per concept and coordinated change-impact handling;
- [CTRL-CORE-004 — Artifact register](../../../ARTIFACT-REGISTER.yaml), which provides immutable artifact identification across path changes;
- the future `ARCH-CORE-005` release architecture, which must define the shipped subset.

No external citation is required because the statement is explicitly labelled as a project decision and does not claim that Cursor mandates this repository model.

## Alternative considered

### Separate builder and final-agent repositories

Potential advantages:

- cleaner consumer-facing repository;
- stronger separation between source research and distributed runtime;
- potentially smaller clone and review surface.

Reasons not selected initially:

- duplicate release and dependency management;
- risk of drift between source knowledge and distributed skills;
- more complex contribution and regression workflows;
- no current product or licensing constraint requiring separation.

The alternative remains available if the release architecture later establishes a material need.

## Decision record prototype

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

## What the trial revealed about the standards

### Research standard

- Not every important repository statement is a research claim.
- Project decisions need explicit rationale, alternatives, consequences, and revisit triggers rather than artificial external citations.
- Evidence may inform a decision without converting the decision into a product requirement.

### Citation standard

- Relative links and immutable artifact IDs are sufficient for internal governance claims.
- Labelling the statement as a project decision prevents false external authority.
- A bibliography would reduce clarity here because no external evidence is needed to establish the chosen repository structure.

### Naming standard

- The artifact should describe the decision topic, not use a generic filename such as `decision-1.md`.
- The immutable artifact ID survives a future move into an architecture-decision directory.

## Acceptance result

**Trial result: PASS**

The standards support a clear internal decision without citation theatre. The trial should inform the future architecture-decision format in Phase 1.
