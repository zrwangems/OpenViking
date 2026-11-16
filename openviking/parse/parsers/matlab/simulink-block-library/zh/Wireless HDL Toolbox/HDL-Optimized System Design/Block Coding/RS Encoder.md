---
type: simulink-block
title: 'RS Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Block Coding'
documentation_page: 'rsencoder'
documentation_source_path: 'ref/rsencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# RS Encoder

## 端口

### 输入

### **data** — 输入消息数据标量

输入消息数据，指定为表示一个符号的标量。

输入字长必须为无符号整数，等于 `ceil`(log2(**Codeword length (N)**))。对于输入数据字长 `3`，码字长度参数 **Codeword length (N)** 必须为 `7`。

`double` 和 `single` 数据类型允许用于仿真，但不允许用于 HDL 代码生成。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`
### 输出

### **data** — 编码码字数据标量

编码码字数据，以标量形式返回。此输出数据宽度与输入数据宽度相同。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **nextFrame** — 模块就绪指示标量

模块就绪指示，以标量形式返回。

当模块准备好接受下一帧的开始时，模块将此信号设置为 `1` (`true`)。如果模块在 **nextFrame** 为 `0` (`false`) 时接收到输入 **ctrl.start** 信号，模块将丢弃正在处理的帧并开始处理新数据。

**数据类型：** `Boolean`

## 参数

### **Codeword length (N)** — 码字长度 `7`（默认） | 7 到 65,535 范围内的整数

指定码字长度。

码字长度必须是等于 2*M* – 1 的整数，其中 *M* 是范围从 3 到 16 的整数。有关为 RS 码表示数据的更多信息，请参阅 Integer Format (Reed-Solomon Only)。

### **Message length (K)** — 消息长度 `3`（默认） | 3 到（**Codeword length (N)** – `2`）范围内的整数

指定消息长度。

有关为 RS 码表示数据的更多信息，请参阅 Integer Format (Reed-Solomon Only)。

### **Source of primitive polynomial** — 本原多项式来源 `Auto`（默认） | `Property`

指定本原多项式的来源。

- 选择 `Auto`，以基于 **Codeword length (N)** 参数值指定本原多项式。本原多项式的次数计算为 *M* = `ceil`(log2(**Codeword length (N)**))。
- 选择 `Property`，以使用 **Primitive polynomial** 参数指定本原多项式。

### **Primitive polynomial** — 本原多项式 `[1 0 1 1]`（默认） | 二进制行向量

指定一个二进制行向量，以幂的降序表示本原多项式。

有关如何指定本原多项式的更多信息，请参阅 Primitive Polynomials and Element Representations。

#### 依赖项

要启用此参数，请将 **Source of primitive polynomial** 参数设置为 `Property`。

### **Source of B, the starting power for roots of the primitive polynomial** — 本原多项式根的起始幂的来源 `Auto`（默认） | `Property`

指定本原多项式根的起始幂的来源。

- 选择 `Auto` 以使用默认 **B value** 参数值 `1`。
- 选择 `Property` 以启用 **B value** 参数。

### **B value** — 本原多项式根的起始幂 `1`（默认） | 正整数

指定本原多项式根的起始幂。

#### 依赖项

要启用此参数，请将 **Source of B, the starting power for roots of the primitive polynomial** 参数设置为 `Property`。

### **Enable puncturing** — 打孔模式来源 `off`（默认） | `on`

选择此参数以启用 **Puncture pattern vector** 参数。

### **Puncture pattern vector** — 打孔向量 `[1; 1; 0; 0]`（默认） | 二进制列向量

指定长度为 **Codeword length (N)** – **Message length (N)** 的二进制列向量。值 `1` 表示模块数据符号未被打孔，并且从数据流中保持不变。值 `0` 表示数据符号从数据流中被打孔（即移除）。

#### 依赖项

要启用此参数，请选择 **Enable puncturing** 参数。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速模式和快速加速模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2020b 中引入**

## 描述

将消息编码为 RS 码字

RS Encoder 模块将消息数据编码为 Reed-Solomon (RS) 码字。该模块接受消息数据和 `samplecontrol` 总线，并输出码字数据符号和 `samplecontrol` 总线。

由于模块的延迟会变化，模块提供输出端口 **nextFrame**，用于指示模块何时准备好接受新的输入消息数据。该模块提供适用于 HDL 代码生成和硬件部署的架构，并支持缩短的消息长度。

您可以使用此模块对许多通信系统前向纠错 (FEC) 码进行建模。该模块支持数字用户线路 (DSL)、WiMAX（802.16 m 和 e）、数字视频广播手持终端 (DVB-H)、数字视频广播卫星 (DVB-S) 服务，以及用于 3 MHz 以下手持设备 (DVB-SH) 的数字视频广播卫星服务。
