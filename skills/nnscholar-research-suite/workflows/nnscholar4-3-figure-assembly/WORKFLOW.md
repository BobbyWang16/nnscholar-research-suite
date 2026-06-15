---
name: nnscholar4-3-figure-assembly
description: Use when NNScholar needs to assemble scientific multi-panel figures from existing subfigures, experimental images, microscopy/gel/IHC/SEM/TEM panels, data plots, Image2 schematics, model diagrams, or table-like image panels. Produces publication-oriented vector-first figure layouts with panel labels, spacing, consistent typography, figure legend, layout manifest, and SVG/PDF/PNG exports. Works across clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, and engineering.
---

# NNScholar 4.3 Figure Assembly

This skill assembles existing visual assets into manuscript-ready multi-panel figures. It does not primarily create new data plots or new Image2 schematics; it arranges, labels, audits, and exports a full figure such as `Figure 1A-F`.

Version: `0.2.0`. Stage: `paper output / figure assembly`. Legacy workflow alias: `$nnscholar4-3-figure-assembly`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar4-3-figure-assembly` / `/nnscholar4-3-figure-assembly`.
- Keep the title format as `NNScholar 4.3 Figure Assembly`.
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

Do not simply stitch images together. First determine the figure's scientific story, panel roles, required order, target venue dimensions, and whether each source panel is vector or raster. Then create a layout plan, assemble a vector-first figure, and write a figure legend.

Preserve vector inputs when possible. Do not pretend microscopy, gel, histology, SEM/TEM, or photos are vector; embed them as raster panels inside a vector SVG/PDF wrapper.

## Boundary

Use this skill for:

- multi-panel paper figures from existing subfigures;
- combining 4.1 data figures and 4.2 Image2 schematics;
- arranging experimental images with quantitative plots;
- adding A/B/C/D labels, panel titles, spacing, and consistent typography;
- creating figure legends and panel maps;
- exporting `SVG`, `PDF`, `PNG`, and optionally `TIFF`.

Do not use this skill for:

- generating a new data plot from raw data; use `nnscholar4-1-data-figure`;
- generating a new schematic or graphical abstract from scratch; use `nnscholar4-2-image-schematic`;
- manuscript tables; use `nnscholar4-4-table-formatting`;
- destructive image editing of raw experimental images.

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar4-1-data-figure`: generated plots, figure reports, plot manifests.
2. `nnscholar4-2-image-schematic`: generated schematics, Image2 prompts, caption files.
3. `nnscholar2-3-paper-architecture`: figure slots, Results story, panel order.
4. `nnscholar2-4-flowchart-design`: route diagrams and figure logic.
5. `nnscholar3-1-experiment-validation-plan`: experiment steps and readouts.
6. User-provided subfigures, experimental images, sketches, or figure drafts.

When files are not specified, search `figures/`, `images/`, `outputs/`, `results/`, `references/`, and `docs/` for `.svg`, `.pdf`, `.png`, `.tif`, `.tiff`, `.jpg`, `.jpeg`, figure reports, and layout manifests. Ask the user to choose only if multiple plausible figure bundles match.

## Interactive Micro-Rounds

Ask at most 1-3 questions per round.

### Round 0: Assembly Intake

Return a short card:

```text
Detected figure slot:
Detected discipline / study family:
Available panels:
Likely figure story:
Missing assets or metadata:
Next questions:
```

If the request is vague, ask:

1. Is this Figure 1, a main result figure, a validation figure, a supplementary figure, or a graphical abstract?
2. Which files should be used as panels, or should I search the workspace for recent 4.1/4.2 outputs?
3. What target format is needed: single-column, double-column, full-page, journal/conference-specific, or custom size?

### Round 1: Panel Inventory

Create a panel inventory table:

```text
Panel | File | Type | Scientific role | Must preserve | Issues
A | ... | schematic/data plot/microscopy/gel/table-like | ... | scale bar/color/legend/aspect | ...
```

Always check:

