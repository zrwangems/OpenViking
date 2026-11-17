---
type: simulink-block
title: 'Image Resizer'
family: 'geometric-transforms'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transforms'
documentation_page: 'imageresizer'
documentation_source_path: 'ref/imageresizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Resizer

## 端口

### 输入

### **pixel** — 输入像素流标量

单个像素，指定为标量值。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `fixdt(0,WL,0), WL between 8 and 16` | `double` | `single`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅像素控制总线。

**数据类型：** `bus`

### **inputSize** — 输入流中活动帧的尺寸 `[ActiveVideoLines,ActivePixelsPerLine]`

输入帧的尺寸，指定为 [*ActiveVideoLines*,*ActivePixelsPerLine*] 形式的行向量。这些尺寸必须是大于或等于 `[16,16]` 且小于或等于 `[4320,8192]` 的整数。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **输入尺寸来源** 参数设置为 `Input port`。

如果同时启用 **inputSize** 和 **outputSize** 端口，并且这些输入使用定点类型，则两个端口必须使用相同的定点类型。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `fixdt(0,WL,0), WL up to 16`

### **outputSize** — 输出流中活动帧的尺寸 `[ActiveVideoLines,ActivePixelsPerLine]`

输出帧的尺寸，指定为 [*ActiveVideoLines*,*ActivePixelsPerLine*] 形式的行向量。这些尺寸必须是大于或等于 `[16,16]` 且小于或等于 `[4320,8192]` 的整数。

输出尺寸必须小于或等于输入尺寸。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

#### 依赖关系

当将 **输出尺寸来源** 参数设置为 `Input port` 时，此端口出现。

如果同时启用 **inputSize** 和 **outputSize** 端口，并且这些输入使用定点类型，则两个端口必须使用相同的定点类型。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `fixdt(0,WL,0), WL up to 16`

### 输出

### **pixel** — 输出像素流标量

使用 **数据类型** 选项卡上的 **输出** 参数配置输出像素的数据类型。

**数据类型：** `uint8` | `uint16` | `fixdt(0,WL,0), WL between 8 and 16` | `double` | `single`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅像素控制总线。

**数据类型：** `bus`

## 参数

### 主要

### **输入高度和宽度** — 输入流中活动帧的尺寸 `[1080,1920]` (默认) | `[ActiveVideoLines,ActivePixelsPerLine]`

输入帧的尺寸，指定为 [*ActiveVideoLines*,*ActivePixelsPerLine*] 形式的行向量。这些尺寸必须是大于或等于 `[16,16]` 且小于或等于 `[4320,8192]` 的整数。

#### 依赖关系

当将 **输入尺寸来源** 参数设置为 `Property` 时，此参数出现。

### **输入尺寸来源** — 输入活动帧尺寸的来源 `Property` (默认) | `Input port`

输入活动帧尺寸的来源，指定为以下选项之一：

- `Property` — 使用 **输入高度和宽度** 参数指定输入尺寸。
- `Input port` — 使用 **inputSize** 输入端口指定输入尺寸。当输入控制总线中的 `vStart` 为 `true` 时，模块对 **inputSize** 和 **outputSize** 端口进行采样。

### **最大输入高度和宽度** — 可容纳最大预期输入尺寸的活动帧尺寸 `[1080,1920]` (默认) | `[ActiveVideoLines,ActivePixelsPerLine]`

最大预期输入帧的尺寸，指定为 [*ActiveVideoLines*,*ActivePixelsPerLine*] 形式的行向量。这些尺寸必须是大于或等于 `[16,16]` 且小于或等于 `[4320,8192]` 的整数。

#### 依赖关系

当将 **输入尺寸来源** 参数设置为 `Input port` 时，此参数出现。

### **输出高度和宽度** — 输出流中活动帧的尺寸 `[720,1280]` (默认) | `[ActiveVideoLines,ActivePixelsPerLine]`

输出帧的尺寸，指定为 [*ActiveVideoLines*,*ActivePixelsPerLine*] 形式的矩阵。这些尺寸必须是大于或等于 `[16,16]` 且小于或等于 `[4320,8192]` 的整数。

输出尺寸必须小于或等于输入尺寸。

#### 依赖关系

当将 **输出尺寸来源** 参数设置为 `Property` 时，此参数出现。

### **输出尺寸来源** — 输出活动帧尺寸的来源 `Property` (默认) | `Input port`

输出活动帧尺寸的来源，指定为以下选项之一：

- `Property` — 使用 **输出高度和宽度** 参数指定输出尺寸。
- `Input port` — 使用 **outputSize** 输入端口指定输出尺寸。当输入控制总线中的 `vStart` 为 `true` 时，模块对 **inputSize** 和 **outputSize** 端口进行采样。

