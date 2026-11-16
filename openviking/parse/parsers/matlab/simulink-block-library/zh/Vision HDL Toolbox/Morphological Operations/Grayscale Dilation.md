---
type: simulink-block
title: 'Grayscale Dilation'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'grayscaledilation'
documentation_source_path: 'ref/grayscaledilation.html'
language: zh-CN
chinese_source: worker-translation
---

# Grayscale Dilation

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

对于单像素流式传输，将 **pixel** 指定为表示灰度强度的无符号标量值。对于多像素流式传输，将 **pixel** 指定为由 **Number of pixels** 个像素强度值组成的列向量。**Number of pixels** 可以为 2、4 或 8。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fi(0,N,0)` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号应用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号应用于向量中索引最高的像素。

**数据类型：** `bus`

### 输出

### **pixel** — 输出像素流 标量 | 向量

输出 **pixel** 的维度与输入 **pixel** 的维度匹配。该模块将输出 **pixel** 返回为标量或由 **Number of pixels** 个值组成的列向量。

此输出 **pixel** 的数据类型与输入 **pixel** 的数据类型相同。

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号应用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号应用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### **Neighborhood** — 像素邻域 `ones(3,3)`（默认） | 由 `1`s 和 `0`s 组成的向量或矩阵

像素邻域，指定为由二进制值组成的向量或矩阵。

该模块支持最多 32×32 像素的平坦邻域。要使用结构元素，将 **Neighborhood** 参数设置为 `getnhood (Image Processing Toolbox)(strel (Image Processing Toolbox)(shape))`，其中 *`shape`* 由 `strel` (Image Processing Toolbox) 函数的输入参数指定。最小邻域大小为 2×2 矩阵，或 2×1 列向量。如果邻域是行向量，则其宽度必须至少为 8 列且不包含零。

### **Line buffer size** — 行内存缓冲区的大小 `2048`（默认） | 正整数

行内存缓冲区的大小，指定为正整数。选择一个能够容纳水平行中活动像素数量的 2 的幂。如果指定的值不是 2 的幂，则缓冲区使用下一个最大的 2 的幂。

使用多像素输入时，此值必须容纳 (**Active pixels per line**)/(**Number of pixels**) + 2。

该模块分配 (*n* – 1)×**Line buffer size** 个内存位置来存储像素，其中 *n* 是 **Neighborhood** 参数值中的行数。

## 所属库

Vision HDL Toolbox / Morphological Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持为 Simulink 加速器和快速加速器模式以及 DPI 组件生成进行 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果此模块位于 Resettable Synchronous Subsystem (HDL Coder) 内，则无法为其生成 HDL 代码。

## 版本历史

**R2016a 中引入**

### R2018b：改进的行缓冲

该模块的内部行缓冲现在可处理突发数据，即像素行内的非连续有效信号。由于改进的填充逻辑以及对具有偶数行数的内核大小的原生支持，此实现使用更少的硬件资源。此更改会影响 Line Buffer 模块以及使用内部行缓冲的模块。

对于某些配置，行缓冲的延迟现在减少了几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳实践是使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

灰度像素数据的形态学膨胀

Grayscale Dilation 模块对像素强度值流执行形态学膨胀。您可以指定最多 32×32 像素的邻域或结构元素。对于宽度超过 8 像素的线形、方形或矩形结构元素，该模块使用 Van Herk 算法查找最大像素值。此算法仅使用三个比较器查找所有行的最大值，然后使用比较树查找行结果的最大像素值。

对于宽度小于 8 像素或包含零元素的结构元素，该模块为邻域的每一行实现一个流水线比较树。额外的比较树查找行结果的最大像素值。如果结构元素包含排除像素的零，则该算法通过不为那些像素位置实现比较器来节省硬件资源。
