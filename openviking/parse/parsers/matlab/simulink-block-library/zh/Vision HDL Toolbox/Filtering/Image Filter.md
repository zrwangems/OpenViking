---
type: simulink-block
title: 'Image Filter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'imagefilter'
documentation_source_path: 'ref/imagefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Filter

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

此模块支持单像素流或多像素流。对于单像素流，将单个输入像素指定为标量强度值。对于多像素流，指定包含两个、四个或八个像素强度值的向量。有关如何为多像素流设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

此模块不支持多分量流。要处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线是相同的，因此您可以将单个总线连接到多个复制的模块。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### **coeff** — 滤波器系数矩阵

将滤波器系数指定为数值的二维矩阵。矩阵的每个维度必须至少有 2 个元素，但不超过 64 个元素。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

该模块仅在帧开始时从 **coeff** 端口采样值，并忽略帧内的任何变化。

#### 依赖关系

要启用此端口，请将 **Filter coefficients source** 参数设置为 `Input port`。

**数据类型：** `int` | `uint` | `fixed point` | `single` | `double`
### 输出

### **pixel** — 输出像素流 标量 | 向量

输出像素流，以表示强度的标量值形式返回，或以包含两个、四个或八个像素强度值的向量形式返回。输出 **pixel** 端口的维度和数据类型与输入 **pixel** 端口的维度和数据类型匹配。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### 主要

### **Filter coefficients source** — 提供滤波器系数的来源 `Property`（默认）| `Input port`

选择用于指定滤波器系数的来源。

- `Property`（默认）— 使用此值通过 **Filter coefficients** 参数指定滤波器系数。
- `Input port` — 使用此值通过 **coeff** 输入端口指定滤波器系数。

### **Filter coefficients** — 滤波器系数 `[ 1, 0; 0, -1 ]`（默认）| 矩阵

将滤波器系数指定为矩阵。矩阵的每个维度必须至少有 2 个元素，但不超过 64 个元素。

#### 依赖关系

要启用此参数，请将 **滤波器系数来源** 参数设置为 `Property`。

### **填充方法** — 填充方法 `Constant`（默认）| `Replicate` | `Symmetric` | `Reflection` | `None`

选择以下方法之一来填充输入图像的边界。有关这些方法的详细信息，请参阅边缘填充。

- `Constant` — 将图像帧外的像素解释为具有常量值。
- `Replicate` — 重复图像边缘处像素的值。
- `Symmetric` — 将填充像素的值设置为镜像图像边缘。
- `Reflection` — 将填充像素的值设置为围绕图像边缘处像素进行反射。
- `None` — 排除填充逻辑。模块不会将图像帧外的像素设置为任何特定值。此选项可减少模块使用的硬件资源以及帧之间所需的消隐时间，但会影响帧边缘处输出像素的精度。为保持像素流时序，输出帧与输入帧大小相同。但是，为避免使用由未定义填充值计算出的像素，请在下游操作中屏蔽帧边缘周围 *KernelSize*/2 个像素。有关详细信息，请参阅通过省略填充提高吞吐量。

### **填充值** — 用于填充输入图像边界的值 `0`（默认）| 整数

指定一个整数来填充输入图像的边界。模块将此值转换为与输入像素相同的数据类型。

#### 依赖关系

要启用此参数，请将 **填充方法** 参数设置为 `Constant`。

### **行缓冲区大小** — 行缓冲区大小 `2048`（默认）| 整数

行内存缓冲区的大小，指定为正整数。选择一个能够容纳水平行中有效像素数量的 2 的幂。如果指定的值不是 2 的幂，缓冲区将使用下一个最大的 2 的幂。

使用多像素输入时，此值必须容纳（**每行有效像素数**）/（**像素数**）+ 2。

模块分配 (*N* – 1)×**行缓冲区大小** 个内存位置来存储像素。*N* 表示系数矩阵的行数。

### 数据类型

### **舍入模式** — 内部定点计算的舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定内部定点计算的舍入方法。

