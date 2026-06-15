---
name: nnscholar5-1-journal-conference-recommendation
description: Use when NNScholar needs to recommend, compare, rank, or revise target journals, conferences, preprint venues, Chinese journals, SCI/SSCI/EI/Scopus venues, CCF/AI conferences, medical journals, materials/chemistry journals, education/psychology journals, economics/social science journals, humanities journals, or interdisciplinary publication venues. Produces multidisciplinary venue fit analysis, submission strategy, risk assessment, revision priorities, fallback plan, and author decision checklist from manuscripts, abstracts, keywords, figures/tables, or NNScholar 4.x outputs.
---

# NNScholar 5.1 Venue Recommendation

This skill recommends publication venues and creates a submission strategy. It is not only a ranking list: it must explain venue fit, rejection risks, required revisions, publication ethics constraints, and fallback paths.

Version: `0.2.0`. Stage: `submission / venue recommendation`. Legacy workflow alias: `$nnscholar5-1-journal-conference-recommendation`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar5-1-journal-conference-recommendation` / `/nnscholar5-1-journal-conference-recommendation`.
- Keep the title format as `NNScholar 5.1 Venue Recommendation`.
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

Do not recommend venues from prestige alone. Match the manuscript's discipline, article type, evidence strength, methods, claims, audience, word limits, open access/fee constraints, review speed, and author priorities.

If current venue information matters, verify with official venue pages or reliable indexing pages before giving final factual claims about scope, fees, deadlines, word limits, or submission categories. If browsing is not performed, mark those fields as "needs verification".

## Boundary

Use this skill for:

- journal/conference recommendation;
- journal vs conference choice;
- target venue shortlist;
- transfer/re-submission strategy;
- novelty and fit risk assessment;
- revision priorities for target venues;
- multidisciplinary venue matching.

Do not use this skill for:

- final formatting to a target venue; use `nnscholar5-2-submission-finalization`;
- portal step-by-step submission; use `nnscholar5-3-submission-portal-workflow`;
- cover letter drafting; use `nnscholar5-4-cover-letter`;
- reviewer response; use `nnscholar5-5-reviewer-response`.

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar4-6-manuscript-polishing`: polished manuscript, consistency audit, risky claims.
2. `nnscholar4-5-manuscript-drafting`: manuscript brief, draft, claim map, missing evidence checklist.
3. `nnscholar2-3-paper-architecture`: article type, storyline, claim boundary, figure/table blueprint.
4. `nnscholar1-2-literature-searching`: comparator journals/conferences from cited work.
5. `nnscholar1-4-domain-expert-knowledge-base`: discipline norms and reviewer risks.
6. User preferences: impact/rank, speed, open access, fees, region, language, journal vs conference, target list, rejection tolerance.

When files are not specified, search `manuscripts/`, `docs/`, `outputs/`, `references/`, and `submission/` for abstracts, manuscripts, briefs, audits, and target-venue notes.

## Workflow

### Step 1: Venue Intake

Return a short card:

```text
Detected article type:
Detected discipline / study family:
Evidence strength:
Target audience:
Author priorities:
Initial venue family:
Missing information:
Next questions:
```

Ask only what is needed:

1. Do you prefer journal, conference, preprint, Chinese journal, or mixed recommendations?
2. What matters most: prestige, acceptance probability, speed, open access fee, indexing, geography/language, or reviewer fit?
3. Should I verify current venue details online before finalizing the list?

### Step 2: Multidisciplinary Fit Router

Use `references/venue-fit-router.md` to classify fit:

- clinical/medical;
- biomedical/wet lab;
- AI/data science;
- materials/chemistry;
- education/psychology;
- economics/social science;
- humanities;
- engineering;
- interdisciplinary.

### Step 3: Shortlist and Risk Tiers

Create 3 tiers:

- `A. Ambitious`: high fit but high rejection risk.
- `B. Balanced`: good fit and realistic.
- `C. Safe/Fast/Fallback`: lower prestige or broader scope but practical.

For each venue include:

- fit rationale;
- article type compatibility;
- evidence/method requirements;
- likely reviewer concerns;
- revisions needed before submission;
- risk level;
- facts that need official verification.

### Step 4: Revision-Aware Recommendation

Do not stop at recommending. Produce a target-specific revision plan:

```text
Venue:
Required manuscript changes:
Abstract/title angle:
Figure/table changes:
Methods/reporting checklist:
Ethics/data/code statements:
Supplementary material needs:
Risky claims to soften:
```

### Step 5: Decision Package

Use `references/recommendation-output-template.md` for a full report. When generating files, use `scripts/create_recommendation_package.py`.

## Discipline Guardrails

- Clinical medicine: check article type, ethics, registry, CONSORT/STROBE/TRIPOD/PRISMA fit, clinical validation, and patient relevance.
- Basic biomedicine: check mechanistic depth, model system, replicate quality, assay completeness, and figure expectations.
- AI/data science: check benchmarks, baselines, ablations, reproducibility, code/data policy, conference deadlines, and double-blind rules.
- Materials/chemistry: check novelty, characterization completeness, performance comparison, mechanism, and reproducibility.
- Education/psychology: check ethics, participant sample, validated instruments, intervention logic, reliability, and reporting standards.
- Economics/social science: check identification strategy, data transparency, robustness, policy/theory contribution, and field journal scope.
- Humanities: check conceptual contribution, corpus/source fit, theoretical conversation, and journal tradition.
- Engineering: check system validation, workload realism, reproducibility, and application relevance.

## Output Rules

Match the user's language. If using current venue data, cite source links or mark "needs verification". Never guarantee acceptance.

Default output files:

```text
submission/recommendation-YYYY-MM-DD-short-topic/
  venue_shortlist.md
  venue_comparison_matrix.md
  revision_strategy.md
  author_decision_checklist.md
  source_manifest.json
```

