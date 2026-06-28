---
name: nnscholar1-1-question-mining
description: Use when NNScholar needs evidence-grounded research question mining, research gap discovery, topic refinement, novelty-first candidate questions, or an agent handoff before full literature search.
---

# NNScholar 1.1 Question Mining

This skill turns a broad research direction into evidence-grounded, novelty-prioritized research questions. It must not invent questions directly from intuition. It first performs a rapid evidence scan, then mines hotspots, controversies, and gaps, and finally hands the strongest question to the literature-search stage.

Version: `0.2.0`. Stage: `literature / question mining`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id and folder name as `nnscholar1-1-question-mining` / `/nnscholar1-1-question-mining`.
- Keep the title format as `NNScholar 1.1 Question Mining`.
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

Accept free-form input. If the user states a time window, use it. If no time window is stated, default to the past 3 years and say so in the output. Only ask a clarifying question when the topic itself is too ambiguous to search responsibly.

## Language, Filename, and Formatting Rule

Match the user's input language in all user-facing output. If the user writes in Chinese, output Chinese. If the user writes in English, output English. If the user mixes languages, use the dominant language or the language explicitly requested. Keep technical terms, database names, trial IDs, gene/protein names, model names, benchmark names, and citation keys in their standard scholarly form.

File names must always use English ASCII slugs, regardless of report language. Use lowercase words, hyphens, and no spaces, punctuation, Chinese characters, or special symbols.

Example:

```text
question-mining-2026-06-10-sclc-immunotherapy.md
question-mining-2026-06-10-ccta-diabetes.md
```

Use clean Markdown with stable headings, compact tables, and editable bullet lists. Avoid dense paragraphs when a table would make later correction easier. Preserve the same section order as the output template unless the user requests a different structure.

## Template Localization Rule

Use the bundled `references/question-mining-output-template.md` as the structural template. The template may contain example headings, but every final report heading and field label must be localized to the detected output language. Keep only file names, source keys, database names, search strings, and citation metadata in English or their original language.

## Workflow

1. Parse the user's topic, discipline, constraints, and time window.
2. Detect output language and create an English ASCII filename slug.
3. Convert the topic into 2-4 English search concept groups and synonyms.
4. Write search terms carefully using controlled vocabulary, abbreviations, Boolean operators, field tags, and phrase quotes when appropriate.
5. Run a rapid evidence scan using sources appropriate to the discipline.
6. Evaluate search results for quality and keep only important, reliable references.
7. Separate active hotspots from true research gaps.
8. Rank gaps by novelty first, then feasibility and research value.
9. Produce one primary recommended question and 2-4 secondary questions.
10. Save the final Markdown output to the project `references/` folder.

## Search Query Rule

Even when the final output is Chinese or another language, literature searching should use English search concepts and English database queries by default. Translate user topics into precise English search terms before searching.

Search terms should include:

- exact phrases for the core topic, such as `"small-cell lung cancer"` or `"coronary CT angiography"`;
- standard abbreviations, such as `SCLC`, `CCTA`, `RAG`, `m6A`;
- synonyms and spelling variants connected with `OR`;
- focused relationships connected with `AND`;
- exclusions with `NOT` only when necessary;
- PubMed field tags or MeSH terms for biomedical searches when useful;
- trial, guideline, benchmark, dataset, or molecular target names when known.

Record the English search concepts and representative search strings in the output document.

## Evidence Quality Rule

Do not treat all search results as equal. Evaluate and filter results before using them as evidence anchors.

Prioritize:

- guidelines, consensus statements, and regulatory documents;
- systematic reviews and meta-analyses;
- pivotal RCTs and major prospective studies;
- high-quality cohort studies or registries;
- highly relevant mechanism papers with clear validation;
- benchmark/dataset papers for AI and data science;
- registered trials for active or emerging clinical directions.

Down-rank or exclude:

