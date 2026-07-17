---
artifact_id: STD-CORE-005
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: STD-CORE-001
    path: naming-standard.md
  - artifact_id: STD-CORE-002
    path: research-standard.md
  - artifact_id: STD-CORE-003
    path: citation-standard.md
  - artifact_id: EX-CORE-001
    path: ../../knowledge/research-register/trials/cursor-rules-and-skills-trial.md
  - artifact_id: EX-CORE-002
    path: ../../knowledge/research-register/trials/internal-source-of-truth-decision-trial.md
  - artifact_id: EX-FIXED-001
    path: ../../knowledge/research-register/trials/new-hire-premium-kpi-trial.md
  - artifact_id: EX-CONSULT-001
    path: ../../knowledge/research-register/trials/consulting-attribution-trial.md
  - artifact_id: EX-VIZ-001
    path: ../../knowledge/research-register/trials/graphical-perception-trial.md
blocks:
  - worked examples
  - benchmark scenarios
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Example-authoring standard

## Purpose

Define how worked examples and benchmark inputs demonstrate approved behaviour without creating hidden rules or exposing sensitive information.

## What this file must establish

- Example types and intended uses
- Required audience, decision, domain, consumption mode, assumptions, and constraints
- Synthetic-data and privacy requirements
- How examples reference approved skills, knowledge, schemas, and templates
- How acceptable design alternatives are represented
- How incomplete, adversarial, and failure examples are written
- Versioning and review requirements

## Required outputs

- Example template
- Benchmark-input template
- Expected-result structure
- Synthetic-data standard
- Redaction checklist
- Valid and invalid examples

## Acceptance criteria

- Examples are reproducible without conversation memory
- Inputs and expected behaviour are clearly separated
- Fictional values cannot be mistaken for real organisational data
- Examples do not silently override approved methods
- At least executive, Business Partner, manager, interactive, and static scenarios are represented
