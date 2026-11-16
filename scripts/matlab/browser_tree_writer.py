#!/usr/bin/env python3
"""Materialize an aligned R2025b Browser manifest as bilingual Markdown."""

from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path


def normalize_block_document(document: str, language: str) -> str:
    """Load the parser's pure normalization helper without package startup."""
    path = Path(__file__).parents[2] / "openviking/parse/parsers/matlab/library.py"
    spec = importlib.util.spec_from_file_location("matlab_block_library", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.normalize_block_document(document, language=language)


def resource_component(value: str) -> str:
    return value.replace("/", "／").replace("\x00", "")


def tree_only_page(product: dict, library: dict, block: dict, language: str) -> str:
    """Keep a real local Browser block without fabricating reference content."""
    localized = "zh-CN" if language == "zh" else "en"
    category = " / ".join([product["name"], *library["path"]])
    lines = [
        "---",
        "type: simulink-block",
        f"title: {block['name']!r}",
        f"family: {product['id']!r}",
        f"product_id: {product['id']!r}",
        f"product_name: {product['name']!r}",
        "documentation_release: R2025b",
        f"official_category: {category!r}",
        f"language: {localized}",
        "documentation_status: tree_only",
        "---",
        "",
        f"# {block['name']}",
        "",
        (
            "该块存在于本机 R2025b Library Browser 树中，但没有可安全复用的独立官方参考正文。"
            if language == "zh"
            else "This block occurs in the local R2025b Library Browser tree, but no unambiguous standalone official reference page is available."
        ),
        "",
    ]
    return normalize_block_document("\n".join(lines), language=language)


def write_browser_tree(manifest: dict, root: Path) -> None:
    """Write exactly the manifest's local products, directories and blocks."""
    if "totals" not in manifest:
        from extract_r2025b_block_manifest import refresh_totals

        refresh_totals(manifest)
    products = manifest["products"]
    source_documents = {
        (id(block), language): (root / document["path"]).read_text(encoding="utf-8")
        for product in products
        for library in product["libraries"]
        for block in library["blocks"]
        for language, document in block["documents"].items()
        if document["status"] == "available" and document["path"]
    }
    canonical_document_paths = {}
    for language in ("en", "zh"):
        browser_root = root / language
        shutil.rmtree(browser_root, ignore_errors=True)
        browser_root.mkdir(parents=True, exist_ok=True)
        root_index = [
            "# Simulink Library Browser" if language == "en" else "# Simulink 库浏览器",
            "",
        ]
        for product in products:
            product_parts = (resource_component(product["name"]),)
            nodes = {(product_parts): {"name": product["name"], "blocks": []}}
            for library in product["libraries"]:
                if not library["blocks"] and not manifest.get("tree_source"):
                    continue
                parts = (
                    *product_parts,
                    *(resource_component(part) for part in library["path"]),
                )
                for depth in range(1, len(parts) + 1):
                    key = tuple(parts[:depth])
                    display = product["name"] if depth == 1 else library["path"][depth - 2]
                    nodes.setdefault(key, {"name": display, "blocks": []})
                nodes[tuple(parts)]["blocks"].extend(library["blocks"])
                name_counts = {}
                for block in library["blocks"]:
                    filename = resource_component(block["name"])
                    name_counts[filename] = name_counts.get(filename, 0) + 1
                for block in library["blocks"]:
                    filename = resource_component(block["name"])
                    if name_counts[filename] > 1:
                        source_name = block.get("documentation_path") or "tree-only"
                        filename += "-" + resource_component(Path(source_name).stem)
                    filename += ".md"
                    block["resource_name"] = filename
                    target = browser_root.joinpath(*parts, filename)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    document = block["documents"][language]
                    if document["status"] == "available" and document["path"]:
                        content = source_documents[(id(block), language)]
                    elif block["documentation_path"]:
                        content = f"# {block['name']}\n\n{block['summary']}\n\n" + (
                            "完整中英文正文待补。\n"
                            if language == "zh"
                            else "Full English and Chinese documentation is pending.\n"
                        )
                    else:
                        content = tree_only_page(product, library, block, language)
                    target.write_text(content, encoding="utf-8")
                    relative = target.relative_to(root).as_posix()
                    block.setdefault("resource_paths", {})[language] = relative
                    if block["documentation_path"]:
                        key = (
                            product["id"],
                            block["documentation_path"],
                            block.get("source_release", "R2025b"),
                            language,
                        )
                        document["path"] = canonical_document_paths.setdefault(key, relative)
            for key, node in nodes.items():
                directory = browser_root.joinpath(*key)
                directory.mkdir(parents=True, exist_ok=True)
                children = [
                    candidate
                    for candidate in nodes
                    if len(candidate) == len(key) + 1 and candidate[:-1] == key
                ]
                lines = [f"# {node['name']}", ""]
                if not node["blocks"] and not children:
                    lines.append(
                        "- 实机 R2025b 树中的空目录（0 块）。"
                        if language == "zh"
                        else "- Empty directory in the local R2025b tree (0 blocks)."
                    )
                lines.extend(
                    f"- [{nodes[child]['name']}]({child[-1]}/index.md)" for child in children
                )
                for block in node["blocks"]:
                    filename = block.get("resource_name", resource_component(block["name"]) + ".md")
                    lines.append(f"- [{block['name']}]({filename})")
                (directory / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        for product in products:
            directory = resource_component(product["name"])
            root_index.append(f"- [{product['name']}]({directory}/index.md)")
        (browser_root / "index.md").write_text("\n".join(root_index) + "\n", encoding="utf-8")

    totals = manifest["totals"]
    (root / "README.md").write_text(
        "# Simulink Block Library\n\n"
        "MATLAB/Simulink R2025b 资源添加时使用的本地块参考库。"
        "`zh/` 和 `en/` 的顶层库、子目录、块名及顺序严格对应 "
        "`scripts/matlab/tree_full.md`；解析器按块原始名称及 `SourceBlock` 匹配文档，无需联网。\n\n"
        "- [中文块库](zh/index.md)\n"
        "- [English block library](en/index.md)\n\n"
        f"当前包含 {totals['products']} 个顶层库、{totals['block_occurrences']} 个块条目，"
        "所有保留块都有完整中英文官方正文或经结构校验的中文工作译本。"
        "实机树中的示例、启动器、产品链接及查无官方块页的条目已按 "
        "`r2025b-block-exclusions.json` 剔除，目录层级保持不变。"
        "预配置变体复用对应基础块官方页；少数支持包老块使用页面标注的实际旧版官方文档。\n\n"
        "`manifest.json` 是解析器和离线生成脚本使用的机器元数据，不是 OV 资源页面。"
        "重新生成使用 `scripts/matlab/` 下的 R2025b 脚本；缓存和失败日志保存在库目录之外。\n",
        encoding="utf-8",
    )
    (root / "index.md").unlink(missing_ok=True)
    for redundant in ("browser", "catalog", "products"):
        shutil.rmtree(root / redundant, ignore_errors=True)
    for report_name in (
        "library-browser-reconciliation.md",
        "scrape-failures.json",
        "scrape-failures.md",
        "translation-failures.json",
    ):
        (root / report_name).unlink(missing_ok=True)
