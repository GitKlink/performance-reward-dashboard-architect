---
artifact_id: EX-CONSULT-001
status: DRAFT
phase: 0
priority: high
depends_on:
  - STD-CORE-001: ../../../docs/standards/naming-standard.md
  - STD-CORE-002: ../../../docs/standards/research-standard.md
  - STD-CORE-003: ../../../docs/standards/citation-standard.md
  - KNOW-CORE-001: ../README.md
  - KNOW-CORE-002: ../sources.yaml
blocks:
  - Phase 0 consulting-attribution review
  - future consulting-technique catalogue
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-10-17
---

# Trial: Consulting-firm technique attribution

## Purpose

Test whether the repository can describe a technique published by a major consulting firm without overstating the firm's internal standards or converting a context-specific method into a universal dashboard rule.

## Research question

What can be attributed directly to McKinsey's public visual performance management publications, and how should the repository translate that material into a bounded dashboard-design recommendation?

## Decision supported

Determine whether the agent may recommend the `1-3-10` principle for executive or operational performance pages, and what caveats must accompany that recommendation.

## Published methodology

McKinsey's April 2022 visual performance management article presents three design principles: define a KPI cascade linked across organisational layers, use simple visualisation following a `1-3-10` principle, and conduct action-oriented performance meetings based on misses against target.[^mckinsey-vpm]

The article defines `1-3-10` as:

- one second to know whether performance is winning or losing;
- three seconds to identify what it is winning or losing at;
- ten seconds to determine the course of action.[^mckinsey-vpm]

A June 2022 follow-up explicitly frames visual performance management as storytelling that helps people take action, states that the performance story should be understandable at a glance, and describes the visual as a one-sentence pitch rather than a full script.[^mckinsey-pitch]

These are directly published claims and may be attributed to the cited articles.

## Attribution classification

| Statement | Classification | Treatment |
|---|---|---|
| McKinsey's public VPM article presents the `1-3-10` principle | Published methodology | Attribute directly |
| The cited VPM articles emphasise action and an at-a-glance performance story | Published methodology | Attribute directly |
| Every McKinsey executive dashboard follows `1-3-10` | Unsupported generalisation | Reject |
| `1-3-10` is a universal law of visual perception | Unsupported claim | Reject |
| `1-3-10` is useful for pages whose purpose is rapid status recognition and action | Project synthesis | Publish as selection guidance |
| A diagnostic Business Partner page must reveal every answer within ten seconds | Misapplication | Reject |

## Bounded repository interpretation

### Appropriate use

Use `1-3-10` as a **rapid-orientation test** when the page is intended to:

- communicate whether performance or risk is on track;
- surface the material driver of the result;
- direct the user toward an immediate action, escalation, or deeper page;
- support a recurring management cadence;
- serve executives, operational leaders, or managers who have limited reading time.

### Inappropriate use

Do not apply it as a rigid completion-time requirement when the page is intended to:

- support exploratory diagnosis;
- compare complex distributions or multiple cohorts;
- enable employee-level planning or calibration;
- document governance evidence;
- explain a multi-stage analytical argument;
- function as a static appendix rather than a decision page.

### Design test

For an appropriate page, ask:

1. Can the intended audience identify the current state without reading every object?
2. Can they identify the material driver or exception without opening a tooltip?
3. Can they identify the next action or navigation path?

The test must be adapted to the audience, content complexity, accessibility requirements, and consumption mode. It is not a stopwatch-based usability guarantee.

## Performance & Reward application

### Executive fixed-reward page

- **One-second orientation:** forecast investment is within or outside approved tolerance.
- **Three-second driver:** market remediation, mandatory increases, or discretionary allocation is causing the variance.
- **Ten-second action:** endorse, redirect, request a scenario, or escalate a control issue.

### Manager action page

- **One-second orientation:** how many cases require attention.
- **Three-second driver:** which type of exception or deadline dominates.
- **Ten-second action:** open the prioritised case list or complete the required decision.

### Business Partner diagnostic page

Use the principle only for the initial summary and navigation layer. Deeper diagnostic pages may require deliberate comparison and exploration.

## Claims matrix

| Claim ID | Claim | Source IDs | Confidence | Repository treatment |
|---|---|---|---|---|
| CAT-001 | McKinsey's VPM article publishes the `1-3-10` principle | `mckinsey-visual-performance-management-2022` | Established | Publish with attribution |
| CAT-002 | The follow-up article frames VPM as storytelling that supports action | `mckinsey-visual-performance-pitch-2022` | Established | Publish with attribution |
| CAT-003 | McKinsey universally applies `1-3-10` to all executive decks | None | Unsupported | Reject |
| CAT-004 | `1-3-10` should be used as a rapid-orientation test for suitable dashboard pages | Project synthesis informed by both sources | Supported synthesis | Publish as repository selection rule |
| CAT-005 | Failure to meet exact seconds proves a dashboard is poorly designed | None | Unsupported | Reject |

## What the trial revealed about the standards

### Research standard

- Firm attribution is reliable when the firm publishes the technique directly.
- The scope of the original publication must be retained: visual performance management is not identical to every dashboard or presentation.
- A useful published method still requires a repository-specific selection rule.

### Citation standard

- The citation must sit beside the attributed claim.
- The repository interpretation must be labelled separately from the firm's published position.
- A second official article can strengthen context without proving universality.

### Naming standard

- Use `one-three-ten-principle` in paths only where words are required for searchability.
- Use `1-3-10` in prose because it is the published label.
- Do not create a skill named after McKinsey; the capability belongs under a neutral consulting or executive-readability skill.

## Acceptance result

**Trial result: PASS**

The standards successfully distinguish direct firm attribution, unsupported generalisation, and project synthesis. The method is suitable for inclusion in the future technique catalogue with bounded invocation rules.

## Sources

[^mckinsey-vpm]: McKinsey & Company, “Getting visual performance management right,” 2022-04-01, retrieved 2026-07-17, https://www.mckinsey.com/capabilities/operations/our-insights/operations-blog/getting-visual-performance-management-right. Central source ID: `mckinsey-visual-performance-management-2022`.

[^mckinsey-pitch]: McKinsey & Company, “Getting visual performance management right — So, what's the pitch?,” 2022-06-06, retrieved 2026-07-17, https://www.mckinsey.com/capabilities/operations/our-insights/operations-blog/getting-visual-performance-management-right-so-whats-the-pitch. Central source ID: `mckinsey-visual-performance-pitch-2022`.
