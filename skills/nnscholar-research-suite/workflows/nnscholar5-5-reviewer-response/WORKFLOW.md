---
name: nnscholar5-5-reviewer-response
description: Use when NNScholar needs to analyze, classify, draft, revise, polish, or audit responses to reviewers, editor decision letters, major revision, minor revision, reject-and-resubmit, conference rebuttal, OpenReview rebuttal, revision summary, point-by-point response, changed manuscript checklist, or reviewer-aware manuscript revisions across disciplines. Produces comment taxonomy, response strategy, manuscript change plan, point-by-point replies, tone audit, unresolved-risk notes, and revision package.
---

# NNScholar 5.5 Reviewer Response

This skill helps respond to reviewer and editor comments with a respectful, evidence-based, traceable revision strategy.

Version: `0.2.0`. Stage: `submission / reviewer response`. Legacy workflow alias: `$nnscholar5-5-reviewer-response`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar5-5-reviewer-response` / `/nnscholar5-5-reviewer-response`.
- Keep the title format as `NNScholar 5.5 Reviewer Response`.
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

Do not argue emotionally. Do not promise experiments, analyses, citations, or changes that were not done. Every response should state what was changed, where it was changed, and what evidence supports the response. If a request cannot be met, explain politely and scientifically.

## Boundary

Use this skill for:

- editor decision letter analysis;
- reviewer comment classification;
- major/minor revision response;
- conference rebuttal;
- OpenReview/CMT response;
- point-by-point response;
- revised manuscript change plan;
- tone and risk audit.

Do not use this skill for:

- first cover letter; use 5.4;
- initial submission portal; use 5.3;
- formatting final package only; use 5.2.

## Upstream Priority

1. Reviewer/editor comments and decision letter.
2. Current manuscript and revised manuscript if available.
3. `nnscholar4-6-manuscript-polishing`: polished draft and risky claims.
4. `nnscholar4-5-manuscript-drafting`: claim map and missing evidence checklist.
5. Figures/tables/statistics added in response to review.
6. User strategy: accept, rebut, partially accept, add analysis, defer to limitation, or appeal.

## Workflow

### Step 1: Review Intake

Return:

```text
Decision type:
Review format:
Number of reviewers:
Main themes:
Required new work:
High-risk comments:
Missing materials:
Next questions:
```

Ask:

1. Do you want a response strategy first or a full point-by-point draft?
2. Do you have a revised manuscript or only the original manuscript?
3. Which requests have already been addressed with new analysis/experiments/text changes?

### Step 2: Comment Taxonomy

Use `references/reviewer-comment-taxonomy.md` to classify each comment:

- mandatory fix;
- clarification;
- new analysis/experiment;
- citation/literature;
- formatting/reporting;
- misunderstanding;
- impossible/unreasonable request;
- editor-only issue.

### Step 3: Response Strategy

For each comment:

```text
Reviewer/comment ID:
Issue:
Strategy:
Manuscript change:
Evidence/source:
Response tone:
Risk:
Author action needed:
```

### Step 4: Point-by-Point Response

Default structure:

```text
Comment:
Response:
Changes made:
Location in manuscript:
```

For conference rebuttals, produce concise, high-density replies within word limits.

### Step 5: Audit

Always audit:

- tone and politeness;
- unsupported promises;
- whether every comment is answered;
- whether claimed changes match manuscript locations;
- whether new claims require new evidence;
- whether limitations are appropriately added;
- whether editor-level issues are addressed.

## Discipline Guardrails

- Clinical medicine: handle requests for subgroup, sensitivity, validation, ethics, missing data, and clinical relevance conservatively.
- Basic biomedicine: handle mechanistic claims, replicate concerns, controls, and image/quantification issues carefully.
- AI/data science: handle baseline, ablation, statistical significance, reproducibility, dataset split, code release, and compute issues.
- Materials/chemistry: handle characterization, performance comparison, stability, mechanism, and reproducibility concerns.
- Education/psychology: handle sample, measurement, reliability, ethics, intervention fidelity, and effect size concerns.
- Economics/social science: handle identification, endogeneity, fixed effects, robustness, standard errors, and external validity.
- Humanities: handle interpretation, source coverage, theoretical framing, and counterargument concerns.

## Output Rules

Default package:

```text
submission/reviewer-response-YYYY-MM-DD-short-topic/
  reviewer_comment_matrix.md
  response_strategy.md
  point_by_point_response.md
  revision_summary_table.md
  manuscript_change_checklist.md
  tone_and_risk_audit.md
  author_queries.md
  source_manifest.json
```

