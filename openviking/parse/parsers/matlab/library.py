# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read the packaged Simulink block library without a generated index."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


def library_root() -> Path:
    """Return the single source of Simulink block knowledge shipped with OV."""
    return Path(__file__).resolve().parent / "simulink-block-library"


@dataclass(frozen=True)
class BlockReference:
    """One official product/library/block occurrence and its document status."""

    product_id: str
    product_name: str
    library_path: tuple[str, ...]
    name: str
    documentation_path: str
    summary: str
    documents: dict[str, dict[str, str | None]]
    resource_paths: dict[str, str]

    @property
    def full_document(self) -> bool:
        return all(self.documents[language]["status"] == "available" for language in ("en", "zh"))

    def resource_path(self, language: str = "en") -> str | None:
        return self.resource_paths.get(language) or self.documents[language]["path"]


@lru_cache(maxsize=1)
def manifest() -> dict:
    return json.loads((library_root() / "manifest.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def block_references() -> tuple[BlockReference, ...]:
    """Read every packaged R2025b Library Browser occurrence, including gaps."""
    return tuple(
        BlockReference(
            product_id=product["id"],
            product_name=product["name"],
            library_path=tuple(library["path"]),
            name=block["name"],
            documentation_path=block["documentation_path"],
            summary=block["summary"],
            documents=block["documents"],
            resource_paths=block.get("resource_paths", {}),
        )
        for product in manifest()["products"]
        for library in product["libraries"]
        for block in library["blocks"]
    )


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


@lru_cache(maxsize=1024)
def read_block_document(family: str, name: str, language: str = "en") -> str:
    """Structure a block page while adding a resource, not in the source library."""
    localized = "zh" if str(language).lower().startswith("zh") else "en"
    path = library_root() / localized / family / f"{slug(name)}.md"
    document = path.read_text(encoding="utf-8")
    return normalize_block_document(document, language=localized)


def read_reference_document(reference: BlockReference, language: str = "en") -> str:
    """Read the exact Browser occurrence, including disambiguated duplicate names."""
    localized = "zh" if str(language).lower().startswith("zh") else "en"
    relative = reference.resource_path(localized)
    if not relative:
        raise FileNotFoundError(
            f"No packaged document for {reference.product_name}/{reference.name}"
        )
    return normalize_block_document(
        (library_root() / relative).read_text(encoding="utf-8"), language=localized
    )


def section(document: str, name: str) -> str:
    match = re.search(
        rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)", document, re.MULTILINE | re.DOTALL
    )
    return match.group(1).strip() if match else ""


def front_matter(document: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*['\"]?(.*?)['\"]?\s*$", document, re.MULTILINE)
    return match.group(1) if match else ""


_STRUCTURED_SECTIONS = {
    "en": (
        "Ports",
        "Parameters",
        "Libraries",
        "Block Characteristics",
        "Extended Capabilities",
        "Version History",
        "Description",
    ),
    "zh": ("端口", "参数", "所属库", "模块特性", "扩展功能", "版本历史", "描述"),
}
_SECTION_ALIASES = {
    "Ports": "Ports",
    "Parameters": "Parameters",
    "Libraries": "Libraries",
    "Block Characteristics": "Block Characteristics",
    "Extended Capabilities": "Extended Capabilities",
    "Version History": "Version History",
    "Description": "Description",
    "端口": "Ports",
    "参数": "Parameters",
    "所属库": "Libraries",
    "库": "Libraries",
    "模块特性": "Block Characteristics",
    "扩展功能": "Extended Capabilities",
    "版本历史": "Version History",
    "版本历史记录": "Version History",
    "描述": "Description",
    "说明": "Description",
}


def normalize_block_document(document: str, language: str = "en") -> str:
    """Use one section order and move the block description to the end."""
    localized = "zh" if str(language).lower().startswith("zh") else "en"
    title_match = re.search(r"^# (.+)$", document, re.MULTILINE)
    if not title_match:
        raise ValueError("Simulink block document has no block-name heading")
    title = title_match.group(1).strip()
    header = document[: title_match.start()].rstrip()
    summary = document[title_match.end() :].split("## ", 1)[0].strip()
    sections: dict[str, str] = {}
    for match in re.finditer(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", document, re.MULTILINE | re.DOTALL):
        canonical = _SECTION_ALIASES.get(match.group(1).strip())
        if canonical:
            content = match.group(2).strip()
            if content:
                sections[canonical] = "\n\n".join(
                    filter(None, (sections.get(canonical, ""), content))
                )
    description = "\n\n".join(filter(None, (summary, sections.get("Description", ""))))
    sections["Description"] = description
    missing = "R2025b 官方文档未提供。" if localized == "zh" else "Not documented in R2025b."
    lines = [header, "", f"# {title}", ""]
    english_names = _STRUCTURED_SECTIONS["en"]
    for english_name, display_name in zip(
        english_names, _STRUCTURED_SECTIONS[localized], strict=True
    ):
        lines.extend([f"## {display_name}", "", sections.get(english_name) or missing, ""])
    return "\n".join(lines).rstrip() + "\n"


@lru_cache(maxsize=1)
def catalog_entries() -> tuple[tuple[str, str, str, str], ...]:
    """Build ``(family, category, block name, summary)`` from Markdown files."""
    entries = []
    root = library_root() / "en"
    if not root.is_dir():
        raise FileNotFoundError(f"Packaged Simulink block library is missing: {root}")
    for family_directory in sorted(root.iterdir()):
        if not family_directory.is_dir():
            continue
        for document_path in sorted(family_directory.glob("*.md")):
            if document_path.name == "index.md":
                continue
            document = document_path.read_text(encoding="utf-8")
            title = front_matter(document, "title")
            category = front_matter(document, "official_category")
            if not title or not category:
                raise ValueError(f"Incomplete Simulink block metadata: {document_path}")
            summary = section(document, "Description").split("\n\n", 1)[0].strip()
            entries.append((family_directory.name, category, title, summary))
    if not entries:
        raise ValueError(f"Packaged Simulink block library is empty: {root}")
    return tuple(entries)
