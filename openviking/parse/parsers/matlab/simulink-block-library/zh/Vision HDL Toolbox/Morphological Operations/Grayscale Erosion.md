---
type: simulink-block
title: 'Grayscale Erosion'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'grayscaleerosion'
documentation_source_path: 'ref/grayscaleerosion.html'
language: zh-CN
chinese_source: worker-translation
---

# Grayscale Erosion

## 端口

### 输入

### **pixel** — 输入像素流标量

像素流中的单个图像像素，指定为表示灰度强度的无符号整数标量。

该软件支持在仿真中使用 `double` 和 `single` 数据类型，但不支持用于 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `double` | `single` | `fi(0,N,0)`

### **ctrl** — 与像素流 `pixelcontrol` bus 相关联的控制信号

`pixelcontrol` bus 包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`
### 输出

### **pixel** — 输出像素流标量

经形态学操作转换后的单个输出像素，以标量值形式返回。

此输出 **pixel** 的数据类型与输入 **pixel** 的数据类型相同。

### **ctrl** — 与像素流 `pixelcontrol` bus 相关联的控制信号

`pixelcontrol` bus 包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`

## 参数

### **Neighborhood** — 像素邻域 `ones(3,3)`（默认）| 由 `1`s 和 `0`s 组成的向量或矩阵

像素邻域，指定为由二进制值组成的向量或矩阵。

该模块支持最大 32×32 像素的平坦邻域。要使用结构元素，请将 **Neighborhood** 参数设置为 `getnhood (Image Processing Toolbox)(strel (Image Processing Toolbox)(shape))`，其中 *`shape`* 由 `strel` (Image Processing Toolbox) 函数的输入参数指定。最小邻域大小为 2×2 矩阵，或 2×1 列向量。如果邻域是行向量，则其宽度必须至少为 8 列，且不包含零。

### **Line buffer size** — 行内存缓冲区大小 `2048`（默认）| 正整数

行内存缓冲区的大小，指定为正整数。选择一个能容纳一条水平线中活动像素数的 2 的幂。如果指定的值不是 2 的幂，缓冲区将使用下一个最大的 2 的幂。

该模块分配 (*n* – 1)×**Line buffer size** 个内存位置来存储像素，其中 *n* 是 **Neighborhood** 参数值中的行数。

## 所属库

Vision HDL Toolbox / Morphological Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果此模块位于 Resettable Synchronous Subsystem (HDL Coder) 内，则不能为其生成 HDL 代码。

## 版本历史

**在 R2016a 中引入**

### R2018b：改进的行缓冲区

此模块的内部行缓冲区现在可以处理突发数据，即像素行内非连续的 valid 信号。由于改进的填充逻辑以及对具有偶数行数的内核大小的原生支持，此实现使用更少的硬件资源。此更改会影响 Line Buffer 模块以及使用内部行缓冲区的模块。

对于某些配置，行缓冲区的延迟现在减少了几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳实践是通过使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

灰度像素数据的形态学腐蚀

Grayscale Erosion 模块对像素强度值流执行形态学腐蚀。您可以指定最大 32×32 像素的邻域或结构元素。对于宽度超过 8 像素的线形、正方形或矩形结构元素，该模块使用 Van Herk 算法查找最小像素值。此算法仅使用三个比较器来查找所有行的最小像素值，然后使用比较树查找各行结果的最小像素值。

对于宽度小于 8 像素的结构元素，或包含零元素的结构元素，该模块为邻域的每一行实现流水线比较树。一个额外的比较树查找各行结果的最小像素值。如果结构元素包含屏蔽像素的零，则该算法通过不为那些像素位置实现比较器来节省硬件资源。
