# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Inline localized Markdown from the packaged block library during SLX ingestion."""

from __future__ import annotations

from pathlib import Path

from openviking.parse.parsers.matlab.catalog import find_block_reference
from openviking.parse.parsers.matlab.library import (
    front_matter,
    read_block_document,
    read_reference_document,
    section,
)


def render_block_template(
    block_type: str, source_block: str = "", language: str = "en"
) -> tuple[str, str] | None:
    """Return ``(canonical name, Markdown)`` in the user's resource language.

    No JSON export, network access, or MATLAB installation is involved. Unknown
    external library blocks return None and retain SourceBlock/parameters in SLX.
    Model identifiers and parameter values never pass through localization.
    """
    reference = find_block_reference(block_type, source_block)
    if not reference:
        return None
    chinese = str(language).lower().startswith("zh")
    name = reference.name
    if not reference.full_document and reference.documentation_path:
        location = " / ".join(reference.library_path)
        if chinese:
            return name, (
                f"官方产品：`{reference.product_name}`；原始目录：`{location}`；"
                f"文档页标识：`{Path(reference.documentation_path).stem}`；基线：`R2025b`。\n\n"
                f"官方英文摘要：{reference.summary}\n\n"
                "完整中英文正文尚未抓取，此模板只包含官方清单元数据，不补写端口或参数。"
            )
        return name, (
            f"Official product: `{reference.product_name}`; original category: `{location}`; "
            f"documentation page: `{Path(reference.documentation_path).stem}`; release: `R2025b`.\n\n"
            f"{reference.summary}\n\n"
            "Full English and Chinese documentation is pending. This template contains "
            "official catalog metadata only and does not invent ports or parameters."
        )
    if not reference.resource_path("en"):
        return None
    if reference.product_id == "simulink" and "Commonly Used Blocks" in source_block.split("/"):
        document = read_block_document("simulink/commonly-used-blocks", name, language=language)
    else:
        document = read_reference_document(reference, language=language)
    category = front_matter(document, "official_category")
    page = front_matter(document, "documentation_page")
    release = front_matter(document, "documentation_release")
    if chinese:
        summary = section(document, "描述").split("\n\n", 1)[0].strip()
        lines = [
            f"官方目录：`{category}`；文档页标识：`{page}`；基线：`{release}`。",
            "",
            summary,
            "",
        ]
        for title in ("所属库", "库", "描述", "说明", "端口", "参数"):
            content = section(document, title)
            if content:
                display_title = {"库": "所属库", "参数": "参数说明"}.get(title, title)
                lines.extend([f"#### {display_title}", "", content, ""])
        return name, "\n".join(lines).strip()

    summary = section(document, "Description").split("\n\n", 1)[0].strip()
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
