# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Structured JSON documents for MATLAB formats that carry nested structure.

The formats here are represented as JSON objects instead of Markdown tables so
that nesting, ordering and references stay machine-readable: SLDD dictionary
trees, Live Script notebooks, figure object trees, test containers,
requirement sets and App Designer apps.
"""

from __future__ import annotations

import base64
import hashlib
import io
import re
import zipfile
from pathlib import Path
from typing import Any

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member

_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _scalar(text: str | None) -> str:
    return (text or "").strip()


def _xml_value(element) -> Any:
    """Convert one SLDD ``P`` payload into a scalar or a nested object."""
    children = [child for child in list(element) if child.tag in {"Element", "Object", "Cell"}]
    if not children:
        return _scalar(element.text)
    if len(children) == 1:
        return _xml_object(children[0])
    return {"items": [_xml_object(child) for child in children]}


def _xml_object(element) -> dict[str, Any]:
    """Recursively keep an SLDD object's class, fields and order."""
    node: dict[str, Any] = {"class": element.get("Class", element.tag)}
    dimension = element.get("Dimension")
    if dimension:
        node["dimension"] = dimension
    for prop in element.findall("./P"):
        name = prop.get("Name")
        if not name:
            continue
        value = _xml_value(prop)
        if prop.get("Dimension"):
            value = {"dimension": prop.get("Dimension"), "value": value}
        node[name] = value
    return node


def _metadata(archive: zipfile.ZipFile) -> dict[str, str]:
    meta: dict[str, str] = {}
    for name in ("metadata/mwcoreProperties.xml", "metadata/coreProperties.xml"):
        if name not in archive.namelist():
            continue
        try:
            root = ET.fromstring(read_xml_member(archive, name))
        except (ET.ParseError, ValueError):
            continue
        for element in root.iter():
            tag = element.tag.rsplit("}", 1)[-1]
            if tag in {"matlabRelease", "creator", "description", "created", "modified"}:
                text = _scalar(element.text)
                if text:
                    meta[tag] = text
    return meta


def parse_sldd_tree(path: str | Path) -> dict[str, Any]:
    """SLDD -> dictionary tree, preserving Bus/ConfigSet nesting and references."""
    path = Path(path)
    try:
        with zipfile.ZipFile(path) as archive:
            chunks = sorted(
                name
                for name in archive.namelist()
                if name.startswith("data/") and name.endswith(".xml")
            )
            roots = [ET.fromstring(read_xml_member(archive, name)) for name in chunks]
            metadata = _metadata(archive)
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid SLDD archive: {path.name}") from exc
    if not roots:
        raise ValueError(f"SLDD archive contains no data XML: {path.name}")

    entries: list[dict[str, Any]] = []
    references: list[str] = []
    for root in roots:
        for obj in root.findall("./Object"):
            obj_class = obj.get("Class", "")
            if obj_class == "DD.DICTIONARYREFERENCE":
                for prop in obj.findall("./P"):
                    if prop.get("Name") == "Subdictionary":
                        reference = _scalar(prop.text)
                        if reference and reference not in references:
                            references.append(reference)
                continue
            if obj_class != "DD.ENTRY":
                continue
            props = {p.get("Name"): p for p in obj.findall("./P") if p.get("Name")}
            entry: dict[str, Any] = {
                "name": _scalar(props["Name"].text) if "Name" in props else "未命名",
            }
            if "UUID" in props:
                entry["uuid"] = _scalar(props["UUID"].text)
            if "Namespace" in props:
                entry["namespace"] = _scalar(props["Namespace"].text)
            if "LastMod" in props:
                entry["last_modified"] = _scalar(props["LastMod"].text)
            if "IsDerived" in props:
                entry["derived"] = _scalar(props["IsDerived"].text) in {"1", "true"}
            value = props.get("Value")
            if value is not None:
                payload = [child for child in list(value) if child.tag in {"Element", "Object"}]
                entry["value"] = _xml_object(payload[0]) if payload else _scalar(value.text)
            entries.append(entry)

    counts: dict[str, int] = {}
    for entry in entries:
        value = entry.get("value")
        class_name = value.get("class", "未知") if isinstance(value, dict) else "未知"
        counts[class_name] = counts.get(class_name, 0) + 1
    return {
        "schema": "ov.matlab.sldd/1",
        "dictionary": path.stem,
        "release": metadata.get("matlabRelease", ""),
        "entries": entries,
        "entry_count": len(entries),
        "classes": counts,
        "references": references,
        "metadata": metadata,
    }


