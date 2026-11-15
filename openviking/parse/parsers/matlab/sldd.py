# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Extract Simulink data dictionary entries from SLDD XML."""

from __future__ import annotations

import zipfile
from pathlib import Path

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member


def _props(element) -> dict[str, object]:
    return {p.get("Name"): p for p in element.findall("./P") if p.get("Name")}


def _value(element, depth: int = 0) -> str:
    if element is None:
        return ""
    children = list(element)
    if not children:
        return (element.text or "").strip()
    if depth >= 4:
        return f"<{len(children)} nested values>"
    parts = []
    for child in children:
        if child.tag == "P":
            parts.append(f"{child.get('Name', 'value')}={_value(child, depth + 1)}")
        elif child.tag in {"Element", "Object", "Cell"}:
            kind = child.get("Class", child.tag)
            parts.append(f"{kind}({_value(child, depth + 1)})")
    return "; ".join(parts)


def _dimension(element, props) -> str:
    dimensions = props.get("Dimensions")
    if dimensions is not None:
        text = (dimensions.text or "").strip()
        if text:
            values = []
            for value in text.split():
                try:
                    values.append(f"{float(value):g}")
                except ValueError:
                    values.append(value)
            return " × ".join(values)
        if dimensions.get("Dimension"):
            return dimensions.get("Dimension", "").replace("*", " × ")
    if element is not None and element.get("Dimension"):
        return element.get("Dimension", "").replace("*", " × ")
    return "未声明"


def _details(props) -> str:
    skip = {"Value", "Condition", "Dimensions", "DataType", "Description", "CoderInfo"}
    ignored = {"UUID", "Namespace", "LastMod", "LastModBy", "IsDerived"}
    parts = []
    for name, prop in props.items():
        if name in skip or name in ignored:
            continue
        text = _value(prop)
        if text:
            parts.append(f"{name}={text}")
    return "; ".join(parts)


def parse_sldd(path: str | Path) -> str:
    path = Path(path)
    try:
        with zipfile.ZipFile(path) as archive:
            chunks = sorted(
                n for n in archive.namelist() if n.startswith("data/") and n.endswith(".xml")
            )
            roots = [ET.fromstring(read_xml_member(archive, name)) for name in chunks]
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid SLDD archive: {path.name}") from exc
    if not roots:
        raise ValueError(f"SLDD archive contains no data XML: {path.name}")

    lines = [
        "---",
        "type: simulink-data-dictionary",
        "---",
        "",
        f"# {path.stem} 数据字典",
        "",
        "字段来自 SLDD 的 `data/*.xml`。未声明的维度或类型不会根据值猜测。",
        "",
        "| 名称 | 对象类型 | 维度 | 数据类型 | 值 / 条件 | 描述 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    references = []
    count = 0
    for root in roots:
        for obj in root.findall("./Object"):
            if obj.get("Class") == "DD.DICTIONARYREFERENCE":
                props = _props(obj)
                reference = _value(props.get("Subdictionary"))
                if reference:
                    references.append(reference)
                continue
            if obj.get("Class") != "DD.ENTRY":
                continue
            props = _props(obj)
            name = _value(props.get("Name")) or "未命名"
            value = props.get("Value")
            element = next(iter(value), None) if value is not None else None
            inner = _props(element) if element is not None else {}
            object_type = element.get("Class", "未知") if element is not None else "未知"
            data_type = (
                _value(inner.get("DataType"))
                or (
                    element.get("Class", "")
                    if element is not None and element.get("Class") == "char"
                    else ""
                )
                or "未声明"
            )
            dimension = _dimension(element, inner)
            description = _value(inner.get("Description")) or "-"
            extra = _details(inner)
            direct_value = _value(inner.get("Value")) or _value(inner.get("Condition"))
            if direct_value:
                rendered_value = direct_value
                if extra:
                    rendered_value += "; " + extra
            else:
                # _value(value) already includes every field in ``inner``. Adding
                # ``extra`` here duplicated large ConfigSet values almost twice.
                rendered_value = _value(value)
            cells = [name, object_type, dimension, data_type, rendered_value or "-", description]
            cells = [c.replace("|", "\\|").replace("\r", "").replace("\n", "<br>") for c in cells]
            lines.append("| " + " | ".join(cells) + " |")
            count += 1
    if not count:
        lines.append("| - | - | - | - | 未发现 DD.ENTRY | - |")
    lines.extend(["", "## 引用字典", ""])
    lines.extend(f"- `{reference}`" for reference in references)
    if not references:
        lines.append("无。")
    lines.extend(
        [
            "",
            f"共提取 **{count}** 个条目；复杂 ConfigSet 等嵌套值保留为文本，不展开成虚构的标量信号。",
            "",
        ]
    )
    return "\n".join(lines)
