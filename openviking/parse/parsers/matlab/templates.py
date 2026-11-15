# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Inline localized Markdown from the packaged block library during SLX ingestion."""

from __future__ import annotations

from openviking.parse.parsers.matlab.catalog import find_block
from openviking.parse.parsers.matlab.library import (
    front_matter,
    read_block_document,
    section,
    subsection,
)


def render_block_template(
    block_type: str, source_block: str = "", language: str = "en"
) -> tuple[str, str] | None:
    """Return ``(canonical name, Markdown)`` in the user's resource language.

    No JSON export, network access, or MATLAB installation is involved. Unknown
    external library blocks return None and retain SourceBlock/parameters in SLX.
    Model identifiers and parameter values never pass through localization.
    """
    match = find_block(block_type, source_block)
    if not match:
        return None
    family, name = match
    document = read_block_document(family, name)
    category = front_matter(document, "official_category")
    page = front_matter(document, "documentation_page")
    release = front_matter(document, "documentation_release")
    chinese = str(language).lower().startswith("zh")
    if chinese:
        localized = section(document, "中文")
        summary = localized.split("### ", 1)[0].strip()
        lines = [
            f"官方目录：`{category}`；文档页标识：`{page}`；基线：`{release}`。",
            "",
            summary,
            "",
        ]
        for title in ("所属库", "库", "描述", "说明", "端口", "参数"):
            content = subsection(localized, title)
            if content:
                display_title = {"库": "所属库", "参数": "参数说明"}.get(title, title)
                lines.extend([f"#### {display_title}", "", content, ""])
        return name, "\n".join(lines).strip()

    summary = document.split(f"# {name}\n", 1)[1].split("## ", 1)[0].strip()
    lines = [
        f"Official category: `{category}`; documentation page: `{page}`; release: `{release}`.",
        "",
        summary,
        "",
    ]
    for title in ("Libraries", "Description", "Ports", "Parameters"):
        content = section(document, title)
        if content:
            lines.extend([f"#### {title}", "", content, ""])
    return name, "\n".join(lines).strip()
