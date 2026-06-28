# Chart Router

Use this file only when deciding which data-driven chart to recommend.

## Universal Questions

1. What is the claim: comparison, trend, association, distribution, prediction, classification, composition, ranking, mechanism support, or robustness?
2. What is the data level: raw observations, summary statistics, model estimates, image-derived quantification, spectra, or benchmark table?
3. Is the design independent, paired, repeated, longitudinal, clustered, censored, or externally validated?
4. Does the reader need exact values, uncertainty, group separation, temporal dynamics, or model performance?

## Common Routes

| Claim / data task | Preferred chart | Avoid |
|---|---|---|
| Compare two or more independent groups with raw observations | dot + box/violin, mean/median interval | bar-only charts without raw points |
| Compare paired pre/post or matched samples | paired line plot, slope chart, paired interval plot | independent boxplot only |
| Time course / dose response / longitudinal mean | line plot with confidence interval and raw/facet option | disconnected bars |
| Many features across groups | heatmap with clustering or ordered rows | unreadable grouped bars |
| Model or method benchmark | grouped dot/bar with uncertainty, critical difference plot | single metric without baseline |
| Ablation study | ordered bar/dot plot with baseline and delta labels | random method order |
| Regression or model effects | coefficient / forest plot with confidence intervals | table-only effect estimates |
| Binary classifier | ROC plus PR curve when imbalance exists | ROC alone for imbalanced data |
| Prediction model | calibration curve, decision curve, discrimination plot | AUC-only figure |
| Survival / time-to-event | Kaplan-Meier curve, hazard forest plot | simple endpoint bar chart |
| Event-study / DID | event-time coefficient plot with pre-trend window | post-only comparison |
| Materials performance over cycles/time | line plot with replicate bands, stability inset | cherry-picked endpoint bar |
| Spectra / curves | overlaid curves with offsets or small multiples | excessive smoothing |
| Composition / proportion | stacked bar, alluvial, mosaic, dot proportion | pie chart for many classes |
| Likert / ordinal responses | diverging stacked bar | mean-only bar chart |
| Omics differential results | volcano plot, heatmap, enrichment dot plot | p-value table only |
| Corpus counts over time | normalized frequency line/area plot | raw count trend without corpus size |
| Engineering parameter sweep | heatmap, contour/response surface, Pareto scatter | one endpoint without operating conditions |

## Helper Script Coverage

`scripts/plot_from_table.py` can be used for straightforward:

- `scatter`, `line`, `bar`, `point`, `box`, `violin`, `hist`, `heatmap`;
- `forest` or `coef` when a result table has `label`, `estimate`, `lower`, `upper`;
- `volcano` when a result table has `log2FC` and `p`/`padj`;
- `roc` when a result table has precomputed `fpr` and `tpr`;
- `stacked_bar` when data contain category/group/value columns.

For survival curves, calibration curves, PR curves from raw predictions, decision curves, enrichment plots, spectra preprocessing, or complex multi-panel layouts, write custom code and document the assumptions.

## Discipline Notes

- Clinical medicine: include sample size, endpoint definition, time window, adjustment status, and validation split.
- Basic biomedicine: show biological replicates separately from technical replicates; label dose/time and controls.
- AI/data science: label dataset, metric direction, baseline, seed/repetition, and train/test split.
- Materials/chemistry: label units, batch count, test condition, instrument-derived preprocessing.
- Education/psychology: label scale range, construct, time point, attrition, and effect size.
- Economics/social science: show confidence intervals, fixed effects or controls status, and robustness/pre-trend where relevant.
- Humanities quantitative work: explain corpus selection and counting/encoding rules.
