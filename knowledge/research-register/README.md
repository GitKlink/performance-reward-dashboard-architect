---
artifact_id: KNOW-CORE-001
status: DRAFT
phase: 0
priority: critical
depends_on:
  - STD-CORE-001: ../../docs/standards/naming-standard.md
  - STD-CORE-002: ../../docs/standards/research-standard.md
  - STD-CORE-003: ../../docs/standards/citation-standard.md
blocks:
  - knowledge/research-register/sources.yaml
  - evidence review of knowledge artifacts
  - source freshness reporting
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Research register

## Purpose

This directory stores reusable source records, research trials, claim matrices, and review evidence for the Performance & Reward Dashboard Architect.

It does not replace claim-level citations in knowledge files. Each published knowledge artifact must remain independently readable and must cite the sources supporting its claims.

## Directory model

```text
knowledge/research-register/
├── README.md
├── sources.yaml
├── claims/
├── trials/
└── reviews/
```

Git tracks only files, so each directory is created when its first substantive artifact is added.

## `sources.yaml`

The central source register contains one reusable record per source.

Required fields:

```yaml
source_id:
title:
author_or_organisation:
source_type:
evidence_level:
url_or_doi:
publication_date:
updated_date:
retrieved_date:
version:
jurisdiction:
licence_or_usage_notes:
relevant_artifacts:
review_notes:
```

Rules:

- `source_id` is stable lower-kebab-case.
- One source appears once in the central register.
- A new edition, release, or materially changed version receives a new source record when the distinction matters.
- `null` is used for unknown values; empty strings are prohibited.
- Product and regulatory sources include version, effective date, or jurisdiction where relevant.
- Licensed or confidential material must not be reproduced.

## `claims/`

Claim matrices connect material claims to one or more source IDs.

Recommended filename:

```text
<artifact-id-lowercase>-claims.yaml
```

Example:

```text
know-fixed-001-claims.yaml
```

Required claim fields:

```yaml
claim_id:
claim:
claim_type:
source_ids:
confidence:
applicability:
limitations:
repository_treatment:
```

`repository_treatment` records whether the claim becomes:

- published evidence;
- supported synthesis;
- labelled inference;
- project decision;
- unresolved question;
- rejected claim.

## `trials/`

Trials test the research and citation standards before those standards are approved.

Phase 0 requires at least:

1. one current-product claim;
2. one Performance & Reward KPI definition;
3. one consulting-firm attribution example;
4. one stable research finding;
5. one internal project decision.

A trial must state:

- question;
- source plan;
- evidence captured;
- claims matrix;
- conflicts or uncertainty;
- repository decision;
- citations;
- what the trial revealed about the standards.

Trials do not automatically become final knowledge artifacts.

## `reviews/`

Reviews record independent checks of research quality and citation accuracy.

Recommended filename:

```text
<artifact-id-lowercase>-review-<yyyy-mm-dd>.md
```

A review must assess:

- authority;
- freshness;
- accurate representation;
- source diversity;
- unsupported causal language;
- consulting attribution;
- jurisdiction and applicability;
- copyright and public-repository safety;
- duplication with existing knowledge.

## Source lifecycle

| State | Meaning |
|---|---|
| `candidate` | Located but not yet assessed |
| `accepted` | Appropriate for the recorded claims |
| `restricted` | Useful but subject to licence, access, or quotation limits |
| `stale` | Requires revalidation before further use |
| `rejected` | Insufficient, misleading, or superseded for the intended claim |

The source record retains rejected or stale status when needed to explain past research decisions.

## Freshness workflow

1. Query sources used by artifacts due for review.
2. Reopen the official page or publication.
3. Confirm the relevant content still exists and remains applicable.
4. Update `retrieved_date` only when the source has actually been rechecked.
5. Record material content changes in `review_notes`.
6. Identify downstream artifacts requiring review.

Do not refresh dates automatically without verifying content.

## Relationship to local citations

A knowledge artifact cites locally using a descriptive Markdown footnote:

```markdown
Cursor project rules are stored in `.cursor/rules`.[^cursor-rules]
```

The source entry in that file contains enough information to locate the source. The same source may also exist in `sources.yaml` under a stable `source_id`.

The central register supports reuse, review, and freshness reporting. The local citation supports independent readability.

## Public-repository constraints

The register must not include:

- credentials or private URLs;
- personal information;
- internal policies not approved for publication;
- licensed market-data tables;
- copied proprietary framework content;
- private research notes identifying individuals;
- pay data derived from real employees.

Use synthetic examples and record access restrictions without exposing restricted content.

## Acceptance criteria

This artifact can move to `IN REVIEW` when:

- `sources.yaml` validates against the planned research-record structure;
- the five Phase 0 trial types have been completed;
- duplicate source detection is defined;
- one freshness review has been simulated;
- local citations and central source IDs reconcile;
- restricted and rejected sources are handled consistently.

It can move to `APPROVED` with the Phase 0 evidence standards after independent review.
