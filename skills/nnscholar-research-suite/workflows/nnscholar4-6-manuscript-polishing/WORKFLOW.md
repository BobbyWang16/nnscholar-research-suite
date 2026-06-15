---
name: nnscholar4-6-manuscript-polishing
description: Use when NNScholar needs to polish, revise, refine, edit, or improve an existing manuscript, manuscript section, abstract, title, response-ready draft, Word/DOCX draft, Markdown draft, reviewer-revision draft, or NNScholar 4.5 manuscript draft. Supports light language polishing, logic polishing, deep structural revision, journal/conference style adaptation, reviewer-comment-aware revision, tracked-change-style change summaries, author queries, risky-claim audits, and consistency checks across clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, and engineering.
---

# NNScholar 4.6 Manuscript Polishing

This skill improves an existing academic manuscript without changing its scientific meaning. It is for polishing, revision, and consistency checks after a draft exists. It can work from NNScholar 4.5 outputs, pasted text, Markdown files, Word/DOCX drafts, reviewer comments, journal instructions, or author notes.

Version: `0.2.0`. Stage: `paper output / manuscript polishing`. Legacy workflow alias: `$nnscholar4-6-manuscript-polishing`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar4-6-manuscript-polishing` / `/nnscholar4-6-manuscript-polishing`.
- Keep the title format as `NNScholar 4.6 Manuscript Polishing`.
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

Do not make the manuscript sound better by changing the science. Preserve factual meaning, numeric values, statistical results, methods, citations, figure/table claims, ethics statements, and uncertainty level unless the user explicitly asks to change them and provides evidence.

Before editing, lock the polishing scope:

- `light`: grammar, word choice, concision, academic tone;
- `logic`: paragraph flow, transitions, redundancy, argument clarity;
- `deep`: section restructuring, claim hierarchy, story flow;
- `venue`: target journal/conference style adaptation;
- `reviewer-aware`: revise according to reviewer comments and author rebuttal strategy;
- `bilingual`: Chinese-English translation polishing or English academic rewrite with source meaning preserved.

For Results and Methods, default to conservative editing. If a sentence contains numbers, p values, model names, sample size, endpoint definitions, eligibility criteria, or instrument conditions, preserve the technical content exactly unless flagging a problem.

## Boundary

Use this skill for:

- polishing an existing manuscript or section;
- improving clarity, style, flow, and academic tone;
- revising abstracts, titles, introductions, methods, results, discussions, limitations, cover letters, and response-ready text;
- adapting drafts to target journal/conference tone;
- checking consistency after 4.5 drafting;
- polishing Word/DOCX or Markdown drafts;
- producing change summaries, author queries, risky-claim audits, and consistency checks.

Do not use this skill for:

- generating a first manuscript from research materials; use `nnscholar4-5-manuscript-drafting`;
- creating figures; use `nnscholar4-1-data-figure`, `nnscholar4-2-image-schematic`, or `nnscholar4-3-figure-assembly`;
- formatting manuscript tables; use `nnscholar4-4-table-formatting`;
- verifying citations or adding new references without source lookup;
- writing point-by-point reviewer responses from scratch unless the request is specifically to polish the response text.

## Upstream Priority

Use local or conversation outputs in this order:

1. User-provided draft text or uploaded manuscript file.
2. `nnscholar4-5-manuscript-drafting`: manuscript draft, audit, claim map, missing-evidence checklist.
3. `nnscholar2-3-paper-architecture`: intended structure and claim boundary.
4. `nnscholar2-2-ars-plan`: protocol/methods authority.
5. `nnscholar4-1` to `nnscholar4-4`: figure/table titles, legends, notes, and supported claims.
6. Reviewer comments, journal instructions, style guide, author notes, and target venue requirements.
7. `nnscholar1-4-domain-expert-knowledge-base`: terminology, definitions, accepted reporting norms.

When files are not specified, search `manuscripts/`, `docs/`, `outputs/`, `references/`, `figures/`, and `tables/` for `manuscript_draft.md`, `manuscript_audit.md`, `polished_manuscript.md`, `.docx`, `.md`, reviewer comments, journal instructions, and 4.5 output folders.

## Interactive Micro-Rounds

Ask at most 1-3 questions per round.

### Round 0: Polishing Intake

Return a compact card:

```text
Detected manuscript source:
Detected article type:
Detected discipline / study family:
Detected polishing need:
Suggested polishing mode:
High-risk content:
Missing information:
Next questions:
```

If the request is vague, ask:

1. Which mode do you want: light, logic, deep, venue, reviewer-aware, or bilingual?
2. What text or file should I polish: pasted section, 4.5 draft, Markdown file, Word file, or full manuscript?
3. What target language and target venue/style should I follow?

Use `references/polishing-router.md` when choosing mode.

### Round 1: Meaning and Risk Lock

Before editing, identify:

- numbers, p values, effect sizes, CIs, sample sizes, and model metrics;
- methods, endpoints, eligibility criteria, analysis plan, instruments, datasets, and baselines;
- citations, figure/table callouts, ethics/funding/data availability statements;
- claim level: causal, associative, exploratory, mechanistic, descriptive, interpretive, benchmark, feasibility;
- phrases that may overstate novelty, impact, causality, generalizability, or mechanism.

If the draft has unsafe claims, flag them before rewriting.

### Round 2: Edit Plan

Produce a short edit plan:

```text
Polishing mode:
Target style:
Sections to edit:
Do-not-change items:
Allowed changes:
Risky claims to soften:
Output format:
```

If the user asks for direct polishing and the text is short, proceed immediately while preserving meaning.

### Round 3: Polish

For short text, return:

```text
Polished version:
Change summary:
Author queries:
Risk notes:
```

For long manuscripts, process section by section and keep a status table:

```text
Section | Status | Main changes | Author queries | Risk notes
```

Use `references/section-polishing-template.md`.

### Round 4: Consistency Audit

For full manuscripts or important sections, always audit:

- terminology and abbreviation consistency;
- figure/table callout consistency;
- Methods-Results consistency;
- statistics and numeric preservation;
- claim strength;
- citation placeholders;
- title/abstract/body alignment;
- limitations and conclusion alignment.

Use `references/consistency-audit-template.md`.

### Round 5: Deliverables

When generating files, save:

```text
manuscripts/polish-YYYY-MM-DD-short-topic/
  polished_manuscript.md
  polishing_report.md
  change_summary.md
  author_queries.md
  consistency_audit.md
  risky_claims.md
  source_manifest.json
