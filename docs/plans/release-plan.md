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
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Release plan

## Purpose

Define the operational sequence for preparing, validating, approving, publishing, and maintaining tagged releases.

## What this file must establish

- Release types and versioning rules
- Candidate, approval, and publication stages
- Required validation and review evidence
- Package assembly and manifest checks
- Changelog and migration-note requirements
- Public-repository safety review
- Rollback, hotfix, and deprecation process
- Post-release monitoring and refresh triggers

## Required outputs

- Release checklist
- Approval matrix
- Tagging and package procedure
- Release-note template
- Migration-note template
- Rollback procedure
- Post-release review schedule

## Acceptance criteria

- A release cannot include placeholders or unapproved runtime dependencies
- Benchmark and validation results are recorded against the exact release commit
- Package contents match the approved release architecture
- Licensing, privacy, and source freshness checks are complete
- Consumers can determine compatibility and upgrade impact
