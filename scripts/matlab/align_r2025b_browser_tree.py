#!/usr/bin/env python3
"""Align the packaged block library with the local R2025b Library Browser tree.

The public product XML catalogs supply documentation, not the Browser layout.
The checked-in tree_full.md is the sole authority for products, directories,
block display names and ordering. Public documentation is reused only when a
name match is exact or an unambiguous alias is known. Verified overrides cover
preconfigured variants and older support-package pages. Browser entries without
an official block reference are explicitly excluded and recorded for review.
"""

from __future__ import annotations

import argparse
import collections
import copy
import difflib
import json
import re
import unicodedata
from pathlib import Path

from browser_tree_writer import write_browser_tree
from extract_r2025b_block_manifest import (
    BROWSER_PRODUCTS,
    RELEASE,
    canonicalize_cross_product_documents,
    discover_products,
    existing_document_index,
    parse_product,
    refresh_totals,
)

TREE_PATH = Path(__file__).with_name("tree_full.md")
OVERRIDES_PATH = Path(__file__).with_name("r2025b-block-doc-overrides.json")


def entry_key(product: str, path: list[str], name: str) -> tuple[str, tuple[str, ...], str]:
    return product, tuple(path), name


DOCUMENT_OVERRIDES = {
    entry_key(item["product"], item["path"], item["name"]): item
    for item in json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
}
# The Browser tree is exhaustive: no leaf is excluded. Every former exclusion
# now has an explicit official block or topic mapping in DOCUMENT_OVERRIDES.
EXCLUDED_ENTRIES = {}

# The local Browser splits several Simscape products into their own top-level
# libraries. These IDs keep their established SourceBlock/document ownership.
PRODUCT_IDS = {
    **dict(BROWSER_PRODUCTS),
    "Battery": "simscape-battery",
    "Driveline": "sdl",
    "Electrical": "sps",
    "Fluids": "hydro",
    "Foundation Library": "simscape",
    "Multibody": "sm",
    "Reinforcement Learning": "reinforcement-learning",
    "Simscape": "simscape-root",
}
SOURCE_PRODUCT_IDS = {
    "Battery": "simscape-battery",
    "Simscape": "simscape",
    "Communications Toolbox HDL Support": "wireless-hdl",
    "DSP System Toolbox HDL Support": "dsphdl",
    "Driveline": "sdl",
    "Electrical": "sps",
    "Fixed-Point Designer HDL Support": "fixedpoint",
    "Fluids": "hydro",
    "Foundation Library": "simscape",
    "Motor Control Blockset HDL Support": "mcb",
    "Multibody": "sm",
    "Reinforcement Learning": "reinforcement-learning",
}

# Display names in the actual Browser can differ from the reference-page
# title. Only established aliases of the same block are listed here.
BLOCK_ALIASES = {
    "In1": "Inport",
    "Out1": "Outport",
    "Product": "Product, Matrix Multiply",
    "Integrator, Second-Order": "Second-Order Integrator",
    "Integrator, Second-Order Limited": "Second-Order Integrator Limited",
    "Add": "Sum",
    "Subtract": "Sum",
    "Sum of Elements": "Sum",
    "Reciprocal Sqrt": "Sqrt",
    "Signed Sqrt": "Sqrt",
    "Cosine": "Sine",
    "Atomic Subsystem": "Subsystem",
    "CodeReuseSubsystem": "Subsystem",
    "Variant Model": "Variant Subsystem",
    "Variant Assembly Subsystem": "Variant Subsystem",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).replace("&", " and ")
    return "".join(character for character in value.lower() if character.isalnum())


def parse_tree(path: Path = TREE_PATH) -> list[dict]:
    """Parse and validate the numbered local Browser inventory."""
    products = []
    product = None
    stack: list[str] = []
    summary = {}
    in_summary = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line == "## 汇总":
            in_summary = True
        match = re.match(r"^\| \d+ \| (.+?) \| \d+ \| (\d+) \|$", line)
        if in_summary and match:
            summary[match.group(1)] = int(match.group(2))
        match = re.match(r"^## \d+\. (.+)$", line)
        if match:
            product = {"name": match.group(1), "directories": [], "blocks": []}
            products.append(product)
            stack = []
            continue
        match = re.match(r"^( *)- \*\*(.+)\*\*（(\d+) 块）$", line)
        if match and product:
            depth = len(match.group(1)) // 2
            stack = [*stack[:depth], match.group(2)]
            product["directories"].append(
                {"path": list(stack), "block_occurrences": int(match.group(3))}
            )
            continue
        match = re.match(r"^( *)- (.+)$", line)
        if match and product:
            depth = len(match.group(1)) // 2
            product["blocks"].append({"path": list(stack[:depth]), "name": match.group(2)})

    if not products or len(products) != len(summary):
        raise ValueError("tree_full.md summary and product sections do not match")
    for product in products:
        name = product["name"]
        if len(product["blocks"]) != summary.get(name):
            raise ValueError(
                f"{name}: tree has {len(product['blocks'])} blocks, summary has {summary.get(name)}"
            )
        blocks_by_directory = collections.Counter(
            tuple(block["path"]) for block in product["blocks"]
        )
        for directory in product["directories"]:
            prefix = tuple(directory["path"])
            actual = sum(
                count
                for path, count in blocks_by_directory.items()
                if path[: len(prefix)] == prefix
            )
            if actual != directory["block_occurrences"]:
                raise ValueError(
                    f"{name}/{'/'.join(prefix)}: {actual} blocks, expected {directory['block_occurrences']}"
                )
    return products


