"""Command line interface for the EKTA runtime."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from .repository import AtlasRepository


def main() -> None:
    parser = argparse.ArgumentParser(prog="ekta", description="EKTA knowledge runtime")
    parser.add_argument("--root", type=Path, default=Path(os.environ.get("EKTA_ROOT", ".")))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("overview", help="print atlas inventory")
    graph = sub.add_parser("graph", help="export the typed graph as JSON")
    graph.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    repo = AtlasRepository(args.root)
    if args.command == "overview":
        print(json.dumps(repo.overview(), ensure_ascii=False, indent=2))
    elif args.command == "graph":
        rendered = json.dumps(repo.graph_data, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")


if __name__ == "__main__":
    main()
