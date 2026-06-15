#!/usr/bin/env python
from __future__ import annotations

import argparse, json
from datetime import date
from pathlib import Path

def slugify(s: str) -> str:
    out=[]
    for c in s.lower():
        if c.isalnum(): out.append(c)
        elif out and out[-1] != "-": out.append("-")
    return "".join(out).strip("-")[:60] or "portal"

def w(p: Path,t: str)->None: p.write_text(t.rstrip()+"\n",encoding="utf-8")

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--topic",required=True)
    ap.add_argument("--portal",default="")
    ap.add_argument("--venue",default="")
    ap.add_argument("--output-dir",type=Path,default=Path("submission"))
    ap.add_argument("--use-date-slug",action="store_true")
    args=ap.parse_args()
    base=args.output_dir / f"portal-{date.today().isoformat()}-{slugify(args.topic)}" if args.use_date_slug else args.output_dir
    base.mkdir(parents=True,exist_ok=True)
    w(base/"portal_step_plan.md","# Portal Step Plan\n\n1. Login manually.\n2. Start new submission.\n3. Enter metadata.\n4. Upload files.\n5. Complete declarations.\n6. Review proof.\n7. Human confirms final submit.")
    w(base/"portal_field_answers.md","# Portal Field Answers\n\n- Title:\n- Abstract:\n- Keywords:\n- Article type:\n- Authors:\n- Declarations:")
    w(base/"upload_file_manifest.md","# Upload File Manifest\n\n| File | Portal role | Status |\n|---|---|---|\n|  |  |  |")
    w(base/"human_only_actions.md","# Human-Only Actions\n\n- Password/login\n- Copyright/license agreement\n- Publication fee approval\n- COI certification\n- Final Submit")
    w(base/"final_confirmation_checklist.md","# Final Human Confirmation Checklist\n\n- All files correct\n- Declarations accurate\n- Authors approve\n- Fees/copyright understood\n- Final submit approved by human")
    (base/"source_manifest.json").write_text(json.dumps(vars(args),indent=2,ensure_ascii=False,default=str),encoding="utf-8")
    print(json.dumps({f.name:str(f) for f in base.iterdir() if f.is_file()},indent=2,ensure_ascii=False))

if __name__=="__main__": main()
