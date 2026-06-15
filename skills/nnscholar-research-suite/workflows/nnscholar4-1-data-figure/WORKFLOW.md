---
name: nnscholar4-1-data-figure
description: Use when NNScholar needs to create publication-oriented figures from structured data, statistical results, benchmark tables, experimental measurements, or spreadsheet files. Guides the user through data intake, chart type selection, journal/conference style requirements, robust plotting, export formats, figure captions, and result interpretation. Works across clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities quantitative analysis, and engineering.
---

# NNScholar 4.1 Data Figure

This skill turns structured data into manuscript-ready scientific figures. It is for data-driven plots, not conceptual diagrams or flowcharts. It must work as a cross-disciplinary plotting router: the same button should support clinical prediction, wet-lab results, AI benchmarks, materials curves, education/psychology scales, social-science estimates, humanities quantitative corpora, and engineering performance data.

Version: `0.2.0`. Stage: `paper output / data figure`. Legacy workflow alias: `$nnscholar4-1-data-figure`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar4-1-data-figure` / `/nnscholar4-1-data-figure`.
- Keep the title format as `NNScholar 4.1 Data Figure`.
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

Do not start by drawing. First clarify the discipline, figure's scientific role, data shape, variables, comparison groups, target venue, and export requirements. Then choose the most defensible chart type, create or specify the plot, and write a caption plus result interpretation.

If the user provides data files, inspect their schema before choosing the figure. If no data file is provided, ask for the minimum data table needed.

The key decision is not "which chart is pretty"; it is "which chart truthfully supports this claim for this discipline and this data-generating process."

## Boundary

Use this skill for:

- structured data figures from CSV, XLSX, TSV, JSON, statistical result tables, or pasted tables;
- clinical plots such as baseline comparisons, ROC, calibration, decision curve, forest plot, survival curve, longitudinal trend, subgroup plot;
- biomedical plots such as dose-response, qPCR, western blot quantification, flow cytometry summaries, volcano plot, heatmap, enrichment dot plot;
- AI plots such as benchmark comparison, ablation, learning curve, confusion matrix, calibration, error distribution;
- materials/chemistry plots such as XRD/FTIR/Raman summaries, stress-strain, degradation, release curve, conductivity, adsorption, stability;
- education/psychology plots such as pre-post change, effect size forest, Likert distribution, mediation/moderation visualization;
- economics/social science plots such as event-study, coefficient plot, DID trend, marginal effects, heterogeneity plot;
- engineering plots such as performance curves, latency-throughput, stress test, failure-rate, parameter sweep.

Do not use this skill for:

- conceptual mechanism diagrams, graphical abstracts, model architecture diagrams, or flowcharts; use `nnscholar4-2` when available or `nnscholar2-4-flowchart-design`;
- manuscript tables; use `nnscholar4-4-table-formatting`;
- full manuscript drafting; use `nnscholar4-5-manuscript-drafting`.

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar2-3-paper-architecture`: planned Results sections and figure slots.
2. `nnscholar2-4-flowchart-design`: figure sequence and study route context.
3. `nnscholar3-1-experiment-validation-plan`: validation object, variables, endpoints, readouts, quality controls.
4. `nnscholar2-2-ars-plan`: Aim/Route/Specification, primary/secondary endpoints.
5. `nnscholar1-4-domain-expert-knowledge-base`: domain definitions and accepted reporting norms.
6. User-provided data files, pasted data, statistical outputs, or current request.

When files are not specified, search `references/`, `reference/`, `docs/`, `outputs/`, `data/`, `results/`, and `figures/` for figure plans, data dictionaries, CSV/XLSX files, and result tables. Ask the user to choose only if multiple plausible datasets match.

## Interactive Micro-Rounds

Ask at most 1-3 questions per round.

### Round 0: Discipline and Figure Intake

Return a short card:

```text
Detected discipline / study family:
Detected figure purpose:
Detected data archetype:
Detected data source:
Likely chart family:
Target output:
Missing information:
Next questions:
```

If the request is vague, ask:

1. Which discipline or study family is this: clinical, biomedical, AI, materials, education/psychology, economics/social science, humanities quantitative, engineering, or mixed?
2. What claim should this figure support?
3. What data file/table should be used, and is the target style general manuscript, Nature/Cell/Science, a medical journal, an AI conference, or another venue?

Use `references/discipline-figure-atlas.md` if the discipline, data archetype, or standard figure family is unclear.

### Round 1: Data and Variable Check

Inspect or request:

