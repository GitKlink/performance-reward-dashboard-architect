---
artifact_id: ARCH-CORE-003
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: ARCH-CORE-002
    path: context-management-strategy.md
blocks:
  - active Cursor skills
  - main orchestrator rule
  - routing evaluations
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Skill-routing model

## Purpose

Define how Cursor selects the minimum appropriate set of skills for each dashboard-design request.

## What this file must establish

- Routing dimensions: audience, decision mode, Performance & Reward domain, consumption mode, workflow stage, and requested output
- Automatic versus explicit invocation rules
- Required foundational skills
- Specialist-skill selection and exclusion rules
- Skill sequencing and dependency handling
- Conflict resolution when multiple skills make competing recommendations
- When to delegate to a subagent
- How to avoid overloading context with irrelevant capabilities

## Required outputs

- Routing decision tree
- Skill dependency graph
- Invocation matrix
- Example routing traces
- Fallback and ambiguity protocol
- Evaluation cases for false-positive and false-negative routing

## Acceptance criteria

- The same request routes differently for executives, Business Partners, managers, and specialist teams where appropriate
- Static, interactive, and hybrid outputs trigger different capabilities
- Domain skills are not invoked without relevant business questions
- The minimum sufficient skill set is preferred
- Routing can be tested deterministically against benchmark scenarios

## Files that consume this content

- Skill-authoring standard
- Main Cursor rule
- Subagent definitions
- Evaluation standard and routing benchmarks
