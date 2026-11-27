# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read .xlsx workbooks into sheet cells, formulas and merged ranges.

A spreadsheet in a MATLAB project is data, not a picture of data: calibration
tables, lookup-table breakpoints, test vectors. The bytes alone cannot be
searched, so every sheet is read cell by cell — values, formulas, dates and
merged ranges — and written as one JSON document plus a readable table page.

Only the file format is implemented here (spreadsheetml in a ZIP); nothing is
executed and no external converter is needed. Sheets are capped so a runaway
table cannot fill the artifact, and the payload says when that happened.
"""

from __future__ import annotations

import datetime
import re
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from defusedxml import ElementTree as ET

WORKBOOK_SCHEMA = "ov.matlab.workbook/1"

# One worksheet XML larger than this is not parsed: the whole document would have
# to be held in memory, and a table that size is not a calibration sheet.
MAX_SHEET_XML_BYTES = 64 * 1024 * 1024

# Caps keep one huge table from dominating the artifact; every cut is reported.
MAX_SHEET_ROWS = 2000
MAX_SHEET_COLUMNS = 256
MAX_WORKBOOK_CELLS = 40000
MAX_CELL_TEXT = 2000
TABLE_PAGE_ROWS = 25
TABLE_PAGE_COLUMNS = 16

_RELATIONSHIP_ID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
_SHEET_TARGET_TYPE = "/worksheet"
_BUILTIN_DATE_FORMATS = frozenset(
    {
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        45,
        46,
        47,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
    }
)
_DATE_TOKENS = re.compile(r"[ymdhs]", re.I)
_QUOTED = re.compile(r'"[^"]*"|\[[^\]]*\]|\\.', re.S)
_CELL_REF = re.compile(r"^([A-Za-z]+)([0-9]+)$")
_INTEGER_TEXT = re.compile(r"^[+-]?[0-9]+$")
_LEAP_DAY = 60  # 1900-02-29, kept by Excel but absent from every real calendar
_EXCEL_EPOCH = datetime.date(1899, 12, 30)
_EXCEL_EPOCH_1904 = datetime.date(1904, 1, 1)


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _read(archive: zipfile.ZipFile, name: str) -> Optional[Any]:
    try:
        with archive.open(name) as stream:
            return ET.fromstring(stream.read())
    except (KeyError, ET.ParseError, ValueError, OSError):
        return None


def _children(element, name: str) -> List[Any]:
    return [child for child in list(element) if _local(child.tag) == name]


def _text_of(element) -> str:
    """Every ``<t>`` under a shared or inline string, in document order."""
    parts: List[str] = []
    for child in element.iter():
        if _local(child.tag) in {"t", "v"} and child.text:
            parts.append(child.text)
    return "".join(parts)


def _column_index(letters: str) -> int:
    index = 0
    for letter in letters.upper():
        index = index * 26 + (ord(letter) - 64)
    return index


def _column_letters(index: int) -> str:
    letters = ""
    while index > 0:
        index, remainder = divmod(index - 1, 26)
        letters = chr(65 + remainder) + letters
    return letters


def _cell_position(ref: str) -> Optional[Tuple[int, int]]:
    match = _CELL_REF.match(ref or "")
    if match is None:
        return None
    return int(match.group(2)), _column_index(match.group(1))


def _is_date_format(format_code: str) -> bool:
    stripped = _QUOTED.sub("", format_code or "")
    section = stripped.split(";")[0]
    return bool(_DATE_TOKENS.search(section))


def _date_styles(root) -> set:
    """Cell style indexes whose number format is a date or time."""
    if root is None:
        return set()
    custom = {
        int(element.get("numFmtId", "0")): element.get("formatCode", "")
        for element in root.iter()
        if _local(element.tag) == "numFmt"
    }
    styles: set = set()
    cell_xfs = next((element for element in root.iter() if _local(element.tag) == "cellXfs"), None)
    if cell_xfs is None:
        return styles
    for index, xf in enumerate(_children(cell_xfs, "xf")):
        try:
            num_fmt_id = int(xf.get("numFmtId", "0"))
        except ValueError:
            continue
        if num_fmt_id in _BUILTIN_DATE_FORMATS:
            styles.add(index)
        elif num_fmt_id in custom and _is_date_format(custom[num_fmt_id]):
            styles.add(index)
    return styles


def _iso_date(value: float, *, date1904: bool) -> str:
    """Excel serial number → ISO date, or datetime when it carries a time."""
    days, fraction = divmod(float(value), 1)
    whole = int(days)
    epoch = _EXCEL_EPOCH_1904 if date1904 else _EXCEL_EPOCH
    if not date1904 and whole == _LEAP_DAY:
        day = datetime.date(1900, 2, 28)
    elif not date1904 and whole < _LEAP_DAY:
        # Serial 1 is 1900-01-01, before Excel's phantom leap day shifts the epoch.
        day = epoch + datetime.timedelta(days=whole + 1)
    else:
        day = epoch + datetime.timedelta(days=whole)
    try:
        if fraction:
            seconds = int(round(fraction * 86400))
            moment = datetime.datetime.combine(day, datetime.time()) + datetime.timedelta(
                seconds=seconds
            )
            return moment.isoformat(sep=" ")
    except (OverflowError, ValueError):
        return str(value)
    return day.isoformat()


def _number(text: str, *, as_date: bool, date1904: bool) -> Any:
    if as_date:
        try:
            return _iso_date(float(text), date1904=date1904)
        except (TypeError, ValueError):
            return text
    if _INTEGER_TEXT.match(text):
        # An integer longer than a float can carry (an identifier, a timestamp in
        # nanoseconds) would lose digits as a number, so it stays text.
        if len(text.lstrip("+-").lstrip("0")) > 15:
            return text
        try:
            return int(text)
        except ValueError:
            return text
    try:
        return float(text)
    except ValueError:
        return text


def _cell_value(
    cell,
    shared: List[str],
    date_styles: set,
    *,
    date1904: bool,
) -> Tuple[Any, str]:
    """Value and formula text of one ``<c>`` element."""
    kind = cell.get("t", "")
    style = int(cell.get("s", "0") or 0)
    formula = ""
    for element in list(cell):
        if _local(element.tag) == "f" and (element.text or "").strip():
            formula = "=" + (element.text or "").strip()
    value_element = next((child for child in list(cell) if _local(child.tag) == "v"), None)
    raw = value_element.text if value_element is not None and value_element.text is not None else ""
    if kind == "s":
        try:
            text = shared[int(raw)]
        except (ValueError, IndexError):
            text = raw
        return text, formula
    if kind == "inlineStr":
        inline = next((child for child in list(cell) if _local(child.tag) == "is"), None)
        return (_text_of(inline) if inline is not None else raw), formula
    if kind == "b":
        return raw == "1", formula
    if kind in {"str", "e"}:
        return raw, formula
    if kind == "d":
        return raw, formula
    if raw == "":
        return None, formula
    return _number(raw, as_date=style in date_styles, date1904=date1904), formula


def _sheet_targets(archive: zipfile.ZipFile) -> Dict[str, str]:
    root = _read(archive, "xl/_rels/workbook.xml.rels")
    targets: Dict[str, str] = {}
    if root is None:
        return targets
    for element in root.iter():
        if _local(element.tag) != "Relationship":
            continue
        target = (element.get("Target") or "").lstrip("/")
        if not target:
            continue
        if not target.startswith("xl/"):
            target = f"xl/{target}"
        targets[element.get("Id", "")] = target.replace("/./", "/")
    return targets


def _sheet_names(archive: zipfile.ZipFile) -> List[Dict[str, Any]]:
    root = _read(archive, "xl/workbook.xml")
    if root is None:
        return []
    targets = _sheet_targets(archive)
    sheets: List[Dict[str, Any]] = []
    for element in root.iter():
        if _local(element.tag) != "sheet":
            continue
        sheets.append(
            {
                "name": element.get("name", ""),
                "state": element.get("state", "visible"),
                "target": targets.get(element.get(_RELATIONSHIP_ID, ""), ""),
            }
        )
    return sheets


def _shared_strings(archive: zipfile.ZipFile) -> List[str]:
    root = _read(archive, "xl/sharedStrings.xml")
    if root is None:
        return []
    return [_text_of(element) for element in root.iter() if _local(element.tag) == "si"]


def _sheet_payload(
    root,
    *,
    shared: List[str],
    date_styles: set,
    date1904: bool,
    budget: int,
) -> Dict[str, Any]:
    """Cells, formulas and merged ranges of one worksheet."""
    dimension = ""
    for element in root.iter():
        if _local(element.tag) == "dimension":
            dimension = element.get("ref", "")
            break
    merged = [
        element.get("ref", "")
        for element in root.iter()
        if _local(element.tag) == "mergeCell" and element.get("ref")
    ]
    cells: Dict[Tuple[int, int], Any] = {}
    formulas: Dict[str, str] = {}
    truncated = False
    for row in root.iter():
        if _local(row.tag) != "row":
            continue
        for cell in _children(row, "c"):
            position = _cell_position(cell.get("r", ""))
            if position is None:
                continue
            row_index, column_index = position
            if row_index > MAX_SHEET_ROWS or column_index > MAX_SHEET_COLUMNS:
                truncated = True
                continue
            if len(cells) >= budget:
                truncated = True
                break
            value, formula = _cell_value(cell, shared, date_styles, date1904=date1904)
            if isinstance(value, str) and len(value) > MAX_CELL_TEXT:
                value = value[:MAX_CELL_TEXT]
            cells[position] = value
            if formula:
                formulas[f"{_column_letters(column_index)}{row_index}"] = formula
        if len(cells) >= budget:
            break
    rows = max((position[0] for position in cells), default=0)
    columns = max((position[1] for position in cells), default=0)
    grid: List[List[Any]] = []
    for row_index in range(1, rows + 1):
        grid.append(
            [cells.get((row_index, column_index)) for column_index in range(1, columns + 1)]
        )
    header: List[Any] = []
    for line in grid:
        if any(item not in (None, "") for item in line):
            header = list(line)
            break
    return {
        "rows": rows,
        "columns": columns,
        "range": dimension or (f"A1:{_column_letters(columns)}{rows}" if rows and columns else ""),
        "truncated": truncated,
        "header": header,
        "cells": grid,
        "formulas": formulas,
        "merged": merged,
        "cell_count": len(cells),
    }


def parse_workbook(path: str | Path) -> Dict[str, Any]:
    """Read every sheet of an .xlsx workbook; never raises for a bad file."""
    path = Path(path)
    payload: Dict[str, Any] = {
        "schema": WORKBOOK_SCHEMA,
        "file": path.name,
        "parse_status": "parsed",
        "sheet_count": 0,
        "sheets": [],
        "summary": {},
    }
    try:
        with zipfile.ZipFile(path) as archive:
            sheets = _sheet_names(archive)
            if not sheets:
                payload["parse_status"] = "unreadable"
                payload["error"] = "工作簿里没有工作表记录（workbook.xml 缺失或损坏）"
                return payload
            shared = _shared_strings(archive)
            styles = _read(archive, "xl/styles.xml")
            date_styles = _date_styles(styles)
            date1904 = False
            workbook = _read(archive, "xl/workbook.xml")
            if workbook is not None:
                for element in workbook.iter():
                    if _local(element.tag) == "workbookPr":
                        date1904 = str(element.get("date1904", "0")).lower() in {"1", "true"}
                        break
            budget = MAX_WORKBOOK_CELLS
            for index, sheet in enumerate(sheets, start=1):
                too_large = False
                if sheet["target"]:
                    try:
                        too_large = archive.getinfo(sheet["target"]).file_size > MAX_SHEET_XML_BYTES
                    except KeyError:
                        too_large = True
                root = (
                    _read(archive, sheet["target"]) if sheet["target"] and not too_large else None
                )
                if root is None:
                    payload["sheets"].append(
                        {
                            "name": sheet["name"],
                            "index": index,
                            "state": sheet["state"],
                            "rows": 0,
                            "columns": 0,
                            "range": "",
                            "truncated": False,
                            "header": [],
                            "cells": [],
                            "formulas": {},
                            "merged": [],
                            "cell_count": 0,
                            "note": (
                                f"工作表 XML 超过 {MAX_SHEET_XML_BYTES} 字节，未读取"
                                if too_large
                                else "工作表 XML 无法读取"
                            ),
                        }
                    )
                    continue
                sheet_payload = _sheet_payload(
                    root,
                    shared=shared,
                    date_styles=date_styles,
                    date1904=date1904,
                    budget=budget,
                )
                budget = max(0, budget - sheet_payload["cell_count"])
                payload["sheets"].append(
                    {
                        "name": sheet["name"],
                        "index": index,
                        "state": sheet["state"],
                        **sheet_payload,
                    }
                )
    except (zipfile.BadZipFile, OSError, RuntimeError) as error:
        payload["parse_status"] = "unreadable"
        payload["error"] = f"不是可读的 xlsx 容器：{error}"
        return payload
    total_cells = sum(sheet["cell_count"] for sheet in payload["sheets"])
    payload["sheet_count"] = len(payload["sheets"])
    payload["summary"] = {
        "sheet_names": [sheet["name"] for sheet in payload["sheets"]],
        "rows": sum(sheet["rows"] for sheet in payload["sheets"]),
        "cells": total_cells,
        "formula_cells": sum(len(sheet["formulas"]) for sheet in payload["sheets"]),
        "merged_ranges": sum(len(sheet["merged"]) for sheet in payload["sheets"]),
        "truncated": any(sheet["truncated"] for sheet in payload["sheets"]),
    }
    return payload


def _cell_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def workbook_text(payload: Dict[str, Any]) -> str:
    """A readable page: what the workbook holds, with the head of every sheet."""
    lines = [f"# {payload.get('file', '')}", ""]
    if payload.get("parse_status") != "parsed":
        lines.append(f"未能读取单元格：{payload.get('error', '')}")
        return "\n".join(lines) + "\n"
    sheets = payload.get("sheets") or []
    shapes = [f"{sheet['name']}（{sheet['rows']} 行 × {sheet['columns']} 列）" for sheet in sheets]
    lines.append(f"工作表 {len(sheets)} 个：" + "、".join(shapes))
    summary = payload.get("summary") or {}
    if summary.get("formula_cells"):
        lines.append(
            f"含公式单元格 {summary['formula_cells']} 个，合并单元格区域 {summary['merged_ranges']} 个。"
        )
    if summary.get("truncated"):
        lines.append(
            f"单元格过多，只保留了前 {MAX_SHEET_ROWS} 行、{MAX_SHEET_COLUMNS} 列、"
            f"合计 {MAX_WORKBOOK_CELLS} 个单元格；完整边界见 workbook.json 的 truncated 字段。"
        )
    for sheet in sheets:
        lines.extend(["", f"## {sheet['name']}"])
        if sheet.get("note"):
            lines.append(sheet["note"])
            continue
        grid = sheet.get("cells") or []
        if not grid:
            lines.append("空表。")
            continue
        width = min(len(grid[0]), TABLE_PAGE_COLUMNS)
        rows = grid[:TABLE_PAGE_ROWS]
        lines.append("| " + " | ".join(_cell_text(value) for value in grid[0][:width]) + " |")
        lines.append("| " + " | ".join("---" for _ in range(width)) + " |")
        for row in rows[1:]:
            lines.append("| " + " | ".join(_cell_text(value) for value in row[:width]) + " |")
        hidden_rows = max(0, len(grid) - len(rows))
        hidden_columns = max(0, len(grid[0]) - width)
        if hidden_rows or hidden_columns:
            lines.append(
                f"（页面只列前 {min(len(rows), TABLE_PAGE_ROWS)} 行、{width} 列；"
                f"另有 {hidden_rows} 行、{hidden_columns} 列未展开，完整数据在 workbook.json）"
            )
        if sheet.get("formulas"):
            sample = list(sheet["formulas"].items())[:5]
            lines.append("公式示例：" + "、".join(f"{ref} {text}" for ref, text in sample))
        if sheet.get("merged"):
            lines.append("合并区域：" + "、".join(sheet["merged"][:10]))
    return "\n".join(lines) + "\n"
