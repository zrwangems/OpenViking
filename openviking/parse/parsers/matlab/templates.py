# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Offline block-template lookup used during SLX resource ingestion."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from openviking.parse.parsers.matlab.catalog import find_block


@lru_cache(maxsize=1)
def _templates() -> dict:
    path = Path(__file__).with_name("block_templates.json")
    return json.loads(path.read_text(encoding="utf-8"))["templates"]


def render_block_template(block_type: str, source_block: str = "") -> tuple[str, str] | None:
    """Return ``(canonical name, Markdown)`` for an original SLX block identity.

    No network or MATLAB installation is involved. Unknown external library
    blocks return None and retain their SourceBlock/parameters in the model.
    """
    match = find_block(block_type, source_block)
    if not match:
        return None
    family, name = match
    template = _templates().get(f"{family}/{name}")
    if template is None:
        return None
    lines = [
        f"官方目录：`{template['category']}`；文档页标识：`{template['documentation_page']}`；基线：`R2025b`。",
        "",
        template["summary"],
        "",
    ]
    for key, title in (
        ("libraries", "所属库"),
        ("description", "用途"),
        ("ports", "端口"),
        ("parameters", "参数说明"),
    ):
        content = template[key]
        if content:
            lines.extend([f"#### {title}", "", content, ""])
    return name, "\n".join(lines).strip()
