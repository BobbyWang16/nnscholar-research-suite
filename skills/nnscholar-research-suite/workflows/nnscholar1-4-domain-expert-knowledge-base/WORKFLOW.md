---
name: nnscholar1-4-domain-expert-knowledge-base
description: Use when NNScholar needs to convert question mining, literature search, hypothesis reports, PDFs, and local research materials into a reusable citation-grounded domain expert knowledge base for study design, data analysis, writing, reviewer-risk checks, or future project consultation.
---

# NNScholar 1.4 Domain Expert KB

This skill turns a project-specific research corpus into a reusable domain expert knowledge base. It sits after:

- `nnscholar1-1-question-mining`;
- `nnscholar1-2-literature-searching`;
- `nnscholar1-3-hypothesis-generation`.

The generated knowledge base should let future agents answer research design, experiment/data analysis, writing, reviewer-risk, journal-selection, and evidence lookup questions by consulting one expert corpus instead of repeatedly re-reading all upstream files.

The architecture is a router expert plus three sub-knowledge-bases:

1. `study-design`: research question, hypothesis, study design, cohort, endpoints, feasibility, bias.
2. `experiment-data-analysis`: experiments, measurements, data structure, statistics, models, figures/tables, robustness.
3. `writing-publication`: manuscript structure, argumentation, citations, journal selection, reviewer risks, response strategy.

The router expert answers simple questions directly. If a question needs deeper expertise, route it to the relevant sub-KB and cite that sub-KB's source keys.

Inspired by `papers-to-skill`: do not create a one-off summary or raw RAG dump. Create a compact, citation-grounded expert operating layer with claims, methods, concepts, contradictions, applications, and a reading map.

Reference: https://github.com/luckylykkk/papers-to-skill

Version: `0.2.0`. Stage: `literature / domain expert knowledge base`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id and folder name as `nnscholar1-4-domain-expert-knowledge-base` / `/nnscholar1-4-domain-expert-knowledge-base`.
- Keep the title format as `NNScholar 1.4 Domain Expert KB`.
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

## Language, Filename, and Formatting Rule

Match the user's input language in all user-facing output and generated KB prose. If the user writes in Chinese, output Chinese. If the user writes in English, output English. If the user mixes languages, use the dominant language or the language explicitly requested. Keep technical terms, database names, trial IDs, gene/protein names, model names, benchmark names, and citation keys in their standard scholarly form.

Folder names, file names, and source keys must always use English ASCII slugs. Use lowercase words, hyphens, and no spaces, punctuation, Chinese characters, or special symbols.

Use clean Markdown with stable headings, compact tables, and editable bullet lists. The KB must be easy to update: shared evidence belongs in `core/`, detailed operating guidance belongs in the three sub-KBs, and long duplicated background summaries should be avoided.

## Template Localization Rule

Use the bundled `references/domain-expert-kb-template.md` as the structural template. The template may contain example headings, but every generated KB heading and field label must be localized to the detected output language. Keep only folder names, file names, source keys, database names, search strings, citation metadata, and standard identifiers in English or their original language.

## Core Rule

Build a reusable multi-expert knowledge base, not a literature summary.

Every substantive recommendation must trace back to:

- an upstream NNScholar output;
- a paper PDF or extracted paper note;
- a local project reference;
- or a clearly marked inference from these sources.

If the corpus does not support a claim, say so. Do not invent paper metadata, study results, thresholds, methods, or reviewer expectations.

## Expert Routing Rule

The root expert is a dispatcher and integrator. It should:

- classify the user's question;
- load the smallest relevant sub-KB;
- answer directly only when the root profile and reading map are sufficient;
- delegate to a sub-KB when the answer requires detailed design, analysis, or writing guidance;
- combine sub-KB answers only when the task crosses boundaries.

Routing:

| User intent | Primary sub-KB | Secondary sub-KB |
|---|---|---|
| "How should I design the study?" | `study-design` | `experiment-data-analysis` |
| "What cohort/endpoints/eligibility?" | `study-design` | `writing-publication` |
| "How should I analyze data?" | `experiment-data-analysis` | `study-design` |
| "What experiments/assays/measurements?" | `experiment-data-analysis` | `study-design` |
| "What figures/tables should I make?" | `experiment-data-analysis` | `writing-publication` |
| "How to write Introduction/Discussion?" | `writing-publication` | `study-design` |
| "Where should I submit?" | `writing-publication` | root evidence files |
| "What will reviewers challenge?" | `writing-publication` | all sub-KBs |
| "Which paper supports this claim?" | root `core` | relevant sub-KB |

If the root expert cannot answer confidently, it must state which sub-expert should handle the question and load that sub-KB.

## Input

Accept:

- a topic, research question, project name, or target article;
- exact paths to 1.1/1.2/1.3 outputs;
- a `references/` or `reference/` folder;
- core paper PDFs;
- extracted PDF notes;
- local protocols, study plans, tables, codebooks, statistical notes, or draft manuscripts.

