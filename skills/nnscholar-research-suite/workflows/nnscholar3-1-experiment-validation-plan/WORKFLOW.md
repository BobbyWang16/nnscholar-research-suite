---
name: nnscholar3-1-experiment-validation-plan
description: Use when NNScholar needs to turn a research hypothesis, ARS plan, protocol, paper architecture, or broad research idea into an interactive experiment or validation plan with step-by-step resource intake, discipline-aware validation route selection, expected results, disconfirming results, feasibility analysis, risk review, quality controls, pilot plan, and go/no-go criteria. Works across clinical medicine, basic biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, and engineering.
---

# NNScholar 3.1 Experiment and Validation Plan

This skill converts a research hypothesis into the most feasible experiment or validation pathway. It is intentionally cross-disciplinary: "experiment" can mean a clinical cohort, wet-lab assay, AI benchmark, materials characterization, survey/intervention, econometric identification, archival/textual validation, or engineering test.

Version: `0.2.0`. Stage: `experiment and validation / feasibility planning`. Legacy workflow alias: `$nnscholar3-1-experiment-validation-plan`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar3-1-experiment-validation-plan` / `/nnscholar3-1-experiment-validation-plan`.
- Keep the title format as `NNScholar 3.1 Experiment and Validation Plan`.
- Name generated folders and files with English ASCII kebab-case slugs, preferably `phase-step-yyyy-mm-dd-topic`, regardless of the report language.

### Input and Language Policy

- Accept free-form user input, upstream NNScholar outputs, local files, pasted tables, figures, reviewer comments, and target-venue instructions when relevant.
- For research planning, literature, experiment, figure/table planning, audits, and author-facing notes: output in the user's input language unless the user requests another language.
- For manuscript-facing text, including titles, abstracts, manuscript sections, figure legends, table titles/notes, cover letters, submission statements, and reviewer responses: default to polished academic English unless the user or target venue explicitly asks for Chinese, bilingual, or another language.
- Preserve identifiers in their standard form: database names, DOI/PMID/arXiv IDs, trial IDs, gene/protein symbols, chemical formulas, datasets, benchmarks, model names, scales, laws, policies, and citation keys.
- Search strings and database queries should normally be formulated in English, then explained in the output language.

### Multidisciplinary and Revision Standard

- First classify the discipline and study family: clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, engineering, or interdisciplinary.
- Use field-appropriate evidence, methods, reporting norms, and terminology. Do not force biomedical templates onto non-biomedical work.
- Every substantive output should include, when applicable: assumptions, missing information, author queries, risk/audit notes, and a revision-ready checklist.
- Do not fabricate citations, ethics approvals, registrations, sample sizes, statistics, experimental results, author declarations, or venue requirements. Mark uncertain items as `needs verification`.
- When revising or polishing, preserve scientific meaning, numeric values, methods, and claim strength unless the user supplies evidence and explicitly asks for a change.

## Core Rule

Do not jump straight to a polished protocol. First guide the user through a short interactive resource intake, then recommend the most feasible validation route, expected results, disconfirming results, and feasibility risks.

If upstream NNScholar outputs exist, use them. If not, start from the user's hypothesis or idea.

## Upstream Priority

Use local files in this order:

1. `nnscholar1-3-hypothesis-generation`: locked hypothesis, variables, endpoints, disconfirming observations.
2. `nnscholar2-2-ars-plan`: protocol lock, Aim/Route/Specification, quality gates.
3. `nnscholar2-1-research-planning`: timeline, resources, milestones.
4. `nnscholar2-4-flowchart-design`: route diagram and method sequence.
5. `nnscholar1-2-literature-searching`: method precedents and evidence gaps.
6. `nnscholar1-1-question-mining`: original gap and not-recommended directions.
7. Current user input.

When files are not specified, search `references/`, `reference/`, `docs/`, and `outputs/` by skill id, topic keywords, hypothesis terms, disease/material/dataset names, and report headings. Ask the user to choose only if multiple plausible bundles match.

## Interactive Micro-Rounds

Ask at most 1-3 questions per round. Keep questions practical and resource-focused.

### Round 0: Evidence Intake

Return a short card:

```text
Current hypothesis:
Detected discipline / study type:
Likely validation route:
Missing resource information:
Next questions:
```

If the hypothesis and study type are clear, proceed. If not, ask:

1. What hypothesis or claim should be validated?
2. What discipline or study system is this: clinical, biomedical, AI, materials, social science, humanities, engineering, or mixed?
3. Do you already have data, samples, materials, documents, equipment, or collaborators?

### Round 1: Discipline and Validation Type

Auto-detect the validation family and ask the user to confirm. Use `references/discipline-router.md` when the discipline is unclear or when crafting discipline-specific questions.

Validation families:

- clinical cohort / case-control / diagnostic or predictive model / RCT;
- cell, animal, organoid, omics, perturbation, mechanism validation;
- AI benchmark, baseline comparison, ablation, external test set;
- materials synthesis, characterization, performance, stability;
- education/psychology intervention, scale measurement, pre-post or quasi-experiment;
- economics/social science panel data, DID, IV, RDD, survey, interview;
- humanities textual, archival, comparative case, counter-evidence validation;
- engineering prototype, simulation, stress test, performance evaluation.

### Round 2: Resource and Constraint Intake

Ask discipline-aware questions. Always cover:

- available data/samples/materials/corpus;
- approximate sample size, repetitions, cases, texts, batches, or observations;
- equipment/software/database/access;
- ethical, privacy, safety, budget, timeline, or collaborator constraints;
- whether a control/comparator/baseline is available.

### Round 3: Candidate Validation Routes

Generate 2-3 routes:

- `A. Minimum feasible validation`: smallest credible test.
- `B. Standard validation`: publishable default if resources allow.
- `C. Ideal validation`: stronger but more resource-intensive.

For each route include:

- required resources;
- core steps;
- expected result if the hypothesis is supported;
- disconfirming result;
- feasibility score from 1-5;
- biggest risk.

Then recommend one route and explain why.

### Round 4: Locked Step-by-Step Plan

After user confirmation or if the user asks for a direct output, produce the plan:

- validation objective;
- study object / samples / data / corpus / materials;
- control or comparator;
- key variables and readouts;
- step-by-step procedure;
- expected results;
- disconfirming results;
- minimum viable version;
- ideal extension.

Steps must be executable. Avoid generic instructions such as "analyze the data" without saying which data, which comparison, and which output.

### Round 5: Feasibility and Quality Analysis

Audit the locked plan:

- feasibility score;
- resource gaps;
- bias/confounding/leakage/batch-effect risks;
- measurement validity;
- ethical/safety/privacy/compliance risks;
- quality controls;
- pilot test;
- go/no-go criteria;
- fallback plan if the main route fails.

Use `references/validation-output-template.md` when saving a full report.

## Discipline-Specific Guardrails

- Clinical medicine: define index date, population, exposure, comparator, endpoint, time window, adjudication rules, confounding, and ethics.
- Basic biomedicine: define model, perturbation, dose/time, controls, readouts, biological replicates, rescue/validation logic.
- AI/data science: define dataset, labels, split, baseline, metric, ablation, external test, leakage checks, compute constraints.
- Materials/chemistry: define synthesis route, composition, characterization, performance test, comparator, batch repeatability, stability.
- Education/psychology: define constructs, validated scales, intervention, randomization or quasi-experiment, pre/post measurement, attrition.
- Economics/social science: define identification strategy, treatment/exposure, outcome, data source, confounders, robustness tests.
- Humanities: define corpus/archive, selection logic, interpretive framework, counter-evidence, comparison cases, source criticism.
- Engineering: define prototype/system, inputs, operating conditions, performance metrics, stress/failure tests, safety constraints.

## Output Rules

Match the user's language. Keep standard names, variables, endpoints, trial IDs, datasets, software, statistical terms, and file names in their original form when clearer.

Save full reports to `references/` or `reference/` using:

```text
validation-plan-YYYY-MM-DD-short-topic.md
```

Use English ASCII slugs for file names.

## Non-Goals

Do not:

- invent resources the user does not have;
- present an ideal experiment as feasible without checking constraints;
- ignore ethical, privacy, safety, or compliance requirements;
- treat observational validation as causal proof without identification strategy;
- treat AI benchmark performance as real-world validation without external testing;
- treat humanities interpretation as an experimental causal claim;
- lock a protocol if key resources or endpoints are missing.
