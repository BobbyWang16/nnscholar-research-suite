---
name: nnscholar2-3-paper-architecture
description: Use when NNScholar needs to plan the paper-writing part of a project: manuscript structure, what each section should write, how experiments determine the required figures/tables, result narrative, claim boundary, article outline, abstract skeleton, journal-ready storyline, or writing blueprint. Prefer this skill after NNScholar 2.2 Experimental ARS Plan exists, but also use it from scratch when the user only provides a topic, idea, hypothesis, or draft.
---

# NNScholar 2.3 Paper Architecture

This skill designs the architecture of a scholarly paper. It does not write the paper body and it does not redesign experiments. It turns upstream research evidence and the 2.2 experimental plan/results into a structured manuscript blueprint: article type, storyline, section-by-section writing plan, figure/table plan, result order, discussion argument, and claim boundary.

Version: `0.2.0`. Stage: `research setting / paper architecture`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id and folder name as `nnscholar2-3-paper-architecture` / `/nnscholar2-3-paper-architecture`.
- Keep the title format as `NNScholar 2.3 Paper Architecture`.
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

Prefer protocol-linked architecture. If `nnscholar2-2-ars-plan` exists, treat it as the design authority for Methods, Results, variables, endpoints, experiments, models, corpora, and analysis methods. Do not silently change the research design. If architecture work reveals a protocol problem, send the user back to `nnscholar2-2-ars-plan`.

If no 2.2 protocol exists, build a provisional paper architecture from available 1.1-1.4/2.1 outputs or the user's current input, and mark which sections cannot be finalized.

2.3 answers:

- What type of paper should this become?
- What should each manuscript section write?
- Which experimental outputs from 2.2 become which results paragraphs?
- Which figures and tables are needed to support the paper's claims?
- What is the safest claim boundary?

2.3 must not create the detailed experimental flowchart or decide how each experiment is performed; those belong to 2.2. It can reference the 2.2 experimental flowchart as the Methods/Figure 1 source.

## Run Modes

| Mode | Trigger | Behavior |
|---|---|---|
| `protocol-linked` | Matching 2.2 ARS Plan exists | Generate full architecture using protocol as Methods/Results authority |
| `upstream-linked` | 1.1-1.4 or 2.1 outputs exist, but no 2.2 | Generate provisional architecture and list protocol gaps |
| `draft-aware` | User provides manuscript draft or outline | Restructure without inventing missing methods/results |
| `scratch` | Only a topic, idea, or hypothesis exists | Ask minimal questions and generate a lightweight provisional architecture |

If the user only clicks the button or gives a vague request, ask only:

1. What is the target article type or output: original article, review, thesis chapter, proposal, methods paper, benchmark paper, case report, or grant?
2. What is the research question/hypothesis and discipline?
3. Is there a 2.2 ARS Plan, protocol, dataset, experiment, literature table, or draft to use?

## Upstream Priority

Use upstream evidence in this order:

1. `nnscholar2-2-ars-plan`: protocol, route, specification, endpoints, methods, lock status.
2. `nnscholar2-1-research-planning`: target output, timeline, work packages, deliverables.
3. `nnscholar1-3-hypothesis-generation`: hypothesis, mechanism, testable prediction, claim boundary.
4. `nnscholar1-2-literature-searching`: evidence base, introduction gap, discussion comparators.
5. `nnscholar1-1-question-mining`: question, novelty, scope.
6. `nnscholar1-4-domain-expert-knowledge-base`: terminology, domain conventions, reviewer risks.
7. Current user input: latest writing goal and constraints.

When files are not specified, search the workspace by skill id, topic keywords, date, disease/model/dataset, method names, and report headings. If multiple bundles match, ask the user to choose.

## Multidisciplinary Selection

Before outlining, choose a discipline/article family:

- clinical, public health, or epidemiology;
- basic biology, translational medicine, or wet-lab experiment;
- computational, AI, statistics, or benchmark study;
- engineering, systems, or design science;
- social science, education, policy, or qualitative/mixed methods;
- humanities, theoretical, conceptual, or interpretive essay;
- systematic review, scoping review, or meta-analysis;
- thesis, grant, or proposal.

Load `references/discipline-architecture-guide.md` when discipline-specific section logic or figure/table patterns matter.

## Supervisor Guardrail Integration

For AI/data-science, database, systems, ML, NLP, benchmark/evaluation, or
technical CS papers, read `../../references/supervisor-research-guardrails.md`
before Step 3. Apply the Technical Paper Logic Gate for method/problem papers,
the Benchmark Paper Gate for benchmark/evaluation papers, the Introduction Gate
for intro logic, and the Core Figure Gate for figure/table blueprint. Any
broken limitation-key idea-challenge-method-contribution chain is a CRITICAL
architecture issue and should route back to 2.2 or an upstream workflow before
drafting.

