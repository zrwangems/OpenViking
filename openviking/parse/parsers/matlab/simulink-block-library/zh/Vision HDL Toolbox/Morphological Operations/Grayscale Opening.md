---
type: simulink-block
title: 'Grayscale Opening'
family: 'morphological-operations'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'grayscaleopening'
documentation_source_path: 'ref/grayscaleopening.html'
language: zh-CN
chinese_source: worker-translation
---

# Grayscale Opening

## 端口

### 输入

### **pixel** — 输入像素流标量

像素流中的单个图像像素，指定为表示灰度强度的无符号整数标量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但 HDL 代码生成不支持。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `double` | `single` | `fi(0,N,0)`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

**数据类型：** `bus`

### 输出

### **pixel** — 输出像素流标量

经形态学运算变换的单个输出像素，以标量值返回。

此输出 **pixel** 的数据类型与输入 **pixel** 的数据类型相同。

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

**数据类型：** `bus`

## 参数

### **Neighborhood** — 像素邻域 `ones(3,3)`（默认）| 由 `1` 和 `0` 组成的向量或矩阵

像素邻域，指定为二值值的向量或矩阵。

该模块支持最大 32×32 像素的平坦邻域。要使用结构元素，请将 **Neighborhood** 参数设置为 `getnhood (Image Processing Toolbox)(strel (Image Processing Toolbox)(shape))`，其中 *`shape`* 由 `strel` (Image Processing Toolbox) 函数的输入参数指定。最小邻域大小为 2×2 矩阵，或 2×1 列向量。如果邻域是行向量，则其宽度必须至少为 8 列，且不能包含零。

### **Line buffer size** — 行内存缓冲区的大小 `2048`（默认）| 正整数

行内存缓冲区的大小，指定为正整数。选择一个足以容纳水平行中有效像素数量的 2 的幂。如果指定的值不是 2 的幂，则缓冲区使用下一个最大的 2 的幂。

该模块分配 (*n* – 1) × **Line buffer size** 个内存位置来存储像素，其中 *n* 是 **Neighborhood** 参数值中的行数。

## 所属库

Vision HDL Toolbox / Morphological Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持 C/C++ 代码生成，适用于 Simulink 加速模式和快速加速模式，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

该模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果此模块位于 Resettable Synchronous Subsystem (HDL Coder) 中，则无法为其生成 HDL 代码。

## 版本历史

**在 R2016a 中引入**

### R2018b：改进的行缓冲区

此模块中的内部行缓冲区现在可处理突发数据，即像素行内非连续的有效信号。由于改进了填充逻辑，并且原生支持行数为偶数的内核大小，此实现使用的硬件资源更少。此更改会影响 Line Buffer 模块以及使用内部行缓冲区的模块。

对于某些配置，行缓冲区的延迟现在减少了几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳做法是使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

灰度像素数据的形态学开运算

Grayscale Opening 模块使用相同的邻域进行形态学腐蚀，随后进行形态学膨胀。该模块对像素强度值流进行操作。您可以指定最大 32×32 像素的邻域或结构元素。对于宽度超过 8 像素的线形、方形或矩形结构元素，该模块使用 Van Herk 算法查找最大和最小像素值。对于宽度小于 8 像素或包含零元素的结构元素，该模块实现流水线比较树来查找最大和最小像素值。
