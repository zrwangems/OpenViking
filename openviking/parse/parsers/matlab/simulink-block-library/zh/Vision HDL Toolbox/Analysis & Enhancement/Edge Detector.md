---
type: simulink-block
title: 'Edge Detector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'edgedetector'
documentation_source_path: 'ref/edgedetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Edge Detector

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

此模块支持单像素流或多像素流。
对于单像素流，将单个输入像素指定为标量强度值。对于多像素流，指定包含两个、四个或八个像素强度值的向量。有关如何为多像素流设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

此模块不支持多分量流。要处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线是相同的，因此您可以将单个总线连接到多个复制的模块。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量有一组控制信号。
由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### **Th** — 阈值 标量

定义边缘的阈值，指定为标量。该模块将此值的平方与梯度平方和进行比较。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int` | `uint` | `fixed point`
### 输出

### **Edge** — 布尔像素值，指示像素是否为边缘 标量 | 向量

对于单像素流，**Edge** 是布尔标量。对于多像素流，**Edge** 是 *M*×1 布尔值向量。每个像素值指示该像素是否为边缘。

**数据类型：** `Boolean`

### **Gv,Gh** — 垂直和水平梯度 标量 | 向量

在以像素位置为中心的核上计算的垂直和水平梯度值。

对于单像素流，该模块将 **Gv** 和 **Gh** 返回为标量值。对于多像素流，该模块将 **Gv** 和 **Gh** 返回为 *M*×1 值的向量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用这些端口，请将 **Method** 设置为 `Sobel` 或 `Prewitt`。

**数据类型：** `single` | `double` | `int` | `uint` | `fixed point`

### **G45,G135** — 正交梯度 标量 | 向量

在以像素位置为中心的核上计算的正交梯度值。

对于单像素流，该模块将 **G45** 和 **G135** 返回为标量值。对于多像素流，该模块将 **G45** 和 **G135** 返回为 *M*×1 值的向量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用这些端口，请将 **Method** 设置为 `Roberts`。

**数据类型：** `single` | `double` | `int` | `uint` | `fixed point`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流传输，每个像素值向量都有一组控制信号。
由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和
`vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### 主

### **Method** — 边缘检测算法 `Sobel`（默认）| `Prewitt` | `Roberts`

当您选择 `Sobel` 或
`Prewitt` 时，该模块计算水平和垂直梯度 `Gv` 和 `Gh`。
当您选择 `Roberts` 时，该模块计算正交梯度 `G45` 和
`G135`。有关每种方法的详细信息，请参阅算法。

**注意**

如果您选择 `Prewitt`，由于 1/6 系数，全精度内部数据类型会很大。请考虑选择 **Output the gradient
components**，以便您可以将数据类型自定义为更小的尺寸。

### **Output the binary image** — 启用边缘输出端口 on（默认）| off

选中此参数后，该模块返回表示输入帧中检测到的边缘的二值像素流。

您必须至少选择 **Output the binary
image** 和 **Output the gradient
components** 中的一个。

### **Output the gradient components** — 启用梯度输出端口 off（默认）| on

选中此参数后，该模块返回表示每个像素处沿两个正交方向计算出的梯度的值流。当您将 **Method** 设置为
`Sobel` 或
`Prewitt` 时，输出端口
**Gv** 和 **Gh** 会出现在该模块上。当您将 **Method** 设置为
`Roberts` 时，输出端口
**G45** 和 **G135** 会出现在该模块上。

您必须至少选择 **Output the binary
image** 和 **Output the gradient
components** 中的一个。

### **Source of threshold value** — 表示边缘的梯度阈值来源 `Property`（默认）| `Input port`

您可以从输入端口或对话框设置阈值。
默认值为 `Property`。选择
`Input port` 会启用
**Th** 端口。

### **Threshold value** — 表示边缘的梯度阈值 `20`（默认）| 标量

该模块将此值的平方与梯度平方和进行比较。该模块将此值转换为梯度的数据类型。

#### 依赖关系

当您将 **Source of threshold
value** 设置为 `Property` 时，此选项可见。

### **Line buffer size** — 行内存缓冲区大小 `2048`（默认）| 整数

