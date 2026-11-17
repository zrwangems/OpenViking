---
type: simulink-block
title: 'Pixel Control Bus Creator'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'pixelcontrolbuscreator'
documentation_source_path: 'ref/pixelcontrolbuscreator.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixel Control Bus Creator

## 端口

### 输入

### **hStart** — 一帧中水平行的第一个像素 标量

一帧中水平行的第一个像素，指定为 `Boolean` 标量。

**数据类型：** `Boolean`

### **hEnd** — 一帧中水平行的最后一个像素 标量

一帧中水平行的最后一个像素，指定为 `Boolean` 标量。

**数据类型：** `Boolean`

### **vStart** — 一帧中第一（顶部）行的第一个像素 标量

一帧中第一（顶部）行的第一个像素，指定为 `Boolean` 标量。

**数据类型：** `Boolean`

### **vEnd** — 一帧中最后（底部）行的最后一个像素 标量

一帧中最后（底部）行的最后一个像素，指定为 `Boolean` 标量。

**数据类型：** `Boolean`

### **valid** — 有效像素指示 标量

有效像素指示，指定为 `Boolean` 标量。

**数据类型：** `Boolean`
### 输出

### **ctrl** — 伴随像素流的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`

## 参数

R2025b 中未记录。

## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink 加速器和快速加速器模式的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015a 中引入**

## 描述

创建用于 Vision HDL Toolbox 模块的控制信号总线

Pixel Control Bus Creator 模块创建一个 `pixelcontrol` 总线。请参阅 Pixel Control Bus。

该模块是 Simulink® Bus Creator 模块的实现。有关更多信息，请参阅 Bus Creator (Simulink)。

**故障排除**

当您从使用 `pixelcontrol` 总线的 Simulink 模型生成 HDL 代码时，可能会遇到此错误。

```
Cannot resolve variable 'pixelcontrol'
```

为避免此问题，请使用 `pixelcontrolbus` 函数在基础工作区中创建总线类型的实例。然后再次尝试生成 HDL 代码。

Vision HDL Toolbox™ 模型模板在 `InitFcn` 回调中包含此行。

```
evalin('base','pixelcontrolbus')
```
