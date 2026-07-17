---
artifact_id: ARCH-CORE-001
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: STD-CORE-001
    path: ../standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../standards/citation-standard.md
  - artifact_id: EX-CORE-001
    path: ../../knowledge/research-register/trials/cursor-rules-and-skills-trial.md
  - artifact_id: EX-CORE-002
    path: ../../knowledge/research-register/trials/internal-source-of-truth-decision-trial.md
blocks:
  - ARCH-CORE-002
  - ARCH-CORE-003
  - STD-CORE-004
  - final Cursor agent structure
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Agent architecture

## Purpose

Define the complete Cursor-native component architecture for the Performance & Reward Dashboard Architect.

## What this file must establish

- Product boundary and intended users
- Main-agent responsibilities and exclusions
- Roles of project rules, Agent Skills, subagents, commands, knowledge packs, templates, schemas, scripts, and evaluations
- Authoritative source hierarchy
- Development repository versus packaged release boundary
- Human decision points and escalation boundaries
- How interactive and static dashboard-design workflows fit the architecture
- How Performance & Reward domain knowledge is separated from reusable methods
- Context, privacy, evidence, and public-repository constraints

## Research required

- Current official Cursor component capabilities and schemas
- Context-loading behaviour for rules, skills, subagents, and commands
- Relevant packaging and version-control practices
- Findings from the Phase 0 current-product and internal-decision trials

## Required outputs

- Component diagram
- Responsibility matrix
- Data and instruction flow
- Source-of-truth model
- Component selection rules
- Explicit anti-patterns
- Architecture decisions requiring separate records
- Dependencies for later architecture and standards files

## Acceptance criteria

- No component has overlapping authority without a resolution rule
- Detailed knowledge is not embedded in persistent rules
- The architecture can operate within Cursor context constraints
- Placeholder components cannot become active accidentally
- The release subset can be derived from the maintained source repository
- Current Cursor claims are supported by official evidence
- The design has been tested against at least three representative dashboard workflows

## Files that consume this content

- Context-management strategy
- Skill-routing model
- Information and release architecture
- Skill, example, and evaluation standards
- Main Cursor rule, subagents, and release plan
