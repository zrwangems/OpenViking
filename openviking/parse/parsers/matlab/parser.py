# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""OpenViking built-in parser for MATLAB/Simulink files."""

from __future__ import annotations

import asyncio
import hashlib
import json
import time
import zipfile
from pathlib import Path
from typing import List, Optional, Union

from openviking.parse.base import NodeType, ParseResult, ResourceNode, create_parse_result
from openviking.parse.output import create_parse_artifact_writer
from openviking.parse.parsers.base_parser import BaseParser
from openviking.parse.parsers.matlab.formats import (
    additional_extensions,
    archive_manifest,
)
from openviking.parse.parsers.matlab.mat import parse_mat_documents
from openviking.parse.parsers.matlab.mdl import parse_mdl
from openviking.parse.parsers.matlab.measurement import parse_measurement
from openviking.parse.parsers.matlab.packages import (
    fmu_metadata,
    jar_metadata,
    package_metadata,
)
from openviking.parse.parsers.matlab.slx import parse_slx, system_json_documents
from openviking.parse.parsers.matlab.stateflow import (
    STATE_FLOW_SCHEMA,
    chart_file_name,
    chart_json,
    chart_system_path,
    parse_stateflow,
)
from openviking.parse.parsers.matlab.structured import (
    parse_fig_tree,
    parse_mlapp,
    parse_mldatx,
    parse_mlx_notebook,
    parse_requirement_set,
    parse_sldd_tree,
    protected_metadata,
    requirement_rows,
    sldd_entry_documents,
)

_NATIVE_BINARY_SUFFIXES = {
    ".mexa64",
    ".mexw32",
    ".mexw64",
    ".mexmaci64",
    ".mexmaca64",
    ".mexglx",
    ".mexsol64",
    ".dll",
    ".exe",
    ".lib",
    ".obj",
    ".pdb",
}
_MEASUREMENT_BINARY_SUFFIXES = {".mdf", ".mf4", ".blf"}
_PRESERVED_CONTAINER_SUFFIXES = {".jar", ".ctf"}
_PACKAGE_MANIFEST_SUFFIXES = {
    ".mlpkginstall",
    ".sltx",
    ".mlproj",
    ".mltbx",
    ".mlappinstall",
    ".fmu",
}


_FOLDER_SUFFIXES = {
    ".slx",
    ".mdl",
    ".sldd",
    ".mlx",
    ".mlapp",
    ".mat",
    ".fig",
    ".mdf",
    ".mf4",
    ".blf",
    ".mlproj",
    ".mltbx",
    ".mlappinstall",
    ".sltx",
    ".mlpkginstall",
    ".slreqx",
    ".slmx",
    ".mldatx",
    ".sfx",
    ".fmu",
    ".ctf",
    ".jar",
    ".p",
    ".slxp",
    ".sscp",
    ".mdlp",
    *_NATIVE_BINARY_SUFFIXES,
}


def _output_folder(path: Path) -> str:
    """Use the file stem, unless a sibling has the same stem but another suffix."""
    try:
        siblings = {
            item.suffix.lower()
            for item in path.parent.iterdir()
            if item.is_file()
            and item.stem == path.stem
            and item.suffix.lower() in _FOLDER_SUFFIXES
        }
    except OSError:
        siblings = set()
    if len(siblings) > 1:
        return f"{path.stem}_{path.suffix.lower().lstrip('.')}"
    return path.stem


def _zip_member_bytes(path: Path, name: str) -> bytes:
    with zipfile.ZipFile(path) as archive:
        return archive.read(name)


def _source_identity(path: Path) -> dict:
    """Byte length and SHA-256 of the source, so output ties to the exact file.

    Most of these containers are stored only as their parsed content, because the
    archive itself has no search value and can be large; the digest is then the
    only record of which file produced the artifact.
    """
    data = path.read_bytes()
    return {"source_bytes": len(data), "source_sha256": hashlib.sha256(data).hexdigest()}


def _parse_is_incomplete(suffix: str, payload: dict) -> bool:
    """Whether the parsed payload is known to leave part of the source out."""
    if suffix == ".fig":
        return bool(payload.get("truncated_value_count"))
    if suffix == ".mldatx":
        return bool(payload.get("unparsed_member_count"))
    return False


