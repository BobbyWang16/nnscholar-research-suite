---
name: nnscholar2-2-ars-plan
description: Use when NNScholar needs to design or lock a research scheme, study protocol, technical route, methods plan, statistical/experimental/computational analysis plan, or ARS plan. Prefer this skill after NNScholar 1.1 question mining, 1.2 literature searching, 1.3 hypothesis generation, 1.4 domain expert knowledge base, or 2.1 research planning outputs exist; also use it from scratch when the user only provides a topic, idea, hypothesis, dataset, or research objective.
---

# NNScholar 2.2 ARS Plan

This skill turns upstream research evidence or a fresh user idea into a defensible research scheme. It is stricter than project planning: it locks how the research will be done, not just when it will be done.

ARS means:

- `Aim`: research objective, question, hypothesis, and success criteria.
- `Route`: study design, technical route, data/experiment/computation path.
- `Specification`: samples, materials, variables, endpoints, methods, bias control, quality gates, and protocol lock.

Version: `0.2.0`. Stage: `research setting / ARS plan`. Legacy workflow alias: `$nnscholar2-2-ars-plan`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar2-2-ars-plan` / `/nnscholar2-2-ars-plan`.
- Keep the title format as `NNScholar 2.2 ARS Plan`.
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

Prefer upstream-linked planning. Before starting from scratch, look for NNScholar 1.1-1.4 and 2.1 outputs that match the current topic. Use them as the evidence base when available. If upstream artifacts conflict with the user's latest message, treat the latest message as active intent and record the conflict.

Do not produce a locked protocol when key design information is missing. Produce a provisional scheme, ask targeted questions, and mark which gates are not yet passed.

## When Starting

Classify the run mode:

| Mode | Trigger | Behavior |
|---|---|---|
| `linked` | Matching 1.1-1.4 or 2.1 outputs exist | Fuse upstream evidence and design a scheme from it |
| `partial` | Only some upstream evidence exists | Build a provisional scheme plus evidence gap table |
| `scratch` | No matching upstream evidence exists | Ask minimal intake questions, then create a provisional scheme |

If the user only clicks the button or gives a vague request, ask only:

1. What is the research question, hypothesis, or topic?
2. What data, samples, experiments, literature table, or knowledge base is already available?
3. What is the target output: paper, proposal, thesis, protocol, grant, algorithm benchmark, or internal scheme?

## Upstream Evidence Priority

Use upstream artifacts in this order:

1. `nnscholar1-3-hypothesis-generation`: locked hypothesis, mechanism, testable prediction, falsification rule.
2. `nnscholar1-2-literature-searching`: evidence base, method precedents, endpoints, controversies, comparison studies.
3. `nnscholar1-1-question-mining`: primary question, secondary questions, novelty rationale, scope.
4. `nnscholar1-4-domain-expert-knowledge-base`: domain constraints, terms, known risks, reviewer concerns.
5. `nnscholar2-1-research-planning`: timeline, milestones, available resources, known bottlenecks.
6. Current user message: latest active intent and constraints.

When exact files are not provided, search the current workspace for likely outputs by skill id, topic keywords, disease/model/dataset, date, and report headings. If multiple plausible bundles exist, show the top 1-3 choices and ask the user to confirm.

For detailed fusion rules, load `references/upstream-evidence-map.md`.

## Workflow

### Step 1: Intake and Evidence Map

Extract or ask for:

- research object and target output;
- primary question or hypothesis;
- available upstream reports and local materials;
- data/sample/material/corpus status;
- discipline and scheme type;
- design constraints, time window, ethics/privacy/licensing constraints.

Return a compact intake card before drafting a long scheme.

### Step 2: Select Scheme Type

Choose the scheme family before filling details:

- clinical or epidemiological study;
- basic/translational experiment;
- computational or AI benchmark;
- systematic review/meta-analysis;
- qualitative/social science study;
- theoretical/modeling study;
- mixed-methods project.

If the family is unclear, ask one question or propose 2-3 candidate routes with rejection criteria.

### Step 3: Build ARS

Build:

- `Aim`: objective, question, hypothesis, success criteria, falsification criteria.
- `Route`: design, population/materials/corpus, comparison/control, timeline logic, technical route.
- `Specification`: inclusion/exclusion, variables, endpoints, methods, analysis plan, quality control, bias control.

Keep the scheme specific enough that downstream writing, figure planning, and flowchart generation cannot silently change the design.

### Step 4: Gate the Scheme

Audit these gates:

| Gate | Question |
|---|---|
| Aim gate | Is the question specific and testable? |
| Evidence gate | Is the scheme grounded in upstream evidence or marked provisional? |
| Data/material gate | Are samples, datasets, materials, or corpora actually available? |
| Method gate | Does the method answer the question? |
| Measurement gate | Are exposure/intervention/grouping and outcomes measurable? |
| Analysis gate | Are statistics, experiments, or benchmarks compatible with data scale? |
| Bias gate | Are confounding, selection, information, leakage, or evaluator biases controlled? |
| Ethics gate | Are IRB, privacy, consent, licensing, and safety needs surfaced? |
| Lock gate | Is the scheme stable enough for downstream 2.3/2.4 work? |

If any critical gate fails, do not lock the protocol.

### Step 5: Output and Handoff

For short chats, return:

- upstream status;
- ARS card;
- scheme summary;
- unresolved gates;
- next 3 actions.

For full reports, use `references/ars-plan-output-template.md`. Localize headings to the user's language while preserving technical terms, model names, data fields, trial IDs, citations, and file paths.

Use `references/ars-plan-test-cases.md` for regression examples.

## Protocol Lock Rule

Only mark `Protocol status: locked` when:

- the user confirms the scheme;
- key variables, endpoints, data/materials, and methods are specified;
- major risks have mitigation;
- downstream writing and flowchart design can safely rely on the scheme.

Otherwise mark `Protocol status: provisional` and list the exact blockers.

Once locked, downstream skills should not add variables, change endpoints, alter analysis methods, or enlarge claims without reopening this skill.

## Non-goals

Do not:

- redo full literature search unless the user asks to return to `nnscholar1-2-literature-searching`;
- invent a hypothesis when 1.3 is missing; ask whether to run hypothesis generation or create a provisional aim;
- write manuscript prose;
- fabricate sample sizes, approvals, datasets, citations, or results;
- accept unrealistic methods or timelines without flagging feasibility risk.
