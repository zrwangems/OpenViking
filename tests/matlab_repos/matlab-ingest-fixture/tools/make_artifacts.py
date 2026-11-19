"""为 MATLAB 入库测试项目补齐安装目录里没有的扩展名。

处理项：
  .hex / .s19  —— 由官方二进制派生（Intel HEX / Motorola S-record）
  .dbc / .ldf  —— 按格式规范合成最小合法文件
  .autosave    —— 编辑器不产出该后缀，按同源文件副本落盘
  .mlappinstall / .mlpkginstall —— 按 MATLAB 附加组件 OPC 结构合成，标注为格式合成
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def intel_hex(data: bytes, base: int = 0, rec_len: int = 16) -> str:
    lines = []
    upper = -1
    for off in range(0, len(data), rec_len):
        chunk = data[off:off + rec_len]
        addr = base + off
        hi = addr >> 16
        if hi != upper:
            upper = hi
            payload = bytes([(hi >> 8) & 0xFF, hi & 0xFF])
            lines.append(":02000004%04X%02X" % (
                int.from_bytes(payload, "big"),
                (-(0x02 + 0x00 + 0x00 + payload[0] + payload[1])) & 0xFF,
            ))
        lo = addr & 0xFFFF
        body = bytes([len(chunk), (lo >> 8) & 0xFF, lo & 0xFF, 0x00]) + chunk
        csum = (-sum(body)) & 0xFF
        lines.append(":" + body.hex().upper() + "%02X" % csum)
    lines.append(":00000001FF")
    return "\n".join(lines) + "\n"


def srecord(data: bytes, base: int = 0, rec_len: int = 16) -> str:
    lines = []
    for off in range(0, len(data), rec_len):
        chunk = data[off:off + rec_len]
        addr = base + off
        body = bytes([len(chunk) + 5]) + addr.to_bytes(4, "big") + chunk
        csum = (~sum(body)) & 0xFF
        lines.append("S3" + body.hex().upper() + "%02X" % csum)
    lines.append("S70500000000FA")
    return "\n".join(lines) + "\n"


DBC = """VERSION ""


NS_ :
\tNS_DESC_
\tCM_
\tBA_DEF_
\tBA_
\tVAL_
\tCAT_DEF_
\tCAT_
\tFILTER
\tBA_DEF_DEF_
\tEV_DATA_
\tENVVAR_DATA_
\tSGTYPE_
\tSGTYPE_VAL_
\tBA_DEF_SGTYPE_
\tBA_SGTYPE_
\tSIG_TYPE_REF_
\tVAL_TABLE_
\tSIG_GROUP_
\tSIG_VALTYPE_
\tSIGTYPE_VALTYPE_
\tBO_TX_BU_
\tBA_DEF_REL_
\tBA_REL_
\tBA_DEF_DEF_REL_
\tBU_SG_REL_
\tBU_EV_REL_
\tBU_BO_REL_
\tSG_MUL_VAL_

BS_:

BU_: VCU BMS

BO_ 500 VCU_Status: 8 VCU
 SG_ VehSpeed : 0|16@1+ (0.01,0) [0|655.35] "km/h" BMS
 SG_ SysVolt : 16|12@1+ (0.1,0) [0|409.5] "V" BMS
 SG_ AliveCnt : 28|4@1+ (1,0) [0|15] "" BMS

CM_ BO_ 500 "VCU status frame";
CM_ SG_ 500 VehSpeed "Vehicle speed";
BA_DEF_ BO_ "GenMsgCycleTime" INT 0 65535;
BA_DEF_DEF_ "GenMsgCycleTime" 100;
BA_ "GenMsgCycleTime" BO_ 500 100;
"""

LDF = """LIN_description_file;
LIN_protocol_version = "2.2";
LIN_language_version = "2.2";
LIN_speed = 19.2 kbps;

Nodes {
  Master: VCU, 10 ms, 0.1 ms;
  Slaves: BMS;
}

Signals {
  VehSpeed: 16, 0, VCU, BMS;
  SysVolt: 12, 0, VCU, BMS;
  AliveCnt: 4, 0, VCU, BMS;
}

Diagnostic_signals {
  MasterReqB0: 8, 0;
  MasterReqB1: 8, 0;
  SlaveRespB0: 8, 0;
  SlaveRespB1: 8, 0;
}

Frames {
  StatusFrame: 0x10, VCU, 8 {
    VehSpeed, 0;
    SysVolt, 16;
    AliveCnt, 28;
  }
}

Sporadic_frames {
}

Event_triggered_frames {
}

Diagnostic_frames {
  MasterReq: 0x3C {
    MasterReqB0, 0;
    MasterReqB1, 8;
  }
  SlaveResp: 0x3D {
    SlaveRespB0, 0;
    SlaveRespB1, 8;
  }
}

Node_attributes {
  BMS {
    LIN_protocol = "2.2";
    configured_NAD = 0x20;
  }
}

Schedule_tables {
  NormalSchedule {
    StatusFrame delay 10 ms;
  }
}

Signal_encoding_types {
  Speed_Encoding {
    physical_value, 0, 65535, 0.01, "km/h";
  }
}

