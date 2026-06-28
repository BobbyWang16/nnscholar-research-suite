#!/usr/bin/env python3
"""Lightweight Mermaid safety checker for NNScholar flowchart outputs.

This is not a full Mermaid parser. It catches common breakages in generated
flowcharts: missing graph declaration, unbalanced subgraphs, unknown edge node
references, unsafe node IDs, and unbalanced brackets/quotes.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


MERMAID_BLOCK = re.compile(r"```mermaid\s*(.*?)```", re.DOTALL | re.IGNORECASE)
SAFE_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
DECLARATION = re.compile(r"^\s*(flowchart|graph)\s+(TD|TB|BT|RL|LR)\b", re.IGNORECASE)
NODE_DEF = re.compile(r"^\s*([A-Za-z][A-Za-z0-9_]*)\s*(?:\[|\(|\{|\(\(|>)")
SUBGRAPH = re.compile(r"^\s*subgraph\s+([A-Za-z][A-Za-z0-9_]*)")
EDGE_SPLIT = re.compile(r"\s*(?:-->|---|-.->|==>)\s*")


def extract_blocks(text: str) -> list[str]:
    blocks = MERMAID_BLOCK.findall(text)
    if blocks:
        return blocks
    if DECLARATION.search(text):
        return [text]
    return []


def strip_edge_label(part: str) -> str:
    part = part.strip()
    part = re.sub(r"^\|.*?\|", "", part).strip()
    return part


def extract_id(token: str) -> str | None:
    token = strip_edge_label(token)
    match = re.match(r"([A-Za-z][A-Za-z0-9_]*)", token)
    return match.group(1) if match else None


def token_defines_node(token: str) -> str | None:
    token = strip_edge_label(token)
    match = re.match(r"([A-Za-z][A-Za-z0-9_]*)\s*(?:\[|\(|\{|\(\(|>)", token)
    return match.group(1) if match else None


def check_balance(block: str, errors: list[str], idx: int) -> None:
    pairs = [("[", "]"), ("(", ")"), ("{", "}")]
    for left, right in pairs:
        if block.count(left) != block.count(right):
            errors.append(f"block {idx}: unbalanced {left}{right}")
    if block.count('"') % 2:
        errors.append(f"block {idx}: unbalanced double quotes")


def validate_block(block: str, idx: int) -> list[str]:
    errors: list[str] = []
    lines = [line.rstrip() for line in block.splitlines() if line.strip()]
    if not lines:
        return [f"block {idx}: empty Mermaid block"]

    if not any(DECLARATION.match(line) for line in lines[:3]):
        errors.append(f"block {idx}: missing flowchart/graph declaration near top")

    check_balance(block, errors, idx)

    declared: set[str] = set()
    referenced: set[str] = set()
    subgraph_depth = 0

    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("%%"):
            continue
        if DECLARATION.match(stripped):
            continue
        if stripped == "end":
            subgraph_depth -= 1
            if subgraph_depth < 0:
                errors.append(f"block {idx}, line {lineno}: extra end")
                subgraph_depth = 0
            continue
        sub = SUBGRAPH.match(stripped)
        if sub:
            subgraph_id = sub.group(1)
            declared.add(subgraph_id)
            subgraph_depth += 1
            continue
        if stripped.startswith(("classDef ", "class ", "style ", "linkStyle ")):
            continue

        node = NODE_DEF.match(stripped)
        if node:
            node_id = node.group(1)
            if not SAFE_ID.match(node_id):
                errors.append(f"block {idx}, line {lineno}: unsafe node id {node_id!r}")
            declared.add(node_id)

        if any(arrow in stripped for arrow in ("-->", "---", "-.->", "==>")):
            parts = EDGE_SPLIT.split(stripped)
            for part in parts:
                defined_id = token_defines_node(part)
                if defined_id:
                    declared.add(defined_id)
                node_id = extract_id(part)
                if node_id:
                    referenced.add(node_id)
                    if not SAFE_ID.match(node_id):
                        errors.append(f"block {idx}, line {lineno}: unsafe edge id {node_id!r}")

        if re.match(r"^\s*[-*]\s+", line):
            errors.append(f"block {idx}, line {lineno}: markdown bullet inside Mermaid block")

    if subgraph_depth:
        errors.append(f"block {idx}: {subgraph_depth} subgraph(s) missing end")

    unknown = sorted(node for node in referenced if node not in declared)
    if unknown:
        errors.append(f"block {idx}: edge references undefined node id(s): {', '.join(unknown)}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Mermaid code blocks in a Markdown or .mmd file.")
    parser.add_argument("path", help="Path to Markdown or Mermaid file")
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    blocks = extract_blocks(text)
    if not blocks:
        print("No Mermaid blocks found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    for idx, block in enumerate(blocks, start=1):
        errors.extend(validate_block(block, idx))

    if errors:
        print("Mermaid validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Mermaid validation passed: {len(blocks)} block(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
