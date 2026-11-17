---
type: simulink-block
title: 'NR CRC Decoder'
family: 'error-detection-and-correction'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrcrcdecoder'
documentation_source_path: 'ref/nrcrcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# NR CRC Decoder

## 端口

### 输入

### **data** — CRC 编码数据 二进制标量 | 二进制向量 | 无符号整数标量

CRC 编码数据，指定为二进制标量、二进制向量或无符号整数标量。

您可以使用以下选项之一指定输入数据：

- 标量 – 指定表示若干位的整数。对于这种情况，模块支持无符号整数（`uint8`、`uint16` 或 `ufixN`）和 `Boolean` 数据类型。
- 向量 – 指定大小为 *N* 的二进制值向量。对于这种情况，模块支持 `Boolean` 和 `ufix1` 数据类型。

*N* 是输入数据宽度，必须小于或等于 CRC 多项式的长度，并且是指定 CRC 多项式长度的因数。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。

**示例：** 对于 CRC 类型 `CRC24A`，有效数据宽度为 24、12、8、6、4、3、2 和 1。整数输入被解释为二进制字。例如，当您指定 `uint8` 输入 `19` 时，它等价于向量输入 `[0 0 0 1 0 0 1 1]`。

**数据类型：** `double` | `single` | `ufix1` | `uint8` | `uint16` | `Boolean` | `ufixN`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **CRCMask** — CRC 校验和掩码 非负整数

CRC 校验和掩码，指定为表示从 0 到 2*CRCLength* – 1 的二进制字的非负整数，其中 *CRCLength* 是 CRC 多项式的长度。

此掩码通常是无线网络临时标识符 (RNTI)。RNTI 用于对 CRC 校验和进行异或。

#### 依赖项

要启用此端口，请将 **CRC type** 参数设置为 `CRC24C port` 并选择 **Enable CRC mask input port** 参数。

**数据类型：** `ufix24`
### 输出

### **data** — CRC 解码数据 标量 | 向量

CRC 解码数据，以标量或向量形式返回。输出数据类型和大小与输入数据相同。

**数据类型：** `double` | `single` | `ufix1` | `uint8` | `uint16` | `Boolean` | `ufixN`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **err** — 接收数据损坏的指示 二进制或整数标量

接收数据损坏的指示，以二进制或整数标量形式返回。

当此值为 `1` 时，消息包含至少一个错误。当此值为 `0` 时，消息包含零个错误。当 **ctrl.end** 设置为 1 `true` 时，此值有效。

如果您选择 **Full checksum mismatch** 参数，此端口返回校验和不匹配的整数异或结果。此值是输入中包含的 CRC 校验和与跨输入数据部分重新计算的 CRC 校验和之间的逻辑 CRC 差值结果。如果您指定 CRC 掩码，模块会将校验和与指定的 CRC 掩码进行异或。

**数据类型：** `Boolean` | `ufix24`

## 参数

### **CRC type** — CRC 类型 `CRC16`（默认）| `CRC6` | `CRC11` | `CRC24A` | `CRC24B` | `CRC24C`

选择 CRC 类型。每种 CRC 类型指示一个多项式，如下表所示。

| CRC 类型 | 多项式 |
| --- | --- |
| `CRC6` | [1 1 0 0 0 0 1] |
| `CRC11` | [1 1 1 0 0 0 1 0 0 0 0 1] |
| `CRC16` | [1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1] |
| `CRC24A` | [1 1 0 0 0 0 1 1 0 0 1 0 0 1 1 0 0 1 1 1 1 1 0 1 1] |
| `CRC24B` | [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1] |
| `CRC24C` | [1 1 0 1 1 0 0 1 0 1 0 1 1 0 0 0 1 0 0 0 1 0 1 1 1] |

这些 CRC 多项式根据 5G 新空口 (NR) 标准 3GPP TS 38.212 [1] 指定。

### **Full checksum mismatch** — 启用完整校验和 `off`（默认）| `on`

选择此参数以启用完整校验和。

当您选择此参数时，**err** 端口返回一个整数，表示 CRC 校验和位中位不匹配的位置。当您清除此参数时，**err** 端口返回一个布尔值，指示是否有任何 CRC 校验和位不匹配。

### **Enable CRC mask input port** — 启用 CRC 校验和掩码输入端口 `off`（默认）| `on`

选择此参数以启用 **CRCMask** 输入端口。

#### 依赖项

要启用此参数，请将 **CRC type** 参数设置为 `CRC24C`。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink® 加速器和快速加速器模式的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2021a 中引入**

## 描述

使用 CRC 检测输入数据中的错误

NR CRC Decoder 模块计算循环冗余校验 (CRC) 校验和，并将其与每个流数据样本帧追加的 CRC 校验和进行比较。如果两个 CRC 校验和不匹配，模块会报告错误。该模块接收并返回带有伴随控制信号的数据样本流。这些控制信号指示样本的有效性和帧的边界。

该模块支持标量和向量输入，并根据输入数据以标量或向量形式输出数据。为实现更高吞吐量，该模块接受二进制向量或无符号整数标量输入，并实现并行架构。输入数据宽度必须小于或等于 CRC 多项式的长度，并且 CRC 多项式的长度必须能被输入数据宽度整除。该模块支持根据 5G 新空口 (NR) 标准 3GPP TS 38.212 [1] 指定的所有 CRC 多项式。当您选择 CRC24C 多项式时，该模块支持动态 CRC 掩码。

该模块提供适用于 HDL 代码生成和硬件部署的接口和硬件优化架构。
