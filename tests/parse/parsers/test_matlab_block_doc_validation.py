# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).parents[3] / "scripts" / "matlab"
sys.path.insert(0, str(SCRIPTS))

from extract_r2025b_block_manifest import (  # noqa: E402
    BROWSER_ALIASES,
    BROWSER_LOCAL_ONLY,
    canonicalize_cross_product_documents,
    resource_component,
    write_browser_tree,
)
from scrape_simulink_blocks import localized_content  # noqa: E402
from translate_r2025b_all_blocks import (  # noqa: E402
    split_source,
    table_shapes,
    validate_translation,
)
from validate_r2025b_block_library import content_lines, markdown_body, xml_occurrences  # noqa: E402


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


def test_nested_description_uses_informative_section_not_empty_wrapper():
    html = b"""<main><h1>Callback Button</h1><p itemprop='purpose'>Execute code</p>
    <div class='block_ref'><h2>Description</h2>
      <div class='refsect1'><h2>Description</h2><p>The complete description.</p></div>
    </div></main>"""
    subtitle, sections = localized_content(html, {"name": "Callback Button"}, "en")
    assert subtitle == "Execute code"
    assert sections == [("Description", "The complete description.")]


def test_cross_product_reference_uses_owner_document():
    manifest = {
        "products": [
            {
                "id": "simulink",
                "libraries": [
                    {
                        "blocks": [
                            {
                                "documentation_path": "slref/gain.html",
                                "documents": {"en": {"path": "en/math/gain.md"}},
                            }
                        ]
                    }
                ],
            },
            {
                "id": "dsp",
                "libraries": [
                    {
                        "blocks": [
                            {
                                "documentation_path": "../simulink/slref/gain.html",
                                "documents": {
                                    "en": {"path": "en/products/dsp/../simulink/slref/gain.md"}
                                },
                            }
                        ]
                    }
                ],
            },
        ]
    }
    canonicalize_cross_product_documents(manifest)
    referenced = manifest["products"][1]["libraries"][0]["blocks"][0]
    assert referenced["documents"]["en"]["path"] == "en/math/gain.md"


def test_browser_resource_names_keep_official_spelling():
    assert resource_component("Aerospace Blockset") == "Aerospace Blockset"
    assert resource_component("And/Or") == "And／Or"


def test_library_browser_screenshot_only_entries_are_explicit():
    assert "Motor Control Blockset HDL Support" in BROWSER_ALIASES
    assert {"Report Generator", "Simulink Extras"} <= BROWSER_LOCAL_ONLY


def test_browser_generation_omits_categories_without_blocks(tmp_path):
    document = {
        language: {"status": "available", "path": f"{language}/source.md"}
        for language in ("en", "zh")
    }
    block = {
        "name": "Real Block",
        "documentation_path": "dds/realblock.html",
        "summary": "A real block",
        "documents": document,
    }
    manifest = {
        "scope": "test",
        "products": [
            {
                "id": "dds",
                "name": "DDS Blockset",
                "status": "enumerated",
                "block_occurrences": 1,
                "unique_document_paths": 1,
                "libraries": [
                    {"path": ["Get Started with DDS Blockset"], "blocks": []},
                    {"path": ["Create DDS Definitions"], "blocks": []},
                    {"path": ["Model DDS Applications in Simulink"], "blocks": [block]},
                    {"path": ["Deploy Applications to DDS Network"], "blocks": []},
                ],
            }
        ],
    }
    for language in ("en", "zh"):
        (tmp_path / language).mkdir()
        (tmp_path / language / "source.md").write_text(
            f"---\ndocumentation_release: R2025b\nlanguage: {language}\n---\n# Real Block\n",
            encoding="utf-8",
        )

    write_browser_tree(manifest, tmp_path)

    for language in ("en", "zh"):
        browser = tmp_path / language
        assert (browser / "DDS Blockset/Model DDS Applications in Simulink/Real Block.md").is_file()
        assert not (browser / "DDS Blockset/Create DDS Definitions").exists()
        assert not (browser / "DDS Blockset/Get Started with DDS Blockset").exists()
        assert not (browser / "DDS Blockset/Deploy Applications to DDS Network").exists()
        assert not (browser / "Report Generator").exists()
        assert not (browser / "Simulink Extras").exists()
        assert "Create DDS Definitions" not in (browser / "DDS Blockset/index.md").read_text(
            encoding="utf-8"
        )


def test_xml_audit_keeps_duplicate_occurrences_and_simscape_blocks(tmp_path):
    (tmp_path / "demo.xml").write_text(
        """<cat><cat><title>Library</title>
        <ref type='block' target='gain.html' name='Gain'/>
        <ref type='block' target='gain.html' name='Gain'/>
        <ref type='simscapeblock' target='resistor.html' name='Resistor'/>
        <ref type='function' target='plot.html' name='plot'/>
        </cat></cat>""",
        encoding="utf-8",
    )
    assert xml_occurrences({"id": "demo"}, tmp_path) == [
        ("demo", "gain.html", "Gain", "block"),
        ("demo", "gain.html", "Gain", "block"),
        ("demo", "resistor.html", "Resistor", "simscapeblock"),
    ]


def test_markdown_body_requires_front_matter_and_preserves_content():
    assert markdown_body("---\nrelease: R2025b\n---\n# Gain\n\nBody\n") == "# Gain\n\nBody"
    with pytest.raises(ValueError, match="front matter"):
        markdown_body("# Gain")


def test_source_content_comparison_ignores_section_order_not_missing_text():
    first = "---\nx: y\n---\n# Gain\n\n## Ports\nInput\n\n## Description\nBody"
    reordered = "---\nx: y\n---\n# Gain\n\n## Description\nBody\n\n## Ports\nInput"
    assert content_lines(first) == content_lines(reordered)
    assert content_lines(first) != content_lines(reordered.replace("Input", ""))
