---
status: DRAFT
phase: 0
priority: critical
depends_on: []
blocks:
  - all dependent artifacts
last_reviewed: 2026-07-17
---

# Artifact Dependency Map

## Core dependency chain

```text
Research and authoring standards
        ↓
Architecture and routing model
        ↓
Schemas
        ↓
Audience framework
        ↓
Holistic P&R value-driver tree
        ↓
Specialist P&R domain packs
        ↓
Consulting and visual-design knowledge
        ↓
Dashboard and chart-selection skills
        ↓
Power BI implementation skills
        ↓
Orchestrator and subagents
        ↓
Evaluation and release
```

## Rules

1. Each artifact must declare `depends_on` and `blocks` in frontmatter.
2. A dependent file must link to its authoritative source instead of duplicating it.
3. A placeholder may identify planned dependencies but cannot satisfy them.
4. `APPROVED` artifacts are authoritative unless explicitly superseded.
5. Circular dependencies must be resolved before approval.
6. Validation scripts will eventually compare file frontmatter with this register.

## Dependency groups

| Group | Must exist first | Primary consumers |
|---|---|---|
| Repository standards | None | All artifacts |
| Architecture | Repository standards | Rules, agents, skills |
| Schemas | Architecture and standards | Templates, skills, evaluation |
| Audience knowledge | Architecture and schemas | Discovery, KPI, UX, storyline skills |
| P&R foundation | Research standard and audience framework | Domain skills, KPI catalogue |
| Consulting knowledge | Research and citation standards | Storyline and static-design skills |
| Visual-design knowledge | Research and citation standards | Visualisation, UX, QA skills |
| Power BI knowledge | Design patterns and current official documentation | Implementation skills and verifier |
| Orchestrator | Stable foundational skills and routing model | Final Cursor agent |
| Evaluation | Schemas, skills, examples | Release decisions |

## File-level register

The complete file-level dependency register will be generated after the scaffold is committed. It must include a unique artifact ID, phase, minimum prerequisite status, and downstream consumers for every substantive file.
