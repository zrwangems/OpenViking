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

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅像素控制总线。

**数据类型：** `bus`

### **minC** — 用于 FAST 算法的指示角点的阈值 非负整数

用于 FAST 算法的指示角点的阈值，指定为非负整数。将圆周上的每个像素与中心像素值相减，只有超过此阈值的差值才用于确定中心像素是否为角点，并用于计算输出度量。此值会转换为与输入 **pixel** 相同的数据类型。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Method** 参数设置为某个 FAST 选项，并将 **Source of minimum contrast value** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint` | `fixed point`

### **thresh** — 用于 Harris 算法的指示角点的阈值 非负整数

用于 Harris 算法的指示角点的阈值，指定为非负整数。此值表示根据梯度结果计算得到的 Harris 矩阵特征值的近似值。对于特征值度量超过此阈值的像素，该模块会返回角点。此值会转换为与输出 **pixel** 相同的数据类型。角点度量的范围是输入像素值的四次方。例如，对于 8-bit 输入像素，全精度输出大小为 44 bits。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Method** 参数设置为 `Harris`，并将 **Source of threshold value** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint` | `fixed point`

### 输出

### **corner** — 指示像素是否为角点的度量 标量

指示像素是否为角点的度量，以 **Output** 数据类型参数指定的数值类型的标量形式返回。当像素不是角点时，该模块对此值返回零。

对于使用 FAST 算法检测到的角点，此值是通过对圆周上的像素与中心像素值使用绝对差和（SAD）计算得到的对比度度量。该度量仅包含超过阈值的那些差值。

对于使用 Harris 算法检测到的角点，此值是根据梯度结果计算得到的 Harris 矩阵特征值的近似值。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅像素控制总线。

**数据类型：** `bus`

## 参数

### 主要

### **Method** — 检测方法 `FAST 5 of 8`（默认） | `FAST 7 of 12` | `FAST 9 of 16` | `Harris`

选择 Harris 算法，或选择 FAST 算法的圆的大小。三个 FAST 选项指定圆周上必须有连续多少个像素超过阈值，中心像素才会被标记为角点。对于这些图中所示的 8、12 和 16 个像素的圆，当分别有 5、7 或 9 个连续像素高于阈值时，该模块会检测到一个角点。该模块会在圆周上的任意位置检查此数量的连续像素。对于 `FAST 5 of 8`，该模块使用大小为 3-by-3 的内核；对于 `FAST 7 of 12`，使用 5-by-5；对于 `FAST 9 of 16`，使用 7-by-7。

三种大小的内核及围绕中心像素的像素圆的示意图。

### **Source of minimum contrast value** — 用于 FAST 算法的指示角点阈值的来源 `Property`（默认） | `Input port`

指定 `Property` 以使用 **MinContrast value** 参数设置阈值。指定 `Input port` 以启用 **minC** 端口。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为某个 FAST 选项。

### **MinContrast value** — 用于 FAST 算法的指示角点的阈值 `20`（默认） | 非负整数

将圆周上的每个像素与中心像素值相减，只有超过此阈值的差值才用于确定中心像素是否为角点，并用于计算输出度量。此值会转换为与输入 **pixel** 相同的数据类型。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为某个 FAST 选项，并将 **Source of minimum contrast value** 参数设置为 `Property`。

### **Source of threshold value** — 用于 Harris 算法的指示角点阈值的来源 `Property`（默认） | `Input port`

指定 `Property` 以使用 **Threshold value** 参数设置阈值。指定 `Input port` 以启用 **thresh** 端口。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为 `Harris`。

### **Threshold value** — 用于 Harris 算法的指示角点的阈值 `2000`（默认） | 非负整数

此值表示根据梯度结果计算得到的 Harris 矩阵特征值的近似值。对于度量超过此阈值的像素，该模块会返回角点。有关详细信息，请参阅 Harris 角点检测示例。此值会转换为与输出 **corner** 相同的数据类型。角点度量的范围是输入像素值的四次方。例如，对于 8-bit 输入像素，全精度输出大小为 44 bits。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为 `Harris`，并将 **Source of threshold value** 参数设置为 `Property`。

### **Line buffer size** — 行缓冲区大小 `2048`（默认） | 整数

行内存缓冲区的大小，指定为正整数。请选择能够容纳一条水平线上有效像素数量的 2 的幂。如果指定的值不是 2 的幂，则该缓冲区使用下一个最大的 2 的幂。

