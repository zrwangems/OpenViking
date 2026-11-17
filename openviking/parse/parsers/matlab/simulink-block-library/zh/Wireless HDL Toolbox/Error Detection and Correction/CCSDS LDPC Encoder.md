---
type: simulink-block
title: 'CCSDS LDPC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ccsdsldpcencoder'
documentation_source_path: 'ref/ccsdsldpcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# CCSDS LDPC Encoder

## 端口

### 输入

### **data** — 输入数据比特 标量 | 列向量

输入数据比特，指定为 `Boolean` 标量或八元素 `Boolean` 列向量。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### 输出

### **data** — 编码输出数据比特 标量 | 向量

编码输出数据比特，返回为 `Boolean` 标量或八元素 `Boolean` 列向量。输出数据类型与输入数据类型相同。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **nextFrame** — 模块就绪指示符 标量

模块就绪指示符，返回为 `Boolean` 标量。

当模块准备好接受下一帧的开始时，模块将此信号设置为 `1`。如果模块在 **nextFrame** 为 `0` 时接收到输入 **ctrl.start** 信号，模块将丢弃正在进行的帧并开始处理新数据。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

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

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 CCSDS 遥测标准中规定的 (8160,7136) LDPC 码对数据进行编码

CCSDS LDPC 编码器模块使用咨询委员会空间数据系统（CCSDS）遥测标准中规定的 (8160,7136) 低密度奇偶校验（LDPC）码对数据进行编码。该模块接受数据比特和一路控制信号流作为输入。该模块输出编码比特、一路控制信号流，以及一个指示模块何时准备好接受新输入的信号。

该模块支持标量输入和大小为 8 的向量输入。该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在用于卫星通信的 CCSDS 发射机中使用此模块。要了解有关 CCSDS 遥测标准的更多信息，请参阅 [1]
