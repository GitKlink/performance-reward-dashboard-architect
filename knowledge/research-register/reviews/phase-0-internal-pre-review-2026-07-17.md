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
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Phase 0 internal pre-review

## Review status

This is a rigorous internal pre-review performed before the required independent review. It does **not** satisfy the independent-review gate because it was conducted within the same implementation workflow.

## Scope

Reviewed:

- Phase 0 build and dependency controls;
- naming, research, and citation standards;
- the five required evidence and decision trials;
- artifact and source registers;
- validation scripts, tests, and CI workflow;
- readiness to move the core standards to `IN REVIEW`.

## Overall conclusion

**Not ready to move to `IN REVIEW`.**

The evidence model and trial design are strong, and automated validation passes. However, one critical governance deadlock and several major consistency issues must be resolved before an independent reviewer can assess a coherent Phase 0 package.

## Findings

### F-001 — Critical — Phase approval deadlock

**Affected artifacts:** `CTRL-CORE-001`, `STD-CORE-002`, `STD-CORE-003`

`BUILD-ORDER.md` requires Phase 0 standards to be `APPROVED` before substantive Phase 1 work. The research standard states that approval occurs only after successful use in Phase 3 and Phase 4 workstreams. The citation standard similarly defers approval until audience and holistic P&R knowledge packs are used.

This creates a dependency deadlock: later phases cannot begin until the standards are approved, while the standards cannot be approved until later phases have begun.

**Required correction:** Permit Phase 0 approval after the five representative trials, automated validation, and independent review. Require a mandatory post-implementation review after the first Phase 3 and Phase 4 applications rather than withholding initial approval.

### F-002 — Major — Research-record schema circular dependency

**Affected artifacts:** `STD-CORE-002`, `STD-CORE-003`, `ARTIFACT-REGISTER.yaml`

Both standards require the research-record schema to implement required fields before moving to `IN REVIEW`, while the standards block that schema and Phase 2 is formally downstream of Phase 1.

**Required correction:** For Phase 0 `IN REVIEW`, require a validated research-record field contract and successful trial records. Reserve formal schema approval for Phase 2. Alternatively move the research-record schema into Phase 0; the first option is preferred because it preserves the agreed build sequence.

### F-003 — Major — Artifact-type registry is incomplete

**Affected artifacts:** `STD-CORE-001`, `ARTIFACT-REGISTER.yaml`

The register contains `TEST-QA-001`, but the naming standard does not define the `TEST` type code. The active GitHub Actions workflow also lacks an appropriate governed artifact type.

**Required correction:** Add `TEST` and `INFRA` type codes, define their scope, reserve their namespaces, and register active tests and CI infrastructure.

### F-004 — Major — Active validators and workflow are not fully registered

**Affected artifacts:** `ARTIFACT-REGISTER.yaml`, `scripts/README.md`

The internal-link validator, source-register validator, their tests, and the GitHub Actions workflow are active but absent from the artifact register.

**Required correction:** Register every active validator, test suite, and workflow with immutable IDs and dependencies.

### F-005 — Major — Source-to-artifact references are partly descriptive

**Affected artifacts:** `KNOW-CORE-002`, `scripts/validate-source-register.py`

Several `relevant_artifacts` entries contain phrases such as `future context-management strategy` rather than immutable artifact IDs. The validator allows these as warnings, weakening traceability.

**Required correction:** Restrict `relevant_artifacts` to registered IDs. Add a separate optional `planned_consumers` field for future or not-yet-registered destinations. Migrate existing records and then promote source-register warnings to CI failures.

### F-006 — Major — Legacy dependency syntax remains in active Phase 0 artifacts

**Affected artifacts:** `STD-CORE-001`, `STD-CORE-002`, `STD-CORE-003`, Phase 0 trials and controls

The canonical metadata model uses dependency objects, but several active files still use path-only, colon-delimited, or one-key mapping forms. CI passes because legacy syntax is only warned.

**Required correction:** Migrate active Phase 0 and registered Phase 1 files to dependency objects, then run dependency validation with `--warnings-as-errors`.

### F-007 — Major — New-hire KPI candidate risks survivorship bias

**Affected artifact:** `EX-FIXED-001`

The candidate eligible population includes hires that are “active or valid at the relevant measurement point.” A historical new-hire premium should not normally exclude a qualifying hire merely because the employee later left, as this can bias the cohort and conceal problematic hiring outcomes.

**Required correction:** Include all valid eligible external starts in the selected hire cohort regardless of current employment status. Use employment status only for separate retention or outcome analysis. Exclude only invalid, rescinded, or non-commenced records according to an explicit rule.

### F-008 — Major — Independent review independence must be explicit

**Affected artifacts:** `STATUS.md`, issue #2, review process

The current implementation workflow cannot itself satisfy an independent review requirement.

**Required correction:** Require a reviewer who did not author the material changes, or a separately isolated review agent/process with no authority to silently approve its own corrections. This internal pre-review may prepare the package but cannot close issue #2.

### F-009 — Minor — Citation standard is not yet applied consistently to the standards

**Affected artifacts:** `STD-CORE-001`, `STD-CORE-002`

The naming and research standards use source-list links rather than the claim-level descriptive footnote model defined by `STD-CORE-003`.

**Required correction:** Before approval, migrate material external claims in the standards to the repository citation model, or explicitly document a temporary drafting exception that expires before approval.

### F-010 — Minor — Scaffold branch type is undocumented

**Affected artifact:** `STD-CORE-001`

The active branch is `scaffold/repository-foundation`, but `scaffold` is not included in the permitted branch types.

**Required correction:** Add `scaffold` as a temporary pre-release branch type or record the existing branch as a one-time exception and use approved types thereafter.

### F-011 — Minor — Reserved repository filenames are incomplete

**Affected artifact:** `STD-CORE-001`

`ARTIFACT-REGISTER.yaml` is a repository control using uppercase conventional naming but is absent from the reserved-filename list.

**Required correction:** Add it to the reserved list and clarify treatment of root-level machine-readable controls.

### F-012 — Minor — CI action references are version tags rather than immutable commits

**Affected artifact:** `.github/workflows/repository-validation.yml`

The workflow uses `actions/checkout@v4`. This is common and currently functional, but immutable commit pinning would provide stronger supply-chain control.

**Required correction:** Decide and document whether public release workflows must pin third-party actions to full commit SHAs. This is not a Phase 0 blocker unless the project adopts a strict supply-chain policy.

## Artifact readiness

| Artifact | Pre-review decision | Reason |
|---|---|---|
| `STD-CORE-001` | Remain `DRAFT` | Type registry, branch exception, filename list, and legacy metadata require correction |
| `STD-CORE-002` | Remain `DRAFT` | Approval deadlock and schema gate require correction |
| `STD-CORE-003` | Remain `DRAFT` | Approval deadlock and schema gate require correction |
| Five Phase 0 trials | Remain `DRAFT` | New-hire trial requires one material cohort correction; others are suitable for independent review |
| Validation suite | Remain `DRAFT` | Active artifacts require registration and warning policy hardening |

## Required sequence

1. Resolve F-001 to F-008.
2. Run all tests and validators with warnings promoted to errors.
3. Update the artifact register, status, and changelog.
4. Present the corrected package to a genuinely independent reviewer under issue #2.
5. Resolve independent critical and major findings.
6. Move eligible standards to `IN REVIEW`.

## Review outcome

**Internal pre-review: FAIL — CORRECTIONS REQUIRED**

The failure is procedural and consistency-related, not a rejection of the overall architecture. The repository should not begin substantive Phase 1 work until the critical and major findings are closed.
