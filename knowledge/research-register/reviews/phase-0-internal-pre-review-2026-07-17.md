---
artifact_id: EVAL-QA-001
status: DRAFT
phase: 0
priority: critical
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
  - artifact_id: EX-CORE-001
    path: ../trials/cursor-rules-and-skills-trial.md
  - artifact_id: EX-CORE-002
    path: ../trials/internal-source-of-truth-decision-trial.md
  - artifact_id: EX-FIXED-001
    path: ../trials/new-hire-premium-kpi-trial.md
  - artifact_id: EX-CONSULT-001
    path: ../trials/consulting-attribution-trial.md
  - artifact_id: EX-VIZ-001
    path: ../trials/graphical-perception-trial.md
blocks:
  - independent Phase 0 review
  - Phase 0 status transition
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Phase 0 internal pre-review

## Review status

This internal pre-review was performed within the implementation workflow. It does **not** satisfy the independent-review gate.

## Scope

Reviewed:

- build and dependency controls;
- naming, research, and citation standards;
- five evidence and decision trials;
- artifact and source registers;
- validators, tests, and CI;
- readiness for a separate independent review.

## Initial outcome

The first pass identified one critical, seven major, and four minor findings. The repository was not ready for independent review at that point.

## Resolution summary

| Finding | Severity | Resolution | Status |
|---|---|---|---|
| F-001 Phase approval deadlock | Critical | Research and citation standards now permit initial approval after Phase 0 trials and independent review, with mandatory later implementation reviews | Resolved |
| F-002 Research-record schema circular dependency | Major | Phase 0 now requires a validated field contract; formal schema implementation remains in Phase 2 | Resolved |
| F-003 Incomplete artifact types | Major | `TEST` and `INFRA` were added to the naming standard and reserved namespaces | Resolved |
| F-004 Active validation artifacts unregistered | Major | Validators, tests, CI workflow, and this review were added to `ARTIFACT-REGISTER.yaml` | Resolved |
| F-005 Descriptive source-to-artifact references | Major | `relevant_artifacts` now contains only immutable IDs; future destinations use `planned_consumers` | Resolved |
| F-006 Legacy dependency syntax | Major | Active Phase 0 and registered Phase 1 Markdown artifacts use canonical dependency objects; CI treats dependency warnings as failures | Resolved |
| F-007 New-hire KPI survivorship bias | Major | Historical cohort now includes all eligible commenced hires regardless of later employment status | Resolved |
| F-008 Independent reviewer separation | Major | Standards and issue #2 explicitly require a reviewer independent of the authoring workflow | Process gate remains open |
| F-009 Standards did not apply citation model to themselves | Minor | Naming and research standards now use claim-level footnotes for material product claims | Resolved |
| F-010 Undocumented `scaffold/` branch type | Minor | Naming standard now allows `scaffold` for initial foundation work only | Resolved |
| F-011 Missing reserved filename | Minor | `ARTIFACT-REGISTER.yaml` added to reserved filenames | Resolved |
| F-012 CI action pinning policy | Minor | Deferred to Phase 1 release/security architecture; not a Phase 0 blocker | Accepted deferral |

## Additional corrections completed

- Rewrote the three core standards with canonical metadata and tighter scope.
- Updated all five trials to canonical dependency objects.
- Registered active scripts, tests, infrastructure, and review artifacts.
- Added source-register and internal-link validation.
- Enabled `--warnings-as-errors` for dependency and source-register validation.
- Updated the source register to distinguish current registered consumers from planned consumers.
- Passed the full CI suite after all corrections.

## Current automated evidence

The latest validation workflow passes:

- all 18 unit-test scenarios;
- artifact ID, path, dependency, frontmatter, cycle, and maturity validation;
- source-register validation with warnings treated as errors;
- internal-link validation;
- dependency metadata validation with warnings treated as errors.

## Artifact readiness for independent review

| Artifact | Internal pre-review decision |
|---|---|
| `STD-CORE-001` | Ready for independent review |
| `STD-CORE-002` | Ready for independent review |
| `STD-CORE-003` | Ready for independent review |
| Five Phase 0 trials | Ready for independent review |
| Artifact and source registers | Ready for independent review |
| Validation suite | Ready for independent review |

## Remaining gate

The package still requires a genuinely independent reviewer who did not author the material changes. That reviewer must record findings under issue #2 and cannot silently approve corrections made within the same review pass.

## Review outcome

**Internal pre-review: PASS TO INDEPENDENT REVIEW**

This outcome confirms that the initial internal critical and major findings were resolved. It does not authorise a status change to `IN REVIEW` or the start of substantive Phase 1 work.
