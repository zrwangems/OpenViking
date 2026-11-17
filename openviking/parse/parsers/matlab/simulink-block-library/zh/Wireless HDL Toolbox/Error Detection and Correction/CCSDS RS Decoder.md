---
type: simulink-block
title: 'CCSDS RS Decoder'
family: 'error-detection-and-correction'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ccsdsrsdecoder'
documentation_source_path: 'ref/ccsdsrsdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# CCSDS RS Decoder

## 端口

### 输入

### **data** — 输入码字数据，0 到 255 范围内的整数

输入码字数据，指定为 0 到 255 范围内的整数。此整数表示一个符号。

对于每帧的输入码字符号数，该模块接受的最大值为 255 x *I*，最小值为 (255 – *k* + 1) x *I*。*k* 是由 **Message length (k)** 参数指定的消息长度。*I* 是由 **Interleaving depth (I)** 参数指定的交织深度。输入码字符号数必须是 *I* 的整数倍。

该模块支持以下情况的背靠背输入帧：

- 当您将 **Message length (k)** 设置为 `223` 并将 **Interleaving depth (I)** 设置为 `3`、`4`、`5` 或 `8` 时的全长度码
- 当您将 **Message length (k)** 设置为 `239` 并将 **Interleaving depth (I)** 设置为 `1`、`2`、`3`、`4`、`5` 或 `8` 时的全长度码

该模块不支持以下情况的背靠背输入帧：

- 任何 **Message length (k)** 和 **Interleaving depth (I)** 值下的缩短码
- 当您将 **Message length (k)** 设置为 `223` 并将 **Interleaving depth (I)** 设置为 `1` 或 `2` 时的全长度码

`double` 和 `single` 数据类型允许用于仿真，但不允许用于 HDL 代码生成。对于 HDL 代码生成，请按 `fixdt(0,8,0)` 或 `uint8` 格式指定此值。

**数据类型：** `double` | `single` | `uint8` | `fixdt(0,8,0)`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，指定为 `samplecontrol` bus。该 bus 包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### 输出

### **data** — 解码后的消息数据，0 到 255 范围内的整数

解码后的消息数据，以 0 到 255 范围内的整数形式返回。输出数据类型与输入数据类型相同。

对于 *N* 个输入码字符号，该模块输出 *N* – (255 – *k*) x *I* 个解码消息符号。*k* 是由 **Message length (k)** 参数指定的消息长度，*I* 是由 **Interleaving depth (I)** 参数指定的交织深度。

**数据类型：** `double` | `single` | `uint8` | `fixdt(0,8,0)`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，以 `samplecontrol` bus 形式返回。该 bus 包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **err** — 输出数据损坏的指示 Boolean 标量

输出数据损坏的指示，以 Boolean 标量形式返回。

当此值为 `1` 时，输出包含错误。当此值为 `0` 时，输出包含零个错误。

如果输入码字数据中的符号错误数大于 (255 - *k*) x *I* / 2，则该模块输出数据而不纠正这些错误，并将 **err** 端口设置为 `1`，以指示输入码字数据中存在无法纠正的错误。*k* 是由 **Message length (k)** 参数指定的消息长度。

**数据类型：** `Boolean`

### **nextFrame** — 模块就绪指示 Boolean 标量

模块就绪指示，以 Boolean 标量形式返回。

当该模块准备好接受下一帧的开始信号时，该模块将此信号设置为 `1`（`true`）。如果该模块在 **nextFrame** 为 `0`（`false`）时接收到输入 **ctrl.start** 信号，则该模块丢弃正在处理的帧并开始处理新数据。

**数据类型：** `Boolean`

### **numCorrErr** — 已纠正错误数 非负标量

已纠正错误数，以非负标量形式返回。

该模块可纠正的最大错误数等于 (255 – *k*) x *I* / 2。如果输入码字数据中的错误数大于 (255 – *k*) x *I* / 2，则该模块输出数据而不纠正这些错误，并将 **numCorrErr** 端口设置为 `0`，以指示这些错误均无法纠正。

当 **err** 端口为 `1` 时，该模块将 **numCorrErr** 端口设置为 `0`。

#### 依赖项

要启用此端口，请选择 **Output number of corrected symbol errors** 参数。

**数据类型：** `uint8`

## 参数

### **Message length (k)** — 消息长度 `223`（默认） | `239`

选择消息长度。

### **Interleaving depth (I)** — 交织深度 `1`（默认） | `2` | `3` | `4` | `5` | `8`

选择交织深度。

### **Output number of corrected symbol errors** — 已纠正符号错误数 `off`（默认） | `on`

选择此参数以启用 **numCorrErr** 输出端口。此端口输出已纠正错误数。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® accelerator 和 rapid accelerator 模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2021b 中引入**

## 描述

根据 CCSDS 标准从 RS 码字解码并恢复消息

CCSDS RS Decoder 模块根据 Consultative Committee for Space Data Systems (CCSDS) 标准 [1] 从 Reed-Solomon (RS) 码字解码并恢复消息。该模块接受码字数据和 `samplecontrol` bus，并输出解码后的消息数据、`samplecontrol` bus、指示解码数据是否损坏以及模块是否准备好接受数据的控制信号，以及用于提供已纠正错误数的可选信号。该模块提供适合 HDL 代码生成和硬件部署的架构。

由于该模块的延迟会变化，该模块提供输出端口 **nextFrame**，用于指示该模块何时准备好接受新的输入码字数据。有关该模块延迟的更多详细信息，请参阅算法部分。

该模块还支持缩短的消息长度。您可以在卫星通信的 CCSDS 接收机中使用此模块。
