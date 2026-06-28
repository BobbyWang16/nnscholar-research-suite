---
name: nnscholar5-3-submission-portal-workflow
description: Use when NNScholar needs to prepare, guide, checklist, or assist a journal/conference official submission portal workflow, including ScholarOne, Editorial Manager, Elsevier/Springer/Wiley/Taylor & Francis portals, OpenReview, CMT, EasyChair, HotCRP, publisher upload systems, manuscript metadata forms, suggested reviewers, file uploads, declarations, and final human confirmation. Produces portal step plans, field-answer drafts, upload manifest, compliance checks, and safety-gated submission instructions across disciplines.
---

# NNScholar 5.3 Submission Portal Workflow

This skill helps the user complete an official submission portal workflow. It is a guided assistant, not an autonomous submitter.

Version: `0.2.0`. Stage: `submission / portal workflow`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id and folder name as `nnscholar5-3-submission-portal-workflow` / `/nnscholar5-3-submission-portal-workflow`.
- Keep the title format as `NNScholar 5.3 Submission Portal Workflow`.
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

Never submit, certify, sign, pay, approve copyright, or confirm author declarations without explicit human confirmation. Do not store passwords. Do not bypass portal rules.

The safe workflow is:

1. understand the portal and target venue;
2. prepare all field answers and file manifest;
3. guide or assist form filling;
4. stop before final submit;
5. produce a final human confirmation checklist.

## Boundary

Use this skill for:

- portal step-by-step preparation;
- manuscript metadata forms;
- author details checklist;
- suggested/opposed reviewers;
- file upload manifest;
- declaration and ethics form preparation;
- conference submission forms;
- final pre-submit checklist.

Do not use this skill for:

- venue selection; use 5.1;
- final manuscript formatting; use 5.2;
- cover letter; use 5.4;
- reviewer response; use 5.5.

## Upstream Priority

1. `nnscholar5-2-submission-finalization`: final file manifest and compliance report.
2. `nnscholar5-4-cover-letter`: cover letter and declarations.
3. Target portal instructions or screenshots.
4. User-provided account/session state and files.
5. Manuscript metadata from `nnscholar4-3-paper-writing`.

## Workflow

### Step 1: Portal Intake

Return:

```text
Target venue:
Portal system:
Submission type:
Available final files:
Required metadata:
Human-only actions:
Missing information:
Next questions:
```

Ask:

1. Which portal/system is used: ScholarOne, Editorial Manager, OpenReview, CMT, EasyChair, HotCRP, or other?
2. Do you want a checklist only, or browser-assisted navigation?
3. Do you have final files from 5.2 and cover letter from 5.4?

### Step 2: Submission Fields

Use `references/portal-field-template.md` to prepare:

- title, running title;
- abstract;
- keywords;
- article type;
- classifications;
- authors and affiliations;
- corresponding author;
- funding;
- ethics/COI/data availability;
- suggested reviewers;
- file upload roles;
- comments to editor.

### Step 3: Safety Gate

Human-only actions:

- login and credentials;
- copyright/license acceptance;
- publication fee approval;
- conflict of interest certification;
- author contribution certification;
- final submit button;
- withdrawal/resubmission confirmation.

### Step 4: Portal Package

Use `scripts/create_portal_package.py` when generating files.

## Discipline Guardrails

- Medical submissions: clinical trial registration, ethics, patient consent, data privacy, reporting checklist, and suggested reviewer conflicts.
- AI conferences: anonymity, supplementary material policy, code/data link policy, reviewer conflict lists, subject areas, rebuttal calendar.
- Materials/chemistry: graphical abstract, highlights, supporting information, compound/material data, safety statements.
- Social science/education/psychology: ethics, preregistration, data access, instruments, consent, replication files.
- Humanities: image permissions, archive permissions, translation rights, copyright.

## Output Rules

Default package:

```text
submission/portal-YYYY-MM-DD-short-topic/
  portal_step_plan.md
  portal_field_answers.md
  upload_file_manifest.md
  human_only_actions.md
  final_confirmation_checklist.md
  source_manifest.json
```

