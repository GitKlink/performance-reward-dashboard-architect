---
status: DRAFT
activation: DISABLED
phase: 2
priority: critical
depends_on:
  - knowledge/performance-reward/holistic-value-driver-tree.md
  - knowledge/performance-reward/performance-management.md
  - knowledge/performance-reward/governance-and-controls.md
blocks:
  - performance management benchmark scenarios
  - performance outcome reporting workflow
last_reviewed: 2026-07-31
---

# Performance management analysis

## Purpose

Provide a repeatable method for analysing performance-management process health, assessment quality, calibration, final outcomes, fairness signals, governance, and downstream reward implications.

This draft remains non-invokable until its dependencies, evaluations, examples, and activation metadata are approved.

## Invoke when

Use this skill when the user needs to:

- design a performance-cycle, calibration, outcome, or manager-action dashboard;
- analyse completion, timeliness, outcome distributions, calibration movement, or manager patterns;
- connect performance outcomes to fixed or variable reward without collapsing the domains;
- assess assessment quality, fairness, consistency, overrides, appeals, or corrections;
- define performance-management semantic-model requirements;
- prepare executive, HRBP, Reward Partner, Performance Partner, manager, or governance reporting.

## Do not invoke when

Do not use this skill for:

- generic project performance or operational KPI tracking;
- making a performance rating decision for an employee;
- defining disciplinary or employee-relations outcomes;
- generic Power BI mechanics with no performance-management semantics;
- variable-reward analysis where performance outcome is only a supplied filter and no performance interpretation is required.

## Required inputs

Collect or mark as unknown:

- audience and decision;
- performance cycle and stage;
- eligible population and exclusions;
- outcome scale and definitions;
- goal, behaviour, evidence, and check-in requirements;
- proposed, calibrated, final, communicated, and corrected states;
- calibration groups and authority;
- deadlines and completion events;
- organisation, position, level, manager, geography, demographic, leave, and service attributes;
- downstream reward or talent uses;
- privacy, security, suppression, and retention rules.

## Progressive loading

Always load:

1. `knowledge/performance-reward/holistic-value-driver-tree.md`
2. `knowledge/performance-reward/performance-management.md`

Load conditionally:

- variable reward for bonus differentiation and multiplier analysis;
- fixed reward for salary-review linkage;
- governance and controls for approval, audit, exception, and correction analysis;
- pay equity for protected-group and comparable-work investigation;
- talent and retention for development, potential, succession, or critical-person implications;
- job architecture for level and role comparability.

## Method

### 1. Frame the decision

State the decision-maker, cycle stage, decision required, population, value at stake, and whether the output is operational, calibration-oriented, executive, or post-cycle.

### 2. Lock lifecycle state

Identify whether records represent eligibility, goal setting, check-in, proposed assessment, calibrated outcome, final outcome, communication, appeal, or correction. Do not mix these states silently.

### 3. Validate population and scale

Confirm eligible population, exclusions, cycle compatibility, outcome scale, role changes, manager history, joiners, movers, leave, and part-year treatment. Quantify missing or incompatible records.

### 4. Assess process readiness

Analyse completion, timeliness, overdue actions, evidence availability, check-in cadence, and unresolved exceptions. Treat readiness as an operational prerequisite rather than a quality conclusion.

### 5. Analyse outcome patterns

Review count and percentage distributions, concentration, absence of differentiation, level and portfolio mix, manager profiles, small populations, and historical comparison. Do not impose an expected shape without policy authority.

### 6. Analyse calibration

Compare proposed with calibrated and final outcomes. Measure upward, downward, and unchanged movement; magnitude; affected populations; calibration group; manager; and documented rationale. Preserve before-and-after states.

### 7. Test quality and fairness

Assess evidence sufficiency, unsupported overrides, manager severity or leniency, demographic and leave-status signals, comparable-work populations, and consistency across appropriate peers. Control for legitimate factors before escalation.

### 8. Connect downstream decisions

Where reward or talent is in scope, preserve the chain from performance evidence to final outcome to downstream recommendation and approval. Do not assume a deterministic rating-to-reward mapping.

### 9. Review governance

Check approval authority, traceability, access, exception evidence, correction controls, minimum-population safeguards, and downstream transmission of approved outcomes only.

### 10. Produce decision-ready output

Separate evidence, interpretation, hypothesis, recommendation, and decision required. Return only the level of detail authorised for the audience.

## Audience routes

### Executive route

Prioritise cycle readiness, final differentiation, material portfolio variation, strategic alignment, fairness and governance signals, reward implications, and decisions required.

### Performance or Reward Partner route

Prioritise proposed and final distributions, manager profiles, calibration movement, evidence gaps, exceptions, and translation into reward outcomes.

### HR Business Partner route

Prioritise team and leader patterns, incomplete actions, quality concerns, workforce context, fairness signals, and intervention priorities.

### People Leader route

Prioritise authorised employee actions, evidence completeness, proposed outcomes, calibration changes, deadlines, exceptions, and submission status.

### Governance and HRIS route

Prioritise eligibility, state transitions, approval authority, audit trail, access, appeals, corrections, and downstream reconciliation.

## Microsoft Power BI delegation

Delegate generic semantic-model implementation, DAX syntax, visual construction, interaction mechanics, performance optimisation, and standard security patterns where maintained Microsoft skills cover them.

Before delegation, provide:

- lifecycle states;
- required facts and grains;
- effective-dating rules;
- outcome scale;
- population logic;
- calibration-group requirements;
- privacy and suppression rules;
- downstream linkage boundaries;
- reconciliation requirements.

Reject technically valid designs that overwrite lifecycle states, use current hierarchy for historical accountability, or expose sensitive evidence improperly.

## Output contract

Return, as applicable:

1. decision statement and audience;
2. cycle stage and population definition;
3. lifecycle-state map;
4. readiness and data-quality assessment;
5. KPI definitions with grain, time basis, numerator, denominator, and exclusions;
6. outcome, manager, and calibration diagnostics;
7. fairness and governance tests;
8. downstream reward or talent linkage;
9. recommended information architecture;
10. semantic-model implications;
11. assumptions and unresolved policy inputs;
12. decisions required.

## Quality checks

Verify that:

- proposed, calibrated, final, and corrected outcomes remain distinct;
- completion is not presented as assessment quality;
- no target distribution is assumed without policy authority;
- manager comparisons control for population size and workforce mix;
- historical manager and organisation attributes use the correct date;
- descriptive differences are not labelled causal;
- reward linkage preserves separate recommendation and approval stages;
- comments and evidence remain restricted;
- small populations are suppressed or qualified;
- the output does not make the employee performance decision.

## Failure conditions

Stop or qualify when:

- eligible population cannot be reconstructed;
- outcome scales or cycles are incompatible and unmapped;
- lifecycle states have been overwritten;
- proposed and final outcomes cannot be distinguished for calibration analysis;
- current hierarchy has replaced cycle-time accountability;
- required evidence or stage dates are materially incomplete;
- privacy rules do not permit the requested detail;
- organisation-specific calibration or rating policy is being assumed.

## Activation gate

Do not change `activation: DISABLED` until:

- the performance-management and governance dependencies are reviewed;
- the skill-authoring standard is satisfied;
- at least two benchmark scenarios pass, including one calibration scenario and one executive outcome scenario;
- routing tests distinguish performance management from variable reward, talent, and generic operational-performance requests;
- Microsoft delegation and fallback behaviour is verified.