---
status: DRAFT
activation: DISABLED
phase: 2
priority: critical
depends_on:
  - knowledge/performance-reward/holistic-value-driver-tree.md
  - knowledge/performance-reward/variable-reward.md
  - knowledge/performance-reward/performance-management.md
  - knowledge/performance-reward/governance-and-controls.md
blocks:
  - variable reward benchmark scenarios
  - pre-EOY salary and bonus planning workflow
last_reviewed: 2026-07-31
---

# Variable reward analysis

## Purpose

Provide a repeatable method for analysing variable-reward populations, pools, recommendations, differentiation, fairness, approvals, and payment reconciliation without duplicating the authoritative domain pack.

This draft is intentionally non-invokable until dependencies, examples, evaluations, and activation metadata are approved.

## Invoke when

Use this skill when the user needs to:

- design or assess a bonus, incentive, GVRP, or variable-pay dashboard;
- analyse target opportunity, pro-ration, organisational factors, individual multipliers, or awards;
- calibrate recommendations against a funded pool;
- assess differentiation by rating or performance cohort;
- investigate portfolio, salary, demographic, plan, or manager patterns;
- reconcile recommended, approved, processed, and paid outcomes;
- define variable-reward semantic-model requirements;
- design pre-cycle, in-cycle, outcome, or control reporting.

## Do not invoke when

Do not use this skill for:

- fixed-pay movement analysis unless variable reward is also materially in scope;
- defining performance ratings or calibration methodology itself;
- long-term incentive valuation or accounting;
- payroll tax or statutory advice;
- generic Power BI implementation questions with no variable-reward semantic content;
- making an award decision on behalf of an authorised human.

## Required inputs

Collect or explicitly mark as unknown:

- business decision and audience;
- cycle, plan, and population scope;
- eligible earnings definition;
- target opportunity;
- pro-ration logic;
- organisational, business, or plan factor;
- individual multiplier or adjustment logic;
- performance outcome inputs;
- risk, conduct, and exception rules;
- available pool and budget hierarchy;
- recommendation, approval, processing, and payment states;
- organisation, position, level, manager, geography, demographic, and currency attributes;
- effective dates and historical hierarchy requirements;
- privacy, security, and minimum-population rules.

## Progressive loading

Load only the knowledge required for the question.

Always load:

1. `knowledge/performance-reward/holistic-value-driver-tree.md`
2. `knowledge/performance-reward/variable-reward.md`

Load conditionally:

- performance management for rating or performance-outcome interpretation;
- fixed reward for total-remuneration or salary-concentration questions;
- governance and controls for conduct, risk, approvals, exceptions, and reconciliation;
- pay equity for protected-group or comparable-work analysis;
- talent and retention for critical-person or retention-risk decisions;
- job architecture for work-level or role-comparability analysis;
- market competitiveness for total-remuneration positioning.

## Method

### 1. Frame the decision

State:

- who is deciding;
- what decision must be made;
- the cycle stage;
- the value at stake;
- the required level of detail;
- whether the output is exploratory, operational, approval-ready, or executive.

### 2. Lock lifecycle state

Identify whether each measure is:

- scenario;
- target;
- recommended;
- approved;
- processed;
- paid;
- corrected.

Never compare or aggregate lifecycle states without an explicit reason.

### 3. Define population and eligibility

Document inclusion and exclusion rules, plan assignment, eligible earnings, pro-ration, service dates, leave, transfers, joiners, leavers, and special cases. Quantify missing or invalid eligibility before interpreting outcomes.

### 4. Reconstruct the calculation chain

Show the applicable sequence from eligible earnings through target opportunity, pro-ration, organisational factor, individual multiplier, adjustments, and final award. Distinguish policy formula from discretionary decision.

### 5. Establish pool control

Calculate available pool, current spend, residual or excess, utilisation, and the hierarchy through which budgets are allocated. Separate funding arithmetic from distribution quality.

### 6. Assess differentiation

