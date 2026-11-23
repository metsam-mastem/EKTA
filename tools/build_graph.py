#!/usr/bin/env python3
"""Export the typed EKTA knowledge graph from the canonical repository."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from ekta_runtime.repository import AtlasRepository  # noqa: E402


def build() -> dict:
    return AtlasRepository(ROOT).graph_data


if __name__ == "__main__":
    graph = build()
    output = ROOT / "build" / "knowledge-graph.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = graph["summary"]
    print(
        f"Wrote {summary['node_count']} nodes and {summary['edge_count']} edges "
        f"({summary['resolved_edge_count']} resolved) to {output.relative_to(ROOT)}"
    )