- low-relevance search hits;
- editorials, news, comments, narrative pieces without evidence, unless used only for context;
- papers from the wrong disease, population, organism, model, or task;
- studies with tiny samples and no validation, unless the topic is rare and uncertainty is stated;
- duplicated records, preprint/published duplicates, and citation-only pages;
- papers whose claims are not supported by accessible metadata, abstract, or full text.

The output must include a short "search result quality screening" note: what was kept, what was excluded, and why.

## Source Selection

| Discipline | First-pass sources |
|---|---|
| Clinical medicine | PubMed, guidelines, systematic reviews, major trials, ClinicalTrials.gov, real-world studies |
| Basic biomedicine | PubMed, reviews, mechanism papers, single-cell/spatial datasets, disease model studies |
| AI and data science | arXiv, Semantic Scholar, OpenAlex, benchmark papers, dataset/model cards, reproducibility studies |
| Materials and chemistry | Recent reviews, primary experiments, synthesis/performance benchmarks, characterization papers |
| Social science, education, psychology | Reviews, meta-analyses, theory papers, validated scales, longitudinal datasets |
| Humanities and history | Historiography reviews, primary source collections, archival notes, methodological debates |

## Novelty Policy

Innovation is the first ranking principle. Prefer questions that combine:

- emerging methods;
- under-tested populations or systems;
- new data types;
- longitudinal or real-world evidence;
- mechanism-to-translation bridges;
- cross-field method transfer.

Speculative questions are allowed when evidence suggests plausibility, but uncertainty and feasibility risks must be explicit.

## Supervisor Guardrail Integration

For AI/data-science, database, systems, ML, NLP, benchmark/evaluation, or
technical CS topics, read
`../../references/supervisor-research-guardrails.md` and apply the Idea
Evaluation Gate before recommending the primary question. Add the strongest
dimension signals and any fatal-flaw warning to the recommendation rationale.
If the topic is explicitly a benchmark or dataset paper, also apply the
Benchmark Paper Gate when judging whether the proposed gap is substantive.

If the proposed topic requires iterative model training, autonomous experiments,
RAG/agent evaluation, or benchmark optimization, also read
`../../references/ai-research-engineering-guardrails.md` and include the likely
Two-Loop Research Cycle, initial benchmark metric, and minimum evidence artifacts
needed before downstream design.

## Required Output

Use the template in `references/question-mining-output-template.md`.

The final document must contain:

- evidence scan;
- hotspots/controversies;
- research gaps;
- one primary recommended question;
- 2-4 secondary recommended questions;
- recommendation rationale;
- main research route;
- Agent Handoff.

## Agent Handoff

The handoff must prepare the next stage. Do not merely say "do literature review next."

It must specify:

- the primary question;
- that the next step is to search all literature directly related to that question;
- search concepts;
- recommended databases and sources;
- study types that must be included;
- evidence matrix fields;
- the search goal: novelty check, direct collision detection, and readiness for study design;
- concrete topics or directions not recommended for immediate research, with reasons, why they waste effort, and safer reframings.

## Save Rule

Save outputs to:

1. `references/` if it exists;
2. `reference/` if that is the established project folder;
3. otherwise create `references/`.

Suggested filename:

```text
question-mining-YYYY-MM-DD-short-topic.md
```

The `short-topic` must be an English ASCII slug.

## Guardrails

- Do not call a hot topic a gap unless the missing evidence is specific.
- Do not claim novelty without checking recent studies and registered/preprint work where relevant.
- Do not invent citations, trials, datasets, guidelines, or benchmark names.
- Do not use non-English database queries when English scholarly terms are needed for better recall and precision.
- Do not cite low-quality or off-topic search results as evidence anchors.
- Do not include search hits from a neighboring field unless the distinction is explicitly labeled.
- Do not recommend only safe incremental questions when a better novel angle is evidence-supported.
- For clinical topics, prefer PICO/PECO framing and state endpoint definitions.
- For mechanism biology, include model, perturbation, readout, and validation logic.
- For AI topics, include dataset, baseline, metric, ablation, and failure-mode analysis.