The user may have multiple projects in the same folder. Do not assume the newest file is correct. Match topic keywords, synonyms, dates, stage names, and user wording.

## Modes

Choose a mode from intent:

| Mode | Use when | Output |
|---|---|---|
| `build` | User wants a new expert knowledge base | `references/domain-experts/<slug>/` |
| `update` | User adds PDFs, notes, or new NNScholar outputs | Updated evidence files and validation report |
| `consult` | User asks a research design/data analysis/writing question using an existing KB | Citation-grounded expert answer |
| `validate` | User asks whether the KB is ready | Coverage and citation integrity report |

If mode is unclear, default to `build`.

## Evidence Discovery

When no exact files are provided:

1. Search `references/`, `reference/`, `docs/`, `outputs/`, and user-specified folders.
2. Prefer a matching 1.3 hypothesis report, then 1.2 literature-search report, then 1.1 question-mining report.
3. Include matching PDFs or paper notes from the same topic.
4. Present the top candidate evidence bundle only if ambiguity remains.

Evidence priority:

1. Locked 1.3 hypothesis report for the same project.
2. 1.2 literature-search report and core literature table.
3. 1.1 question-mining report and research gap.
4. PDFs and extracted paper notes.
5. Local study design, data dictionary, protocol, or draft manuscript.
6. Current conversation text.

If PDFs are not yet present, build a provisional KB from 1.1/1.2/1.3 and mark `pdf_coverage: pending`.

## Output Location

Save the knowledge base to:

```text
references/domain-experts/<english-ascii-slug>/
```

Suggested example:

```text
references/domain-experts/sclc-tarlatamab-pdl1/
```

Use English ASCII slugs only.

## Required Output Files

Generate or update:

