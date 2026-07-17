---
artifact_id: EVAL-QA-002
status: DRAFT
phase: 0
priority: critical
depends_on:
  - artifact_id: EVAL-QA-001
    path: phase-0-internal-pre-review-2026-07-17.md
  - artifact_id: CTRL-CORE-001
    path: ../../../BUILD-ORDER.md
  - artifact_id: CTRL-CORE-002
    path: ../../../DEPENDENCIES.md
  - artifact_id: CTRL-CORE-004
    path: ../../../ARTIFACT-REGISTER.yaml
blocks:
  - independent Phase 0 review execution
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Phase 0 independent-review instructions

## Purpose

Provide a controlled prompt and review process for a reviewer who did not author the Phase 0 material changes.

The reviewer must use a fresh Cursor chat, isolated subagent, or human review context. The implementation chat that produced the artifacts cannot satisfy this gate.

## Reviewer independence

The reviewer must:

- begin without relying on the implementation conversation;
- inspect the repository artifacts directly;
- treat the internal pre-review as evidence of prior defects and corrections, not as proof of quality;
- have no authority to silently edit and approve the same finding;
- record findings before any correction pass begins;
- identify uncertainty rather than assuming intent.

A reviewer may use tools to inspect the repository and validate sources, but AI-generated statements are not evidence.

## Branch and review target

```text
Repository: GitKlink/performance-reward-dashboard-architect
Branch: scaffold/repository-foundation
Pull request: #1
Review issue: #2
```

## Artifacts in scope

### Repository controls

- `BUILD-ORDER.md`
- `DEPENDENCIES.md`
- `STATUS.md`
- `ARTIFACT-REGISTER.yaml`

### Core standards

- `docs/standards/naming-standard.md`
- `docs/standards/research-standard.md`
- `docs/standards/citation-standard.md`

### Research governance

- `knowledge/research-register/README.md`
- `knowledge/research-register/sources.yaml`

### Trials

- `knowledge/research-register/trials/cursor-rules-and-skills-trial.md`
- `knowledge/research-register/trials/new-hire-premium-kpi-trial.md`
- `knowledge/research-register/trials/consulting-attribution-trial.md`
- `knowledge/research-register/trials/graphical-perception-trial.md`
- `knowledge/research-register/trials/internal-source-of-truth-decision-trial.md`

### Prior internal review

- `knowledge/research-register/reviews/phase-0-internal-pre-review-2026-07-17.md`

### Validation implementation

- `scripts/README.md`
- `scripts/validate-dependencies.py`
- `scripts/validate-source-register.py`
- `scripts/check-internal-links.py`
- `tests/`
- `.github/workflows/repository-validation.yml`

## Required review questions

1. Is the mandatory build sequence coherent and free of approval deadlocks?
2. Are dependencies acyclic, explicit, and at the right level of granularity?
3. Are artifact IDs, paths, type codes, domain codes, statuses, and versions internally consistent?
4. Does the naming standard cover all active artifact classes without overconstraining later implementation?
5. Does the research standard distinguish evidence, synthesis, inference, project decision, unresolved claims, and rejected claims correctly?
6. Is source authority treated as claim-relative rather than absolute?
7. Are freshness rules proportionate to product, market, regulatory, and stable-theory evidence?
8. Does the citation model provide both local readability and reusable provenance without unnecessary duplication?
9. Are consulting-firm claims bounded to direct published support?
10. Does the new-hire premium candidate avoid mix distortion, survivorship bias, and unsupported thresholds?
11. Does the graphical-perception trial avoid converting research into a universal chart hierarchy?
12. Does the internal source-of-truth decision record rationale, alternatives, consequences, and revisit triggers?
13. Do validators enforce documented standards rather than creating undocumented policy?
14. Are validator tests sufficient for the current Phase 0 acceptance criteria?
15. Are privacy, confidentiality, copyright, licensing, and public-repository controls adequate?
16. Can the Phase 0 package support Phase 1 architecture without relying on conversation memory?

## Severity model

| Severity | Meaning |
|---|---|
| `critical` | Creates an unsafe, circular, unusable, or fundamentally untrustworthy foundation; blocks all progress |
| `major` | Materially weakens correctness, traceability, maintainability, or governance; blocks status transition |
| `minor` | Should be corrected but does not prevent controlled progress |
| `editorial` | Wording, consistency, or presentation improvement without behavioural impact |

## Finding format

Record each finding using:

```markdown
### <finding-id> — <severity> — <short title>

**Artifact:** `<artifact-id>` — `<path>`

**Section or line:**

**Finding:**

**Impact:**

**Required correction:**

**Evidence or rationale:**
```

Do not combine unrelated defects into one finding.

## Required artifact decisions

For each core standard, return one decision:

```text
READY FOR IN REVIEW
NOT READY — CRITICAL FINDINGS
NOT READY — MAJOR FINDINGS
```

Also provide decisions for:

- the five trials as a group;
- the artifact and source registers;
- the validation suite;
- the overall Phase 0 package.

## Review output

Post the review to GitHub issue #2 using this structure:

```markdown
# Independent Phase 0 review

## Reviewer declaration

## Executive conclusion

## Critical findings

## Major findings

## Minor and editorial findings

## Artifact decisions

## Required correction sequence

## Final gate decision
```

The reviewer must state explicitly:

- whether they were independent of the authoring workflow;
- which commit or branch state was reviewed;
- whether CI was passing at the reviewed commit;
- whether any source claims were independently rechecked.

## Correction protocol

After findings are recorded:

1. the implementation workflow prepares corrections;
2. corrections reference finding IDs;
3. automated validation runs;
4. the independent reviewer verifies closure;
5. only the independent reviewer records acceptance of critical and major corrections;
6. status transitions occur in a separate commit after the review result is recorded.

## Prohibited reviewer actions

- Do not assume passing CI proves content quality.
- Do not approve an artifact merely because it is detailed.
- Do not infer missing evidence from plausible wording.
- Do not rewrite files before recording the original finding.
- Do not approve corrections that were not rechecked.
- Do not treat the internal pre-review as independent evidence.
- Do not start substantive Phase 1 architecture work during this review.

## Completion condition

The independent review is complete when:

- the full review is posted to issue #2;
- every core standard has an explicit readiness decision;
- critical and major findings are clearly separated;
- the reviewed commit is identified;
- the overall Phase 0 gate decision is unambiguous.