### **最大输出高度和宽度** — 可容纳最大预期输出尺寸的活动帧尺寸 `[720, 1280]` (默认) | `[ActiveVideoLines,ActivePixelsPerLine]`

最大预期输出帧的尺寸，指定为 [*ActiveVideoLines*,*ActivePixelsPerLine*] 形式的行向量。这些尺寸必须是大于或等于 `[16,16]` 且小于或等于 `[4320,8192]` 的整数。

#### 依赖关系

当将 **输出尺寸来源** 参数设置为 `Input port` 时，此参数出现。

### **插入水平消隐** — 在活动行之间添加无效周期 off (默认) | on

水平消隐间隔是一行结束和下一行开始之间的非活动周期。选中此选项时，模块包含一个缓冲区，用于在输出视频流的活动行之间插入额外水平消隐周期时存储输出像素。在 **最小输出水平消隐** 参数中设置消隐周期数。有关何时使用水平消隐的信息，请参阅配置消隐间隔。

### **最小输出水平消隐** — 在输出行之间插入的非活动周期数 `370` (默认)

水平消隐间隔是一行结束和下一行开始之间的非活动周期。如果下游处理需要特定的消隐间隔，请在此参数中指定该间隔。此参数值必须是介于 `1` 和 `1195` 之间的整数。模块包含一个缓冲区，用于存储输出像素，直到达到最小消隐周期数。

对于使用行缓冲区的 Vision HDL Toolbox 库模块，建议的最小水平消隐间隔是：使用填充时为 2×*Kw*，或者当将 **填充方法** 参数设置为 `None` 时为 12 个周期。有关图像处理系统消隐要求的更多信息，请参阅配置消隐间隔。

#### 依赖关系

要启用此参数，请选择 **插入水平消隐**。

### **插值方法** — 插值像素值的方法 `Bilinear` (默认) | `Nearest Neighbor`

在水平和垂直方向上插值像素值的方法，指定为以下类型之一：

- `Bilinear` — 模块在每个方向上实现一个双抽头滤波器，其中抽头为当前像素值和前一个像素值。
- `Nearest Neighbor` — 该对象实现多路复用器，以选择当前像素值或前一个像素值中最接近的值。此插值方法使用的硬件资源最少，但代价是插值精度较粗。

有关插值方法的更多信息，请参阅 Change Image Size 示例。

插值精度比较

### **在下采样时执行抗锯齿** — 在调整尺寸前应用抗锯齿滤波器 on (默认) | off

当将此属性设置为 `true` 时，该对象会在调整尺寸操作之前对输入图像应用抗锯齿滤波器。抗锯齿滤波器是可分离的 5×5 滤波器。系数为 `[1 4 6 4 1]/16`。

### 数据类型

### **舍入模式** — 内部定点计算的舍入方法 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定内部定点计算的舍入方法。

### **整数溢出时饱和** — 内部定点计算的溢出操作 `off` (默认) | `on`

清除此参数时，当值溢出该数据类型可表示的范围时，定点值和整数值会回绕到零。选中此参数时，值会饱和到最大可表示值。

### **系数** — 插值滤波器系数的数据类型 `fixdt(0,16)` (默认) | `<data type expression>`

将滤波器系数的数据类型指定为 `fixdt(0,WL)` 形式的数据类型表达式，其中类型为无符号，*WL* 是范围为 2 到 17 的字长。模块会计算二进制小数点定标，以适配插值系数。将系数转换为指定的数据类型时，模块使用 **舍入模式** 和 **溢出操作** 参数的设置。

插值滤波器还会将内部像素数据类型限制为 24 位宽，以便滤波器映射到 FPGA 上的 DSP 模块。

### **输出** — 输出数据类型 `Inherit: Same as first input` (默认) | `fixdt(0,16,0)` | `<data type expression>`

将输出像素的数据类型指定为 `Inherit: Same as first input`，或指定为 `fixdt(0,WL,0)` 形式的数据类型表达式，其中类型为无符号，*WL* 是范围为 8 到 16 的字长。

- `Inherit: Same as first input` — 将输出像素的数据类型设置为与输入 **pixel** 端口的数据类型匹配。
- `<data type expression>` — 将输出像素的数据类型设置为此数据类型。

将像素值转换为指定的数据类型时，模块使用 **舍入模式** 和 **溢出操作** 参数的设置。

## 所属库

Vision HDL Toolbox / Geometric Transforms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2023a 中引入**

## 描述

更改像素流中图像的尺寸

Image Resizer 模块对灰度输入图像进行下采样。水平和垂直缩放因子相互独立，您可以选择实时指定输入和输出尺寸。该模块提供可选的抗锯齿滤波器，您可以选择最近邻或双线性插值。

您可以将此模块用于图像调整尺寸操作，例如：

- 将图像转换为统一尺寸，以输入到深度学习算法
- 修改不同的源视频，以满足处理、资源或显示要求
