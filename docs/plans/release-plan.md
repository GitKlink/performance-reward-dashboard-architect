---
artifact_id: PLAN-CORE-003
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: ARCH-CORE-005
    path: ../architecture/release-architecture.md
  - artifact_id: STD-CORE-006
    path: ../standards/evaluation-standard.md
  - artifact_id: PLAN-CORE-002
    path: implementation-roadmap.md
blocks:
  - tagged releases
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Release plan

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until package-building scripts, release manifests, approval roles, and a release-candidate rehearsal are implemented.

## Purpose

Define the operational sequence for preparing, validating, reviewing, approving, publishing, maintaining, and rolling back releases of the Performance & Reward Dashboard Architect.

## Release objectives

A release must be:

- reproducible from a tagged source commit;
- compatible with the declared Cursor environment;
- complete with all required runtime dependencies;
- free of placeholders and unapproved runtime content;
- tested through the integrated benchmark suite;
- safe for public distribution;
- clear about limitations, configuration, and migration;
- reversible to a prior known-good version.

## Release types

### Initial release

```text
v0.1.0
```

Establishes the first coherent public runtime package and compatibility baseline.

### Minor release

```text
v0.x.0
```

Adds backward-compatible capabilities, knowledge, examples, or implementation support.

Before `v1.0.0`, a minor release may contain breaking changes, but they must be declared prominently and include migration instructions.

### Patch release

```text
v0.x.y
```

Corrects defects without intentionally changing public contracts.

### Hotfix

Urgent patch for:

- security or privacy defect;
- materially misleading KPI or P&R guidance;
- broken runtime discovery;
- package integrity failure;
- critical compatibility regression.

### Release candidate

```text
v0.1.0-rc.1
v0.1.0-rc.2
```

Used for frozen package and integrated Phase 12 evaluation.

### Development snapshot

Optional non-release build tied to a commit. It must be clearly labelled unsupported and must not use a stable release tag.

## Version decision rules

Increment major or pre-`1.0` minor when changing:

- runtime package layout incompatibly;
- skill or subagent invocation contracts;
- schema fields incompatibly;
- required configuration;
- organisation-overlay strategy;
- minimum Cursor support materially;
- removed or renamed capabilities without compatibility aliases.

Increment minor when adding:

- new backward-compatible skill;
- new P&R domain pack;
- new optional package profile;
- new approved examples or benchmarks;
- additional Power BI implementation guidance.

Increment patch when correcting:

- wording or evidence citation;
- routing description without contract change;
- formula implementation defect while preserving the approved definition;
- packaging or link issue;
- non-breaking validation defect.

## Release roles

| Role | Responsibility |
|---|---|
| Product decision owner | confirms release scope and acceptable residual risks |
| Release coordinator | manages freeze, checklist, package, tag, and publication |
| Artifact owners | confirm readiness and resolve findings |
| Technical verifier | validates Cursor and Power BI compatibility |
| Evidence reviewer | verifies current sources, citations, and licences |
| Privacy and security reviewer | checks sensitive content, permissions, scripts, and package safety |
| Independent reviewer | conducts Phase 12 integrated review |
| Release authority | records final approval or rejection |

During early development one person may cover several roles. The independent review and final risk acceptance must still be explicit.

## Approval matrix

| Decision | Required authority |
|---|---|
| Define release scope | product decision owner |
| Freeze release candidate | release coordinator and product owner |
| Close critical or major architecture finding | artifact owner plus independent reviewer verification |
| Accept minor residual risk | product decision owner or release authority |
| Approve privacy or security exception | accountable privacy or security authority |
| Publish stable release | release authority |
| Initiate critical rollback | release coordinator or release authority |
| Remove compromised release | release authority |

## Release stages

### Stage 1 — Scope

Create a release issue containing:

- target version;
- package profiles;
- included capabilities;
- deferred capabilities;
- compatibility target;
- known risks;
- milestone and benchmark requirements;
- intended release window where relevant.

### Stage 2 — Readiness inventory

Review `ARTIFACT-REGISTER.yaml` and identify:

- runtime entry points;
- mandatory runtime dependencies;
- status and content versions;
- placeholder or draft blockers;
- source freshness requirements;
- migration impacts;
- owners.

### Stage 3 — Source freeze

- choose candidate commit;
- stop unrelated changes to the release branch;
- update changelog and status;
- freeze manifest inputs;
- create release-candidate tag or branch;
- record exact Cursor and other test environments.

### Stage 4 — Build package profiles

Build from a clean environment:

- minimal runtime package;
- standard runtime package where planned;
- contributor source tag.

Generate:

- `RELEASE-MANIFEST.yaml`;
- file hashes;
- package inventory;
- exclusion report;
- licence and attribution files;
- migration notes where required.

### Stage 5 — Automated validation

Run against both source and staged package:

