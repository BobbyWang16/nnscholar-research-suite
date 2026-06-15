#!/usr/bin/env python
from __future__ import annotations

import argparse, json
from datetime import date
from pathlib import Path

def slugify(s: str)->str:
    out=[]
    for c in s.lower():
        if c.isalnum(): out.append(c)
        elif out and out[-1] != "-": out.append("-")
    return "".join(out).strip("-")[:60] or "cover-letter"

def w(p:Path,t:str)->None: p.write_text(t.rstrip()+"\n",encoding="utf-8")

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--topic",required=True)
    ap.add_argument("--venue",default="")
    ap.add_argument("--output-dir",type=Path,default=Path("submission"))
    ap.add_argument("--use-date-slug",action="store_true")
    args=ap.parse_args()
    base=args.output_dir / f"cover-letter-{date.today().isoformat()}-{slugify(args.topic)}" if args.use_date_slug else args.output_dir
    base.mkdir(parents=True,exist_ok=True)
    w(base/"cover_letter.md","# Cover Letter\n\nDear Editor,\n\n[Cover letter draft]\n\nSincerely,\n\n[Corresponding author]")
    w(base/"cover_letter_short.md","# Short Cover Letter\n\n[Concise version]")
    w(base/"editorial_pitch.md","# Editorial Pitch\n\n- Core problem:\n- Contribution:\n- Venue fit:\n- Reader value:")
    w(base/"declaration_checklist.md","# Declaration Checklist\n\n- Originality:\n- No concurrent submission:\n- Ethics:\n- COI:\n- Funding:\n- Data/code availability:")
    w(base/"author_queries.md","# Author Queries\n\n- [AUTHOR CHECK: confirm declarations and corresponding author details]")
    (base/"source_manifest.json").write_text(json.dumps(vars(args),indent=2,ensure_ascii=False,default=str),encoding="utf-8")
    print(json.dumps({f.name:str(f) for f in base.iterdir() if f.is_file()},indent=2,ensure_ascii=False))

if __name__=="__main__": main()
