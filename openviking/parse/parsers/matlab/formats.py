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
    ".mlpkginstall": FormatSpec(
        "MATLAB support package installer",
        "ZIP 包清单与 XML 元数据",
        "https://www.mathworks.com/help/matlab/ref/matlab.addons.install.html",
        archive=True,
    ),
    ".sltx": FormatSpec(
        "Simulink project template",
        "ZIP 包清单与模板元数据",
        "https://www.mathworks.com/help/simulink/ug/create-a-simulink-project-template.html",
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
    ".jar": FormatSpec(
        "Java archive",
        "ZIP 包清单与 XML/属性元数据；不加载 Java 类",
        "https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jar.html",
        archive=True,
    ),
    ".ctf": FormatSpec(
        "MATLAB Component Technology File",
        "检测 ZIP 可读性；能列成员就列清单，否则保留原件和哈希",
        "https://www.mathworks.com/help/compiler/ctf-files.html",
        archive=True,
        opaque=True,
    ),
    ".mdf": FormatSpec(
        "ASAM MDF measurement data",
        "解压通道组/通道并导出 CSV；未知压缩块保留原因",
        "https://www.asam.net/standards/detail/mdf/",
    ),
    ".mf4": FormatSpec(
        "ASAM MDF4 measurement data",
        "解压通道组/通道并导出 CSV；未知压缩块保留原因",
        "https://www.asam.net/standards/detail/mdf/",
    ),
    ".blf": FormatSpec(
        "Vector Binary Logging Format",
        "统计帧、通道和报文 ID；有 DBC 时保留帧级信息",
        "https://www.vector.com/int/en/products/products-a-z/software/canalyzer/",
    ),
}
_MEX_RE = re.compile(r"\.mex(?:a64|w32|w64|maci64|maca64|glx|sol64)$")


def additional_extensions() -> list[str]:
    return [*_FORMATS, ".mexa64", ".mexw32", ".mexw64", ".mexmaci64", ".mexmaca64"]


def archive_manifest(path: str | Path) -> dict:
    """Return a stable member manifest for a ZIP-based MATLAB package.

    Listing works for encrypted archives too; the per-member ``encrypted`` flag
    records that the bytes were not read. A central-directory failure returns an
    empty member list instead of raising.
    """
    path = Path(path)
    try:
        with zipfile.ZipFile(path) as archive:
            infos = sorted(archive.infolist(), key=lambda item: item.filename)
            members = [
                {
                    "name": info.filename,
                    "size": info.file_size,
                    "compressed_size": info.compress_size,
                    "encrypted": bool(info.flag_bits & 0x1),
                }
                for info in infos
                if not info.is_dir()
            ]
    except (zipfile.BadZipFile, OSError, RuntimeError):
        members = []
    return {
        "schema": "ov.matlab.container/1",
        "file": path.name,
        "format": path.suffix.lower().lstrip("."),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "encrypted": any(member["encrypted"] for member in members),
        "member_count": len(members),
        "members": members,
        "boundary": "Members are listed, not executed; encrypted bytes were not read.",
    }
