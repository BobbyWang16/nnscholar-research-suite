# Discipline Router

Use this reference only when selecting discipline-specific intake questions or feasibility checks.

## Clinical Medicine

Ask:

1. What patient population, disease stage, treatment, and index date are available?
2. Which fields are accessible: records, labs, imaging, medication dates, procedures, outcomes, follow-up?
3. Can endpoints be adjudicated by clinicians or an MDT?

Require:

- PICO/PECO;
- inclusion/exclusion criteria;
- endpoint time window;
- confounder plan;
- missing-data plan;
- ethics/privacy plan.

Common risks: selection bias, immortal time bias, indication bias, endpoint misclassification, insufficient events.

## Basic Biomedicine

Ask:

1. What model is available: cell line, organoid, animal, tissue, omics dataset?
2. What perturbation or intervention can be applied?
3. What readouts and validation/rescue experiments are feasible?

Require:

- biological and technical replicates;
- positive/negative controls;
- dose/time design;
- assay validation;
- rescue or orthogonal validation when mechanism is claimed.

Common risks: batch effect, weak model relevance, antibody/reagent specificity, no rescue validation.

## AI / Data Science

Ask:

1. What dataset, labels, and data split are available?
2. What baselines and metrics are expected in the field?
3. Is there an external test set or deployment-like evaluation?

Require:

- train/validation/test split;
- leakage checks;
- baseline comparison;
- ablation;
- calibration when probabilities guide decisions;
- error/failure-mode analysis.

Common risks: data leakage, overfitting, label noise, benchmark-only claims, missing external validation.

## Materials / Chemistry

Ask:

1. What material, composition, synthesis route, and comparator are available?
2. Which characterization instruments are accessible?
3. Which performance, stability, or degradation tests are feasible?

Require:

- synthesis repeatability;
- batch consistency;
- structural characterization;
- performance comparator;
- stability and stress conditions;
- mechanism evidence if claimed.

Common risks: no standard comparator, irreproducible synthesis, insufficient characterization, cherry-picked performance.

## Education / Psychology

Ask:

1. What population, setting, and intervention/exposure are available?
2. Which validated scales, tests, logs, or behavioral measures can be collected?
3. Can randomization, matching, or pre-post design be used?

Require:

- construct definition;
- validated instruments;
- baseline measurement;
- attrition plan;
- confounder plan;
- ethics and consent.

Common risks: weak construct validity, non-random attrition, teacher/instructor effects, small classroom samples.

## Economics / Social Science

Ask:

1. What unit of analysis, time period, and data source are available?
2. What exposure/treatment and outcome can be measured?
3. What identification strategy is plausible: DID, IV, RDD, panel fixed effects, matching, survey/interview?

Require:

- identification assumptions;
- covariates/confounders;
- robustness checks;
- placebo/falsification tests when possible;
- data provenance and missingness.

Common risks: endogeneity, omitted variables, reverse causality, weak instruments, measurement error.

## Humanities

Ask:

1. What corpus, archive, source collection, period, language, or region is available?
2. What interpretive claim or proposition needs validation?
3. What counter-evidence, comparison cases, or alternative interpretations must be checked?

Require:

- source selection logic;
- provenance and representativeness;
- interpretive framework;
- counterexample search;
- comparison cases;
- limits of inference.

Common risks: selective corpus, presentism, overgeneralization, weak source criticism.

## Engineering

Ask:

1. What system, prototype, simulation, or process is available?
2. What operating conditions and constraints matter?
3. What performance metrics and failure modes should be tested?

Require:

- baseline system;
- controlled inputs;
- stress/failure tests;
- reproducible environment;
- safety constraints;
- performance thresholds.

Common risks: unrealistic conditions, no baseline, insufficient stress testing, hidden hardware/software dependencies.
