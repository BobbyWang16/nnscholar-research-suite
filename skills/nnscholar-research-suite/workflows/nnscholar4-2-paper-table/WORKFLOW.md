---
name: nnscholar4-2-paper-table
description: Use when NNScholar needs paper table production: manuscript tables, baseline tables, statistical/regression tables, AI benchmark and ablation tables, result tables, literature comparison tables, variable definition tables, data dictionaries, Word three-line tables, Markdown/HTML/LaTeX tables, table titles, notes, abbreviations, statistical footnotes, and table quality audits while coordinating with 4.1 figures and 4.3 writing.
---

# NNScholar 4.2 Paper Table Production

This skill turns research data, results, statistical outputs, and rough tables into manuscript-ready tables. It is the table authority for NNScholar Stage 4.

Version: `0.3.0`. Stage: `paper output / tables`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the canonical workflow id as `nnscholar4-2-paper-table` / `/nnscholar4-2-paper-table`.
- Keep the title format as `NNScholar 4.2 Paper Table Production`.
- Name generated folders and files with English ASCII kebab-case slugs.

### Input and Language Policy

- Accept free-form requests, pasted tables, CSV/XLSX/TSV/JSON/Markdown, statistical outputs, benchmark results, literature matrices, Word/DOCX tables, upstream NNScholar outputs, reviewer comments, and venue instructions.
- For table planning, audits, and author-facing notes: output in the user's input language unless requested otherwise.
- For manuscript-facing table titles, notes, callouts, and Methods/Results sentences: default to polished academic English unless the user or venue requests another language.
- Preserve identifiers in their standard form: variables, endpoints, metrics, datasets, model names, scales, software, p values, confidence intervals, and citation keys.
- Do not fabricate sample sizes, p values, model outputs, table values, citations, or statistical tests.

## Core Rule

Do not only convert a rough table into a prettier table. First identify what the table must communicate, the discipline/style, row/column meaning, comparison logic, statistical notes, abbreviations, and whether a figure would communicate the result better. Then produce the formatted table and manuscript-ready text around it.

One table should support one main claim or one coherent evidence block.

## Boundary

Use this skill for:

- baseline characteristic tables;
- descriptive statistics, variable definitions, and data dictionaries;
- regression/model result tables;
- AI benchmark, ablation, leaderboard, and metric tables;
- clinical, biomedical, materials, education/psychology, economics/social science, humanities, and engineering result tables;
- literature comparison and evidence-summary tables;
- Word `.docx`, Markdown, HTML, and LaTeX/booktabs-style outputs;
- table titles, notes, abbreviations, statistical footnotes, and quality audits.

Do not use this skill for:

