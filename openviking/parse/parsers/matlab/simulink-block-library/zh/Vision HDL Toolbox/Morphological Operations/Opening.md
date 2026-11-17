---
type: simulink-block
title: 'Opening'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'opening'
documentation_source_path: 'ref/opening.html'
language: zh-CN
chinese_source: worker-translation
---

# Opening

## 端口

### 输入

### **pixel** — 布尔输入像素或多像素向量 标量 | 向量

此模块支持单像素流式传输或多像素流式传输。对于单像素流式传输，将单个输入像素指定为标量布尔值。对于多像素流式传输，指定由四个或八个布尔值组成的向量。有关如何为多像素流式传输设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

**数据类型：** `Boolean`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于该向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于该向量中索引最高的像素。

**数据类型：** `bus`
### 输出

### **pixel** — 布尔输出像素或多像素向量 标量 | 向量

此模块支持单像素流式传输或多像素流式传输。使用单像素流式传输时，该模块返回单个像素作为标量布尔值。使用多像素流式传输时，该模块返回布尔值向量。此向量的大小与输入 **pixel** 向量相同。有关如何为多像素流式传输设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

**数据类型：** `Boolean`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于该向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于该向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### **Neighborhood** — 像素邻域 `[0,1,0; 1,1,1; 0,1,0]`（默认）| 由 `1` 和 `0` 组成的向量或矩阵

像素邻域，指定为由二进制值组成的向量或矩阵。

该模块支持最大 32×32 像素的邻域。要使用结构元素，请将 **Neighborhood** 参数设置为 `getnhood (Image Processing Toolbox)(strel (Image Processing Toolbox)(shape))`，其中 *`shape`* 由 `strel` (Image Processing Toolbox) 函数的输入参数指定。

使用多像素向量输入时，邻域在每个维度上必须至少为两个像素。

### **Line buffer size** — 行内存缓冲区大小 `2048`（默认）| 正整数

行内存缓冲区大小，指定为正整数。选择一个能够容纳水平行中活动像素数量的 2 的幂。如果指定的值不是 2 的幂，则缓冲区使用下一个最大的 2 的幂。

使用多像素输入时，此值必须容纳（**Active pixels per line**）/（**Number of pixels**）+ 2。

该模块分配 (*n* – 1)×**Line buffer size** 个内存位置来存储像素，其中 *n* 是 **Neighborhood** 参数值中的行数。

### **Padding method** — 填充边界的方法 `Constant`（默认）| `None`

选择以下方法之一来填充输入图像的边界。
有关这些方法的详细信息，请参阅 Edge Padding。

- `Constant` — 该模块在膨胀操作时用零填充图像，在腐蚀操作时用一填充图像。这些值可防止在活动帧的边界处发生开运算。
- `None` — 排除填充逻辑。该模块不会将图像帧之外的像素设置为任何特定值。此选项可减少模块使用的硬件资源以及帧之间所需的消隐时间，但会影响帧边缘处输出像素的准确性。为保持像素流时序，输出帧与输入帧大小相同。但是，为避免使用由未定义填充值计算出的像素，请在下游操作中屏蔽掉帧边缘周围 *KernelSize*/2 个像素。有关详细信息，请参阅 Increase Throughput by Omitting Padding。

## 所属库

Vision HDL Toolbox / Morphological Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果该模块位于 Resettable Synchronous Subsystem (HDL Coder) 内，则无法为其生成 HDL 代码。

## 版本历史

**在 R2015a 中引入**

### R2020a：省略填充的选项

现在可以将该模块配置为不在活动帧边界周围添加填充。此选项可减少模块使用的硬件资源以及帧之间所需的消隐时间，但会影响帧边缘处输出像素的准确性。要使用此选项，请将 **Padding method** 参数设置为 `None`。有关示例，请参阅 Increase Throughput by Omitting Padding。

### R2020a：多像素流

Opening 模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

对于多像素流，这些模块支持 4 或 8 个像素的输入和输出列向量。**ctrl** 端口仍为标量，`pixelcontrol` 总线中的控制信号适用于向量中的所有像素。

### R2018b：改进的行缓冲

此模块中的内部行缓冲现在可处理突发数据，即像素行内非连续的有效信号。由于改进了填充逻辑并原生支持具有偶数行数的核大小，此实现使用的硬件资源更少。此更改会影响 Line Buffer 模块以及使用内部行缓冲的模块。

对于某些配置，行缓冲的延迟现在减少几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳实践是使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

二值像素数据的形态学开运算

Opening 模块通过使用相同的邻域进行形态学腐蚀，然后进行形态学膨胀。该模块对二值强度值流进行操作。您可以指定最大为 32×32 像素的邻域或结构元素。

此模块使用带有帧控制信号总线的流式像素接口。此接口使模块能够独立于图像大小和格式进行操作。此模块上的 **pixel** 端口支持单像素流式传输或多像素流式传输。单像素流式传输每个时钟周期接受并返回一个像素值。多像素流式传输每个时钟周期接受并返回 *M* 个像素的向量，以支持高帧率或高分辨率格式。*M* 值对应于 Frame To Pixels 模块的 **Number of pixels** 参数。除像素外，该模块还接受并返回包含五个控制信号的 `pixelcontrol` 总线。控制信号指示每个像素的有效性及其在帧中的位置。对于多像素流式传输，一组控制信号适用于向量中的所有像素。要将帧（像素矩阵）转换为串行像素流和控制信号，请使用 Frame To Pixels 模块。有关该接口的完整描述，请参阅 Streaming Pixel Interface。
