---
name: nnscholar5-2-submission-finalization
description: Use when NNScholar needs to revise, format, finalize, audit, or package a manuscript for a specific journal, conference, preprint server, thesis submission, or publisher after target recommendation. Handles author guidelines, formatting compliance, title page, blinded manuscript, highlights, graphical abstract notes, supplementary files, ethics/funding/COI/data-code availability statements, checklist completion, revision-before-submission, and final submission package quality control across disciplines.
---

# NNScholar 5.2 Submission Finalization

This skill converts a polished manuscript into a target-specific submission package. It checks author guidelines, revises required components, and creates a finalization checklist.

Version: `0.2.0`. Stage: `submission / finalization`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id and folder name as `nnscholar5-2-submission-finalization` / `/nnscholar5-2-submission-finalization`.
- Keep the title format as `NNScholar 5.2 Submission Finalization`.
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

Do not merely say "looks good". Audit the manuscript against the target venue requirements and produce a concrete finalization package. If official guidelines are needed and not provided, ask for them or verify from official pages before final compliance claims.

Never fabricate ethics approval numbers, clinical trial registrations, ORCID IDs, funder IDs, author contributions, conflicts of interest, data availability, code availability, or supplementary files.

## Boundary

Use this skill for:

- target-venue final checks;
- formatting and compliance audit;
- title page and blinded manuscript preparation;
- highlights, abstract, keywords, graphical abstract notes;
- statements: ethics, funding, COI, author contributions, data/code availability;
- supplementary file checklist;
- revised final package after 5.1 recommendation.

Do not use this skill for:

- choosing venues; use `nnscholar5-1-journal-conference-recommendation`;
- portal navigation; use `nnscholar5-3-submission-portal-workflow`;
- cover letter; use `nnscholar5-4-cover-letter`;
- reviewer responses; use `nnscholar5-5-reviewer-response`.

## Upstream Priority

1. `nnscholar5-1-journal-conference-recommendation`: selected target, revision priorities.
2. Official author guidelines, conference CFP, template, or user-provided requirements.
3. `nnscholar4-3-paper-writing`: manuscript draft, polished manuscript, consistency audit, and missing-evidence checklist.
4. `nnscholar4-1-paper-figure`: figure outputs, graphical abstract notes, captions, and export notes.
5. `nnscholar4-2-paper-table`: table outputs, titles, notes, and format notes.
6. User-provided title page, author info, supplementary materials, statements, and files.

## Workflow

### Step 1: Finalization Intake

Return:

```text
Target venue:
Article type:
Submission type:
Available files:
Guidelines source:
Missing package components:
High-risk compliance items:
Next questions:
```

Ask:

1. What is the exact target journal/conference and article type?
2. Do you have official author guidelines or a template?
3. Should the manuscript be blinded, non-blinded, or both?

### Step 2: Guideline Checklist

Use `references/finalization-checklist.md` to audit:

- title length and title page;
- abstract format and word count;
- keywords/highlights;
- manuscript structure;
- figure/table count and format;
- references;
- supplementary files;
- statements;
- anonymity/double-blind requirements;
- reporting checklist.

For Nature-family, Cell, Science, CNS-style, flagship society, or other high-impact targets, also read `../../references/high-impact-paper-guardrails.md` and audit:

- terminology ledger consistency across title, abstract, main text, figures, tables, and supplement;
- display-item count, main-text vs supplementary placement, and whether every central figure/table has a source-data route;
- Data Availability, Code Availability, repository identifier, accession/DOI, license, README/metadata, and restricted-data access procedure;
- citation/source verification for central claims, factual venue statements, and reused datasets;
- reviewer-style risks across technical soundness, originality/significance, and interdisciplinary readability.

### Step 3: Revision and Package Plan

Produce:

```text
Required edits:
Optional improvements:
Files to create:
Files to verify:
Author-provided facts required:
Submission blockers:
```

Block final approval when a central dataset lacks a durable access route, a DOI/accession/repository identifier is unresolved, restricted data lack an access procedure, source data are missing for central figures/tables, or the data/code availability statements conflict with the actual files.

### Step 4: Finalization Outputs

When generating files, use `scripts/create_finalization_package.py`. Use `references/finalization-output-template.md` for the report.

## Discipline Guardrails

- Clinical medicine: require ethics, consent/waiver, registry when relevant, reporting guideline, data sharing, and patient privacy checks.
- AI/data science: check code/data availability, reproducibility, double-blind policy, supplementary appendix, and artifact checklist.
- Materials/chemistry: check graphical abstract, highlights, experimental details, CIF/supporting information, and characterization files.
- Education/psychology: check ethics, consent, instruments, preregistration if relevant, and scale permissions.
- Economics/social science: check data/code availability, appendices, replication files, and model tables.
- Humanities: check citation style, transliteration, source permissions, images, archives, and notes format.

## Supervisor Guardrail Integration

For AI/data-science, database, systems, ML, NLP, benchmark/evaluation, or
technical CS submissions, read
`../../references/supervisor-research-guardrails.md` and apply the
Pre-Submission Review Gate before final package approval. Add CRITICAL and
MAJOR findings to `submission blockers` or `required edits`, especially broken
paper logic, missing baselines, unsupported benchmark claims, figure-quality
failures, LaTeX/formatting issues, artifact checklist gaps, and repeated
AI-tone wording.

For AI/ML/LLM/systems venues, also read
`../../references/ai-research-engineering-guardrails.md`. Apply the Citation
and Venue Gate, Evaluation Harness Gate, ARA Provenance Gate, and Rigor Review
Gate as applicable. Final approval requires verified venue rules, reproducible
benchmark settings, code/data/artifact statement status, and explicit
placeholders for any unverified citation or compliance item.

## Output Rules

Default package:

```text
submission/finalization-YYYY-MM-DD-short-topic/
  finalization_checklist.md
  required_edits.md
  submission_file_manifest.md
  author_queries.md
  compliance_report.md
  source_manifest.json
```

