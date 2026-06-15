# Discipline Architecture Guide

Use this guide when `nnscholar2-3-paper-architecture` needs discipline-specific manuscript logic.

## Selection Rule

Choose the article family from the user's topic, protocol, target venue, method, data type, and discipline. If uncertain, propose 2-3 article families and ask the user to pick.

## Clinical / Public Health / Epidemiology

Typical structure:

- Introduction: disease burden -> current evidence -> clinical gap -> objective/hypothesis.
- Methods: design, setting, population, exposure/intervention, outcomes, covariates, statistical analysis, ethics.
- Results: cohort flow, baseline characteristics, primary outcome, adjusted analyses, subgroup/sensitivity analyses.
- Discussion: principal findings, comparison with studies, mechanism/clinical interpretation, strengths/limitations, implication.

Figure/table pattern:

- Figure 1: cohort flow / study design.
- Table 1: baseline characteristics.
- Figure 2: primary outcome, survival curve, effect estimate, or main model result.
- Table 2: adjusted model.
- Supplement: subgroup/sensitivity, missingness, variable definitions.

Claim boundary:

- Observational studies support association, prediction, or real-world signal; avoid causal claims unless design supports them.

## Basic / Translational / Wet-Lab

Typical structure:

- Introduction: biological process -> unknown mechanism -> hypothesis.
- Methods: cells/animals/samples, assays, controls, interventions, readouts, replicates, statistics.
- Results: validation, primary mechanism result, perturbation/rescue, orthogonal confirmation.
- Discussion: mechanism model, relation to prior biology, translational meaning, limitations.

Figure/table pattern:

- Figure 1: model/system validation.
- Figure 2: primary phenotype/mechanism.
- Figure 3: perturbation or dose/time course.
- Figure 4: rescue/validation/clinical correlation.

Claim boundary:

- Separate mechanistic evidence from translational implication; avoid clinical efficacy claims from preclinical data.

## Computational / AI / Statistics / Benchmark

Typical structure:

- Introduction: task importance -> limitations of existing methods/benchmarks -> contribution.
- Methods: dataset/corpus/task, model/baseline, experimental setup, metrics, reproducibility, leakage control.
- Results: benchmark overview, main performance, ablation, robustness, error analysis.
- Discussion: what performance means, failure modes, generalizability, limitations.

Figure/table pattern:

- Table 1: dataset/task statistics.
- Figure 1: pipeline or benchmark design.
- Table 2: main performance comparison.
- Figure 2: ablation/robustness/error categories.
- Supplement: prompts, hyperparameters, model versions, annotation rubric.

Claim boundary:

- Claims depend on dataset scope, leakage control, evaluation validity, and model version stability.

## Engineering / Systems / Design Science

Typical structure:

- Problem/context -> design requirements -> system/method architecture -> implementation -> evaluation -> deployment/limitations.

Figure/table pattern:

- Figure 1: system architecture.
- Table 1: requirements/design constraints.
- Figure 2: workflow or module interaction.
- Table 2: evaluation metrics/performance.
- Figure 3: case study or stress test.

Claim boundary:

- Distinguish implemented capability from validated performance and real-world adoption.

## Social Science / Education / Policy / Qualitative

Typical structure:

- Introduction: social phenomenon -> literature/theory gap -> research questions.
- Methods: setting, participants/corpus, sampling, instruments/interviews, coding/analysis, reflexivity, ethics.
- Results/Findings: themes, models, quantitative patterns, case evidence.
- Discussion: theoretical contribution, policy/practice implications, limitations.

Figure/table pattern:

- Table 1: participant/sample/context characteristics.
- Figure 1: conceptual framework.
- Table 2: themes/coding framework.
- Figure 2: model of relationships or mechanism.

Claim boundary:

- Avoid overgeneralization beyond sample/context; state positionality and transferability limits when needed.

## Humanities / Theoretical / Conceptual

Typical structure:

- Research problem -> conceptual background -> interpretive/theoretical framework -> argument sections -> counterarguments -> contribution.

Figure/table pattern:

- Tables are optional; use concept maps, chronology, taxonomy, or comparative matrix only when helpful.

Claim boundary:

- Emphasize argumentative coherence, textual/source grounding, and interpretive limits instead of empirical certainty.

## Systematic Review / Scoping Review / Meta-Analysis

Typical structure:

- Introduction: field uncertainty -> review objective.
- Methods: protocol/registration, databases, search strategy, eligibility, screening, extraction, risk of bias, synthesis.
- Results: PRISMA flow, study characteristics, evidence map, synthesis/meta-analysis.
- Discussion: evidence certainty, heterogeneity, limitations, implications.

Figure/table pattern:

- Figure 1: PRISMA flow.
- Table 1: included study characteristics.
- Figure/Table 2: evidence map or forest plot.
- Table 2: risk of bias/quality.

Claim boundary:

- Match conclusions to evidence certainty and heterogeneity; avoid overclaiming when evidence quality is low.

## Thesis / Grant / Proposal

Typical structure:

- Background/significance -> gap -> aims -> innovation -> approach -> expected outcomes -> risks/fallbacks -> timeline.

Figure/table pattern:

- Figure 1: conceptual model or technical route.
- Table 1: aims and deliverables.
- Table 2: timeline/milestones.
- Figure 2: risk/fallback map.

Claim boundary:

- Frame as planned work, feasibility, and expected contribution, not completed findings.
