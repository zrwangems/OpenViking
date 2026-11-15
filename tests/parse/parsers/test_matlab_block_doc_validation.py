# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).parents[3] / "scripts" / "matlab"
sys.path.insert(0, str(SCRIPTS))

from translate_r2025b_all_blocks import (  # noqa: E402
    split_source,
    table_shapes,
    validate_translation,
)


def test_table_shapes_ignore_enum_pipes_and_compare_every_table():
    source = (
        "# Block\n\n"
        "An enum continued on the next line\n"
        "| No thermal port** or **other value\n\n"
        "| A | B |\n| --- | --- |\n| one | two |\n"
    )
    translated = (
        "# Block\n\n换行枚举值\n不带热端口或其他值\n\n| 甲 | 乙 |\n| --- | --- |\n| 一 | 二 |\n"
    )
    assert table_shapes(source) == [3]
    assert table_shapes(translated) == [3]
    validate_translation(source, translated)
    with pytest.raises(ValueError, match="table shapes changed"):
        validate_translation(source, translated.rsplit("\n", 2)[0])


def test_large_table_is_not_split_between_rows():
    table = "| A | B |\n| --- | --- |\n" + "\n".join(
        f"| signal_{index} | value_{index} |" for index in range(100)
    )
    source = f"# Block\n\n## Parameters\n\n{table}\n"
    chunks = split_source(source, limit=500)
    assert any(table in chunk for chunk in chunks)
    assert sum(chunk.count("signal_") for chunk in chunks) == 100
