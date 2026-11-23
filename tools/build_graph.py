#!/usr/bin/env python3
"""Build a minimal JSON node/edge index from EKTA concept front matter."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONCEPT_DIR = ROOT / "encyclopedia" / "concepts"
OUT = ROOT / "build" / "knowledge-graph.json"

def scalar(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.M)
    return match.group(1).strip().strip('"') if match else None

def list_value(text: str, key: str) -> list[str]:
    match = re.search(rf"^{re.escape(key)}:\s*\[([^]]*)\]", text, re.M)
    if not match:
        return []
    return [item.strip().strip('"\'') for item in match.group(1).split(",") if item.strip()]

def build() -> dict:
    nodes, edges = [], []
    for path in sorted(CONCEPT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        node_id = scalar(text, "id")
        if not node_id:
            continue
        nodes.append({
            "id": node_id,
            "label": scalar(text, "canonical_name") or path.stem,
            "status": scalar(text, "status"),
            "domains": list_value(text, "domains"),
            "layers": list_value(text, "layers"),
            "knowledge_types": list_value(text, "knowledge_types"),
            "source_file": path.relative_to(ROOT).as_posix(),
        })
    return {"schema_version": 1, "nodes": nodes, "edges": edges,
            "note": "Initial node index. Typed edges will be emitted when relationship front matter is standardized."}

if __name__ == "__main__":
    graph = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(graph['nodes'])} nodes to {OUT.relative_to(ROOT)}")
