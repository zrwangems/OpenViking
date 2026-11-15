# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""MATLAB code and Live Script (MLX) to Markdown conversion."""

from __future__ import annotations

import hashlib
import re
import zipfile
from pathlib import Path

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member

_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def parse_mlx(path: str | Path) -> str:
    path = Path(path)
    try:
        with zipfile.ZipFile(path) as archive:
            document = ET.fromstring(read_xml_member(archive, "matlab/document.xml"))
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid MLX archive: {path.name}") from exc
    except KeyError as exc:
        raise ValueError(f"MLX archive has no matlab/document.xml: {path.name}") from exc
    lines = ["---", "type: matlab-live-script", "---", "", f"# {path.stem}", ""]
    for paragraph in document.iter(_W + "p"):
        # AlternateContent contains Choice and Fallback; only use direct runs so
        # text is not duplicated. Paragraph properties may still live in Choice.
        texts = [
            node.text or ""
            for run in paragraph.findall("./" + _W + "r")
            for node in run.iter(_W + "t")
        ]
        text = "".join(texts)
        if not text.strip():
            continue
        style_node = paragraph.find("./" + _W + "pPr/" + _W + "pStyle")
        if style_node is None:
            style_node = paragraph.find(".//" + _W + "pStyle")
        style = style_node.get(_W + "val", "text") if style_node is not None else "text"
        if style == "code":
            lines.extend(["```matlab", text, "```", ""])
        elif style.startswith("heading"):
            try:
                level = min(6, max(2, int(style.removeprefix("heading") or 1) + 1))
            except ValueError:
                level = 2
            lines.extend(["#" * level + " " + text, ""])
        else:
            lines.extend([text, ""])
    lines.extend(
        [
            "## 解析边界",
            "",
            "仅转换 Live Script 正文和代码。`matlab/output.xml` 中保存的运行输出、图片及交互控件状态不作为可执行逻辑重复注入。",
            "",
        ]
    )
    return "\n".join(lines)


def parse_p_file(path: str | Path) -> str:
    """Describe opaque P-code without pretending to recover its source.

    MathWorks documents P-code as an obfuscated, executable content-obscured
    format, not as a documented interchange AST. Static source recovery would
    require a version-specific reverse engineering implementation.
    """
    path = Path(path)
    raw = path.read_bytes()
    return "\n".join(
        [
            "---",
            "type: matlab-pcode",
            "parse_status: opaque",
            "---",
            "",
            f"# {path.name}",
            "",
            "MATLAB P-code 是内容混淆的可执行格式。MathWorks 没有公开用于恢复 M 源码或 AST 的容器规范，"
            "因此本页只记录可验证元数据，原始 `.p` 文件与本页一起保留。",
            "",
            f"- 字节数：`{len(raw)}`",
            f"- SHA-256：`{hashlib.sha256(raw).hexdigest()}`",
            f"- 文件头（前 32 字节）：`{raw[:32].hex()}`",
            "",
            "## Compile 约束",
            "",
            "可以在其他 MLX/M 页面中检索同名调用，建立依赖关系；不得根据文件名推断内部实现。"
            "若必须理解逻辑，需要原 M 源码，或在获得授权的 MATLAB 环境中通过公开诊断接口补充信息。",
            "",
            "格式说明：https://www.mathworks.com/help/matlab/ref/pcode.html",
            "",
        ]
    )


def parse_m_file(path: str | Path) -> str:
    path = Path(path)
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "gb18030", "cp1252"):
        try:
            content = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        content = raw.decode("latin-1")
    functions = re.findall(
        r"(?im)^\s*function\s+(?:\[[^\n=]*\]|\w+)?\s*=?\s*([A-Za-z]\w*)\s*(?:\([^\n]*\))?", content
    )
    class_match = re.search(
        r"(?m)^\s*classdef(?:\s*\([^)]*\))?\s+([A-Za-z]\w*)(?:\s*<\s*([^\n%]+))?",
        content,
    )
    packages = [part[1:] for part in path.parent.parts if part.startswith("+")]
    class_folders = [part[1:] for part in path.parent.parts if part.startswith("@")]
    kind = "class" if class_match else "function" if functions else "script"
    lines = [
        "---",
        "type: matlab-code",
        f"matlab_kind: {kind}",
        "---",
        "",
        f"# {path.name}",
        "",
    ]
    if packages:
        lines.extend(["MATLAB package：" + ".".join(f"`{name}`" for name in packages), ""])
    if class_match:
        class_name = class_match.group(1)
        parents = class_match.group(2)
        lines.extend(
            [f"classdef：`{class_name}`" + (f"，继承 `{parents.strip()}`" if parents else ""), ""]
        )
    if class_folders:
        lines.extend(["类方法目录：" + "、".join(f"`@{name}`" for name in class_folders), ""])
    if functions:
        lines.extend(["函数 / 方法：" + ", ".join(f"`{name}`" for name in functions), ""])
    section_count = len(re.findall(r"(?m)^\s*%%(?:\s|$)", content))
    if section_count:
        lines.extend([f"代码节（`%%`）：**{section_count}**", ""])
    lines.extend(["```matlab", content, "```", ""])
    return "\n".join(lines)