Analyse employee counts, award-to-target, multipliers, and spend by performance cohort. Use both employee-average and spend-weighted views. Test overlap, distance, outliers, and portfolio variation.

### 7. Test concentration and fairness

Assess salary quartiles, management level, plan, geography, portfolio, manager, demographic group, leave status, and comparable-work populations. Control for legitimate factors before escalating a signal.

### 8. Review governance and exceptions

Identify conduct or risk gates, overrides, caps, approval authority, unsupported exceptions, missing evidence, and segregation-of-duties concerns.

### 9. Reconcile lifecycle transitions

Where outcome or operational analysis is required, reconcile recommendation to approval, instruction, payment, and correction. Surface unmatched, duplicated, stale, or unauthorised records.

### 10. Produce decision-ready output

Return the smallest output that supports the decision. Separate evidence, interpretation, hypothesis, recommendation, and decision required.

## Audience routes

### Executive route

Prioritise total pool, affordability, differentiation, material portfolio variance, fairness and risk signals, strategic workforce implications, and decisions required. Avoid operational detail unless it changes the decision.

### Reward Partner route

Prioritise pool control, rating and multiplier distributions, salary concentration, outliers, exceptions, scenario impacts, and challenge points.

### People Leader route

Prioritise available guidance, employee recommendations, exceptions, submission completeness, and impact of adjustments. Restrict access to the authorised population.

### HRBP or Performance Partner route

Prioritise translation of performance outcomes into reward, team and manager patterns, talent implications, and unsupported overrides.

### Governance, Payroll, and HRIS route

Prioritise eligibility validity, approval authority, conduct and risk gates, lifecycle reconciliation, duplicate or missing records, and audit evidence.

## Microsoft Power BI delegation

Delegate generic implementation work when maintained Microsoft skills provide it, including:

- semantic-model mechanics after the business grain is fixed;
- DAX syntax and optimisation;
- report interaction implementation;
- theme construction;
- performance tuning;
- standard security implementation patterns.

Before delegation, provide the domain contract:

- lifecycle states;
- required grains;
- effective-dating rules;
- population rules;
- calculation definitions;
- scenario and version requirements;
- security roles;
- suppression and privacy constraints;
- reconciliation expectations.

Reject an implementation that violates this contract even if technically valid.

## Output contract

Return, as applicable:

1. decision statement;
2. scope and lifecycle state;
3. population and eligibility definition;
4. calculation chain;
5. pool and budget controls;
6. KPI set with numerator, denominator, grain, time basis, and exclusions;
7. differentiation and fairness tests;
8. governance and reconciliation controls;
9. recommended information architecture;
10. semantic-model implications;
11. assumptions and unresolved policy inputs;
12. decisions required.

## Quality checks

Before completion verify that:

- target, recommended, approved, and paid values are distinct;
- employee-average and spend-weighted analysis are not conflated;
- salary and target-opportunity effects are controlled;
- plan differences are not hidden;
- historical organisation attributes use the correct effective date;
- pool balancing is not treated as the sole objective;
- descriptive differences are not presented as causal findings;
- exceptions and overrides remain traceable;
- employee-level data is restricted appropriately;
- the output does not make the human award decision.

## Failure conditions

Stop or qualify the analysis when:

- eligible population cannot be reconstructed;
- target opportunity or eligible earnings is materially incomplete;
- lifecycle states are mixed or unknown;
- the pool basis is not reconcilable;
- performance outcomes use incompatible scales without mapping;
- current hierarchy has overwritten cycle-time accountability;
- privacy or authority rules do not permit the requested detail;
- organisation-specific policy is being assumed rather than supplied.

## Activation gate

Do not change `activation: DISABLED` until:

- the variable-reward, performance-management, and governance dependencies are reviewed;
- the skill-authoring standard is satisfied;
- at least two benchmark scenarios pass, including one calibration scenario and one lifecycle-reconciliation scenario;
- routing tests distinguish variable reward from fixed reward, performance management, and generic Power BI requests;
- Microsoft delegation and fallback behaviour is verified.