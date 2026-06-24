# Publication Visual Pattern Library

Use this library together with `references/figure-screenshot-gallery.md` when a
task needs concrete, portable reference examples for tables, subfigures,
multi-panel figures, flowcharts, or data-analysis plots. The examples are
original pattern cards. They do not require Zotero at runtime.

## Crop And Keep Rules

- **Keep full reference**: inspect the bundled full crop as a whole when panel
  ordering, density, or storyline matters.
- **Crop subpanel only**: inspect a subregion only when the user asks for a
  specific chart type or panel role, and preserve the source DOI/license in the
  handoff.
- **Abstract structure only**: use the layout logic, row/column schema, or
  panel sequence without reusing visual content.
- **Never final-copy**: generate original tables, plots, schematics, and
  captions for the user's project.

## Three-Line Tables

Use three-line tables for manuscript-ready statistical summaries: top rule,
header rule, bottom rule, minimal vertical lines, compact footnotes, explicit
units, and aligned estimates.

- Example 1: Cohort baseline table. Rows: age, sex, stage, modality timepoints,
  treatment, endpoint, missingness. Columns: training, internal validation,
  external validation, and P value. Crop/keep rule: abstract structure only.
- Example 2: Model performance table. Rows: candidate models and baselines.
  Columns: AUC, AUPRC, sensitivity, specificity, calibration slope, Brier score,
  DCA net benefit, and 95% CI. Crop/keep rule: abstract structure only.
- Example 3: Radiomics feature table. Rows: feature families or selected
  features. Columns: source image, stability filter, coefficient/rank, direction,
  biological interpretation, and validation cohort. Crop/keep rule: abstract
  structure only.
- Example 4: Segmentation benchmark table. Rows: organs, lesions, or classes.
  Columns: Dice, HD95, precision, recall, failure count, and reader adjudication.
  Crop/keep rule: abstract structure only.
- Example 5: Ablation table. Rows: model variants. Columns: removed component,
  input modality, internal metric, external metric, calibration, and conclusion.
  Crop/keep rule: abstract structure only.
- Example 6: Missing-modality table. Rows: modality availability patterns.
  Columns: sample count, missingness reason, imputation/fusion route, AUC, C
  index, and robustness note. Crop/keep rule: abstract structure only.
- Example 7: Subgroup analysis table. Rows: age group, stage, scanner/vendor,
  center, treatment subgroup. Columns: N, effect estimate, CI, interaction P,
  and interpretation boundary. Crop/keep rule: abstract structure only.
- Example 8: External validation table. Rows: external cohorts. Columns: site,
  country/region, inclusion window, scanner/modality, endpoint, model metric,
  and dataset shift note. Crop/keep rule: abstract structure only.
- Example 9: Data/code availability table. Rows: dataset, annotation, model
  weights, code, pretrained embeddings, and scripts. Columns: availability,
  access condition, identifier/link, license, and restriction. Crop/keep rule:
  abstract structure only.
- Example 10: Reviewer-response change table. Rows: reviewer concern, revision
  action, added analysis, manuscript location, and residual limitation. Columns:
  reviewer, issue, response type, evidence added, and line/page pointer.
  Crop/keep rule: abstract structure only.

## Subfigure And Group-Figure Layouts

Use these examples when assembling multi-panel figures with letters, shared
legends, common axes, and a clear panel hierarchy.

- Example 1: Dataset-to-model overview group. Reference: `figref-01` or
  `figref-09`. Panels: dataset source, preprocessing, model, downstream tasks,
  external validation. Crop/keep rule: keep full reference for storyline.
- Example 2: Performance-focused group. Reference: `figref-02` or `figref-10`.
  Panels: bar comparison, ROC, CI/uncertainty, external cohort contrast.
  Crop/keep rule: crop subpanel only for chart grammar; keep full reference for
  ordering.
- Example 3: Cohort-design plus validation group. Reference: `figref-03` and
  `figref-04`. Panels: patient flow, imaging/assay linkage, model output, ROC,
  confusion or threshold analysis. Crop/keep rule: keep full reference.
- Example 4: Longitudinal imaging-biology group. Reference: `figref-05` and
  `figref-06`. Panels: timepoints, temporal encoder, response endpoint, immune
  association, validation metrics. Crop/keep rule: keep full reference.