class MatlabParser(BaseParser):
    """Parse MATLAB project files into the plan's JSON, JSONL and original-file set."""

    # One source file maps to one output folder named after it; flattening that
    # folder would make every single-system model in a directory write the same
    # <dir>/main.json and lose the rest.
    keeps_output_folder = True

    @property
    def supported_extensions(self) -> List[str]:
        return [
            ".slx",
            ".sldd",
            ".mlx",
            ".mat",
            ".m",
            ".p",
            *_NATIVE_BINARY_SUFFIXES,
            *additional_extensions(),
        ]

    async def parse(self, source: Union[str, Path], instruction: str = "", **kwargs) -> ParseResult:
        path = Path(source)
        if not path.is_file():
            raise FileNotFoundError(f"MATLAB file not found: {path}")
        started = time.time()
        output_store = kwargs.pop("parse_output_store", None)
        language = kwargs.get("language", "zh")
        writer = await create_parse_artifact_writer(
            output_store, viking_fs=self._get_viking_fs() if output_store is None else None
        )
        warnings: list[str] = []
        try:
            suffix = path.suffix.lower()
            if suffix == ".slx" or (suffix == ".mdl" and zipfile.is_zipfile(path)):
                model = await asyncio.to_thread(parse_slx, path)
                documents = await asyncio.to_thread(system_json_documents, model, language)
                charts = await asyncio.to_thread(parse_stateflow, path)
                chart_files: set[str] = set()
                for chart in charts:
                    system_path = chart_system_path(chart)
                    nested_page = f"{system_path}/main.json"
                    leaf_page = f"{system_path}.json"
                    if nested_page in documents:
                        subsystem_index = nested_page
                    elif leaf_page in documents:
                        subsystem_index = leaf_page
                    else:
                        subsystem_index = "main.json"
                    chart_name = chart_file_name(chart)
                    if chart_name in chart_files:
                        stem, _, suffix = chart_name.rpartition(".")
                        index = 2
                        while f"{stem}-{index}.{suffix}" in chart_files:
                            index += 1
                        chart_name = f"{stem}-{index}.{suffix}"
                    chart_files.add(chart_name)
                    documents[chart_name] = await asyncio.to_thread(chart_json, chart)
                    documents[subsystem_index].setdefault("stateflow", []).append(
                        {"chart": chart.name, "path": chart_name}
                    )
                root_dir = _output_folder(path)
                for name, document in documents.items():
                    await writer.write_text(
                        f"{root_dir}/{name}",
                        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
                    )
                systems = list(_flatten(model))
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "system_count": len(systems),
                    "block_count": sum(len(system.blocks) for system in systems),
                    "subsystems": [system.name for system in systems],
                    "stateflow_chart_count": len(charts),
                    "stateflow_state_count": sum(len(chart.states) for chart in charts),
                    "stateflow_function_count": sum(len(chart.functions) for chart in charts),
                    "stateflow_note_count": sum(len(chart.notes) for chart in charts),
                    "stateflow_transition_count": sum(len(chart.transitions) for chart in charts),
                    "original_preserved": False,
                    "language": "zh-CN" if str(language).lower().startswith("zh") else "en",
                    **_source_identity(path),
                }
                title = path.stem
            elif suffix == ".mdl":
                model = await asyncio.to_thread(parse_mdl, path)
                documents = await asyncio.to_thread(system_json_documents, model, language)
                root_dir = _output_folder(path)
                for name, document in documents.items():
                    await writer.write_text(
                        f"{root_dir}/{name}",
                        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
                    )
                systems = list(_flatten(model))
                meta = {
                    "matlab_format": "mdl",
                    "system_count": len(systems),
                    "block_count": sum(len(system.blocks) for system in systems),
                    "subsystems": [system.name for system in systems],
                    "stateflow_chart_count": 0,
                    "stateflow_state_count": 0,
                    "stateflow_function_count": 0,
                    "stateflow_note_count": 0,
                    "stateflow_transition_count": 0,
                    "original_preserved": False,
                    "language": "zh-CN" if str(language).lower().startswith("zh") else "en",
                    **_source_identity(path),
                }
                title = path.stem
            elif suffix == ".mat":
                folder = _output_folder(path)
                documents, mat_warnings = await asyncio.to_thread(parse_mat_documents, path)
                for name, document in documents.items():
                    if isinstance(document, bytes):
                        await writer.write_bytes(f"{folder}/{name}", document)
                    else:
                        await writer.write_text(f"{folder}/{name}", document)
                warnings.extend(mat_warnings)
                # A MAT file is kept as its parsed values, except when the reader
                # reports content it could not expand (HDF5 reference arrays):
                # then the bytes stay the only complete copy.
                incomplete = bool(mat_warnings)
                if incomplete:
                    await writer.write_bytes(
                        f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                    )
                meta = {
                    "matlab_format": "mat",
                    "original_preserved": incomplete,
                    **_source_identity(path),
                }
                title = path.stem
            elif suffix == ".p":
                folder = _output_folder(path)
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(protected_metadata, path, "pcode")
                await writer.write_text(
                    f"{folder}/metadata.json",
                    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": "p",
                    "parse_status": "opaque",
                    "original_preserved": True,
                }
                title = path.stem
            elif suffix in {".sldd", ".mlx", ".fig", ".mldatx", ".slreqx", ".slmx", ".mlapp"}:
                payload: dict = {}
                auxiliary: dict[str, bytes] = {}
                if suffix == ".sldd":
                    payload = await asyncio.to_thread(parse_sldd_tree, path)
                elif suffix == ".mlx":
                    payload, auxiliary = await asyncio.to_thread(parse_mlx_notebook, path)
                elif suffix == ".fig":
                    payload = await asyncio.to_thread(parse_fig_tree, path)
                elif suffix == ".mldatx":
                    payload = await asyncio.to_thread(parse_mldatx, path)
                elif suffix in {".slreqx", ".slmx"}:
                    payload = await asyncio.to_thread(parse_requirement_set, path)
                else:
                    payload, auxiliary = await asyncio.to_thread(parse_mlapp, path)
                folder = _output_folder(path)
                # Only parsed content is kept: the archive itself has no search
                # value and can be tens of megabytes. When the parse reports
                # content it could not expand, the bytes stay as well.
                preserved = _parse_is_incomplete(suffix, payload)
                if preserved:
                    await writer.write_bytes(
                        f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                    )
                for name, data in auxiliary.items():
                    await writer.write_bytes(f"{folder}/{name}", data)
                if suffix == ".sldd":
                    rows, data_files = await asyncio.to_thread(sldd_entry_documents, payload)
                    for name, content in data_files.items():
                        await writer.write_bytes(f"{folder}/{name}", content)
                    await writer.write_text(
                        f"{folder}/entries.jsonl",
                        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
                    )
                elif suffix == ".mlx":
                    await writer.write_text(
                        f"{folder}/notebook.json",
                        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                    )
                elif suffix == ".fig":
                    await writer.write_text(
                        f"{folder}/figure.json",
                        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                    )
                elif suffix == ".mldatx":
                    await writer.write_text(
                        f"{folder}/tests.json",
                        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                    )
                elif suffix in {".slreqx", ".slmx"}:
                    requirements, links = await asyncio.to_thread(requirement_rows, payload)
                    if suffix == ".slreqx":
                        await writer.write_text(
                            f"{folder}/requirements.jsonl",
                            "\n".join(
                                json.dumps(row, ensure_ascii=False) for row in requirements
                            )
                            + "\n",
                        )
                    await writer.write_text(
                        f"{folder}/links.jsonl",
                        "\n".join(json.dumps(row, ensure_ascii=False) for row in links) + "\n",
                    )
                else:
                    await writer.write_text(
                        f"{folder}/app.json",
                        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                    )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "structured_format": payload.get("schema", ""),
                    "original_preserved": preserved,
                    **_source_identity(path),
                }
                title = path.stem
            elif suffix == ".sfx":
                folder = _output_folder(path)
                # A Stateflow chart file is fully parsed, so only that parsed
                # chart is kept; the ZIP itself would only duplicate it.
                charts = await asyncio.to_thread(parse_stateflow, path)
                await writer.write_text(
                    f"{folder}/stateflow.json",
                    json.dumps(
                        {
                            "schema": STATE_FLOW_SCHEMA,
                            "file": path.name,
                            "charts": [chart_json(chart) for chart in charts],
                        },
                        ensure_ascii=False,
                        indent=2,
                    )
                    + "\n",
                )
                meta = {
                    "matlab_format": "sfx",
                    "original_preserved": False,
                    "stateflow_chart_count": len(charts),
                    "stateflow_state_count": sum(len(chart.states) for chart in charts),
                    "stateflow_function_count": sum(len(chart.functions) for chart in charts),
                    "stateflow_note_count": sum(len(chart.notes) for chart in charts),
                    "stateflow_transition_count": sum(len(chart.transitions) for chart in charts),
                    **_source_identity(path),
                }
                title = path.stem
            elif suffix in _NATIVE_BINARY_SUFFIXES:
                folder = _output_folder(path)
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(
                    protected_metadata, path, f"native-{suffix.removeprefix('.')}"
                )
                await writer.write_text(
                    f"{folder}/metadata.json",
                    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "parse_status": "opaque",
                    "original_preserved": True,
                }
                title = path.stem
            elif suffix in _MEASUREMENT_BINARY_SUFFIXES:
                folder = _output_folder(path)
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(
                    protected_metadata, path, f"measurement-{suffix.removeprefix('.')}"
                )
                documents, measurement_warnings = await asyncio.to_thread(
                    parse_measurement, path
                )
                for name, document in documents.items():
                    await writer.write_text(f"{folder}/{name}", document)
                warnings.extend(measurement_warnings)
                channel_payload = json.loads(documents["channels.json"])
                metadata["parse_status"] = channel_payload.get("parse_status", "metadata-only")
                await writer.write_text(
                    f"{folder}/metadata.json",
                    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": True,
                }
                title = path.stem
            elif suffix in _PRESERVED_CONTAINER_SUFFIXES:
                folder = _output_folder(path)
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                manifest = await asyncio.to_thread(archive_manifest, path)
                manifest["type"] = suffix.removeprefix(".")
                if suffix == ".jar":
                    manifest = await asyncio.to_thread(jar_metadata, path, manifest)
                await writer.write_text(
                    f"{folder}/manifest.json",
                    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": True,
                    "encrypted": manifest["encrypted"],
                }
                title = path.stem
            elif suffix in _PACKAGE_MANIFEST_SUFFIXES:
                folder = _output_folder(path)
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                manifest = await asyncio.to_thread(archive_manifest, path)
                manifest["type"] = suffix.removeprefix(".")
                if suffix == ".fmu":
                    manifest = await asyncio.to_thread(fmu_metadata, path, manifest)
                else:
                    manifest = await asyncio.to_thread(package_metadata, path, manifest)
                await writer.write_text(
                    f"{folder}/manifest.json",
                    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                )
                if suffix == ".fmu" and "modelDescription.xml" in {
                    member["name"] for member in manifest["members"]
                }:
                    await writer.write_bytes(
                        f"{folder}/modelDescription.xml",
                        await asyncio.to_thread(
                            _zip_member_bytes, path, "modelDescription.xml"
                        ),
                    )
                if suffix == ".sltx":
                    template = dict(manifest.get("template") or {})
                    template.update(
                        {
                            "schema": "ov.matlab.template/1",
                            "file": path.name,
                            "members": [
                                member["name"]
                                for member in manifest["members"]
                                if "template" in member["name"].casefold()
                            ],
                        }
                    )
                    await writer.write_text(
                        f"{folder}/template.json",
                        json.dumps(template, ensure_ascii=False, indent=2) + "\n",
                    )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": True,
                    "encrypted": manifest["encrypted"],
                }
                title = path.stem
            elif suffix in {".slxp", ".mdlp", ".sscp"}:
                folder = _output_folder(path)
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(
                    protected_metadata, path, suffix.removeprefix(".")
                )
                await writer.write_text(
                    f"{folder}/metadata.json",
                    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "parse_status": "opaque",
                    "original_preserved": True,
                }
                title = path.stem
            else:
                # Plan: plain source/configuration files are stored as the
                # original bytes, never as a parser-generated Markdown page.
                await writer.write_bytes(path.name, await asyncio.to_thread(path.read_bytes))
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": True,
                }
                title = path.stem

            root = ResourceNode(type=NodeType.ROOT, title=title, level=0)
            result = create_parse_result(
                root=root,
                source_path=str(path),
                source_format=f"matlab-{suffix.removeprefix('.')}",
                parser_name="MatlabParser",
                parser_version="1.0",
                parse_time=time.time() - started,
                meta=meta,
                warnings=warnings,
            )
            result.artifact_ref = await writer.finalize()
            result.temp_dir_path = result.artifact_ref.root
            return result
        except Exception:
            await writer.cleanup()
            raise

    async def parse_content(
        self, content: str, source_path: Optional[str] = None, instruction: str = "", **kwargs
    ) -> ParseResult:
        raise NotImplementedError("MATLAB/Simulink containers must be parsed from a file path")


def _flatten(root):
    yield root
    for child in root.children:
        yield from _flatten(child)
