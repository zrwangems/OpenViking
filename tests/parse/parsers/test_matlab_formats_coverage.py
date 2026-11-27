import asyncio
import json
import zipfile
from pathlib import Path

import pytest

from openviking.parse.directory_scan import scan_directory
from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.matlab.parser import MatlabParser


def test_text_and_binary_project_extensions_are_classified(tmp_path):
    (tmp_path / "plant.ssc").write_text("component plant\nend\n", encoding="utf-8")
    for ext in (".arxml", ".dbc", ".ldf", ".a2l", ".rsp", ".map"):
        (tmp_path / f"file{ext}").write_text("sample\n", encoding="utf-8")
    (tmp_path / "solver.dll").write_bytes(b"MZ\x00\x00")
    (tmp_path / "solver.mexw32").write_bytes(b"MZ\x00\x00")
    (tmp_path / "old.asv").write_text("function y=f()\ny=1;\nend\n", encoding="utf-8")

    result = scan_directory(tmp_path, strict=True)

    assert result.unsupported == []
    assert {entry.path.name for entry in result.processable} >= {
        "file.arxml",
        "file.dbc",
        "file.ldf",
        "file.a2l",
        "file.rsp",
        "file.map",
        "solver.dll",
        "solver.mexw32",
    }
    # An editor backup is a stale copy of a source file already in the project.
    assert "old.asv" not in {entry.path.name for entry in result.processable}
    assert any(entry.startswith("old.asv (") for entry in result.skipped)


def test_legacy_mdl_becomes_system_json(tmp_path):
    model = """Model {
  Name "legacy"
  System {
    Block { BlockType Inport Name "u" Port "1" }
    Block { BlockType Gain Name "g" Gain "2" }
    Block { BlockType Outport Name "y" Port "1" }
    Line { SrcBlock "u" SrcPort 1 DstBlock "g" DstPort 1 Name "u" }
    Line { SrcBlock "g" SrcPort 1 DstBlock "y" DstPort 1 Name "y" }
  }
}"""
    path = tmp_path / "legacy.mdl"
    path.write_text(model, encoding="utf-8")
    result = asyncio.run(
        MatlabParser().parse(path, parse_output_store=LocalParseOutputStore(tmp_path / "art"))
    )
    root = Path(result.artifact_ref.root)
    document = json.loads((root / "legacy" / "main.json").read_text(encoding="utf-8"))
    assert document["schema"] == "ov.matlab.simulink/1"
    assert [block["name"] for block in document["blocks"]] == ["u", "g", "y"]
    assert len(document["edges"]) == 2


@pytest.mark.asyncio
async def test_jar_keeps_only_its_manifest_and_native_binary_keeps_original(tmp_path):
    jar = tmp_path / "library.jar"
    with zipfile.ZipFile(jar, "w") as archive:
        archive.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n")
        archive.writestr("org/example/Engine.class", b"\xca\xfe\xba\xbe")
    dll = tmp_path / "solver.dll"
    dll.write_bytes(b"MZ\x00\x00")

    result = await MatlabParser().parse(
        jar, parse_output_store=LocalParseOutputStore(tmp_path / "art-jar")
    )
    root = Path(result.artifact_ref.root)
    # A package container is recorded, not ingested: the manifest says what is
    # inside and the archive bytes are not stored.
    assert not list(root.rglob(jar.name))
    manifest = json.loads((root / "library" / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["classes"] == ["org/example/Engine.class"]
    assert manifest["java_manifest"]["Manifest-Version"] == "1.0"
    assert result.meta["original_preserved"] is False

    result = await MatlabParser().parse(
        dll, parse_output_store=LocalParseOutputStore(tmp_path / "art-dll")
    )
    assert list(Path(result.artifact_ref.root).rglob(dll.name)), dll
