---
type: simulink-block
title: 'Grayscale Opening'
family: 'visionhdl'
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
```yaml
ports:
- name: pixel
  summary: 输入像素流标量
  direction: input
  data_types: uint8 | uint16 | uint32 | uint64 | double | single | fi(0,N,0)
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: input
  data_types: bus
- name: pixel
  summary: 输出像素流标量
  direction: output
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: output
  data_types: bus
```

### 输入

### **pixel** — 输入像素流标量

像素流中的单个图像像素，指定为表示灰度强度的无符号整数标量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `double` | `single` | `fi(0,N,0)`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`

### 输出

### **pixel** — 输出像素流标量

经形态学运算变换后的单个输出像素，以标量值返回。

此输出 **pixel** 的数据类型与输入 **pixel** 的数据类型相同。

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Neighborhood
  summary: 像素邻域 ones(3,3)（默认）| 由 1 和 0 组成的向量或矩阵
  group: ''
- name: Line buffer size
  summary: 行存储器缓冲区大小 2048（默认）| 正整数
  group: ''
```

### **Neighborhood** — 像素邻域 `ones(3,3)`（默认）| 由 `1` 和 `0` 组成的向量或矩阵

像素邻域，指定为由二进制值组成的向量或矩阵。

该模块支持最大 32×32 像素的平坦邻域。要使用结构元素，请将 **Neighborhood** 参数设置为 `getnhood (Image Processing Toolbox)(strel (Image Processing Toolbox)(shape))`，其中 *`shape`* 由 `strel` (Image Processing Toolbox) 函数的输入参数指定。最小邻域大小为 2×2 矩阵或 2×1 列向量。如果邻域为行向量，则其宽度必须至少为 8 列且不包含零。

### **Line buffer size** — 行存储器缓冲区大小 `2048`（默认）| 正整数

行存储器缓冲区大小，指定为正整数。选择一个能够容纳水平行中有效像素数量的 2 的幂。如果指定的值不是 2 的幂，则缓冲区使用下一个最大的 2 的幂。

该模块分配 (*n* – 1)×**Line buffer size** 个存储位置来存储像素，其中 *n* 是 **Neighborhood** 参数值中的行数。
## 所属库

Vision HDL Toolbox / Morphological Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

如果该模块位于可复位同步子系统 (HDL Coder) 内，则无法为其生成 HDL 代码。

## 版本历史

**在 R2016a 中引入**

### R2018b：改进的行缓冲

此模块中的内部行缓冲现在可以处理突发数据，即像素行内非连续的有效信号。由于改进了填充逻辑以及对具有偶数行数的内核尺寸的原生支持，此实现使用更少的硬件资源。此更改会影响 Line Buffer 模块以及使用内部行缓冲的模块。

对于某些配置，行缓冲的延迟现在减少几个周期。您可能需要重新平衡模型中的并行路径延迟。最佳做法是使用像素流控制信号来同步模型中的并行路径，而不是插入特定数量的延迟。

## 描述

灰度像素数据的形态学开运算

Grayscale Opening 模块通过使用相同的邻域进行形态学腐蚀，然后进行形态学膨胀。该模块对像素强度值流进行操作。您可以指定一个最大为 32×32 像素的邻域，即结构元素。对于宽度超过 8 像素的线形、方形或矩形结构元素，该模块使用 Van Herk 算法来查找最大和最小像素值。对于宽度小于 8 像素或包含零元素的结构元素，该模块实现流水线比较树来查找最大和最小像素值。
