---
artifact_id: EX-VIZ-001
status: DRAFT
phase: 0
priority: high
depends_on:
  - artifact_id: STD-CORE-001
    path: ../../../docs/standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../../../docs/standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../../../docs/standards/citation-standard.md
  - artifact_id: KNOW-CORE-001
    path: ../README.md
  - artifact_id: KNOW-CORE-002
    path: ../sources.yaml
blocks:
  - Phase 0 stable-research review
  - future visual-perception knowledge pack
  - future chart-selection skill
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2027-07-17
---

# Trial: Stable graphical-perception research

## Purpose

Test the repository's handling of an established research paper whose findings are influential but often simplified into rigid chart-selection folklore.

## Research question

What can the repository safely derive from Cleveland and McGill's 1984 graphical-perception research, and how should the future chart-selection capability avoid overstating it?

## Decision supported

Determine how perceptual accuracy should influence visual selection for Performance & Reward dashboards without turning one experimental ordering into an absolute hierarchy for every task, audience, or user.

## Primary research

Cleveland and McGill define graphical perception as the visual decoding of quantitative and qualitative information encoded in graphs. Their paper seeks a scientific foundation for graphical methods by identifying elementary perceptual tasks and testing how accurately people perform them.[^cleveland-mcgill]

The research supports the broad principle that graphical encodings do not provide equal accuracy for every quantitative-comparison task.[^cleveland-mcgill]

The contribution is not merely a list of approved and prohibited chart types. It is a theory-and-experiment approach to evaluating how viewers decode graphical marks.

## Repository interpretation

### Supported principles

1. Chart choice follows the business and comparison task.
2. Precise quantitative comparison should favour encodings that support accurate judgement.
3. Position and length are generally stronger starting points than area, volume, or angle where precision matters.
4. Every chart recommendation should state the perceptual task it requires.
5. Precision requirements affect the acceptable encoding.
6. Scale, sorting, labels, density, interaction, and accessibility can strengthen or undermine the chosen encoding.

The preference for position and length is a research-informed repository synthesis. It is not presented as a universal law.

### Unsupported simplifications

Do not claim:

- bar charts are always superior to every alternative;
- pie charts are invalid in every context;
- a population-average ordering predicts every individual's performance;
- perceptual accuracy is the only chart-selection criterion;
- the 1984 study directly establishes Power BI usability or executive reading behaviour;
- a highly ranked encoding automatically communicates the correct business message.

## Performance & Reward applications

### Precise category comparison

Use sorted bars or dots when comparing:

- fixed-reward increase by rating;
- pay position across job families;
- budget variance by division;
- attrition rates across critical populations.

The primary task is position or length comparison.

### Distribution comparison

Use histograms, strip plots, box plots, or small multiples when the question concerns overlap, spread, skew, or outliers. Do not force a distribution question into a simple category-ranking chart.

### Part-to-whole communication

A composition visual may support rough orientation. Precise comparison across many components should generally use aligned bars or a table.

### Executive emphasis

A perceptually accurate encoding can still fail if the executive cannot identify the decision, comparator, material exception, or action. Perceptual accuracy is one design input, not a substitute for audience and decision framing.

## Claims matrix

| Claim ID | Claim | Source IDs | Confidence | Treatment |
|---|---|---|---|---|
| VIZ-001 | Graphical perception concerns visual decoding of information encoded in graphs | `cleveland-mcgill-graphical-perception-1984` | Established | Publish |
| VIZ-002 | The paper identifies elementary perceptual tasks and tests their accuracy | `cleveland-mcgill-graphical-perception-1984` | Established | Publish |
| VIZ-003 | Different encodings can support different levels of quantitative accuracy | `cleveland-mcgill-graphical-perception-1984` | Established | Publish |
| VIZ-004 | Position and length are preferred starting points for precise dashboard comparison | Research-informed project synthesis | Supported synthesis | Publish with scope |
| VIZ-005 | The experimental ordering is universal for every person and task | None sufficient | Unsupported | Reject |
| VIZ-006 | Perceptual rank alone determines the correct chart | None | Unsupported | Reject |

## Selection-rule prototype

The future chart-selection skill should ask:

1. What business question and decision does the visual support?
2. What relationship must be perceived: comparison, trend, distribution, composition, correlation, flow, or variance?
3. How precise must the judgement be?
4. Which perceptual task does each candidate visual require?
5. What audience, accessibility, density, and interaction constraints apply?
6. Can the visual be implemented and exported reliably in Power BI?

This sequence prevents perceptual research from being isolated from business and implementation context.

## Acceptance result

**Trial result: PASS**

The standards preserve the value of the research while preventing a simplistic universal chart ranking. The result can inform Phase 7 and Phase 8 research after independent review.

## Source

[^cleveland-mcgill]: William S. Cleveland and Robert McGill, “Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods,” *Journal of the American Statistical Association* 79, no. 387 (1984): 531–554, https://doi.org/10.1080/01621459.1984.10478080. Central source ID: `cleveland-mcgill-graphical-perception-1984`.