```

If working from `.docx`, preserve the original file and create Markdown extracted text or a new polished `.docx` only when the required document tooling is available. If tracked changes are not available, provide a tracked-change-style report instead of pretending true Word tracked changes were created.

## Discipline Guardrails

- Clinical medicine: keep cohort, endpoint, model, p value, confidence interval, ethics, and causal language conservative; align with STROBE/CONSORT/TRIPOD-style boundaries when relevant.
- Basic biomedicine: distinguish association, mechanism, representative image, quantification, biological replicate, and technical replicate.
- AI/data science: preserve dataset names, splits, metrics, baselines, seeds, hardware, and uncertainty; do not inflate benchmark superiority.
- Materials/chemistry: preserve synthesis conditions, composition, characterization settings, testing conditions, units, and structure-property limits.
- Education/psychology: preserve scale direction, time points, reliability, effect sizes, intervention details, attrition, and ethics.
- Economics/social science: preserve identification language, fixed effects, clustered errors, sample restrictions, and robustness claims.
- Humanities: improve argument clarity and prose without forcing IMRaD or removing interpretive nuance.
- Engineering: preserve system environment, workload, baselines, hardware/software details, repetitions, and failure mode descriptions.

## Output Rules

Match the user's requested language. If the user asks for English polishing from Chinese source, preserve source meaning and field terminology; do not translate names, datasets, endpoint labels, or citations when the original form is clearer.

Prefer showing edits in a compact table when the user needs traceability:

```text
Original issue | Revised wording | Reason | Risk
```

Use placeholders for missing facts:

```text
[AUTHOR CHECK: confirm ethics approval number]
[CITATION NEEDED: support this claim]
[VALUE CHECK: verify p value]
```

For package creation or long revision projects, use `scripts/create_polishing_package.py`.

