---
artifact_id: STD-CORE-004
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: ARCH-CORE-002
    path: ../architecture/context-management-strategy.md
  - artifact_id: ARCH-CORE-003
    path: ../architecture/skill-routing-model.md
  - artifact_id: STD-CORE-001
    path: naming-standard.md
  - artifact_id: STD-CORE-002
    path: research-standard.md
  - artifact_id: STD-CORE-003
    path: citation-standard.md
blocks:
  - all active Cursor skills
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Skill-authoring standard

## Purpose

Define the mandatory structure, invocation logic, evidence boundaries, context strategy, and quality requirements for every active Cursor skill.

## What this file must establish

- Current supported Cursor skill metadata
- Folder and `SKILL.md` naming rules
- Required purpose, triggers, exclusions, inputs, method, outputs, references, examples, anti-patterns, and quality checks
- Automatic versus explicit invocation treatment
- How skills reference shared knowledge without duplicating it
- Context-loading and script-use rules
- Status and activation controls
- Versioning and compatibility requirements

## Required outputs

- Canonical skill template
- Frontmatter schema
- Description-writing rules for reliable routing
- Required and optional sections
- Activation checklist
- Worked valid and invalid examples
- Validation requirements

## Acceptance criteria

- Active skill metadata is verified against current official Cursor documentation
- Folder name and skill name agree
- Invocation and non-invocation conditions are testable
- Each skill has a bounded responsibility and structured output contract
- Supporting knowledge remains authoritative outside the skill where appropriate
- At least two benchmark scenarios pass before approval
- Placeholder skills cannot be discovered as active capabilities
