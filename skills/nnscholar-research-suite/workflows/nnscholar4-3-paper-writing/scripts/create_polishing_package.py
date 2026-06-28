#!/usr/bin/env python
"""Create a standard manuscript polishing package for NNScholar 4.6."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    cleaned = []
    for char in value.lower():
        if char.isalnum():
            cleaned.append(char)
        elif cleaned and cleaned[-1] != "-":
            cleaned.append("-")
    return "".join(cleaned).strip("-")[:60] or "manuscript"


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def create_package(args: argparse.Namespace) -> dict[str, str]:
    base = args.output_dir
    if args.use_date_slug:
        base = base / f"polish-{date.today().isoformat()}-{slugify(args.topic)}"
    base.mkdir(parents=True, exist_ok=True)

    manifest = {
        "topic": args.topic,
        "mode": args.mode,
        "language": args.language,
        "target_venue": args.target_venue,
        "source": args.source,
    }

    write(
        base / "polished_manuscript.md",
        f"""# Polished Manuscript

Topic: {args.topic}
Mode: {args.mode}
Language: {args.language}
Target venue/style: {args.target_venue or "[not specified]"}
Source: {args.source or "[not specified]"}

## Polished Text

[Polished manuscript placeholder]
""",
    )

    write(
        base / "polishing_report.md",
        """# Polishing Report

## Scope

- Mode:
- Target style:
- Sections polished:
- Do-not-change items:

## Main Improvements

- 

## Remaining Risks

- 
""",
    )

    write(
        base / "change_summary.md",
        """# Change Summary

| Location | Original issue | Revision type | Reason |
|---|---|---|---|
|  |  | language / logic / structure / claim-softening |  |
""",
    )

    write(
        base / "author_queries.md",
        """# Author Queries

- [AUTHOR CHECK: confirm factual details before submission]
""",
    )

    write(
        base / "consistency_audit.md",
        """# Consistency Audit

## Terminology

- 

## Numbers and Statistics

- 

## Figure/Table Callouts

- 

## Methods-Results Alignment

- 
""",
    )

    write(
        base / "risky_claims.md",
        """# Risky Claims

| Claim | Risk | Suggested safer wording |
|---|---|---|
|  |  |  |
""",
    )

    (base / "source_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return {item.name: str(item) for item in base.iterdir() if item.is_file()}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a manuscript polishing package.")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("manuscripts"))
    parser.add_argument("--mode", default="logic", choices=["light", "logic", "deep", "venue", "reviewer-aware", "bilingual"])
    parser.add_argument("--language", default="Chinese")
    parser.add_argument("--target-venue", default="")
    parser.add_argument("--source", default="")
    parser.add_argument("--use-date-slug", action="store_true")
    return parser.parse_args()


def main() -> None:
    print(json.dumps(create_package(parse_args()), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
