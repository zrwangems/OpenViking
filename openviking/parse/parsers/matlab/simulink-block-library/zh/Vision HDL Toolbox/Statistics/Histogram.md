---
type: simulink-block
title: 'Histogram'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'histogram'
documentation_source_path: 'ref/histogram.html'
language: zh-CN
chinese_source: worker-translation
---

# Histogram

## 端口
```yaml
ports:
- name: pixel
  summary: 输入像素流 标量 | 向量
  direction: input
  data_types: uint | fixdt(0,W,0) | Boolean | double | single
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: input
  data_types: bus
- name: binAddr
  summary: 用于读取直方图值的 bin 编号 整数
  direction: input
  data_types: fixdt(0,W,0)
- name: binReset
  summary: 重置直方图 bin 值 标量
  direction: input
  data_types: Boolean
- name: readRdy
  summary: 指示直方图 bin 可供读取 标量
  direction: output
  data_types: Boolean
- name: hist
  summary: 与请求地址对应的 bin 值 整数
  direction: output
  data_types: fixed point
- name: validOut
  summary: 指示直方图值有效 标量
  direction: output
  data_types: Boolean
```

### 输入

### **pixel** — 输入像素流 标量 | 向量

此模块支持单像素流或多像素流。
对于单像素流，将单个输入像素指定为标量强度值。对于多像素流，指定包含两个、四个或八个像素强度值的向量。有关如何为多像素流设置模型的详细信息，请参阅 Filter Multipixel Video Streams。

此模块不支持多分量流。要处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线完全相同，因此您可以将单个总线连接到多个复制的模块。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `fixdt(0,W,0)` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。
由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### **binAddr** — 用于读取直方图值的 bin 编号 整数

在 **readRdy** 输出端口为 1（`true`）的每个周期，模块都会捕获此值。数据类型为 `fixdt(0,W,0)`，W = 5,6,...,12。字长必须为 log2(**Number of bins**)。

**数据类型：** `fixdt(0,W,0)`

### **binReset** — 重置直方图 bin 值 标量

**binReset** 值为 1（`true`）会触发 RAM 初始化序列，从而重置直方图 bin 值。重置需要 `NumBins` 个周期来清除所有位置。在此间隔期间，输入信号将被忽略。

**数据类型：** `Boolean`

### 输出

### **readRdy** — 指示直方图 bin 可供读取 标量

当 **readRdy** 为 1（`true`）时，直方图 bin 已准备好读取。在帧的最后一个像素之后两个周期，模块将 **readRdy** 返回为 1（`true`）。

**数据类型：** `Boolean`

### **hist** — 与请求地址对应的 bin 值 整数

与请求地址 **binAddr** 对应的直方图 bin 值。**Data type** 参数指定此值的数据类型。

**数据类型：** `fixed point`

### **validOut** — 指示直方图值有效 标量

当 **validOut** 为 1（`true`）时，直方图 bin 值 **hist** 有效。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Number of bins
  summary: 直方图 bin 的数量 256（默认）| 32 到 4096 之间的 2 的幂
  group: ''
- name: Data type
  summary: 直方图 bin 值的数据类型 Unsigned fixed point（默认）| double | single
  group: ''
- name: Word length
  summary: 直方图 bin 的字长 16（默认）| 整数
  group: ''
```

### **Number of bins** — 直方图 bin 的数量 `256`（默认）| `32` 到 `4096` 之间的 2 的幂

根据输入字长（WL）选择 bin 的数量。如果 bin 的数量小于 2WL，模块会截断每个像素的最低有效位。如果 bin 的数量大于 2WL，则某些 bin 不会被使用，并且在综合设计后，它将使用比必要更多的硬件资源。

### **Data type** — 直方图 bin 值的数据类型 `Unsigned fixed point`（默认）| `double` | `single`

直方图 bin 值的数据类型。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

### **Word length** — 直方图 bin 的字长 `16`（默认）| 整数

直方图 bin 的字长。如果某个 bin 溢出，计数将饱和，并且模块会显示警告。

#### 依赖关系

当您将 **Data type** 设置为 `Unsigned fixed point` 时，此参数适用。
## 所属库

Vision HDL Toolbox / Statistics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速模式和快速加速模式的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法为可重置同步子系统 (HDL Coder) 内的此模块生成 HDL。

## 版本历史

**在 R2015a 中引入**

### R2022b：每时钟两像素流式传输

此模块现在支持每时钟周期 2 像素的多像素流。

### R2022a：多像素流式传输

Histogram 模块现在支持多像素流。HDL 实现为每个像素并行复制算法。

此模块支持 *NumPixels* 个值的输入列向量，其中 *NumPixels* 为 4 或 8。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号应用于矩阵中的所有像素。无论输入是标量还是向量，输出接口都相同。

### R2019b：增加的直方图大小

您现在可以将模块配置为具有 2048 或 4096 个直方图 bin。

## 描述

视频流中像素值的频率分布

Histogram 模块计算视频流中像素值的频率分布。您可以配置 bin 的数量和大小。此模块提供用于访问每个 bin 的读取接口。此模块保持运行中的直方图，直到您重置 bin 值。
