---
name: nnscholar1-3-hypothesis-generation
description: Use when NNScholar needs interactive research hypothesis generation, hypothesis refinement, mechanistic hypothesis critique, falsifiability checks, or pre-study-design hypothesis locking for article-type empirical papers.
---

# NNScholar 1.3 Hypothesis Generation

This skill turns a selected research question and local literature base into testable research hypotheses before study or experiment design. It is for article-type empirical papers where hypotheses guide design, variables, interventions, endpoints, and analysis.

Inspired by Academic Research Skills' human-in-the-loop and Socratic workflow principles: the researcher stays in control; the agent challenges, structures, verifies, and records decisions. Do not let the agent silently invent the hypothesis and move on.

Version: `0.2.0`. Stage: `literature / hypothesis generation`. Legacy workflow alias: `$nnscholar1-3-hypothesis-generation`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar1-3-hypothesis-generation` / `/nnscholar1-3-hypothesis-generation`.
- Keep the title format as `NNScholar 1.3 Hypothesis Generation`.
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

Hypothesis generation must be interactive and evidence-grounded. Do not produce only one polished hypothesis in a single pass unless the user explicitly asks for a quick draft.

The default process is multi-round:

1. locate the most relevant local evidence files;
2. clarify article type and study context;
3. extract the evidence base from question-mining, literature-search, or local project documents;
4. generate candidate hypotheses;
5. challenge and revise them;
6. test falsifiability, measurability, feasibility, and ethical/statistical fit;
7. lock the final hypothesis set only after user confirmation.

Keep interaction efficient. Each dialogue round should be short, decision-focused, and resumable. Avoid dumping large evidence summaries into chat; save detailed reports to `references/`.

## Language, Filename, and Formatting Rule

Match the user's input language in all user-facing output. If the user writes in Chinese, output Chinese. If the user writes in English, output English. If the user mixes languages, use the dominant language or the language explicitly requested. Keep technical terms, database names, trial IDs, gene/protein names, model names, benchmark names, and citation keys in their standard scholarly form.

File names must always use English ASCII slugs:

```text
hypothesis-2026-06-10-sclc-tarlatamab-pdl1.md
hypothesis-2026-06-10-ccta-diabetes.md
```

Use clean Markdown with stable headings, compact tables, and editable bullet lists. Keep chat turns short and decision-oriented, but make the saved report complete enough that a later agent can resume without replaying the whole conversation.

## Template Localization Rule

Use the bundled `references/hypothesis-output-template.md` as the structural template. The template may contain example headings, but every final report heading and field label must be localized to the detected output language. Keep only file names, source keys, database names, hypothesis IDs, citation metadata, and standard identifiers in English or their original language.

## When to Use

Use for:

- article-type empirical research;
- clinical, basic biomedical, materials/chemistry, AI/data science, social science, education/psychology, economics/finance, and engineering studies;
- turning a research gap into primary/secondary hypotheses;
- building mechanistic, causal, predictive, comparative, or intervention hypotheses;
- preparing handoff to study design or experiment design.

Do not force a "hypothesis" when the output type is:

- pure literature review;
- historiography or humanities argument where "thesis/proposition" is more appropriate;
- protocol-only work without a testable research claim;
- descriptive mapping work with no planned comparison, mechanism, prediction, or theory test.

For these cases, offer a "research proposition" or "analytical thesis" instead.

## Input

Accept:

- a research question;
- a `nnscholar1-1-question-mining` output;
- a `nnscholar1-2-literature-searching` output;
- a literature table;
- user constraints about article type, population/model/data, intervention/exposure, endpoints, methods, sample availability, or target journal.

The user may have multiple tasks in the same project. Do not assume the latest 1.1 or 1.2 file belongs to the current topic. Match local files to the user's topic before using them.

## Evidence Discovery and Fallback

When the user gives a topic/question but not exact file paths:

1. Search local project folders for likely evidence files.
2. Prefer `references/`, `reference/`, `docs/`, `outputs/`, and user-specified folders.
3. Use `rg --files` and targeted filename/content search.
4. Match candidate files by topic keywords, synonyms, date, and NNScholar stage.
5. Present the top 1-3 candidate evidence bundles and ask the user to confirm only if ambiguity remains.

Evidence priority:

1. Matching `nnscholar1-2-literature-searching` output for the same topic.
2. Matching `nnscholar1-1-question-mining` output for the same topic.
3. Local literature tables, summaries, protocols, or notes.
4. User-provided text in the current conversation.
5. If evidence is insufficient, ask to run or provide `1.2` before locking hypotheses.

Fallback behavior:

- If `1.1` is missing but `1.2` exists: proceed using `1.2` as the primary evidence source.
- If `1.2` is missing but `1.1` exists: draft only a provisional hypothesis map and recommend running `1.2` before locking.
- If both are missing but local project files exist: extract a provisional evidence base and clearly label it as local-file-based.
- If no evidence exists: ask the user to choose between running `1.2` first or generating a speculative preliminary hypothesis draft.

## Upstream Integration

When available, extract:

From `1.1 question mining`:

- research gap;
- recommended research question;
- recommended rationale;
- initial study route;
- directions not recommended.

From `1.2 literature searching`:

- core literature table;
- literature summary/review;
- evidence insufficiencies;
- research gaps;
- research idea or plan;
- key variables, endpoints, models, datasets, or study populations;
- citation list.

Build a compact evidence-to-hypothesis chain:

```text
Research gap -> Evidence anchors -> Missing mechanism/decision -> Testable hypothesis -> Required design
```

Keep this chain under 8 bullets in chat. Put detailed mapping in the saved report.

If the hypothesis conflicts with 1.1 or 1.2, flag it:

- repeats an already discouraged direction;
- ignores a major evidence gap;
- relies on weak or missing evidence;
- cannot be tested with available data/materials.

If the user only provides a topic and no suitable evidence file is found, ask for the minimum missing context:

1. article type or discipline;
2. intended study system/population/data;
3. whether they want clinical, mechanistic, predictive, or intervention hypotheses.

## Efficient Dialogue Rule

Use "micro-rounds" by default:

- Ask at most 1-3 questions per round.
- Offer compact choices when possible.
- Summarize state in a "working hypothesis card" after each major change.
- Do not repeat the full evidence base in every round.
- Maintain a revision ledger in the saved report, not in long chat messages.
- If context is long, use local file paths and section names instead of pasting content.

Working hypothesis card format:

```text
Current claim:
Study object:
Mechanism/path:
Primary measurable endpoint:
Main uncertainty:
Next decision needed:
```

## Interactive Dialogue Protocol

### Round 0: Evidence Location and Intake

First locate matching local evidence files unless the user supplied file paths.

Report briefly:

- selected 1.2 file, if found;
- selected 1.1 file, if found;
- other local files used;
- missing evidence.

Ask concise questions if missing:

- What article type is this? clinical article, basic biomedical article, AI article, social science article, etc.
- What is the study object? patient population, disease model, dataset, material system, cohort, intervention, or text corpus.
- Is the goal mechanism, prediction, comparison, intervention effect, association, or theory testing?

If the user has already provided enough context, proceed without asking.

### Round 1: Evidence-to-Hypothesis Mapping and Confirmation

Summarize:

- research question;
- key evidence anchors;
- known gaps;
- likely causal/mechanistic path;
- variables or constructs;
- available data/materials;
- constraints.

Ask the user to confirm or correct the framing before generating final hypotheses. Keep the summary under 8 bullets.

Socratic prompts:

- What phenomenon are we trying to explain or predict?
- Which part is most uncertain: mechanism, patient selection, intervention effect, measurement, or generalizability?
- What observation would make this idea fail?

### Round 2: Candidate Hypotheses

Generate 3-5 candidate hypotheses:

- one primary hypothesis;
- 2-4 secondary or alternative hypotheses;
- one null/negative hypothesis when appropriate;
- one risky or creative hypothesis if evidence supports plausibility.

Each candidate must include:

- hypothesis statement;
- hypothesis type;
- evidence basis;
- core assumptions;
- predicted observable result;
- required data/experiment;
- feasibility;
- main risk.

Use a compact table in chat. Put full details in the report.

### Round 3: Challenge and Revision

Before accepting the user's preferred hypothesis, challenge it:

- What alternative explanation could produce the same observation?
- Is the direction too obvious or too broad?
- Is the mechanism actually testable?
- Are key variables measurable?
- Is there a confounder, leakage, reverse causality, batch effect, or selection bias?
- Does the hypothesis overclaim beyond available evidence?

If the user pushes back, do not concede automatically. Concede only when their correction directly addresses the methodological or evidentiary concern.

Use one targeted challenge at a time when possible. Avoid broad lists unless the user asks for a full critique.

### Round 4: Hypothesis Quality Gate

Score each candidate from 1-5:

| Criterion | Meaning |
|---|---|
| Evidence groundedness | Is it anchored in cited literature or prior data? |
| Falsifiability | Could a realistic result disprove it? |
| Specificity | Are population/model, exposure/intervention, comparator, and outcome clear? |
| Mechanistic clarity | Is the proposed causal/mechanistic path explicit? |
| Measurability | Are variables, endpoints, readouts, or constructs measurable? |
| Feasibility | Can the study be done with available data/materials/time? |
| Novelty | Does it avoid merely restating existing findings? |
| Design readiness | Can it be handed to study design without major ambiguity? |

Flag any score under 3 and propose a revision.

Show only the final score table in chat. Put scoring rationale in the saved report.

### Round 5: Lock and Handoff

After user confirmation, save the final Markdown report to `references/` or `reference/`.

Use `references/hypothesis-output-template.md`.

The report must include:

- local evidence files used;
- final primary hypothesis;
- secondary hypotheses;
- null/alternative hypotheses;
- evidence-to-hypothesis chain;
- variables/readouts/endpoints;
- expected observations;
- disconfirming observations;
- quality gate scores;
- revision log;
- handoff to study design.

## Paper Structure Derivation

When the user asks to structure the paper, or when the task is article planning, derive a concise article skeleton from the locked hypothesis:

- Title direction;
- Introduction logic ending in the hypothesis;
- Methods modules required to test the hypothesis;
- Results figure/table sequence;
- Discussion claims, limitations, and next step.

Use this only after the hypothesis is stable enough. Do not generate a full manuscript outline before the core hypothesis is clear.

## Discipline-Specific Framing

| Discipline | Hypothesis shape |
|---|---|
| Clinical medicine | PICO/PECO: population, intervention/exposure, comparator, endpoint, time window, safety |
| Basic biomedicine | Model, perturbation, mechanism, readout, rescue/validation |
| Materials/chemistry | Composition/process -> structure -> property/performance -> mechanism |
| AI/data science | Dataset/task, model/intervention, baseline, metric, ablation, failure mode |
| Social science/education/psychology | Theory, population, construct, measurement, causal/associational path, confounders |
| Economics/finance | Identification strategy, treatment/exposure, outcome, mechanism, robustness |
| Engineering | System, control/input, performance metric, constraints, failure mode |
| Humanities/history | Research proposition or thesis, source base, interpretation, counter-argument |

## Hypothesis Types

Use one or more:

- causal hypothesis;
- mechanistic hypothesis;
- predictive hypothesis;
- comparative hypothesis;
- mediation/moderation hypothesis;
- intervention-effect hypothesis;
- dose-response hypothesis;
- non-inferiority/equivalence hypothesis;
- exploratory proposition.

## Guardrails

- Do not invent evidence or cite papers that were not retrieved or supplied.
- Do not use the wrong local 1.1/1.2 file just because it is recent.
- Do not convert every research question into a causal hypothesis.
- Do not confuse research objective, hypothesis, endpoint, and method.
- Do not write a hypothesis that cannot be falsified.
- Do not recommend experiments before the hypothesis is locked.
- Do not ignore negative, conflicting, or null evidence.
- Do not hide uncertainty; state weak links in the evidence chain.
- For clinical studies, separate efficacy, safety, and biomarker hypotheses.
- For mechanism studies, require perturbation and rescue/validation when possible.
- For AI studies, require baselines, metrics, ablations, and leakage checks.
- For social science, state theory, constructs, measurement, and confounders.
- If no 1.2 evidence exists, do not lock final hypotheses without clearly marking them provisional.
- If multiple matching evidence bundles exist, ask the user which bundle to use before final locking.

## Attribution Note

This skill was designed for NNScholar and is conceptually inspired by the human-in-the-loop, Socratic dialogue, checkpoints, and integrity-gate philosophy of Academic Research Skills by Cheng-I Wu:

https://github.com/Imbad0202/academic-research-skills
