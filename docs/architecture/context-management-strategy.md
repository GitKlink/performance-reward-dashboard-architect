---
artifact_id: ARCH-CORE-002
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: STD-CORE-001
    path: ../standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../standards/research-standard.md
  - artifact_id: EX-CORE-001
    path: ../../knowledge/research-register/trials/cursor-rules-and-skills-trial.md
blocks:
  - ARCH-CORE-003
  - Cursor rules
  - subagent handoffs
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Context-management strategy

## Purpose

Define how the Cursor agent keeps the main context focused while retaining durable project knowledge and traceable design decisions.

## What this file must establish

- What belongs in persistent rules, dynamically loaded skills, subagent context, project files, and handoff artifacts
- Context budgets and warning thresholds
- Progressive loading and reference-selection rules
- Major-phase handoff requirements
- How the agent avoids importing whole research packs unnecessarily
- How approved decisions and artifacts replace conversation memory
- Isolation rules for research, critique, implementation, and evaluation tasks
- How prior projects and examples are selected without contaminating current work

## Research required

- Current Cursor context behaviour and supported component boundaries
- Findings from the current-product trial
- Practical patterns for long-running Cursor projects
- Failure modes from oversized prompts and duplicated instructions

## Required outputs

- Context-layer model
- Loading and summarisation rules
- Subagent handoff contracts
- Phase-transition protocol
- Context-risk checklist
- Re-entry and recovery process
- Metrics for detecting context overload or duplication

## Acceptance criteria

- The main agent does not load all knowledge packs by default
- Persistent context remains small and stable
- Research detail can be reconstructed from repository artifacts
- Subagents receive only the context needed for their task
- Handoffs preserve decisions, dependencies, and open questions
- The strategy has been trialled on a multi-page dashboard design and a deep-research task

## Files that consume this content

- Skill-routing model
- Skill-authoring standard
- Main Cursor rule
- Subagent definitions
- Research and implementation handoff templates