- data format and sheet/table name;
- row meaning: patient, sample, batch, experiment repeat, model, material, time point, text, institution, or observation;
- data archetype: raw observations, paired/repeated measures, time-to-event, model predictions, model coefficients, spectra/curves, image quantification, benchmark table, survey/scale responses, panel data, corpus counts, or performance logs;
- key columns: x, y, group, subgroup, time, endpoint, uncertainty, p value, model, batch, label, lower/upper confidence interval, score/probability, event, censoring, term, corpus unit;
- missing values, units, ranges, outliers, censoring, repeated measures, clustering, batch effects, paired design, train/test split, or survey weights;
- whether values are raw data, summary statistics, model outputs, or already normalized results.

Never infer a statistical design from column names alone when paired/repeated/censored data may exist.

### Round 2: Chart Route Selection

Use `references/chart-router.md` when selecting a chart family.

Produce 2-3 candidate routes:

- `A. Minimal honest figure`: simplest defensible chart.
- `B. Manuscript-ready figure`: publication default with uncertainty and annotations.
- `C. Stronger multi-panel figure`: combines primary result, robustness, and subgroup/secondary evidence.

For each route include:

- required data columns;
- chart type;
- what claim it can support;
- what it cannot prove;
- risk of misleading presentation;
- recommended route.

### Round 3: Plot Specification

Before drawing, lock a plot specification:

```text
Figure ID:
Discipline / data archetype:
Scientific claim:
Data source:
Chart type:
X / Y / group / facet / time / uncertainty / model estimate:
Statistical annotations:
Color and label rules:
Output formats:
Caption plan:
```

If the user asks for direct drawing and the data are sufficient, proceed without another confirmation.

### Round 4: Generate Figure

Prefer robust, reproducible code.

- For common CSV/XLSX plots, use `scripts/plot_from_table.py` when it fits the requested chart.
- For publication multi-panel figures, load `scientific-visualization` or `nature-figure` as needed.
- For discipline-specific figures beyond the helper script, write a custom Python script and explicitly document required columns and transformations.
- For statistical plots requiring model estimates, do the statistics explicitly or ask for the model output table.
- Save figure code next to the output image when possible.
- Export at least one editable/vector format (`.svg` or `.pdf`) plus one preview (`.png`) unless the user asks otherwise.
- Add a short downstream handoff for `nnscholar4-5-manuscript-drafting`: figure slot, Results insertion cue, one claim sentence the figure supports, and one Methods sentence describing data/analysis provenance.

### Round 5: Caption and Result Interpretation

Always provide:

- figure title;
- manuscript caption;
- legend/color/shape/line meaning when any encoding is used;
- axis labels, units, time windows, and scale/transformation notes;
- statistical annotation note, including test/model, correction, uncertainty interval, and sample size when relevant;
- abbreviation definitions;
- source/data transformation note;
- what the reader should conclude;
- what the figure does not show;
- quality checks and possible failure modes;
- next revision suggestions.

Use `references/figure-output-template.md` for a full report.

## Guardrails

- Preserve raw data; never overwrite user files.
- Use labeled axes with units.
- Do not hide sample size, uncertainty, or censoring when relevant.
- Do not use bar charts for distributions when raw points, box/violin, or interval plots are more honest.
- Do not add significance marks unless the test, comparison, and correction are known.
- Avoid rainbow palettes and inaccessible red-green contrasts.
- For AI benchmarks, show dataset, metric direction, baseline, and variance where available.
- For clinical prediction, separate discrimination, calibration, clinical utility, and external validation.
- For survival analysis, require time, event indicator, group/model, and censoring assumptions.
- For materials characterization, do not smooth or baseline-correct spectra without stating the method.
- For social-science causal figures, distinguish descriptive trends from identification evidence; show pre-trends and uncertainty when relevant.
- For survey/psychology figures, preserve scale direction and label the response anchors.
- For humanities quantitative figures, state corpus selection and coding/counting rules.
- For engineering figures, label operating conditions and do not compare performance across incompatible hardware or workloads.

## Output Rules

Match the user's language. Keep variable names, endpoint names, model names, datasets, journals, and software names in their original form when clearer.

Save generated assets using ASCII slugs:

```text
figures/figure-YYYY-MM-DD-short-topic/
  figure.png
  figure.svg
  figure.pdf
  plot_code.py
  figure_report.md
```

If the workspace lacks a `figures/` folder, create one only when generating files.

For downstream manuscript drafting, make sure `figure_report.md` includes:

```text
4.5 handoff:
Results insertion cue:
Supported claim sentence:
Methods/provenance sentence:
Caption-ready figure title:
Caption-ready figure legend:
Limitations sentence:
```
