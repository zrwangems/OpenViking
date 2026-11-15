# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Additional documented MATLAB/Simulink formats with honest degradation.

The registry is deliberately product-format based, not a claim that every toolbox
invented by MathWorks or third parties uses one of these suffixes. Unknown formats
remain the directory scanner's responsibility and must not be silently accepted.
"""

from __future__ import annotations

import hashlib
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member
from openviking.parse.parsers.matlab.scripts import parse_m_file, parse_mlx


@dataclass(frozen=True)
class FormatSpec:
    title: str
    handling: str
    source: str
    text: bool = False
    archive: bool = False
    opaque: bool = False


# Official format references are kept here rather than copied into every result.
_FORMATS = {
    ".asv": FormatSpec(
        "MATLAB editor backup",
        "按 M 源码读取，不执行",
        "https://www.mathworks.com/help/matlab/",
        text=True,
    ),
    ".fig": FormatSpec(
        "MATLAB figure",
        "按 MAT 容器提取句柄结构；不还原像素",
        "https://www.mathworks.com/help/matlab/ref/savefig.html",
    ),
    ".mlapp": FormatSpec(
        "MATLAB App Designer app",
        "提取 Live Code 文档或 ZIP 清单",
        "https://www.mathworks.com/help/matlab/app-designer.html",
        archive=True,
    ),
    ".mlappinstall": FormatSpec(
        "MATLAB app installer",
        "ZIP 包清单与 XML 元数据",
        "https://www.mathworks.com/help/matlab/ref/matlab.apputil.install.html",
        archive=True,
    ),
    ".mltbx": FormatSpec(
        "MATLAB toolbox installer",
        "ZIP 包清单与 XML 元数据",
        "https://www.mathworks.com/help/matlab/matlab_prog/create-and-share-custom-matlab-toolboxes.html",
        archive=True,
    ),
    ".mlproj": FormatSpec(
        "MATLAB project archive",
        "ZIP 包清单与 XML 元数据",
        "https://www.mathworks.com/help/matlab/projects.html",
        archive=True,
    ),
    ".prj": FormatSpec(
        "MATLAB/Simulink project definition",
        "ZIP 或 XML 元数据",
        "https://www.mathworks.com/help/matlab/projects.html",
        archive=True,
    ),
    ".mdl": FormatSpec(
        "legacy Simulink model",
        "文本 MDL 块/连线；ZIP 变体按 SLX",
        "https://www.mathworks.com/help/simulink/slref/save_system.html",
    ),
    ".slxp": FormatSpec(
        "protected Simulink model",
        "保留原文件和容器清单，不伪造可读模型",
        "https://www.mathworks.com/help/simulink/",
        archive=True,
        opaque=True,
    ),
    ".mdlp": FormatSpec(
        "protected legacy Simulink model",
        "保留原文件和可验证元数据",
        "https://www.mathworks.com/help/simulink/",
        opaque=True,
    ),
    ".slxc": FormatSpec(
        "Simulink simulation cache",
        "派生缓存，只记录边界和哈希",
        "https://www.mathworks.com/help/simulink/",
        opaque=True,
    ),
    ".autosave": FormatSpec(
        "Simulink autosave/backup",
        "保留原文件和可验证元数据，不猜测其主文件版本",
        "https://www.mathworks.com/help/simulink/",
        opaque=True,
    ),
    ".ssc": FormatSpec(
        "Simscape language source",
        "保留组件、节点、输入输出和方程原文",
        "https://www.mathworks.com/help/simscape/",
        text=True,
    ),
    ".sscp": FormatSpec(
        "protected Simscape source",
        "保留原文件，不声称恢复 Simscape 源码",
        "https://www.mathworks.com/help/simscape/ref/sscprotect.html",
        opaque=True,
    ),
    ".sfx": FormatSpec(
        "standalone Stateflow chart",
        "提取 XML 文本和状态/转移标签",
        "https://www.mathworks.com/help/stateflow/",
        archive=True,
    ),
    ".slreqx": FormatSpec(
        "Simulink Requirements set",
        "ZIP 清单及 XML 文本",
        "https://www.mathworks.com/help/slrequirements/",
        archive=True,
    ),
    ".slmx": FormatSpec(
        "Simulink requirement link set",
        "ZIP 清单及 XML 文本",
        "https://www.mathworks.com/help/slrequirements/",
        archive=True,
    ),
    ".mldatx": FormatSpec(
        "Simulink Test file",
        "ZIP 清单及 XML 文本，不执行测试",
        "https://www.mathworks.com/help/sltest/",
        archive=True,
    ),
    ".tlc": FormatSpec(
        "Target Language Compiler source",
        "文本源码，不执行代码生成",
        "https://www.mathworks.com/help/rtw/tlc/what-is-the-target-language-compiler.html",
        text=True,
    ),
    ".fmu": FormatSpec(
        "Functional Mock-up Unit",
        "ZIP 清单及 modelDescription.xml 接口",
        "https://www.mathworks.com/help/simulink/",
        archive=True,
    ),
}
_MEX_RE = re.compile(r"\.mex(?:a64|w64|maci64|maca64|glx|sol64)$")


def is_additional_format(suffix: str) -> bool:
    suffix = suffix.lower()
    return suffix in _FORMATS or bool(_MEX_RE.fullmatch(suffix))


def additional_extensions() -> list[str]:
    return [*_FORMATS, ".mexa64", ".mexw64", ".mexmaci64", ".mexmaca64"]


def format_spec(suffix: str) -> FormatSpec:
    suffix = suffix.lower()
    return _FORMATS.get(suffix) or FormatSpec(
        "MATLAB MEX binary",
        "保留平台可执行文件，不反汇编、不执行",
        "https://www.mathworks.com/help/matlab/matlab_external/introducing-mex-files.html",
        opaque=True,
    )


def parse_additional(path: str | Path) -> tuple[str, str]:
    """Return Markdown and a stable format label for a non-core MATLAB file."""
    path = Path(path)
    suffix = path.suffix.lower()
    spec = format_spec(suffix)
    if suffix in {".asv", ".tlc"}:
        return _replace_type(parse_m_file(path), "matlab-text-source", spec), suffix[1:]
    if suffix == ".ssc":
        return _simscape_source(path, spec), "ssc"
    if suffix == ".fig":
        from openviking.parse.parsers.matlab.mat import parse_mat

        try:
            content, _ = parse_mat(path)
        except Exception as exc:
            # FIG permits versioned MATLAB handle objects that SciPy cannot
            # deserialize. Keep the asset importable without inventing a figure.
            content = _opaque(path, spec)
            content += f"\nFIG 静态 MAT 提取未完成：`{type(exc).__name__}`。原始 FIG 已保留。\n"
            return content, "fig"
        return _replace_type(content, "matlab-figure", spec), "fig"
    if suffix == ".mdl" and not zipfile.is_zipfile(path):
        return _legacy_mdl(path, spec), "mdl"
    if suffix == ".mlapp" and zipfile.is_zipfile(path):
        try:
            with zipfile.ZipFile(path) as archive:
                if "matlab/document.xml" in archive.namelist():
                    return _replace_type(parse_mlx(path), "matlab-app", spec), "mlapp"
        except (KeyError, ValueError, ET.ParseError):
            pass
    if spec.archive and zipfile.is_zipfile(path):
        return _archive_inventory(path, spec), suffix[1:]
    return _opaque(path, spec), suffix[1:] or "mex"


def _replace_type(content: str, kind: str, spec: FormatSpec) -> str:
    content = re.sub(r"type: [^\n]+", f"type: {kind}", content, count=1)
    return content + f"\n## 格式处理\n\n{spec.handling}。官方说明：{spec.source}\n"


def _decode(raw: bytes) -> str:
    for encoding in ("utf-8-sig", "gb18030", "cp1252"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            pass
    return raw.decode("latin-1")


def _legacy_mdl(path: Path, spec: FormatSpec) -> str:
    text = _decode(path.read_bytes())
    blocks = re.findall(r"(?m)^\s*BlockType\s+\"?([^\n\"]+)", text)
    names = re.findall(r"(?m)^\s*Name\s+\"([^\n\"]+)\"", text)
    lines = _header(path, "simulink-legacy-model", spec)
    lines.extend(
        [
            "## 静态结构",
            "",
            f"- BlockType 声明：**{len(blocks)}**",
            f"- Name 声明：**{len(names)}**",
            "",
        ]
    )
    if blocks:
        from collections import Counter

        lines.extend(["| BlockType | 数量 |", "| --- | ---: |"])
        lines.extend(f"| `{name}` | {count} |" for name, count in Counter(blocks).most_common())
        lines.append("")
    lines.extend(["## MDL 原文", "", "```text", text, "```", ""])
    return "\n".join(lines)


def _simscape_source(path: Path, spec: FormatSpec) -> str:
    text = _decode(path.read_bytes())
    lines = _header(path, "simscape-source", spec)
    lines.extend(
        [
            "## 语言边界",
            "",
            "Simscape `nodes` 是守恒网络节点，不归类为输入输出；`inputs` / `outputs` 是物理信号。组件、参数、变量、分支和方程均保留原文，不执行 acausal 求解。",
            "",
            "```ssc",
            text,
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def _archive_inventory(path: Path, spec: FormatSpec) -> str:
    lines = _header(path, "matlab-container", spec)
    with zipfile.ZipFile(path) as archive:
        infos = sorted(archive.infolist(), key=lambda item: item.filename)
        lines.extend(["## 容器清单", "", "| 成员 | 未压缩字节 |", "| --- | ---: |"])
        for info in infos[:300]:
            member_name = info.filename.replace("|", "\\|")
            lines.append(f"| `{member_name}` | {info.file_size} |")
        if len(infos) > 300:
            lines.append(f"| 其余 {len(infos) - 300} 个成员 | 已保留在原包 |")
        lines.append("")
        xml_names = [
            info.filename
            for info in infos
            if info.filename.lower().endswith((".xml", ".rels"))
            and not info.is_dir()
            and info.file_size <= 8 * 1024 * 1024
        ]
        for name in xml_names[:20]:
            try:
                root = ET.fromstring(read_xml_member(archive, name))
            except (ET.ParseError, ValueError):
                continue
            texts = []
            for element in root.iter():
                value = (element.text or "").strip()
                if value and value not in texts:
                    texts.append(value)
                if len(texts) >= 120:
                    break
            if texts:
                lines.extend([f"### `{name}` 文本", "", "```text", "\n".join(texts), "```", ""])
    lines.extend(
        [
            "## 解析边界",
            "",
            "这是静态容器与元数据提取，不执行 app、工程、需求链接、测试或 FMU。成员较多或 XML 文本较长时有界展示，完整内容保留在原始文件中。",
            "",
        ]
    )
    return "\n".join(lines)


def _opaque(path: Path, spec: FormatSpec) -> str:
    raw = path.read_bytes()
    lines = _header(path, "matlab-opaque", spec)
    lines.extend(
        [
            "## 可验证元数据",
            "",
            f"- 字节数：`{len(raw)}`",
            f"- SHA-256：`{hashlib.sha256(raw).hexdigest()}`",
            f"- 文件头：`{raw[:32].hex()}`",
            "",
        ]
    )
    if spec.opaque:
        lines.extend(
            [
                "## 解析边界",
                "",
                f"{spec.handling}。原始文件已保留；不得由文件名或文件头补写内部逻辑。",
                "",
            ]
        )
    return "\n".join(lines)


def _header(path: Path, kind: str, spec: FormatSpec) -> list[str]:
    return [
        "---",
        f"type: {kind}",
        "parse_status: static",
        "---",
        "",
        f"# {path.name}",
        "",
        f"格式：{spec.title}。处理方式：{spec.handling}。",
        "",
        f"官方格式说明：{spec.source}",
        "",
    ]
