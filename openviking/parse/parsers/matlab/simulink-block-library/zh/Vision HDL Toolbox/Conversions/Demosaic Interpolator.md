---
type: simulink-block
title: 'Demosaic Interpolator'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'demosaicinterpolator'
documentation_source_path: 'ref/demosaicinterpolator.html'
language: zh-CN
chinese_source: worker-translation
---

# Demosaic Interpolator

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

对于单像素流，将 **pixel** 指定为标量。对于多像素流，将 **pixel** 指定为 **Number of pixels**×1 的像素值向量。**Number of pixels** 可以为 2、4 或 8。Bayer 格式的图像在每个像素位置有一个颜色分量。使用 **Sensor alignment** 参数选择 R、G 和 B 像素的序列。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `fixdt(0,W,F)` | `single` | `double`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

对于多像素流式传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### 输出

### **pixel** — 输出像素流 向量 | 矩阵

对于单像素流，输出 **pixel** 是包含三个元素的 RGB 值向量。对于多像素流，输出 **pixel** 是 **Number of pixels**×3 的 RGB 值矩阵。该模块使用您在 **Interpolation algorithm** 参数中指定的方法，计算每个像素缺失颜色分量的值。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `fixdt(0,W,F)` | `single` | `double`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

对于多像素流式传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### **Interpolation algorithm** — 用于计算缺失像素值的算法 `Gradient-corrected linear`（默认） | `Bilinear`

用于计算缺失像素值的算法，指定为以下选项之一：

- `Gradient-corrected linear` —
  针对强度梯度校正的双线性平均值
- `Bilinear` — 周围 3×3 邻域中像素值的平均值

### **Sensor alignment** — 输入流中像素的颜色序列 `RGGB`（默认） | `GBRG` | `GRBG` | `BGGR`

选择与输入图像左上角 2×2 像素块对应的 R、G 和 B 像素序列。按从左到右、从上到下的顺序指定序列。例如，默认序列 `RGGB` 表示具有以下模式的图像。

顶部为 R 和 G、底部为 G 和 B 的 2×2 网格

### **Line buffer size** — 行内存缓冲区的大小 `2048`（默认） | integer

行内存缓冲区的大小，指定为正整数。选择一个 2 的幂，使其能够容纳一条水平线中的活动像素数。如果指定的值不是 2 的幂，缓冲区将使用下一个更大的 2 的幂。

使用多像素输入时，此值必须能够容纳 (**Active pixels per line**)/(**Number of pixels**) + 2。

分配的总内存大小取决于您选择的 **Interpolation algorithm**：

- `Bilinear`：2×**Line buffer size** 个内存位置
- `Gradient-corrected linear`：4×**Line buffer size** 个内存位置

## 所属库

Vision HDL Toolbox / Conversions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成

使用 HDL Coder™ 生成面向 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在可重置同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2015a 中引入**

### R2022a：每时钟周期两个像素的流式传输

该模块现在支持每时钟周期 2 个像素的多像素流。

### R2021b：多像素流式传输

Demosaic Interpolator 模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

该模块接受 *NumPixels*×1 值的输入向量，并返回 *NumPixels*×3 值的输出矩阵。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号应用于矩阵中的所有像素。

### R2018b：改进的行缓冲区

此模块中的内部行缓冲区现在可处理突发数据，即像素行内非连续的 `valid` 信号。由于改进了填充逻辑以及对具有偶数行数的内核大小的原生支持，此实现使用更少的硬件资源。此更改会影响 Line Buffer 模块以及使用内部行缓冲区的模块。

对于某些配置，行缓冲区的延迟现在减少了几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳做法是使用像素流控制信号同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

从 Bayer 图案像素流构造 RGB 像素数据

Demosaic Interpolator 模块为流式视频数据提供 Bayer 图案插值滤波器。该模块使用硬件高效、无乘法器的算法进行计算，以用于 HDL 代码生成。您可以选择低复杂度的双线性插值，或中等复杂度的梯度校正双线性插值。

- 当您选择双线性插值时，该模块仅使用加法和位移运算在 3×3 像素窗口上操作。
- 当您选择梯度校正时，该模块在 5×5 像素窗口上操作。计算使用位移、加法和低阶规范有符号数字 (CSD) 乘法执行。
