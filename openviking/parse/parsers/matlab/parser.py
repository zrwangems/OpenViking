# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""OpenViking built-in parser for MATLAB/Simulink files."""

from __future__ import annotations

import asyncio
import contextvars
import hashlib
import json
import posixpath
import shutil
import tempfile
import time
import zipfile
from contextlib import suppress
from pathlib import Path
from typing import Any, List, Optional, Union

from openviking.parse.base import NodeType, ParseResult, ResourceNode, create_parse_result
from openviking.parse.output import copy_artifact_tree, create_parse_artifact_writer
from openviking.parse.parsers.base_parser import BaseParser
from openviking.parse.parsers.matlab.figures import figure_text, parse_figure
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
    state_transition_count,
)
from openviking.parse.parsers.matlab.structured import (
    parse_mlapp,
    parse_mldatx,
    parse_mlx_notebook,
    parse_requirement_set,
    parse_sldd_tree,
    protected_metadata,
    requirement_rows,
    sldd_entry_documents,
)
from openviking.parse.parsers.matlab.workbook import parse_workbook, workbook_text

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
    ".sltx",
    ".mlproj",
    ".mltbx",
    ".fmu",
}
# Package containers whose members are the content: the archive itself is only a
# listing, so members that carry searchable meaning are parsed on their own and
# placed under ``members/``.
_MEMBER_EXPANSIONS = frozenset({".sltx", ".mlproj", ".mltbx"})
# Members live under this prefix in a package archive; the rest is metadata.
_MEMBER_ROOT = "fsroot/"
# Members that carry no searchable meaning: platform binaries, protected sources,
# firmware images and nested packages. Their names stay in the manifest; their
# bytes are not stored and they are not counted as failed expansion.
_MEMBER_SKIP_SUFFIXES = frozenset(
    {
        *_NATIVE_BINARY_SUFFIXES,
        ".p",
        ".slxp",
        ".mdlp",
        ".sscp",
        ".mlappinstall",
        ".mlpkginstall",
        ".jar",
        ".ctf",
        ".sltx",
        ".mlproj",
        ".mltbx",
        ".hex",
        ".s19",
        ".bin",
        ".elf",
        ".slxc",
        ".autosave",
        ".asv",
    }
)
_MEMBER_EXPANSION_DEPTH = contextvars.ContextVar("matlab_member_expansion_depth", default=0)

# Formats the general document pipeline also claims. Inside a MATLAB project the
# project parser owns them: a workbook is a table of numbers there, so its cells
# are read instead of being handed to the office-document renderer.
PROJECT_SHARED_EXTENSIONS = frozenset({".xlsx"})
# Sources whose bytes are the only useful output. Installers, p-code and
# platform binaries are imported as the original file itself: no wrapper
# folder and no manifest/metadata sidecar. L0/L1 decides what the file is for.
_ORIGINAL_ONLY_SUFFIXES = {
    ".p",
    ".mlappinstall",
    ".mlpkginstall",
    *_NATIVE_BINARY_SUFFIXES,
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
    ".sltx",
    ".slreqx",
    ".slmx",
    ".mldatx",
    ".sfx",
    ".fmu",
    ".ctf",
    ".jar",
    ".slxp",
    ".sscp",
    ".mdlp",
    ".xlsx",
}


def _member_rel(name: str) -> str:
    """Member path below ``fsroot/``, refusing anything that would escape it."""
    rel = name[len(_MEMBER_ROOT) :].replace("\\", "/").strip("/")
    parts = [part for part in rel.split("/") if part not in {"", "."}]
    if not parts or any(part == ".." for part in parts):
        return ""
    return "/".join(parts)


def _already_in_project(import_root: Optional[str], rel: str, data: bytes) -> bool:
    """Whether the imported project already holds this member byte for byte.

    A package archive is usually exported from a project that is being imported
    at the same time; storing its members again would only duplicate the tree.
    """
    if not import_root:
        return False
    candidate = Path(import_root).joinpath(*rel.split("/"))
    try:
        if not candidate.is_file() or candidate.stat().st_size != len(data):
            return False
        return hashlib.sha256(candidate.read_bytes()).digest() == hashlib.sha256(data).digest()
    except OSError:
        return False


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
        # Charts recovered from the MCOS payload keep the source bytes too: the
        # reader works by position, and re-reading is cheap if a later release
        # changes the record layout.
        return payload.get("status") not in {None, "parsed"}
    if suffix == ".mldatx":
        return bool(payload.get("unparsed_member_count"))
    return False


