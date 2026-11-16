#!/usr/bin/env python3
"""Translate English block pages that have no official Chinese documentation.

Requires a caller-supplied OV JSON config with a ``vlm`` chat-completions
endpoint. Credentials are read at runtime and are never written to the library.
Raw translations are cached outside the repository for resumable runs.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import time
from pathlib import Path

import requests
from extract_r2025b_block_manifest import (
    manifest_failures,
    refresh_totals,
    report,
    write_browser_tree,
    write_catalog,
)
from scrape_r2025b_all_blocks import unique_entries


def source_parts(markdown: str) -> tuple[list[str], str]:
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", markdown, re.DOTALL)
    if not match:
        raise ValueError("Generated English page has no front matter")
    return match.group(1).splitlines(), match.group(2).strip()


def table_shapes(markdown: str) -> list[int]:
    """Return row counts for actual Markdown tables, not enum values with pipes."""
    lines = markdown.splitlines()
    shapes = []
    index = 0
    while index < len(lines):
        if (
            lines[index].startswith("|")
            and index + 1 < len(lines)
            and re.match(r"^\|\s*:?-{3,}", lines[index + 1])
        ):
            rows = 0
            while index < len(lines) and lines[index].startswith("|"):
                rows += 1
                index += 1
            shapes.append(rows)
        else:
            index += 1
    return shapes


def validate_translation(source: str, translated: str) -> None:
    if len(translated) < len(source) * 0.25:
        raise ValueError(f"translation too short: {len(translated)} vs {len(source)}")
    source_headings = len(re.findall(r"^#{1,6} ", source, re.MULTILINE))
    translated_headings = len(re.findall(r"^#{1,6} ", translated, re.MULTILINE))
    if translated_headings != source_headings:
        raise ValueError(f"heading count changed: {translated_headings} vs {source_headings}")
    source_shapes = table_shapes(source)
    translated_shapes = table_shapes(translated)
    if translated_shapes != source_shapes:
        raise ValueError(f"table shapes changed: {translated_shapes} vs {source_shapes}")
    if not re.search(r"[\u4e00-\u9fff]", translated):
        raise ValueError("translation contains no Chinese text")


def split_source(source: str, limit: int = 16000) -> list[str]:
    """Split large reference pages at headings without dropping table rows."""
    units = re.split(r"(?=^#{1,4} )", source, flags=re.MULTILINE)
    chunks = []
    current = ""
    for unit in units:
        if len(current) + len(unit) <= limit:
            current += unit
            continue
        if current:
            chunks.append(current)
            current = ""
        while len(unit) > limit:
            cut = unit.rfind("\n\n", 0, limit)
            if cut < limit // 2:
                cut = limit
            if cut < len(unit) and unit[cut] != "\n":
                cut = unit.rfind("\n", 0, cut) + 1
            before = unit[:cut].rstrip()
            after = unit[cut:].lstrip()
            # Never split a Markdown table between rows. A long table is sent
            # as one chunk because dropping rows is worse than a larger prompt.
            if (
                before.splitlines()
                and before.splitlines()[-1].startswith("|")
                and after.splitlines()
                and after.splitlines()[0].startswith("|")
            ):
                table_start = unit.rfind("\n\n", 0, cut)
                table_end = unit.find("\n\n", cut)
                cut = table_start if table_start >= limit // 2 else table_end
                if cut <= 0:
                    cut = len(unit)
            chunks.append(unit[:cut])
            unit = unit[cut:]
        current = unit
    if current:
        chunks.append(current)
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--product", action="append")
    parser.add_argument("--path", action="append", help="Only this documentation path; repeatable")
    parser.add_argument(
        "--selection",
        type=Path,
        help="JSON array of [product, documentation_path] pairs to translate",
    )
    parser.add_argument(
        "--force", action="store_true", help="Retranslate even when Chinese is available"
    )
    parser.add_argument("--limit", type=int)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--chunk-workers", type=int, default=1)
    parser.add_argument("--chunk-size", type=int, default=16000)
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).parents[2]
        / "openviking/parse/parsers/matlab/simulink-block-library/manifest.json",
    )
    parser.add_argument("--cache", type=Path, default=Path("/tmp/r2025b-block-translations"))
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))["vlm"]
    url = config["api_base"].rstrip("/") + "/chat/completions"
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json",
    }
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    selected = set(args.product or [])
    selected_paths = set(args.path or [])
    selection = (
        {tuple(item) for item in json.loads(args.selection.read_text(encoding="utf-8"))}
        if args.selection
        else None
    )
    work = []
    for product in manifest["products"]:
        if selected and product["id"] not in selected:
            continue
        for entry in unique_entries(product):
            if selected_paths and entry["documentation_path"] not in selected_paths:
                continue
            if (
                selection is not None
                and (product["id"], entry["documentation_path"]) not in selection
            ):
                continue
            if entry["documents"]["en"]["status"] == "available" and (
                args.force or entry["documents"]["zh"]["status"] != "available"
            ):
                work.append((product, entry))
    if args.limit:
        work = work[: args.limit]
    print(f"TRANSLATING {len(work)} unique documents", flush=True)

    def translate(item) -> tuple[dict, str, int]:
        product, entry = item
        english_relative = entry["documents"]["en"]["path"]
        english_path = args.manifest.parent / english_relative
        metadata, source = source_parts(english_path.read_text(encoding="utf-8"))
        relative = (
            f"zh/products/{product['id']}/{Path(entry['documentation_path']).with_suffix('.md')}"
        )
        target = args.manifest.parent / relative
        cached = args.cache / product["id"] / Path(entry["documentation_path"]).with_suffix(".md")
        if cached.exists() and cached.stat().st_size > 100:
            translated = cached.read_text(encoding="utf-8").strip()
        else:

            def translate_chunk(chunk: str) -> str:
                prompt = (
                    "将下面 Simulink 模块文档完整翻译成简体中文。保留 Markdown 表格、标题层级和缩进；"
                    "模块名、信号名、变量名、函数名、参数 programmatic 标识符、代码、文件路径、"
                    "枚举值（如 on/off）、数据类型和单位保持原文，不要翻译或改写。"
                    "技术描述必须准确，不得省略任何段落、表格行或参数。一级标题模块名保持原文。"
                    "将 Description、Ports、Parameters、Libraries、Block Characteristics、"
                    "Extended Capabilities、Version History 分别译为描述、端口、参数、所属库、"
                    "模块特性、扩展功能、版本历史。仅输出翻译后的 Markdown 正文，不要代码围栏，不要解释。\n\n"
                    + chunk
                )
                payload = {
                    "model": config["model"],
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": args.temperature,
                    "max_tokens": 32768,
                }
                for attempt in range(5):
                    try:
                        response = requests.post(url, headers=headers, json=payload, timeout=360)
                        response.raise_for_status()
                        result = response.json()["choices"][0]["message"]["content"].strip()
                        if result.startswith("```"):
                            result = re.sub(r"^```(?:markdown)?\s*|\s*```$", "", result).strip()
                        validate_translation(chunk, result)
                        return result
                    except Exception:
                        if attempt == 4:
                            raise
                        time.sleep(5 * (attempt + 1))
                raise AssertionError("unreachable")

            chunks = split_source(source, args.chunk_size)
            if args.chunk_workers > 1:
                with concurrent.futures.ThreadPoolExecutor(
                    max_workers=args.chunk_workers
                ) as chunk_pool:
                    translated_chunks = list(chunk_pool.map(translate_chunk, chunks))
            else:
                translated_chunks = [translate_chunk(chunk) for chunk in chunks]
            translated = "\n\n".join(translated_chunks).strip()
            validate_translation(source, translated)
            cached.parent.mkdir(parents=True, exist_ok=True)
            cached.write_text(translated + "\n", encoding="utf-8")
        validate_translation(source, translated)
        chinese_metadata = []
        for line in metadata:
            if line.startswith("language:"):
                line = "language: zh-CN"
            chinese_metadata.append(line)
        chinese_metadata.append("chinese_source: worker-translation")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            "---\n" + "\n".join(chinese_metadata) + "\n---\n\n" + translated + "\n",
            encoding="utf-8",
        )
        return {"status": "available", "path": relative}, "translated", len(translated)

    failures = []
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(translate, item): item for item in work}
        for future in concurrent.futures.as_completed(futures):
            product, entry = futures[future]
            try:
                status, _, size = future.result()
                for library in product["libraries"]:
                    for block in library["blocks"]:
                        if block["documentation_path"] == entry["documentation_path"]:
                            block["documents"]["zh"] = status
                completed += 1
                if completed % 10 == 0 or completed == len(work):
                    print(
                        f"{completed}/{len(work)} translated; last {size} chars; {len(failures)} failures",
                        flush=True,
                    )
            except Exception as exc:
                failures.append(
                    {
                        "product": product["id"],
                        "path": entry["documentation_path"],
                        "error": str(exc),
                    }
                )
                print(f"FAILED {product['id']}:{entry['documentation_path']}: {exc}", flush=True)
    refresh_totals(manifest)
    args.manifest.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    write_catalog(manifest, args.manifest.parent)
    write_browser_tree(manifest, args.manifest.parent)
    remaining = manifest_failures(manifest)
    (args.manifest.parent / "scrape-failures.json").write_text(
        json.dumps(remaining, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    docs = Path(__file__).parents[2] / "docs"
    en, zh = report(manifest)
    (docs / "en/reference/matlab-block-library-coverage.md").write_text(en, encoding="utf-8")
    (docs / "zh/reference/matlab-block-library-coverage.md").write_text(zh, encoding="utf-8")
    (args.manifest.parent / "translation-failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest["totals"], ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(f"{len(failures)} translations failed; resume after reviewing the log")


if __name__ == "__main__":
    main()
