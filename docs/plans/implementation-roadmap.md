---
artifact_id: PLAN-CORE-002
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: CTRL-CORE-001
    path: ../../BUILD-ORDER.md
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: ARCH-CORE-003
    path: ../architecture/skill-routing-model.md
blocks:
  - milestone planning
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Implementation roadmap

## Purpose

Translate the approved build order and architecture into manageable milestones, deliverables, dependencies, and validation gates.

## What this file must establish

- Milestones and phased scope
- MVP versus later capability boundaries
- Required artifacts and owners per milestone
- Entry and exit criteria
- Dependencies and parallel workstreams
- Validation and review points
- Risks, assumptions, and resourcing constraints
- Rework and reprioritisation process

## Required outputs

- Milestone table
- Dependency-aware sequence
- Deliverable checklist
- Definition of done by phase
- Risk register
- Progress-reporting method

## Acceptance criteria

- The roadmap aligns with `BUILD-ORDER.md`
- No milestone assumes unapproved dependencies
- The first usable agent is intentionally narrower than the full catalogue
- Every milestone produces reviewable repository artifacts
- Context-heavy work is isolated and handed back through structured outputs
