---
name: nnscholar5-4-cover-letter
description: Use when NNScholar needs to draft, revise, polish, adapt, or audit a journal submission cover letter, conference submission note, editor letter, transfer letter, resubmission letter, presubmission inquiry, or publication declaration. Uses manuscript, target venue, contribution, ethics/COI/data statements, and venue fit to produce multidisciplinary cover letters with revision notes and compliance checks.
---

# NNScholar 5.4 Cover Letter

This skill writes and revises cover letters and editor-facing submission letters. It emphasizes fit, contribution, declarations, and professional tone.

Version: `0.2.0`. Stage: `submission / cover letter`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id and folder name as `nnscholar5-4-cover-letter` / `/nnscholar5-4-cover-letter`.
- Keep the title format as `NNScholar 5.4 Cover Letter`.
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

The cover letter must be specific to the manuscript and target venue. Do not use generic flattery. Do not invent novelty, exclusivity, ethics approval, conflicts, funding, data availability, or prior communications.

## Boundary

Use this skill for:

- journal cover letter;
- editor letter;
- transfer/resubmission cover letter;
- presubmission inquiry;
- short conference submission note;
- cover letter polishing and compliance audit.

Do not use this skill for:

- venue recommendation; use 5.1;
- final formatting package; use 5.2;
- portal workflow; use 5.3;
- point-by-point reviewer response; use 5.5.

## Upstream Priority

1. `nnscholar5-1-journal-conference-recommendation`: venue fit rationale.
2. `nnscholar5-2-submission-finalization`: final title, abstract, statements, article type.
3. `nnscholar4-3-paper-writing`: final polished manuscript, core story, and claim map.
5. User-provided target editor, prior inquiry, transfer history, declaration requirements.

## Workflow

### Step 1: Cover Letter Intake

Return:

```text
Target venue:
Article type:
Core contribution:
Fit rationale:
Required declarations:
Missing author facts:
Suggested letter type:
Next questions:
```

Ask:

1. Is this a first submission, transfer, resubmission, or presubmission inquiry?
2. Do you have required declarations: originality, no concurrent submission, ethics, COI, funding, data availability?
3. Should the tone be concise standard, strong editorial pitch, or conservative formal?

### Step 2: Letter Contract

Lock:

```text
Recipient:
Manuscript title:
Article type:
Core contribution:
Why this venue:
High-impact pitch:
Declarations:
Corresponding author:
Do-not-say items:
```

### Step 3: Draft and Revise

Use `references/cover-letter-template.md`. Always provide:

- full cover letter;
- short version;
- editorial pitch bullets;
- missing facts/author queries;
- compliance audit.

For high-impact targets, read `../../references/high-impact-paper-guardrails.md` and make the pitch concrete: what was found, what is new, why it matters beyond the immediate specialty, what evidence supports it, and where the evidence boundary sits. Avoid generic broad-interest language and do not introduce novelty, data, or implications that are not present in the manuscript.

## Discipline Guardrails

- Clinical medicine: emphasize patient/clinical relevance without overclaiming; include ethics/consent/registration placeholders when required.
- AI/data science: emphasize method contribution, evaluation, reproducibility, and fit to audience.
- Materials/chemistry: emphasize material novelty, characterization, performance, and mechanism boundary.
- Education/psychology/social science: emphasize theoretical/practical contribution, ethics, and measurement rigor.
- Humanities: emphasize argument, sources/corpus, and contribution to the journal's conversation.

## Output Rules

Default package:

```text
submission/cover-letter-YYYY-MM-DD-short-topic/
  cover_letter.md
  cover_letter_short.md
  editorial_pitch.md
  declaration_checklist.md
  author_queries.md
  source_manifest.json
```

