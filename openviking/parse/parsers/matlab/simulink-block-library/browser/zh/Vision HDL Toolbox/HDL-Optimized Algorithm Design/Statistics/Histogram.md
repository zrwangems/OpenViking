---
type: simulink-block
title: 'Histogram'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Algorithm Design / Statistics'
documentation_page: 'histogram'
documentation_source_path: 'ref/histogram.html'
language: zh-CN
chinese_source: worker-translation
---

# Histogram

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

此模块支持单像素流式传输或多像素流式传输。对于单像素流式传输，请将单个输入像素指定为标量强度值。对于多像素流式传输，请指定包含两个、四个或八个像素强度值的向量。有关如何为多像素流式传输设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

此模块不支持多分量流式传输。要处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线都相同，因此可以将单个总线连接到多个复制的模块。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint` | `fixdt(0,W,0)` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流式传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### **binAddr** — 用于读取直方图值的 bin 编号 integer

在 **readRdy** 输出端口为 1（`true`）的每个周期，该模块都会捕获此值。数据类型为 `fixdt(0,W,0)`，W = 5,6,...,12。字长必须为 log2(**Number of bins**)。

**数据类型：** `fixdt(0,W,0)`

### **binReset** — 重置直方图 bin 值 标量

**binReset** 值为 1（`true`）会触发 RAM 初始化序列，从而重置直方图 bin 值。重置需要 `NumBins` 个周期来清除所有位置。在此间隔期间，输入信号会被忽略。

**数据类型：** `Boolean`

### 输出

### **readRdy** — 指示可用于读取的直方图 bin 标量

当 **readRdy** 为 1（`true`）时，直方图 bin 已准备好读取。该模块在一帧的最后一个像素之后两个周期将 **readRdy** 返回为 1（`true`）。

**数据类型：** `Boolean`

### **hist** — 与请求地址对应的 bin 值 integer

与请求地址 **binAddr** 对应的直方图 bin 值。**Data type** 参数指定此值的数据类型。

**数据类型：** `fixed point`

### **validOut** — 指示直方图值有效 标量

当 **validOut** 为 1（`true`）时，直方图 bin 值 **hist** 有效。

**数据类型：** `Boolean`

## 参数

### **Number of bins** — 直方图 bin 数量 `256`（默认） | `32` 到 `4096` 之间的 2 的幂

根据输入字长（WL）选择 bin 数量。如果 bin 数量小于 2WL，则该模块会截断每个像素的最低有效位。如果 bin 数量大于 2WL，则某些 bin 不会被使用，并且在综合设计后，它将使用比所需更多的硬件资源。

### **Data type** — 直方图 bin 值的数据类型 `Unsigned fixed point`（默认） | `double` | `single`

直方图 bin 值的数据类型。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

### **Word length** — 直方图 bin 的字长 `16`（默认） | integer

直方图 bin 的字长。如果某个 bin 溢出，则计数会饱和，并且该模块会显示警告。

#### 依赖关系

当您将 **Data type** 设置为 `Unsigned fixed point` 时，此参数适用。

## 所属库

Vision HDL Toolbox / Statistics

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2015a 中引入**

### R2022b：每时钟周期两个像素的流式传输

该模块现在支持每时钟周期有 2 个像素的多像素流。

### R2022a：多像素流式传输

Histogram 模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

该模块支持包含 *NumPixels* 个值的输入列向量，其中 *NumPixels* 为 4 或 8。**ctrl** 端口保持标量，并且 `pixelcontrol` 总线中的控制信号适用于矩阵中的所有像素。无论输入是标量还是向量，输出接口都相同。

### R2019b：增大的直方图大小

现在可以将该模块配置为具有 2048 或 4096 个直方图 bin。

## 描述

视频流中像素值的频率分布

Histogram 模块计算视频流中像素值的频率分布。您可以配置 bin 的数量和大小。该模块提供用于访问每个 bin 的读取接口。该模块会持续维护运行中的直方图，直到您重置 bin 值。
