# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""OpenViking built-in parser for MATLAB/Simulink files."""

from __future__ import annotations

import asyncio
import posixpath
import time
import zipfile
from pathlib import Path
from typing import List, Optional, Union

from openviking.parse.base import NodeType, ParseResult, ResourceNode, create_parse_result
from openviking.parse.output import create_parse_artifact_writer
from openviking.parse.parsers.base_parser import BaseParser
from openviking.parse.parsers.matlab.coverage import render_coverage
from openviking.parse.parsers.matlab.formats import (
    additional_extensions,
    is_additional_format,
    parse_additional,
)
from openviking.parse.parsers.matlab.mat import parse_mat_documents
from openviking.parse.parsers.matlab.scripts import parse_m_file, parse_mlx, parse_p_file
from openviking.parse.parsers.matlab.sldd import parse_sldd
from openviking.parse.parsers.matlab.slx import parse_slx, system_documents
from openviking.parse.parsers.matlab.stateflow import (
    chart_system_path,
    parse_stateflow,
    render_stateflow,
)


class MatlabParser(BaseParser):
    """Convert MATLAB containers into searchable Markdown without executing code."""

    @property
    def supported_extensions(self) -> List[str]:
        return [".slx", ".sldd", ".mlx", ".mat", ".m", ".p", *additional_extensions()]

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
                documents = await asyncio.to_thread(system_documents, model, language)
                charts = await asyncio.to_thread(parse_stateflow, path)
                for chart in charts:
                    system_path = chart_system_path(chart)
                    nested_page = f"{system_path}/main.md"
                    leaf_page = f"{system_path}.md"
                    if nested_page in documents:
                        subsystem_index = nested_page
                    elif leaf_page in documents:
                        subsystem_index = leaf_page
                    else:
                        subsystem_index = "main.md"
                    chart_name = f"stateflow/chart_{chart.chart_id}.md"
                    documents[chart_name] = render_stateflow(chart)
                    link = posixpath.relpath(chart_name, posixpath.dirname(subsystem_index))
                    documents[subsystem_index] += (
                        f"\n- [Stateflow Chart {chart.chart_id}：状态、动作与转移]({link})\n"
                    )
                root_dir = path.stem
                for name, content in documents.items():
                    await writer.write_text(f"{root_dir}/{name}", content)
                await writer.write_text(
                    f"{root_dir}/coverage.md", await asyncio.to_thread(render_coverage, path, model)
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
            elif suffix == ".p":
                content = await asyncio.to_thread(parse_p_file, path)
                await writer.write_text(f"{path.stem}/index.md", content)
                meta = {"matlab_format": "p", "parse_status": "opaque", "original_preserved": False}
                title = path.stem
            else:
                if suffix == ".sldd":
                    content = await asyncio.to_thread(parse_sldd, path)
                elif suffix == ".mlx":
                    content = await asyncio.to_thread(parse_mlx, path)
                elif suffix == ".mat":
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
                if suffix in {".m", ".asv", ".ssc", ".tlc"}:
                    await writer.write_bytes(path.name, await asyncio.to_thread(path.read_bytes))
                elif suffix != ".mat":
                    await writer.write_text(f"{path.name}.md", content)
                meta = {
                    "matlab_format": suffix.removeprefix("."),
                    "original_preserved": suffix in {".m", ".asv", ".ssc", ".tlc"},
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
