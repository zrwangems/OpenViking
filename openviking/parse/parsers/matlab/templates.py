# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Inline Markdown from the packaged block library during SLX ingestion."""

from __future__ import annotations

from openviking.parse.parsers.matlab.catalog import find_block
from openviking.parse.parsers.matlab.library import front_matter, read_block_document, section


def render_block_template(block_type: str, source_block: str = "") -> tuple[str, str] | None:
    """Return ``(canonical name, Markdown)`` read directly from the block library.

    No JSON export, network access, or MATLAB installation is involved. Unknown
    external library blocks return None and retain SourceBlock/parameters in SLX.
    """
    match = find_block(block_type, source_block)
    if not match:
        return None
    family, name = match
    document = read_block_document(family, name)
    category = front_matter(document, "official_category")
    page = front_matter(document, "documentation_page")
    release = front_matter(document, "documentation_release")
    summary = document.split(f"# {name}\n", 1)[1].split("## ", 1)[0].strip()
    lines = [
        f"官方目录：`{category}`；文档页标识：`{page}`；基线：`{release}`。",
        "",
        summary,
        "",
    ]
    for title in ("Libraries", "Description", "Ports", "Parameters"):
        content = section(document, title)
        if content:
            translated = {
                "Libraries": "所属库",
                "Description": "用途",
                "Ports": "端口",
                "Parameters": "参数说明",
            }[title]
            lines.extend([f"#### {translated}", "", content, ""])
    return name, "\n".join(lines).strip()
