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
import struct
import zipfile
from pathlib import Path
from typing import Any

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member
from openviking.parse.parsers.matlab.requirements import parse_requirements_container

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
            value = {
                "dimension": prop.get("Dimension"),
                "class": prop.get("Class", ""),
                "value": value,
            }
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
            if "LastModBy" in props:
                entry["last_modified_by"] = _scalar(props["LastModBy"].text)
            if "IsDerived" in props:
                entry["derived"] = _scalar(props["IsDerived"].text) in {"1", "true"}
            value = props.get("Value")
            if value is not None:
                # A plain numeric value stores its shape and class on the P itself.
                entry["value_dimension"] = value.get("Dimension") or ""
                entry["value_class"] = value.get("Class") or ""
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
    return "".join(node.text or "" for node in paragraph.iter(_W + "t"))


def _paragraph_style(paragraph) -> str:
    style_node = paragraph.find("./" + _W + "pPr/" + _W + "pStyle")
    if style_node is None:
        style_node = paragraph.find(".//" + _W + "pStyle")
    return style_node.get(_W + "val", "text") if style_node is not None else "text"


def _markdown_paragraph(paragraph, text: str) -> str:
    """Keep one Live Script paragraph as the Markdown a reader would expect."""
    style = _paragraph_style(paragraph)
    if style == "title":
        return f"# {text}"
    heading = re.fullmatch(r"heading([1-6])?", style)
    if heading:
        level = 2 if heading.group(1) is None else min(6, int(heading.group(1)) + 1)
        return f"{'#' * level} {text}"
    if style.lower().startswith("tocheading"):
        return f"## {text}"
    if paragraph.find("./" + _W + "pPr/" + _W + "numPr") is not None:
        return f"- {text}"
    return text


def _mlx_blocks(
    archive: zipfile.ZipFile,
) -> tuple[list[dict[str, Any]], dict[int, tuple[int, int]]]:
    """Document blocks in document order, with the code line range of each.

    Consecutive Markdown paragraphs stay in one block, so a heading and the text
    under it are not split. Code blocks record their cumulative code line range,
    which is what ``matlab/output.xml`` line numbers refer to.
    """
    document = ET.fromstring(read_xml_member(archive, "matlab/document.xml"))
    blocks: list[dict[str, Any]] = []
    code_ranges: dict[int, tuple[int, int]] = {}
    markdown: list[str] = []
    code_line = 0

    def flush_markdown() -> None:
        if markdown:
            blocks.append({"type": "markdown", "content": "\n\n".join(markdown)})
            markdown.clear()

    for paragraph in document.iter(_W + "p"):
        text = _paragraph_text(paragraph)
        style = _paragraph_style(paragraph)
        if style == "code":
            flush_markdown()
            lines = text.count("\n") + 1 if text else 0
            start = code_line + 1
            code_line += lines
            if not text:
                continue
            if blocks and blocks[-1]["type"] == "code":
                blocks[-1]["content"] += "\n" + text
                code_ranges[len(blocks) - 1] = (code_ranges[len(blocks) - 1][0], code_line)
            else:
                blocks.append({"type": "code", "content": text})
                code_ranges[len(blocks) - 1] = (start, code_line)
            continue
        if not text.strip():
            if paragraph.find("./" + _W + "pPr/" + _W + "sectPr") is not None:
                flush_markdown()
            continue
        markdown.append(_markdown_paragraph(paragraph, text.strip()))
    flush_markdown()
    return blocks, code_ranges