- whether a panel is vector (`svg`, `pdf`, `eps`) or raster (`png`, `jpg`, `tif`);
- whether scale bars, colorbars, legends, or axis labels must remain visible;
- whether panels need consistent color/labels with previous figures;
- whether any experimental image requires non-destructive handling or annotation restrictions.

### Round 2: Figure Story and Layout Options

Use `references/assembly-router.md` and `references/discipline-panel-patterns.md` when choosing layout.

Produce 2-3 layout options:

- `A. Balanced grid`: panels have similar visual weight.
- `B. Hero + evidence`: one large schematic/main result plus smaller evidence panels.
- `C. Narrative route`: left-to-right or top-to-bottom sequence.

For each option include:

- panel order;
- canvas orientation and approximate size;
- strengths;
- risks;
- recommended option.

### Round 3: Locked Layout Specification

Before assembling, lock:

```text
Figure ID:
Canvas size:
Columns / rows:
Panel order:
Panel labels:
Panel title policy:
Gutter / margins:
Font:
Output formats:
Legend plan:
```

If the user asks for direct assembly and panel files are sufficient, proceed without another confirmation.

### Round 4: Assemble Figure

Prefer deterministic assembly using `scripts/assemble_figure.py`.

Recommended workflow:

1. Create a `layout_manifest.json` listing panels and layout options.
2. Run `scripts/assemble_figure.py` to generate a self-contained SVG.
3. Export PDF/PNG when dependencies support it.
4. Inspect output dimensions and file existence.
5. Write `figure_legend.md`.
6. Add a downstream handoff for `nnscholar4-5-manuscript-drafting`: figure slot, Results paragraph cue, panel-by-panel claim map, and any Methods details that must be mentioned.

The script is intentionally conservative: it embeds panels into a vector SVG wrapper, adds labels/titles, and preserves aspect ratio. For highly custom layouts, write a custom SVG or Python script but keep a manifest.

### Round 5: Figure Legend and Quality Audit

Always provide:

- figure title;
- panel-by-panel legend;
- source-panel map;
- abbreviation definitions;
- scale bar, colorbar, axis, unit, and transformation notes for each relevant panel;
- statistical annotation note for panels containing tests, models, confidence intervals, or p values;
- cross-panel consistency note for fonts, colors, labels, and terminology;
- quality audit;
- journal-readiness checklist;
- next revision suggestions.

Use `references/figure-assembly-template.md` for a full report.

## Guardrails

- Never overwrite raw images or original subfigures.
- Do not crop microscopy/gel/histology/SEM/TEM panels unless the user explicitly approves.
- Do not remove scale bars, colorbars, legends, axes, or sample labels unless replacing them with correct equivalents.
- Do not upscale low-resolution raster panels and claim they are publication quality.
- Do not flatten vector panels unless necessary for export.
- Use consistent panel labels and avoid tiny text.
- Keep figure legend separate from the image unless the target format requires embedded captions.
- For clinical figures, separate workflow, model performance, calibration, and clinical utility panels.
- For biomedical figures, separate representative images from quantification panels.
- For AI figures, separate architecture, benchmark, ablation, and error analysis.
- For materials figures, separate synthesis schematic, morphology, characterization, performance, and stability.

## Output Rules

Match the user's language. Keep labels, endpoint names, model names, datasets, journals, and software names in their original form when clearer.

Save generated assets using ASCII slugs:

```text
figures/assembly-YYYY-MM-DD-short-topic/
  assembled_figure.svg
  assembled_figure.pdf
  assembled_figure.png
  layout_manifest.json
  figure_legend.md
  assembly_report.md
```

If the workspace lacks a `figures/` folder, create it only when generating files.

For downstream manuscript drafting, make sure `assembly_report.md` includes:

```text
4.5 handoff:
Figure placement:
Results paragraph cue:
Panel-by-panel claim map:
Methods details to mention:
Caption-ready title:
Caption-ready legend:
Limitations sentence:
```