```text
references/domain-experts/<slug>/
|-- README.md
|-- router.md
|-- source-manifest.md
|-- papers.md
|-- core/
|   |-- expert-profile.md
|   |-- evidence-table.md
|   |-- claims.md
|   |-- concepts.md
|   |-- contradictions.md
|   |-- decision-rules.md
|   `-- reading-map.md
|-- study-design/
|   |-- expert-profile.md
|   |-- design-guide.md
|   |-- hypothesis-to-design.md
|   |-- population-endpoints.md
|   |-- feasibility-bias.md
|   |-- reviewer-risks.md
|   `-- consultation-protocol.md
|-- experiment-data-analysis/
|   |-- expert-profile.md
|   |-- experiment-measurement-guide.md
|   |-- data-dictionary-plan.md
|   |-- statistical-analysis-plan.md
|   |-- figures-tables-plan.md
|   |-- robustness-sensitivity.md
|   `-- consultation-protocol.md
|-- writing-publication/
|   |-- expert-profile.md
|   |-- manuscript-structure.md
|   |-- argumentation-guide.md
|   |-- citation-map.md
|   |-- journal-selection.md
|   |-- reviewer-response-risks.md
|   `-- consultation-protocol.md
`-- validation-report.md
```

Use the bundled `references/domain-expert-kb-template.md` for section expectations.

## Pipeline

### 1. Resolve Project Bundle

Identify:

- project slug;
- research question;
- article type;
- stage outputs used;
- PDFs available or missing;
- local notes or protocols available.

If there are multiple plausible bundles, ask one concise confirmation question.

### 2. Build Source Manifest

Create `source-manifest.md`:

- file path;
- source type;
- title/topic;
- extraction status;
- relevance;
- limitations;
- citation key if applicable.

For PDFs:

- use existing extraction tools when available;
- extract title, abstract, methods, results, limitations, and conclusions;
- record failed extraction, partial extraction, or missing tables.

Do not paste raw full paper text into the KB.

### 3. Create Stable Citation Keys

Use stable keys:

```text
firstauthor-year-short-title
nct-06211036
nnscholar-1-2-sclc-tarlatamab-pdl1-2026-06-10
```

Every substantive claim in the KB should cite one or more keys.

### 4. Distill Shared Core Evidence

Distill shared evidence into `core/`:

| Lane | Output file | What to extract |
|---|---|---|
| Claims | `core/claims.md` | findings, hypotheses, effect directions, confidence |
| Concepts | `core/concepts.md` | definitions, taxonomies, mechanisms, construct relationships |
| Contradictions | `core/contradictions.md` | negative results, disagreements, boundary conditions, weak links |
| Decision rules | `core/decision-rules.md` | what future agents should recommend, avoid, or check |
| Reading map | `core/reading-map.md` | which source and sub-KB to read for each future question |

Each lane must distinguish:

- paper-supported claims;
- upstream NNScholar synthesis;
- agent inference;
- unknown or unresolved issues.

### 5. Build the Three Sub-Knowledge-Bases

Each sub-KB should be richer than a simple guide and should contain operational instructions, defaults, traps, and templates.

#### Study Design Sub-KB

Purpose: turn question/hypothesis/evidence into a feasible article design.

Include:

- study type options and recommended default;
- population/system definition;
- inclusion/exclusion criteria;
- exposure/intervention/comparator;
- primary and secondary endpoints;
- hypothesis-to-design mapping;
- sample/data requirements;
- bias, confounding, feasibility, and ethics;
- minimum viable design vs stronger design;
- design reviewer risks.

#### Experiment and Data Analysis Sub-KB

Purpose: guide experiments, measurements, data structure, statistical modeling, robustness, and figure/table planning.

Include:

- measurement/assay/data collection plan;
- variable dictionary plan;
- primary analysis model;
- secondary analyses;
- missing data handling;
- confounder adjustment;
- subgroup and interaction analyses;
- sensitivity/robustness checks;
- figure/table plan;
- common analysis mistakes and reviewer challenges.

For clinical projects, this sub-KB can focus on data analysis and biomarker measurement. For basic or wet-lab projects, include experimental design, perturbation, readouts, controls, rescue/validation, and reproducibility.

#### Writing and Publication Sub-KB

Purpose: guide manuscript structure, scientific argumentation, citation placement, journal selection, and reviewer response.

Include:

- title/abstract direction;
- Introduction logic;
- Methods reporting checklist;
- Results narrative and figure sequence;
- Discussion claims and limitations;
- citation map by claim;
- target journal tiers and fit logic;
- reviewer-risk questions;
- response strategy and wording cautions.

### 6. Synthesize Router and Expert Profiles

Root `router.md` must include:

- project scope;
- available sub-KBs;
- routing table;
- answer escalation rules;
- citation behavior;
- when to load which files;
- when to say "insufficient evidence".

Each `expert-profile.md` must include:

- expert identity;
- scope;
- best-supported conclusions;
- uncertain areas;
- forbidden overclaims;
- default answer behavior;
- citation requirements;
- when to ask for more evidence;
- when to route to study design, data analysis, writing, or evidence lookup.

Keep root files compact. Future agents should read `router.md` and `core/reading-map.md` first, then load only the relevant sub-KB.

### 7. Build Consultation Protocols

Each sub-KB `consultation-protocol.md` must define answer patterns for its own tasks.

Root routing protocol must define answer patterns for:

- research design;
- data analysis/statistics;
- manuscript writing;
- figure/table planning;
- reviewer-risk check;
- evidence lookup;
- updating the KB with new PDFs.

Every substantive answer should end with a short `References` section using stable citation keys.

### 8. Validate

Create `validation-report.md`:

- source coverage;
- missing PDFs or failed extraction;
- lane coverage;
- citation traceability;
- 3 realistic test prompts;
- dry-run answer checks;
- residual risks;
- update recommendations.

Validation should check:

- all required files exist;
- three sub-KBs exist and have expert profiles;
- claims cite source keys;
- contradictions are preserved;
- future answers require references;
- limitations are visible;
- the KB does not overclaim beyond its corpus.

## Consultation Behavior

When using an existing KB:

1. Read `router.md`.
2. Read `core/reading-map.md`.
3. Classify the user's question.
4. Load only the relevant sub-KB files.
5. Answer with:
   - recommendation;
   - evidence basis;
   - caveats;
   - next action;
   - references.

Do not load all KB files by default.

## Domain-Specific Routing

| User asks | Route to |
|---|---|
| "How should I design this study?" | `study-design/` plus `core/decision-rules.md` |
| "How should I analyze the data?" | `experiment-data-analysis/` plus `core/contradictions.md` |
| "What experiments or measurements should I run?" | `experiment-data-analysis/` plus `study-design/` |
| "How should I write the Introduction/Discussion?" | `writing-publication/` plus `core/claims.md` |
| "Which journal should I submit to?" | `writing-publication/journal-selection.md` |
| "Which papers support this?" | `papers.md`, `core/evidence-table.md`, `core/reading-map.md` |
| "What would reviewers challenge?" | `writing-publication/reviewer-response-risks.md`, `core/contradictions.md`, relevant sub-KB risks |
| "Can I add new PDFs?" | `source-manifest.md`, then update all affected lane files |

## Guardrails

- Do not create a generic field overview when a project-specific expert KB is requested.
- Do not silently mix multiple topics or projects.
- Do not cite papers absent from `papers.md` or `source-manifest.md`.
- Do not treat upstream NNScholar synthesis as primary paper evidence.
- Do not hide missing PDFs, failed extraction, or weak evidence lanes.
- Do not flatten contradictions into consensus.
- Do not answer future consultation questions without references unless the user explicitly asks for uncited brainstorming.
- Do not paste long copyrighted PDF text into the KB.
- If fewer than two primary sources are available, mark the KB as provisional and say cross-paper synthesis is limited.
- Do not let the root expert improvise deep design, analysis, or writing advice when a sub-KB exists; route first.
- Do not duplicate large content across all three sub-KBs; put shared evidence in `core/` and link to it.

