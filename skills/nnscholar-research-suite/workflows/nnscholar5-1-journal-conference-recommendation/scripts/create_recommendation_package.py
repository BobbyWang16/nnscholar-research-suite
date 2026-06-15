#!/usr/bin/env python
from __future__ import annotations

import argparse, json
from datetime import date
from pathlib import Path

def slugify(s: str) -> str:
    out = []
    for c in s.lower():
        if c.isalnum(): out.append(c)
        elif out and out[-1] != "-": out.append("-")
    return "".join(out).strip("-")[:60] or "submission"

def write(p: Path, text: str) -> None:
    p.write_text(text.rstrip() + "\n", encoding="utf-8")

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--output-dir", type=Path, default=Path("submission"))
    ap.add_argument("--discipline", default="")
    ap.add_argument("--priority", default="")
    ap.add_argument("--use-date-slug", action="store_true")
    args = ap.parse_args()
    base = args.output_dir / f"recommendation-{date.today().isoformat()}-{slugify(args.topic)}" if args.use_date_slug else args.output_dir
    base.mkdir(parents=True, exist_ok=True)
    write(base / "venue_shortlist.md", "# Venue Shortlist\n\n| Tier | Venue | Fit | Risk | Revision needed |\n|---|---|---|---|---|\n| Ambitious |  |  |  |  |\n| Balanced |  |  |  |  |\n| Safe/Fast |  |  |  |  |")
    write(base / "venue_comparison_matrix.md", "# Venue Comparison Matrix\n\n| Venue | Scope fit | Article fit | Fee/OA | Speed | Risk | Verify |\n|---|---|---|---|---|---|---|\n|  |  |  |  |  |  |  |")
    write(base / "revision_strategy.md", "# Revision Strategy\n\n- Title/abstract angle:\n- Methods/reporting changes:\n- Figure/table changes:\n- Claims to soften:\n- Missing information:")
    write(base / "author_decision_checklist.md", "# Author Decision Checklist\n\n- Preferred tier:\n- Fee constraints:\n- Speed constraints:\n- Indexing requirements:\n- Verification needed:")
    (base / "source_manifest.json").write_text(json.dumps(vars(args), indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(json.dumps({f.name: str(f) for f in base.iterdir() if f.is_file()}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
