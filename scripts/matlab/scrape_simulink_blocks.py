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
from bs4 import BeautifulSoup
from markdownify import markdownify

from openviking.parse.parsers.matlab.catalog import export_catalog

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


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def source_url(path: str) -> str:
    return f"https://www.mathworks.com/help/releases/{RELEASE}/simulink/{path}"


def fetch(entry: dict[str, str], cache: Path) -> tuple[dict[str, str], Path]:
    path = entry["path"]
    target = cache / f"{RELEASE}-{path.replace('/', '-')}"
    if not target.exists():
        response = requests.get(source_url(path), timeout=45)
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


def html_to_markdown(html: bytes, entry: dict[str, str]) -> str:
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
    family = slug(entry["category"])
    lines = [
        "---",
        "type: simulink-block",
        f"title: {entry['name']!r}",
        f"family: {family}",
        f"documentation_release: {RELEASE}",
        f"official_category: {entry['category']!r}",
        f"documentation_page: {Path(entry['path']).stem!r}",
        "---",
        "",
        f"# {entry['name']}",
        "",
        subtitle,
        "",
    ]
    library = next(
        (p for p in main.find_all("p") if p.get_text(" ", strip=True).startswith("Libraries:")),
        None,
    )
    if library:
        library_text = " ".join(
            library.get_text(" ", strip=True).removeprefix("Libraries:").split()
        )
        lines.extend(["## Libraries", "", library_text, ""])

    for section in main.select("div.refsect1.description, div.ref_sect"):
        section_heading = section.find("h2", recursive=False)
        if section_heading is None:
            continue
        title = section_heading.get_text(" ", strip=True)
        if title not in SECTIONS:
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
            lines.extend([f"## {title}", "", markdown, ""])
    if len(lines) < 14:
        raise ValueError(f"No usable documentation sections for {entry['name']}")
    return "\n".join(lines).strip() + "\n"


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

    # Fetch each distinct document once, then render it into every official category.
    distinct = {entry["path"]: entry for entry in entries}
    fetched: dict[str, Path] = {}
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch, entry, args.cache): path for path, entry in distinct.items()}
        for future in concurrent.futures.as_completed(futures):
            path = futures[future]
            try:
                entry, target = future.result()
                fetched[path] = target
                print(f"FETCHED {path}", flush=True)
            except Exception as exc:
                failures.append((path, str(exc)))
                print(f"FAILED {path}: {exc}", flush=True)
    if failures and not args.offline:
        raise SystemExit(f"Refusing to write an incomplete catalog: {len(failures)} failures")

    written = 0
    render_failures = []
    for entry in entries:
        try:
            markdown = html_to_markdown(fetched[entry["path"]].read_bytes(), entry)
            family = slug(entry["category"])
            target = args.output / family / f"{slug(entry['name'])}.md"
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

    export_catalog(args.output)
    if failures:
        report = ["# 未完成抓取", ""] + [f"- {path}: {error}" for path, error in failures]
        (args.output / "scrape-failures.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Wrote {written} official directory entries; {len(failures)} fetch failures")


if __name__ == "__main__":
    main()
