# Image2 Prompt Template

Use this template to convert a scientific visual blueprint into an Image2-ready prompt.

## Prompt Package

```text
Use case: scientific-educational / infographic-diagram
Asset type: publication schematic figure for [journal/conference/manuscript]
Primary request: Create a clean scientific schematic showing [core message].

Canvas and layout:
- Aspect ratio: [landscape 16:9 / square 1:1 / portrait / double-column figure].
- Layout: [left-to-right / top-to-bottom / three-panel / central mechanism with side inputs].
- White or very light background, no decorative texture.

Scientific content:
- Include these components: [component list].
- Show these relationships/arrows: [relationship list].
- Required labels: [short labels only].
- If labels are many, use numbered callouts and leave detailed wording for the caption.

Visual style:
- Publication-ready scientific illustration.
- Clean vector-like shapes, crisp arrows, high contrast, balanced spacing.
- Colorblind-friendly palette with restrained colors.
- Consistent icon style and no 3D clutter unless requested.

Accuracy constraints:
- Do not add unrequested molecules, organs, model modules, patient groups, datasets, or mechanisms.
- Do not imply causality beyond the supplied study design.
- Keep the figure schematic, not photorealistic, unless explicitly requested.

Text policy:
- Render only the short labels exactly as provided.
- No extra words, no watermark, no fake axes, no fake citations.
```

## Negative Constraints

Add when relevant:

```text
Avoid: tiny unreadable labels, dense paragraphs, decorative icons, stock-photo style, random DNA helices, fake UI panels, unnecessary 3D render, blurry arrows, misspelled labels, inconsistent colors, extra objects.
```

## Label Strategy

Prefer:

- 3-8 short labels in the image;
- numbered callouts for complex diagrams;
- full terminology in caption/legend;
- no p values, references, detailed equations, or long endpoint names inside the raster image.

## Revision Prompt

For one targeted iteration:

```text
Revise the previous scientific schematic. Keep the same layout, style, colors, and all correct components. Change only: [specific change]. Preserve these labels exactly: [labels]. Do not add new elements.
```

