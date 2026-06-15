---
name: nnscholar4-4-table-formatting
description: Use when NNScholar needs to format, rewrite, or export scientific manuscript tables from pasted tables, CSV/Excel/TSV/JSON/Markdown tables, statistical result tables, baseline tables, model performance tables, literature comparison tables, variable definition tables, or journal/conference-specific tables. Produces Word .docx three-line tables, Markdown/HTML table versions, table titles, column headers, table notes, abbreviations, statistical footnotes, and quality checks. Works across clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, and engineering.
---

# NNScholar 4.4 Table Formatting

This skill turns research results or rough tables into publication-ready manuscript tables. It focuses on table structure, table title, column headers, table notes, abbreviations, statistical footnotes, and Word-ready three-line table output.

Version: `0.2.0`. Stage: `paper output / table formatting`. Legacy workflow alias: `$nnscholar4-4-table-formatting`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar4-4-table-formatting` / `/nnscholar4-4-table-formatting`.
- Keep the title format as `NNScholar 4.4 Table Formatting`.
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

Do not only convert data into a visual table. First identify what the table must communicate, which discipline/style it belongs to, whether rows/columns are correctly arranged, and what notes/abbreviations/statistical explanations are needed. Then produce the formatted table and all manuscript text around it.

Every table output must include:

- table number placeholder or ID;
- table title/caption;
- cleaned column headers;
- formatted body;
- table notes, including abbreviation definitions and statistical test/model notes when relevant;
- source/data caveat if the table was derived from user data;
- Word `.docx` output when requested or when the user says Word/涓夌嚎琛?

## Boundary

Use this skill for:

- Word three-line tables;
- baseline characteristic tables;
- statistical regression/model result tables;
- AI benchmark and ablation tables;
- materials/chemistry composition/property/performance tables;
- education/psychology scale/intervention result tables;
- economics/social-science regression/robustness tables;
- humanities corpus/source/comparison tables;
- literature comparison and evidence-summary tables;
- variable definition and data dictionary tables.

Do not use this skill for:

- data-driven figures; use `nnscholar4-1-data-figure`;
- schematic images; use `nnscholar4-2-image-schematic`;
- multi-panel figure assembly; use `nnscholar4-3-figure-assembly`;
- full manuscript drafting; use `nnscholar4-5-manuscript-drafting`.

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar2-3-paper-architecture`: table slots and Results story.
2. `nnscholar3-1-experiment-validation-plan`: variables, endpoints, readouts, comparison groups.
3. `nnscholar4-1-data-figure`: data transformations and plotted result context.
4. `nnscholar4-3-figure-assembly`: figure legend and panel map for companion tables.
5. `nnscholar1-4-domain-expert-knowledge-base`: abbreviations and field-specific reporting norms.
6. User-provided table, data file, statistical output, or draft manuscript.

When files are not specified, search `tables/`, `results/`, `data/`, `outputs/`, `references/`, and `docs/` for `.csv`, `.xlsx`, `.tsv`, `.json`, `.md`, `.docx`, result tables, model outputs, and table drafts.

## Interactive Micro-Rounds

Ask at most 1-3 questions per round.

### Round 0: Table Intake

Return a short card:

```text
Detected table purpose:
Detected discipline / style:
Detected source:
Likely table type:
Missing information:
Next questions:
```

If the request is vague, ask:

1. What table is this: baseline, results, model performance, regression, literature comparison, variable definition, or other?
2. What source should be used: pasted table, CSV/Excel, statistical output, or existing Word table?
3. What output do you need: Word 涓夌嚎琛? Markdown, HTML, journal-specific format, or all?

Use `references/table-router.md` for table-type selection and `references/discipline-table-patterns.md` for discipline-specific norms.

### Round 1: Structure and Header Check

Inspect or request:

- row meaning and column meaning;
- grouping variables;
- units and measurement windows;
- sample sizes and denominators;
- uncertainty format: SD, SE, CI, IQR, p value, adjusted p value;
- model/test details;
- abbreviations;
- target journal/conference/table style.

Never silently change the meaning of rows/columns. If a table appears transposed or ambiguous, ask before reformatting.

### Round 2: Table Text Contract

Before final output, produce or lock:

```text
Table ID:
Title:
Population/data source:
Primary comparison or purpose:
Column header policy:
Decimal/significance policy:
Required notes:
Abbreviations:
Output formats:
```

If the user asks for direct output and the source is sufficient, proceed.

### Round 3: Generate Table

Prefer deterministic output using `scripts/table_to_docx.py`.

Recommended workflow:

1. Save or identify the source table.
2. Create `table_manifest.json` when metadata are complex.
3. Run `scripts/table_to_docx.py` for Word/Markdown/HTML.
4. Inspect generated file existence and output paths.
5. Write `table_report.md` with table title, notes, and quality audit.
6. Add a downstream handoff for `nnscholar4-5-manuscript-drafting`: table slot, Results insertion cue, summary sentence, Methods/statistics sentence, and notes that must appear in the manuscript.

### Round 4: Table Quality Audit

Always check:

- whether row/column headers are self-explanatory;
- whether sample sizes and denominators are visible;
- whether units and time windows are present;
- whether statistical tests/models are described;
- whether abbreviations are defined;
- whether precision/decimal places are consistent;
- whether the table supports the manuscript claim without overstatement.

Use `references/table-output-template.md` for a full report.

## Discipline Guardrails

- Clinical medicine: include cohort, n, endpoint windows, test/model adjustment status, missing data note, and abbreviation definitions.
- Basic biomedicine: separate biological vs technical replicates; state normalization, control group, and n.
- AI/data science: include dataset, metric direction, split, seeds/folds, baseline, and whether values are mean/SD or CI.
- Materials/chemistry: include composition, synthesis/test condition, units, batch/repetition count, and instrument conditions.
- Education/psychology: include scale range, time point, intervention/control, attrition/missingness, and reliability when relevant.
- Economics/social science: include model specification, fixed effects, standard error clustering, sample size, and robustness notes.
- Humanities: include corpus/source selection, period, coding rules, and interpretive limits.
- Engineering: include system/workload, operating condition, hardware/software environment, units, and repetitions.

## Output Rules

Match the user's language. Keep variable names, endpoints, models, datasets, journal names, and abbreviations in their original form when clearer.

Save generated assets using ASCII slugs:

```text
tables/table-YYYY-MM-DD-short-topic/
  table.docx
  table.md
  table.html
  table_manifest.json
  table_report.md
```

If the workspace lacks a `tables/` folder, create it only when generating files.

For downstream manuscript drafting, make sure `table_report.md` includes:

```text
4.5 handoff:
Table placement:
Results insertion cue:
Summary sentence:
Methods/statistics sentence:
Caption-ready table title:
Required table notes:
Limitations sentence:
```
