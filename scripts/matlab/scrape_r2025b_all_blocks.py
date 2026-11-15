#!/usr/bin/env python3
"""Fetch full English and official-Chinese pages for the all-product manifest.

Documents are stored once per product/documentation path. Library occurrences
link to these files. Failures and untranslated pages remain explicit; no page
is generated from a block name or from guessed ports and parameters.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import threading
import time
from pathlib import Path

import requests
from extract_r2025b_block_manifest import (
    RELEASE,
    manifest_failures,
    refresh_totals,
    report,
    write_browser_tree,
    write_catalog,
)
from scrape_simulink_blocks import localized_content

from openviking.parse.parsers.matlab.library import normalize_block_document

_PRINT_LOCK = threading.Lock()


def source_url(product: str, path: str, language: str) -> str:
    host = "ww2.mathworks.cn" if language == "zh" else "www.mathworks.com"
    return f"https://{host}/help/releases/{RELEASE}/{product}/{path}"


def fetch(product: str, path: str, language: str, cache: Path, offline: bool) -> Path:
    target = cache / product / language / f"{path}.html"
    if target.exists():
        return target
    if offline:
        raise FileNotFoundError(f"Offline HTML is missing: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(7):
        response = requests.get(source_url(product, path, language), timeout=60)
        if response.ok:
            target.write_bytes(response.content)
            return target
        if response.status_code == 404:
            raise ValueError("missing: official documentation returned 404")
        if response.status_code in {401, 403}:
            raise ValueError(f"access_denied: HTTP {response.status_code}")
        if response.status_code != 429:
            raise ValueError(f"fetch_failed: HTTP {response.status_code}")
        time.sleep(min(2**attempt, 30))
    raise ValueError("fetch_failed: repeated HTTP 429")


def render_page(html: bytes, entry: dict, product: dict, language: str) -> tuple[str, bool]:
    subtitle, sections = localized_content(html, entry, "zh-CN" if language == "zh" else "en")
    official_chinese = language == "en" or bool(re.search(r"[\u4e00-\u9fff]", subtitle))
    if language == "zh" and not official_chinese:
        raise ValueError("translation_required: MathWorks page has no official Chinese body")
    if not sections:
        raise ValueError("missing: no usable block-documentation sections")
    metadata = [
        "---",
        "type: simulink-block",
        f"title: {entry['name']!r}",
        f"family: {product['id']!r}",
        f"product_id: {product['id']!r}",
        f"product_name: {product['name']!r}",
        f"documentation_release: {RELEASE}",
        f"official_category: {' / '.join(entry['library_path'])!r}",
        f"documentation_page: {Path(entry['documentation_path']).stem!r}",
        f"documentation_source_path: {entry['documentation_path']!r}",
        f"language: {'zh-CN' if language == 'zh' else 'en'}",
    ]
    if language == "zh":
        metadata.append("chinese_source: official")
    lines = [*metadata, "---", "", f"# {entry['name']}", "", subtitle, ""]
    for title, content in sections:
        lines.extend([f"## {title}", "", content, ""])
    return normalize_block_document("\n".join(lines), language=language), official_chinese


def unique_entries(product: dict) -> list[dict]:
    entries = {}
    for library in product["libraries"]:
        for block in library["blocks"]:
            entries.setdefault(
                block["documentation_path"], {**block, "library_path": library["path"]}
            )
    return list(entries.values())


def process(
    product: dict,
    entry: dict,
    root: Path,
    cache: Path,
    offline: bool,
) -> tuple[dict, list[dict]]:
    statuses = {}
    failures = []
    for language in ("en", "zh"):
        relative = (
            f"{language}/products/{product['id']}/"
            f"{Path(entry['documentation_path']).with_suffix('.md')}"
        )
        try:
            html = fetch(
                product["id"], entry["documentation_path"], language, cache, offline
            ).read_bytes()
            markdown, _ = render_page(html, entry, product, language)
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
            statuses[language] = {"status": "available", "path": relative}
        except Exception as exc:
            reason = str(exc)
            status = reason.split(":", 1)[0]
            if status not in {
                "missing",
                "access_denied",
                "fetch_failed",
                "translation_required",
            }:
                status = "missing"
            statuses[language] = {"status": status, "path": None}
            failures.append(
                {
                    "product": product["id"],
                    "path": entry["documentation_path"],
                    "language": language,
                    "status": status,
                    "error": reason,
                }
            )
    return statuses, failures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", action="append", help="Only this product; repeatable")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).parents[2]
        / "openviking/parse/parsers/matlab/simulink-block-library/manifest.json",
    )
    parser.add_argument("--cache", type=Path, default=Path("/tmp/r2025b-block-docs"))
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    selected = set(args.product or [])
    products = [
        product
        for product in manifest["products"]
        if product["status"] == "enumerated" and (not selected or product["id"] in selected)
    ]
    unknown = selected - {product["id"] for product in products}
    if unknown:
        raise SystemExit(f"Unknown or blockless products: {sorted(unknown)}")
    work = [(product, entry) for product in products for entry in unique_entries(product)]
    root = args.manifest.parent
    all_failures = []
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(process, product, entry, root, args.cache, args.offline): (
                product,
                entry,
            )
            for product, entry in work
        }
        for future in concurrent.futures.as_completed(futures):
            product, entry = futures[future]
            try:
                statuses, failures = future.result()
            except Exception as exc:
                failures = [
                    {
                        "product": product["id"],
                        "path": entry["documentation_path"],
                        "language": "both",
                        "status": "fetch_failed",
                        "error": str(exc),
                    }
                ]
                statuses = {}
            all_failures.extend(failures)
            for library in product["libraries"]:
                for block in library["blocks"]:
                    if block["documentation_path"] == entry["documentation_path"]:
                        block["documents"].update(statuses)
            completed += 1
            if completed % 10 == 0 or completed == len(work):
                with _PRINT_LOCK:
                    print(
                        f"{completed}/{len(work)} documents; {len(all_failures)} language gaps",
                        flush=True,
                    )
    refresh_totals(manifest)
    args.manifest.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    write_catalog(manifest, root)
    write_browser_tree(manifest, root)
    failure_path = root / "scrape-failures.json"
    all_failures = manifest_failures(manifest)
    failure_path.write_text(
        json.dumps(all_failures, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    docs = Path(__file__).parents[2] / "docs"
    en, zh = report(manifest)
    (docs / "en/reference/matlab-block-library-coverage.md").write_text(en, encoding="utf-8")
    (docs / "zh/reference/matlab-block-library-coverage.md").write_text(zh, encoding="utf-8")
    print(json.dumps(manifest["totals"], ensure_ascii=False, indent=2))
    if all_failures:
        print(f"Explicit gaps: {failure_path}")


if __name__ == "__main__":
    main()