def _paragraph_text(paragraph) -> str:
    texts = [
        node.text or ""
        for run in paragraph.findall("./" + _W + "r")
        for node in run.iter(_W + "t")
    ]
    return "".join(texts)


def _paragraph_style(paragraph) -> str:
    style_node = paragraph.find("./" + _W + "pPr/" + _W + "pStyle")
    if style_node is None:
        style_node = paragraph.find(".//" + _W + "pStyle")
    return style_node.get(_W + "val", "text") if style_node is not None else "text"


def _mlx_cells(archive: zipfile.ZipFile) -> list[dict[str, Any]]:
    document = ET.fromstring(read_xml_member(archive, "matlab/document.xml"))
    cells: list[dict[str, Any]] = []
    for paragraph in document.iter(_W + "p"):
        text = _paragraph_text(paragraph)
        if not text.strip():
            continue
        style = _paragraph_style(paragraph)
        if style == "code":
            if cells and cells[-1]["type"] == "code":
                cells[-1]["source"] += "\n" + text
            else:
                cells.append({"type": "code", "source": text})
        elif style.startswith("heading"):
            try:
                level = min(6, max(2, int(style.removeprefix("heading") or 1) + 1))
            except ValueError:
                level = 2
            cells.append({"type": "heading", "level": level, "text": text})
        else:
            cells.append({"type": "text", "text": text})
    return cells


def _mlx_outputs(archive: zipfile.ZipFile) -> tuple[list[dict[str, Any]], dict[str, bytes]]:
    if "matlab/output.xml" not in archive.namelist():
        return [], {}
    root = ET.fromstring(read_xml_member(archive, "matlab/output.xml"))
    outputs: list[dict[str, Any]] = []
    files: dict[str, bytes] = {}
    image_index = 0
    for element in root.iter("element"):
        kind = (element.findtext("type") or "").strip()
        data = element.find("outputData")
        if data is None:
            continue
        if kind == "text":
            text = (data.findtext("text") or "").strip()
            if text:
                outputs.append({"type": "text", "text": text})
        elif kind == "figure":
            uri = (data.findtext("figureUri") or "").strip()
            match = re.match(r"data:image/([a-zA-Z0-9+.-]+);base64,(.+)", uri, re.DOTALL)
            if match:
                image_index += 1
                image_type = match.group(1).replace("jpeg", "jpg")
                name = f"outputs/figure_{image_index:03d}.{image_type}"
                files[name] = base64.b64decode(match.group(2))
                outputs.append({"type": "image", "path": name})
        else:
            text = " ".join(
                _scalar(node.text) for node in data.iter() if _scalar(node.text)
            )
            if text:
                outputs.append({"type": kind or "value", "text": text})
    return outputs, files


