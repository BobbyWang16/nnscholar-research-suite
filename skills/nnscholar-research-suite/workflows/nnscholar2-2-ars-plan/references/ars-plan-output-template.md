# ARS Plan Output Template

This template defines structure, not output language. Translate headings and field labels to the user's language. Keep technical terms, datasets, model names, variable names, file paths, trial IDs, and citation keys in their original form when appropriate.

Delete empty placeholder rows in the final output. Mark missing information as `missing`, `uncertain`, or `provisional`.

```markdown
# [TOPIC] ARS Research Scheme

## 1. Scheme Status

- Protocol status: provisional / ready for confirmation / locked
- Run mode: linked / partial / scratch
- Target output:
- Discipline / scheme family:
- Active user intent:
- Upstream evidence used:
- Generated date:

## 2. Upstream Evidence Map

| Source | Status | Key extracted content | How it shapes the scheme | Limitations |
|---|---|---|---|---|
| 1.1 Question mining |  |  |  |  |
| 1.2 Literature searching |  |  |  |  |
| 1.3 Hypothesis generation |  |  |  |  |
| 1.4 Domain knowledge base |  |  |  |  |
| 2.1 Research planning |  |  |  |  |
| Current user input |  |  |  |  |

## 3. ARS Card

- Aim:
- Route:
- Specification:
- Main blocker:
- Next decision:

## 4. Aim

- Primary research question:
- Hypothesis / claim:
- Secondary questions:
- Success criteria:
- Falsification criteria:

## 5. Route

- Study / project design:
- Population, sample, material, corpus, or dataset:
- Comparison, control, baseline, or grouping:
- Technical route:

```text
[route step 1] -> [route step 2] -> [route step 3]
```

## 6. Specification

### Objects and Eligibility

- Inclusion criteria:
- Exclusion criteria:
- Unit of analysis:
- Time window:

### Variables / Constructs / Measurements

| Role | Name | Definition | Measurement/source | Status |
|---|---|---|---|---|
| Exposure/intervention/group |  |  |  |  |
| Primary outcome/metric |  |  |  |  |
| Secondary outcome/metric |  |  |  |  |
| Covariate/control |  |  |  |  |

### Method / Analysis Plan

- Primary method:
- Secondary method:
- Sensitivity / robustness checks:
- Missing data / failed experiment handling:
- Software, tool, or model requirements:

## 7. Bias, Risk, and Mitigation

| Risk | Source | Impact | Mitigation | Fallback |
|---|---|---|---|---|
|  |  |  |  |  |

## 8. Quality Gates

| Gate | Status | Reason | Required action |
|---|---|---|---|
| Aim gate | pass / provisional / fail |  |  |
| Evidence gate | pass / provisional / fail |  |  |
| Data/material gate | pass / provisional / fail |  |  |
| Method gate | pass / provisional / fail |  |  |
| Measurement gate | pass / provisional / fail |  |  |
| Analysis gate | pass / provisional / fail |  |  |
| Bias gate | pass / provisional / fail |  |  |
| Ethics gate | pass / provisional / fail |  |  |
| Lock gate | pass / provisional / fail |  |  |

## 9. Protocol Lock Card

- Lock decision: locked / not locked
- Lock blockers:
- Items that downstream skills must not change:
- Items allowed to evolve:
- User confirmation needed:

## 10. Next 3 Actions

1. 
2. 
3. 

## 11. Handoff

- To `nnscholar2-3-paper-architecture` when manuscript structure is next.
- To `nnscholar2-4-flowchart-design` when visual route design is next.
- Back to `nnscholar1-2-literature-searching` when evidence is too weak.
- Back to `nnscholar1-3-hypothesis-generation` when the hypothesis is not testable.
```
