---
status: DRAFT
phase: 2
priority: critical
depends_on:
  - knowledge/performance-reward/holistic-value-driver-tree.md
  - knowledge/performance-reward/performance-management.md
  - knowledge/performance-reward/governance-and-controls.md
blocks:
  - .cursor/skills/performance-reward/variable-reward-analysis/SKILL.md
  - pre-EOY salary and bonus planning workflow
  - variable reward calibration workflow
last_reviewed: 2026-07-31
---

# Variable reward

## Purpose

This pack defines the business and analytical semantics required to design variable-reward decisions, models, dashboards, and controls. It is the local authority for variable-reward concepts. Generic Power BI implementation mechanics may be delegated to maintained Microsoft skills, but business definitions, calculation logic, decision boundaries, grain, controls, and governance remain repository-owned.

## Domain boundary

Variable reward covers contingent remuneration linked to organisational, business, team, individual, plan, risk, conduct, or other approved outcomes. It includes target opportunity, eligibility, pro-ration, funding, performance factors, individual outcomes, recommendations, approvals, payment, deferral where relevant, and post-cycle reconciliation.

It does not define fixed-pay movement, long-term incentive accounting, benefits valuation, payroll tax treatment, or performance-rating methodology except where those domains provide an input to a variable-reward decision.

## Canonical decision chain

1. Determine the eligible population and applicable plan.
2. establish target opportunity and eligible earnings;
3. calculate pro-ration and other approved eligibility adjustments;
4. establish the funded pool using the approved organisational or plan factor;
5. translate performance, risk, conduct, and policy outcomes into an individual recommendation;
6. calibrate differentiation, affordability, fairness, and control outcomes;
7. approve the award;
8. process payment, deferral, holdback, or forfeiture;
9. reconcile approved, processed, and paid outcomes.

A dashboard must state which decision stage it represents. Planned, recommended, approved, processed, and paid awards are not interchangeable.

## Core value drivers

### Eligibility integrity

- correct plan assignment;
- valid employment and service dates;
- correct eligible earnings base;
- accurate pro-ration;
- approved treatment of leave, transfers, termination, commencement, suspension, and special circumstances.

### Funding and affordability

- target pool;
- approved organisational or plan performance factor;
- available pool;
- recommended spend;
- approved spend;
- unallocated or over-allocated amount;
- recurring versus non-recurring cost distinction where applicable.

### Performance differentiation

- relationship between performance outcomes and award outcomes;
- proportional separation between performance groups;
- distribution of individual multipliers;
- concentration of spend among high-paid employees;
- outliers and unexplained overrides;
- consistency across comparable portfolios and populations.

### Risk, conduct, and governance

- conduct or risk gates;
- malus, holdback, forfeiture, or deferral indicators where applicable;
- approval authority;
- exception reason and evidence;
- segregation of duties;
- audit trail from recommendation to payment.

### Fairness and workforce outcomes

- demographic outcome differences;
- comparable-work outcome differences;
- treatment of leave and part-year service;
- manager or portfolio patterns;
- interaction between rating, salary, target opportunity, and final award;
- retention and critical-skill implications.

## Canonical calculations

The following formulas are conceptual defaults. Organisation-specific policy must be injected explicitly.

### Target award

`Target award = Eligible earnings × Target opportunity % × Pro-ration factor`

### Funded target award

`Funded target award = Target award × Approved organisational or plan factor`

### Recommended award

`Recommended award = Funded target award × Individual performance multiplier × Approved adjustment factors`

Where the organisation uses the confirmed GVRP-style formulation, the conceptual relationship is:

`Award = Fixed or eligible earnings × target % × GPI × IPM`

The exact earnings basis, factor ranges, caps, rounding, and eligibility treatment are policy inputs rather than universal rules.

### Award as percentage of target

`Award to target % = Recommended or approved award ÷ Target award`

### Average individual multiplier

`Average multiplier = Sum of applicable individual multipliers ÷ Eligible employee count`

A weighted average may be required when the analytical question concerns spend rather than employee treatment.

### Pool utilisation

`Pool utilisation % = Recommended or approved spend ÷ Available pool`

### Variance to pool

`Pool variance = Available pool − Recommended or approved spend`

### Spend share

`Spend share = Population award spend ÷ Total award spend`

### Population share

`Population share = Population headcount ÷ Total eligible headcount`

Comparing spend share with population share can reveal concentration, but interpretation must control for target opportunity, salary, pro-ration, plan, and performance mix.

## Required grains

A robust model normally separates:

- employee-plan-cycle eligibility grain;
- employee-plan-cycle target opportunity grain;
- employee-plan-cycle recommendation grain;
- employee-plan-cycle approval grain;
- employee payment-event grain;
- portfolio-plan-cycle pool grain;
- rating or performance-outcome grain;
- conduct, risk, and exception-event grain;
- approval-action grain.

Do not collapse these into one mutable employee row when lifecycle reconciliation, auditability, or historical analysis matters.

## Time and population rules

Every measure must identify:

- cycle or performance year;
- eligibility measurement period;
- effective date of employee, organisation, position, and plan attributes;
- population inclusion and exclusion rules;
- treatment of movers, joiners, leavers, leave, secondments, and international assignments;
- currency and conversion date;
- whether the measure represents recommendation, approval, processing, or payment.

