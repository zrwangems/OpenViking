#!/usr/bin/env python3
"""Build the complete R2025b Simulink block knowledge base.

The manifest is extracted from the official dynamic Simulink Blocks category
list. It contains 341 entries in 20 categories and 333 distinct documentation
paths. Requires requests, beautifulsoup4, and markdownify. Generated pages have
no external links; raw HTML is cached outside the resource tree.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
from pathlib import Path

import requests
from browser_tree_writer import normalize_block_document
from bs4 import BeautifulSoup
from markdownify import markdownify

RELEASE = "R2025b"
SECTIONS = {
    "Description",
    "Ports",
    "Parameters",
    "Block Characteristics",
    "Programmatic Use: Add Block",
    "Extended Capabilities",
    "Version History",
}
ZH_SECTIONS = {
    "描述",
    "端口",
    "参数",
    "模块特性",
    "编程式使用: 添加模块",
    "编程式使用：添加模块",
    "扩展功能",
    "版本历史",
    "版本历史记录",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source_url(path: str, language: str = "en") -> str:
    host = "ww2.mathworks.cn" if language == "zh-CN" else "www.mathworks.com"
    return f"https://{host}/help/releases/{RELEASE}/simulink/{path}"


def cache_path(path: str, language: str = "en") -> str:
    suffix = ".zh-CN.html" if language == "zh-CN" else ""
    return f"{RELEASE}-{path.replace('/', '-')}{suffix}"


def fetch(entry: dict[str, str], cache: Path, language: str = "en") -> tuple[dict[str, str], Path]:
    path = entry["path"]
    target = cache / cache_path(path, language)
    if not target.exists():
        response = requests.get(source_url(path, language), timeout=45)
        response.raise_for_status()
        target.write_bytes(response.content)
    return entry, target


def clean_section(section) -> None:
    for element in section.select("script, style, svg, iframe"):
        element.decompose()
    for element in section.select("button, nav"):
        element.unwrap()
    for element in section.select(".switch"):
        element.decompose()
    for image in section.find_all("img"):
        alt = image.get("alt", "").strip()
        image.replace_with(alt) if alt and len(alt) > 2 else image.decompose()
    for link in section.find_all("a"):
        link.unwrap()


def localized_content(html: bytes, entry: dict[str, str], language: str) -> tuple[str, list]:
    soup = BeautifulSoup(html, "html.parser")
    main = soup.select_one("main") or soup
    heading = main.select_one("h1")
    if heading is None:
        raise ValueError(f"No documentation heading for {entry['name']}")
    subtitle_node = main.select_one("p[itemprop='purpose']") or heading.find_next_sibling("p")
    subtitle = " ".join(
        (
            subtitle_node.get_text(" ", strip=True)
            if subtitle_node
            else heading.get_text(" ", strip=True)
        ).split()
    )
    sections = []
    library_prefix = "库:" if language == "zh-CN" else "Libraries:"
    library = next(
        (p for p in main.find_all("p") if p.get_text(" ", strip=True).startswith(library_prefix)),
        None,
    )
    if library:
        library_text = " ".join(
            library.get_text(" ", strip=True).removeprefix(library_prefix).split()
        )
        sections.append(("所属库" if language == "zh-CN" else "Libraries", library_text))

    allowed = ZH_SECTIONS if language == "zh-CN" else SECTIONS
    candidates = main.select("div.refsect1.description, div.ref_sect, div.block_ref, div.refsect1")
    # A block_ref wrapper can have a direct Description h2 while the actual
    # prose lives in a nested refsect1 with the same h2. Select the richest
    # candidate for each section instead of rendering the empty wrapper and
    # then discarding the informative child as a duplicate.
    by_title = {}
    for candidate in candidates:
        heading = candidate.find("h2", recursive=False)
        if heading is not None:
            title = heading.get_text(" ", strip=True)
            if title in allowed:
                by_title.setdefault(title, []).append(candidate)
    selected = {
        title: max(
            items,
            key=lambda item: (
                sum(len(text) for text in item.stripped_strings if text != title),
                len(list(item.parents)),
            ),
        )
        for title, items in by_title.items()
    }
    for section in candidates:
        section_heading = section.find("h2", recursive=False)
        if section_heading is None:
            continue
        title = section_heading.get_text(" ", strip=True)
        if title not in allowed or selected[title] is not section:
            continue
        section_heading.extract()
        fragments = [section]
        # Ports often use sibling ref_sect containers for Input and Output.
        for sibling in section.find_next_siblings("div", class_="ref_sect"):
            if sibling.find("h2", recursive=False) is not None:
                break
            fragments.append(sibling)
        rendered = []
        for fragment in fragments:
            clean_section(fragment)
            rendered.append(markdownify(str(fragment), heading_style="ATX", bullets="-"))
        markdown = re.sub(r"\n{3,}", "\n\n", "\n".join(rendered)).strip()
        markdown = "\n".join(line.rstrip() for line in markdown.splitlines())
        if markdown:
            sections.append((title, markdown))
    return subtitle, sections


def html_to_markdown(
    html: bytes,
    entry: dict[str, str],
    chinese_html: bytes,
    translated_chinese: str | None = None,
) -> tuple[str, str]:
    subtitle, sections = localized_content(html, entry, "en")
    chinese_subtitle, chinese_sections = localized_content(chinese_html, entry, "zh-CN")
    chinese_official = bool(re.search(r"[\u4e00-\u9fff]", chinese_subtitle))
    if not chinese_official and translated_chinese is None:
        raise ValueError(f"Chinese documentation needs worker translation: {entry['path']}")
    if not sections:
        raise ValueError(f"No usable documentation sections for {entry['name']}")
    family = slug(entry["category"])
    metadata = [
        "---",
        "type: simulink-block",
        f"title: {entry['name']!r}",
        f"family: {family}",
        f"documentation_release: {RELEASE}",
        f"official_category: {entry['category']!r}",
        f"documentation_page: {Path(entry['path']).stem!r}",
    ]
    english_lines = [
        *metadata,
        "language: en",
        "---",
        "",
        f"# {entry['name']}",
        "",
        subtitle,
        "",
    ]
    for title, content in sections:
        english_lines.extend([f"## {title}", "", content, ""])

    chinese_lines = [
        *metadata,
        "language: zh-CN",
        f"chinese_source: {'official' if chinese_official else 'worker-translation'}",
        "---",
        "",
        f"# {entry['name']}",
        "",
        chinese_subtitle if chinese_official else "",
        "",
    ]
    if chinese_official:
        for title, content in chinese_sections:
            chinese_lines.extend([f"## {title}", "", content, ""])
    else:
        top_level = {
            "所属库",
            "库",
            "描述",
            "说明",
            "端口",
            "参数",
            "模块特性",
            "扩展功能",
            "版本历史",
        }
        for line in translated_chinese.strip().splitlines():
            if line.startswith("### ") and line[4:].strip() in top_level:
                line = line[1:]
            chinese_lines.append(line)
        chinese_lines.append("")
    return (
        normalize_block_document("\n".join(english_lines), language="en"),
        normalize_block_document("\n".join(chinese_lines), language="zh-CN"),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("openviking/parse/parsers/matlab/simulink-block-library"),
    )
    parser.add_argument("--cache", type=Path, default=Path("/tmp/simulink-block-knowledge-cache"))
    parser.add_argument(
        "--manifest", type=Path, default=Path(__file__).with_name("simulink-block-manifest.json")
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    entries = json.loads(args.manifest.read_text(encoding="utf-8"))
    if len(entries) != 341 or len({entry["path"] for entry in entries}) != 333:
        raise SystemExit(
            "R2025b manifest completeness check failed: expected 341 entries / 333 document paths"
        )

    # Fetch each distinct English and Chinese document once, then render every category.
    distinct = {entry["path"]: entry for entry in entries}
    fetched: dict[tuple[str, str], Path] = {}
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(fetch, entry, args.cache, language): (path, language)
            for path, entry in distinct.items()
            for language in ("en", "zh-CN")
        }
        for future in concurrent.futures.as_completed(futures):
            path, language = futures[future]
            try:
                entry, target = future.result()
                fetched[(path, language)] = target
                print(f"FETCHED {language} {path}", flush=True)
            except Exception as exc:
                failures.append((f"{language}:{path}", str(exc)))
                print(f"FAILED {language} {path}: {exc}", flush=True)
    if failures and not args.offline:
        raise SystemExit(f"Refusing to write an incomplete catalog: {len(failures)} failures")

    written = 0
    render_failures = []
    for entry in entries:
        try:
            translation_path = args.cache / f"{cache_path(entry['path'], 'zh-CN')}.translated.md"
            translated = (
                translation_path.read_text(encoding="utf-8") if translation_path.is_file() else None
            )
            documents = html_to_markdown(
                fetched[(entry["path"], "en")].read_bytes(),
                entry,
                fetched[(entry["path"], "zh-CN")].read_bytes(),
                translated,
            )
            family = slug(entry["category"])
            for language, markdown in zip(("en", "zh"), documents, strict=True):
                target = args.output / language / family / f"{slug(entry['name'])}.md"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(markdown, encoding="utf-8")
            written += 1
        except Exception as exc:
            render_failures.append((entry, str(exc)))
            print(f"RENDER FAILED {entry['name']}: {exc}", flush=True)
    if render_failures:
        raise SystemExit(
            f"Refusing to write an incomplete catalog: {len(render_failures)} render failures"
        )

    from openviking.parse.parsers.matlab.catalog import export_catalog

    export_catalog(args.output / "en")
    export_catalog(args.output / "zh")
    (args.output / "index.md").write_text(
        "# Simulink Block Library\n\n- [English](en/index.md)\n- [中文](zh/index.md)\n",
        encoding="utf-8",
    )
    if failures:
        report = ["# 未完成抓取", ""] + [f"- {path}: {error}" for path, error in failures]
        (args.output / "scrape-failures.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Wrote {written} official directory entries; {len(failures)} fetch failures")


if __name__ == "__main__":
    main()
