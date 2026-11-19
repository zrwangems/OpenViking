# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Bounded reads for XML members in MATLAB ZIP containers."""

from __future__ import annotations

import zipfile

MAX_XML_MEMBER_BYTES = 128 * 1024 * 1024


def read_xml_member(archive: zipfile.ZipFile, name: str, *, max_bytes: int | None = None) -> bytes:
    """Read one member without allowing a ZIP bomb to allocate unbounded memory."""
    limit = MAX_XML_MEMBER_BYTES if max_bytes is None else max_bytes
    info = archive.getinfo(name)
    if info.file_size > limit:
        raise ValueError(f"ZIP member {name} exceeds the {limit}-byte XML safety limit")
    with archive.open(info) as stream:
        data = stream.read(limit + 1)
    if len(data) > limit:
        raise ValueError(f"ZIP member {name} exceeds the {limit}-byte XML safety limit")
    return data