Current organisation attributes must not silently replace cycle-time attributes.

## Diagnostic patterns

### Differentiation analysis

Assess award outcomes by performance rating or approved performance cohort. Test employee-count distribution, award-to-target distribution, spend-weighted outcomes, salary quartiles, management level, portfolio, and plan. A strong relationship is not automatically fair; a weak relationship is not automatically wrong where policy permits discretion or other factors apply.

### High-salary multiplier concentration

Identify whether high-salary employees receive systematically higher multipliers or disproportionate spend. Control for target opportunity, plan, performance, level, pro-ration, and approved exceptions. Employee-average and spend-weighted views should both be shown.

### Pool calibration

Compare available pool, current recommendation, residual pool, required movement to budget, and distributional consequences. Separate arithmetic balancing from the business decision about where adjustments should occur.

### Rating-to-award consistency

Compare relative distance between rating groups, overlap of award distributions, exceptions, and portfolio variation. Avoid assuming one universal multiplier per rating unless policy explicitly requires it.

### Fairness review

Compare similarly situated employees after controlling for plan, target opportunity, performance, salary, service, work level, geography, and other legitimate factors. Descriptive differences should be labelled as signals requiring investigation, not proof of discrimination.

### Lifecycle reconciliation

Reconcile recommendation, approved award, payroll instruction, payment, and later correction. Highlight missing transitions, mismatched amounts, duplicate events, and unauthorised changes.

## Audience-specific questions

### Executives

- Is the total pool affordable and within approved funding?
- Is differentiation consistent with enterprise performance and reward philosophy?
- Where are material portfolio, risk, fairness, or retention concerns?
- What decisions or trade-offs remain?

### Reward Partners

- Which populations are under- or over-allocated?
- Are rating and multiplier patterns defensible?
- Which outliers require challenge or documented exception?
- What changes would rebalance the pool without distorting intended differentiation?

### People Leaders

- What is the available budget or guidance for my population?
- Which recommendations are outside expected ranges?
- What evidence supports an exception?
- What actions remain before submission?

### HR Business Partners and Performance Partners

- Are performance outcomes translating consistently into reward outcomes?
- Which teams show unusual differentiation or override patterns?
- Are organisational or talent risks influencing recommendations appropriately?

### Governance, Risk, Payroll, and HRIS

- Have conduct and risk gates been applied correctly?
- Are approvals complete and within authority?
- Do approved values reconcile to processing and payment?
- Are changes traceable and supported?

## Product patterns

### Pre-EOY planning

Focus on target population, target opportunity, pro-ration, scenario pool, assumed organisational factor, performance distributions, and projected spend. Do not present unapproved projections as outcomes.

### Calibration workspace

Focus on current multiplier and spend distributions, rating relationships, pool variance, salary concentration, exceptions, and adjustment impact. Preserve before-and-after states.

### Executive outcome summary

Focus on approved spend, funding utilisation, differentiation, material portfolio variation, fairness signals, governance exceptions, and comparison with prior cycles or approved intent.

### Operational control view

Focus on missing eligibility, invalid plan assignments, approval status, payment reconciliation, duplicate or conflicting records, and unresolved exceptions.

## Power BI implementation implications

The semantic model should support:

- separate eligibility, target, recommendation, approval, pool, and payment facts;
- effective-dated employee, position, organisation, plan, and target-opportunity dimensions;
- scenario or version dimensions for planning and calibration;
- explicit currency and conversion logic;
- employee-average and spend-weighted measures;
- row-level security for leader, HR, Reward, governance, and payroll roles;
- suppression and aggregation controls for sensitive populations;
- traceability from executive aggregate to governed employee-level evidence where authorised.

Generic DAX optimisation, visual construction, performance tuning, and interaction implementation should be delegated when Microsoft skills cover them, but the implementation must preserve these semantics.

## Anti-patterns

- presenting award spend without the eligible population or target basis;
- using final payment data to represent managerial decision quality without preserving recommendations and approvals;
- comparing raw multipliers across different plans or target opportunities;
- treating correlation between rating and award as proof of appropriate differentiation;
- hiding salary concentration by showing only employee-average multipliers;
- using current hierarchy for historical cycle accountability;
- mixing forecast, recommended, approved, and paid values in one measure;
- balancing a pool through unexplained across-the-board adjustments;
- exposing employee-level remuneration data beyond authorised roles.

## Organisation-specific policy inputs

A production implementation must supply:

- eligible earnings definition;
- target opportunity rules;
- pro-ration rules;
- organisational or plan factor methodology;
- individual multiplier ranges and caps;
- performance-rating treatment;
- risk and conduct gates;
- discretion and override policy;
- deferral, holdback, malus, and forfeiture rules where relevant;
- approval authorities;
- currency, rounding, and payroll rules;
- privacy and minimum-population thresholds.

## Current maturity and research gaps

This is a domain draft based on established reward practice and confirmed project context. It still requires formal source registration, jurisdiction review, organisation-policy validation, and benchmark testing. The pack must not imply that the conceptual formulas or diagnostic thresholds are universal policy.