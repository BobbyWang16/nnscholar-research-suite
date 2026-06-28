---
name: nnscholar4-3-paper-writing
description: Use when NNScholar needs paper writing: manuscript brief, first draft, section-by-section drafting, figure/table callout integration, claim-evidence map, missing-evidence checklist, manuscript audit, polishing, deep revision, venue/style adaptation, bilingual academic rewriting, risky-claim audit, consistency check, and response-ready text improvement while coordinating with 4.1 figures and 4.2 tables.
---

# NNScholar 4.3 Paper Writing

This skill turns upstream research materials into manuscript prose and improves existing drafts without changing the science. It unifies first drafting, figure/table integration, polishing, structure-aware revision, and manuscript audits.

Version: `0.3.0`. Stage: `paper output / writing`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the canonical workflow id as `nnscholar4-3-paper-writing` / `/nnscholar4-3-paper-writing`.
- Keep the title format as `NNScholar 4.3 Paper Writing`.
- Name generated folders and files with English ASCII kebab-case slugs.

### Input and Language Policy

- Accept free-form input, upstream NNScholar outputs, figures/tables, result summaries, manuscripts, DOCX/Markdown/LaTeX drafts, reviewer comments, author notes, and target-venue instructions.
- For author-facing plans, audits, and revision notes: output in the user's input language unless requested otherwise.
- For manuscript-facing text: default to polished academic English unless the user or target venue requests Chinese, bilingual, or another language.
- Preserve identifiers in their standard form: DOI/PMID/arXiv IDs, gene/protein symbols, datasets, benchmarks, model names, scales, laws, policies, citation keys, variable names, and figure/table labels.
- Do not fabricate citations, ethics approvals, registrations, sample sizes, statistics, experimental results, author declarations, funding, or venue requirements.

## Core Rule

Do not make the manuscript sound stronger by changing the science. Every sentence must respect the evidence boundary, protocol authority, figure/table support, and claim strength. If a required fact is missing, use an author-check placeholder and list it in the missing-evidence checklist.

For first drafts, build a manuscript brief before drafting unless the user explicitly asks for direct drafting and upstream evidence is complete. For polishing, lock the edit mode and preserve numeric/methodological content.

## Boundary

Use this skill for:

- manuscript brief and full first draft;
- section-by-section drafting;
- abstract, title, introduction, methods, results, discussion, limitation, conclusion, and data/code/ethics placeholders;
- integrating 4.1 figures and 4.2 tables into Results and Methods;
- claim-evidence mapping and missing-evidence checklist;
- light, logic, deep, venue, reviewer-aware, and bilingual polishing;
- risky-claim, terminology, figure/table callout, and Methods-Results consistency audits.

Do not use this skill for:

- creating figures; use `nnscholar4-1-paper-figure`;
- creating tables; use `nnscholar4-2-paper-table`;
- protocol redesign; use `nnscholar2-2-ars-plan`;
- paper architecture redesign before drafting; use `nnscholar2-3-paper-architecture`;
- point-by-point reviewer response from scratch; use `nnscholar5-5-reviewer-response`;
- citation verification alone; use citation/literature workflows.

## Run Modes

| Mode | Trigger | Behavior |
|---|---|---|
| `brief` | upstream artifacts exist but manuscript plan needs confirmation | build manuscript brief, claim ceiling, figure/table callout plan |
| `draft` | user wants first draft or section draft | draft from upstream evidence and placeholders |
| `revise` | user provides draft plus desired changes | revise while preserving meaning |
| `polish-light` | grammar, word choice, concision | conservative language edit |
| `polish-logic` | flow, transitions, redundancy, paragraph logic | structure-aware edit |
| `polish-deep` | section restructuring or venue adaptation | produce edit plan, then revise |
| `reviewer-aware` | reviewer comments or response-ready draft | revise with risks and response alignment |
| `bilingual` | translation polishing or English academic rewrite | preserve source meaning and terms |

## Upstream Priority

Use local or conversation outputs in this order:

