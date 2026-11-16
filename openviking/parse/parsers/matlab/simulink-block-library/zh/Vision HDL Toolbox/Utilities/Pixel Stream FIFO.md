---
type: simulink-block
title: 'Pixel Stream FIFO'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'pixelstreamfifo'
documentation_source_path: 'ref/pixelstreamfifo.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixel Stream FIFO

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量 | 矩阵

对于单像素流，将 **pixel** 指定为标量或表示单个像素的 1-by-**Number of components** 值的向量。对于多像素流，将 **pixel** 指定为 **Number of pixels**-by-**Number of components** 像素强度值的矩阵。**Number of pixels** 可以是二、四或八。

自 R2025a 起，软件支持将 `single` 数据类型用于仿真和 HDL 代码生成。要在您的模型中为 `single` 数据类型启用 HDL 代码生成，请打开 **HDL Coder** 应用，转到 **Floating Point** 窗格，然后选中 **Use Floating Point** 复选框。`double` 数据类型仅支持仿真，不支持 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量都有一组控制信号。由于向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### 输出

### **pixel** — 输出像素流 标量 | 向量 | 矩阵

输出流的每一行都具有连续的有效像素。输出 **pixel** 流的维度和数据类型与输入 **pixel** 流匹配。该模块将输出像素流返回为标量、1-by-**Number of components** 值的向量，或 **Number of pixels**-by-**Number of components** 值的矩阵。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **ctrl** — 伴随像素流 `pixelcontrol` 总线的控制信号

伴随像素流的控制信号，返回为包含五个信号的 `pixelcontrol` 总线。这些信号指示像素的有效性及其在帧中的位置。有关信号协议的详细信息，请参阅 Pixel Control Bus。

Pixel Stream FIFO 模块返回每一行像素，其中 **ctrl**.`valid` 信号在 **ctrl**.`hStart` 和 **ctrl**.`hEnd` 之间连续为 `true`。该模块会缓冲整个输入行，然后再返回修改后的行。

**数据类型：** `bus`

## 参数

### **Line buffer size** — 行内存缓冲区的大小 `2048`（默认） | 正整数

指定一个二的幂，其应能容纳单条水平线中的有效像素数量。如果指定的值不是二的幂，该模块将使用下一个最大的二的幂。

使用多像素输入时，此值必须能容纳 (**Active pixels per line**)/(**Number of pixels**) + 2。

## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持针对 Simulink® 加速模式和快速加速模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成：使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL Architecture**

此模块有一个默认 HDL 架构。

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟而在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Enabled Subsystem (Simulink)、Resettable Synchronous Subsystem (HDL Coder) 或 Triggered Subsystem (Simulink) 内为此模块生成 HDL。

## 版本历史

**R2018a 中引入**

### R2025a：`single` 数据类型支持 HDL 代码生成

该模块现在支持使用 `single` 数据类型像素输入进行 HDL 代码生成。

### R2022a：每时钟两个像素的流式传输

该模块现在支持每个时钟周期有 2 个像素的多像素流。

### R2021a：多像素多分量流式传输

该模块现在支持既多像素又多分量的流。HDL 实现会并行地为每个像素和分量复制该算法。

该模块支持 *NumPixels*-by-*NumComponents* 像素的输入和输出矩阵。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号适用于矩阵中的所有像素。

## 描述

缓冲输入流以创建具有连续有效像素的图像行

Pixel Stream FIFO 模块存储传入的有效像素和伴随的控制信号，并返回相同的像素流，且每一行的有效像素之间没有间隙。该模块保留视频流的总行大小和总帧大小，包括无效周期。

使用 Pixel Stream FIFO 模块来缓冲视频源。该波形显示了一个直接内存访问 (DMA) 视频源（其中像素以突发方式读取）和一个 Camera Link® 视频源（其中像素每隔一个时钟周期有效）。为了创建连续的视频行，Pixel Stream FIFO 模块会缓冲每个源的输入像素和控制信号。

针对 DMA 视频源和 Camera Link 视频源的 Pixel Stream FIFO 模块输入和输出信号的 Logic Analyzer 波形
