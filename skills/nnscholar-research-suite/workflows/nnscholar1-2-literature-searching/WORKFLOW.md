---
name: nnscholar1-2-literature-searching
description: Use when NNScholar needs interactive literature searching, paper retrieval, source selection by discipline, citation verification, literature summaries, evidence tables, or review-style outputs after a topic or research question is chosen.
---

# NNScholar 1.2 Literature Searching

This skill performs interactive literature retrieval after a topic or research question is chosen. It selects search sources by discipline, retrieves and screens papers, verifies citations, condenses each paper into useful fields, and writes either a literature-review report or a research-oriented literature summary with study ideas.

Version: `0.2.0`. Stage: `literature / literature searching`. Legacy workflow alias: `$nnscholar1-2-literature-searching`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar1-2-literature-searching` / `/nnscholar1-2-literature-searching`.
- Keep the title format as `NNScholar 1.2 Literature Searching`.
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

This is a literature-search skill, not a question-mining skill. Do not make novelty/collision judgment the default center of the report. The default center is:

- where the literature was searched;
- which papers were found and why they matter;
- each paper's citation, source, methods/data, key findings, limits, and reuse value;
- a concise literature review;
- if the user is preparing a study, a research idea and plan based on the retrieved literature.

Every search must report databases or search sources used, exact search strings when available, date range, result counts when available, source/API limitations, and screening rules.

## Interactive Rule

If the user only provides a topic/question and asks to use this skill, ask the user to choose a search mode before running the search. Present the choices clearly:

1. `quick scan`: fast search for core papers.
2. `standard search`: balanced search for a research topic.
3. `review search`: literature-review-oriented search and synthesis.
4. `systematic-ready`: stricter search log and screening counts for scoping/systematic review preparation.

If the user already specifies a mode, do not ask again. If the runtime supports interactive choice UI, use it. Otherwise ask a short question in chat.

Only ask additional questions when the output purpose is ambiguous between:

- `research planning`: literature summary plus research gap, study idea, and plan;
- `literature review only`: literature review summary only, no research plan.

## Language, Filename, and Formatting Rule

Match the user's input language in all user-facing output. If the user writes in Chinese, output Chinese. If the user writes in English, output English. If the user mixes languages, use the dominant language or the language explicitly requested. Keep technical terms, database names, trial IDs, gene/protein names, model names, benchmark names, and citation keys in their standard scholarly form.

File names must always use English ASCII slugs, regardless of report language. Use lowercase words, hyphens, and no spaces, punctuation, Chinese characters, or special symbols.

Example:

```text
literature-search-2026-06-10-sclc-immunotherapy-maintenance.md
literature-search-2026-06-10-ccta-diabetes-risk.md
```

Use clean Markdown with stable headings, compact tables, and editable bullet lists. Keep the paper table concise but information-rich: one row should be enough for a future researcher to decide whether to re-read the source. Preserve the report section order unless the user requests a different structure.

## Template Localization Rule

Use the bundled `references/search-protocol-template.md` and `references/evidence-matrix-template.md` as structural templates. The templates may contain example headings, but every final report heading and field label must be localized to the detected output language. Keep only file names, source keys, database names, search strings, citation metadata, and standard identifiers in English or their original language.

## Input

Accept:

- a research question;
- a broad literature-review topic;
- the Agent Handoff from question mining;
- a full output file from `nnscholar1-1-question-mining`;
- optional time window;
- optional discipline, databases, inclusion/exclusion criteria, target output size, citation style, and output purpose.

If no time window is stated, use the question-mining handoff window when available; otherwise default to the past 5 years for fast-moving fields and past 10 years for clinical guideline/systematic evidence, while including seminal older papers when needed. State this choice in the report.

## Search Depth Modes

Ask the user to choose a mode unless they already specified one.

| Mode | Use when | Expected output |
|---|---|---|
| `quick scan` | User needs fast core literature | 10-25 core papers, concise table, short summary |
| `standard search` | User is preparing a research topic | 30-80 candidate records when available, screened core set, literature summary, research idea/plan if relevant |
| `review search` | User wants a literature-review task | Thematic review, representative evidence, citation-ready references, no forced research plan |
| `systematic-ready` | User needs scoping/systematic review preparation | Reproducible protocol, database logs, screening counts, exclusion categories |

## Workflow

### 1. Confirm Mode and Output Purpose

If not specified, ask for the mode. If the task could be either study planning or a literature review, ask whether the user wants:

- literature review only;
- literature review plus research idea/plan.

### 2. Build the Search Protocol

Use `references/search-protocol-template.md`.

Define:

- research question;
- search concepts and synonyms;
- inclusion/exclusion criteria;
- date range;
- study types required;
- databases and why each is needed;
- literature table fields.

When the input includes Agent Handoff from `nnscholar1-1-question-mining`, extract and preserve:

- primary question;
- search concepts;
- required study types;
- literature table fields;
- evidence that needs focused supplementation.

### 3. Translate Topic Into Search Concepts

For international scholarly databases, use English search concepts by default. For Chinese humanities, social science, education, psychology, policy, and China-focused questions, also use Chinese search terms for CNKI/Wanfang-style sources when accessible.

Include:

- exact phrases for the topic;
- standard abbreviations;
- synonyms and spelling variants;
- controlled vocabulary such as MeSH when useful;
- field tags such as Title/Abstract for PubMed;
- study, trial, drug, model, dataset, benchmark, molecule, or guideline names when known.

Record representative English and Chinese queries in the output as applicable.

### 4. Choose Search Sources by Discipline

| Discipline/need | First-pass sources | Notes |
|---|---|---|
| Clinical medicine | PubMed, ClinicalTrials.gov, FDA/EMA, guidelines, Cochrane when available, Semantic Scholar/OpenAlex | Prioritize databases and clinical trials; include regulatory/guideline sources when treatment decisions are involved |
| Basic biomedicine | PubMed as the primary source; add PMC/bioRxiv/medRxiv only when needed | Usually focus on PubMed first; distinguish human, animal, cell, organoid, omics, and mechanism evidence |
| AI and data science | Google Scholar-style web search, arXiv, Semantic Scholar, OpenAlex, Papers with Code or benchmark pages | Include datasets, baselines, metrics, ablations, code availability |
| Materials and chemistry | Crossref/OpenAlex/Semantic Scholar, domain journals, synthesis/performance benchmarks | Track synthesis route, characterization, comparator, reproducibility |
| Humanities and social sciences | CNKI/Wanfang when accessible, Google Scholar-style web search, Semantic Scholar, OpenAlex, books/reviews, archival catalogues | Use Chinese sources for China-focused topics; label paywalled or inaccessible sources |
| Economics and finance | Google Scholar-style web search, NBER/SSRN/RePEc when relevant, Semantic Scholar/OpenAlex | Track working papers separately from peer-reviewed papers |
| No clear disciplinary tendency | Google Scholar-style web search first, then Semantic Scholar/OpenAlex as fallback | State that the source choice is generic because no field signal was provided |

If a requested source such as Google Scholar, CNKI, or Wanfang is not directly accessible through available tools, use web search or accessible metadata pages as fallback and state the limitation.

### 5. Execute Search

Minimum expectations:

- Clinical topic: PubMed plus ClinicalTrials.gov; add guideline/regulatory sources when relevant.
- Basic biomedical topic: PubMed first; add preprints or broad scholarly sources only when the question requires newest mechanism data.
- AI/data science topic: arXiv plus Google Scholar-style web search and Semantic Scholar/OpenAlex.
- Humanities/social science topic: CNKI/Wanfang-style Chinese search when accessible, plus Semantic Scholar/OpenAlex and Google Scholar-style web search.
- No clear field: Google Scholar-style web search first, then Semantic Scholar/OpenAlex.

Record exact search strings, API endpoints or database names, date searched, result counts when available, and any failures. If only web search is used, do not claim the search is comprehensive; label it as a web-based rapid scan.

### 6. Dedupe and Rank

Deduplicate by DOI first, then PMID/PMCID/arXiv ID, then normalized title + year. Keep stable paper IDs.

Ranking should consider:

- direct relevance to the research question;
- study design quality;
- recency;
- citation influence;
- whether it is a trial, guideline, systematic review, benchmark, dataset, or mechanism paper;
- whether it is useful for the user's review or research plan.

### 7. Screen Relevance

Use two-stage screening:

1. Title/abstract screening.
2. Deep dive for high-priority papers.

Score papers against the specific question, not the broad topic. Record exclusion reasons.

Use this quality hierarchy unless the discipline requires a different one:

- A: guideline, regulatory document, pivotal RCT, systematic review/meta-analysis, validated benchmark/dataset, high-quality prospective study.
- B: strong cohort/registry, multi-center retrospective study, validated mechanism study, reproducible model or method paper.
- C: small sample, single-center, abstract-only, case series, preprint, exploratory mechanism study.
- Excluded: wrong disease/population/model/task, duplicate record, comment/news/editorial without data, inaccessible metadata, low relevance.

### 8. Retrieve Full Text or Open Access Version

For high-priority papers:

- check PMC for biomedical full text;
- use DOI/publisher page;
- use Unpaywall for OA copies;
- use arXiv/bioRxiv/medRxiv where appropriate;
- record when only abstract-level evidence is available.

### 9. Verify Citations and Apply Citation Style

Use DOI, PMID, PMCID, arXiv ID, Crossref, PubMed, or OpenAlex metadata. Do not invent missing metadata. Mark unresolved identifiers.

Use an appropriate citation style:

- Biomedical/clinical: Vancouver by default.
- Chinese humanities/social science/education: GB/T 7714 by default.
- AI/data science and general international topics: APA or ACM/IEEE when the user requests it; otherwise APA.
- If the user specifies a style, follow it.

### 10. Build the Literature Table

Use `references/evidence-matrix-template.md`.

The table must condense each paper, not merely list titles. Include citation, source, year, study type, population/system/data, methods, main findings, limitations, relevance to the topic, and reusable points.

For clinical topics, include PICO, endpoints, follow-up, safety, and guideline relevance. For basic science, include model, perturbation, readouts, mechanism, and validation. For AI, include dataset, baseline, metric, ablation, error modes, code/data availability, and reproducibility. For humanities/social science, include theory, data/source corpus, method, period/region, conclusion, and debate position.

### 11. Write Literature Review and Optional Research Plan

Default synthesis:

- If the user asks for literature review only, write a literature review organized by themes, evidence strength, disagreements, and limitations.
- If the user is preparing a study, write a literature summary plus research gaps, research idea, and a practical research plan.
- If the user explicitly asks for novelty/collision check, include it as an optional short section.

## Required Output

Save the final Markdown report to `references/` or `reference/`.

Suggested filename:

```text
literature-search-YYYY-MM-DD-short-topic.md
```

The report must include:

- search protocol;
- databases searched;
- source/API transparency and failures;
- exact search strings;
- result counts;
- deduplication summary;
- screening summary;
- quality grading summary;
- core literature table;
- citation-formatted reference list;
- literature summary/review;
- research gaps only when relevant to the user's task;
- research idea and plan only when the user is preparing a study;
- next recommended action.

## Guardrails

- Do not mix NSCLC/SCLC, adult/pediatric, preclinical/clinical, or benchmark/real-world evidence without labeling the distinction.
- Do not treat a review as primary evidence.
- Do not equate citation count with relevance.
- Do not claim comprehensive search if only web search was used.
- Do not omit negative or conflicting studies.
- Do not silently drop databases that failed; report failures and fallback searches.
- Do not proceed to literature synthesis before dedupe and relevance screening are documented.
- Do not use non-English database queries when English scholarly terms are needed for precision and recall.
- Do not make novelty/collision checking the default output unless the user asks for it or the source question explicitly requires it.
- Do not over-expand sources. Match the source strategy to the discipline and user's purpose.
