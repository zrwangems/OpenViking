---
type: simulink-block
title: 'Bilateral Filter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'bilateralfilter'
documentation_source_path: 'ref/bilateralfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Bilateral Filter

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

此模块支持单像素流或多像素流。
对于单像素流，将单个输入像素指定为标量强度值。对于多像素流，指定包含两个、四个或八个像素强度值的向量。有关如何为多像素流设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

此模块不支持多分量流。要处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线是相同的，因此您可以将单个总线连接到多个复制模块。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量有一组控制信号。
由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`
### 输出

### **pixel** — 输出像素流 标量 | 向量

输出像素流，以表示强度的标量值形式返回，或以包含两个、四个或八个像素强度值的向量形式返回。
输出 **pixel** 端口的维度和数据类型与输入 **pixel** 端口的维度和数据类型匹配。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量有一组控制信号。
由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### 主

### **Neighborhood size** — 用于求平均的图像区域大小 `3×3`（默认）| `5×5` | `7×7` | `9×9` | `11×11` | `13×13` | `15×15`

用于计算平均值的图像区域大小，指定为 *N*×*N* 像素正方形。

### **Spatial standard deviation** — 空间标准差目标 `0.5`（默认）| 正实数

用于计算空间高斯滤波器系数的空间标准差目标，指定为正实数。此参数没有限制，但推荐值为 0.1 到 10。在高值时，分布变得平坦且系数较小。在低值时，分布在中心达到峰值，邻域其余部分的系数较小。这些边界值还取决于邻域大小和用于系数的数据类型。

### **Intensity standard deviation** — 强度标准差目标 `0.5`（默认）| 正实数

用于计算强度高斯滤波器系数的强度标准差目标，指定为正实数。该参数没有限制，但推荐值为 0.1 到 10。在高值时，分布变得平坦且系数较小。在低值时，分布集中在中心，邻域其余部分的系数较小。这些边界值还取决于邻域大小和用于系数的数据类型。

当强度标准差较大时，双边滤波器更像高斯模糊滤波器，因为强度高斯的峰值较低。相反，当强度标准差较小时，强度中的边缘会被保留或增强。

### **Padding method** — 填充输入图像边界的方法 `Constant`（默认）| `Replicate` | `Symmetric` | `Reflection` | `None`

选择以下方法之一来填充输入图像的边界。有关这些方法的详细信息，请参阅 Edge Padding。

- `Constant` — 将图像帧外的像素解释为具有常量值。
- `Replicate` — 重复图像边缘处像素的值。
- `Symmetric` — 将填充像素的值设置为镜像图像边缘。
- `Reflection` — 将填充像素的值设置为围绕图像边缘处像素反射。
- `None` — 排除填充逻辑。该模块不会将图像帧外的像素设置为任何特定值。此选项可减少模块使用的硬件资源以及帧之间所需消隐，但会影响帧边缘处输出像素的精度。为保持像素流时序，输出帧与输入帧大小相同。但是，为避免使用由未定义填充值计算出的像素，请在下游操作中屏蔽帧边缘周围 *KernelSize*/2 个像素。有关详细信息，请参阅 Increase Throughput by Omitting Padding。

### **Padding value** — 用于填充输入图像边界的值 `0`（默认）| 整数

指定一个整数来填充输入图像的边界。该模块将此值转换为与输入像素相同的数据类型。

#### 依赖关系

要启用此参数，请将 **Padding method** 参数设置为 `Constant`。

### **Line buffer size** — 行内存缓冲区大小 `2048`（默认）| 正整数

行内存缓冲区大小，指定为正整数。选择一个能够容纳水平行中有效像素数量的 2 的幂。如果指定的值不是 2 的幂，则缓冲区使用下一个最大的 2 的幂。

使用多像素输入时，此值必须容纳（**Active pixels per line**）/（**Number of pixels**）+ 2。

### 数据类型

### **Rounding mode** — 内部定点计算的舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

为内部定点计算指定舍入方法。

### **Saturate on integer overflow** — 内部定点计算的溢出模式 on（默认）| off

当输入为任何整数或定点数据类型时，算法在内部计算中使用定点运算。默认情况下，定点值在溢出时饱和。当输入数据类型为 `single` 或 `double` 时，此选项不适用。

### **Coefficients** — 确定滤波器系数数据类型的方法 `Inherit: Same as first input`（默认）| `fixdt(1,16,0)` | 数据类型表达式

指定一个可表示小于 1 的值的无符号数据类型。
系数通常需要比输入数据类型具有更高精度的数据类型。该模块根据邻域大小以及 **Intensity standard
deviation** 和 **Spatial standard
deviation** 的值来计算系数。较大的邻域会使高斯函数分布更广，从而使每个系数值更小。较大的标准差会使高斯函数更平坦，使系数在性质上更加均匀，而较小的标准差会产生尖峰响应。

**注意**

如果您尝试某种数据类型，并且在量化之后超过一半的系数变为零，该模块会发出警告。如果量化之后所有系数均为零，该模块会发出错误。
这些消息意味着该模块无法使用指定的数据类型来表达所请求的滤波器。为避免此问题，请选择更高精度的系数数据类型或调整标准差目标。

### **Output** — 确定输出像素数据类型的方法 `Inherit: Same as first input`（默认）| `fixdt(1,16,0)` | 数据类型表达式

滤波后的像素值会被转换为该数据类型。

## 所属库

Vision HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink accelerator 和 rapid accelerator 模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017b 中引入**

### R2022a: 多像素流式传输

Bilateral Filter 模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

该模块支持包含 *NumPixels* 个值的输入列向量，其中 *NumPixels* 可以为 2、4 或 8。**ctrl**
端口仍为标量，并且 `pixelcontrol`
总线中的控制信号应用于矩阵中的所有像素。该模块返回与输入向量大小相同的输出向量。

### R2021b: 反射填充

通过围绕边缘像素值进行反射来填充帧边缘。此填充方法有助于减少边缘对比度效应，并可在保持原始帧大小的同时改善机器学习结果。

### R2020a: 省略填充的选项

您现在可以将该模块配置为不在活动帧边界周围添加填充。此选项可减少该模块使用的硬件资源以及帧之间所需消隐，但会影响帧边缘处输出像素的精度。要使用此选项，请将 **Padding
method** 参数设置为 `None`。有关示例，请参阅 Increase Throughput by Omitting Padding。

### R2018b：改进的行缓冲

此模块中的内部行缓冲现在可处理突发数据，即像素行内非连续的有效信号。由于改进了填充逻辑以及对具有偶数行数的内核尺寸的原生支持，此实现使用更少的硬件资源。此更改会影响 Line Buffer 模块以及使用内部行缓冲的模块。

对于某些配置，行缓冲的延迟现在减少几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳实践是使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

二维双边滤波

Bilateral Filter 模块在保留边缘的同时对图像进行滤波。双边滤波的一些应用包括在保留边缘的同时去噪、将纹理与光照分离，以及通过卡通化增强边缘。该滤波器使用空间高斯滤波器和强度高斯滤波器计算出的平均值来替换邻域中心的每个像素。该模块根据以下内容确定滤波器系数：

- 邻域中的空间位置（类似于高斯模糊滤波器）
- 与邻域中心值的强度差

该模块提供两个标准差参数，用于独立控制空间系数和强度系数。
