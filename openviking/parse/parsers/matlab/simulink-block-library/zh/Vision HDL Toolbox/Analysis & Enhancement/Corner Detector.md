---
type: simulink-block
title: 'Corner Detector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'cornerdetector'
documentation_source_path: 'ref/cornerdetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Corner Detector

## 端口

### 输入

### **pixel** — 输入像素流标量

像素流中的单个图像像素，指定为表示灰度强度的标量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`

### **minC** — 指示 FAST 算法角点的阈值 非负整数

指示 FAST 算法角点的阈值，指定为非负整数。圆中的每个像素减去中心像素值，只有超过此阈值的差值才用于确定中心像素是否为角点并计算输出度量。此值被转换为与输入 **pixel** 相同的数据类型。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Method** 参数设置为某个 FAST 选项，并将 **Source of minimum contrast value** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint` | `fixed point`

### **thresh** — 指示 Harris 算法角点的阈值 非负整数

指示 Harris 算法角点的阈值，指定为非负整数。此值表示根据梯度结果计算的 Harris 矩阵特征值的近似值。该模块为特征值度量超过此阈值的像素返回角点。此值被转换为与输出 **pixel** 相同的数据类型。角点度量的范围是输入像素值的四次方。例如，对于 8 位输入像素，全精度输出大小为 44 位。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Method** 参数设置为 `Harris`，并将 **Source of threshold value** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint` | `fixed point`
### 输出

### **corner** — 指示像素是否为角点的度量 标量

指示像素是否为角点的度量，返回为由 **Output** 数据类型参数指定的数值类型的标量。当像素不是角点时，该模块为此值返回零。

对于使用 FAST 算法检测到的角点，此值是通过使用圆周围像素与中心像素值的绝对差之和（SAD）计算的对比度度量。该度量仅包含超过阈值的差值。

对于使用 Harris 算法检测到的角点，此值是根据梯度结果计算的 Harris 矩阵特征值的近似值。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`

## 参数

### 主要

### **Method** — 检测方法 `FAST 5 of 8`（默认）| `FAST 7 of 12` | `FAST 9 of 16` | `Harris`

选择 Harris 算法，或 FAST 算法的圆尺寸。三个 FAST 选项指定圆上有多少个连续像素必须超过阈值，中心像素才会被标记为角点。对于这些图中所示的 8、12 和 16 像素圆，当分别有 5、7 或 9 个连续像素高于阈值时，模块检测到角点。模块检查圆上任意位置是否存在该数量的连续像素。模块对 `FAST 5 of 8` 使用 3×3 大小的核，对 `FAST 7 of 12` 使用 5×5，对 `FAST 9 of 16` 使用 7×7。

三种核尺寸及中心像素周围像素圆的示意图。

### **Source of minimum contrast value** — FAST 算法中指示角点的阈值来源 `Property`（默认）| `Input port`

指定 `Property` 以通过 **MinContrast value** 参数设置阈值。指定 `Input port` 以启用 **minC** 端口。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为某个 FAST 选项。

### **MinContrast value** — FAST 算法中指示角点的阈值 `20`（默认）| 非负整数

将圆中的每个像素与中心像素值相减，只有超过此阈值的差值才用于确定中心像素是否为角点，并用于计算输出度量。此值会被转换为与输入 **pixel** 相同的数据类型。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为某个 FAST 选项，并将 **Source of minimum contrast value** 参数设置为 `Property`。

### **Source of threshold value** — Harris 算法中指示角点的阈值来源 `Property`（默认）| `Input port`

指定 `Property` 以通过 **Threshold value** 参数设置阈值。指定 `Input port` 以启用 **thresh** 端口。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为 `Harris`。

### **Threshold value** — Harris 算法中指示角点的阈值 `2000`（默认）| 非负整数

此值表示根据梯度结果计算出的 Harris 矩阵特征值的近似值。对于度量超过此阈值的像素，模块返回角点。有关详细信息，请参阅 Harris Corner Detection 示例。此值会被转换为与输出 **corner** 相同的数据类型。角点度量的范围是输入像素值的四次方。例如，对于 8 位输入像素，全精度输出大小为 44 位。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为 `Harris`，并将 **Source of threshold value** 参数设置为 `Property`。

### **Line buffer size** — 行缓冲区大小 `2048`（默认）| 整数

行内存缓冲区的大小，指定为正整数。请选择能够容纳水平行中活动像素数量的 2 的幂。如果指定的值不是 2 的幂，则缓冲区使用下一个最大的 2 的幂。

