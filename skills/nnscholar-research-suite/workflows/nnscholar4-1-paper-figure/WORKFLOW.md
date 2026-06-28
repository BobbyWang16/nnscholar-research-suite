---
name: nnscholar4-1-paper-figure
description: Use when NNScholar needs paper figure production: data plots, statistical charts, benchmark figures, scientific schematics, graphical abstracts, mechanism diagrams, model architecture diagrams, workflow illustrations, multi-panel figure assembly, figure legends, image-generation prompts, journal-ready SVG/PDF/PNG/TIFF exports, and figure quality audits.
---

# NNScholar 4.1 Paper Figure Production

This skill produces manuscript-ready figures. It unifies quantitative plotting, scientific schematics, graphical abstracts, model/workflow diagrams, and multi-panel figure assembly. It is the figure authority for NNScholar Stage 4.

Version: `0.3.0`. Stage: `paper output / figures`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the canonical workflow id as `nnscholar4-1-paper-figure` / `/nnscholar4-1-paper-figure`.
- Keep the title format as `NNScholar 4.1 Paper Figure Production`.
- Name generated folders and files with English ASCII kebab-case slugs.

### Input and Language Policy

- Accept free-form requests, upstream NNScholar outputs, local data files, result tables, images, sketches, Mermaid diagrams, figure plans, manuscripts, reviewer comments, and target-venue instructions.
- For figure planning, audits, captions, and author-facing notes: output in the user's input language unless requested otherwise.
- For manuscript-facing figure titles, captions, legends, callouts, and Methods/Results handoff sentences: default to polished academic English unless the user or venue requests another language.
- Preserve identifiers in their standard form: dataset names, model names, gene/protein symbols, endpoints, metrics, software, trial IDs, DOI/arXiv IDs, file paths, and citation keys.
- Do not fabricate data, sample sizes, image evidence, statistics, or result claims.

### Multidisciplinary Standard

- First classify the discipline and figure family: clinical, biomedical, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, engineering, or interdisciplinary.
- Use field-appropriate figure types and reporting norms.
- Every substantive output should include assumptions, missing information, risk/audit notes, and a revision-ready checklist when applicable.

## Core Rule

Do not start by drawing. First define the figure's scientific role, claim boundary, evidence source, figure family, target venue/export requirements, and whether the figure is numerical, conceptual, assembled from panels, or mixed. Then generate or specify the figure, write caption-ready text, and audit scientific honesty.

The key decision is not "what looks nice"; it is "what visual form truthfully supports this manuscript claim."

## Boundary

Use this skill for:

- structured data figures from CSV/XLSX/TSV/JSON/statistical outputs;
- ROC, calibration, DCA, forest, survival, longitudinal, subgroup, volcano, heatmap, enrichment, spectra, stress-strain, event-study, coefficient, benchmark, ablation, training-curve, confusion-matrix, and performance figures;
- scientific schematics, graphical abstracts, mechanisms, workflows, model architectures, clinical processes, conceptual frameworks, and engineering system diagrams;
- multi-panel figure assembly from plots, images, schematics, microscopy, gel, IHC, SEM/TEM, screenshots, or existing panels;
- figure titles, captions, legends, panel maps, label maps, source manifests, and export audits.

Do not use this skill for:

