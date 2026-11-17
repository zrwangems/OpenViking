#!/usr/bin/env python3
"""Audit every R2025b XML block occurrence and its bilingual documentation.

This deliberately checks content, not just manifest totals. With the HTML cache
available, official-language pages must also equal a fresh render of their
cached MathWorks source. Worker translations must preserve every paragraph,
heading and Markdown table row, localize generic labels, and contain no English
prose outside technical identifiers. Third-party and machine-local libraries
are outside scope.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from align_r2025b_browser_tree import EXCLUDED_ENTRIES, entry_key, parse_tree
from scrape_r2025b_all_blocks import (
    cached_source_path,
    document_source,
    render_page,
    unique_entries,
)
from translate_r2025b_all_blocks import GENERIC_HEADINGS, validate_translation


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


ENGLISH_HEADINGS = re.compile(
    r"^#{2,6} (?:Description|Ports|Parameters|Libraries|Block Characteristics|"
    r"Extended Capabilities|Version History|Input|Inputs|Output|Outputs|Conserving|"
    r"Dependencies|Dependency|Programmatic Use|Tips?|See Also|MATLAB Command|"
    r"Get Started|Main|Variables|Equations|Data Types|Assumptions and Limitations|"
    r"Faults|Signal Attributes|Initial Conditions|Parameter Dependencies|Limitations|"
    r"Code Generation|General|Advanced|Configuration|Simulation)(?: Tab)?$"
)
ENGLISH_TABLE_LABELS = re.compile(
    r"\*\*(?:Block Parameter|Type|Values|Default|Programmatic Use)(?:\*\*[:：]|[:：]\*\*)"
)
ENGLISH_WORDS = re.compile(
    r"\b(the|and|for|with|from|this|that|using|specified|generate|select|input|"
    r"output|parameter|data|model|simulation|introduced|default|command|window|"
    r"browser|click|close|run|enter|information|before|after|when|into|each|you|"
    r"your|are|not|can|use|value|values|type|table|during|shows|display|displays|"
    r"block|blocks|port|ports|signal|signals)\b",
    re.IGNORECASE,
)
ENGLISH_SENTENCE_START = re.compile(
    r"^(?:The|This|These|To|You|When|If|For|Use|Select|Run|Click|Close|An|In|"
    r"On|By|After|Before|During|Generate|Specify|Set|Enable|Disable)\b"
)


def untranslated_prose(markdown: str) -> list[str]:
    """Find English prose, not identifiers, equations, code or library paths."""
    result = []
    section = ""
    fenced = False
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            fenced = not fenced
            continue
        if fenced or not stripped or stripped.startswith("# ") or line.startswith("    "):
            continue
        if stripped.startswith("## "):
            section = stripped
        if section in {"## 所属库", "## Libraries"} or re.search(r"[\u4e00-\u9fff]", stripped):
            continue
        scrubbed = re.sub(r"`[^`]*`", "", stripped)
        if "=" in scrubbed and not ENGLISH_SENTENCE_START.search(scrubbed):
            continue  # Equations commonly contain the English words "for" and "and".
        words = {word.lower() for word in ENGLISH_WORDS.findall(scrubbed)}
        if len(words) >= 2 or (
            ENGLISH_SENTENCE_START.search(scrubbed)
            and len(re.findall(r"[A-Za-z]+", scrubbed)) >= 5
        ):
            result.append(stripped)
    return result


def validate_chinese_language(translated: str) -> None:
    """Check language completeness independently of section ordering."""
    lines = translated.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("## "):
            next_section = index + 1
            while next_section < len(lines) and not lines[next_section].startswith("## "):
                next_section += 1
            if not any(item.strip() for item in lines[index + 1 : next_section]):
                raise ValueError(f"empty Chinese section: {line}")
    for line in lines:
        if ENGLISH_HEADINGS.match(line):
            raise ValueError(f"untranslated heading: {line}")
        if ENGLISH_TABLE_LABELS.search(line):
            raise ValueError(f"untranslated table label: {line}")
    if re.search(r"\*\*Introduced (?:in|before)", translated):
        raise ValueError("untranslated version-history introduction")
    english_prose = untranslated_prose(translated)
    if english_prose:
        raise ValueError(f"untranslated English prose: {english_prose[:3]}")


def validate_translation_for_audit(source: str, translated: str) -> None:
    """Require every source paragraph, heading, table row and generic label in Chinese."""
    validate_translation(source, translated)
    validate_chinese_language(translated)
    source_sections = re.findall(r"^## (.+)$", source, re.MULTILINE)
    translated_sections = re.findall(r"^## (.+)$", translated, re.MULTILINE)
    core_sections = {
        "Ports",
        "Parameters",
        "Libraries",
        "Block Characteristics",
        "Extended Capabilities",
        "Version History",
        "Description",
    }
    for source_title, translated_title in zip(source_sections, translated_sections, strict=True):
        if source_title in core_sections and translated_title != GENERIC_HEADINGS[source_title]:
            raise ValueError(
                f"section mismatch: {source_title} -> {translated_title}; "
                f"expected {GENERIC_HEADINGS[source_title]}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).parents[2]
        / "openviking/parse/parsers/matlab/simulink-block-library/manifest.json",
    )
    parser.add_argument("--xml-cache", type=Path, default=Path("/tmp/r2025b-products"))
    parser.add_argument(
        "--tree",
        type=Path,
        default=Path(__file__).with_name("tree_full.md"),
    )
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
    retained_source_documents = 0

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
                    key = (
                        product["id"],
                        block["documentation_path"],
                        block.get("source_release", "R2025b"),
                        language,
                    )
                    if not block["documentation_path"]:
                        failures["unexpected_tree_only_entry"].append(key)
                    elif document["status"] != "available" or not document["path"]:
                        failures["unavailable_document"].append(key)
                    elif key in documents and documents[key] != document["path"]:
                        failures["inconsistent_document_mapping"].append(key)
                    else:
                        documents[key] = document["path"]
    expected_tree = parse_tree(args.tree)
    actual_tree = [
        {
            "name": product["name"],
            "directories": [library["path"] for library in product["libraries"] if library["path"]],
            "blocks": [
                (library["path"], block["name"])
                for library in product["libraries"]
                for block in library["blocks"]
            ],
        }
        for product in manifest["products"]
    ]
    expected_flat = [
        {
            "name": product["name"],
            "directories": [directory["path"] for directory in product["directories"]],
            "blocks": [
                (block["path"], block["name"])
                for block in product["blocks"]
                if entry_key(product["name"], block["path"], block["name"]) not in EXCLUDED_ENTRIES
            ],
        }
        for product in expected_tree
    ]
    actual_structure = [(product["name"], product["directories"]) for product in actual_tree]
    expected_structure = [(product["name"], product["directories"]) for product in expected_flat]
    actual_blocks = collections.Counter(
        (product["name"], tuple(path), name)
        for product in actual_tree
        for path, name in product["blocks"]
    )
    expected_blocks = collections.Counter(
        (product["name"], tuple(path), name)
        for product in expected_flat
        for path, name in product["blocks"]
    )
    if actual_structure != expected_structure or actual_blocks != expected_blocks:
        failures["tree_full_mismatch"].append(
            "products, ordered directories, or complete block paths differ from tree_full.md"
        )

    for (
        _product_id,
        _documentation_path,
        _source_release,
        language,
    ), relative in documents.items():
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
        if not re.search(r"documentation_release: R20\d\d[ab]", markdown):
            failures["wrong_release"].append(relative)
        if not re.match(r"^#\s+\S", body) or len(body) < 40:
            failures["empty_body"].append(relative)
        if language == "zh" and not re.search(r"[\u4e00-\u9fff]", body):
            failures["no_chinese_body"].append(relative)
        if (
            "Full English and Chinese documentation is pending" in body
            or "完整中英文正文待补" in body
        ):
            failures["pending_placeholder"].append(relative)

    for product in manifest["products"]:
        if product["status"] != "enumerated":
            continue
        for entry in unique_entries(product):
            english = root / entry["documents"]["en"]["path"]
            chinese = root / entry["documents"]["zh"]["path"]
            source_product, source_document = document_source(product, entry)
            source_release = entry.get("source_release", "R2025b")
            source_path = cached_source_path(
                args.html_cache, source_product, source_document, "en", source_release
            )
            if not source_path.is_file():
                # A missing external HTML cache must not skip the local bilingual audit.
                retained_source_documents += 1
            elif not args.skip_source_render:
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
                if args.skip_source_render:
                    continue
                source_path = cached_source_path(
                    args.html_cache, source_product, source_document, "zh", source_release
                )
                try:
                    expected, _ = render_page(source_path.read_bytes(), entry, product, "zh")
                    if content_lines(chinese.read_text(encoding="utf-8")) != content_lines(
                        expected
                    ):
                        failures["chinese_source_render_mismatch"].append(
                            [product["id"], entry["documentation_path"]]
                        )
                    validate_chinese_language(markdown_body(chinese.read_text(encoding="utf-8")))
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
                    failures["worker_translation_mismatch"].append(
                        [product["id"], entry["documentation_path"], str(exc)]
                    )

    # A browser page is a full copy, never a metadata-only substitute.
    for product in manifest["products"]:
        for library in product["libraries"]:
            for block in library["blocks"]:
                for language, relative in block.get("resource_paths", {}).items():
                    browser = root / relative
                    if not block["documentation_path"]:
                        if (
                            not browser.is_file()
                            or "documentation_status: tree_only"
                            not in browser.read_text(encoding="utf-8")
                        ):
                            failures["invalid_tree_only_page"].append(relative)
                        continue
                    source = root / block["documents"][language]["path"]
                    if not browser.is_file() or browser.read_bytes() != source.read_bytes():
                        failures["browser_copy_mismatch"].append(relative)

    report = {
        "release": "R2025b",
        "scope": manifest["scope"],
        "tree_occurrences_checked": len(occurrences),
        "retained_documents_without_cached_html": retained_source_documents,
        "unique_bilingual_documents_checked": len(documents) // 2,
        "official_chinese_source_renders_checked": official_compared,
        "worker_translations_checked": worker_compared,
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