1. User-provided manuscript text or file when polishing/revising.
2. `nnscholar2-3-paper-architecture`: manuscript structure, section order, storyline, figure/table blueprint.
3. `nnscholar3-1-experiment-validation-plan`: result summary, claim-evidence map, integrity audit, narrative handoff.
4. `nnscholar2-2-ars-plan`: Methods authority, endpoints, variables, analysis plan, protocol lock.
5. `nnscholar4-1-paper-figure`: figure reports, captions, panel maps, supported claim sentences.
6. `nnscholar4-2-paper-table`: table titles, notes, summary sentences, statistical notes.
7. `nnscholar1-4-domain-expert-knowledge-base`: expert terminology, definitions, mechanism boundaries, domain constraints, reviewer risks, journal-positioning cues, and citation-backed writing-publication guidance.
8. `nnscholar1-2-literature-searching`: evidence base, literature context, comparison studies.
9. `nnscholar1-3-hypothesis-generation` and `nnscholar1-1-question-mining`: hypothesis, gap, novelty, claim boundary.
10. Target venue/style instructions and author notes.

When files are not specified, search `manuscripts/`, `docs/`, `outputs/`, `references/`, `figures/`, `tables/`, `results/`, `research-runs/`, and `data/`.

## Workflow

### Step 1: Writing Intake

Return a compact card:

```text
Detected mode:
Detected article type:
Detected discipline / study family:
Available upstream materials:
Figures/tables found:
Drafting or polishing risks:
Missing information:
Next questions:
```

Ask at most 1-3 questions if needed.

### Step 2: Evidence and Claim Inventory

Build a source inventory:

```text
Source | Role | Stable facts | Claims supported | Unsafe gaps
2.2 protocol | Methods authority | ... | ... | ...
3.1 results | Evidence authority | ... | ... | ...
1.4 expert KB | Expert reference | ... | ... | ...
4.1 figure report | Visual evidence | ... | ... | ...
4.2 table report | Tabular evidence | ... | ... | ...
```

Separate stable facts, planned/expected results, missing data, and prohibited claims.

For high-impact targets, read
`../../references/high-impact-paper-guardrails.md` and classify the paper type
as `research`, `methods`, `hypothesis`, `algorithmic`, or `review`. Create or
update the terminology ledger before drafting or polishing.

### Step 3: Manuscript Brief or Edit Plan

For drafting, produce:

```text
Working title:
Paper type:
Article type:
Target audience / venue:
High-impact argument chain:
One-sentence storyline:
Central contribution:
Allowed claim ceiling:
Prohibited claims:
Section plan:
Figure/table callout plan:
Citation/evidence gaps:
Author decisions needed:
```

For polishing, produce:

```text
Polishing mode:
Target style:
Sections to edit:
Do-not-change items:
Allowed changes:
Risky claims to soften:
Output format:
```

### Step 3.5: Expert Knowledge Reference

If a 1.4 expert knowledge base exists, consult the root expert and the relevant
sub-KB before drafting or deep polishing:

- `study-design` for cohort/object, endpoint, hypothesis, bias, and claim
  ceiling;
- `experiment-data-analysis` for variables, measurements, statistics, models,
  robustness, and figure/table interpretation;
- `writing-publication` for manuscript structure, terminology, citation
  positioning, reviewer risks, and venue-sensitive framing.

Use the expert KB to constrain terminology, mechanism wording, causal language,
limitations, and Discussion claims. If 1.4 and the current draft disagree, do
not silently smooth over the conflict; add an author query and mark the affected
claim as `needs verification`.

### Step 4: Draft or Revise

For first drafts, draft in this order unless requested otherwise:

1. Title and abstract skeleton.
2. Introduction.
3. Methods or study design.
4. Results with figure/table callouts.
5. Discussion.
6. Conclusion, limitations, data/code availability, ethics, funding, and acknowledgement placeholders.

For polishing, preserve factual meaning, numbers, p values, model names, sample sizes, endpoints, eligibility criteria, instrument conditions, citations, and figure/table callouts.

### Step 5: Figure and Table Integration

Every cited figure/table must have:

- callout in manuscript body;
- caption-ready figure/table title;
- location in Results, Methods, or Supplement;
- supported claim sentence;
- Methods/provenance sentence when needed;
- limitation or boundary note.

Do not cite a figure/table that does not exist, has not been generated, or was not described by the user. Use placeholders only when explicitly planned.

