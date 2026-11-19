# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read Simulink Requirements ``.slreqx`` and link ``.slmx`` containers."""

from __future__ import annotations

import html
import re
import zipfile
from pathlib import Path
from typing import Any

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _text(node, name: str) -> str:
    for child in list(node):
        if _local(child.tag) == name:
            return (child.text or "").strip()
    return ""


def _child(node, name: str):
    for child in list(node):
        if _local(child.tag) == name:
            return child
    return None


def _attr(node, name: str, default: str = "") -> str:
    return str(node.get(name, default)).strip()


def _plain(text: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return re.sub(r"\s+", " ", text).strip()


def _requirements(raw: bytes) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    root = ET.fromstring(raw)
    items = [
        item
        for item in root.iter()
        if _local(item.tag) == "items" and _attr(item, "type").endswith("MwRequirement")
    ]
    by_uuid: dict[str, str] = {}
    for item in items:
        uuid = _attr(item, "uuid")
        sid = _text(item, "sid")
        if uuid and sid:
            by_uuid[uuid] = sid

    requirements: list[dict[str, Any]] = []
    for item in items:
        sid = _text(item, "sid") or _attr(item, "uuid")
        description = _text(item, "description")
        parent = _child(item, "parent")
        parent_sid = None
        if parent is not None:
            parent_sid = by_uuid.get(_attr(parent, "uuid")) or _attr(parent, "uuid") or None
        requirements.append(
            {
                "id": sid,
                "title": _text(item, "summary"),
                "description": description,
                "description_text": _plain(description),
                "reason": _text(item, "rationale") or _text(item, "justification"),
                "status": _text(item, "status") or _text(item, "statusName") or None,
                "parent": parent_sid,
                "type": _text(item, "typeName"),
                "revision": _text(item, "revision"),
                "uuid": _attr(item, "uuid"),
                "created": _text(item, "createdOn"),
                "modified": _text(item, "modifiedOn"),
            }
        )
    return requirements, []


def _links(raw: bytes) -> list[dict[str, Any]]:
    root = ET.fromstring(raw)
    links: list[dict[str, Any]] = []
    for item in root.iter():
        if _local(item.tag) != "items":
            continue
        if not _attr(item, "type").endswith("LinkableItem"):
            continue
        element = _text(item, "id")
        for link in list(item):
            kind = _local(link.tag)
            if kind not in {"outgoingLinks", "incomingLinks"}:
                continue
            reference = _child(link, "dest" if kind == "outgoingLinks" else "source")
            if reference is None:
                continue
            requirement = _text(reference, "reqSetUri") or _text(reference, "artifactId")
            links.append(
                {
                    "requirement": requirement or None,
                    "element": element or None,
                    "block": element or None,
                    "type": _text(link, "typeName") or kind,
                    "description": _text(link, "comment") or "",
                    "artifact": _text(reference, "artifactUri") or None,
                    "domain": _text(reference, "domain") or None,
                    "linked_version": _text(reference, "linkedVersion") or None,
                    "link_id": _text(link, "sid") or _attr(link, "uuid") or None,
                    "direction": "outgoing" if kind == "outgoingLinks" else "incoming",
                }
            )
    return links


def parse_requirements_container(path: str | Path) -> dict[str, Any]:
    """Return normalized requirement/link rows from an SLREQX or SLMX file."""
    path = Path(path)
    with zipfile.ZipFile(path) as archive:
        members = [
            {"name": info.filename, "bytes": info.file_size}
            for info in sorted(archive.infolist(), key=lambda item: item.filename)
            if not info.is_dir()
        ]
        data_name = "slrequirements/data.xml"
        if data_name in archive.namelist():
            raw = read_xml_member(archive, data_name)
        else:
            candidates = [
                name
                for name in archive.namelist()
                if name.endswith(".xml") and not name.startswith("metadata/")
            ]
            if not candidates:
                raise ValueError(f"No requirement XML in {path.name}")
            raw = read_xml_member(archive, candidates[0])
    requirements, _ = _requirements(raw)
    links = _links(raw)
    return {
        "schema": "ov.matlab.requirements/1",
        "file": path.name,
        "members": members,
        "requirements": requirements,
        "links": links,
        "boundary": "Requirement text is preserved; implementation status is not judged.",
    }