模块分配 (*N* – 1)×**Line buffer size** 个内存位置来存储像素。*N* 是核的大小。

当 **Method** 参数为 `FAST 5 of 8` 时，模块使用 3×3 大小的核；当 **Method** 为 `FAST 7 of 12` 时使用 5×5；当 **Method** 为 `FAST 9 of 16` 时使用 7×7。

当将 **Method** 设置为 `Harris` 时，模块使用一个 1×3 核和一个 3×1 核进行梯度计算，并使用三个 5×5 核对三个梯度分量进行圆形窗口滤波。

### **Padding method** — 边界填充方法 `Symmetric`（默认）| `Replicate` | `Reflection` | `None`

选择以下方法之一来填充输入图像的边界。有关这些方法的详细信息，请参阅 Edge Padding。

- `Replicate` — 重复图像边缘像素的值。
- `Symmetric` — 将填充像素的值设置为图像边缘的镜像。此选项可防止在活动帧的边界处检测到边缘。
- `Reflection` — 将填充像素的值设置为围绕图像边缘像素的反射。
- `None` — 排除填充逻辑。模块不会将图像帧外的像素设置为任何特定值。此选项可减少模块使用的硬件资源以及帧之间所需的消隐时间，但会影响帧边缘处输出像素的精度。为保持像素流时序，输出帧与输入帧大小相同。但是，为避免使用由未定义填充值计算出的像素，请在下游操作中屏蔽帧边缘周围 *KernelSize*/2 个像素。有关详细信息，请参阅 Increase Throughput by Omitting Padding。

Harris 算法中使用的圆形窗口滤波器使用 `Replicate` 填充来填充帧的边缘。

### 数据类型

### **Rounding mode** — 内部定点计算的舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定内部定点计算的舍入方法。

### **Saturate on integer overflow** — 内部定点计算的溢出操作 `off`（默认）| `on`

当您清除此参数时，如果定点值和整数值溢出该数据类型可表示的范围，则回绕为零。当您选中此参数时，该值饱和为最大可表示值。

### **Output** — **corner** 输出端口的数据类型 `Inherit same as first input`（默认）| 数据类型表达式 | `Inherit via internal rule`

指定输出 **corner** 端口的数据类型。默认情况下，模块使用与输入 **pixel** 端口相同的数据类型返回角点度量。

## 所属库

Vision HDL Toolbox / Analysis & Enhancement

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink 加速器和快速加速器模式的 C/C++ 代码生成，以及 DPI 组件生成。

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

## 版本历史

**在 R2020a 中引入**

### R2021b: Reflection padding

通过围绕边缘像素值进行反射来填充帧的边缘。此填充方法有助于减少边缘对比度效应，并可在保持原始帧大小的同时改善机器学习的结果。

### R2020b: Harris 角点检测

该模块现在提供在 FAST 算法与 Harris 和 Stephens 互连边缘算法之间进行选择。请参阅 Harris 角点检测。

### R2020a: 省略填充的选项

您现在可以将该模块配置为不在活动帧的边界周围添加填充。此选项可减少该模块使用的硬件资源以及帧之间所需消隐，但会影响帧边缘处输出像素的精度。要使用此选项，请将 **Padding method** 参数设置为 `None`。有关示例，请参阅通过省略填充提高吞吐量。

## 描述

使用 FAST 或 Harris 算法查找角点

Corner Detector 模块通过使用加速分段测试特征（FAST）算法或相交边缘（Harris）算法来检测角点。对于每个像素，如果该像素是角点，则该模块返回角点度量。如果该像素不是角点，则该模块返回像素值零。

FAST 算法测试角点潜在中心周围的圆形区域。如果一段连续像素要么比中心加阈值更亮，要么比中心减阈值更暗，则该测试会检测到角点。您可以将最小对比度阈值指定为参数或端口，并从三种规则中选择一种来定义角点。这些规则指定在像素圆中有多少像素必须超过最小对比度，中心像素才被视为角点。该模块对圆周围连续像素的所有组合执行并行测试。FAST 使用的硬件资源非常少

Harris 算法计算水平和垂直梯度，使用圆形 5×5 高斯滤波器对梯度分量进行滤波，并计算表示角点强度的度量。您可以指定一个阈值，该阈值决定检测角点的水平。对于度量超过此阈值的像素，该模块返回角点。Harris 算法比 FAST 算法使用更多硬件资源，但可以检测 FAST 算法可能找不到的角点。