### Step 6: Manuscript Audit

Always produce or update:

- paper-type fit and high-impact argument-chain audit when relevant;
- terminology ledger;
- claim-evidence map;
- Methods-Results consistency audit;
- figure/table callout checklist;
- missing evidence checklist;
- overclaim and causality audit;
- citation gap list;
- abbreviation and terminology audit;
- next revision plan.

## External Writing Skill Integration

Use companion skills as subroutines:

- `evidence-driven-writing` for Introduction, Related Work, and citation-driven background.
- `writing-core`, `writing-chapters`, and `paper-orchestration` for chapter packets and large manuscript structure.
- `ml-paper-writing` for AI/ML venues, citation anti-hallucination, and conference paper conventions.
- `systems-paper-writing` for systems venues.
- `paper-claim-audit`, `citation-audit`, and `pre-submission-reviewer` before deadline-facing outputs when available.

NNScholar keeps the evidence boundary, workflow stage order, and handoff contract.

High-impact style is handled natively through
`../../references/high-impact-paper-guardrails.md`; do not route to an external
Nature-style writing skill unless the user explicitly requests that separate
tool.

## Discipline Guardrails

- Clinical medicine: follow observational/interventional reporting boundaries; state cohort, eligibility, endpoints, validation, ethics placeholders, and avoid causal language unless design supports it.
- Basic biomedicine: distinguish mechanism, association, assay readout, biological replicate, technical replicate, and representative image.
- AI/data science: report datasets, splits, baselines, metrics, uncertainty, ablations, implementation details, and integrity/audit status; avoid benchmark claims without comparable settings.
- Materials/chemistry: report synthesis, characterization, property testing, operating conditions, units, and batch/repetition limits.
- Education/psychology: report participants, instruments, scale direction, reliability, intervention, time points, attrition, and ethics.
- Economics/social science: separate identification strategy from descriptive association; report model specification, fixed effects, clustering, sample restrictions, and robustness.
- Humanities: preserve interpretive argument, corpus/source selection, period, language, coding rules, and evidentiary limits.
- Engineering: report system architecture, hardware/software environment, workloads, repetitions, and failure modes.

## Supervisor and AI Research Integration

For technical CS/AI manuscripts, read `../../references/supervisor-research-guardrails.md` before the manuscript brief. Apply Technical Paper Logic, Benchmark Paper, Introduction, Core Figure, and Pre-Submission gates as relevant.

For manuscripts drafted from repos, result folders, experiment logs, training runs, or autonomous research notes, read `../../references/ai-research-engineering-guardrails.md`. Apply Repo-to-Paper Evidence, Citation and Venue, Evaluation Harness, and Rigor Review gates. Use placeholders rather than inventing missing metrics, citations, or observed findings.

For high-impact manuscripts, apply the reviewer-style pre-submission audit in
`../../references/high-impact-paper-guardrails.md`: technical soundness,
originality/significance, interdisciplinary readership, and nonspecialist
readability. Any not-assessable claim remains a visible author query.

## Output Rules

Match the user's language for author-facing reports. Use polished academic English for manuscript-facing text unless requested otherwise.

Save generated assets using ASCII slugs:

```text
manuscripts/paper-writing-YYYY-MM-DD-short-topic/
  manuscript_brief.md
  manuscript_draft.md
  polished_manuscript.md
  section_claim_map.md
  figure_table_callouts.md
  missing_evidence_checklist.md
  manuscript_audit.md
  change_summary.md
  author_queries.md
  source_manifest.json
```

For package creation, reuse `scripts/create_manuscript_package.py` when it fits.
For polishing package creation, reuse `scripts/create_polishing_package.py` when it fits.

Always include:

```text
## NNScholar Suite Handoff

From workflow: nnscholar4-3-paper-writing
To recommended next workflow:
Project/topic:
Locked decisions:
Open questions:
Files/artifacts created or used:
Evidence boundary:
Companion skill bridge used:
Risks requiring human confirmation:
```

## Non-goals

Do not fabricate citations, results, ethics approvals, funding, or venue requirements. Do not change scientific meaning during polishing. Do not hide missing evidence behind fluent prose. Do not draft a full result paper from only a broad topic; route upstream first.
