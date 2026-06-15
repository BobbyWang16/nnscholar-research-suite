# Discipline Figure Atlas

Use this file when the request is cross-disciplinary or when the user only says "draw a figure from my data".

## Clinical Medicine

Typical data:
- patient-level rows, clinical endpoints, treatment/exposure groups, model predictions, survival data, subgroup estimates.

High-value figure families:
- cohort flow is a schematic, not this skill;
- baseline or outcome comparison: dot/box/violin with sample size and endpoint definition;
- prediction model: ROC, PR curve for imbalance, calibration curve, decision curve, confusion matrix;
- survival: Kaplan-Meier with number at risk, hazard ratio forest plot;
- treatment effect/subgroup: forest plot with confidence intervals;
- longitudinal toxicity/lab values: line plot with CI or spaghetti + summary.

Minimum fields:
- group comparison: patient/sample id, group, endpoint, time window;
- ROC: true label and predicted score, or precomputed FPR/TPR;
- survival: time, event, group or risk score;
- forest: term/subgroup, estimate, lower CI, upper CI.

## Basic Biomedicine

Typical data:
- biological replicate rows, technical replicates, treatment, dose, time, gene/protein/readout, normalized expression.

High-value figure families:
- treatment comparison: dot + box/violin, mean with CI only when raw points are shown;
- dose-response/time-course: line with replicate bands;
- omics: volcano, heatmap, enrichment dot plot;
- image quantification: paired raw points plus representative images handled separately;
- rescue or mechanism: multi-panel result figure with controls and readouts.

Minimum fields:
- treatment, readout, replicate id, biological vs technical replicate flag when possible;
- omics: feature/gene id, log2FC, p value or adjusted p value.

## AI / Data Science

Typical data:
- dataset/method/metric rows, seed repetitions, ablations, predictions, labels, errors, latency/cost.

High-value figure families:
- benchmark: grouped dot/bar with uncertainty and baseline;
- ablation: ordered bar/dot with delta from full model;
- learning curve: metric vs data size/training step;
- classification: confusion matrix, ROC/PR when labels/scores are available;
- calibration/error: reliability diagram, error distribution, subgroup performance;
- efficiency: latency-throughput, accuracy-cost Pareto plot.

Minimum fields:
- method, dataset, metric, value, seed or fold;
- prediction-level: true label, predicted label, score/probability;
- ablation: component, metric, value, baseline/full model.

## Materials / Chemistry

Typical data:
- composition, batch, synthesis condition, cycle/time, instrument signal, performance metric.

High-value figure families:
- spectra/curves: XRD/FTIR/Raman/UV-vis line plot with offsets or small multiples;
- performance over time/cycles: line with replicate bands;
- composition-property: scatter/line with uncertainty;
- stability/degradation/release: time-course with fit or interval;
- characterization summary: multi-panel combining spectra, morphology quantification, and performance.

Minimum fields:
- sample/material id, condition/composition, x value, y signal/metric, unit, batch/replicate.

## Education / Psychology

Typical data:
- participant rows, scale scores, time points, intervention/control, item responses, construct scores.

High-value figure families:
- pre/post or intervention effect: paired line/slope chart, effect-size forest;
- Likert items: diverging stacked bar;
- scale distribution: violin/box with scale anchors;
- mediation/moderation: coefficient plot or marginal effects.

Minimum fields:
- participant id, group, time point, outcome/scale, scale range, item response labels if Likert.

## Economics / Social Science

Typical data:
- panel rows, treatment timing, units, outcomes, model coefficients, event-time estimates, survey weights.

High-value figure families:
- DID/event study: coefficient plot by event time with pre-trend window;
- regression results: coefficient/forest plot;
- heterogeneity: subgroup coefficient plot;
- descriptive trend: line plot by treatment/comparison group;
- marginal effects: line/ribbon or coefficient plot.

Minimum fields:
- unit, time, treatment/exposure, outcome for descriptive/panel plots;
- term/event time, estimate, lower CI, upper CI for model-output plots.

## Humanities Quantitative / Digital Humanities

Typical data:
- corpus/document rows, period, genre, author, topic, entity, coded category, count/frequency.

High-value figure families:
- frequency over time: line or area plot with corpus-size normalization;
- topic/entity comparison: heatmap, ranked dot plot;
- network metrics: node/edge tables should be routed to a network-specific plot if needed;
- coded evidence distribution: stacked bar or mosaic.

Minimum fields:
- corpus unit/document id, category/topic/entity, count or normalized frequency, time/genre/group.

## Engineering

Typical data:
- run/log rows, operating condition, workload, parameter setting, performance metric, failure/safety event.

High-value figure families:
- performance curves: line/scatter with operating condition labels;
- parameter sweep: heatmap or response surface;
- stress/failure: failure-rate curve, survival-like time-to-failure plot;
- latency-throughput: scatter/Pareto frontier.

Minimum fields:
- system/prototype, workload/condition, parameter, metric, unit, run id.