def _mlx_output_blocks(
    archive: zipfile.ZipFile,
) -> tuple[list[dict[str, Any]], dict[str, bytes], list[tuple[int, int]]]:
    """Saved outputs in document order, with the code lines they cover."""
    if "matlab/output.xml" not in archive.namelist():
        return [], {}, []
    root = ET.fromstring(read_xml_member(archive, "matlab/output.xml"))
    outputs: list[dict[str, Any]] = []
    spans: list[tuple[int, int]] = []
    files: dict[str, bytes] = {}
    image_index = 0
    for element in root.iter("element"):
        kind = (element.findtext("type") or "").strip()
        data = element.find("outputData")
        if data is None:
            continue
        block: dict[str, Any] | None = None
        if kind == "text":
            text = (data.findtext("text") or "").strip("\n")
            if text.strip():
                block = {"type": "output", "content": text, "media": "text"}
        elif kind == "figure":
            uri = (data.findtext("figureUri") or "").strip()
            match = re.match(r"data:image/([a-zA-Z0-9+.-]+);base64,(.+)", uri, re.DOTALL)
            if match:
                image_index += 1
                image_type = match.group(1).replace("jpeg", "jpg")
                name = f"outputs/figure_{image_index:03d}.{image_type}"
                files[name] = base64.b64decode(match.group(2))
                block = {"type": "output", "content": name, "media": "image"}
        else:
            text = " ".join(
                _scalar(node.text) for node in data.iter() if _scalar(node.text)
            )
            if text:
                block = {"type": "output", "content": text, "media": kind or "value"}
        if block is None:
            continue
        numbers = [
            int(item.text)
            for item in element.findall("lineNumbers/element")
            if (item.text or "").strip().isdigit()
        ]
        outputs.append(block)
        spans.append((min(numbers), max(numbers)) if numbers else (0, 0))
    return outputs, files, spans


def _mlx_attach_outputs(
    blocks: list[dict[str, Any]],
    code_ranges: dict[int, tuple[int, int]],
    outputs: list[dict[str, Any]],
    spans: list[tuple[int, int]],
) -> list[dict[str, Any]]:
    """Place each output right after the code block whose lines produced it."""
    by_block: dict[int, list[dict[str, Any]]] = {}
    trailing: list[dict[str, Any]] = []
    for output, span in zip(outputs, spans, strict=False):
        target: int | None = None
        for index, (start, end) in code_ranges.items():
            if start <= span[1] <= end:
                target = index
        if target is None:
            for index, (start, _) in code_ranges.items():
                if start <= span[1]:
                    target = index
        if target is None:
            trailing.append(output)
        else:
            by_block.setdefault(target, []).append(output)
    ordered: list[dict[str, Any]] = list(trailing)
    for index, block in enumerate(blocks):
        ordered.append(block)
        ordered.extend(by_block.get(index, []))
    return ordered


