---
type: simulink-block
title: 'Median Filter'
family: 'analysis-enhancement'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'medianfilter'
documentation_source_path: 'ref/medianfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Median Filter

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

此模块支持单像素流或多像素流。对于单像素流，将单个输入像素指定为标量强度值。对于多像素流，指定包含两个、四个或八个像素强度值的向量。有关如何为多像素流设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

此模块不支持多分量流。要处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线完全相同，因此可以将单个总线连接到多个复制的模块。

该软件支持用于仿真的 `double` 和 `single` 数据类型，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### 输出

### **pixel** — 输出像素流 标量 | 向量

此模块支持单像素流或多像素流。使用单像素流时，模块返回单个像素作为标量强度值。使用多像素流时，模块返回强度值向量。此向量的大小与输入 **pixel** 向量相同。有关如何为多像素流设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

输出像素数据类型与输入像素的数据类型相同。

该软件支持用于仿真的 `double` 和 `single` 数据类型，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### **邻域大小** — 用于计算中值的图像区域大小 `3×3`（默认）| `5×5` | `7×7`

选择邻域大小（以像素为单位），可选 `3×3`、`5×5` 或 `7×7`。

当使用多像素流并将 **填充方法** 设置为 `None` 时，不能使用 `7×7` 的邻域大小。

### **填充方法** — 输入图像边界的填充方法 `Symmetric`（默认）| `Constant` | `Replicate` | `Reflection` | `None`

选择以下方法之一来填充输入图像的边界。有关这些方法的更多信息，请参阅 Edge Padding。

- `Constant` — 将图像帧外的像素解释为具有常量值。
- `Replicate` — 重复图像边缘处像素的值。
- `Symmetric` — 将填充像素的值设置为镜像图像边缘。
- `Reflection` — 将填充像素的值设置为围绕图像边缘像素进行反射。
- `None` — 排除填充逻辑。该模块不会将图像帧外的像素设置为任何特定值。此选项可减少模块使用的硬件资源以及帧之间所需的消隐，但会影响帧边缘处输出像素的准确性。为了保持像素流时序，输出帧与输入帧大小相同。但是，为了避免使用根据未定义填充值计算出的像素，请为下游操作屏蔽掉帧边缘周围的 *KernelSize*/2 个像素。有关详细信息，请参阅 Increase Throughput by Omitting Padding。

当将 **填充方法** 设置为 `None` 时，不能使用 `7×7` 的邻域大小。

### **填充值** — 用于填充输入图像边界的值 `0`（默认）| 整数

指定一个整数来填充输入图像的边界。该模块会将此值转换为与输入像素相同的数据类型。

#### 依赖关系

要启用此参数，请将 **填充方法** 参数设置为 `Constant`。

### **行缓冲大小** — 行缓冲区的大小 `2048`（默认）| 整数

行内存缓冲区的大小，指定为正整数。选择一个 2 的幂，以容纳水平行中的有效像素数。如果指定的值不是 2 的幂，则缓冲区使用下一个最大的 2 的幂。

使用多像素输入时，此值必须满足（**每行有效像素数**）/（**像素数**）+ 2。

该模块分配 (*N*— 1) × **行缓冲大小** 个内存位置，以存储用于计算中值的像素。*N* 是由 **邻域大小** 参数指定的正方形区域的维度。

## 所属库

Vision HDL Toolbox / Analysis & Enhancement Vision HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成 C/C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果此模块位于 Resettable Synchronous Subsystem (HDL Coder) 内，则无法为其生成 HDL 代码。

## 版本历史

**在 R2015a 中引入**

### R2023a：每个时钟两个像素的流式传输

此模块现在支持每个时钟周期 2 个像素的多像素流。

### R2021b：反射填充

通过围绕边缘像素值进行反射来填充帧的边缘。此填充方法有助于减少边缘对比度效应，并可在保持原始帧大小的同时改善机器学习结果。

### R2020a：省略填充的选项

现在可以将模块配置为不在有效帧边界周围添加填充。此选项可减少模块使用的硬件资源以及帧之间所需的消隐，但会影响帧边缘处输出像素的准确性。要使用此选项，请将 **填充方法** 参数设置为 `None`。有关示例，请参阅 Increase Throughput by Omitting Padding。

### R2019b：多像素流

Median Filter 模块现在支持多像素流。HDL 实现会并行复制每个像素的算法。

对于多像素流，此模块支持 4 个或 8 个像素的输入和输出列向量。**ctrl** 端口仍为标量，并且 `pixelcontrol` 总线中的控制信号适用于向量中的所有像素。

### R2018b：改进的行缓冲区

此模块内部的行缓冲区现在可处理突发数据，即像素行内不连续的 `valid` 信号。由于改进了填充逻辑并原生支持具有偶数行数的内核大小，此实现使用的硬件资源更少。此更改会影响 Line Buffer 模块以及使用内部行缓冲区的模块。

对于某些配置，行缓冲区的延迟现在减少几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳做法是使用像素流控制信号（而不是插入特定数量的延迟）来同步模型中的并行路径。

## 描述

二维中值滤波

Median Filter 模块将每个输入像素替换为指定周围 *N*×*N* 邻域的中值。中值比均值对极端值更不敏感。您可以使用此模块从图像中去除椒盐噪声，而不会显著降低图像的锐度。您可以指定邻域大小以及输入图像边缘的填充值。
