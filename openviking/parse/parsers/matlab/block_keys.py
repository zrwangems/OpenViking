# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Stable keys for Simulink block descriptions.

One key names one library block independently of the Library Browser position
and of the instance values the block was dragged with.  It is computed from the
block itself, so the same function runs while a project model is imported and
while the description library is built.

Rules, in order:

* ``SubSystem``: no key.  Subsystems are expanded by the parser and their
  children are described individually; a subsystem never gets a description.
* ``Reference`` with a non-empty ``SourceType``: the key is ``SourceType``.
  This is the common case for toolbox library blocks.
* ``Reference`` without ``SourceType``: the key is the last segment of
  ``SourceBlock`` (palette nodes such as ``soclib/Examples``).
* every other ``BlockType``: the key is the block type itself
  (``Gain``, ``Trigonometry``, ``Lookup_n-D`` ...).

Whitespace inside a key is collapsed to single spaces: MATLAB writes the label
of a long block name with a line break (``RoadRunner Scenario\nReader``), which
must not become part of the identity.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - imported only for type checkers
    from openviking.parse.parsers.matlab.slx import Block

REFERENCE = "Reference"
SUBSYSTEM = "SubSystem"

_WHITESPACE = re.compile(r"\s+")


def _collapse(value: str) -> str:
    return _WHITESPACE.sub(" ", value or "").strip()


def source_block_tail(source_block: str) -> str:
    """Return the block name at the end of a ``SourceBlock`` library path."""
    path = _collapse(source_block).rstrip("/")
    return path.rsplit("/", 1)[-1].strip() if path else ""


def block_key(block: "Block") -> str | None:
    """Return the description key of one block, or ``None`` for a subsystem."""
    if block.block_type == SUBSYSTEM:
        return None
    if block.block_type == REFERENCE:
        source_type = _collapse(block.parameters.get("SourceType", ""))
        if source_type:
            return source_type
        tail = source_block_tail(block.parameters.get("SourceBlock", "") or block.source_block)
        return tail or None
    return _collapse(block.block_type) or None


def key_rule(block: "Block") -> str | None:
    """Return the rule that produced :func:`block_key`, for metadata only."""
    if block.block_type == SUBSYSTEM:
        return None
    if block.block_type == REFERENCE:
        if _collapse(block.parameters.get("SourceType", "")):
            return "source_type"
        return "source_block" if block_key(block) else None
    return "block_type"
