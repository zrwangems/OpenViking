# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""OpenViking built-in parser for MATLAB/Simulink files."""

from __future__ import annotations

import asyncio
import json
import time
import zipfile
from pathlib import Path
from typing import List, Optional, Union

from openviking.parse.base import NodeType, ParseResult, ResourceNode, create_parse_result
from openviking.parse.output import create_parse_artifact_writer
from openviking.parse.parsers.base_parser import BaseParser
from openviking.parse.parsers.matlab.coverage import coverage_json
from openviking.parse.parsers.matlab.formats import (
    additional_extensions,
    is_additional_format,
    parse_additional,
)
from openviking.parse.parsers.matlab.mat import parse_mat_documents
from openviking.parse.parsers.matlab.mdl import parse_mdl
from openviking.parse.parsers.matlab.scripts import parse_m_file
from openviking.parse.parsers.matlab.slx import parse_slx, system_json_documents
from openviking.parse.parsers.matlab.stateflow import (
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


class MatlabParser(BaseParser):
    """Convert MATLAB containers into searchable Markdown without executing code."""

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
        language = kwargs.get("language", "en")
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
                    chart_name = f"stateflow/chart_{chart.chart_id}.json"
                    documents[chart_name] = await asyncio.to_thread(chart_json, chart)
                    documents[subsystem_index].setdefault("stateflow", []).append(
                        {"chart_id": chart.chart_id, "path": chart_name}
                    )
                root_dir = path.stem
                for name, document in documents.items():
                    await writer.write_text(
                        f"{root_dir}/{name}",
                        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
                    )
                coverage = await asyncio.to_thread(coverage_json, path, model)
                await writer.write_text(
                    f"{root_dir}/coverage.json",
                    json.dumps(coverage, ensure_ascii=False, indent=2) + "\n",
                )
                systems = list(_flatten(model))
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "system_count": len(systems),
                    "block_count": sum(len(system.blocks) for system in systems),
                    "subsystems": [system.name for system in systems],
                    "stateflow_chart_count": len(charts),
                    "stateflow_state_count": sum(len(chart.states) for chart in charts),
                    "stateflow_transition_count": sum(len(chart.transitions) for chart in charts),
                    "original_preserved": False,
                    "language": "zh-CN" if str(language).lower().startswith("zh") else "en",
                }
                title = path.stem
            elif suffix == ".mdl":
                model = await asyncio.to_thread(parse_mdl, path)
                documents = await asyncio.to_thread(system_json_documents, model, language)
                root_dir = path.stem
                for name, document in documents.items():
                    await writer.write_text(
                        f"{root_dir}/{name}",
                        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
                    )
                systems = list(_flatten(model))
                coverage = {
                    "schema": "ov.matlab.simulink-coverage/1",
                    "model": path.stem,
                    "systems": len(systems),
                    "blocks": sum(len(system.blocks) for system in systems),
                    "edges": sum(len(system.edges) for system in systems),
                    "conserving_edges": sum(
                        edge.kind == "physical-conserving"
                        for system in systems
                        for edge in system.edges
                    ),
                    "physical_ports": sum(len(system.physical_ports) for system in systems),
                    "subsystem_types": sorted(
                        {kind for system in systems for kind in system.subsystem_types}
                    ),
                    "stateflow_charts": [],
                    "workspace_data": [],
                    "boundary": "Text MDL grammar is not public; unresolved sections are kept out of the graph.",
                }
                await writer.write_text(
                    f"{root_dir}/coverage.json",
                    json.dumps(coverage, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": "mdl",
                    "system_count": len(systems),
                    "block_count": sum(len(system.blocks) for system in systems),
                    "subsystems": [system.name for system in systems],
                    "stateflow_chart_count": 0,
                    "stateflow_state_count": 0,
                    "stateflow_transition_count": 0,
                    "original_preserved": False,
                    "language": "zh-CN" if str(language).lower().startswith("zh") else "en",
                }
                title = path.stem
            elif suffix == ".p":
                folder = path.stem
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(protected_metadata, path, "pcode")
                await writer.write_text(
                    f"{folder}/{path.name}.json",
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
                folder = path.stem if suffix in {".mlx", ".mlapp"} else ""
                for name, data in auxiliary.items():
                    await writer.write_bytes(f"{folder}/{name}" if folder else name, data)
                target = f"{folder}/{path.name}.json" if folder else f"{path.name}.json"
                await writer.write_text(
                    target,
                    json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "structured_format": payload.get("schema", ""),
                    "original_preserved": False,
                }
                title = path.stem
            elif suffix in _NATIVE_BINARY_SUFFIXES:
                folder = path.stem
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(
                    protected_metadata, path, f"native-{suffix.removeprefix('.')}"
                )
                await writer.write_text(
                    f"{folder}/{path.name}.json",
                    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "parse_status": "opaque",
                    "original_preserved": True,
                }
                title = path.stem
            elif suffix in _MEASUREMENT_BINARY_SUFFIXES:
                folder = path.stem
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(
                    protected_metadata, path, f"measurement-{suffix.removeprefix('.')}"
                )
                metadata["boundary"] = (
                    "Original bytes are kept. Channel decoding requires an ASAM MDF or "
                    "Vector BLF library; this parser does not guess signal values."
                )
                await writer.write_text(
                    f"{folder}/{path.name}.json",
                    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                )
                await writer.write_text(
                    f"{folder}/channels.json",
                    json.dumps(
                        {
                            "schema": "ov.matlab.measurement/1",
                            "format": suffix.removeprefix("."),
                            "channels": [],
                            "parse_status": "metadata-only",
                        },
                        ensure_ascii=False,
                        indent=2,
                    )
                    + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "parse_status": "metadata-only",
                    "original_preserved": True,
                }
                title = path.stem
            elif suffix in _PRESERVED_CONTAINER_SUFFIXES:
                folder = path.stem
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                content, _ = await asyncio.to_thread(parse_additional, path)
                await writer.write_text(f"{folder}/{path.name}.md", content)
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": True,
                }
                title = path.stem
            elif suffix in {".slxp", ".mdlp", ".sscp"}:
                folder = path.stem
                await writer.write_bytes(
                    f"{folder}/{path.name}", await asyncio.to_thread(path.read_bytes)
                )
                metadata = await asyncio.to_thread(
                    protected_metadata, path, suffix.removeprefix(".")
                )
                await writer.write_text(
                    f"{folder}/{path.name}.json",
                    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
                )
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "parse_status": "opaque",
                    "original_preserved": True,
                }
                title = path.stem
            else:
                if suffix == ".mat":
                    mat_documents, mat_warnings = await asyncio.to_thread(parse_mat_documents, path)
                    for name, document in mat_documents.items():
                        await writer.write_text(name, document)
                    warnings.extend(mat_warnings)
                    content = mat_documents[f"{path.name}.md"]
                elif suffix == ".m":
                    content = await asyncio.to_thread(parse_m_file, path)
                elif is_additional_format(suffix):
                    content, _ = await asyncio.to_thread(parse_additional, path)
                else:
                    raise ValueError(f"Unsupported MATLAB extension: {suffix}")
                # Plain MATLAB source stays a code resource. Containers become
                # parsed Markdown/data only; never expose their binary as text.
                if suffix in {".m", ".asv", ".ssc", ".tlc"} or (
                    suffix == ".prj" and not zipfile.is_zipfile(path)
                ):
                    await writer.write_bytes(path.name, await asyncio.to_thread(path.read_bytes))
                elif suffix != ".mat":
                    await writer.write_text(f"{path.name}.md", content)
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": suffix in {".m", ".asv", ".ssc", ".tlc"}
                    or (suffix == ".prj" and not zipfile.is_zipfile(path)),
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
