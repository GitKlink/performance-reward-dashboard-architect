---
artifact_id: STD-CORE-006
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: ARCH-CORE-003
    path: ../architecture/skill-routing-model.md
  - artifact_id: STD-CORE-005
    path: example-authoring-standard.md
blocks:
  - evaluation rubric
  - release quality gates
content_version: 0.0.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Evaluation standard

## Purpose

Define how the agent, skills, routing, knowledge, outputs, and releases are tested consistently.

## What this file must establish

- Evaluation dimensions and severity levels
- Scenario, expected-result, and reviewer requirements
- Deterministic checks versus judgement-based review
- Audience, P&R, analytical, visual, accessibility, Power BI, evidence, and governance criteria
- Routing false-positive and false-negative tests
- Regression-test process
- Human review and disagreement resolution
- Release-blocking failure conditions

## Required outputs

- Evaluation rubric
- Severity and weighting model
- Benchmark-case format
- Expected-result format
- Regression process
- Review record and sign-off requirements
- Release threshold

## Acceptance criteria

- Different reviewers can apply the rubric consistently
- Critical metric, evidence, privacy, and audience failures cannot be averaged away
- Acceptable alternative designs are permitted where the decision logic remains sound
- Static and interactive products are evaluated differently where appropriate
- Results are versioned and traceable to the tested agent state
