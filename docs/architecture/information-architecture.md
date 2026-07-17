---
artifact_id: ARCH-CORE-004
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: STD-CORE-001
    path: ../standards/naming-standard.md
blocks:
  - repository navigation
  - release packaging
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Repository information architecture

## Purpose

Define how contributors and Cursor agents locate authoritative instructions, knowledge, examples, schemas, evaluations, and release assets.

## What this file must establish

- Repository navigation model
- Authoritative locations for each artifact type
- Cross-linking and index conventions
- Boundaries between `.cursor`, `knowledge`, `docs`, `schemas`, `templates`, `examples`, `evaluations`, and `scripts`
- Rules for local skill references versus shared knowledge packs
- How approved, draft, placeholder, and superseded content is surfaced
- Navigation for contributors who should not need to understand the entire internal structure

## Required outputs

- Repository map
- Artifact-location decision table
- Navigation entry points by contributor task
- Index-generation requirements
- Duplication and misplaced-content checklist

## Acceptance criteria

- A new contributor can locate the current authority for a concept without relying on chat history
- Runtime and development artifacts remain clearly separated
- Shared knowledge is not duplicated into multiple skill folders
- Generated indexes cannot become competing authorities
- Release packaging can identify required support files deterministically
