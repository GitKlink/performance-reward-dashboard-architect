---
artifact_id: KNOW-CORE-001
status: DRAFT
phase: 0
priority: critical
depends_on:
  - artifact_id: STD-CORE-001
    path: ../../docs/standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../../docs/standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../../docs/standards/citation-standard.md
blocks:
  - KNOW-CORE-002
  - evidence review of knowledge artifacts
  - source freshness reporting
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Research register

## Purpose

This directory stores reusable source records, evidence trials, claim matrices, and review records for the Performance & Reward Dashboard Architect.

It does not replace claim-level citations. Every published knowledge artifact must remain independently readable and cite the evidence supporting its material claims.

## Directory model

```text
knowledge/research-register/
├── README.md
├── sources.yaml
├── claims/
├── trials/
└── reviews/
```

Git creates each directory when its first substantive file is committed.

## Central source register

`sources.yaml` contains one reusable record for each materially distinct source or source version.

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
lifecycle_state:
licence_or_usage_notes:
relevant_artifacts:
planned_consumers:
relevant_claims:
review_notes:
```

Rules:

- `source_id` is stable lowercase kebab-case.
- One materially distinct source version appears once.
- `null` represents an unknown date; empty strings are not used.
- `relevant_artifacts` contains only registered immutable artifact IDs.
- Future destinations belong in `planned_consumers`.
- Current-product and regulatory sources identify version, effective date, or jurisdiction where relevant.
- Licensed or confidential content is never reproduced.

## Claim matrices

Claim matrices connect material claims to evidence and repository treatment.

Recommended filename:

```text
<artifact-id-lowercase>-claims.yaml
```

Required fields:

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

- established evidence;
- supported synthesis;
- labelled inference;
- project decision;
- unresolved question;
- rejected claim.

## Trials

Trials test the research, citation, and naming standards before approval.

Phase 0 includes:

1. current-product evidence;
2. Performance & Reward KPI definition;
3. consulting-firm attribution;
4. stable academic research;
5. internal project decision.

A trial states:

- research question and decision supported;
- scope and exclusions;
- source plan;
- evidence captured;
- claims matrix;
- conflicts and uncertainty;
- repository decision;
- citations;
- what the trial revealed about the standards.

Trials do not automatically become final knowledge artifacts.

## Reviews

Review records assess evidence quality, consistency, and readiness.

Recommended filename:

```text
<artifact-id-lowercase>-review-<yyyy-mm-dd>.md
```

A review covers:

- source authority and freshness;
- accurate representation;
- source diversity and counterevidence;
- unsupported causal language;
- consulting attribution;
- jurisdiction and applicability;
- copyright, privacy, and public-repository safety;
- duplication and source-of-truth conflicts.

An internal pre-review may prepare the package but cannot satisfy an independent approval-review requirement.

## Source lifecycle

| State | Meaning |
|---|---|
| `candidate` | Located but not fully assessed |
| `accepted` | Appropriate for the recorded claims |
| `restricted` | Useful but subject to licence, access, or quotation limits |
| `stale` | Requires revalidation before further use |
| `rejected` | Insufficient, misleading, or superseded for the intended claim |

Rejected and stale records may remain where needed to explain prior decisions.

## Freshness workflow

1. Identify sources used by artifacts due for review.
2. Reopen the official page or publication.
3. Confirm the relevant content remains present and applicable.
4. Update `retrieved_date` only after verification.
5. Record material changes in `review_notes`.
6. Identify dependent artifacts requiring review.

Dates are not refreshed automatically.

## Relationship to local citations

A knowledge artifact cites locally:

```markdown
Cursor project rules are stored in `.cursor/rules`.[^cursor-rules]
```

The source entry under `## Sources` contains enough information to relocate the evidence and includes the central source ID where one exists.

The central register supports reuse, automated validation, and freshness reporting. The local citation supports independent readability.

## Public-repository restrictions

Do not include:

- credentials or private URLs;
- personal information;
- internal policies not approved for publication;
- licensed market-data tables;
- copied proprietary frameworks;
- employee-level pay data;
- private research notes identifying individuals.

Use synthetic examples and describe access restrictions without exposing restricted content.

## Validation

The source-register validator checks:

- required fields;
- source-ID and URL uniqueness;
- allowed evidence and lifecycle values;
- valid dates and freshness warnings;
- registered artifact references;
- central source IDs used by trial and review files.

CI treats source-register warnings as failures.

## Acceptance criteria

This artifact can move to `IN REVIEW` when:

- `sources.yaml` validates without warnings;
- all five Phase 0 trial types are present;
- duplicate-source handling is defined;
- local citations and central source IDs reconcile;
- restricted, stale, and rejected sources are handled consistently;
- the internal pre-review's critical and major findings are resolved.

It can move to `APPROVED` after independent review and correction of all critical and major findings.
