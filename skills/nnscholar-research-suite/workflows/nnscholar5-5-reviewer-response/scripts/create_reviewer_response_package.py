#!/usr/bin/env python
from __future__ import annotations

import argparse, json
from datetime import date
from pathlib import Path

def slugify(s:str)->str:
    out=[]
    for c in s.lower():
        if c.isalnum(): out.append(c)
        elif out and out[-1] != "-": out.append("-")
    return "".join(out).strip("-")[:60] or "reviewer-response"

def w(p:Path,t:str)->None: p.write_text(t.rstrip()+"\n",encoding="utf-8")

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--topic",required=True)
    ap.add_argument("--decision",default="")
    ap.add_argument("--output-dir",type=Path,default=Path("submission"))
    ap.add_argument("--use-date-slug",action="store_true")
    args=ap.parse_args()
    base=args.output_dir / f"reviewer-response-{date.today().isoformat()}-{slugify(args.topic)}" if args.use_date_slug else args.output_dir
    base.mkdir(parents=True,exist_ok=True)
    w(base/"reviewer_comment_matrix.md","# Reviewer Comment Matrix\n\n| ID | Comment | Type | Required action | Status |\n|---|---|---|---|---|\n|  |  |  |  |  |")
    w(base/"response_strategy.md","# Response Strategy\n\n| ID | Strategy | Manuscript change | Evidence | Risk |\n|---|---|---|---|---|\n|  |  |  |  |  |")
    w(base/"point_by_point_response.md","# Point-by-Point Response\n\nDear Editor and Reviewers,\n\n[Response draft]")
    w(base/"revision_summary_table.md","# Revision Summary Table\n\n| Change | Location | Reason |\n|---|---|---|\n|  |  |  |")
    w(base/"manuscript_change_checklist.md","# Manuscript Change Checklist\n\n- ")
    w(base/"tone_and_risk_audit.md","# Tone and Risk Audit\n\n- Tone:\n- Unsupported promises:\n- Missing responses:\n- Location mismatches:")
    w(base/"author_queries.md","# Author Queries\n\n- [AUTHOR CHECK: confirm completed changes before claiming them]")
    (base/"source_manifest.json").write_text(json.dumps(vars(args),indent=2,ensure_ascii=False,default=str),encoding="utf-8")
    print(json.dumps({f.name:str(f) for f in base.iterdir() if f.is_file()},indent=2,ensure_ascii=False))

if __name__=="__main__": main()