class MatlabParser(BaseParser):
    """Parse MATLAB project files into the plan's JSON, JSONL and original-file set."""

    # One source file maps to one output folder named after it; flattening that
    # folder would make every single-system model in a directory write the same
    # <dir>/main.json and lose the rest.
    keeps_output_folder = True

    async def _expand_members(
        self,
        path: Path,
        writer: Any,
        folder: str,
        manifest: dict,
        warnings: list[str],
        *,
        language: str,
        import_root: Optional[str] = None,
    ) -> dict:
        """Parse the ``fsroot/`` members of a package archive into ``members/``.

        Only members with searchable meaning are kept: each one goes through the
        same parser a standalone file would get, so a model inside an archive
        yields the same JSON as that model on disk. Two kinds of member are
        recorded but not stored — binaries and nested packages, which carry no
        readable content, and members the imported project already holds byte for
        byte, which would only duplicate the tree. The caller keeps the archive
        bytes when a member that should expand could not be read.
        """
        members = [
            member
            for member in manifest.get("members", [])
            if member["name"].startswith(_MEMBER_ROOT)
            and not member["name"].endswith("/")
            and not member.get("encrypted")
        ]
        record: dict = {
            "root": "members",
            "member_prefix": _MEMBER_ROOT,
            "member_count": len(members),
            "expanded": 0,
            "failed": [],
            "skipped": [],
            "skipped_note": "",
            "members": [],
        }
        if not members:
            record["skipped_note"] = "包内没有 fsroot 成员"
            return {"complete": True, "expanded": 0, "record": record}
        if manifest.get("encrypted"):
            record["skipped_note"] = "成员加密，字节无法读出"
            return {"complete": False, "expanded": 0, "record": record}
        if _MEMBER_EXPANSION_DEPTH.get() > 0:
            record["skipped_note"] = "包内嵌套的包容器不再二次展开"
            return {"complete": False, "expanded": 0, "record": record}

        expanded: list[dict] = []
        used_stems: set[tuple[str, str]] = set()
        temp_root = Path(tempfile.mkdtemp(prefix="matlab-members-"))
        token = _MEMBER_EXPANSION_DEPTH.set(_MEMBER_EXPANSION_DEPTH.get() + 1)
        try:
            with zipfile.ZipFile(path) as archive:
                for member in members:
                    rel = _member_rel(member["name"])
                    if not rel:
                        record["failed"].append(
                            {"member": member["name"], "error": "成员路径不安全，未展开"}
                        )
                        continue
                    parent, _, name = rel.rpartition("/")
                    stem, extension = posixpath.splitext(name)
                    data = archive.read(member["name"])
                    if extension.lower() in _MEMBER_SKIP_SUFFIXES:
                        # No searchable text in a binary or a nested package: the
                        # manifest already names it, so its bytes are dropped.
                        record["skipped"].append(
                            {"member": member["name"], "reason": "二进制或嵌套包容器，无可检索语义"}
                        )
                        continue
                    if _already_in_project(import_root, rel, data):
                        record["skipped"].append(
                            {"member": member["name"], "reason": "工程里已有同名同内容文件"}
                        )
                        continue
                    # Two members with one stem (model.slx beside model.sldd) would
                    # both write a folder named after the stem; the second keeps its
                    # suffix so neither overwrites the other.
                    local_name = name
                    if extension.lower() in _FOLDER_SUFFIXES and (parent, stem) in used_stems:
                        local_name = f"{stem}_{extension.lstrip('.')}{extension}"
                    used_stems.add((parent, stem))
                    local = (
                        temp_root.joinpath(*parent.split("/")) / local_name
                        if parent
                        else temp_root / local_name
                    )
                    local.parent.mkdir(parents=True, exist_ok=True)
                    local.write_bytes(data)
                    target = f"{folder}/members" + (f"/{parent}" if parent else "")
                    nested = None
                    try:
                        nested = await self.parse(
                            local, parse_output_store=writer.store, language=language
                        )
                        await copy_artifact_tree(
                            source_store=writer.store,
                            source_ref=nested.artifact_ref,
                            source_rel="",
                            target=writer,
                            target_rel=target,
                        )
                    except Exception as error:  # one bad member must not lose the rest
                        record["failed"].append({"member": member["name"], "error": str(error)})
                        warnings.append(f"模板成员未展开 {rel}: {error}")
                    else:
                        output = (
                            f"{target}/{posixpath.splitext(local_name)[0]}"
                            if extension.lower() in _FOLDER_SUFFIXES
                            else f"{target}/{local_name}"
                        )
                        expanded.append(
                            {
                                "member": member["name"],
                                "path": output.removeprefix(f"{folder}/"),
                            }
                        )
                    finally:
                        if nested is not None:
                            with suppress(Exception):
                                await writer.store.cleanup(nested.artifact_ref)
        finally:
            _MEMBER_EXPANSION_DEPTH.reset(token)
            shutil.rmtree(temp_root, ignore_errors=True)
        record["expanded"] = len(expanded)
        record["members"] = expanded
        return {
            "complete": not record["failed"],
            "expanded": len(expanded),
            "record": record,
        }

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
        suffix = path.suffix.lower()
        writer = await create_parse_artifact_writer(
            output_store,
            viking_fs=self._get_viking_fs() if output_store is None else None,
            root_type="file" if suffix in _ORIGINAL_ONLY_SUFFIXES else "dir",
        )
        warnings: list[str] = []
        try:
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
                    "stateflow_transition_count": sum(
                        state_transition_count(chart) for chart in charts
                    ),
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
            elif suffix == ".xlsx":
                folder = _output_folder(path)
                payload = await asyncio.to_thread(parse_workbook, path)
                parsed = payload.get("parse_status") == "parsed"
                await writer.write_text(
                    f"{folder}/workbook.json",
                    json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                )
                # The table page is what the ingest searches; the JSON keeps every
                # cell, formula and merged range for anything that needs the values.
                await writer.write_text(f"{folder}/workbook.md", workbook_text(payload))
                if not parsed:
                    # An unreadable workbook (encrypted, renamed .xls, damaged ZIP)
                    # leaves the bytes as the only copy of the file.
                    await writer.write_bytes(
                        f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                    )
                    warnings.append(
                        f"{path.name}: 单元格读取失败，保留原件（{payload.get('error', '')}）"
                    )
                meta = {
                    "matlab_format": "xlsx",
                    "structured_format": payload["schema"],
                    "original_preserved": not parsed,
                    "sheet_count": payload.get("sheet_count", 0),
                    "cell_count": (payload.get("summary") or {}).get("cells", 0),
                    "formula_cells": (payload.get("summary") or {}).get("formula_cells", 0),
                    **_source_identity(path),
                }
                title = path.stem
            elif suffix in _ORIGINAL_ONLY_SUFFIXES:
                # The source is the resource: import it at the artifact root so
                # the import yields one file node and nothing else.
                data = await asyncio.to_thread(path.read_bytes)
                await writer.write_bytes(path.name, data)
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "parse_status": "original-only",
                    "original_preserved": True,
                    "source_bytes": len(data),
                    "source_sha256": hashlib.sha256(data).hexdigest(),
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
                    payload, auxiliary = await asyncio.to_thread(parse_figure, path)
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
                    # FIG series files already carry their folder; other formats
                    # return plain names inside the output folder.
                    target = name if name.startswith(f"{folder}/") else f"{folder}/{name}"
                    await writer.write_bytes(target, data)
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
                    # figure.json carries the chart types, series and labels;
                    # figure.md is the readable page the ingest searches.
                    await writer.write_text(
                        f"{folder}/figure.json",
                        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                    )
                    await writer.write_text(f"{folder}/figure.md", figure_text(payload))
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
                    "stateflow_transition_count": sum(
                        state_transition_count(chart) for chart in charts
                    ),
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
                # A jar or ctf expands into classes or opaque bytes, not into
                # readable content, so the archive is the resource itself; the
                # manifest only gives L0/L1 what it needs to describe it.
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                manifest = await asyncio.to_thread(archive_manifest, path)
                manifest["type"] = suffix.removeprefix(".")
                if suffix == ".jar":
                    manifest = await asyncio.to_thread(jar_metadata, path, manifest)
                manifest["boundary"] = (
                    "无可读成员的包：原件作为资源保留，成员名、类型与大小见 members，"
                    "由 L0/L1 描述其用途。"
                )
                await writer.write_text(
                    f"{folder}/manifest.json",
                    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": True,
                    "encrypted": manifest["encrypted"],
                    **_source_identity(path),
                }
                title = path.stem
            elif suffix in _PACKAGE_MANIFEST_SUFFIXES:
                folder = _output_folder(path)
                manifest = await asyncio.to_thread(archive_manifest, path)
                manifest["type"] = suffix.removeprefix(".")
                if suffix == ".fmu":
                    manifest = await asyncio.to_thread(fmu_metadata, path, manifest)
                else:
                    manifest = await asyncio.to_thread(package_metadata, path, manifest)
                # Packages are containers: their own bytes are kept only for an
                # FMU (a compiled artifact with no readable content) and for a
                # template whose members could not all be expanded.
                expansion: dict = {}
                if suffix in _MEMBER_EXPANSIONS:
                    expansion = await self._expand_members(
                        path,
                        writer,
                        folder,
                        manifest,
                        warnings,
                        language=language,
                        import_root=kwargs.get("link_rewrite_root"),
                    )
                    manifest["expansion"] = expansion["record"]
                complete = expansion.get("complete", True)
                preserved = suffix == ".fmu" or not complete
                if suffix == ".fmu":
                    # An FMU is compiled: its bytes and modelDescription are the content.
                    boundary = "FMU 保留原件字节与 modelDescription.xml 清单。"
                elif preserved:
                    boundary = (
                        "有成员未能展开，原件字节保留以固化完整内容；已展开的成员见 expansion。"
                    )
                elif expansion.get("expanded"):
                    boundary = (
                        "有语义的 fsroot 成员已逐个解析到 members/，原件字节不保存；"
                        "二进制与工程里已有的成员只记在 expansion.skipped。"
                    )
                else:
                    boundary = (
                        "包容器只留清单：成员要么无检索语义、要么工程里已有，原件字节不保存；"
                        "成员名、类型与大小见 members。"
                    )
                manifest["boundary"] = boundary
                if preserved:
                    await writer.write_bytes(
                        f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
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
                await writer.write_text(
                    f"{folder}/manifest.json",
                    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": preserved,
                    "encrypted": manifest["encrypted"],
                    "expanded_member_count": expansion.get("expanded", 0),
                    **_source_identity(path),
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
            result.artifact_ref = await writer.finalize(
                resource_rel=path.name if suffix in _ORIGINAL_ONLY_SUFFIXES else ""
            )
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
