# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read the packaged Simulink block library without a generated index."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path


def library_root() -> Path:
    """Return the single source of Simulink block knowledge shipped with OV."""
    return Path(__file__).resolve().parents[3] / "simulink-block-library"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


@lru_cache(maxsize=512)
def read_block_document(family: str, name: str) -> str:
    return (library_root() / family / f"{slug(name)}.md").read_text(encoding="utf-8")


def section(document: str, name: str) -> str:
    match = re.search(
        rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)", document, re.MULTILINE | re.DOTALL
    )
    return match.group(1).strip() if match else ""


def front_matter(document: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*['\"]?(.*?)['\"]?\s*$", document, re.MULTILINE)
    return match.group(1) if match else ""


@lru_cache(maxsize=1)
def catalog_entries() -> tuple[tuple[str, str, str, str], ...]:
    """Build ``(family, category, block name, summary)`` from Markdown files."""
    entries = []
    root = library_root()
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
            summary = document.split(f"# {title}\n", 1)[1].split("## ", 1)[0].strip()
            entries.append((family_directory.name, category, title, summary))
    if not entries:
        raise ValueError(f"Packaged Simulink block library is empty: {root}")
    return tuple(entries)
