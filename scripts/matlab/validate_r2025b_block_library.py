#!/usr/bin/env python3
"""Audit every R2025b XML block occurrence and its bilingual documentation.

This deliberately checks content, not just manifest totals. With the HTML cache
available, official-language pages must also equal a fresh render of their
cached MathWorks source. Worker translations must preserve every heading and
Markdown table row. Third-party and machine-local libraries are outside scope.
"""

from __future__ import annotations

import argparse
import collections
import json
import posixpath
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from scrape_r2025b_all_blocks import render_page, unique_entries
from translate_r2025b_all_blocks import table_shapes


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def xml_occurrences(
    product: dict, cache: Path, simulink_block_libraries_only: bool = False
) -> list[tuple[str, str, str, str]]:
    path = cache / f"{product['id']}.xml"
    if not path.exists():
        return []
    root = ET.parse(path).getroot()
    if not simulink_block_libraries_only:
        return [
            (product["id"], ref.get("target", ""), ref.get("name", ""), ref.get("type", ""))
            for ref in root.iter()
            if local_name(ref.tag) == "ref" and ref.get("type", "").endswith("block")
        ]
    result = []

    def visit(element, ancestry):
        for child in element:
            if local_name(child.tag) not in {"cat", "sub"}:
                continue
            title = next(
                (
                    " ".join("".join(node.itertext()).split())
                    for node in child
                    if local_name(node.tag) == "title"
                ),
                "",
            )
            lineage = [*ancestry, title]
            if lineage[1:3] == ["Simulink Environment Fundamentals", "Block Libraries"]:
                result.extend(
                    (product["id"], ref.get("target", ""), ref.get("name", ""), ref.get("type", ""))
                    for ref in child
                    if local_name(ref.tag) == "ref" and ref.get("type", "").endswith("block")
                )
            visit(child, lineage)

    visit(root, [])
    return result


def markdown_body(markdown: str) -> str:
    match = re.match(r"\A---\n.*?\n---\n(.*)\Z", markdown, re.DOTALL)
    if not match:
        raise ValueError("missing or malformed front matter")
    return match.group(1).strip()


def content_lines(markdown: str) -> collections.Counter:
    """Ignore legacy section ordering while still detecting every missing line."""
    lines = []
    placeholder = re.compile(
        r"(?:Not documented in R2025b\.|(?:在 )?R2025b 中未记录。|R2025b 官方文档未提供。)"
    )
    for line in markdown_body(markdown).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("# "):
            continue
        stripped = {"## 版本历史记录": "## 版本历史"}.get(stripped, stripped)
        if placeholder.fullmatch(stripped):
            if lines and lines[-1].startswith("## "):
                lines.pop()
            continue
        lines.append(stripped)
    return collections.Counter(lines)


