---
type: simulink-block
title: 'Pixel Stream Aligner'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'pixelstreamaligner'
documentation_source_path: 'ref/pixelstreamaligner.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixel Stream Aligner

## 端口

### 输入

此模块使用带帧控制信号总线的流式像素接口。此接口使模块能够独立于图像尺寸和格式运行。此模块上的 **pixel** 端口支持单像素流式传输或多像素流式传输。单像素流式传输在每个时钟周期接受并返回单个像素值。多像素流式传输在每个时钟周期接受并返回 *M* 个像素的向量，以支持高帧率或高分辨率格式。*M* 值对应于 Frame To Pixels 模块的 **Number of pixels** 参数。除像素外，此模块还接受并返回包含五个控制信号的 `pixelcontrol` 总线。控制信号指示每个像素的有效性及其在帧中的位置。对于多像素流式传输，一组控制信号适用于向量中的所有像素。要将帧（像素矩阵）转换为串行像素流和控制信号，请使用 Frame To Pixels 模块。有关该接口的完整描述，请参阅 Streaming Pixel Interface。

此模块还支持多像素-多分量流，其中像素输入是 *M* 乘 *N* 值的矩阵。*M* 是像素数，*N* 是分量数。这些值对应于 Frame To Pixels 模块的 **Number of pixels** 和 **Number of components** 参数。

### **pixel** — 输入像素流 标量 | 向量 | 矩阵

对于单像素流，将 **pixel** 指定为标量或 1 乘 **Number of components** 值的向量。对于多像素流，将 **pixel** 指定为 **Number of pixels** 乘 **Number of components** 像素强度值的矩阵。**Number of pixels** 可以是二、四或八。

因为此模块延迟此像素流以匹配参考流的控制信号，所以 **pixel** 必须是两个流中较早的流。

自 R2025a 起，软件支持 `single` 数据类型用于仿真和 HDL 代码生成。要在您的模型中为 `single` 数据类型启用 HDL 代码生成，请打开 **HDL Coder** 应用，转到 **Floating Point** 窗格，然后选中 **Use Floating Point** 复选框。`double` 数据类型仅支持仿真，不支持 HDL 代码生成。

**数据类型：** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量有一组控制信号。因为该向量只有一个 `valid` 信号，所以该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于该向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于该向量中索引最高的像素。

**数据类型：** `bus`

### **refPixel** — 参考像素流 标量 | 向量 | 矩阵

将 **refPixel** 指定为标量、1 乘 **Number of components** 值的向量，或 **Number of pixels** 乘 **Number of components** 像素强度值的矩阵。

**refPixel** 允许的维度取决于输入 **pixel** 流的维度。**Number of pixels** 必须相同。

| 输入 pixel 维度 | 允许的 refPixel 维度 |
| --- | --- |
| 1-by-*N* | 1-by-1、1-by-3 或 1-by-4 |
| 2-by-*N* | 2-by-1、2-by-3 或 2-by-4 |
| 4-by-*N* | 4-by-1、4-by-3 或 4-by-4 |
| 8-by-*N* | 8-by-1、8-by-3 或 8-by-4 |

因为此模块延迟 **pixel** 输入流以匹配参考控制信号，所以 **refPixel** 必须是两个流中较晚的流。参考数据及其控制信号以小延迟通过模块。

自 R2025a 起，软件支持 `single` 数据类型用于仿真和 HDL 代码生成。要在您的模型中为 `single` 数据类型启用 HDL 代码生成，请打开 **HDL Coder** 应用，转到 **Floating Point** 窗格，然后选中 **Use Floating Point** 复选框。`double` 数据类型仅支持仿真，不支持 HDL 代码生成。

**数据类型：** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

### **refCtrl** — 参考像素流控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量有一组控制信号。因为该向量只有一个 `valid` 信号，所以该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于该向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于该向量中索引最高的像素。

此模块将这些控制信号用于对齐后的输出流。

**数据类型：** `bus`

### 输出

### **pixel** — 对齐后的像素流 标量 | 向量 | 矩阵

输出 **pixel** 流的时序与输出 **refPixel** 流的时序匹配。输出 **pixel** 流的维度和数据类型与输入 **pixel** 流的维度和数据类型匹配。

