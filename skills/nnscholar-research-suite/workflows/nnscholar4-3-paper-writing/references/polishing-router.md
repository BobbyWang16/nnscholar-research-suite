# Polishing Router

Choose the polishing mode before editing.

## Modes

| Mode | Use when | Main output |
|---|---|---|
| `light` | Text is structurally sound but needs grammar, concision, and academic tone | Polished text + brief change summary |
| `logic` | Paragraphs feel repetitive, weakly connected, or unclear | Polished text + flow notes |
| `deep` | Section order, argument hierarchy, or story logic needs revision | Revised structure + polished section |
| `venue` | User provides journal/conference style or word limit | Venue-adapted text + compliance notes |
| `reviewer-aware` | User provides reviewer comments or revision goal | Revised text + response-relevant change summary |
| `bilingual` | Chinese-English translation polishing or English rewrite from Chinese | Polished English + source meaning notes |

## Default

- For pasted paragraph: use `light` unless user asks for deeper revision.
- For Introduction/Discussion: use `logic` by default.
- For Abstract/Title: use `venue` when target journal or word limit is known.
- For Results/Methods: use conservative `light` unless technical inconsistencies are found.
- For full manuscript: use `logic` plus consistency audit.

## Red Flags

Pause or flag before rewriting if the text includes:

- unsupported causal language;
- changed endpoint definitions;
- inconsistent sample sizes;
- p values or confidence intervals that conflict with tables/figures;
- missing ethics/data availability;
- claims stronger than 2.3/4.5 allowed claim ceiling.