- unit tests;
- artifact dependency validation;
- source-register validation;
- internal-link validation;
- schema validation;
- skill metadata and discovery validation;
- package dependency closure;
- status and placeholder exclusion;
- manifest and checksum validation;
- secret and private-information scanning;
- archive path and symlink safety;
- reproducibility check.

### Stage 6 — Runtime smoke testing

In a clean Cursor workspace:

- install or copy the package;
- verify rules, skills, subagents, commands, and hooks included in the profile;
- test automatic and explicit invocation;
- resolve referenced knowledge, schemas, templates, assets, and scripts;
- run one executive, Business Partner, manager, and KPI-definition smoke scenario;
- record actual Cursor version and observed limitations.

### Stage 7 — Phase 12 integrated evaluation

Execute:

- complete benchmark suite;
- routing false-positive and false-negative tests;
- context and handoff tests;
- cross-skill contradiction analysis;
- P&R and KPI review;
- static, interactive, hybrid, and export scenarios;
- Power BI feasibility and implementation review;
- accessibility review;
- evidence, privacy, security, and licensing review;
- independent architecture and product review.

### Stage 8 — Correction cycle

For every critical or major finding:

1. record the finding before correction;
2. assign the owning artifact;
3. implement the correction;
4. add a regression case where applicable;
5. rebuild affected packages;
6. rerun relevant local tests;
7. rerun the integrated affected suite;
8. obtain independent closure verification.

Create a new release candidate when package contents change materially.

### Stage 9 — Final approval

The release authority reviews:

- manifest;
- benchmark and regression results;
- open findings;
- residual risks;
- compatibility statement;
- privacy, security, and licence evidence;
- migration and rollback plans;
- package hashes.

Record one decision:

```text
APPROVED FOR RELEASE
REJECTED — CRITICAL FINDINGS
REJECTED — MAJOR FINDINGS
DEFERRED — SCOPE OR COMPATIBILITY
```

### Stage 10 — Publish

- create stable tag;
- publish GitHub release;
- attach package archives and checksums;
- publish release notes;
- link migration guidance;
- update `STATUS.md` and `CHANGELOG.md`;
- close the release issue;
- retain release evidence.

### Stage 11 — Post-release review

- confirm download and package integrity;
- monitor reported discovery, routing, compatibility, or content defects;
- verify documentation links;
- classify incidents;
- update source freshness triggers;
- schedule patch or next-version work.

## Branch and pull-request model

Recommended after the initial foundation branch:

```text
main                         # stable source history
feat/<capability>            # bounded feature work
docs/<scope>                 # documentation and knowledge
research/<scope>             # evidence work
release/<version>            # short-lived release preparation
fix/<defect>                 # corrections
```

Release work should not continue indefinitely in the original scaffold pull request.

Before Milestone 2, decide whether to:

- merge the foundation and Phase 1 drafts into `main`; or
- create a clean Phase 2 branch from the current foundation head.

## Release checklist

### Scope and status

- [ ] release version chosen;
- [ ] package profiles chosen;
- [ ] included and deferred capabilities listed;
- [ ] runtime artifacts registered;
- [ ] runtime artifacts and mandatory dependencies approved;
- [ ] placeholders excluded;
- [ ] changelog updated.

### Compatibility

- [ ] current Cursor documentation rechecked;
- [ ] tested Cursor versions recorded;
- [ ] skill and subagent discovery tested;
- [ ] command and hook behaviour tested where included;
- [ ] script runtime requirements recorded;
- [ ] Power BI assumptions rechecked where material.

### Validation

- [ ] source CI green;
- [ ] package validators green;
- [ ] schemas validate;
- [ ] dependency closure complete;
- [ ] manifest matches archive;
- [ ] checksums generated and verified;
- [ ] clean-workspace smoke tests pass;
- [ ] benchmark and regression suite passes.

### Review

- [ ] independent review complete;
- [ ] critical findings closed;
- [ ] major findings closed;
- [ ] accepted minor risks recorded;
- [ ] P&R and KPI review complete;
- [ ] accessibility review complete;
- [ ] privacy and security review complete;
- [ ] evidence and licensing review complete.

### Documentation

- [ ] consumer README complete;
- [ ] release notes complete;
- [ ] compatibility notes complete;
- [ ] configuration documented;
- [ ] migration notes complete where required;
- [ ] rollback procedure verified;
- [ ] known limitations visible.

### Publication

- [ ] final source commit recorded;
- [ ] stable tag created;
- [ ] archives attached;
- [ ] checksums published;
- [ ] release approval recorded;
- [ ] status updated;
- [ ] release issue closed.

## Release note template

```markdown
# Performance & Reward Dashboard Architect <version>

## Summary

## Included capabilities

## Package profiles

## Compatibility

## Installation or upgrade

## Breaking changes

## Improvements

## Fixes

## Known limitations

## Validation and review

## Privacy, security, and licensing

## Migration

## Rollback

## Source commit and checksums
```

## Migration-note template

