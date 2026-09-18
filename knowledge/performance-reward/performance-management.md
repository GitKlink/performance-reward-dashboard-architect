---
status: DRAFT
phase: 2
priority: critical
depends_on:
  - knowledge/performance-reward/holistic-value-driver-tree.md
  - knowledge/performance-reward/governance-and-controls.md
blocks:
  - knowledge/performance-reward/variable-reward.md
  - .cursor/skills/performance-reward/performance-management-analysis/SKILL.md
  - performance outcome reporting workflow
last_reviewed: 2026-07-31
---

# Performance management

## Purpose

This pack defines the semantics needed to analyse performance-management processes and outcomes and to connect them safely to reward decisions. It covers goal setting, check-ins, assessment, calibration, final outcomes, completion, quality, fairness, and governance.

Performance management provides evidence and decisions used by reward, talent, development, and workforce planning. It must not be reduced to a rating-distribution report.

## Domain boundary

Performance management includes:

- population eligibility;
- goal and expectation setting;
- ongoing feedback and check-ins;
- self and manager assessment;
- calibration;
- final performance outcomes;
- process completion and timeliness;
- overrides and exceptions;
- quality, fairness, and governance controls;
- links to reward, development, promotion, talent, conduct, and risk decisions.

It does not define remuneration formulas, job evaluation, disciplinary procedures, or talent succession methodology, although it may provide inputs to those domains.

## Canonical lifecycle

1. establish eligible population and performance period;
2. set goals, expectations, and measures;
3. record ongoing feedback and check-ins;
4. collect self and manager assessments;
5. review evidence and proposed outcomes;
6. calibrate across relevant peer groups;
7. approve final outcomes;
8. communicate outcomes;
9. apply authorised downstream uses;
10. monitor appeals, corrections, and post-cycle quality.

A report must distinguish proposed, calibrated, final, communicated, and corrected outcomes.

## Core value drivers

### Strategic alignment

- goals linked to business and role expectations;
- appropriate balance of outcomes, behaviours, risk, and conduct;
- measurable and controllable expectations;
- alignment across organisational levels.

### Process participation

- goal-setting completion;
- check-in completion and cadence;
- self-assessment completion;
- manager assessment completion;
- calibration completion;
- finalisation and communication timeliness.

Completion is an operational signal, not proof of assessment quality.

### Assessment quality

- evidence sufficiency;
- differentiation where warranted;
- consistency of standards;
- appropriate use of rating or outcome scales;
- absence of unsupported overrides;
- clear relationship between goals, behaviours, evidence, and final outcome.

### Fairness and consistency

- comparable treatment across teams and populations;
- demographic and leave-status signals;
- manager severity or leniency;
- calibration changes and override patterns;
- treatment of joiners, movers, part-year workers, and employees with changed roles.

### Governance and trust

- valid approval authority;
- traceable changes;
- documented exceptions;
- privacy and access controls;
- separation of evidence, judgement, recommendation, and decision;
- appropriate use of outcomes in reward and talent processes.

## Required grains

A robust model normally separates:

- employee-performance-cycle eligibility grain;
- employee-goal grain;
- employee-check-in event grain;
- employee-assessment-stage grain;
- employee-proposed-outcome grain;
- employee-calibrated-outcome grain;
- employee-final-outcome grain;
- calibration-session or calibration-group grain;
- outcome-change event grain;
- approval and communication event grain;
- exception or appeal grain.

Do not overwrite proposed outcomes with final outcomes when calibration analysis or auditability matters.

## Canonical measures

### Eligible population

Distinct employees meeting the cycle's inclusion rules at the applicable eligibility date or period.

### Completion rate

`Completion rate = Completed eligible records ÷ Eligible records`

The completion event and denominator must be defined for each stage. Goal-setting, check-in, assessment, calibration, and finalisation completion are separate measures.

### On-time completion rate

`On-time completion rate = Records completed by deadline ÷ Eligible records`

Late completion should not be silently counted as on time.

### Outcome distribution

Employee count and percentage by final outcome, with the scale, population, exclusions, and cycle stated.

### Proposed-to-final change rate

`Change rate = Employees whose final outcome differs from proposed outcome ÷ Employees with both outcomes`

Direction and magnitude of change should also be analysed.

### Manager outcome profile

Distribution and central tendency of outcomes assigned by a manager, controlled for population size and workforce mix.

### Calibration movement

Count and percentage moved upward, downward, or unchanged during calibration, by calibration group, manager, portfolio, level, and other authorised dimensions.

### Check-in cadence

