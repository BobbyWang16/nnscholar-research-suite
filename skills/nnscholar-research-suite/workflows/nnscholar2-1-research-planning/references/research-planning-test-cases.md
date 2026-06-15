# Research Planning Test Cases

Use these examples to check whether `nnscholar2-1-research-planning` behaves correctly.

## Case 1: Empty Button Click

User:

```text
Use $nnscholar2-1-research-planning.
```

Expected behavior:

- Do not invent a plan.
- Ask only the minimum questions: topic/question, target output, time window, and available materials.

## Case 2: Topic Only

User:

```text
I want to study radiation pneumonitis. Help me make a research plan.
```

Expected behavior:

- Classify as S0 topic only.
- Ask for target output and available data/materials.
- Offer only a provisional exploratory plan unless the user provides more context.

## Case 3: Literature Output Exists

User:

```text
Based on `literature-search-2026-06-10-ccta-diabetes-risk.md`, build an 8-week plan for a clinical research paper.
```

Expected behavior:

- Use the provided 1.2 literature file as primary evidence.
- Classify likely S1 or S2 depending on whether a hypothesis exists.
- Produce work packages, timeline, risks, and next 3 actions.
- Flag missing cohort/data availability if not provided.

## Case 4: Hypothesis Locked

User:

```text
I already have a hypothesis: patients with pulmonary sarcomatoid carcinoma and high PD-L1 expression may benefit from immunotherapy plus chemotherapy. Give me a 12-week research plan.
```

Expected behavior:

- Classify as S2 hypothesis locked.
- Ask whether data/cohort is available if missing, or mark the plan provisional.
- Include design, endpoint, cohort/data, analysis, figures, and writing work packages.
- Include feasibility, confounding, sample size, and ethics/IRB risks.

## Case 5: AI / Computational Project

User:

```text
We want to benchmark LLM agents on biomedical literature review tasks. Build a 6-week executable research plan.
```

Expected behavior:

- Output in English.
- Include dataset/task construction, baseline selection, metrics, annotation/evaluation, error analysis, and writing.
- Include risks around benchmark leakage, evaluator bias, reproducibility, and compute constraints.

## Case 6: Education / Psychology Project

User:

```text
Design a 10-week plan to test whether LLM tutoring feedback improves undergraduate metacognitive calibration and exam performance.
```

Expected behavior:

- Include theory/construct mapping, validated scales, intervention design, recruitment, consent, outcome measures, analysis, and writing.
- Flag risks around measurement validity, instructor/classroom confounding, attrition, privacy, and student consent.

## Case 7: Materials / Chemistry Project

User:

```text
Build a 12-week plan for a paper on MOF-derived carbon catalysts for electrochemical nitrate reduction.
```

Expected behavior:

- Include synthesis, characterization, comparator selection, electrochemical performance testing, mechanism analysis, reproducibility, safety, and manuscript figures.
- Flag risks around batch variance, unsupported mechanism claims, electrolyte/control mismatch, and durability.

## Case 8: Unrealistic Deadline

User:

```text
I have a brand-new clinical prediction model idea and want to submit to a top journal in two weeks. Arrange the research plan.
```

Expected behavior:

- Do not accept the deadline blindly.
- Mark timeline overreach as high risk.
- Offer a fallback plan: two-week feasibility package, protocol, preprint outline, or reduced scope.

## Case 9: Active Project Recovery

User:

```text
We have collected data, but the variable dictionary is messy, the statistical plan is not locked, and only the Introduction is drafted. Build the next 4-week plan.
```

Expected behavior:

- Classify as S5 active project.
- Create a recovery/backlog plan.
- Prioritize variable dictionary, data cleaning, endpoint lock, statistical analysis plan, and results table shells before writing.

## Case 10: Expected Minimal Planning Card

After intake, the skill should be able to show:

```text
Planning card:
Target output: clinical research paper
Research object: pulmonary sarcomatoid carcinoma cohort
Current maturity: S2 hypothesis locked, S3 materials unclear
Main constraint: cohort availability and confounding control
Next decision: confirm available dataset and primary endpoint
```
