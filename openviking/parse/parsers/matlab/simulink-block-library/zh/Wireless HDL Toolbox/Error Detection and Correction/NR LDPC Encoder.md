---
type: simulink-block
title: 'NR LDPC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrldpcencoder'
documentation_source_path: 'ref/nrldpcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# NR LDPC Encoder

## 端口

### 输入

### **data** — 输入数据比特 标量 | 向量

输入数据比特，指定为标量或大小为 64 的列向量。

有关如何指定向量输入数据的更多信息，请参阅指定向量输入。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，指定为 `samplecontrol` bus。该 bus 包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`

### **bgn** — 基图编号 标量

基图编号，指定为标量。当此值为 `0` 时，该模块应用 *bgn 1*。当此值为 `1` 时，该模块应用 *bgn 2*。有关 *bgn 1* 和 *bgn 2* 的更多信息，请参阅 TS 38.212 [1] 的 5.3.2 节。

**数据类型：** `Boolean`

### **liftingSize** — 输入提升大小 标量

输入提升大小，指定为标量。

对于无效的 **liftingSize** 值，该模块丢弃当前帧并等待新帧。

有关支持的提升大小值的更多信息，请参阅 TS 38.212 [1] 的 5.3.2 节。

**数据类型：** `uint16`

### 输出

### **data** — 编码输出数据比特 标量 | 向量

编码输出数据比特，返回为标量或大小为 64 的列向量。

该模块以与输入数据比特相似的格式输出数据比特。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，返回为 `samplecontrol` bus。该 bus 包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`

### **liftingSize** — 输出提升大小 标量

输出提升大小，返回为标量。

**数据类型：** `uint16`

### **nextFrame** — 准备好接受新输入 标量

当该模块准备好接受下一帧的起始时，该模块将此信号设置为 `1`。如果该模块在 **nextFrame** 为 `0` 时接收到输入 **start** 信号，则该模块丢弃正在处理的帧并开始处理新数据。

有关更多信息，请参阅使用 nextFrame 输出信号。

**数据类型：** `Boolean`

## 参数

未在 R2025b 中记录。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® accelerator 和 rapid accelerator 模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2020a 中引入**

## 描述

根据 5G NR 标准执行 LDPC 编码

NR LDPC Encoder 模块实现了一种带有硬件友好控制信号的低密度奇偶校验（LDPC）编码器。该模块接受数据比特、控制信号流、基图编号和提升大小。该模块输出编码比特、控制信号流、提升大小，以及一个指示该模块何时准备好接受新输入的信号。

该模块功能与函数 `nrLDPCEncode` (5G Toolbox) 的功能一致。根据 5G 新无线电 (NR) 标准 TS 38.212 [1]，您可以将此模块用于下行链路和上行链路共享信道以及寻呼信道的信道编码。

该模块支持标量和向量输入。该模块提供了适用于 HDL 代码生成和硬件部署的架构。有关更多信息，请参阅算法。