行内存缓冲区大小，指定为正整数。请选择能够容纳一条水平行中有效像素数量的 2 的幂。如果您指定的值不是 2 的幂，则缓冲区将使用下一个最大的 2 的幂。

当您使用多像素输入时，此值必须容纳（**Active pixels per line**）/（**Number of pixels**）+ 2。

该模块分配 (*N – 1*)×**Line
buffer size** 个内存位置来存储像素，其中
*N* 是差分近似矩阵中的行数。如果您将 **Method** 设置为
`Sobel` 或
`Prewitt`，则 *N* 为 3。
如果您将 **Method** 设置为
`Roberts`，则 *N* 为
2。

### **Padding method** — 边界填充方法 `Symmetric`（默认）| `None`

选择以下方法之一来填充输入图像的边界。有关这些方法的详细信息，请参阅 Edge Padding。

- `Symmetric` — 将填充像素的值设置为镜像图像边缘。此选项可防止在活动帧的边界处检测到边缘。
- `None` — 排除填充逻辑。该模块不会将图像帧外的像素设置为任何特定值。此选项可减少模块使用的硬件资源以及帧之间所需的消隐时间，但会影响帧边缘处输出像素的准确性。为保持像素流时序，输出帧与输入帧大小相同。但是，为避免使用由未定义填充值计算出的像素，请在下游操作中屏蔽帧边缘周围的 *KernelSize*/2 个像素。有关详细信息，请参阅 Increase Throughput by Omitting Padding。

### 数据类型

### **Rounding mode** — 内部定点计算的舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定内部定点计算的舍入方法。

### **Saturate on integer overflow** — 内部定点计算的溢出操作 `off`（默认）| `on`

当您清除此参数时，如果定点值和整数值溢出该数据类型可表示的范围，则回绕为零。当您选中此参数时，该值饱和为最大可表示值。

### **Gradient Data Type** — 梯度输出端口的数据类型 `Inherit via internal rule`（默认）| 数据类型表达式

两个梯度输出端口的数据类型。默认情况下，该模块自动选择全精度数据类型。

#### 依赖关系

要启用此参数，请在 **Main** 选项卡上选择 **Output the gradient components**。

## 所属库

Vision HDL Toolbox / Analysis & Enhancement

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL Architecture**

此模块具有一个默认 HDL 架构。

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**Restrictions**

您无法在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2015a 中引入**

### R2023a: Two pixels-per-clock streaming

该模块现在支持每时钟周期 2 个像素的多像素流。

### R2020a：省略填充的选项

现在，您可以将该模块配置为不在活动帧的边界周围添加填充。此选项可减少模块使用的硬件资源以及帧之间所需消隐，但会影响帧边缘处输出像素的精度。要使用此选项，请将 **Padding method** 参数设置为 `None`。有关示例，请参阅通过省略填充提高吞吐量。

### R2019b：多像素流

Edge Detector 模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

对于多像素流，该模块支持 4 或 8 个像素的输入和输出列向量。**ctrl** 端口仍为标量，并且 `pixelcontrol` 总线中的控制信号适用于该向量中的所有像素。

### R2018b：改进的行缓冲

此模块中的内部行缓冲现在可处理突发数据，即像素行内非连续的有效信号。由于改进了填充逻辑，并且原生支持具有偶数行数的内核大小，此实现使用的硬件资源更少。此更改会影响 Line Buffer 模块以及使用内部行缓冲的模块。

对于某些配置，行缓冲的延迟现在减少几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳实践是使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

查找灰度像素流中对象的边缘

Edge Detector 模块通过使用 Sobel、Prewitt 或 Roberts 方法查找灰度像素流中的边缘。该模块将输入像素与导数近似矩阵进行卷积，以沿两个正交方向查找像素幅度的梯度。然后，它将梯度的平方和与可配置阈值的平方进行比较，以确定这些梯度是否表示边缘。

默认情况下，该模块返回二值图像作为像素值流。像素值为 1 表示该像素是边缘。您可以禁用边缘输出。您还可以启用每个像素处两个正交方向上的梯度值输出。
