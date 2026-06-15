from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SUITE_ROOT = REPO_ROOT / "skills" / "nnscholar-research-suite"
WORKFLOWS_ROOT = SUITE_ROOT / "workflows"

EXPECTED_WORKFLOWS = [
    "nnscholar1-1-question-mining",
    "nnscholar1-2-literature-searching",
    "nnscholar1-3-hypothesis-generation",
    "nnscholar1-4-domain-expert-knowledge-base",
    "nnscholar2-1-research-planning",
    "nnscholar2-2-ars-plan",
    "nnscholar2-3-paper-architecture",
    "nnscholar2-4-flowchart-design",
    "nnscholar3-1-experiment-validation-plan",
    "nnscholar4-1-data-figure",
    "nnscholar4-2-image-schematic",
    "nnscholar4-3-figure-assembly",
    "nnscholar4-4-table-formatting",
    "nnscholar4-5-manuscript-drafting",
    "nnscholar4-6-manuscript-polishing",
    "nnscholar5-1-journal-conference-recommendation",
    "nnscholar5-2-submission-finalization",
    "nnscholar5-3-submission-portal-workflow",
    "nnscholar5-4-cover-letter",
    "nnscholar5-5-reviewer-response",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip()
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


class SuiteStructureTest(unittest.TestCase):
    def test_single_root_skill(self) -> None:
        skill_files = sorted(path.relative_to(REPO_ROOT).as_posix() for path in (REPO_ROOT / "skills").rglob("SKILL.md"))
        self.assertEqual(skill_files, ["skills/nnscholar-research-suite/SKILL.md"])

        root_skill = SUITE_ROOT / "SKILL.md"
        meta = frontmatter(read_text(root_skill))
        self.assertEqual(meta.get("name"), "nnscholar-research-suite")
        self.assertEqual(meta.get("user-invocable"), "true")

    def test_manifest_matches_workflows(self) -> None:
        manifest = json.loads(read_text(SUITE_ROOT / "manifest.json"))
        self.assertEqual(manifest["name"], "nnscholar-research-suite")
        self.assertEqual(manifest["workflows"], EXPECTED_WORKFLOWS)

        workflow_dirs = sorted(path.name for path in WORKFLOWS_ROOT.iterdir() if path.is_dir())
        self.assertEqual(workflow_dirs, EXPECTED_WORKFLOWS)

    def test_workflow_entry_files(self) -> None:
        for workflow_id in EXPECTED_WORKFLOWS:
            workflow_dir = WORKFLOWS_ROOT / workflow_id
            workflow_file = workflow_dir / "WORKFLOW.md"
            self.assertTrue(workflow_file.exists(), f"missing {workflow_file}")
            self.assertFalse((workflow_dir / "SKILL.md").exists(), f"internal workflow must not expose SKILL.md: {workflow_id}")

            meta = frontmatter(read_text(workflow_file))
            self.assertEqual(meta.get("name"), workflow_id)
            self.assertTrue(meta.get("description"), f"missing description for {workflow_id}")

    def test_root_router_covers_every_workflow(self) -> None:
        root_text = read_text(SUITE_ROOT / "SKILL.md")
        for workflow_id in EXPECTED_WORKFLOWS:
            self.assertIn(f"/{workflow_id}", root_text)
            self.assertIn(f"workflows/{workflow_id}/WORKFLOW.md", root_text)

    def test_referenced_local_files_exist(self) -> None:
        local_ref = re.compile(r"`?((?:references|scripts)/[A-Za-z0-9._/-]+\.(?:md|py|json|yaml|yml|txt|csv))`?")
        for workflow_id in EXPECTED_WORKFLOWS:
            workflow_dir = WORKFLOWS_ROOT / workflow_id
            workflow_text = read_text(workflow_dir / "WORKFLOW.md")
            for match in local_ref.finditer(workflow_text):
                rel = match.group(1).rstrip(".,;:)")
                path = workflow_dir / rel
                self.assertTrue(path.exists(), f"{workflow_id} references missing file {rel}")

    def test_no_stale_workflow_names(self) -> None:
        stale_names = [
            "nnscholar2-2-research-scheme",
        ]
        all_text = "\n".join(read_text(path) for path in SUITE_ROOT.rglob("*") if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".py"})
        for stale_name in stale_names:
            self.assertNotIn(stale_name, all_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