- manuscript tables; use `nnscholar4-2-paper-table`;
- manuscript drafting or polishing; use `nnscholar4-3-paper-writing`;
- experimental flowcharts whose purpose is protocol design rather than manuscript figure output; use `nnscholar2-2-ars-plan`;
- destructive edits to raw experimental images.

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar2-3-paper-architecture`: figure slots, story order, figure/table blueprint, Figure 1 logic.
2. `nnscholar3-1-experiment-validation-plan`: result summary, raw result paths, claim-evidence map, audit status.
3. `nnscholar2-2-ars-plan`: experimental route, Aim/Route/Specification, endpoint/metric definitions.
4. `nnscholar4-2-paper-table`: companion table titles, notes, and data transformations.
5. `nnscholar1-4-domain-expert-knowledge-base`: expert terminology, mechanisms, domain constraints, reporting norms, visual pitfalls, reviewer risks, and source-backed concept boundaries.
6. User-provided data, images, sketches, manuscripts, or target venue instructions.

When files are not specified, search `figures/`, `images/`, `results/`, `outputs/`, `data/`, `tables/`, `references/`, `docs/`, and `research-runs/` for figure plans, panels, data files, result summaries, and prior 4.x outputs.

## Figure Family Router

| Request / evidence | Route |
|---|---|
| numerical axes, metrics, structured table, statistical output | data figure |
| mechanism, workflow, graphical abstract, model architecture, concept diagram | schematic / generated image / diagram |
| existing panels that need labels, layout, export, or legend | figure assembly |
| Figure 1 or high-impact overview needing both diagram and results | mixed multi-panel figure |
| poster-like, presentation-like, or HTML visual artifact | use companion `paper-poster-html` or `render-html` only as subroutine |

## Workflow

### Step 1: Figure Intake

Return a compact card:

```text
Detected discipline / study family:
Detected figure family:
Scientific claim:
Evidence source:
Target figure slot:
Target venue/export:
Missing information:
Next questions:
```

Ask at most 1-3 questions if needed.

### Step 2: Evidence and Source Check

Inspect or request:

- data schema, image/panel files, result summary, or architecture notes;
- row/column meaning, variables, units, groups, uncertainty, sample size, model/dataset, and split when numerical;
- required nodes, relationships, labels, and evidence boundary when conceptual;
- panel inventory, vector/raster status, scale bars, colorbars, and label constraints when assembling.

Never infer statistical design or image provenance from filenames alone.

### Step 3: Route Options

Produce 2-3 figure routes:

- `A. Minimal honest figure`: simplest defensible visual.
- `B. Manuscript-ready figure`: publication default with caption and audit.
- `C. Stronger multi-panel figure`: combines overview, evidence, robustness, or error analysis.

For each route, include what claim it supports, what it cannot prove, required inputs, and risk of misleading presentation.

### Step 4: Lock Figure Specification

Before generating, lock:

```text
Figure ID:
Figure family:
Scientific claim:
Evidence source:
Panel layout:
Chart/diagram type:
Variables / nodes / panels:
Statistical or label policy:
Color and accessibility policy:
Output formats:
Caption plan:
```

### Step 5: Generate, Draw, or Assemble

Use deterministic tools where possible:

- For common CSV/XLSX plots, prefer `scripts/plot_from_table.py` when it fits.
- For custom plots, write reproducible Python/R code and save it with the figure.
- For schematics, create a visual blueprint and Image2-ready prompt; use built-in `image_gen` only when actual image generation is requested.
- For multi-panel figures, prefer `scripts/assemble_figure.py` with a layout manifest.
- Preserve vector inputs when possible; embed raster panels inside vector wrappers when needed.

External skill additions:

- Use `academic-plotting` patterns for ML/AI architecture diagrams and matplotlib/seaborn benchmark figures.
- Use `figures-python` for robust Python plotting patterns and `figures-diagram` for text-to-diagram prompt structure when useful.
- Use `figure-designer`, `paper-figure`, `figure-spec`, or `paper-illustration` only as companion guidance; NNScholar keeps the figure claim boundary and handoff.

### Step 6: Caption, Legend, and Audit

Always provide:

- figure title;
- caption-ready legend;
- panel map or label map;
- source/provenance note;
- statistical/model note where relevant;
- abbreviation definitions;
- what the figure supports;
- what the figure does not prove;
- quality audit and revision checklist.

For high-impact or Nature/CNS-style figures, read
`../../references/high-impact-paper-guardrails.md` and apply the native figure
contract:

```text
Core conclusion:
Figure archetype:
Final size:
Panel map:
Evidence hierarchy:
Statistics needed:
Source data needed:
Image-integrity notes:
Reviewer risk:
```

Every panel must answer a distinct scientific question. Legends must be
self-contained: panel mapping, color/shape meanings, sample size, error type,
statistical test/correction, units, and source-data notes where relevant.

### Step 7: Expert Knowledge Reference

If a 1.4 expert knowledge base exists, consult it before finalizing the figure
specification and caption. Use it to verify:

- field-specific terms, abbreviations, units, and endpoint names;
- whether the proposed nodes, arrows, mechanisms, and causal wording are
  supported by the expert corpus;
- discipline-specific reporting expectations and reviewer objections;
- which concepts require citation-backed caveats or visual restraint.

If the expert KB contradicts the proposed visual story, mark the figure as
provisional and list the minimum fix.

### Step 8: High-Impact Export and Integrity Gate

For submission-grade figures, audit:

- editable vector output for line art or mixed figures;
- readable font size at final single-column or double-column width;
- no rainbow map, color-only encoding, or inconsistent condition colors;
- traceable source data for quantitative panels;
- image integrity notes for raw file, crop, contrast, pseudo-color, scale bar,
  stitching, reuse, and quantification link;
- model-figure notes for split, seed/fold count, metric definition, CI/variance,
  and baseline definition.

## Discipline Guardrails

- Clinical medicine: separate discrimination, calibration, DCA, external validation, workflow, and clinical utility; avoid causal implication from observational figures.
- Basic biomedicine: distinguish representative images from quantification; preserve scale bars and replicate information.
- AI/data science: include dataset, metric direction, split, baseline, seeds/variance when available, and config/commit provenance for claim-supporting figures.
- Materials/chemistry: state synthesis/test conditions, instrument settings, units, smoothing/baseline correction, and batch/repetition limits.
- Education/psychology: preserve scale direction, response anchors, time points, attrition, and uncertainty.
- Economics/social science: distinguish descriptive plots from identification evidence; show uncertainty, pre-trends, omitted categories, and sample restrictions.
- Humanities: state corpus/source selection, coding/counting rules, and interpretive boundaries.
- Engineering: label workloads, operating conditions, hardware/software environment, units, and failure/stress conditions.

## Supervisor and AI Research Integration

For technical CS/AI figures, read `../../references/supervisor-research-guardrails.md` and apply the Core Figure Gate. For training curves, benchmark tables-as-figures, LLM evaluation, RAG/agent metrics, and experiment trajectories, read `../../references/ai-research-engineering-guardrails.md` and require benchmark settings, run counts, variance/CI where available, metric direction, config, and artifact provenance.

## Output Rules

Match the user's language. Keep labels, endpoint names, model names, datasets, journals, and software names in their original form when clearer.

Save generated assets using ASCII slugs:

```text
figures/figure-YYYY-MM-DD-short-topic/
  figure.svg
  figure.pdf
  figure.png
  figure.tiff
  figure_code.py
  figure_prompt.md
  layout_manifest.json
  figure_report.md
  source_manifest.json
```

Include downstream handoff:

```text
4.3 handoff:
Figure placement:
Results insertion cue:
Panel-by-panel claim map:
Methods/provenance sentence:
Caption-ready title:
Caption-ready legend:
Limitations sentence:
```

## Non-goals

Do not overwrite raw data or raw experimental images. Do not hide sample size, uncertainty, censoring, failed runs, or image provenance. Do not use color-only encoding. Do not add significance marks unless the test/model/comparison is known. Do not recreate copyrighted figures or official logos.
