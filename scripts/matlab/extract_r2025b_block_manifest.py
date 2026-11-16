#!/usr/bin/env python3
"""Enumerate every block in the official R2025b MathWorks product catalog.

The unit of completeness is the official product -> category -> block XML tree,
not the 20 hand-picked categories on the Simulink Blocks web page. Products with
no block XML are retained explicitly. Documentation availability is tracked
separately: an enumerated block is not represented as a scraped full document.

Network use is only needed to refresh the cache. The checked-in manifest and
coverage reports can be rebuilt offline from a previously populated cache.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import shutil
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
from bs4 import BeautifulSoup

RELEASE = "R2025b"
CATALOG = f"https://www.mathworks.com/help/releases/{RELEASE}/"
MIRRORS = (
    f"https://www.mathworks.com/help/releases/{RELEASE}/",
    f"https://ww2.mathworks.cn/help/releases/{RELEASE}/",
)
EXPECTED = {
    "products": 133,
    "products_with_blocks": 74,
    "products_without_block_library": 59,
    "block_occurrences": 5431,
    "unique_product_document_paths": 4603,
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def children(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in element if local_name(child.tag) == name]


def text(element: ET.Element | None) -> str:
    return " ".join("".join(element.itertext()).split()) if element is not None else ""


def get(url: str, timeout: int = 45) -> requests.Response:
    error = ""
    for attempt in range(6):
        response = requests.get(url, timeout=timeout)
        if response.ok:
            return response
        error = f"{response.status_code} {url}"
        if response.status_code != 429:
            break
        time.sleep(min(2**attempt, 20))
    raise RuntimeError(error)


def discover_products(cache: Path, offline: bool) -> list[dict[str, str]]:
    target = cache / "_catalog.html"
    if not target.exists():
        if offline:
            raise FileNotFoundError(f"Offline product catalog is missing: {target}")
        target.write_bytes(get(CATALOG).content)
    soup = BeautifulSoup(target.read_bytes(), "html.parser")
    prefix = f"/help/releases/{RELEASE}/"
    products: dict[str, str] = {}
    for link in soup.select("a[href]"):
        href = link["href"].split("?", 1)[0]
        if not href.startswith(prefix) or not href.endswith("/index.html"):
            continue
        product = href[len(prefix) :].split("/", 1)[0]
        if product and href == f"{prefix}{product}/index.html":
            products[product] = " ".join(link.stripped_strings)
    if not products:
        raise ValueError("No products discovered in the official release catalog")
    return [{"id": key, "name": products[key]} for key in sorted(products)]


def fetch_product(product: dict[str, str], cache: Path, offline: bool) -> str:
    target = cache / f"{product['id']}.xml"
    if target.exists():
        return "cached"
    missing = cache / f"{product['id']}.missing"
    if offline:
        return "no_block_library" if missing.exists() else "not_fetched"
    for mirror in MIRRORS:
        url = f"{mirror}{product['id']}/referencelist_block_cat.xml"
        try:
            response = get(url)
        except RuntimeError as exc:
            if str(exc).startswith("404 "):
                continue
            return f"error: {exc}"
        target.write_bytes(response.content)
        missing.unlink(missing_ok=True)
        return "fetched"
    missing.write_text("Official product has no referencelist_block_cat.xml\n", encoding="utf-8")
    return "no_block_library"


def parse_product(
    product: dict[str, str], cache: Path, old_documents: dict, document_root: Path
) -> dict:
    path = cache / f"{product['id']}.xml"
    result = {
        **product,
        "documentation_index": f"{product['id']}/index.html",
        "block_catalog": f"{product['id']}/referencelist_block_cat.xml",
        "status": "enumerated" if path.exists() else "no_block_library",
        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None,
        "libraries": [],
        "block_occurrences": 0,
        "unique_document_paths": 0,
    }
    if not path.exists():
        return result
    root = ET.parse(path).getroot()
    paths: set[str] = set()

    def visit(category: ET.Element, ancestry: list[dict[str, str]]) -> None:
        for child in category:
            if local_name(child.tag) not in {"cat", "sub"}:
                continue
            title = text(next(iter(children(child, "title")), None))
            if not title:
                continue
            lineage = [*ancestry, {"name": title, "target": child.get("target", "")}]
            blocks = []
            for ref in children(child, "ref"):
                reference_type = ref.get("type", "")
                if not reference_type.endswith("block"):
                    continue
                document_path = ref.get("target", "")
                name = ref.get("name", "")
                old = old_documents.get((document_path, name))
                if not old:
                    generated = {
                        language: f"{language}/products/{product['id']}/{Path(document_path).with_suffix('.md')}"
                        for language in ("en", "zh")
                    }
                    if all((document_root / path).is_file() for path in generated.values()):
                        old = generated
                blocks.append(
                    {
                        "name": name,
                        "type": reference_type,
                        "documentation_path": document_path,
                        "summary": text(next(iter(children(ref, "purpose")), None)),
                        "introduced": ref.get("data-swrelease"),
                        "updated": (ref.get("data-updaterels", "").split()),
                        "documents": {
                            language: (
                                {"status": "available", "path": old[language]}
                                if old
                                else {"status": "pending", "path": None}
                            )
                            for language in ("en", "zh")
                        },
                    }
                )
                paths.add(document_path)
            # Keep empty library nodes too: they are part of the official tree.
            result["libraries"].append(
                {
                    "path": [part["name"] for part in lineage],
                    "targets": [part["target"] for part in lineage],
                    "blocks": blocks,
                }
            )
            result["block_occurrences"] += len(blocks)
            visit(child, lineage)

    top = next(iter(children(root, "cat")), None)
    if top is None:
        raise ValueError(f"No root library category: {path}")
    visit(top, [])
    result["unique_document_paths"] = len(paths)
    return result


def old_document_index(path: Path) -> dict:
    if not path.exists():
        return {}
    entries = json.loads(path.read_text(encoding="utf-8"))
    return {
        (entry["path"], entry["name"]): {
            language: f"{language}/{slug(entry['category'])}/{slug(entry['name'])}.md"
            for language in ("en", "zh")
        }
        for entry in entries
    }


def existing_document_index(path: Path, product_id: str) -> dict:
    """Preserve canonical document paths without crossing product boundaries."""
    if not path.exists():
        return {}
    manifest = json.loads(path.read_text(encoding="utf-8"))
    return {
        (block["documentation_path"], block["name"]): {
            language: block["documents"][language]["path"] for language in ("en", "zh")
        }
        for product in manifest.get("products", [])
        if product["id"] == product_id
        for library in product["libraries"]
        for block in library["blocks"]
        if all(block["documents"][language]["path"] for language in ("en", "zh"))
    }


def refresh_totals(manifest: dict) -> None:
    products = manifest["products"]
    totals = {
        "products": len(products),
        "products_with_blocks": sum(p["status"] == "enumerated" for p in products),
        "products_without_block_library": sum(p["status"] == "no_block_library" for p in products),
        "block_occurrences": sum(p["block_occurrences"] for p in products),
        "unique_product_document_paths": sum(p["unique_document_paths"] for p in products),
    }
    occurrences = [
        block
        for product in products
        for library in product["libraries"]
        for block in library["blocks"]
    ]
    all_paths = {
        (product["id"], block["documentation_path"], language)
        for product in products
        for library in product["libraries"]
        for block in library["blocks"]
        for language in ("en", "zh")
    }
    available_paths = {
        (product["id"], block["documentation_path"], language)
        for product in products
        for library in product["libraries"]
        for block in library["blocks"]
        for language in ("en", "zh")
        if block["documents"][language]["status"] == "available"
    }
    totals["full_document_occurrences"] = {
        language: sum(
            block["documents"][language]["status"] == "available" for block in occurrences
        )
        for language in ("en", "zh")
    }
    totals["full_documents"] = {
        language: sum(key[2] == language for key in available_paths) for language in ("en", "zh")
    }
    totals["pending_documents"] = {
        language: sum(key[2] == language for key in all_paths - available_paths)
        for language in ("en", "zh")
    }
    manifest["totals"] = totals


def manifest_failures(manifest: dict) -> list[dict]:
    failures = []
    seen = set()
    for product in manifest["products"]:
        for library in product["libraries"]:
            for block in library["blocks"]:
                for language in ("en", "zh"):
                    document = block["documents"][language]
                    key = (product["id"], block["documentation_path"], language)
                    if document["status"] == "available" or key in seen:
                        continue
                    seen.add(key)
                    failures.append(
                        {
                            "product": product["id"],
                            "path": block["documentation_path"],
                            "language": language,
                            "status": document["status"],
                            "error": f"{document['status']}: see scraper or translation log",
                        }
                    )
    return failures


def report(manifest: dict) -> tuple[str, str]:
    totals = manifest["totals"]
    products = manifest["products"]
    english = [
        f"# MathWorks {RELEASE} block-library coverage",
        "",
        "Completeness is measured against every official product `referencelist_block_cat.xml`, including all nested categories and both `block` and `simscapeblock` references. An occurrence is a block at one library location; the same documentation path can occur in several libraries.",
        "",
        f"- Official catalog entries: **{totals['products']}**",
        f"- Products with an enumerated block library: **{totals['products_with_blocks']}**",
        f"- Products without an official block-library XML: **{totals['products_without_block_library']}** (not silently counted as empty third-party libraries)",
        f"- Product/library/block occurrences: **{totals['block_occurrences']}**",
        f"- Unique product/documentation paths: **{totals['unique_product_document_paths']}**",
        f"- Existing full English pages: **{totals['full_documents']['en']}**; Chinese pages: **{totals['full_documents']['zh']}**",
        f"- Pending full English pages: **{totals['pending_documents']['en']}**; Chinese pages: **{totals['pending_documents']['zh']}**",
        "",
        "Third-party, support-package and locally licensed libraries are outside this public product catalog. They must be enumerated from the user's MATLAB installation and are not fabricated here. HTTP failures, license-denied pages and fetch failures are represented as gaps, never as successful documents.",
        "",
        "| Product | Library entries | Unique document paths | Status |",
        "| --- | ---: | ---: | --- |",
    ]
    chinese = [
        f"# MathWorks {RELEASE} 块库覆盖与缺口",
        "",
        "完整性以每个官方产品的 `referencelist_block_cat.xml` 为准，递归保留所有子库以及 `block`、`simscapeblock`。条目数表示块在库中的出现次数，同一文档可以属于多个库。",
        "",
        f"- 官方产品目录条目：**{totals['products']}**",
        f"- 枚举到块库的产品：**{totals['products_with_blocks']}**",
        f"- 没有官方块库 XML 的产品：**{totals['products_without_block_library']}**（不是静默跳过，也不冒充第三方空库）",
        f"- 产品→库→块条目：**{totals['block_occurrences']}**",
        f"- 产品内独立文档路径：**{totals['unique_product_document_paths']}**",
        f"- 已有完整英文文档：**{totals['full_documents']['en']}**；中文文档：**{totals['full_documents']['zh']}**",
        f"- 待补完整英文文档：**{totals['pending_documents']['en']}**；中文文档：**{totals['pending_documents']['zh']}**",
        "",
        "第三方、硬件支持包和用户本机授权库不在公开产品总目录内，需要从用户 MATLAB 安装实例枚举，不能凭空生成。抓取失败、无权限和正文缺失都单独记为缺口，不把只有元数据的条目称为完整文档。",
        "",
        "| 产品 | 库中块条目 | 独立文档路径 | 状态 |",
        "| --- | ---: | ---: | --- |",
    ]
    for product in products:
        status = (
            "enumerated / 已枚举"
            if product["status"] == "enumerated"
            else "no block XML / 无块库 XML"
        )
        row = f"| {product['name']} (`{product['id']}`) | {product['block_occurrences']} | {product['unique_document_paths']} | {status} |"
        english.append(row)
        chinese.append(row)
    return "\n".join(english) + "\n", "\n".join(chinese) + "\n"


# Top-level order from the requester's R2025b Library Browser. The two
# canonical language directories contain only this installation profile.
BROWSER_PRODUCTS = [
    ("Simulink", "simulink"),
    ("Aerospace Blockset", "aeroblks"),
    ("Audio Toolbox", "audio"),
    ("Automated Driving Toolbox", "driving"),
    ("AUTOSAR Blockset", "autosar"),
    ("C2000 Microcontroller Blockset", "ti-c2000"),
    ("Communications Toolbox", "comm"),
    ("Communications Toolbox HDL Support", "communications-toolbox-hdl-support"),
    ("Computer Vision Toolbox", "vision"),
    ("Control System Toolbox", "control"),
    ("Data Acquisition Toolbox", "daq"),
    ("DDS Blockset", "dds"),
    ("Deep Learning Toolbox", "deeplearning"),
    ("DSP HDL Toolbox", "dsphdl"),
    ("DSP System Toolbox", "dsp"),
    ("DSP System Toolbox HDL Support", "dsp-system-toolbox-hdl-support"),
    ("Embedded Coder", "ecoder"),
    ("Fixed-Point Designer", "fixedpoint"),
    ("Fixed-Point Designer HDL Support", "fixed-point-designer-hdl-support"),
    ("Fuzzy Logic Toolbox", "fuzzy"),
    ("HDL Coder", "hdlcoder"),
    ("HDL Verifier", "hdlverifier"),
    ("Image Acquisition Toolbox", "imaq"),
    ("Industrial Communication Toolbox", "icomm"),
    ("Instrument Control Toolbox", "instrument"),
    ("Lidar Toolbox", "lidar"),
    ("Mixed-Signal Blockset", "msblks"),
    ("Model Predictive Control Toolbox", "mpc"),
    ("Motor Control Blockset", "mcb"),
    ("Motor Control Blockset HDL Support", "motor-control-blockset-hdl-support"),
    ("Navigation Toolbox", "nav"),
    ("Phased Array System Toolbox", "phased"),
    ("Powertrain Blockset", "autoblks"),
    ("Radar Toolbox", "radar"),
    ("Reinforcement Learning Toolbox", "reinforcement-learning"),
    ("Report Generator", "report-generator"),
    ("Requirements Toolbox", "slrequirements"),
    ("RF Blockset", "simrf"),
    ("Robotics System Toolbox", "robotics"),
    ("Robust Control Toolbox", "robust"),
    ("ROS Toolbox", "ros"),
    ("Satellite Communications Toolbox", "satcom"),
    ("Sensor Fusion and Tracking Toolbox", "fusion"),
    ("SerDes Toolbox", "serdes"),
    ("Signal Integrity Toolbox", "signal-integrity"),
    ("SimEvents", "simevents"),
    ("Simscape", "simscape"),
    ("Simulink 3D Animation", "sl3d"),
    ("Simulink Coder", "rtw"),
    ("Simulink Control Design", "slcontrol"),
    ("Simulink Design Optimization", "sldo"),
    ("Simulink Design Verifier", "sldv"),
    ("Simulink Desktop Real-Time", "sldrt"),
    ("Simulink Extras", "simulink-extras"),
    ("Simulink Fault Analyzer", "fault-analyzer"),
    ("Simulink Real-Time", "slrealtime"),
    ("Simulink Test", "sltest"),
    ("SoC Blockset", "soc"),
    ("Stateflow", "stateflow"),
    ("Statistics and Machine Learning Toolbox", "stats"),
    ("System Identification Toolbox", "ident"),
    ("UAV Toolbox", "uav"),
    ("Vehicle Dynamics Blockset", "vdynblks"),
    ("Vehicle Network Toolbox", "vnt"),
    ("Vision HDL Toolbox", "visionhdl"),
    ("Wireless HDL Toolbox", "wireless-hdl"),
]

BROWSER_ALIASES = {
    "Communications Toolbox HDL Support": ("communications-toolbox-hdl-support", "wireless-hdl"),
    "DSP System Toolbox HDL Support": ("dsp-system-toolbox-hdl-support", "dsphdl"),
    "Fixed-Point Designer HDL Support": ("fixed-point-designer-hdl-support", "hdlcoder"),
    "Motor Control Blockset HDL Support": ("motor-control-blockset-hdl-support", "mcb"),
}

# These entries are visible in the local Browser but have no independent
# referencelist_block_cat.xml in the public R2025b catalog. Do not invent a
# block list: a local MATLAB enumeration is required to populate their children.
BROWSER_LOCAL_ONLY = {"Report Generator", "Simulink Extras"}


COMMON_BLOCKS = [
    "Bus Creator",
    "Bus Selector",
    "Constant",
    "Data Type Conversion",
    "Delay",
    "Demux",
    "Discrete-Time Integrator",
    "Gain",
    "Ground",
    "Inport",
    "Integrator",
    "Logical Operator",
    "Mux",
    "Outport",
    "Product, Matrix Multiply",
    "Relational Operator",
    "Saturation",
    "Scope",
    "Subsystem",
    "Sum",
    "Switch",
    "Terminator",
    "Vector Concatenate",
]


def write_browser_tree(manifest: dict, root: Path) -> None:
    """Materialize the Simulink Library Browser hierarchy with full block pages."""
    by_id = {p["id"]: p for p in manifest["products"]}
    browser_ids = {directory for _, directory in BROWSER_PRODUCTS}
    products = [
        by_id[directory]
        for _, directory in BROWSER_PRODUCTS
        if directory in by_id and by_id[directory]["status"] == "enumerated"
    ]
    for product in products:
        if product["id"] == "simulink":
            product["libraries"] = [
                library
                for library in product["libraries"]
                if tuple(library["path"][:2])
                == ("Simulink Environment Fundamentals", "Block Libraries")
            ]
        product["block_occurrences"] = sum(
            len(library["blocks"]) for library in product["libraries"]
        )
        product["unique_document_paths"] = len(
            {
                block["documentation_path"]
                for library in product["libraries"]
                for block in library["blocks"]
            }
        )
    manifest["products"] = products
    manifest["scope"] = "the 66-entry local R2025b Library Browser installation profile"
    refresh_totals(manifest)
    if len(BROWSER_PRODUCTS) != 66 or len(browser_ids) != 66:
        raise ValueError("The installed Browser profile must contain 66 unique top-level entries")
    # Scraper staging files and previous Browser trees are both valid inputs.
    # Load them before replacing either canonical language directory.
    source_documents = {
        (id(block), language): (root / document["path"]).read_text(encoding="utf-8")
        for product in products
        for library in product["libraries"]
        for block in library["blocks"]
        for language, document in block["documents"].items()
        if document["status"] == "available" and document["path"]
    }
    for language in ("en", "zh"):
        browser_root = root / language
        shutil.rmtree(browser_root, ignore_errors=True)
        browser_root.mkdir(parents=True, exist_ok=True)
        root_index = [
            "# Simulink Library Browser" if language == "en" else "# Simulink 库浏览器",
            "",
        ]
        root_entries = []
        for product in products:
            libraries = product["libraries"]
            if product["id"] == "simulink":
                prefix = ("Simulink Environment Fundamentals", "Block Libraries")
                libraries = [
                    library for library in libraries if tuple(library["path"][:2]) == prefix
                ]
            nodes = {}
            for library in libraries:
                relative_parts = (
                    library["path"][2:] if product["id"] == "simulink" else library["path"]
                )
                if not relative_parts:
                    continue
                parts = [product["id"], *(slug(part) for part in relative_parts)]
                for depth in range(1, len(parts) + 1):
                    key = tuple(parts[:depth])
                    display = product["name"] if depth == 1 else relative_parts[depth - 2]
                    nodes.setdefault(key, {"name": display, "blocks": []})
                nodes[tuple(parts)]["blocks"].extend(library["blocks"])
                name_counts = {}
                for block in library["blocks"]:
                    key = slug(block["name"])
                    name_counts[key] = name_counts.get(key, 0) + 1
                for block in library["blocks"]:
                    filename = slug(block["name"])
                    if name_counts[filename] > 1:
                        filename += "-" + slug(Path(block["documentation_path"]).stem)
                    filename += ".md"
                    block["resource_name"] = filename
                    target = browser_root.joinpath(*parts, filename)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    document = block["documents"][language]
                    if document["status"] == "available" and document["path"]:
                        content = source_documents[(id(block), language)]
                    else:
                        content = f"# {block['name']}\n\n{block['summary']}\n\n" + (
                            "完整中英文正文待补。\n"
                            if language == "zh"
                            else "Full English and Chinese documentation is pending.\n"
                        )
                    target.write_text(content, encoding="utf-8")
                    relative = target.relative_to(root).as_posix()
                    block.setdefault("resource_paths", {})[language] = relative
                    document["path"] = relative
            if product["id"] == "simulink":
                common_key = ("simulink", "commonly-used-blocks")
                nodes.setdefault(("simulink",), {"name": "Simulink", "blocks": []})
                nodes[common_key] = {"name": "Commonly Used Blocks", "blocks": []}
                by_name = {}
                for library in product["libraries"]:
                    for block in library["blocks"]:
                        by_name.setdefault(block["name"], block)
                for name in COMMON_BLOCKS:
                    block = by_name[name]
                    nodes[common_key]["blocks"].append(block)
                    content = source_documents[(id(block), language)]
                    target = browser_root / "simulink/commonly-used-blocks" / f"{slug(name)}.md"
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(content, encoding="utf-8")
                nodes[("simulink", "quick-insert")] = {
                    "name": "Quick Insert",
                    "blocks": [],
                    "description": (
                        "Quick Insert 是依赖模型上下文的动态插入入口，没有固定块清单。"
                        if language == "zh"
                        else "Quick Insert is a model-context-dependent dynamic insertion surface and has no fixed block list."
                    ),
                }
            for key, node in nodes.items():
                directory = browser_root.joinpath(*key)
                directory.mkdir(parents=True, exist_ok=True)
                # dict insertion order is the official XML traversal order.
                children = [
                    candidate
                    for candidate in nodes
                    if len(candidate) == len(key) + 1 and candidate[:-1] == key
                ]
                lines = [f"# {node['name']}", ""]
                lines.extend(
                    f"- [{nodes[child]['name']}]({child[-1]}/index.md)" for child in children
                )
                for block in node["blocks"]:
                    filename = block.get("resource_name", slug(block["name"]) + ".md")
                    lines.append(f"- [{block['name']}]({filename})")
                if len(lines) == 2:
                    lines.append(
                        node.get(
                            "description",
                            (
                                "这是 R2025b Library Browser 的官方分类节点。当前节点没有子目录，"
                                "官方块清单也未在此列出固定块；保留该页是为了维持官方目录层级，"
                                "不表示对应产品功能为空。"
                                if language == "zh"
                                else "This is an official R2025b Library Browser category. It has no "
                                "subdirectories or fixed block entries in the official block manifest. "
                                "The page preserves the official hierarchy and does not imply that the "
                                "corresponding product functionality is unavailable."
                            ),
                        )
                    )
                    if len(key) > 1:
                        lines.extend(
                            [
                                "",
                                (
                                    "- [返回上级目录](../index.md)"
                                    if language == "zh"
                                    else "- [Back to parent directory](../index.md)"
                                ),
                            ]
                        )
                    if len(key) > 2:
                        product_index = "../" * (len(key) - 1) + "index.md"
                        product_name = nodes[(key[0],)]["name"]
                        lines.append(
                            f"- [查看 {product_name} 目录]({product_index})"
                            if language == "zh"
                            else f"- [Browse {product_name}]({product_index})"
                        )
                (directory / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        for name, (directory, target_product) in BROWSER_ALIASES.items():
            alias = browser_root / directory
            alias.mkdir(parents=True, exist_ok=True)
            (alias / "index.md").write_text(
                f"# {name}\n\n"
                + (
                    "这是本机 Library Browser 支持库入口。公开 R2025b 目录没有它的独立块库 XML，以下链接只用于查阅关联产品文档，不代表已枚举该支持库的全部块。\n\n"
                    if language == "zh"
                    else "This support-library entry is visible in the local Library Browser. The public R2025b catalog has no independent block XML for it; the associated product below is reference documentation, not a claim that every support-library block has been enumerated.\n\n"
                )
                + f"[{'打开关联产品文档' if language == 'zh' else 'Open associated product documentation'}](../{target_product}/index.md)\n",
                encoding="utf-8",
            )
        for name in BROWSER_LOCAL_ONLY:
            directory = dict(BROWSER_PRODUCTS)[name]
            local = browser_root / directory
            local.mkdir(parents=True, exist_ok=True)
            (local / "index.md").write_text(
                f"# {name}\n\n"
                + (
                    "该入口来自用户本机 R2025b Library Browser。公开产品目录没有对应的独立块库 XML，因此这里没有虚构子库或块；需要从该 MATLAB 安装实例导出本机库树后补齐。\n"
                    if language == "zh"
                    else "This entry comes from the user's local R2025b Library Browser. The public product catalog has no corresponding independent block XML, so no children are fabricated; enumerate the local MATLAB installation to populate them.\n"
                ),
                encoding="utf-8",
            )
        root_entries = BROWSER_PRODUCTS
        root_index.extend(f"- [{name}]({directory}/index.md)" for name, directory in root_entries)
        (browser_root / "index.md").write_text("\n".join(root_index) + "\n", encoding="utf-8")
    totals = manifest["totals"]
    (root / "README.md").write_text(
        "# Simulink Block Library\n\n"
        "MATLAB/Simulink R2025b 资源添加时使用的本地块参考库。"
        "`zh/` 和 `en/` 是正式 Library Browser 目录，按产品、子库和块组织；"
        "解析器按块原始名称及 `SourceBlock` 匹配文档，无需联网。\n\n"
        "- [中文块库](zh/index.md)\n"
        "- [English block library](en/index.md)\n\n"
        f"当前包含 {totals['block_occurrences']} 个库中块条目，中英文正文均已生成。"
        "`manifest.json` 是解析器和离线生成脚本使用的机器元数据，不是 OV 资源页面。"
        "重新生成使用 `scripts/matlab/` 下的 R2025b 脚本；抓取缓存和失败日志保存在库目录之外。\n",
        encoding="utf-8",
    )
    (root / "index.md").unlink(missing_ok=True)
    for redundant in ("browser", "catalog"):
        shutil.rmtree(root / redundant, ignore_errors=True)
    for report_name in (
        "library-browser-reconciliation.md",
        "scrape-failures.json",
        "scrape-failures.md",
        "translation-failures.json",
    ):
        (root / report_name).unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, default=Path("/tmp/r2025b-products"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parents[2]
        / "openviking/parse/parsers/matlab/simulink-block-library/manifest.json",
    )
    parser.add_argument(
        "--coverage-directory", type=Path, default=Path(__file__).with_name("r2025b-block-coverage")
    )
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--no-count-check", action="store_true")
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    products = discover_products(args.cache, args.offline)
    if not args.offline:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            statuses = list(pool.map(lambda p: fetch_product(p, args.cache, False), products))
        errors = [
            status for status in statuses if status.startswith("error") or status == "not_fetched"
        ]
        if errors:
            raise SystemExit(f"Refusing an incomplete manifest: {errors}")
    old = old_document_index(Path(__file__).with_name("simulink-block-manifest.json"))
    manifest = {
        "schema_version": 1,
        "release": RELEASE,
        "source_catalog": CATALOG,
        "scope": "all official MathWorks products with Simulink blocks; third-party and machine-local support packages excluded",
        "block_reference_types": ["block", "simscapeblock"],
        "status_contract": {
            "product": ["enumerated", "no_block_library", "fetch_failed", "license_required"],
            "document": ["available", "pending", "missing", "fetch_failed", "license_required"],
            "external_scope": {
                "third_party": "not in the MathWorks public product catalog; enumerate from the user's installation",
                "support_package": "not assumed complete from the public product catalog; enumerate from the user's installation",
            },
        },
        "products": [
            parse_product(
                product,
                args.cache,
                {**old, **existing_document_index(args.output, product["id"])},
                args.output.parent,
            )
            for product in products
        ],
    }
    refresh_totals(manifest)
    totals = manifest["totals"]
    if not args.no_count_check:
        differences = {
            key: (value, totals[key]) for key, value in EXPECTED.items() if totals[key] != value
        }
        if differences:
            raise SystemExit(
                f"Official R2025b snapshot changed; review before updating: {differences}"
            )
    write_browser_tree(manifest, args.output.parent)
    # Browser generation assigns the canonical document paths; persist them.
    args.output.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.coverage_directory.mkdir(parents=True, exist_ok=True)
    en, zh = report(manifest)
    (args.coverage_directory / "index.md").write_text(en, encoding="utf-8")
    (args.coverage_directory / "index.zh-CN.md").write_text(zh, encoding="utf-8")
    print(json.dumps(totals, indent=2))


if __name__ == "__main__":
    main()