def parse_mlx_notebook(path: str | Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    """Live Script -> the document's own blocks: code, markdown and output.

    The three block types share the ``type`` and ``content`` fields, outputs sit
    right after the code block they belong to, and figures are saved next to the
    notebook and referenced from the block's content.
    """
    path = Path(path)
    try:
        with zipfile.ZipFile(path) as archive:
            blocks, code_ranges = _mlx_blocks(archive)
            outputs, files, spans = _mlx_output_blocks(archive)
            metadata = _metadata(archive)
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid MLX archive: {path.name}") from exc
    except KeyError as exc:
        raise ValueError(f"MLX archive has no matlab/document.xml: {path.name}") from exc
    blocks = _mlx_attach_outputs(blocks, code_ranges, outputs, spans)
    counts = {"code": 0, "markdown": 0, "output": 0}
    for block in blocks:
        counts[block["type"]] = counts.get(block["type"], 0) + 1
    return (
        {
            "schema": "ov.matlab.notebook/1",
            "file": path.name,
            "name": path.stem,
            "release": metadata.get("matlabRelease", ""),
            "blocks": blocks,
            "block_count": len(blocks),
            "counts": counts,
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


def _fig_type(value: Any) -> str:
    if isinstance(value, dict):
        raw = value.get("Type") or value.get("type")
    else:
        raw = getattr(value, "dtype", None)
        names = getattr(raw, "names", None)
        if names and "type" in names:
            raw = value["type"]
        else:
            raw = None
    try:
        import numpy as np

        while isinstance(raw, np.ndarray):
            raw = raw.ravel()[0] if raw.size else ""
        if isinstance(raw, (list, tuple)) and raw:
            raw = raw[0]
    except ImportError:
        pass
    return str(raw or "").strip()


def _fig_node(value: Any, depth: int = 0) -> dict[str, Any]:
    """Convert one MATLAB handle object into a compact parent/child tree."""
    if depth > 32:
        return {"type": "truncated"}
    if isinstance(value, dict):
        node_type = _fig_type(value)
        props = value.get("properties") or value.get("Properties") or {}
        children = value.get("children") or value.get("Children") or []
        handle = value.get("handle") or value.get("Handle")
        properties = _mat_object(props) if props else {}
        child_nodes = [_fig_node(item, depth + 1) for item in children] if isinstance(children, list) else []
        return {
            "type": node_type or "object",
            "handle": _mat_scalar(handle) if handle is not None else None,
            "properties": properties,
            "children": child_nodes,
        }
    import numpy as np

    if isinstance(value, np.void) and value.dtype.names:
        raw_type = _fig_type(value)
        raw_props = value["properties"] if "properties" in value.dtype.names else {}
        raw_children = value["children"] if "children" in value.dtype.names else []
        raw_handle = value["handle"] if "handle" in value.dtype.names else None
        return {
            "type": raw_type or "object",
            "handle": _mat_scalar(raw_handle) if raw_handle is not None else None,
            "properties": _mat_object(raw_props) if raw_props is not None else {},
            "children": [_fig_node(item, depth + 1) for item in raw_children.flat]
            if isinstance(raw_children, np.ndarray)
            else [],
        }
    if isinstance(value, np.ndarray):
        if value.dtype.names:
            nodes = [_fig_node(item, depth + 1) for item in value.flat]
            return nodes[0] if len(nodes) == 1 else {"type": "group", "children": nodes}
        if value.dtype == object:
            nodes = [_fig_node(item, depth + 1) for item in value.flat]
            return nodes[0] if len(nodes) == 1 else {"type": "group", "children": nodes}
        return {"type": "array", "value": _mat_scalar(value)}
    return {"type": type(value).__name__, "value": _mat_scalar(value)}


def parse_fig_tree(path: str | Path) -> dict[str, Any]:
    """FIG -> a compact Figure/Axes/Line/Text object tree from the MAT handle data."""
    path = Path(path)
    try:
        from scipy.io import loadmat
    except ImportError as exc:
        raise RuntimeError(
            "FIG parsing requires scipy; install OpenViking with the 'matlab' extra"
        ) from exc
    values = loadmat(path, squeeze_me=False, struct_as_record=True)
    objects: dict[str, Any] = {}
    roots: list[dict[str, Any]] = []
    for name, value in values.items():
        if name.startswith("__"):
            continue
        objects[name] = _mat_object(value)
        node = _fig_node(value)
        if node.get("type") == "figure":
            roots.append(node)
        elif node.get("children"):
            roots.extend(
                child for child in node["children"] if child.get("type") == "figure"
            )
    if not roots and objects:
        roots = [_fig_node(next(iter(objects.values())))]

    def count(nodes: list[dict[str, Any]]) -> dict[str, int]:
        counts: dict[str, int] = {}
        stack = list(nodes)
        while stack:
            node = stack.pop()
            kind = node.get("type", "object")
            counts[kind] = counts.get(kind, 0) + 1
            stack.extend(node.get("children", []))
        return counts

    return {
        "schema": "ov.matlab.figure/1",
        "figure": path.stem,
        "tree": roots[0] if roots else None,
        "object_counts": count(roots),
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


def _local_tag(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _xml_dict(element) -> dict[str, Any]:
    node: dict[str, Any] = {}
    if element.attrib:
        node["attributes"] = dict(element.attrib)
    text = _scalar(element.text)
    if text:
        node["text"] = text
    for child in list(element):
        key = _local_tag(child.tag)
        value = _xml_dict(child)
        if key in node:
            if not isinstance(node[key], list):
                node[key] = [node[key]]
            node[key].append(value)
        else:
            node[key] = value
    return node


def _find_first(node: Any, name: str) -> Any:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == name:
                return value
            found = _find_first(value, name)
            if found is not None:
                return found
    elif isinstance(node, list):
        for item in node:
            found = _find_first(item, name)
            if found is not None:
                return found
    return None


def _flat_values(node: Any, names: set[str]) -> list[Any]:
    found: list[Any] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key in names:
                found.append(value)
            found.extend(_flat_values(value, names))
    elif isinstance(node, list):
        for item in node:
            found.extend(_flat_values(item, names))
    return found


def parse_mldatx(path: str | Path) -> dict[str, Any]:
    """Simulink Test container -> suites, cases, inputs, criteria and results."""
    path = Path(path)
    if not zipfile.is_zipfile(path):
        return {
            "schema": "ov.matlab.mldatx/1",
            "file": path.name,
            "members": [],
            "suites": [],
            "tests": [],
            "boundary": "Not a ZIP container; no test structure was readable.",
        }
    with zipfile.ZipFile(path) as archive:
        members = [
            {"name": info.filename, "bytes": info.file_size}
            for info in sorted(archive.infolist(), key=lambda item: item.filename)
            if not info.is_dir()
        ]
        raw_xml: dict[str, bytes] = {}
        for name in archive.namelist():
            if name.endswith(".xml") and not name.startswith("metadata/"):
                raw_xml[name] = read_xml_member(archive, name)

    suites_by_path: dict[str, dict[str, Any]] = {}
    case_documents: list[tuple[str, dict[str, Any], str]] = []
    generic_tests: list[dict[str, Any]] = []
    for member, raw in sorted(raw_xml.items()):
        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            continue
        document = _xml_dict(root)
        root_tag = _local_tag(root.tag)
        if root_tag == "TestSuiteDefinition":
            model = document.get("model", {})
            if isinstance(model, list):
                model = model[0] if model else {}
            suite_path = str(Path(member).parent)
            suites_by_path[suite_path] = {
                "name": (model.get("Name") or {}).get("text", ""),
                "uuid": (model.get("UUID") or {}).get("text", ""),
                "description": (model.get("Description") or {}).get("text", ""),
                "enabled": (model.get("Enabled") or {}).get("text", ""),
                "location": (model.get("Location") or {}).get("text", ""),
                "member": member,
                "parent": None,
                "cases": [],
            }
        elif root_tag == "TestCaseDefinition":
            case_documents.append((str(Path(member).parent), document, member))
        # Keep a compact flat index for callers that only scan tags.
        stack = [root]
        while stack:
            element = stack.pop()
            tag = _local_tag(element.tag)
            if "suit" in tag.lower() or "case" in tag.lower() or "result" in tag.lower():
                attributes = dict(element.attrib)
                label = attributes.get("name") or attributes.get("Name") or _scalar(element.text)
                generic_tests.append(
                    {
                        "tag": tag,
                        "name": _scalar(label)[:300],
                        "attributes": attributes,
                        "text": _scalar(element.text)[:2000],
                        "member": member,
                    }
                )
            stack.extend(list(element))

    for suite_path, suite in suites_by_path.items():
        parent = None
        for candidate in suites_by_path:
            if candidate != suite_path and suite_path.startswith(candidate + "/"):
                if parent is None or len(candidate) > len(parent):
                    parent = candidate
        suite["parent"] = suites_by_path[parent]["name"] if parent else None

    for suite_path, document, member in case_documents:
        model = document.get("model", {})
        if isinstance(model, list):
            model = model[0] if model else {}
        permutation = _find_first(document, "TestCasePermutationDefinition") or {}
        criteria = document.get("Criteria") or {}
        results = _flat_values(document, {"Result", "ResultStatus", "Verdict", "Outcome"})
        statuses = [
            item.get("text") if isinstance(item, dict) else _scalar(str(item))
            for item in results
        ]
        case = {
            "name": (model.get("Name") or {}).get("text", ""),
            "hierarchy": (model.get("Hiearchy") or {}).get("text", ""),
            "description": (model.get("Description") or {}).get("text", ""),
            "enabled": (model.get("Enabled") or {}).get("text", ""),
            "uuid": (model.get("UUID") or {}).get("text", ""),
            "type": (model.get("TestCaseType") or {}).get("text", ""),
            "member": member,
            "inputs": permutation,
            "criteria": criteria,
            "results": statuses,
            "definition": document,
        }
        suite = suites_by_path.get(suite_path)
        if suite is None:
            suite = {
                "name": suite_path.split("/")[-1] if suite_path else "tests",
                "uuid": "",
                "description": "",
                "enabled": "",
                "location": "",
                "member": f"{suite_path}/TestSuiteInfo.xml",
                "parent": None,
                "cases": [],
            }
            suites_by_path[suite_path] = suite
        suite["cases"].append(case)

    suites = list(suites_by_path.values())
    return {
        "schema": "ov.matlab.mldatx/1",
        "file": path.name,
        "members": members,
        "suites": suites,
        "tests": generic_tests,
        "coverage": {
            "suites": len(suites),
            "cases": sum(len(suite["cases"]) for suite in suites),
        },
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
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as archive:
            if "slrequirements/data.xml" in archive.namelist():
                return parse_requirements_container(path)
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
            code_cells = [block for block in _mlx_blocks(archive)[0] if block["type"] == "code"]
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
    code = "\n".join(cell["content"] for cell in code_cells)
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
    metadata: dict[str, Any] = {
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
    if raw.startswith(b"PK") and zipfile.is_zipfile(path):
        metadata["container"] = "zip"
        try:
            with zipfile.ZipFile(path) as archive:
                metadata["members"] = [
                    {"name": info.filename, "bytes": info.file_size}
                    for info in sorted(archive.infolist(), key=lambda item: item.filename)
                    if not info.is_dir()
                ]
        except (zipfile.BadZipFile, OSError):
            metadata["members"] = []
    header = raw[:16].decode("latin-1", errors="replace")
    version = next(
        (part for part in ("v01.00", "v00.00", "R20", "R201") if part in header),
        "",
    )
    if version:
        metadata["version_hint"] = version
    if raw[:4] == b"v01." or raw[:1] == b"v":
        metadata["version_hint"] = raw[:8].decode("latin-1", errors="replace")
    return metadata


_NUMBER = re.compile(
    r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?|[-+]?(?:NaN|Inf|nan|inf)"
)
_SLDD_PROPERTY_MAP = {
    "Name": "name",
    "Class": "class",
    "DataType": "dtype",
    "DataType_internal": "dtype",
    "Dimensions": "dimensions",
    "Complexity": "complexity",
    "Min": "min",
    "Min_internal": "min",
    "Max": "max",
    "Max_internal": "max",
    "DocUnits": "unit",
    "Units": "unit",
    "Unit": "unit",
    "Argument": "argument",
    "Description": "description",
    "Condition": "condition",
    "SampleTime": "sample_time",
    "DimensionsMode": "dimensions_mode",
    "SamplingMode": "sampling_mode",
    "DataScope": "data_scope",
    "HeaderFile": "header_file",
    "Alignment": "alignment",
    "PreserveElementDimensions": "preserve_element_dimensions",
    "InitialValue": "initial_value",
    "DefaultValue": "default_value",
    "StorageType": "storage_type",
    "AddClassNameToEnumNames": "add_class_name_to_enum_names",
}


def _snake(name: str) -> str:
    text = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name)
    text = re.sub(r"[^0-9A-Za-z_]+", "_", text)
    return text.strip("_").lower() or "field"


def _array_stem(name: str) -> str:
    return re.sub(r"[^\w.-]+", "_", name, flags=re.UNICODE).strip("._") or "entry"


def _dimension_list(value: Any) -> Any:
    """Normalize SLDD dimensions to a compact list of integers."""
    if isinstance(value, list):
        try:
            return [int(item) for item in value]
        except (TypeError, ValueError):
            return None
    if isinstance(value, (int, float)):
        return [int(value)]
    if isinstance(value, dict):
        # ``Dimensions`` carries the real shape in value; ``Elements_internal``
        # uses the dimension attribute only as a container shape.
        raw = value.get("value") if value.get("value") not in (None, "") else value.get("dimension")
        value = raw
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        parts = [part for part in re.split(r"[*,\s]+", text) if part]
        try:
            return [int(float(part)) for part in parts]
        except ValueError:
            return None
    return None


def _number_tokens(text: str) -> list[str] | None:
    parts = [part for part in re.split(r"[\s,;]+", text.strip()) if part]
    if not parts or any(_NUMBER.fullmatch(part) is None for part in parts):
        return None
    return parts


def _array_payload(raw: Any, dimensions: Any, dtype: str = "") -> list[str] | None:
    """Numeric tokens when one value is an array that belongs in its own .npy.

    Only a 1x1 value stays inline in ``entries.jsonl``; every other array is
    externalized, whatever its size, so the JSONL line never carries numbers.
    """
    if isinstance(raw, list):
        if not raw or not all(isinstance(item, (int, float)) for item in raw):
            return None
        tokens = [repr(item) for item in raw]
    elif isinstance(raw, str):
        tokens = _number_tokens(raw)
    else:
        return None
    if not tokens or not dimensions:
        return None
    product = 1
    for dimension in dimensions:
        product *= dimension
    if product != len(tokens):
        return None
    if product == 1:
        return None
    return tokens


def _npy_bytes(tokens: list[str], dimensions: list[int]) -> bytes:
    """Serialize numeric tokens as a Fortran-order float64 .npy file.

    Values are stored column-major, the order MATLAB keeps them in, so the file
    reads back as the exact original array. The writer is pure Python: a
    dictionary keeps its numbers readable without numpy being installed.
    """
    shape = tuple(int(part) for part in dimensions)
    header = (
        "{'descr': '<f8', 'fortran_order': True, 'shape': %s, }"
        % (shape,)
    )
    padding = 16 - (10 + len(header) + 1) % 16
    header = header + " " * padding + "\n"
    body = b"".join(struct.pack("<d", _token_float(token)) for token in tokens)
    return b"\x93NUMPY\x01\x00" + struct.pack("<H", len(header)) + header.encode("latin-1") + body


def _token_float(token: str) -> float:
    text = token.strip()
    if text.lower() in {"nan", "+nan", "-nan"}:
        return float("nan")
    return float(text)


class _SlddArrayWriter:
    """Collects the .npy files referenced by the entry rows of one dictionary."""

    def __init__(self) -> None:
        self.files: dict[str, bytes] = {}
        self.pointers: dict[str, dict[str, Any]] = {}

    def add(self, stem: str, tokens: list[str], dimensions: list[int]) -> str:
        name = f"{_array_stem(stem)}.npy"
        base = name[: -len(".npy")]
        counter = 1
        while name in self.files:
            counter += 1
            name = f"{base}_{counter}.npy"
        self.files[name] = _npy_bytes(tokens, dimensions)
        self.pointers[name] = {"format": "npy", "dtype": "double"}
        return name

    def pointer(self, name: str) -> dict[str, Any]:
        return dict(self.pointers.get(name, {}))


def _unwrap(value: Any) -> Any:
    if isinstance(value, dict) and "value" in value and set(value) <= {
        "dimension",
        "class",
        "value",
        "data",
    }:
        return value["value"]
    return value


def _clean(value: Any) -> Any:
    value = _unwrap(value)
    if isinstance(value, str):
        return value if value.strip() else None
    return value


def _inline_value(value: Any) -> Any:
    """Inline value for scalars and small one-dimensional arrays."""
    value = _unwrap(value)
    if isinstance(value, str):
        tokens = _number_tokens(value)
        if tokens and len(tokens) > 1:
            return [float(token) for token in tokens]
        return value.strip() or None
    return value


def _rewrite_arrays(
    node: Any, collector: _SlddArrayWriter, path: str, root: bool = False
) -> Any:
    """Replace every numeric array inside a value tree with a .npy pointer.

    ``root`` marks the entry's own value object, whose ``Value`` property names
    the data file after the entry instead of after ``<entry>.Value``.
    """
    if isinstance(node, dict):
        dimensions = node.get("dimension")
        if dimensions is not None and "value" in node and not isinstance(node["value"], dict):
            dims = _dimension_list(dimensions)
            tokens = _array_payload(node["value"], dims, str(node.get("class") or ""))
            if tokens is not None and dims is not None:
                pointer = {key: item for key, item in node.items() if key != "value"}
                pointer["data"] = collector.add(path or "value", tokens, dims)
                pointer.update(collector.pointer(pointer["data"]))
                return pointer
        return {
            key: (
                item
                # ``class`` is a tag and ``Dimensions`` describes the entry's
                # shape (``value`` there is the dimension list, not the array),
                # so neither is data that belongs in a file.
                if key in {"class", "Dimensions"}
                else _rewrite_arrays(
                    item,
                    collector,
                    path if root and key == "Value" else (f"{path}.{key}" if path else key),
                )
            )
            for key, item in node.items()
        }
    if isinstance(node, list):
        return [
            _rewrite_arrays(item, collector, f"{path}[{index}]" if path else f"[{index}]")
            for index, item in enumerate(node)
        ]
    return node


def _property_row(properties: dict[str, Any], skip: set[str]) -> dict[str, Any]:
    """Flatten one SLDD object's properties, keeping every field it carries."""
    row: dict[str, Any] = {}
    for name, prop in properties.items():
        if name in skip:
            continue
        key = _SLDD_PROPERTY_MAP.get(name) or _snake(name)
        if key in row:
            continue
        if name == "Dimensions":
            row[key] = _dimension_list(prop)
            continue
        if name in ("Elements_internal", "Elements"):
            row["elements"] = _bus_element_rows(prop)
            continue
        if name == "Components":
            components = _container_items(prop)
            if components:
                row["components"] = [
                    item.get("class", "") for item in components if item.get("class")
                ]
            continue
        if name == "Enumerals":
            enumerals = _container_items(prop)
            if enumerals:
                row["enumerals"] = [
                    {
                        "name": _clean(item.get("Name")),
                        "value": _clean(item.get("Value")),
                        "description": _clean(item.get("Description")),
                    }
                    for item in enumerals
                ]
            continue
        if name == "CoderInfo":
            if isinstance(prop, dict):
                storage = _clean(prop.get("StorageClass"))
                if storage:
                    row["storage"] = storage
                row["coder_info"] = {
                    _snake(item): _clean(value)
                    for item, value in prop.items()
                    if item not in {"class", "dimension"}
                }
            continue
        row[key] = _clean(prop)
    return row


def _bus_element_rows(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        raw = value.get("Elements_internal") or value.get("Elements") or value
    else:
        raw = value
    elements = []
    for item in _container_items(raw):
        row = {
            "name": item.get("Name", ""),
            "class": item.get("class", ""),
        }
        row.update(
            _property_row(
                item,
                {
                    "Name",
                    "class",
                    "dimension",
                    "Elements_internal",
                    "Elements",
                    "Components",
                    "CoderInfo",
                },
            )
        )
        elements.append(row)
    return elements


def _container_items(value: Any) -> list[dict[str, Any]]:
    value = _unwrap(value)
    if isinstance(value, dict):
        value = value.get("items", value)
    if isinstance(value, dict):
        value = [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    return []


def sldd_entry_documents(
    tree: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, bytes]]:
    """One row per dictionary entry, plus the .npy files its arrays need."""
    collector = _SlddArrayWriter()
    rows: list[dict[str, Any]] = []
    for index, entry in enumerate(tree.get("entries", []), 1):
        stem = f"{index:04d}_{_array_stem(entry.get('name', ''))}"
        row: dict[str, Any] = {
            "name": entry.get("name", ""),
            "class": "",
            "status": None,
            "complexity": None,
            "min": None,
            "max": None,
            "dtype": None,
            "dimensions": None,
            "unit": None,
            "argument": None,
            "storage": None,
            "data_source": None,
            "description": None,
            "last_modified": entry.get("last_modified") or None,
            "last_modified_by": entry.get("last_modified_by") or None,
            "uuid": entry.get("uuid") or None,
            "namespace": entry.get("namespace") or None,
            "is_derived": entry.get("derived"),
        }
        value = entry.get("value")
        if isinstance(value, dict) and isinstance(value.get("class"), str) and value[
            "class"
        ].startswith("Simulink"):
            row["class"] = value["class"]
            rewritten = _rewrite_arrays(value, collector, stem, root=True)
            row.update(
                _property_row(
                    rewritten,
                    {"Name", "class", "dimension", "Value", "Dimensions"},
                )
            )
            row["dimensions"] = _dimension_list(rewritten.get("Dimensions"))
            nested = rewritten.get("Value")
            if isinstance(nested, dict) and "data" in nested:
                row["data"] = nested["data"]
                row.update(collector.pointer(row["data"]))
                dimensions = _dimension_list(nested.get("dimension"))
                if dimensions is not None:
                    row["dimensions"] = dimensions
                if row["dtype"] is None:
                    row["dtype"] = _clean(nested.get("class")) or None
            elif "Value" in rewritten:
                row["value"] = _inline_value(nested)
        elif isinstance(value, dict):
            row["class"] = value["class"] if isinstance(value.get("class"), str) else ""
            row["value"] = _rewrite_arrays(value, collector, stem)
        else:
            dimensions = _dimension_list(entry.get("value_dimension")) or [1, 1]
            dtype = entry.get("value_class") or ""
            tokens = _array_payload(value, dimensions, dtype) if isinstance(value, str) else None
            row["dimensions"] = dimensions
            if dtype:
                row["dtype"] = dtype
            if tokens is not None:
                row["data"] = collector.add(stem, tokens, dimensions)
                row.update(collector.pointer(row["data"]))
            elif value is not None:
                row["value"] = _inline_value(value)
        rows.append(row)
    return rows, collector.files


def sldd_entry_rows(tree: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten dictionary entries into the plan's one-object-per-line shape."""
    return sldd_entry_documents(tree)[0]


def requirement_rows(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Map requirement/link nodes to the plan's JSONL fields."""
    requirements = []
    for item in payload.get("requirements", []):
        if "id" in item and "title" in item:
            requirements.append(item)
            continue
        attributes = item.get("attributes", {})
        text = str(item.get("text", ""))
        title = (
            attributes.get("title")
            or attributes.get("name")
            or attributes.get("summary")
            or (text.splitlines()[0][:300] if text else "")
        )
        requirements.append(
            {
                "id": item.get("id") or attributes.get("id") or attributes.get("ID"),
                "title": title,
                "description": text,
                "status": attributes.get("status"),
                "parent": attributes.get("parent") or attributes.get("parentId"),
            }
        )
    links = []
    for item in payload.get("links", []):
        if "requirement" in item:
            links.append(item)
            continue
        attributes = item.get("attributes", {})
        links.append(
            {
                "requirement": attributes.get("requirement")
                or attributes.get("source")
                or attributes.get("id"),
                "element": attributes.get("element")
                or attributes.get("target")
                or attributes.get("sid"),
                "block": attributes.get("block") or attributes.get("blockPath"),
                "type": attributes.get("type") or item.get("tag"),
                "description": item.get("text", ""),
            }
        )
    return requirements, links
