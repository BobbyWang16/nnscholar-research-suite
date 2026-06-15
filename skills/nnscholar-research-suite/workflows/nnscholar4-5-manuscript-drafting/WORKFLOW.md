---
name: nnscholar4-5-manuscript-drafting
description: Use when NNScholar needs to generate, assemble, or revise a first manuscript draft from upstream research outputs, including question mining, literature search, hypothesis, domain knowledge base, research plan, ARS protocol, paper architecture, flowchart, experiment/validation plan, figures, figure legends, tables, table notes, or user-provided notes. Produces a manuscript brief for author confirmation, section-by-section academic draft, figure/table callouts, claim-evidence map, missing-evidence checklist, and manuscript audit. Works across clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, and engineering.
---

# NNScholar 4.5 Manuscript Drafting

This skill turns NNScholar's upstream research work into a disciplined first manuscript draft. It is a drafting orchestrator, not a result generator. It must preserve the locked research design, integrate figure/table text, and avoid inventing unsupported evidence.

Version: `0.2.0`. Stage: `paper output / manuscript drafting`. Legacy workflow alias: `$nnscholar4-5-manuscript-drafting`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar4-5-manuscript-drafting` / `/nnscholar4-5-manuscript-drafting`.
- Keep the title format as `NNScholar 4.5 Manuscript Drafting`.
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

Do not immediately write a full paper. First build a manuscript brief and ask the author to confirm or revise it unless the user explicitly asks for direct drafting and the upstream evidence is already complete.

The default workflow is:

1. collect upstream evidence;
2. produce a manuscript brief;
3. lock section plan and claim boundaries;
4. draft section by section;
5. integrate figure/table callouts, captions, table titles, notes, and abbreviations;
6. audit consistency and missing evidence.

Never invent sample size, statistical results, experimental findings, ethics approval, datasets, citations, instrument parameters, or funding details. If a required fact is missing, write a placeholder and list it in the missing-evidence checklist.

## Boundary

Use this skill for:

- first full manuscript drafts;
- section-by-section manuscript generation;
- manuscript brief before drafting;
- converting 2.3 paper architecture into IMRaD or discipline-specific prose;
- integrating 4.1-4.4 figure/table outputs into Results and Methods;
- claim-evidence mapping;
- missing evidence and overclaim audit;
- multidisciplinary paper drafts, thesis chapters, conference papers, short communications, case reports, methods papers, reviews, and proposals.

Do not use this skill for:

- creating new figures from data; use `nnscholar4-1-data-figure`;
- creating new schematics; use `nnscholar4-2-image-schematic`;
- assembling multi-panel figures; use `nnscholar4-3-figure-assembly`;
- formatting manuscript tables; use `nnscholar4-4-table-formatting`;
- final language polishing of an existing manuscript; use a later polishing skill;
- citation verification or reference formatting alone.

## Run Modes

| Mode | Trigger | Behavior |
|---|---|---|
| `upstream-linked` | 2.3 architecture and 4.x outputs exist | Build brief from upstream files, then draft |
| `protocol-linked` | 2.2 ARS protocol exists | Treat protocol as Methods authority |
| `figure-table-linked` | 4.1-4.4 outputs exist | Draft Results around figure/table callouts |
| `draft-aware` | User provides existing draft | Revise structure and fill gaps without inventing data |
| `scratch` | Only topic/question exists | Ask minimal questions and draft a provisional outline or proposal-style draft, not a fake result paper |

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar2-3-paper-architecture`: manuscript structure, drafting contract, section order, figure/table blueprint.
2. `nnscholar2-2-ars-plan`: locked Aim/Route/Specification, Methods authority, endpoints, analysis plan.
3. `nnscholar4-1-data-figure`: figure reports, supported claim sentences, Methods/provenance sentences.
4. `nnscholar4-2-image-schematic`: schematic captions, label maps, evidence boundary notes.
5. `nnscholar4-3-figure-assembly`: final figure legends, panel-by-panel claim maps.
6. `nnscholar4-4-table-formatting`: table titles, notes, summary sentences, statistical notes.
7. `nnscholar3-1-experiment-validation-plan`: validation resources, steps, feasibility, quality gates.
8. `nnscholar1-4-domain-expert-knowledge-base`: terminology, definitions, reviewer risks.
9. `nnscholar1-2-literature-searching`: evidence base, literature context, comparison studies.
10. `nnscholar1-3-hypothesis-generation` and `nnscholar1-1-question-mining`: hypothesis, gap, novelty, claim boundary.
11. User-provided notes, datasets, results, draft files, reference manager exports, or target journal instructions.

