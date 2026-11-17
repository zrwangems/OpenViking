---
type: simulink-block
title: 'Pixel Control Bus Selector'
family: 'utilities'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'pixelcontrolbusselector'
documentation_source_path: 'ref/pixelcontrolbusselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixel Control Bus Selector

## 端口

### 输入

### **Port\_1** — 伴随像素流 `pixelcontrol` 总线的控制信号

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`
### 输出

### **Port\_1** — 帧中水平线的第一个像素标量

帧中水平线的第一个像素，以 `Boolean` 标量形式返回。此端口从输入总线返回
`hStart` 信号。

**数据类型：** `Boolean`

### **Port\_2** — 帧中水平线的最后一个像素标量

帧中水平线的最后一个像素，以 `Boolean` 标量形式返回。此端口从输入总线返回
`hEnd` 信号。

**数据类型：** `Boolean`

### **Port\_3** — 帧第一（顶部）行的第一个像素标量

帧第一（顶部）行的第一个像素，以 `Boolean` 标量形式返回。此端口从输入总线返回
`vStart` 信号。

**数据类型：** `Boolean`

### **Port\_4** — 帧最后（底部）行的最后一个像素标量

帧最后（底部）行的最后一个像素，以 `Boolean` 标量形式返回。此端口从输入总线返回
`vEnd` 信号。

**数据类型：** `Boolean`

### **Port\_5** — 有效像素指示符标量

有效像素指示符，以 `Boolean` 标量形式返回。此端口从输入总线返回 `valid` 信号。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持为 Simulink 加速器和快速加速器模式以及 DPI 组件生成 C/C++ 代码。

### HDL 代码生成：使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

要详细了解将总线用于 HDL 代码生成，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

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

## 描述

从 Vision HDL Toolbox 模块使用的控制信号总线中选择信号

Pixel Control Bus Selector 模块从 `pixelcontrol` 总线中选择信号。请参阅 Pixel Control Bus。

该模块是 Simulink® Bus Selector 模块的实现。有关更多信息，请参阅 Bus Selector (Simulink)。
