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
    return "".join(out).strip("-")[:60] or "finalization"

def w(p: Path, t: str) -> None: p.write_text(t.rstrip() + "\n", encoding="utf-8")

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--venue", default="")
    ap.add_argument("--output-dir", type=Path, default=Path("submission"))
    ap.add_argument("--use-date-slug", action="store_true")
    args = ap.parse_args()
    base = args.output_dir / f"finalization-{date.today().isoformat()}-{slugify(args.topic)}" if args.use_date_slug else args.output_dir
    base.mkdir(parents=True, exist_ok=True)
    w(base/"finalization_checklist.md", "# Finalization Checklist\n\n- Target venue:\n- Article type:\n- Abstract:\n- Main manuscript:\n- Figures/tables:\n- Supplementary files:\n- Statements:\n- Reporting checklist:")
    w(base/"required_edits.md", "# Required Edits\n\n| Item | Problem | Required action | Blocker |\n|---|---|---|---|\n|  |  |  |  |")
    w(base/"submission_file_manifest.md", "# Submission File Manifest\n\n| File | Role | Required | Status |\n|---|---|---|---|\n|  |  |  |  |")
    w(base/"author_queries.md", "# Author Queries\n\n- [AUTHOR CHECK: confirm all declarations before submission]")
    w(base/"compliance_report.md", "# Compliance Report\n\n## Pass\n\n## Needs Revision\n\n## Blockers\n")
    (base/"source_manifest.json").write_text(json.dumps(vars(args), indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(json.dumps({f.name: str(f) for f in base.iterdir() if f.is_file()}, indent=2, ensure_ascii=False))

if __name__ == "__main__": main()