For papers based on repos, training logs, benchmark runs, or autonomous research
iterations, also read `../../references/ai-research-engineering-guardrails.md`.
Use the Repo-to-Paper Evidence Gate to map sections and figures to concrete
artifacts, and use the Evaluation Harness Gate to require benchmark settings and
uncertainty before claiming leaderboard-style improvements.

## High-Impact Paper Integration

For Nature/CNS, Nature-family, Cell/Science-family, or other high-impact
multidisciplinary targets, read
`../../references/high-impact-paper-guardrails.md` before Step 2. Apply its
paper-type taxonomy and argument chain:

```text
field-scale need -> unresolved bottleneck -> proposed move -> decisive evidence -> broader implication -> boundary
```

The architecture must include a paper type (`research`, `methods`,
`hypothesis`, `algorithmic`, or `review`), a terminology ledger, Results
evidence ladder, and claim ceiling. If a link is missing, mark the architecture
provisional instead of hiding the gap with stronger prose.

## Workflow

### Step 1: Architecture Intake

Extract:

- target article/output type;
- discipline and audience;
- protocol status: locked, provisional, missing;
- research question, hypothesis, or thesis;
- available methods/results/data/materials;
- target journal, venue, thesis committee, funder, or style guide if available.

Return a compact architecture card before long output.

### Step 2: Build Core Storyline

Define:

- paper type and high-impact argument chain when relevant;
- terminology ledger decisions for repeated methods, models, datasets, cohorts,
  metrics, materials, assays, or concepts;
- one-sentence storyline;
- central contribution;
- opening gap;
- evidence path;
- strongest allowable claim;
- claims that must not be made.

Use careful claim language. For observational or incomplete work, prefer association, feasibility, pattern, signal, or exploratory language over causal or definitive language.

### Step 3: Design Section Architecture

Create section-level logic appropriate for the discipline. For empirical IMRaD papers, include:

- Title candidates;
- Abstract skeleton;
- Introduction paragraph logic and what each paragraph should establish;
- Methods architecture, derived strictly from 2.2;
- Results architecture, mapping each experiment/result block to a paper subsection;
- Discussion architecture, including interpretation, comparison, implications, limitations, and claim boundary;
- Conclusion boundary.

For non-IMRaD outputs, adapt the structure instead of forcing IMRaD.

### Step 4: Design Figure and Table Blueprint

Every figure/table must answer a specific manuscript question. Include:

- figure core conclusion or table primary claim;
- figure/table title;
- experiment/result block that generates it;
- evidence displayed;
- section placement;
- dependency on data/protocol;
- claim supported;
- risk if missing.

For high-impact targets, also state the figure archetype, hero evidence,
supporting evidence, source-data need, and whether the item belongs in main text
or supplementary material.

When real results are not available, label figure/table content as `planned` or `expected display`, not as observed results.

For detailed template, use `references/paper-architecture-output-template.md`.

### Step 5: Gate and Handoff

Audit:

- protocol consistency;
- discipline fit;
- section completeness;
- Methods/Results alignment;
- figure/table sufficiency;
- claim boundary;
- missing evidence;
- downstream readiness.

If ready, hand off to `nnscholar4-3-paper-writing`. If Methods/Results architecture or the experiment flowchart is unstable, hand back to `nnscholar2-2-ars-plan`.

When handing off to 4.3, include a compact drafting contract:

```text
Drafting readiness:
Target article type:
Target audience / venue:
Core storyline:
Locked Methods authority:
Results section order:
Required figures:
Required tables:
Claims allowed:
Claims prohibited:
Sections still unsafe to draft:
```

## Output Rules

Match the user's language. Keep scientific names, model names, datasets, variables, endpoints, trial IDs, citation keys, and file paths in their original form.

Return a concise architecture brief in chat unless the user asks for a full report. For full reports, follow `references/paper-architecture-output-template.md`.

Use `references/paper-architecture-test-cases.md` for regression examples.

## Non-goals

Do not:

- write full manuscript prose;
- invent results, tables, figures, experiments, citations, samples, approvals, or datasets;
- change a locked 2.2 protocol;
- add endpoints, variables, models, or claims that are not supported by upstream evidence;
- force clinical IMRaD structure onto humanities, conceptual, engineering, or qualitative work when another structure fits better.
- draw or revise the executable experimental flowchart; use 2.2 for that.
