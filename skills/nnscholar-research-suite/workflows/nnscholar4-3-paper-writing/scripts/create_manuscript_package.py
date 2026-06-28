#!/usr/bin/env python
"""Create a standard manuscript drafting package for NNScholar 4.5."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


DEFAULT_SECTIONS = [
    "Title and Abstract",
    "Introduction",
    "Methods",
    "Results",
    "Discussion",
    "Conclusion",
]


def slugify(value: str) -> str:
    cleaned = []
    for char in value.lower():
        if char.isalnum():
            cleaned.append(char)
        elif cleaned and cleaned[-1] != "-":
            cleaned.append("-")
    slug = "".join(cleaned).strip("-")
    return slug[:60] or "manuscript"


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def create_package(args: argparse.Namespace) -> dict[str, str]:
    base = args.output_dir
    if args.use_date_slug:
        base = base / f"draft-{date.today().isoformat()}-{slugify(args.topic)}"
    base.mkdir(parents=True, exist_ok=True)

    sections = args.sections or DEFAULT_SECTIONS
    manifest = {
        "topic": args.topic,
        "article_type": args.article_type,
        "language": args.language,
        "target_venue": args.target_venue,
        "sections": sections,
    }

    write(
        base / "manuscript_brief.md",
        f"""# Manuscript Brief

Topic: {args.topic}
Article type: {args.article_type}
Language: {args.language}
Target venue/style: {args.target_venue or "[not specified]"}

## Core Story

- Working title:
- One-sentence storyline:
- Central contribution:
- Claim ceiling:
- Prohibited claims:

## Section Plan

| Section | Purpose | Source authority | Status |
|---|---|---|---|
"""
        + "\n".join(f"| {section} |  |  | placeholder |" for section in sections),
    )

    write(
        base / "manuscript_draft.md",
        "# Manuscript Draft\n\n" + "\n\n".join(f"## {section}\n\n[Draft placeholder]" for section in sections),
    )

    write(
        base / "section_claim_map.md",
        """# Section Claim Map

| Section | Claim | Evidence/source | Status |
|---|---|---|---|
|  |  |  | missing |
""",
    )

    write(
        base / "figure_table_callouts.md",
        """# Figure and Table Callouts

| Item | Placement | Supported claim | Caption/title | Status |
|---|---|---|---|---|
|  |  |  |  | missing |
""",
    )

    write(
        base / "missing_evidence_checklist.md",
        """# Missing Evidence Checklist

- Sample/data details:
- Statistics:
- Citations:
- Ethics/funding/data availability:
- Figure/table assets:
""",
    )

    write(
        base / "manuscript_audit.md",
        """# Manuscript Audit

## Claim-Evidence Audit

| Claim | Evidence/source | Status | Fix |
|---|---|---|---|
|  |  | missing |  |

## Methods-Results Consistency

| Methods item | Results counterpart | Status |
|---|---|---|
|  |  | missing |
""",
    )

    manifest_path = base / "source_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    return {item.name: str(item) for item in base.iterdir() if item.is_file()}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a manuscript drafting package.")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("manuscripts"))
    parser.add_argument("--article-type", default="original article")
    parser.add_argument("--language", default="Chinese")
    parser.add_argument("--target-venue", default="")
    parser.add_argument("--sections", nargs="*", default=None)
    parser.add_argument("--use-date-slug", action="store_true")
    return parser.parse_args()


def main() -> None:
    outputs = create_package(parse_args())
    print(json.dumps(outputs, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