### **整数溢出时饱和** — 内部定点计算的溢出操作 `off`（默认）| `on`

当您清除此参数时，如果定点值和整数值溢出该数据类型可表示的范围，则回绕为零。当您选中此参数时，该值饱和为可表示的最大值。

### **系数** — 滤波器系数数据类型 `Inherit: Same as first input`（默认）| `fixdt(1,16,0)` | `<data type expression>`

选择确定滤波器系数数据类型的方法。

单击“显示数据类型助手”按钮以显示 **数据类型助手**，它可帮助您设置 **系数** 参数的数据类型。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

将系数转换为指定的数据类型时，模块会舍入到最接近的可表示值，如果该值超过该数据类型可表示的最大值，则饱和到最大值。

#### 依赖关系

要启用此参数，请将 **滤波器系数来源** 参数设置为 `Property`。

### **Output** — 输出数据类型 `Inherit: Same as first input`（默认）| `Inherit: Inherit via internal rule` | `fixdt(1,16,0)` | `<data type expression>`

选择确定输出像素数据类型的方法。

点击 Show data type assistant 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数的数据类型。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Lock data type settings against changes by the fixed-point tools** — 锁定数据类型设置 `off`（默认）| `on`

选择此参数以锁定此模块的所有数据类型设置，使其不受 Fixed-Point Tool 和 Fixed-Point Advisor 的更改。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Vision HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 规范有符号数字（CSD）或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果此模块位于 Resettable Synchronous Subsystem (HDL Coder) 内，则无法为其生成 HDL 代码。

## 版本历史

**在 R2015a 中引入**

### R2025a：在模块掩码上显示算法延迟

此模块现在在模块掩码上显示其延迟。延迟显示为行数和像素数。确切的时钟周期数取决于图像帧一行中的像素数以及输入像素有效模式。将显示的延迟信息与 `pixelcontrol` 总线信号一起使用，以对齐设计中的并行数据路径。

### R2022a：每时钟两像素流式传输

此模块现在支持每时钟周期 2 像素的多像素流。

### R2021b：反射填充

通过围绕边缘像素值进行反射来填充帧的边缘。此填充方法有助于减少边缘对比度效应，并可在保持原始帧大小的同时改善机器学习的结果。

### R2020a：省略填充的选项

您现在可以将模块配置为不在活动帧的边界周围添加填充。此选项可减少模块使用的硬件资源，并减少帧之间所需的消隐间隔，但会影响帧边缘处输出像素的精度。要使用此选项，请将 **Padding method** 参数设置为 `None`。有关示例，请参阅 Increase Throughput by Omitting Padding。

### R2019b：多像素流

该模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

对于多像素流，该模块支持 4 或 8 个像素的输入和输出列向量。**ctrl** 端口仍为标量，并且 `pixelcontrol` 总线中的控制信号应用于向量中的所有像素。

### R2019a：增大内核大小限制

该模块现在允许系数内核最多包含 64×64 个元素。

### R2018b：可编程系数

该模块现在可从输入端口接受系数。矩阵的每个维度必须至少有 2 个且不超过 16 个元素。该模块仅在帧开始时从 **coeff** 端口采样值，并忽略帧内的任何变化。

在以前的版本中，您可以指定系数行向量，即 1×N 个元素的矩阵。现在，系数矩阵在每个维度上必须至少有 2 个元素。

### R2018b：改进的行缓冲

该模块中的内部行缓冲现在可处理突发数据，即像素行内非连续的 valid 信号。由于改进了填充逻辑以及对具有偶数行数的内核大小的原生支持，此实现使用的硬件资源更少。此更改会影响 Line Buffer 模块以及使用内部行缓冲的模块。

对于某些配置，行缓冲的延迟现在减少几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳实践是使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

二维 FIR 滤波

Image Filter 模块对像素流执行二维有限脉冲响应（FIR）滤波，并支持使用可编程滤波器系数。
