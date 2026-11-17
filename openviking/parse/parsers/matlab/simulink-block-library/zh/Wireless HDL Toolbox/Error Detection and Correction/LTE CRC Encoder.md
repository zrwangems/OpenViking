---
type: simulink-block
title: 'LTE CRC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ltecrcencoder'
documentation_source_path: 'ref/ltecrcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE CRC Encoder

## 端口
```yaml
ports:
- name: data
  summary: 输入样本 二值标量 | 无符号整数标量 | 二值向量
  direction: input
  data_types: single | double | Boolean | ufix1 | uint8 | uint16 | uint32 | ufixN
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: input
  data_types: bus
- name: data
  summary: 输出样本 二值标量 | 整数标量 | 二值向量
  direction: output
  data_types: single | double | Boolean | ufix1 | uint8 | uint16 | uint32 | ufixN
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
```

### 输入

### **data** — 输入样本 二值标量 | 无符号整数标量 | 二值向量

输入样本，指定为二值标量、无符号整数标量或二值向量。向量大小 *InputSize* 必须小于或等于多项式的长度。CRC 长度也必须能被向量大小整除。例如，对于多项式类型 `CRC24A`，有效的向量大小为 24、12、8、6、4、3、2 和 1。整数输入被解释为二值字。例如，向量输入 `[0 0 0 1 0 0 1 1]` 等价于 `uint8` 输入 `19`。

`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32` | `ufixN`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### 输出

### **data** — 输出样本 二值标量 | 整数标量 | 二值向量

输出样本，返回为与输入样本具有相同数据类型和大小的二值标量、整数标量或二值向量。该模块在每个帧的末尾附加计算并掩码后的校验和。

`double` 和 `single` 二值支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32` | `ufixN`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: CRC Type
  summary: 编码多项式 CRC16（默认）| CRC8 | CRC24A | CRC24B
  group: ''
- name: CRC Mask
  summary: 应用于校验和的掩码 0（默认）| 从 0 到 2*CRCLength* – 1 的整数
  group: ''
```

### **CRC Type** — 编码多项式 `CRC16`（默认）| `CRC8` | `CRC24A` | `CRC24B`

编码多项式选项为 LTE 标准 TS 36.212 [1] 第 5.1.1 节中描述的四种 CRC 类型。

### **CRC Mask** — 应用于校验和的掩码 `0`（默认）| 从 0 到 2*CRCLength* – 1 的整数

应用于校验和的掩码，指定为表示从 0 到 2*CRCLength* – 1 的二值字的整数。该掩码通常为无线网络临时标识符（RNTI）。
## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017b 中引入**

## 描述

生成校验和并附加到输入样本流

LTE CRC Encoder 模块为每帧流式数据样本计算并附加循环冗余校验 (CRC) 校验和。您可以从 LTE 标准 TS 36.212 [1] 指定的多项式中选择。该模块提供了硬件优化的架构和接口。

此模块使用带有相关控制信号总线的流式样本接口。该接口使模块能够独立于帧大小运行，并轻松连接到其他 Wireless HDL Toolbox™ 模块。该模块接受并返回表示单个样本的值，以及包含三个控制信号的总线。这些信号指示每个样本的有效性和帧边界。要将矩阵转换为样本流和这些控制信号，请使用 Frame To Samples 模块或 `whdlFramesToSamples` 函数。有关该接口的完整描述，请参阅 Streaming Sample Interface。

在前一帧完成之前，不得应用另一帧。硬件友好的算法会增加 `(CRCLength + 3)/InputSize` 个周期的延迟。为了考虑附加校验和样本的额外周期以及延迟，您必须在输入帧之间应用 `(2*CRCLength + 3)/InputSize` 的最小间隔。或者，您可以使用输出信号 **ctrl**.`end` 来确定模块何时准备好接收新输入。如果过早应用下一帧，**ctrl**.`start` 信号将重置校验和计算并截断前一帧。

此波形显示了一个 40 样本的帧，每次两个样本输入到 CRC16 编码器。因此，输入帧之间的间隔为 8 个周期。由于插入了校验和，输出 **ctrl**.`valid` 信号保持连续高电平，帧之间没有间隙。输入和输出 **ctrl** 总线被展开以显示控制信号。`start` 和 `end` 显示帧边界，`valid` 限定数据样本。

显示流式数据和控制信号的 Logic Analyzer 波形。