**数据类型：** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

### **refPixel** — 参考像素流 标量 | 向量 | 矩阵

输出 **refPixel** 流的维度和数据类型与输入 **refPixel** 流的维度和数据类型匹配。此模块使此流原样通过模块。

**数据类型：** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

### **refCtrl** — 参考控制信号 `pixelcontrol` 总线

此模块使输入 **refCtrl** 信号以小延迟通过模块。

**数据类型：** `bus`

## 参数

### **Line buffer size** — 行存储器缓冲区的大小 `2048`（默认） | 正整数

选择一个 2 的幂，以容纳水平行中的活动像素数。如果指定的值不是 2 的幂，则模块使用下一个最大的 2 的幂。此模块实现一个 2*m* 像素的循环缓冲区，其中 *m* 是 **Maximum number of lines** + log2(**Line buffer size**)。

使用多像素输入时，此值必须容纳（**Active pixels per line**）/（**Number of pixels**）+ 2。

### **Maximum number of lines** — 容纳输入流之间时序偏移的缓冲区深度 `10`（默认） | 正整数

此模块实现一个 2*m* 像素的循环缓冲区，其中 *m* 是 **Maximum number of lines** + log2(**Line buffer size**)，以及一个具有 **Maximum number of lines** 个位置的线地址缓冲区。循环存储器存储较早的输入行，直到参考控制信号到达。线地址缓冲区存储每一行起始的地址。当参考控制信号到达时，模块使用存储的地址读取并发送延迟的行。此参数必须容纳两个输入流之间的时序差异，包括模块读取第一行之前的内部延迟。在仿真期间，当发生溢出时，模块会发出警告。要避免溢出情况，请增大 **Maximum number of lines**。流之间的延迟不能超过整个帧。

当输入 **pixel** 是向量或矩阵时，模块为每个元素复制循环缓冲区。对于多像素流式传输，模块调整行缓冲区大小以存储 1/**Number of pixels** 个像素。例如，对于 4 乘 3 的输入流，每个缓冲区存储一行中 ¼ 的像素，并且缓冲区为 12×2*m-2* 个位置。线地址缓冲区保持相同大小。

## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL Architecture**

此模块有一种默认 HDL 架构。

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2017a 中引入**

### R2025a：支持用于 HDL 代码生成的 `single` 数据类型

此模块现在支持使用 `single` 数据类型像素输入进行 HDL 代码生成。

### R2022b：每时钟两个像素的流式传输

此模块现在支持每时钟周期 2 个像素的多像素流。

### R2021a：多像素-多分量流式传输

此模块现在支持同时为多像素和多分量的流。HDL 实现会并行复制每个像素和分量的算法。

此模块支持 *NumPixels* 乘 *NumComponents* 像素的输入和输出矩阵，其中 *NumPixels* 为 4 或 8。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号适用于矩阵中的所有像素。

### R2020b：多像素流式传输

Pixel Stream Aligner 模块现在支持多像素流。HDL 实现会并行复制每个像素的算法。不能同时使用多分量和多像素。

对于多像素流式传输，此模块支持 4 或 8 个像素的输入和输出列向量。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号适用于向量中的所有像素。

## 描述

对齐两个像素数据流

Pixel Stream Aligner 模块通过延迟一个流以匹配参考流的时序来同步两个像素流。许多 Vision HDL Toolbox™ 算法会延迟像素流，并且延迟量可能会随着您调整算法参数而变化。您可以使用此模块对齐流，以进行叠加、比较或组合两个流，例如在高斯模糊操作中。将延迟后的流连接到 **refPixel** 和 **refCtrl** 输入端口，将较早的流连接到 **pixel** 和 **ctrl** 输入端口。

此波形图显示输入流 `pixelIn` 和 `refPixelIn` 及其关联的控制信号。参考输入帧比 `pixelIn` 帧开始得晚。输出信号显示此模块延迟 `pixelIn` 以匹配参考流，并且两个输出流共享控制信号。该波形显示输入 `refCtrl` 和输出 `refCtrl` 之间的短延迟。在此仿真中，为了容纳输入流之间四行的延迟，**Maximum number of lines** 参数必须至少设置为 4。
