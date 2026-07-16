---
status: DRAFT
phase: 0
priority: critical
depends_on:
  - BUILD-ORDER.md
  - DEPENDENCIES.md
blocks:
  - release decisions
last_reviewed: 2026-07-17
---

# Repository Status

This is the authoritative high-level completion register.

## Current milestone

`v0.1 — Cursor Agent Foundation`

## Current activity

The complete initial repository scaffold has been created on branch `scaffold/repository-foundation`.

The scaffold currently contains 171 versioned files covering repository controls, Cursor rules, subagents, skills, architecture, standards, knowledge packs, schemas, templates, examples, evaluations, and validation scripts.

All generated files remain placeholders unless explicitly marked otherwise. Placeholder Cursor rules cannot apply, placeholder subagents must not be delegated work, and placeholder skills do not yet contain active Cursor skill frontmatter.

## Status definitions

| Status | Meaning |
|---|---|
| `PLACEHOLDER` | Scope and instructions exist; substantive content does not |
| `RESEARCH IN PROGRESS` | Evidence gathering has started |
| `DRAFT` | Substantive content exists but has not passed review |
| `IN REVIEW` | Acceptance criteria are being assessed |
| `APPROVED` | Authoritative and available to dependent artifacts |
| `SUPERSEDED` | Replaced by a named authoritative artifact |

## Phase summary

| Phase | Name | Status |
|---:|---|---|
| 0 | Repository controls | DRAFT |
| 1 | Architecture and standards | PLACEHOLDER |
| 2 | Schemas and templates | PLACEHOLDER |
| 3 | Audience and decision foundation | PLACEHOLDER |
| 4 | Holistic P&R foundation | PLACEHOLDER |
| 5 | Specialist P&R domains | PLACEHOLDER |
| 6 | Consulting communication | PLACEHOLDER |
| 7 | Visual-design foundation | PLACEHOLDER |
| 8 | Visualisation patterns | PLACEHOLDER |
| 9 | Dashboard experience | PLACEHOLDER |
| 10 | Power BI implementation | PLACEHOLDER |
| 11 | Orchestrator and subagents | PLACEHOLDER |
| 12 | Evaluation and validation | PLACEHOLDER |
| 13 | Integration and release | PLACEHOLDER |

## Completed scaffold groups

- Repository controls and top-level project files
- Four safe, non-applying Cursor rule placeholders
- Three non-operational Cursor subagent placeholders
- Forty-nine Cursor skill placeholders across nine capability groups
- Architecture, standards, and planning placeholders
- Audience, P&R, consulting, visual-design, visualisation, and Power BI knowledge placeholders
- Eight output schemas and nine output templates
- Audience and format example locations
- Five benchmark scenarios with expected-result locations
- Five validation-script placeholders

## Immediate next steps

1. Review and merge the scaffold pull request.
2. Complete Phase 0 standards in the order defined by `BUILD-ORDER.md`.
3. Replace generic phase and dependency metadata with file-specific values.
4. Build the detailed machine-validated dependency and status index.