```markdown
# Migration from <old-version> to <new-version>

## Who needs to migrate

## Breaking changes

## Renamed or moved artifacts

## Schema changes

## Skill and invocation changes

## Configuration changes

## Automatic steps

## Manual steps

## Validation after migration

## Rollback

## Known incompatibilities
```

## Release manifest review

The release coordinator verifies:

- source commit matches tag;
- package profile is correct;
- included artifact IDs and versions match source;
- required entry points exist;
- all dependency paths resolve;
- hashes match;
- exclusions are intentional;
- compatibility and limitations are visible;
- review evidence is linked.

## Rollback procedure

### Trigger conditions

- critical security or privacy defect;
- materially incorrect P&R or KPI guidance;
- broken runtime discovery for core capabilities;
- package corruption;
- widespread compatibility failure;
- migration causing data or configuration loss.

### Steps

1. Stop promoting or distributing the affected version.
2. Identify the last known-good release.
3. Publish a release warning.
4. Preserve evidence and affected package.
5. Restore the prior package and configuration.
6. Run smoke and regression tests.
7. Record the rollback in status and changelog.
8. Open a hotfix issue with severity and root cause.
9. Revoke or remove the affected release where continued availability is unsafe.

### Rollback validation

- previous manifest matches restored files;
- runtime discovery works;
- organisation overlays remain intact;
- benchmark smoke tests pass;
- security or privacy exposure is contained;
- consumers receive clear instructions.

## Hotfix process

A hotfix may use a reduced scope but cannot skip:

- defect reproduction;
- owning-artifact correction;
- regression case;
- package rebuild;
- relevant security, privacy, evidence, or compatibility review;
- final approval.

The independent review may be limited to the affected surface when the release authority documents why broader review is unnecessary.

## Deprecation process

When deprecating a skill, schema, command, package profile, or compatibility target:

1. announce deprecation and replacement;
2. identify last supported version;
3. provide migration guidance;
4. stop automatic routing to the deprecated capability where appropriate;
5. retain compatibility aliases for the declared period where feasible;
6. remove in a documented breaking release;
7. preserve historical artifacts for reproducibility.

## Post-release monitoring

Track:

- installation failures;
- skill or subagent discovery failures;
- unexpected automatic routing;
- context overload;
- broken references or package dependencies;
- incorrect P&R or KPI outputs;
- Power BI feasibility defects;
- accessibility issues;
- privacy or security incidents;
- stale current-product sources;
- migration and overlay conflicts.

## Incident severity

Use the evaluation severity model.

Examples:

- critical: privacy exposure or materially misleading financial allocation guidance;
- major: core skill inaccessible or wrong audience routing across common prompts;
- minor: one broken example link or local formatting defect;
- editorial: release-note wording.

## Post-release cadence

### Within 24 hours of release

- verify assets and checksums;
- confirm installation instructions;
- review immediate defects.

### After initial adoption

- review routing and compatibility reports;
- capture regressions;
- update next-version backlog.

### Before each subsequent release

- refresh current Cursor and Power BI evidence;
- review unresolved incidents;
- verify deprecated capabilities and migrations;
- rerun complete applicable release checks.

No fixed calendar cadence is required before adoption levels and maintenance capacity are understood.

## `v0.1.0` release-specific plan

### Required package

- minimal runtime profile;
- standard profile if selected examples are ready;
- contributor source tag.

### Required capabilities

- thin orchestrator;
- foundational skills defined in the implementation roadmap;
- three focused subagents where current Cursor support is verified;
- audience and holistic P&R knowledge;
- initial fixed reward, performance, and variable reward coverage;
- output schemas and templates;
- five primary benchmark scenarios plus adversarial cases;
- validation and release manifest.

### Required proof

- complete workflow in a clean Cursor workspace;
- executive, Business Partner, and manager products are materially distinct;
- KPI definitions are complete and implementable;
- static and interactive outputs behave as declared;
- no unresolved critical or major finding;
- package reproducible from tag.

## Anti-patterns

- Publishing directly from a working development directory.
- Building archives before manifest scope is frozen.
- Treating a green source CI run as package validation.
- Including all knowledge and examples by default.
- Shipping draft or placeholder runtime files.
- Reusing a stable version after package contents change.
- Omitting migration notes because the release is pre-`1.0`.
- Allowing authors to close their own critical findings without independent verification.
- Publishing without testing in a clean Cursor workspace.
- Relying on current-product assumptions recorded months earlier.
- Hiding known limitations in issue comments rather than release documentation.
- Performing a hotfix without adding a regression.

## Draft acceptance assessment

This draft defines:

- release types and versioning;
- roles and approval matrix;
- eleven release stages;
- branch and pull-request model;
- comprehensive release checklist;
- release, migration, rollback, hotfix, and deprecation procedures;
- monitoring and incident handling;
- `v0.1.0`-specific scope and proof.

It must be rehearsed with a generated release-candidate package before status changes.
