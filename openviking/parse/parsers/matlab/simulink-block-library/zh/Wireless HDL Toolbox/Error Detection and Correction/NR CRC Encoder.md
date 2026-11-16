---
type: simulink-block
title: 'NR CRC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrcrcencoder'
documentation_source_path: 'ref/nrcrcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# NR CRC Encoder

## 端口

### 输入

### **data** — 输入数据 二进制标量 | 二进制向量 | 无符号整数标量

输入数据，指定为二进制标量、二进制向量或无符号整数标量。

您可以使用以下选项之一指定输入数据：

- 标量 – 指定表示若干位的整数。对于这种情况，该模块支持无符号整数（`uint8`、`uint16` 或 `ufixN`）和 `Boolean` 数据类型。
- 向量 – 指定大小为 *N* 的二进制值向量。对于这种情况，该模块支持 `Boolean` 和 `ufix1` 数据。

*N* 是输入数据宽度，并且它必须小于或等于 CRC 多项式的长度，并且是指定 CRC 多项式长度的因子。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。

**示例：** 对于 CRC 类型 `CRC24A`，有效数据宽度为 24、12、8、6、4、3、2 和 1。整数输入被解释为二进制字。例如，当您指定 `uint8` 输入为 `19` 时，它等效于向量输入 `[0 0 0 1 0 0 1 1]`。

**数据类型：** `double` | `single` | `ufix1` | `uint8` | `uint16` | `Boolean` | `ufixN`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关详细信息，请参阅采样控制总线。

**数据类型：** `bus`

### **CRCMask** — CRC 校验和掩码 非负整数

CRC 校验和掩码，指定为表示从 0 到 2*CRCLength* – 1 的二进制字的非负整数，其中 *CRCLength* 是 CRC 多项式的长度。

此掩码通常是无线网络临时标识符 (RNTI)。RNTI 用于对 CRC 校验和进行异或。

#### 依赖项

要启用此端口，请将 **CRC type** 参数设置为 `CRC24C`，并选择 **Enable CRC mask input port** 参数。

**数据类型：** `ufix24`

### 输出

### **data** — CRC 编码数据 标量 | 向量

带附加 CRC 校验和的 CRC 编码数据，以标量或向量形式返回。输出数据类型和大小与输入数据相同。

**数据类型：** `double` | `single` | `ufix1` | `uint8` | `uint16` | `Boolean` | `ufixN`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关详细信息，请参阅采样控制总线。

**数据类型：** `bus`

## 参数

### **CRC type** — CRC 类型 `CRC16`（默认）| `CRC6` | `CRC11` | `CRC24A` | `CRC24B` | `CRC24C`

选择 CRC 类型。每种 CRC 类型表示一个多项式，如下表所示。

| CRC 类型 | 多项式 |
| --- | --- |
| `CRC6` | [1 1 0 0 0 0 1] |
| `CRC11` | [1 1 1 0 0 0 1 0 0 0 0 1] |
| `CRC16` | [1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1] |
| `CRC24A` | [1 1 0 0 0 0 1 1 0 0 1 0 0 1 1 0 0 1 1 1 1 1 0 1 1] |
| `CRC24B` | [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1] |
| `CRC24C` | [1 1 0 1 1 0 0 1 0 1 0 1 1 0 0 0 1 0 0 0 1 0 1 1 1] |

这些 CRC 多项式根据 5G NR 标准 3GPP TS 38.212 [1] 指定。

### **Enable CRC mask input port** — 启用 CRC 校验和掩码输入端口 `off`（默认）| `on`

选择此参数以启用 **CRCMask** 输入端口。

#### 依赖项

要启用此参数，请将 **CRC type** 参数设置为 `CRC24C`。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成

使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2021a 中引入**

## 描述

生成 CRC 码位并将其附加到输入数据

NR CRC Encoder 模块计算并生成一个短的、固定长度的二进制序列，称为循环冗余校验 (CRC) 校验和，将其附加到流式数据样本的每一帧，并输出 CRC 编码数据。该模块接受并返回带有伴随控制信号的数据样本流。控制信号指示样本的有效性和帧边界。

该模块支持标量和向量输入，并根据输入数据以标量或向量形式输出数据。为了实现更高的吞吐量，该模块接受二进制向量或无符号整数标量输入，并实现并行架构。输入数据宽度必须小于或等于 CRC 多项式的长度，并且 CRC 多项式的长度必须能被输入数据宽度整除。该模块支持根据 5G 新无线电 (NR) 标准 3GPP TS 38.212 [1] 指定的所有 CRC 多项式。当您选择 CRC24C 多项式时，该模块支持动态 CRC 掩码。

该模块提供适用于 HDL 代码生成和硬件部署的接口和硬件优化架构。
