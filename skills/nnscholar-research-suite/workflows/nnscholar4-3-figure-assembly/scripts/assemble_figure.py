#!/usr/bin/env python
"""Assemble multi-panel scientific figures into a vector SVG wrapper.

The script is conservative by design:
- embeds source panels as self-contained SVG image elements;
- preserves aspect ratio inside each slot;
- adds panel labels and optional titles;
- exports PNG/PDF when cairosvg is available.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
import shutil
from pathlib import Path
from typing import Any


def mm_to_px(value_mm: float, dpi: int = 96) -> float:
    return value_mm / 25.4 * dpi


def data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(str(path))
    if path.suffix.lower() == ".svg":
        mime = "image/svg+xml"
    if mime is None:
        mime = "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if "panels" not in data or not isinstance(data["panels"], list) or not data["panels"]:
        raise ValueError("Manifest must contain a non-empty 'panels' list.")
    return data


def resolve_panel_path(manifest_path: Path, panel_path: str) -> Path:
    path = Path(panel_path)
    if not path.is_absolute():
        path = manifest_path.parent / path
    if not path.exists():
        raise FileNotFoundError(f"Panel file not found: {path}")
    return path.resolve()


def build_svg(manifest_path: Path, manifest: dict[str, Any], args: argparse.Namespace) -> str:
    panels = manifest["panels"]
    cols = int(manifest.get("cols") or args.cols or min(len(panels), 3))
    rows = int(manifest.get("rows") or args.rows or ((len(panels) + cols - 1) // cols))

    width_mm = float(manifest.get("width_mm") or args.width_mm)
    height_mm = float(manifest.get("height_mm") or args.height_mm)
    width = mm_to_px(width_mm)
    height = mm_to_px(height_mm)
    margin = float(manifest.get("margin") or args.margin)
    gutter = float(manifest.get("gutter") or args.gutter)
    label_size = float(manifest.get("label_size") or args.label_size)
    title_size = float(manifest.get("title_size") or args.title_size)
    font = str(manifest.get("font") or args.font)

    slot_w = (width - 2 * margin - (cols - 1) * gutter) / cols
    slot_h = (height - 2 * margin - (rows - 1) * gutter) / rows
    image_top_pad = label_size + 8

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width_mm}mm" height="{height_mm}mm" viewBox="0 0 {width:.2f} {height:.2f}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<style>text{{font-family:{html.escape(font)},Arial,Helvetica,sans-serif;fill:#111;}}</style>',
    ]

    for idx, panel in enumerate(panels):
        row = idx // cols
        col = idx % cols
        x = margin + col * (slot_w + gutter)
        y = margin + row * (slot_h + gutter)

        path = resolve_panel_path(manifest_path, panel["path"])
        label = str(panel.get("label") or chr(ord("A") + idx))
        title = str(panel.get("title") or "")
        uri = data_uri(path)

        parts.append(f'<g id="panel-{html.escape(label)}">')
        parts.append(
            f'<text x="{x:.2f}" y="{y + label_size:.2f}" font-size="{label_size:.2f}" font-weight="700">{html.escape(label)}</text>'
        )
        if title:
            parts.append(
                f'<text x="{x + label_size + 10:.2f}" y="{y + label_size:.2f}" font-size="{title_size:.2f}" font-weight="600">{html.escape(title)}</text>'
            )
        img_y = y + image_top_pad
        img_h = max(slot_h - image_top_pad, 8)
        parts.append(
            f'<image href="{uri}" x="{x:.2f}" y="{img_y:.2f}" width="{slot_w:.2f}" height="{img_h:.2f}" preserveAspectRatio="xMidYMid meet"/>'
        )
        if args.show_boxes:
            parts.append(
                f'<rect x="{x:.2f}" y="{img_y:.2f}" width="{slot_w:.2f}" height="{img_h:.2f}" fill="none" stroke="#ddd" stroke-width="1"/>'
            )
        parts.append("</g>")

    parts.append("</svg>")
    return "\n".join(parts)


def export_with_cairosvg(svg_path: Path, png_path: Path | None, pdf_path: Path | None, dpi: int) -> list[str]:
    outputs: list[str] = []
    try:
        import cairosvg  # type: ignore
    except Exception:
        return outputs

    if png_path is not None:
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), dpi=dpi)
        outputs.append(str(png_path))
    if pdf_path is not None:
        cairosvg.svg2pdf(url=str(svg_path), write_to=str(pdf_path), dpi=dpi)
        outputs.append(str(pdf_path))
    return outputs


def write_example_manifest(path: Path) -> None:
    example = {
        "width_mm": 180,
        "height_mm": 140,
        "cols": 2,
        "rows": 2,
        "panels": [
            {"label": "A", "path": "panel_a.svg", "title": "Study workflow"},
            {"label": "B", "path": "panel_b.png", "title": "Primary result"},
            {"label": "C", "path": "panel_c.png", "title": "Representative image"},
            {"label": "D", "path": "panel_d.svg", "title": "Quantification"},
        ],
    }
    path.write_text(json.dumps(example, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Assemble a multi-panel scientific figure.")
    parser.add_argument("--manifest", type=Path, help="JSON manifest with panel paths and layout.")
    parser.add_argument("--output-dir", type=Path, required=False)
    parser.add_argument("--basename", default="assembled_figure")
    parser.add_argument("--width-mm", type=float, default=180)
    parser.add_argument("--height-mm", type=float, default=140)
    parser.add_argument("--cols", type=int, default=None)
    parser.add_argument("--rows", type=int, default=None)
    parser.add_argument("--margin", type=float, default=24)
    parser.add_argument("--gutter", type=float, default=18)
    parser.add_argument("--label-size", type=float, default=20)
    parser.add_argument("--title-size", type=float, default=12)
    parser.add_argument("--font", default="Arial")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--formats", default="svg,png,pdf")
    parser.add_argument("--show-boxes", action="store_true")
    parser.add_argument("--write-example-manifest", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.write_example_manifest:
        write_example_manifest(args.write_example_manifest)
        print(json.dumps({"example_manifest": str(args.write_example_manifest)}, indent=2))
        return

    if not args.manifest:
        raise ValueError("--manifest is required unless --write-example-manifest is used.")
    manifest_path = args.manifest.resolve()
    manifest = load_manifest(manifest_path)
    output_dir = (args.output_dir or manifest_path.parent).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    svg = build_svg(manifest_path, manifest, args)
    svg_path = output_dir / f"{args.basename}.svg"
    svg_path.write_text(svg, encoding="utf-8")

    copied_manifest = output_dir / "layout_manifest.json"
    if copied_manifest.resolve() != manifest_path:
        shutil.copy2(manifest_path, copied_manifest)

    formats = {item.strip().lower() for item in args.formats.split(",") if item.strip()}
    outputs = [str(svg_path)]
    png_path = output_dir / f"{args.basename}.png" if "png" in formats else None
    pdf_path = output_dir / f"{args.basename}.pdf" if "pdf" in formats else None
    outputs.extend(export_with_cairosvg(svg_path, png_path, pdf_path, args.dpi))

    report = {
        "svg": str(svg_path),
        "outputs": outputs,
        "manifest": str(copied_manifest),
        "pdf_png_exported": any(path.endswith((".png", ".pdf")) for path in outputs),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
