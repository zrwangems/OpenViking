#!/usr/bin/env python3
"""Package R2025b block templates used by SLX resource ingestion."""

from __future__ import annotations

import json
import re
from pathlib import Path

from openviking.parse.parsers.matlab.catalog_data import _CATALOG, _CATEGORY_TITLES


def section(document: str, name: str) -> str:
    match = re.search(
        rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)", document, re.MULTILINE | re.DOTALL
    )
    return match.group(1).strip() if match else ""


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main() -> None:
    root = Path("resources/simulink-block-library")
    target = Path("openviking/parse/parsers/matlab/block_templates.json")
    templates = {}
    for family, names in _CATALOG.items():
        for name in names:
            document = (root / family / f"{slug(name)}.md").read_text(encoding="utf-8")
            summary = document.split(f"# {name}\n", 1)[1].split("## ", 1)[0].strip()
            page = re.search(r"^documentation_page: '(.+)'$", document, re.MULTILINE).group(1)
            templates[f"{family}/{name}"] = {
                "name": name,
                "category": _CATEGORY_TITLES[family],
                "documentation_page": page,
                "summary": summary,
                "libraries": section(document, "Libraries"),
                "description": section(document, "Description"),
                "ports": section(document, "Ports"),
                "parameters": section(document, "Parameters"),
            }
    payload = {"schema_version": 1, "release": "R2025b", "templates": templates}
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(templates)} templates to {target}")


if __name__ == "__main__":
    main()
