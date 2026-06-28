# Diagram Patterns

Use this guide to choose a diagram pattern by research type.

## Clinical / Epidemiology

Recommended diagrams:

- cohort flow;
- study design timeline;
- analysis pipeline;
- bias/confounding DAG when requested.

Typical nodes:

```text
Source population -> eligibility -> final cohort -> grouping/exposure -> outcomes -> statistical analysis -> interpretation
```

Guardrails:

- Do not draw randomization unless the study is randomized.
- Use `classified by`, `grouped by`, or `stratified by` for observational groups.
- Show exclusions clearly.

## Basic / Translational / Wet-Lab

Recommended diagrams:

- experimental workflow;
- mechanism hypothesis map;
- validation chain;
- assay pipeline.

Typical nodes:

```text
Hypothesis -> model system -> perturbation -> phenotype assay -> mechanism assay -> rescue/validation -> interpretation
```

Guardrails:

- Label mechanisms as `hypothesized` unless proven.
- Separate experimental steps from interpretation.

## Computational / AI / Benchmark

Recommended diagrams:

- data pipeline;
- model/evaluation pipeline;
- benchmark task construction;
- reproducibility workflow.

Typical nodes:

```text
Corpus -> task construction -> annotation/gold standard -> models/baselines -> evaluation metrics -> error analysis -> release
```

Guardrails:

- Include leakage control, model versioning, and evaluation metric nodes when relevant.
- Do not imply real-world deployment if only benchmark evaluation was done.

## Systematic Review / Meta-Analysis

Recommended diagrams:

- PRISMA-style flow;
- evidence map;
- screening/extraction/synthesis pipeline.

Typical nodes:

```text
Database records -> de-duplication -> title/abstract screening -> full-text screening -> included studies -> synthesis
```

Guardrails:

- Show exclusion reasons when available.
- Mark counts as `n = ?` if unknown instead of inventing numbers.

## Social Science / Qualitative / Mixed Methods

Recommended diagrams:

- recruitment flow;
- coding framework;
- conceptual model;
- mixed-methods integration flow.

Typical nodes:

```text
Recruitment -> participants/materials -> data collection -> coding/analysis -> themes/model -> validation/member checking
```

Guardrails:

- Avoid overgeneralization arrows.
- Show reflexivity/ethics when relevant.

## Engineering / Systems

Recommended diagrams:

- system architecture;
- module interaction;
- deployment/evaluation workflow;
- requirements-to-validation route.

Typical nodes:

```text
Requirements -> architecture -> modules -> integration -> evaluation -> deployment/iteration
```

Guardrails:

- Distinguish implemented modules from planned modules.
- Distinguish performance test from real-world validation.

## Humanities / Theoretical / Conceptual

Recommended diagrams:

- argument map;
- conceptual taxonomy;
- chronology/source comparison;
- interpretive framework.

Typical nodes:

```text
Research problem -> conceptual lens -> source/material groups -> argument sections -> counterargument -> contribution
```

Guardrails:

- Use `interprets`, `compares`, or `supports` instead of causal arrows.

## Grant / Thesis / Proposal

Recommended diagrams:

- technical roadmap;
- aims-to-methods map;
- timeline/milestone flow;
- risk/fallback diagram.

Typical nodes:

```text
Aim 1/Aim 2/Aim 3 -> methods -> deliverables -> milestones -> expected outcomes
```

Guardrails:

- Mark planned work as planned.
- Do not present expected outcomes as completed results.
