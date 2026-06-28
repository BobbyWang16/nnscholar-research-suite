# Assembly Router

Use this file to choose a multi-panel figure layout.

## Figure Intent

| Intent | Recommended layout | Notes |
|---|---|---|
| Figure 1 overview | hero schematic + workflow/data source panels | Usually combines 4.2 schematic with cohort/design or pipeline panels |
| Main result | hero result + validation/robustness panels | Put the strongest result where the reader sees it first |
| Mechanism validation | schematic + experimental image + quantification | Keep representative images paired with quantification |
| Model paper result | architecture + benchmark + ablation + error/case | Separate method explanation from performance evidence |
| Materials paper result | synthesis + morphology + characterization + performance | Respect scale bars and instrument labels |
| Supplementary figure | balanced grid | Prioritize completeness over visual drama |

## Layout Patterns

### Balanced Grid

Use when panels have similar importance.

- 2 panels: 1x2 or 2x1.
- 3 panels: 1x3 for comparable plots; 2x2 with one blank/large panel only if story requires it.
- 4 panels: 2x2.
- 5-6 panels: 2x3.
- 7-9 panels: 3x3, usually supplementary.

### Hero + Evidence

Use when one panel explains the story and smaller panels validate it.

- A large left/top panel: schematic, architecture, or main result.
- Smaller right/bottom panels: plots, images, subgroup checks.
- Good for Figure 1 or main result figures.

### Narrative Route

Use when the reader should follow a process.

- Left-to-right for pipeline and model workflow.
- Top-to-bottom for experimental sequence or patient pathway.
- Use arrows only if the relationship is procedural or causal by design.

## Sizing Defaults

- Single-column figure: width 85 mm.
- Double-column figure: width 170-180 mm.
- Full-page figure: width 180 mm, height up to 220-240 mm.
- Poster/slide: use 16:9 or square as requested.

Use 300 dpi preview PNG and vector SVG/PDF for manuscript assembly.

