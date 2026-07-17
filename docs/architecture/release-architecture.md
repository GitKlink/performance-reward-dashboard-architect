---
artifact_id: ARCH-CORE-005
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: ARCH-CORE-004
    path: information-architecture.md
  - artifact_id: EX-CORE-002
    path: ../../knowledge/research-register/trials/internal-source-of-truth-decision-trial.md
blocks:
  - release plan
  - package validation
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Release architecture

## Purpose

Define how the maintained source repository produces a stable, reviewable Cursor agent release.

## What this file must establish

- Source repository versus release-package boundaries
- Required runtime and support artifacts
- Development-only exclusions
- Versioning and compatibility rules
- Packaging, validation, and integrity checks
- Treatment of optional knowledge packs and examples
- Upgrade and migration behaviour
- Rollback and superseded-release handling
- Public-release checks for privacy, licensing, and confidential content

## Required outputs

- Release-content manifest
- Packaging workflow
- Compatibility matrix
- Release quality gates
- Migration and rollback procedure
- Rules for tags, changelog entries, and generated archives

## Acceptance criteria

- A release can be reproduced from a tagged source commit
- The package includes every referenced runtime dependency
- Development placeholders and unapproved content are excluded
- No confidential or licensed material is exposed
- A consumer can identify version, prerequisites, and upgrade impact
- The source repository remains the authority after packaging