Count of valid check-ins per eligible employee over the defined period. Administrative events and duplicate records must be excluded.

## Diagnostic patterns

### Distribution analysis

Use distributions to identify concentration, absence of differentiation, or unusual portfolio patterns. Do not assume a target distribution unless policy explicitly defines one. Small populations and different role mixes require caution.

### Manager severity and leniency

Compare manager outcome profiles with appropriate peers after controlling for level, role mix, geography, performance evidence, and population size. Treat results as investigation signals, not proof of bias or poor judgement.

### Calibration impact

Analyse who changed, in which direction, by how much, and under which calibration group. Separate legitimate standardisation from unsupported compression, quota behaviour, or seniority effects.

### Process-quality analysis

Combine completion, timeliness, evidence availability, check-in cadence, change patterns, overrides, and appeals. Completion alone is insufficient.

### Fairness review

Assess demographic, leave, part-year, and comparable-work outcomes while controlling for legitimate factors and minimum population thresholds. Avoid causal claims from descriptive differences.

### Reward linkage

When performance outcomes feed variable or fixed reward, test the relationship without assuming a deterministic mapping. Preserve the distinction between performance evidence, final outcome, reward recommendation, and reward approval.

## Audience-specific questions

### Executives

- Is the process complete and decision-ready?
- Are outcomes differentiated and credible?
- Where are material fairness, consistency, or governance risks?
- Are performance outcomes supporting strategic and workforce decisions?

### Performance and Reward Partners

- Which portfolios require calibration challenge?
- Where are unusual distributions, manager patterns, or override rates?
- Are proposed-to-final movements defensible?
- How are outcomes translating into reward decisions?

### HR Business Partners

- Which teams show process, quality, or fairness concerns?
- Where do leaders need intervention or support?
- Are talent, conduct, retention, or organisational changes relevant to interpretation?

### People Leaders

- Which actions remain incomplete?
- Where is evidence insufficient?
- Which proposed outcomes require review?
- What changed during calibration and why?

### Governance and HRIS

- Are eligibility, status transitions, approvals, and access correct?
- Are changes traceable?
- Are exceptions, appeals, and corrections controlled?
- Do downstream systems receive only approved outcomes?

## Product patterns

### Cycle readiness view

Population, eligibility, stage completion, overdue actions, data-quality failures, and operational risks.

### Calibration workspace

Proposed distributions, evidence indicators, manager profiles, peer comparisons, movement scenarios, and documented decisions. Preserve pre- and post-calibration states.

### Executive outcome summary

Final distribution, strategic differentiation, major portfolio variation, fairness and governance signals, downstream reward implications, and decisions required.

### Manager action view

Employee-level authorised actions, evidence completeness, proposed outcomes, exception indicators, deadlines, and submission status.

### Post-cycle quality review

Timeliness, calibration movement, overrides, appeals, corrections, downstream reconciliation, and lessons for the next cycle.

## Power BI implementation implications

The model should support:

- stage-specific facts rather than one mutable current record;
- effective-dated employee, position, organisation, manager, and role attributes;
- proposed, calibrated, final, communicated, and corrected outcome states;
- calibration groups and sessions;
- process events and deadlines;
- restricted employee evidence and comments;
- minimum-population suppression;
- historical manager accountability;
- authorised linkage to reward outcomes without collapsing the two domains.

Generic Power BI mechanics may be delegated, but implementations must preserve lifecycle state, historical organisation context, and privacy controls.

## Anti-patterns

- treating a rating distribution as the complete performance story;
- imposing a normal distribution without policy authority;
- using current hierarchy for historical manager accountability;
- overwriting proposed outcomes after calibration;
- presenting completion as quality;
- interpreting small manager populations without safeguards;
- claiming bias or causality from descriptive differences alone;
- exposing goals, evidence, comments, or outcomes beyond authorised roles;
- assuming performance ratings mechanically determine reward outcomes;
- mixing employees from incompatible cycles, scales, or plans.

## Organisation-specific inputs

A production implementation must supply:

- cycle and eligibility rules;
- outcome scale and definitions;
- goal and behaviour framework;
- required stages and deadlines;
- calibration groups and authority;
- treatment of joiners, movers, leave, and exceptions;
- conduct and risk interactions;
- downstream reward and talent uses;
- privacy, access, suppression, and retention rules;
- appeal and correction procedures.

## Current maturity and research gaps

This draft establishes the domain structure and analytical controls. It still requires formal source registration, policy validation, jurisdiction review, benchmark scenarios, and reconciliation with governance, variable reward, talent, and pay-equity packs.