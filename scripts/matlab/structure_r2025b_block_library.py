#!/usr/bin/env python3
"""Rebuild structured YAML indexes in every packaged block document.

No network, manifest totals, parallel JSON, or generated prose are involved.
Each unique document is updated once and then copied to its Library Browser
occurrences. Use --check to verify the committed library without writing it.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from openviking.parse.parsers.matlab.structure import (
    structure_block_document,
    validate_structured_document,
    without_structured_data,
)


def content_lines(document: str) -> list[str]:
    return [line for line in document.splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).parents[2]
        / "openviking/parse/parsers/matlab/simulink-block-library/manifest.json",
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.manifest.parent
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    documents = {
        root / block["documents"][language]["path"]
        for product in manifest["products"]
        for library in product["libraries"]
        for block in library["blocks"]
        for language in ("en", "zh")
        if block["documents"][language]["path"]
    }
    failures = []
    for path in sorted(documents):
        source = path.read_text(encoding="utf-8")
        structured = structure_block_document(source)
        try:
            validate_structured_document(structured)
            # Only generated YAML (and empty sections for the two official
            # library-topic pages) may be added. Every original content line
            # remains in its original order.
            before = content_lines(without_structured_data(source))
            after = content_lines(without_structured_data(structured))
            retained = 0
            for line in after:
                if retained < len(before) and line == before[retained]:
                    retained += 1
            if retained != len(before):
                raise ValueError("original Markdown content changed")
            if args.check and source != structured:
                raise ValueError("document is not in structured form")
        except Exception as exc:
            failures.append((str(path.relative_to(root)), str(exc)))
            continue
        if not args.check and source != structured:
            path.write_text(structured, encoding="utf-8")

    copies = 0
    for product in manifest["products"]:
        for library in product["libraries"]:
            for block in library["blocks"]:
                for language in ("en", "zh"):
                    relative = block.get("resource_paths", {}).get(language)
                    source_relative = block["documents"][language]["path"]
                    if not relative or not source_relative:
                        continue
                    source = root / source_relative
                    target = root / relative
                    if args.check:
                        if not target.is_file() or target.read_bytes() != source.read_bytes():
                            failures.append((relative, "browser copy differs from source"))
                    elif target != source:
                        target.write_bytes(source.read_bytes())
                    copies += 1
    if failures:
        for path, error in failures[:50]:
            print(f"{path}: {error}")
        raise SystemExit(f"{len(failures)} structured-document failures")
    action = "validated" if args.check else "rebuilt"
    print(f"{action} {len(documents)} unique bilingual documents and {copies} browser copies")


if __name__ == "__main__":
    main()