- Example 5: Multimodal missingness group. Reference: `figref-07` and
  `figref-08`. Panels: modality availability, encoder branches, fusion block,
  missing-modality stress test, endpoint. Crop/keep rule: keep full reference.
- Example 6: Pathology diagnostic group. Reference: `figref-11`. Panels:
  representative regions, model label map, diagnostic outputs, validation cohort,
  failure examples. Crop/keep rule: crop subpanel only for visual-example roles.
- Example 7: Pathology prognostic group. Reference: `figref-12`. Panels:
  quantitative feature map, score distribution, survival stratification, clinical
  covariate adjustment. Crop/keep rule: keep full reference.
- Example 8: Radiomics habitat group. Panels: raw CT/MRI slice, ROI mask,
  habitat map, selected features, model performance, interpretation.
  Crop/keep rule: abstract structure unless a bundled image matches the
  modality.
- Example 9: Survival-model group. Panels: cohort split, risk-score histogram,
  Kaplan-Meier curve, time-dependent ROC, calibration, multivariable forest plot.
  Crop/keep rule: abstract structure only.
- Example 10: Manuscript Figure 1 group. Panels: clinical problem, cohort
  design, model route, primary result, biological or translational validation.
  Crop/keep rule: keep full reference for panel hierarchy; generate originals.

## Flowcharts

Use flowcharts for study design, analysis routes, reproducibility workflows, and
reviewer-facing method clarification. Keep labels short and make each arrow a
real transformation.

- Example 1: Dataset curation flow. Source datasets -> eligibility filters ->
  de-identification -> preprocessing -> split -> audit log. Crop/keep rule: keep
  full reference if using `figref-01`; otherwise abstract structure.
- Example 2: Clinical cohort flow. Screened patients -> exclusions -> eligible
  cohort -> train/internal/external cohorts -> endpoint availability. Crop/keep
  rule: abstract structure only.
- Example 3: Longitudinal imaging flow. Baseline MRI -> mid-treatment MRI ->
  temporal alignment -> transformer encoder -> response prediction. Crop/keep
  rule: keep full reference if using `figref-05`.
- Example 4: Segmentation workflow. Image volume -> prompt/ROI -> model mask ->
  postprocessing -> reader QC -> Dice/HD95 report. Crop/keep rule: abstract
  structure only.
- Example 5: Multimodal fusion flow. Radiology branch + pathology branch +
  clinical covariates -> fusion -> risk score -> validation. Crop/keep rule: keep
  full reference if using `figref-07` or `figref-08`.
- Example 6: Radiogenomics flow. Imaging phenotype -> feature embedding ->
  immune/pathway association -> external assay validation -> claim boundary.
  Crop/keep rule: keep full reference if using `figref-05`.
- Example 7: Model evaluation flow. Patient-level split -> model selection ->
  discrimination -> calibration -> DCA -> subgroup analysis. Crop/keep rule:
  abstract structure only.
- Example 8: Figure-production flow. Data audit -> plot choice -> draft panel ->
  statistical annotation -> caption -> DPI/export check. Crop/keep rule: abstract
  structure only.
- Example 9: Submission-compliance flow. Target journal -> limits/checklists ->
  figures/tables -> statements -> source files -> final human submit. Crop/keep
  rule: abstract structure only.
- Example 10: Reviewer-response flow. Comment cluster -> evidence gap -> added
  analysis -> manuscript edit -> response paragraph -> residual limitation.
  Crop/keep rule: abstract structure only.

## Data-Analysis Plots

Use these examples when the user provides data or asks for plotting code,
statistical visuals, or publication figure panels.

- Example 1: ROC panel. Plot internal and external cohorts separately, include
  AUC with CI, patient-level split note, and baseline model. Crop/keep rule: crop
  subpanel only from `figref-04`, `figref-06`, or `figref-10` for grammar.
- Example 2: Precision-recall panel. Use when class imbalance matters; report
  prevalence, AUPRC, baseline prevalence line, and threshold marker. Crop/keep
  rule: abstract structure only.
- Example 3: Calibration panel. Show observed vs predicted risk, calibration
  slope/intercept, confidence band, and cohort facets. Crop/keep rule: abstract
  structure only.
- Example 4: Decision-curve panel. Plot net benefit across threshold
  probabilities with treat-all/treat-none references. Crop/keep rule: abstract
  structure only.