When files are not specified, search `manuscripts/`, `docs/`, `outputs/`, `references/`, `figures/`, `tables/`, `results/`, and `data/` for architecture reports, ARS plans, figure reports, legends, table reports, draft notes, and source materials.

## Interactive Micro-Rounds

Ask at most 1-3 questions per round.

### Round 0: Draft Intake

Return a compact intake card:

```text
Detected article type:
Detected discipline / study family:
Available upstream materials:
Likely manuscript sections:
Figures/tables found:
Drafting risks:
Missing information:
Next questions:
```

If the request is vague, ask:

1. What output do you want: full paper, short communication, thesis chapter, conference paper, review, case report, proposal, or grant-style draft?
2. Should I use previous NNScholar outputs, uploaded files, or start from the topic only?
3. What target language and target venue/style should the first draft follow?

Use `references/manuscript-router.md` when choosing article family.

### Round 1: Evidence and Claim Inventory

Build a source inventory:

```text
Source | Role | Stable facts | Claims supported | Unsafe gaps
2.2 ARS | Methods authority | ... | ... | ...
2.3 architecture | Section plan | ... | ... | ...
4.1 figure report | Results evidence | ... | ... | ...
4.4 table report | Results evidence | ... | ... | ...
```

Separate:

- stable facts that can be written;
- planned or expected results that must remain conditional;
- missing data that require placeholders;
- claims that are prohibited because the design or evidence does not support them.

### Round 2: Manuscript Brief Before Drafting

Before full drafting, produce:

```text
Working title:
Article type:
Target audience / venue:
One-sentence storyline:
Central contribution:
Allowed claim ceiling:
Prohibited claims:
Section plan:
Figure/table callout plan:
Citation/evidence gaps:
Author decisions needed:
```

If the author confirms, continue. If not, revise the brief first.

Use `references/manuscript-brief-template.md`.

### Round 3: Draft Section by Section

Draft in this order unless the user requests otherwise:

1. Title and abstract skeleton.
2. Introduction.
3. Methods or study design.
4. Results, with figure/table callouts.
5. Discussion.
6. Conclusion, limitations, data/code availability placeholders, ethics/funding/acknowledgements placeholders.

For long manuscripts, generate one section at a time and keep a section status table.

Use `references/discipline-drafting-patterns.md` for discipline-specific prose logic.

### Round 4: Figure and Table Integration

Every cited figure/table must have:

- callout in the manuscript body;
- caption-ready title or table title;
- location in Results, Methods, or Supplement;
- supported claim sentence;
- limitation or boundary note when relevant.

Do not cite a figure/table in Results if it was not found, generated, or described by the user. Use placeholders such as `[Figure 2 placeholder: calibration curve]` only when the author has explicitly planned that output.

### Round 5: Manuscript Audit

Always produce:

- claim-evidence map;
- Methods-Results consistency audit;
- figure/table callout checklist;
- missing evidence checklist;
- overclaim and causality audit;
- citation gap list;
- abbreviation and terminology audit;
- next revision plan.

Use `references/manuscript-audit-template.md`.

## Discipline Guardrails

- Clinical medicine: follow observational/interventional reporting boundaries; state cohort, eligibility, endpoints, model validation, ethics placeholders, and avoid causal language unless design supports it.
- Basic biomedicine: distinguish mechanism, association, assay readout, biological replicate, and technical replicate.
- AI/data science: report dataset splits, baselines, metrics, uncertainty, ablations, and implementation details; avoid benchmark claims without comparable settings.
- Materials/chemistry: report synthesis, characterization, property testing, operating conditions, and batch/repetition limits.
- Education/psychology: report participants, instruments, scale direction, reliability, intervention, time points, attrition, and ethics.
- Economics/social science: separate identification strategy from descriptive association; report model specification, fixed effects, clustering, sample restrictions, and robustness.
- Humanities: preserve interpretive argument, corpus/source selection, period, language, coding rules, and evidentiary limits.
- Engineering: report system architecture, hardware/software environment, workloads, repetitions, and failure modes.

## Output Rules

Match the user's language. Keep variable names, endpoint names, model names, datasets, journal names, and abbreviations in their original form when clearer.

Save generated assets using ASCII slugs:

```text
manuscripts/draft-YYYY-MM-DD-short-topic/
  manuscript_brief.md
  manuscript_draft.md
  section_claim_map.md
  figure_table_callouts.md
  missing_evidence_checklist.md
  manuscript_audit.md
  source_manifest.json
```

If the workspace lacks a `manuscripts/` folder, create it only when generating files.

For a blank package or early-stage project, use `scripts/create_manuscript_package.py` to create the standard file structure.

