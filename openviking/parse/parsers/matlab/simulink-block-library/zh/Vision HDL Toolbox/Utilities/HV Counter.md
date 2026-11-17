---
type: simulink-block
title: 'HV Counter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'hvcounter'
documentation_source_path: 'ref/hvcounter.html'
language: zh-CN
chinese_source: worker-translation
---

# HV Counter

## 端口

### 输入

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`
### 输出

### **hCount** — 行内像素位置 正整数

行内的像素位置，以正整数形式返回。该模块在每行开始时清除像素计数。如果每行输入的像素数超过计数器的大小，则该模块返回饱和值，直到下一行开始。

**数据类型：** `fixdt(0,ceil(log2(ActiveVideoLines)),0)`

### **vCount** — 帧内行位置 正整数

帧或感兴趣区域内的行位置，以正整数形式返回。该模块在每帧开始时清除行计数。如果每帧输入的行数超过计数器的大小，则该模块返回饱和值，直到下一帧开始。

**数据类型：** `fixdt(0,ceil(log2(ActiveVideoLines)),0)`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`

## 参数

### **Active pixels per line** — 每行最大像素数 `320`（默认）| 正整数

每行最大像素数，指定为正整数。该模块实现一个像素计数器，其位数为
`ceil(log2(ActivePixelsPerLine))`。例如，对于每行 320 像素的帧，计数器有 9 位。对于每行 1024 像素的帧，计数器有 11 位。

### **Active video lines** — 每帧最大行数 `240`（默认）| 正整数

每帧最大行数，指定为正整数。该模块实现一个行计数器，其位数为
`ceil(log2(ActiveVideoLines))`。例如，对于每行 240 像素的帧，计数器有 8 位。对于每行 1080 像素的帧，计数器有 11 位。

## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2019a 中引入**

## 描述

统计像素流的有效维度

HV Counter 模块分析视频流，并返回每帧行数和每行像素数的当前计数。该模块还会延迟像素流的控制信号，使其与计数结果相对应。可将此模块用于使用像素在帧或感兴趣区域中位置的算法。

此波形展示了每行 10 个像素的视频帧前两行的像素流控制信号以及由此产生的计数器输出。HV Counter 模块具有两个周期的延迟来返回当前计数器值。

HV Counter 模块输入和输出信号的 Logic Analyzer 波形