def parse_mlx_notebook(path: str | Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    """Live Script -> notebook JSON (cells + saved outputs), images as files."""
    path = Path(path)
    try:
        with zipfile.ZipFile(path) as archive:
            cells = _mlx_cells(archive)
            outputs, files = _mlx_outputs(archive)
            metadata = _metadata(archive)
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid MLX archive: {path.name}") from exc
    except KeyError as exc:
        raise ValueError(f"MLX archive has no matlab/document.xml: {path.name}") from exc
    return (
        {
            "schema": "ov.matlab.notebook/1",
            "name": path.stem,
            "release": metadata.get("matlabRelease", ""),
            "cells": cells,
            "cell_count": len(cells),
            "outputs": outputs,
            "output_assignment": "document-level; saved output index has no cell id",
            "metadata": metadata,
        },
        files,
    )


def _mat_scalar(value: Any) -> Any:
    import numpy as np

    if isinstance(value, np.void) and value.dtype.names:
        return {field: _mat_scalar(value[field]) for field in value.dtype.names}
    if isinstance(value, np.ndarray):
        if value.dtype.names:
            items = [_mat_object(item) for item in value.flat]
            return items[0] if len(items) == 1 else items
        if value.dtype == object:
            return [_mat_scalar(item) for item in value.flat]
        if value.ndim == 0:
            return _mat_scalar(value.item())
        if value.ndim <= 2 and value.size <= 20000:
            return value.tolist()
        return {
            "shape": list(value.shape),
            "dtype": str(value.dtype),
            "omitted_values": int(value.size),
        }
    if isinstance(value, (np.floating, np.integer, np.bool_)):
        return value.item()
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    return value


def _mat_object(value: Any) -> Any:
    fields = getattr(value, "_fieldnames", None)
    if fields:
        return {field: _mat_scalar(getattr(value, field)) for field in fields}
    return _mat_scalar(value)


def parse_fig_tree(path: str | Path) -> dict[str, Any]:
    """FIG -> JSON object tree from the MAT handle structure."""
    path = Path(path)
    try:
        from scipy.io import loadmat
    except ImportError as exc:
        raise RuntimeError(
            "FIG parsing requires scipy; install OpenViking with the 'matlab' extra"
        ) from exc
    values = loadmat(path, squeeze_me=False, struct_as_record=True)
    objects: dict[str, Any] = {}
    for name, value in values.items():
        if name.startswith("__"):
            continue
        objects[name] = _mat_object(value)
    return {
        "schema": "ov.matlab.figure/1",
        "figure": path.stem,
        "objects": objects,
        "boundary": "MAT handle tree; custom drawing callbacks and pixel rendering are not evaluated.",
    }


def _element_tree(element, depth: int = 0, max_depth: int = 40) -> dict[str, Any]:
    node: dict[str, Any] = {"tag": element.tag.rsplit("}", 1)[-1]}
    if element.attrib:
        node["attributes"] = dict(element.attrib)
    text = _scalar(element.text)
    if text:
        node["text"] = text
    if depth < max_depth:
        children = [_element_tree(child, depth + 1, max_depth) for child in list(element)]
        if children:
            node["children"] = children
    return node


def _xml_members(archive: zipfile.ZipFile) -> list[dict[str, Any]]:
    documents: list[dict[str, Any]] = []
    for name in sorted(archive.namelist()):
        if not name.lower().endswith((".xml", ".rels")) or name.endswith("/"):
            continue
        try:
            root = ET.fromstring(read_xml_member(archive, name))
        except (ET.ParseError, ValueError):
            continue
        documents.append({"member": name, "root": _element_tree(root)})
    return documents


def parse_mldatx(path: str | Path) -> dict[str, Any]:
    """Simulink Test container -> every member and all suite/result XML trees."""
    path = Path(path)
    if not zipfile.is_zipfile(path):
        return {
            "schema": "ov.matlab.mldatx/1",
            "file": path.name,
            "documents": [],
            "tests": [],
            "boundary": "Not a ZIP container; no test structure was readable.",
        }
    with zipfile.ZipFile(path) as archive:
        members = [
            {"name": info.filename, "bytes": info.file_size}
            for info in sorted(archive.infolist(), key=lambda item: item.filename)
            if not info.is_dir()
        ]
        documents = _xml_members(archive)
    tests: list[dict[str, Any]] = []
    for document in documents:
        stack = [document["root"]]
        while stack:
            node = stack.pop()
            tag = node["tag"].lower()
            if any(word in tag for word in ("suit", "case", "result", "test", "verdict", "outcome")):
                attributes = node.get("attributes", {})
                label = (
                    attributes.get("name")
                    or attributes.get("id")
                    or attributes.get("Name")
                    or node.get("text", "")
                )
                tests.append(
                    {
                        "tag": node["tag"],
                        "name": _scalar(label)[:300],
                        "attributes": attributes,
                        "text": node.get("text", "")[:2000],
                        "member": document["member"],
                    }
                )
            stack.extend(node.get("children", []))
    return {
        "schema": "ov.matlab.mldatx/1",
        "file": path.name,
        "members": members,
        "documents": documents,
        "tests": tests,
        "boundary": "Static test structure and results; tests are not executed.",
    }


def _node_text(node: dict[str, Any]) -> str:
    parts = [node.get("text", "")]
    for child in node.get("children", []):
        parts.append(_node_text(child))
    return " ".join(part for part in parts if part).strip()


def _requirement_nodes(documents: list[dict[str, Any]]) -> tuple[list, list]:
    requirements: list[dict[str, Any]] = []
    links: list[dict[str, Any]] = []
    for document in documents:
        stack = [document["root"]]
        while stack:
            node = stack.pop()
            tag = node["tag"].lower()
            attributes = node.get("attributes", {})
            text = _scalar(node.get("text", ""))
            if tag in {"requirements", "slreq.requirements"}:
                stack.extend(node.get("children", []))
                continue
            if "link" in tag or "trace" in tag:
                links.append(
                    {
                        "tag": node["tag"],
                        "attributes": attributes,
                        "text": text[:2000],
                        "member": document["member"],
                    }
                )
            elif "requirement" in tag or "justification" in tag:
                requirements.append(
                    {
                        "id": attributes.get("id") or attributes.get("ID") or attributes.get("sid"),
                        "tag": node["tag"],
                        "attributes": attributes,
                        "text": _node_text(node)[:4000],
                        "member": document["member"],
                    }
                )
            stack.extend(node.get("children", []))
    return requirements, links


def parse_requirement_set(path: str | Path) -> dict[str, Any]:
    """Requirement set or requirement link set -> JSON requirements and links."""
    path = Path(path)
    suffix = path.suffix.lower()
    if not zipfile.is_zipfile(path):
        documents = [
            {
                "member": path.name,
                "root": _element_tree(ET.fromstring(path.read_bytes())),
            }
        ]
        members: list[dict[str, Any]] = [{"name": path.name, "bytes": path.stat().st_size}]
    else:
        with zipfile.ZipFile(path) as archive:
            members = [
                {"name": info.filename, "bytes": info.file_size}
                for info in sorted(archive.infolist(), key=lambda item: item.filename)
                if not info.is_dir()
            ]
            documents = _xml_members(archive)
    requirements, links = _requirement_nodes(documents)
    return {
        "schema": "ov.matlab.requirements/1",
        "file": path.name,
        "kind": "requirement-links" if suffix == ".slmx" else "requirements",
        "members": members,
        "requirements": requirements,
        "links": links,
        "documents": documents,
        "boundary": "Static requirement text and links; implementation status is not judged.",
    }


def parse_mlapp(path: str | Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    """App Designer app -> classdef code plus the component tree when readable."""
    path = Path(path)
    files: dict[str, bytes] = {}
    code_cells: list[dict[str, Any]] = []
    components: Any = None
    component_status = "appdesigner/appModel.mat not present"
    if not zipfile.is_zipfile(path):
        return (
            {
                "schema": "ov.matlab.mlapp/1",
                "app": path.stem,
                "code": "",
                "cells": [],
                "components": None,
                "component_status": "Not a ZIP/OPC container",
            },
            files,
        )
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        if "matlab/document.xml" in names:
            code_cells = _mlx_cells(archive)
        if "appdesigner/appModel.mat" in names:
            try:
                from scipy.io import loadmat

                raw = read_xml_member(archive, "appdesigner/appModel.mat", max_bytes=64 * 1024 * 1024)
                values = loadmat(io.BytesIO(raw), squeeze_me=False, struct_as_record=True)
                components = {
                    name: _mat_object(value)
                    for name, value in values.items()
                    if not name.startswith("__")
                }
                component_status = "parsed"
            except Exception as exc:  # noqa: BLE001 - version dependent container
                component_status = f"unreadable: {type(exc).__name__}"
    code = "\n".join(
        cell["source"] for cell in code_cells if cell.get("type") == "code"
    )
    if code:
        files["code.m"] = code.encode("utf-8")
    return (
        {
            "schema": "ov.matlab.mlapp/1",
            "app": path.stem,
            "code": code,
            "cells": code_cells,
            "components": components,
            "component_status": component_status,
            "boundary": "Static classdef and component properties; the GUI is not rebuilt.",
        },
        files,
    )


def protected_metadata(path: str | Path, kind: str) -> dict[str, Any]:
    path = Path(path)
    raw = path.read_bytes()
    return {
        "schema": "ov.matlab.protected/1",
        "file": path.name,
        "format": kind,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "header_hex": raw[:32].hex(),
        "parse_status": "opaque",
        "original_preserved": True,
        "boundary": "Original bytes are kept; no decompilation or source recovery is attempted.",
    }
