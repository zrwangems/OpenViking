---
type: simulink-block
title: 'CCSDS RS Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Block Coding'
documentation_page: 'ccsdsrsencoder'
documentation_source_path: 'ref/ccsdsrsencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# CCSDS RS Encoder

## 端口

### 输入

### **data** — 输入消息符号，范围为 0 到 255 的整数

输入消息符号，指定为范围 0 到 255 的整数。每个整数表示一个符号。

每帧输入消息符号数必须等于 *p* × *I*，其中 *p* 可以是范围为 1 到 *k* 的任意整数。*k* 是消息长度，*I* 是模块掩码上指定的交织深度。

为提供正确的输出，模块要求输入帧之间存在 (255 – *k*) × *I* clock cycles 的最小帧间隔。

`double` 和 `single` 数据类型允许用于仿真，但不允许用于 HDL 代码生成。对于 HDL 代码生成，请以 `fixdt(0,8,0)` 或 `uint8` 格式指定此值。

**数据类型：** `double` | `single` | `uint8` | `fixdt(0,8,0)`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入
  **data** 端口上的数据有效

有关更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`

### 输出

### **data** — 编码码字符号，范围为 0 到 255 的整数

编码码字符号，返回为范围 0 到 255 的整数。输出数据类型与输入数据类型相同。

模块每帧输出 *N* + (255 – *k*) × *I* 个码字符号，其中 *N* 是输入消息符号数。*k* 是使用 **Message length (k)** 参数指定的消息长度，*I* 是使用 **Interleaving depth (I)** 参数指定的交织深度。

**数据类型：** `double` | `single` | `uint8` | `fixdt(0,8,0)`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出
  **data** 端口上的数据有效

有关更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`

### **nextFrame** — 模块就绪指示符 Boolean 标量

模块就绪指示符，返回为 Boolean 标量。

当模块准备好接受下一帧的起始时，模块将此信号设置为 `1` (`true`)。如果模块在 **nextFrame** 为 `0` (`false`) 时收到输入 **ctrl.start** 信号，模块将丢弃正在处理的帧并开始处理新数据。

**数据类型：** `Boolean`

## 参数

### **Message length (k)** — 消息长度 `223` (默认) | `239`

选择消息长度。

### **Interleaving depth (I)** — 交织深度 `1` (默认) | `2` | `3` | `4` | `5` | `8`

选择交织深度。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2022a 中引入**

## 描述

根据 CCSDS 标准将消息编码为 RS 码字

CCSDS RS Encoder 模块根据空间数据系统咨询委员会 (CCSDS) 标准 [1] 将消息符号编码为 Reed-Solomon (RS) 码字。该模块接受消息符号和 `samplecontrol` 总线，并输出编码码字数据、`samplecontrol` 总线以及一个 **nextFrame** 信号，该信号指示模块何时准备好接受新的输入消息符号。

该模块还支持缩短的消息长度。您可以在用于卫星通信的 CCSDS 发射机中使用此模块。该模块提供了适用于 HDL 代码生成和硬件部署的架构。