def _source_entries(products: list[dict]) -> list[tuple[dict, dict, dict]]:
    return [
        (product, library, block)
        for product in products
        for library in product["libraries"]
        for block in library["blocks"]
    ]


def _best_candidate(
    candidates: list[tuple[dict, dict, dict]], product_name: str, path: list[str]
) -> tuple[dict, dict, dict]:
    """Use product ownership and directory proximity to disambiguate exact names."""
    preferred = SOURCE_PRODUCT_IDS.get(
        product_name, PRODUCT_IDS.get(product_name, slug(product_name))
    )

    def score(item: tuple[dict, dict, dict]) -> tuple[float, ...]:
        product, library, _block = item
        source_path = library["path"]
        exact_path = source_path[-len(path) :] == path if path else False
        common = 0
        for left, right in zip(reversed(source_path), reversed(path), strict=False):
            if normalized(left) != normalized(right):
                break
            common += 1
        similarity = difflib.SequenceMatcher(None, "/".join(path), "/".join(source_path)).ratio()
        return (product["id"] == preferred, exact_path, common, similarity)

    return max(candidates, key=score)


def align_manifest(full_manifest: dict, tree_path: Path = TREE_PATH) -> dict:
    """Project public documentation onto the exact local Browser inventory."""
    tree = parse_tree(tree_path)
    sources = _source_entries(full_manifest["products"])
    by_name: dict[str, list] = collections.defaultdict(list)
    by_normalized: dict[str, list] = collections.defaultdict(list)
    by_stem: dict[str, list] = collections.defaultdict(list)
    for item in sources:
        block = item[2]
        by_name[block["name"]].append(item)
        by_normalized[normalized(block["name"])].append(item)
        by_stem[normalized(Path(block["documentation_path"]).stem)].append(item)

    products = []
    conflicts = []
    for tree_product in tree:
        name = tree_product["name"]
        product_id = PRODUCT_IDS.get(name, slug(name))
        product = {
            "id": product_id,
            "name": name,
            "documentation_index": None,
            "block_catalog": None,
            "status": "enumerated",
            "source_sha256": None,
            "libraries": [],
            "block_occurrences": len(tree_product["blocks"]),
            "unique_document_paths": 0,
        }
        libraries = {
            tuple(directory["path"]): {
                "path": directory["path"],
                "targets": [],
                "blocks": [],
            }
            for directory in tree_product["directories"]
        }
        if any(not block["path"] for block in tree_product["blocks"]):
            libraries[()] = {"path": [], "targets": [], "blocks": []}
        for tree_block in tree_product["blocks"]:
            block_name = tree_block["name"]
            key = entry_key(name, tree_block["path"], block_name)
            override = DOCUMENT_OVERRIDES.get(key)
            candidates = [] if override else by_name.get(block_name, [])
            match_kind = "exact"
            if not candidates and block_name in BLOCK_ALIASES:
                candidates = by_name.get(BLOCK_ALIASES[block_name], [])
                match_kind = "known_alias"
            if not candidates:
                candidates = by_normalized.get(normalized(block_name), [])
                match_kind = "normalized_name"
            if not candidates:
                candidates = by_stem.get(normalized(block_name), [])
                match_kind = "documentation_stem"

            # Non-exact matching is accepted only when it identifies one source
            # document. Similar names in different products are not aliases.
            identities = {(item[0]["id"], item[2]["documentation_path"]) for item in candidates}
            if match_kind not in {"exact", "known_alias"} and len(identities) != 1:
                if candidates:
                    conflicts.append(
                        {"product": name, **tree_block, "candidates": sorted(identities)}
                    )
                candidates = []
            if override:
                source_product_id = override["source_product"]
                source_path = override["source_path"]
                documentation_path = source_path
                if source_product_id != product_id:
                    documentation_path = f"../{source_product_id}/{source_path}"
                block = {
                    "name": block_name,
                    "type": "block",
                    "documentation_path": documentation_path,
                    "summary": "",
                    "introduced": None,
                    "updated": [],
                    "documented_as": override["title"],
                    "source_release": override["release"],
                    "content_kind": override.get("content_kind", "block"),
                    "match_kind": "verified_override",
                    "documents": {
                        language: {"status": "pending", "path": None} for language in ("en", "zh")
                    },
                }
            elif candidates:
                source_product, _source_library, source_block = _best_candidate(
                    candidates, name, tree_block["path"]
                )
                block = copy.deepcopy(source_block)
                if block["name"] != block_name:
                    block["documented_as"] = block["name"]
                block["name"] = block_name
                block["match_kind"] = match_kind
                if source_product["id"] != product_id:
                    block["documentation_path"] = (
                        f"../{source_product['id']}/{source_block['documentation_path']}"
                    )
            else:
                block = {
                    "name": block_name,
                    "type": "block",
                    "documentation_path": None,
                    "summary": "",
                    "introduced": None,
                    "updated": [],
                    "match_kind": "tree_only",
                    "documents": {
                        language: {"status": "tree_only", "path": None} for language in ("en", "zh")
                    },
                }
            libraries[tuple(tree_block["path"])]["blocks"].append(block)
        # Dict insertion follows tree order; root blocks, when present, come first.
        product["libraries"] = list(libraries.values())
        product["block_occurrences"] = sum(
            len(library["blocks"]) for library in product["libraries"]
        )
        product["unique_document_paths"] = len(
            {
                (block["documentation_path"], block.get("source_release", RELEASE))
                for library in product["libraries"]
                for block in library["blocks"]
                if block["documentation_path"]
            }
        )
        products.append(product)

    manifest = {
        key: copy.deepcopy(value)
        for key, value in full_manifest.items()
        if key not in {"products", "totals"}
    }
    manifest.update(
        {
            "schema_version": 1,
            "release": RELEASE,
            "source_catalog": f"https://www.mathworks.com/help/releases/{RELEASE}/",
            "block_reference_types": ["block", "simscapeblock"],
            "products": products,
            "scope": "the 75-library local MATLAB R2025b Library Browser tree_full.md",
            "tree_source": "scripts/matlab/tree_full.md",
        }
    )
    manifest["status_contract"] = {
        "product": ["enumerated", "no_block_library", "fetch_failed", "license_required"],
        "document": [
            "available",
            "pending",
            "missing",
            "fetch_failed",
            "license_required",
            "tree_only",
        ],
        "external_scope": {
            "third_party": "not in the MathWorks public product catalog; enumerate from the user's installation",
            "support_package": "not assumed complete from the public product catalog; enumerate from the user's installation",
        },
    }
    canonicalize_cross_product_documents(manifest)
    refresh_totals(manifest)
    manifest["reconciliation"] = {
        "tree_products": len(tree),
        "tree_directories": sum(len(product["directories"]) for product in tree),
        "tree_blocks": sum(len(product["blocks"]) for product in tree),
        "matched_blocks": sum(
            block["match_kind"] != "tree_only"
            for product in products
            for library in product["libraries"]
            for block in library["blocks"]
        ),
        "tree_only_blocks": sum(
            block["match_kind"] == "tree_only"
            for product in products
            for library in product["libraries"]
            for block in library["blocks"]
        ),
        "verified_override_blocks": sum(
            block["match_kind"] == "verified_override"
            for product in products
            for library in product["libraries"]
            for block in library["blocks"]
        ),
        "excluded_non_block_entries": [],
        "ambiguous_non_exact_matches_retained_as_tree_only": conflicts,
    }
    return manifest


def load_full_manifest(cache: Path, root: Path) -> dict:
    """Rebuild all public product catalogs offline as documentation sources."""
    products = [
        parse_product(
            product,
            cache,
            existing_document_index(root / "manifest.json", product["id"]),
            root,
        )
        for product in discover_products(cache, offline=True)
    ]
    return {"products": products, "status_contract": {"document": []}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, default=Path("/tmp/r2025b-products"))
    parser.add_argument("--tree", type=Path, default=TREE_PATH)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).parents[2]
        / "openviking/parse/parsers/matlab/simulink-block-library/manifest.json",
    )
    parser.add_argument("--materialize", action="store_true")
    args = parser.parse_args()
    full = load_full_manifest(args.cache, args.manifest.parent)
    manifest = align_manifest(full, args.tree)
    if args.materialize:
        write_browser_tree(manifest, args.manifest.parent)
    args.manifest.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest["reconciliation"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