- Example 5: Kaplan-Meier panel. Show number at risk, hazard ratio, log-rank P,
  censoring marks, and prespecified cutoff method. Crop/keep rule: abstract
  structure only.
- Example 6: Forest plot. Use for subgroup or multivariable estimates; include
  reference group, effect estimate, CI, interaction P, and sample count. Crop/keep
  rule: abstract structure only.
- Example 7: Violin/box/swarm panel. Use for score distributions across response
  groups; show sample count, test, effect size, and outlier policy. Crop/keep
  rule: crop subpanel only from performance references if needed.
- Example 8: Heatmap panel. Use for features, pathways, immune cells, or
  modality contribution; include clustering method, scale, colorbar, and
  annotation tracks. Crop/keep rule: abstract structure only.
- Example 9: Confusion-matrix panel. Use absolute counts and normalized
  percentages, label axes clearly, and pair with threshold information. Crop/keep
  rule: crop subpanel only from `figref-04` if needed.
- Example 10: Ablation/missing-modality panel. Plot model variants with
  confidence intervals, external-cohort facets, and missingness pattern labels.
  Crop/keep rule: keep full reference if using `figref-07` or `figref-08`.

## Companion Skill Example Packs

Use these packs when NNScholar hands off to an installed specialist skill. Each
pack gives at least five examples so the specialist behavior has concrete local
anchors.

### companion-radiology-skills

- Example 1: CT radiomics project: verify ROI source, voxel spacing,
  resampling, feature stability, and external scanner/vendor validation.
- Example 2: MRI response project: separate baseline, interim, and delta
  features; require timepoint availability and leakage checks.
- Example 3: Segmentation project: report annotation protocol, inter-reader
  adjudication, Dice/HD95, and failure-case review.
- Example 4: Imaging foundation model: document pretraining data, target task,
  OOD center testing, and baseline comparison.
- Example 5: Clinical translation: bind each imaging claim to endpoint,
  validation cohort, calibration, and decision utility.

### companion-dl-radiology-skill

- Example 1: Deep-learning pipeline: dataset audit -> preprocessing -> model ->
  training split -> external validation -> interpretability.
- Example 2: Transfer learning: compare random initialization, ImageNet,
  radiology pretraining, and task-specific finetuning under low-label settings.
- Example 3: Multimodal model: define image encoder, clinical encoder, fusion
  layer, missing-modality route, and ablation design.
- Example 4: Model robustness: test scanner/vendor shift, reconstruction kernel,
  slice thickness, and center-held-out cohorts.
- Example 5: Reporting: include architecture, hyperparameters, split strategy,
  calibration, uncertainty, and reproducibility artifacts.

### companion-medical-research-skills

- Example 1: Clinical question: specify population, intervention/model,
  comparator, endpoint, setting, and time horizon.
- Example 2: Observational study: identify confounding, selection bias,
  missingness, sensitivity analyses, and causal boundary.
- Example 3: Diagnostic/prognostic model: require TRIPOD-style cohort
  description, validation, calibration, and clinical utility.
- Example 4: Treatment-response project: lock response definition, assessment
  window, comparator, and subgroup plan before writing claims.
- Example 5: Ethics/reporting: flag IRB, consent, data privacy, dataset access,
  and human oversight requirements.

### companion-literature-evidence-skills

- Example 1: Search strategy: split terms by disease, modality, model family,
  endpoint, and validation type.
- Example 2: Screening rubric: define inclusion/exclusion criteria, study type,
  imaging modality, endpoint, and minimum validation.
- Example 3: Evidence matrix: extract cohort, intervention/model, comparator,
  metric, validation, limitations, and DOI.
- Example 4: Claim calibration: downgrade causal language when evidence is
  associative or single-center.
- Example 5: Citation chasing: use seed papers, forward citations, backward
  references, and method neighbors.

### companion-manuscript-submission-skills

- Example 1: Paper architecture: map clinical problem -> method -> validation ->
  interpretation -> limitation -> next-step claim.
- Example 2: Figure legend: state panel role, cohort, metric, statistical test,
  and abbreviation definitions.
- Example 3: Table formatting: use three-line tables, units in headers, compact
  notes, and no unexplained abbreviations.
- Example 4: Cover letter: pitch unmet need, novelty, validation strength, and
  bounded clinical relevance.
- Example 5: Reviewer response: answer each concern with action, evidence,
  manuscript location, and residual limitation.
