from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SUITE_ROOT = REPO_ROOT / "skills" / "nnscholar-research-suite"
WORKFLOWS_ROOT = SUITE_ROOT / "workflows"
ATLAS_PATH = SUITE_ROOT / "references" / "zotero-example-atlas.md"
FIGURE_GALLERY_PATH = SUITE_ROOT / "references" / "figure-screenshot-gallery.md"
FIGURE_ASSET_ROOT = SUITE_ROOT / "assets" / "zotero-figure-examples"
FIGURE_ASSET_MANIFEST = FIGURE_ASSET_ROOT / "manifest.json"

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


def markdown_section(text: str, heading: str) -> str | None:
    pattern = rf"^### {re.escape(heading)}\s*\n(?P<body>.*?)(?=^### |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if match is None:
        return None
    return match.group("body")


LOCAL_REF_RE = re.compile(r"`?((?:references|scripts)/[A-Za-z0-9._/-]+\.(?:md|py|json|yaml|yml|txt|csv))`?")


class SuiteStructureTest(unittest.TestCase):
    def test_single_root_skill(self) -> None:
        skill_files = sorted(path.relative_to(REPO_ROOT).as_posix() for path in (REPO_ROOT / "skills").rglob("SKILL.md"))
        self.assertEqual(skill_files, ["skills/nnscholar-research-suite/SKILL.md"])

        root_skill = SUITE_ROOT / "SKILL.md"
        meta = frontmatter(read_text(root_skill))
        self.assertEqual(meta.get("name"), "nnscholar-research-suite")
        self.assertEqual(set(meta), {"name", "description"})

    def test_manifest_matches_workflows(self) -> None:
        manifest = json.loads(read_text(SUITE_ROOT / "manifest.json"))
        version = read_text(REPO_ROOT / "VERSION").strip()
        self.assertEqual(manifest["name"], "nnscholar-research-suite")
        self.assertEqual(manifest["adapter_version"], version)
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
        root_text = read_text(SUITE_ROOT / "SKILL.md")
        for match in LOCAL_REF_RE.finditer(root_text):
            rel = match.group(1).rstrip(".,;:)")
            path = SUITE_ROOT / rel
            self.assertTrue(path.exists(), f"root SKILL.md references missing file {rel}")

        for workflow_id in EXPECTED_WORKFLOWS:
            workflow_dir = WORKFLOWS_ROOT / workflow_id
            workflow_text = read_text(workflow_dir / "WORKFLOW.md")
            for match in LOCAL_REF_RE.finditer(workflow_text):
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

    def test_zotero_atlas_example_coverage(self) -> None:
        self.assertTrue(ATLAS_PATH.exists(), "missing Zotero example atlas")
        atlas_text = read_text(ATLAS_PATH)
        self.assertIn("references/figure-screenshot-gallery.md", atlas_text)
        self.assertIn("assets/zotero-figure-examples/manifest.json", atlas_text)

        for workflow_id in EXPECTED_WORKFLOWS:
            section = markdown_section(atlas_text, workflow_id)
            self.assertIsNotNone(section, f"missing atlas section for {workflow_id}")
            assert section is not None

            if workflow_id == "nnscholar4-1-data-figure":
                count = len(re.findall(r"^- Figure example \d+:", section, flags=re.MULTILINE))
                self.assertGreaterEqual(count, 10, "data-figure atlas needs at least 10 figure examples")
            else:
                count = len(re.findall(r"^- Example \d+:", section, flags=re.MULTILINE))
                self.assertGreaterEqual(count, 5, f"{workflow_id} atlas needs at least 5 examples")

    def test_zotero_figure_screenshot_manifest(self) -> None:
        self.assertTrue(FIGURE_ASSET_MANIFEST.exists(), "missing Zotero figure asset manifest")
        manifest = json.loads(read_text(FIGURE_ASSET_MANIFEST))
        self.assertIsInstance(manifest, list)
        self.assertGreaterEqual(len(manifest), 10)

        seen_ids: set[str] = set()
        suite_root = SUITE_ROOT.resolve()
        for entry in manifest:
            self.assertNotIn("att", entry, "manifest must not require local Zotero attachment keys")
            self.assertNotIn("source_pdf_attachment", entry, "manifest must not require local Zotero attachments")
            self.assertTrue(entry.get("portable"), "manifest entries must be portable bundled assets")

            asset_id = entry.get("id")
            self.assertIsInstance(asset_id, str)
            self.assertNotIn(asset_id, seen_ids)
            seen_ids.add(asset_id)

            license_text = str(entry.get("license", "")).upper().replace("-", " ")
            self.assertIn("CC BY", license_text, f"{asset_id} must use a reusable CC BY license")
            self.assertNotIn("NC", license_text, f"{asset_id} must not be non-commercial only")
            self.assertNotIn("ND", license_text, f"{asset_id} must not be no-derivatives only")

            rel_file = entry.get("bundled_file")
            self.assertIsInstance(rel_file, str)
            self.assertTrue(rel_file.endswith(".jpg"), f"{asset_id} must point to a JPG asset")
            asset_path = (SUITE_ROOT / rel_file).resolve()
            asset_path.relative_to(suite_root)
            self.assertTrue(asset_path.exists(), f"missing screenshot asset {rel_file}")
            self.assertGreater(asset_path.stat().st_size, 10_000, f"screenshot asset is unexpectedly small: {rel_file}")

            self.assertTrue(entry.get("source_key"), f"{asset_id} missing source key")
            self.assertTrue(entry.get("zotero_key"), f"{asset_id} missing Zotero provenance key")
            self.assertTrue(entry.get("doi"), f"{asset_id} missing DOI")
            self.assertTrue(entry.get("pattern"), f"{asset_id} missing pattern")

    def test_figure_gallery_embeds_bundled_images(self) -> None:
        self.assertTrue(FIGURE_GALLERY_PATH.exists(), "missing bundled figure screenshot gallery")
        gallery_text = read_text(FIGURE_GALLERY_PATH)
        embeds = re.findall(r"!\[[^\]]+\]\((\.\./assets/zotero-figure-examples/[^)]+\.jpg)\)", gallery_text)
        self.assertGreaterEqual(len(embeds), 10)

        for rel_embed in embeds:
            asset_path = (FIGURE_GALLERY_PATH.parent / rel_embed).resolve()
            asset_path.relative_to(SUITE_ROOT.resolve())
            self.assertTrue(asset_path.exists(), f"gallery embeds missing asset {rel_embed}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
