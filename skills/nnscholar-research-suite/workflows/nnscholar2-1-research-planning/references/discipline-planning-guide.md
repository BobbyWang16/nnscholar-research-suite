# Discipline Planning Guide

Use this guide only when discipline-specific work packages, risks, or quality gates matter. Keep the final plan compact and tailored to the user's current output goal.

## Clinical Medicine and Epidemiology

Typical work packages:

1. Cohort or trial definition: population, inclusion/exclusion criteria, exposure/intervention, comparator, follow-up window.
2. Endpoint and variable dictionary: primary endpoint, secondary endpoints, safety endpoints, covariates, missingness rules.
3. Evidence and guideline alignment: relevant guidelines, trials, registries, systematic reviews, and active trials.
4. Statistical analysis plan: model family, confounding control, subgroup plan, sensitivity analyses, sample size or EPV check.
5. Ethics and data governance: IRB, consent, privacy, data-use agreement, de-identification.
6. Figures/tables and manuscript path: cohort flow, baseline table, outcome table, model/forest plot, limitations.

Quality gates:

- PICO/PECO is explicit.
- Primary endpoint and time window are measurable.
- Treatment/exposure and comparator cannot be misread.
- Confounding, immortal time bias, indication bias, and missing data are surfaced.
- Claims avoid causal language unless design supports causality.

## Basic Biomedicine and Translational Research

Typical work packages:

1. Model and perturbation plan: cell line, animal model, organoid, tissue, omics dataset, genetic or pharmacologic perturbation.
2. Measurement/readout plan: assays, controls, time points, replicates, batch handling.
3. Mechanism and validation plan: rescue, knockdown/overexpression, orthogonal assay, external dataset validation.
4. Analysis plan: normalization, differential analysis, pathway analysis, statistics, multiple testing.
5. Reproducibility and materials: reagent identity, antibody validation, randomization/blinding if relevant.
6. Figure sequence: mechanism schematic, validation panels, quantitative readouts.

Quality gates:

- Model-system limitations are explicit.
- Perturbation and readout test the same mechanism.
- Controls and replicates are sufficient.
- Hypothesis is not drawn as proven mechanism before validation.

## AI, Data Science, and Computational Research

Typical work packages:

1. Task and dataset definition: task boundary, input/output, inclusion/exclusion, splits, labels, provenance.
2. Baseline and comparator plan: simple baseline, current strong baseline, ablations, human or expert comparator when appropriate.
3. Evaluation protocol: metrics, confidence intervals, statistical tests, error taxonomy, robustness checks.
4. Leakage and bias audit: train/test overlap, prompt leakage, label leakage, demographic/domain bias, benchmark contamination.
5. Reproducibility package: code, environment, seeds, model versions, data cards, prompt logs.
6. Results and writing: main table, ablation table, failure cases, limitations, release plan.

Quality gates:

- Dataset and benchmark are separable from model development.
- Metrics match the scientific question.
- Baselines are strong enough to make the result meaningful.
- Compute and data licensing constraints are visible.

## Education, Psychology, and Social Science

Typical work packages:

1. Theory and construct map: theory, construct definition, hypothesized pathway, measurement model.
2. Instrument and data plan: validated scales, interview guide, observation rubric, learning outcomes, reliability plan.
3. Sampling and recruitment: population, setting, sample size rationale, inclusion/exclusion, attrition plan.
4. Design and analysis: experimental, quasi-experimental, longitudinal, mixed-methods, qualitative coding, mediation/moderation.
5. Ethics and participant protection: consent, privacy, minors/vulnerable groups, intervention risk.
6. Reporting path: preregistration, transparent materials, effect sizes, qualitative trustworthiness.

Quality gates:

- Constructs are not confused with measurement instruments.
- Instruments are validated or adaptation is justified.
- Confounders and contextual effects are addressed.
- Qualitative and quantitative strands have compatible integration logic.

## Materials, Chemistry, and Engineering

Typical work packages:

1. Composition/process plan: synthesis route, formulation, fabrication parameters, controls.
2. Characterization plan: structure, morphology, chemistry, stability, reproducibility, batch variance.
3. Performance testing: target application, comparator, stress tests, cycling/durability, safety.
4. Mechanism analysis: structure-property-performance relation, kinetics, interfacial chemistry, failure mode.
5. Scale-up and reproducibility: yield, cost, equipment, environmental/safety constraints.
6. Figure/table plan: synthesis schematic, characterization panels, performance benchmark, mechanism diagram.

Quality gates:

- Comparator is field-relevant.
- Characterization supports the claimed mechanism.
- Performance metric matches the application.
- Safety and reproducibility are not left until writing.

## Reviews, Meta-Analyses, and Evidence Maps

Typical work packages:

1. Review question and eligibility: PICO/SPIDER/PCC as appropriate.
2. Search protocol: databases, strings, date range, grey literature, language limits.
3. Screening and extraction: dedupe, title/abstract screening, full-text screening, extraction fields.
4. Quality appraisal: risk of bias, certainty, heterogeneity, evidence gaps.
5. Synthesis: narrative synthesis, meta-analysis feasibility, subgroup/sensitivity analysis.
6. Reporting: PRISMA flow, evidence table, limitations, update strategy.

Quality gates:

- Search is reproducible.
- Inclusion/exclusion criteria are operational.
- Screening counts and exclusion reasons are recorded.
- Meta-analysis is not forced when heterogeneity is too high.
