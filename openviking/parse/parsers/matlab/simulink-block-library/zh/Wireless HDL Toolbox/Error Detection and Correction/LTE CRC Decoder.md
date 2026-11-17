---
type: simulink-block
title: 'LTE CRC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ltecrcdecoder'
documentation_source_path: 'ref/ltecrcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE CRC Decoder

## 端口

### 输入

### **data** — 输入样本 二值标量 | 无符号整数标量 | 二值向量

输入样本，指定为二值标量、无符号整数标量或二值向量。向量大小必须小于或等于多项式的长度。CRC 长度还必须能被向量大小整除。例如，对于多项式类型 `CRC24A`，有效的向量大小为 24、12、8、6、4、3、2 和 1。整数输入被解释为二值字。例如，向量输入 `[0 0 0 1 0 0 1 1]` 等价于 `uint8` 输入 `19`。

`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`
### 输出

### **data** — 输出样本 二值标量 | 整数标量 | 二值向量

输出样本，返回为与输入样本具有相同数据类型和大小的二值标量、无符号整数标量或二值向量。校验和从帧末尾移除。

`double` 和 `single` 二值值支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32` | `ufixN`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **err** — 校验和不匹配指示 二值标量 | 整数标量

校验和不匹配指示，返回为二值标量或整数标量。如果选择 **Full checksum mismatch**，此端口返回计算出的校验和与附加校验和的整数 XOR 结果。当 **ctrl**.`end` 为 1（`true`）时，**err** 值有效。此端口的数据类型与输入样本的数据类型匹配。

**数据类型：** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32` | `ufixN`

## 参数

### **CRC Type** — 编码多项式 `CRC16`（默认）| `CRC8` | `CRC24A` | `CRC24B`

编码多项式选项是 LTE 标准 TS 36.212 [1] 第 5.1.1 节中描述的四种 CRC 类型。

### **Full checksum mismatch** — 返回逐位不匹配信息 off（默认）| on

未选择此参数时，**err** 端口在应用 **CRC Mask** 后返回一个布尔值，指示是否有任何校验和位不匹配。选择此参数时，**err** 端口返回一个整数，表示校验和中位不匹配的位置。

### **CRC Mask** — 应用于校验和的掩码 0（默认）| 从 0 到 2*CRCLength* – 1 的整数

应用于校验和的掩码，指定为表示从 0 到 2*CRCLength* – 1 的二值字的整数。此掩码通常是无线网络临时标识符（RNTI）。

#### 依赖关系

当 **Full checksum mismatch** 被清除时，此参数出现。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持为 Simulink® 加速器和快速加速器模式以及 DPI 组件生成生成 C/C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017b 中引入**

## 描述

使用校验和检测输入样本中的错误

LTE CRC 解码器模块计算循环冗余校验 (CRC)，并将其与附加的校验和进行比较，针对流式数据样本的每一帧。您可以从 LTE 标准 TS 36.212 [1] 指定的多项式中进行选择。该模块提供硬件优化的架构和接口。

此模块使用带有相关控制信号总线的流式样本接口。此接口使模块能够独立于帧大小运行，并轻松与其他 Wireless HDL Toolbox™ 模块连接。该模块接受并返回表示单个样本的值，以及包含三个控制信号的总线。这些信号指示每个样本的有效性和帧的边界。要将矩阵转换为样本流和这些控制信号，请使用 Frame To Samples 模块或 `whdlFramesToSamples` 函数。有关接口的完整描述，请参阅流式样本接口。
