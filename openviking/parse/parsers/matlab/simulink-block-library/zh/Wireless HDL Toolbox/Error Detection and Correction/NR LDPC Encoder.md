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

### **data** — 输入数据位 标量 | 向量

输入数据位，指定为标量或大小为 64 的列向量。

有关如何指定向量输入数据的详细信息，请参阅 Specifying Vector Input。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **bgn** — 基图编号 标量

基图编号，指定为标量。当该值为 `0` 时，模块应用 *bgn 1*。当该值为 `1` 时，模块应用 *bgn 2*。有关 *bgn 1* 和 *bgn 2* 的更多信息，请参阅 TS 38.212 [1] 的第 5.3.2 节。

**数据类型：** `Boolean`

### **liftingSize** — 输入提升大小 标量

输入提升大小，指定为标量。

对于无效的 **liftingSize** 值，模块丢弃当前帧并等待新帧。

有关支持的提升大小值的更多信息，请参阅 TS 38.212 [1] 的第 5.3.2 节。

**数据类型：** `uint16`

### 输出

### **data** — 编码输出数据位 标量 | 向量

编码输出数据位，返回为标量或大小为 64 的列向量。

模块以与输入数据位相似的格式输出数据位。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **liftingSize** — 输出提升大小 标量

输出提升大小，返回为标量。

**数据类型：** `uint16`

### **nextFrame** — 准备好接收新输入 标量

当模块准备好接受下一帧的开始信号时，模块将该信号设置为 `1`。如果模块在 **nextFrame** 为 `0` 时接收到输入 **start** 信号，模块将丢弃正在进行的帧并开始处理新数据。

有关更多信息，请参阅 Using the nextFrame Output Signal。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法为 Resettable Synchronous Subsystem (HDL Coder) 内的此模块生成 HDL。

## 版本历史

**在 R2020a 中引入**

## 描述

根据 5G NR 标准执行 LDPC 编码

NR LDPC Encoder 模块实现具有硬件友好控制信号的低密度奇偶校验 (LDPC) 编码器。该模块接受数据位、控制信号流、基图编号和提升大小。该模块输出编码位、控制信号流、提升大小，以及一个指示模块何时准备好接受新输入信号的信号。

该模块的功能与函数 `nrLDPCEncode` (5G Toolbox) 的功能匹配。您可以将此模块用于根据 5G 新无线电 (NR) 标准 TS 38.212 [1] 的下行链路和上行链路共享信道以及寻呼信道的信道编码。

该模块支持标量和向量输入。该模块提供适合 HDL 代码生成和硬件部署的架构。有关更多信息，请参阅算法。