该模块分配 (*N*  – 1)-by-**Line buffer size** 个内存位置来存储像素。*N* 是内核的大小。

当 **Method** 参数为 `FAST 5 of 8` 时，该模块使用大小为 3-by-3 的内核；当 **Method** 为 `FAST 7 of 12` 时，使用 5-by-5；当 **Method** 为 `FAST 9 of 16` 时，使用 7-by-7。

当将 **Method** 设置为 `Harris` 时，该模块使用一个 1-by-3 内核和一个 3-by-1 内核进行梯度计算，并使用三个 5-by-5 内核来对三个梯度分量进行圆形窗口滤波。

### **Padding method** — 填充方法 `Symmetric`（默认） | `Replicate` | `Reflection` | `None`

选择以下方法之一来填充输入图像的边界。有关这些方法的更多信息，请参阅边缘填充。

- `Replicate` — 重复图像边缘处像素的值。
- `Symmetric` — 将填充像素的值设置为镜像图像边缘。此选项可防止在有效帧的边界处检测到边缘。
- `Reflection` — 将填充像素的值设置为围绕图像边缘处的像素进行反射。
- `None` — 排除填充逻辑。该模块不会将图像帧之外的像素设置为任何特定值。此选项可减少该模块使用的硬件资源以及帧之间所需的消隐，但会影响帧边缘处输出像素的精度。为保持像素流时序，输出帧与输入帧大小相同。但是，为避免使用根据未定义填充值计算出的像素，请为下游操作屏蔽掉帧边缘周围的 *KernelSize*/2 个像素。有关详细信息，请参阅通过省略填充提高吞吐量。

Harris 算法中使用的圆形窗口滤波器使用 `Replicate` 填充来填充帧的边缘。

### 数据类型

### **Rounding mode** — 内部定点计算的舍入方法 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定内部定点计算的舍入方法。

### **Saturate on integer overflow** — 内部定点计算的溢出操作 `off`（默认） | `on`

清除此参数时，当值溢出该数据类型可表示的范围时，定点和整数值会回绕到零。选择此参数时，值会在最大可表示值处饱和。

### **Output** — **corner** 输出端口的数据类型 `Inherit same as first input`（默认） | 数据类型表达式 | `Inherit via internal rule`

指定输出 **corner** 端口的数据类型。默认情况下，该模块使用与输入 **pixel** 端口相同的数据类型返回角点度量。

## 所属库

Vision HDL Toolbox / Analysis & Enhancement

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2020a 中引入**

### R2021b：Reflection 填充

通过围绕边缘像素值进行反射来填充帧的边缘。此填充方法有助于减少边缘对比度效应，并可在保持原始帧大小的同时改善机器学习结果。

### R2020b：Harris 角点检测

该模块现在提供 FAST 算法与 Harris and Stephens 互连边缘算法之间的选择。请参阅 Harris 角点检测。

### R2020a：省略填充的选项

现在可以将该模块配置为不在有效帧的边界周围添加填充。此选项可减少该模块使用的硬件资源以及帧之间所需的消隐，但会影响帧边缘处输出像素的精度。要使用此选项，请将 **Padding method** 参数设置为 `None`。有关示例，请参阅通过省略填充提高吞吐量。

## 描述

使用 FAST 或 Harris 算法查找角点

Corner Detector 模块使用 features-from-accelerated-segment test (FAST) 算法或 intersecting edges (Harris) 算法检测角点。对于每个像素，如果该像素是角点，则该模块返回角点度量。如果该像素不是角点，则该模块返回像素值零。

FAST 算法会测试角点潜在中心周围的圆形区域。如果一段连续像素要么比中心加上阈值更亮，要么比中心减去阈值更暗，则该测试会检测到角点。您可以将最小对比度阈值指定为参数或端口，并从三种规则中选择来定义角点。这些规则指定像素圆中有多少个像素必须超过最小对比度，中心像素才会被视为角点。该模块会并行测试圆周上连续像素的所有组合。FAST 使用的硬件资源非常少

Harris 算法计算水平和垂直梯度，使用圆形 5-by-5 高斯滤波器对梯度分量进行滤波，并计算表示角点强度的度量。您可以指定一个阈值来确定检测角点的水平。对于度量超过此阈值的像素，该模块会返回角点。Harris 算法比 FAST 算法使用更多硬件资源，但可以检测到 FAST 算法可能找不到的角点。