Signal_representation {
  Speed_Encoding: VehSpeed;
}
"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default ContentType="application/vnd.mathworks.matlab.filesystemDefault" Extension="mlapp"/>
  <Default ContentType="application/vnd.openxmlformats-package.relationships+xml" Extension="rels"/>
  <Default ContentType="text/plain;charset=utf-8" Extension="m"/>
  <Default ContentType="application/vnd.mathworks.matlab.addon.properties+xml" Extension="xml"/>
  <Override ContentType="application/vnd.mathworks.matlab.addon.configuration+xml" PartName="/metadata/configuration.xml"/>
  <Override ContentType="application/vnd.openxmlformats-package.core-properties+xml" PartName="/metadata/coreProperties.xml"/>
  <Override ContentType="application/vnd.mathworks.package.filesystemManifest+xml" PartName="/metadata/filesystemManifest.xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Target="metadata/addonProperties.xml" Type="http://schemas.mathworks.com/matlab/addon/2014/relationships/addonProperties"/>
  <Relationship Id="rId2" Target="metadata/coreProperties.xml" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties"/>
  <Relationship Id="rId3" Target="metadata/filesystemManifest.xml" Type="http://schemas.mathworks.com/package/2013/relationships/filesystemManifest"/>
  <Relationship Id="rId4" Target="metadata/configuration.xml" Type="http://schemas.mathworks.com/matlab/addon/2014/relationships/configuration"/>
</Relationships>
"""

ADDON_PROPS = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><addonProperties xmlns="http://schemas.mathworks.com/matlab/addon/2014/addonProperties"><identifier type="GUID">ingest-fixture-app</identifier><description>HEV ingest fixture app package</description></addonProperties>"""

CONFIG = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><configuration xmlns="http://schemas.mathworks.com/matlab/addon/2014/configuration"><apps><app><name>bertool</name><file>fsroot/HevIngestApp/bertool.mlapp</file></app></apps><matlabPaths><matlabPath>fsroot/HevIngestApp</matlabPath></matlabPaths></configuration>"""

CORE = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <dc:title>Ingest Fixture App</dc:title>
  <dc:creator>Ingest Fixture</dc:creator>
</cp:coreProperties>
"""

MANIFEST = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<filesystemManifest xmlns="http://schemas.mathworks.com/package/2013/filesystemManifest">
  <entry><path>fsroot/HevIngestApp/bertool.mlapp</path><type>file</type></entry>
</filesystemManifest>
"""

SUPPORT_INFO = """<?xml version="1.0" encoding="UTF-8"?>
<supportPackageInfo>
  <name>Ingest Fixture Hardware Support</name>
  <version>25.2.0</version>
  <vendor>Ingest Fixture</vendor>
  <hardware>Generic Fixture Board</hardware>
  <thirdParty>
    <component>fixture-driver</component>
    <license>BSD-3-Clause</license>
  </thirdParty>
</supportPackageInfo>
"""

INSTALL_M = """function install()
%INSTALL 支持包安装入口（入库测试用最小实现）
fprintf('Ingest Fixture support package installed.\\n');
end
"""


def write_hex_and_s19():
    blob = (ROOT / "bin" / "snapshot_blob.bin").read_bytes()[:8192]
    (ROOT / "bin" / "ingest_firmware.hex").write_text(intel_hex(blob), encoding="utf-8")
    (ROOT / "bin" / "ingest_firmware.s19").write_text(srecord(blob), encoding="utf-8")
    return len(blob)


def write_text_assets():
    (ROOT / "config" / "ingest_can.dbc").write_text(DBC, encoding="utf-8")
    (ROOT / "config" / "ingest_lin.ldf").write_text(LDF, encoding="utf-8")


def write_autosave():
    src = ROOT / "model" / "asbCubeSatMBSE" / "CubeSatMBSEModel" / "ModelConfiguration" / "detectChangeOrbitalElements.m"
    (ROOT / "src" / "detectChangeOrbitalElements.autosave").write_bytes(src.read_bytes())


def write_mlappinstall():
    out = ROOT / "packages" / "IngestFixtureApp.mlappinstall"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("metadata/addonProperties.xml", ADDON_PROPS)
        z.writestr("metadata/configuration.xml", CONFIG)
        z.writestr("metadata/coreProperties.xml", CORE)
        z.writestr("metadata/filesystemManifest.xml", MANIFEST)
        z.write(ROOT / "src" / "bertool.mlapp", "fsroot/HevIngestApp/bertool.mlapp")
    return out


def write_mlpkginstall():
    out = ROOT / "packages" / "IngestFixtureSupport.mlpkginstall"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("install.m", INSTALL_M)
        z.writestr("metadata/supportPackageInfo.xml", SUPPORT_INFO)
        z.writestr("thirdparty/fixture-driver/README.md",
                   "Placeholder payload for ingest testing.\n")
    return out


if __name__ == "__main__":
    n = write_hex_and_s19()
    write_text_assets()
    write_autosave()
    a = write_mlappinstall()
    p = write_mlpkginstall()
    print(f"hex/s19 源字节数: {n}")
    print("生成:", a.name, a.stat().st_size)
    print("生成:", p.name, p.stat().st_size)
