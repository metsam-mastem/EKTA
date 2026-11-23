#!/usr/bin/env python3
"""Static structural and JavaScript syntax checks for the EKTA browser explorer."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HTML = ROOT / "runtime" / "web" / "index.html"
REQUIRED_IDS = {
    "query", "search-button", "result-list", "detail-view",
    "territory-filter", "domain-filter", "layer-filter", "type-filter",
    "status-filter", "kind-filter", "tag-cloud", "load-more",
}


class ExplorerParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicates: set[str] = set()
        self.scripts: list[str] = []
        self._in_script = False
        self.html_attributes: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.html_attributes = {key: value or "" for key, value in attributes.items()}
        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicates.add(element_id)
            self.ids.add(element_id)
        if tag == "script":
            self._in_script = True
            self.scripts.append("")

    def handle_endtag(self, tag: str) -> None:
        if tag == "script":
            self._in_script = False

    def handle_data(self, data: str) -> None:
        if self._in_script and self.scripts:
            self.scripts[-1] += data


def validate_frontend(path: Path = DEFAULT_HTML, require_node: bool = True) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"Explorer HTML not found: {path}"]
    source = path.read_text(encoding="utf-8")
    if "<!doctype html>" not in source.casefold():
        errors.append("Explorer must declare an HTML5 doctype")

    parser = ExplorerParser()
    parser.feed(source)
    parser.close()

    if parser.html_attributes.get("lang") != "fa" or parser.html_attributes.get("dir") != "rtl":
        errors.append("Explorer root must declare lang='fa' and dir='rtl'")
    if parser.duplicates:
        errors.append("Duplicate HTML IDs: " + ", ".join(sorted(parser.duplicates)))
    missing = REQUIRED_IDS - parser.ids
    if missing:
        errors.append("Missing required explorer elements: " + ", ".join(sorted(missing)))
    if not parser.scripts or not any(script.strip() for script in parser.scripts):
        errors.append("Explorer must contain its inline interaction script")

    node = shutil.which("node")
    if node is None:
        if require_node:
            errors.append("Node.js is required to syntax-check the explorer JavaScript")
    else:
        for index, script in enumerate(parser.scripts):
            if not script.strip():
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as handle:
                handle.write(script)
                handle.flush()
                result = subprocess.run(
                    [node, "--check", handle.name],
                    capture_output=True,
                    text=True,
                    timeout=20,
                    check=False,
                )
            if result.returncode != 0:
                errors.append(
                    f"Inline JavaScript block {index + 1} has a syntax error: "
                    f"{result.stderr.strip() or result.stdout.strip()}"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML)
    parser.add_argument("--allow-missing-node", action="store_true")
    args = parser.parse_args()
    errors = validate_frontend(args.html, require_node=not args.allow_missing_node)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: explorer HTML structure, RTL contract, required controls, and JavaScript syntax")
    return 0


if __name__ == "__main__":
    sys.exit(main())