def validate_translation_for_audit(source: str, translated: str) -> None:
    """Allow legacy section reordering, but not dropped headings or table rows."""
    if len(translated) < len(source) * 0.25:
        raise ValueError(f"translation too short: {len(translated)} vs {len(source)}")
    source_headings = len(re.findall(r"^#{1,6} ", source, re.MULTILINE))
    translated_headings = len(re.findall(r"^#{1,6} ", translated, re.MULTILINE))
    if translated_headings < source_headings:
        raise ValueError(f"heading count changed: {translated_headings} vs {source_headings}")
    if sorted(table_shapes(source)) != sorted(table_shapes(translated)):
        raise ValueError("table shapes changed")
    if not re.search(r"[\u4e00-\u9fff]", translated):
        raise ValueError("translation contains no Chinese text")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).parents[2]
        / "openviking/parse/parsers/matlab/simulink-block-library/manifest.json",
    )
    parser.add_argument("--xml-cache", type=Path, default=Path("/tmp/r2025b-products"))
    parser.add_argument("--html-cache", type=Path, default=Path("/tmp/r2025b-block-docs"))
    parser.add_argument("--report", type=Path)
    parser.add_argument("--skip-source-render", action="store_true")
    args = parser.parse_args()
    root = args.manifest.parent
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    failures: dict[str, list] = collections.defaultdict(list)
    documents: dict[tuple[str, str, str], str] = {}
    occurrences = []
    official_compared = 0
    worker_compared = 0

    for product in manifest["products"]:
        for library in product["libraries"]:
            for block in library["blocks"]:
                item = (
                    product["id"],
                    block["documentation_path"],
                    block["name"],
                    block["type"],
                )
                occurrences.append(item)
                for language in ("en", "zh"):
                    document = block["documents"][language]
                    key = (product["id"], block["documentation_path"], language)
                    if document["status"] != "available" or not document["path"]:
                        failures["unavailable_document"].append(key)
                    elif key in documents and documents[key] != document["path"]:
                        failures["inconsistent_document_mapping"].append(key)
                    else:
                        documents[key] = document["path"]
        expected = xml_occurrences(
            product,
            args.xml_cache,
            simulink_block_libraries_only=(
                product["id"] == "simulink" and manifest["scope"].startswith("the 66-entry")
            ),
        )
        if expected:
            actual = [item for item in occurrences if item[0] == product["id"]]
            if collections.Counter(actual) != collections.Counter(expected):
                failures["xml_occurrence_mismatch"].append(product["id"])
        elif product["status"] == "enumerated":
            failures["missing_xml_cache"].append(product["id"])

    for (_product_id, _documentation_path, language), relative in documents.items():
        path = root / relative
        if not path.is_file():
            failures["missing_file"].append(relative)
            continue
        markdown = path.read_text(encoding="utf-8")
        try:
            body = markdown_body(markdown)
        except ValueError as exc:
            failures["invalid_front_matter"].append([relative, str(exc)])
            continue
        if "documentation_release: R2025b" not in markdown:
            failures["wrong_release"].append(relative)
        if not re.match(r"^# \S.+", body) or len(body) < 40:
            failures["empty_body"].append(relative)
        if language == "zh" and not re.search(r"[\u4e00-\u9fff]", body):
            failures["no_chinese_body"].append(relative)
        if (
            "Full English and Chinese documentation is pending" in body
            or "完整中英文正文待补" in body
        ):
            failures["pending_placeholder"].append(relative)

    if not args.skip_source_render:
        canonical_entries = {}
        source_entries = {}
        for product in manifest["products"]:
            if product["status"] != "enumerated":
                continue
            for entry in unique_entries(product):
                if ".." not in Path(entry["documentation_path"]).parts:
                    source_entries[(product["id"], entry["documentation_path"])] = (
                        product,
                        entry,
                    )
                relative = entry["documents"]["zh"]["path"]
                if (
                    ".." not in Path(relative).parts
                    and ".." not in Path(entry["documentation_path"]).parts
                ):
                    canonical_entries[(root / relative).resolve()] = (product, entry)
        for product in manifest["products"]:
            if product["status"] != "enumerated":
                continue
            for entry in unique_entries(product):
                english = root / entry["documents"]["en"]["path"]
                chinese = root / entry["documents"]["zh"]["path"]
                source_path = (
                    args.html_cache / product["id"] / "en" / f"{entry['documentation_path']}.html"
                )
                try:
                    expected, _ = render_page(source_path.read_bytes(), entry, product, "en")
                    if content_lines(english.read_text(encoding="utf-8")) != content_lines(
                        expected
                    ):
                        failures["english_source_render_mismatch"].append(
                            [product["id"], entry["documentation_path"]]
                        )
                except Exception as exc:
                    failures["english_source_render_error"].append(
                        [product["id"], entry["documentation_path"], str(exc)]
                    )
                if "chinese_source: official" in chinese.read_text(encoding="utf-8"):
                    documentation_path = entry["documentation_path"]
                    if ".." in Path(documentation_path).parts:
                        normalized = posixpath.normpath(documentation_path)
                        while normalized.startswith("../"):
                            normalized = normalized[3:]
                        owner, owner_path = normalized.split("/", 1)
                        source_product, source_entry = source_entries.get(
                            (owner, owner_path), (product, entry)
                        )
                    else:
                        source_product, source_entry = canonical_entries.get(
                            chinese.resolve(), (product, entry)
                        )
                    source_path = (
                        args.html_cache
                        / source_product["id"]
                        / "zh"
                        / f"{source_entry['documentation_path']}.html"
                    )
                    try:
                        expected, _ = render_page(
                            source_path.read_bytes(), source_entry, source_product, "zh"
                        )
                        if content_lines(chinese.read_text(encoding="utf-8")) != content_lines(
                            expected
                        ):
                            failures["chinese_source_render_mismatch"].append(
                                [product["id"], entry["documentation_path"]]
                            )
                        official_compared += 1
                    except Exception as exc:
                        failures["chinese_source_render_error"].append(
                            [product["id"], entry["documentation_path"], str(exc)]
                        )
                else:
                    try:
                        validate_translation_for_audit(
                            markdown_body(english.read_text(encoding="utf-8")),
                            markdown_body(chinese.read_text(encoding="utf-8")),
                        )
                        worker_compared += 1
                    except Exception as exc:
                        failures["worker_translation_structure_mismatch"].append(
                            [product["id"], entry["documentation_path"], str(exc)]
                        )

    # A browser page is a full copy, never a metadata-only substitute.
    for product in manifest["products"]:
        for library in product["libraries"]:
            for block in library["blocks"]:
                for language, relative in block.get("resource_paths", {}).items():
                    browser = root / relative
                    source = root / block["documents"][language]["path"]
                    if not browser.is_file() or browser.read_bytes() != source.read_bytes():
                        failures["browser_copy_mismatch"].append(relative)

    report = {
        "release": "R2025b",
        "scope": manifest["scope"],
        "xml_occurrences_checked": len(occurrences),
        "unique_bilingual_documents_checked": len(documents) // 2,
        "official_chinese_source_renders_checked": official_compared,
        "worker_translation_structures_checked": worker_compared,
        "failures": failures,
        "failure_count": sum(map(len, failures.values())),
        "external_scope_requires_local_matlab": [
            "third-party libraries",
            "hardware support packages not present in the public product catalog",
            "machine-local and licensed library contents",
        ],
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text, encoding="utf-8")
    print(text, end="")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