- data visualization or graphical figures; use `nnscholar4-1-paper-figure`;
- manuscript drafting/polishing; use `nnscholar4-3-paper-writing`;
- new statistical modeling or analysis that is not already specified; route to relevant analysis skill or 2.2/3.1 first.

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar2-3-paper-architecture`: table slots, Results story, main/supplement placement.
2. `nnscholar3-1-experiment-validation-plan`: result summary, raw result paths, claim-evidence map, audit status.
3. `nnscholar2-2-ars-plan`: variables, endpoints, readouts, comparison groups, validation route, quality gates.
4. `nnscholar4-1-paper-figure`: companion figure reports, plotted data context, panel maps.
5. `nnscholar1-4-domain-expert-knowledge-base`: abbreviations, variable semantics, domain constraints, field-specific reporting norms, expected reviewer challenges, and citation-backed interpretation boundaries.
6. User-provided table, data file, statistical output, manuscript, or venue instruction.

When files are not specified, search `tables/`, `results/`, `data/`, `outputs/`, `research-runs/`, `references/`, `docs/`, and `manuscripts/`.

## Workflow

### Step 1: Table Intake

Return a compact card:

```text
Detected table purpose:
Detected discipline / style:
Detected source:
Likely table type:
Target output:
Missing information:
Next questions:
```

Ask at most 1-3 questions if needed.

### Step 2: Structure and Meaning Check

Inspect or request:

- row meaning and column meaning;
- grouping variables;
- units and measurement windows;
- sample sizes and denominators;
- uncertainty format: SD, SE, CI, IQR, p value, adjusted p value;
- model/test details;
- abbreviations;
- target journal/conference/table style.

Never silently transpose, aggregate, round, or relabel values in a way that changes meaning.

### Step 3: Table Contract

Lock:

```text
Table ID:
Title:
Population/data source:
Primary comparison or purpose:
Row policy:
Column header policy:
Decimal/significance policy:
Required notes:
Abbreviations:
Output formats:
```

### Step 4: Generate Table

Prefer deterministic output:

- Use `scripts/table_to_docx.py` for Word/Markdown/HTML when it fits.
- Use `spreadsheets:Spreadsheets` when spreadsheet parsing, formula inspection, or workbook editing is required.
- Use `aer-tables-figures` conventions for economics/regression tables: booktabs, no vertical rules, specification rows, standard error notes, and one claim per exhibit.
- Use `statistical-analysis` when the table requires explicit statistical reporting choices.
- Use `ml-paper-writing` table conventions for AI/ML benchmark tables: metric direction, best-value bolding, seeds/variance, and comparable settings.

### Step 5: Table Notes and Audit

Always provide:

- table title;
- cleaned column headers;
- formatted table body;
- table notes;
- abbreviation definitions;
- statistical/model notes;
- source/data caveat;
- what the table supports and does not prove;
- downstream writing handoff.

For high-impact or Nature/CNS-style tables, read
`../../references/high-impact-paper-guardrails.md` and enforce:

- one table, one coherent evidence block;
- self-contained title and notes;
- explicit denominators, sample sizes, units, measurement windows, uncertainty,
  and model/test details;
- source-data or dataset mapping when table values support central claims;
- clear decision on main-text versus supplementary placement.

### Step 6: Expert Knowledge Reference

If a 1.4 expert knowledge base exists, consult it before finalizing table
structure and notes. Use it to verify:

- field-specific variable names, definitions, abbreviations, units, and
  measurement windows;
- whether row/column groupings match accepted domain distinctions;
- reporting expectations for denominators, uncertainty, missingness,
  replicates, model settings, or corpus selection;
- reviewer-risk notes that should appear as table notes or limitations.

If the expert KB indicates that a table could overstate the evidence, add a
source-backed caveat and flag the table as provisional.

### Step 7: Data Availability Linkage

When the table supports a central claim, record which dataset, source-data file,
or supplementary table must be available later in 5.2. If the access route is
unknown, add `needs verification` to the table report.

## Discipline Guardrails

- Clinical medicine: include cohort, n, denominator, endpoint windows, adjustment status, missing data note, and abbreviation definitions.
- Basic biomedicine: separate biological vs technical replicates; state normalization, control group, and n.
- AI/data science: include dataset, metric direction, split, seeds/folds, baseline, comparable settings, and whether values are mean/SD or CI.
- Materials/chemistry: include composition, synthesis/test condition, units, batch/repetition count, and instrument conditions.
- Education/psychology: include scale range, time point, intervention/control, attrition/missingness, and reliability when relevant.
- Economics/social science: include model specification, fixed effects, standard error clustering, observations, R-squared/fit statistics, and robustness notes.
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
  table.tex
  table_manifest.json
  table_report.md
  source_manifest.json
```

For downstream manuscript writing, include:

```text
4.3 handoff:
Table placement:
Results insertion cue:
Summary sentence:
Methods/statistics sentence:
Caption-ready table title:
Required table notes:
Limitations sentence:
```

## Non-goals

Do not fabricate numbers, tests, p values, denominators, or citations. Do not hide sample size or uncertainty. Do not use significance stars without a stated convention. Do not make a table wider than a manuscript page without recommending a split, supplement move, or figure alternative.
