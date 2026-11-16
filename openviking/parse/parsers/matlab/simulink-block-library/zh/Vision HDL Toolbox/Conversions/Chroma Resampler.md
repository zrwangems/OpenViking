---
type: simulink-block
title: 'Chroma Resampler'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'chromaresampler'
documentation_source_path: 'ref/chromaresampler.html'
language: zh-CN
chinese_source: worker-translation
---

# Chroma Resampler

## 端口

### 输入

### **pixel** — Y'CbCr 颜色空间中的输入像素流 向量 | 矩阵

对于标量像素流，将 **pixel** 指定为 1×3 值的向量。对于多像素流，将 **pixel** 指定为 **Number of pixels**×3 像素强度值的矩阵。**Number of pixels** 可以是二、四或八。

像素流必须位于 Y'CbCr 颜色空间。整数和定点数据类型必须介于 8 到 16 位之间。这些值必须是无符号的。

该软件支持 `double` 和 `single` 数据类型进行仿真，但不支持 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `fi(0,N,0) , where N = 8,9,...,16` | `single` | `double`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅像素控制总线。

对于多像素流，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### 输出

### **pixel** — Y'CbCr 颜色空间中的输出像素流 向量 | 矩阵

Y'CbCr 颜色空间中的输出像素流，返回为单像素流或多像素流。输出流的数据类型和 **Number of pixels** 与输入像素流相同。

该软件支持 `double` 和 `single` 数据类型进行仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `fixed point`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅像素控制总线。

对于多像素流，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### 主要

### **Resampling** — 重采样类型 `4:4:4 to 4:2:2`（默认）| `4:2:2 to 4:4:4`

如果选择 `4:4:4 to 4:2:2`，该模块执行下采样操作。如果选择 `4:2:2 to 4:4:4`，该模块执行上采样操作。

### **Antialiasing filter** — 跟随下采样操作的低通滤波器 `Auto`（默认）| `Property` | `None`

如果选择 `Auto`，该模块使用内置低通滤波器。如果选择 `Property`，**Horizontal filter coefficients** 参数将出现在对话框中。如果选择 `None`，该模块不对输入信号进行滤波。

#### 依赖关系

当将 **Resampling** 设置为 `4:4:4 to 4:2:2` 时，此参数可见。

### **Horizontal filter coefficients** — 抗混叠滤波器的系数 `[0.2 0.6 0.2]`（默认）| 向量

抗混叠滤波器的系数，指定为向量。

#### 依赖关系

如果将 **Resampling** 设置为 `4:4:4 to 4:2:2` 且将 **Antialiasing filter** 设置为 `Property`，则此参数可见。

### **Interpolation** — 上采样操作的插值方法 `Linear`（默认）| `Pixel replication`

如果选择 `Linear`，该模块使用线性插值来计算缺失值。如果选择 `Pixel replication`，该模块重复前一个像素的色度值来创建缺失像素。

#### 依赖关系

如果将 **Resampling** 设置为 `4:2:2 to 4:4:4`，则此参数可见。

### 数据类型

此选项卡上的参数仅在相关时出现。如果将模块配置为不需要滤波器系数，或者不可能发生舍入或溢出，则无关参数会隐藏。

### **Rounding mode** — 内部定点计算的舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

指定内部定点计算的舍入方法。

### **Saturate on integer overflow** — 内部定点计算的溢出操作 `off`（默认）| `on`

当清除此参数时，定点值和整数值在溢出该数据类型可表示的范围时回绕到零。当选择此参数时，值饱和到最大可表示值。

### **Filter coefficients** — 抗混叠滤波器系数的数据类型 `fixdt(1,16,15)`（默认）| 数据类型表达式

当将 **Antialiasing filter** 设置为 `Auto` 或 `Property` 时，此参数适用。

## 所属库

Vision HDL Toolbox / Conversions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持为 Simulink 加速器和快速加速器模式以及 DPI 组件生成进行 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015a 中引入**

### R2025a: 多像素多分量流

Chroma Resampler 模块现在支持多像素多分量流。该模块接受并返回 *NumPixels*×3 值的矩阵。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号适用于矩阵中的所有像素。HDL 实现并行地为每个像素复制该算法。

## 描述

下采样或上采样色度分量

Chroma Resampler 模块对像素流进行下采样或上采样。

- 下采样通过将多个像素上的像素色度分量组合起来，降低视频系统中的带宽和存储需求。您可以通过选择默认滤波器或输入系数来指定滤波器以防止混叠。
- 上采样将信号恢复到其原始速率。要计算额外样本，您可以使用插值或复制。

该模块接受亮度和色度分量。该模块不修改亮度分量，并应用延迟将其与重采样的色度输出对齐。输出亮度分量的速率与输入的速率相同。
