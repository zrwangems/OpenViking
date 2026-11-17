---
type: simulink-block
title: 'Image Statistics'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'imagestatistics'
documentation_source_path: 'ref/imagestatistics.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Statistics

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量

对于单像素流，将 **pixel** 指定为表示灰度强度的无符号标量值。对于多像素流，将 **pixel** 指定为包含 **Number of pixels** 个像素强度值的列向量。**Number of pixels** 可以为 2、4 或 8。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`
### 输出

该模块使用全精度算术进行内部计算。在输出端口，中间数据通过以下定点设置转换回输入类型：**Rounding method** = `Nearest`，**Overflow action** = `Saturate`。下表显示了每次计算相对于输入字长（*IWL*）的输出字长。

| Mean | Variance | Std. Deviation |
| --- | --- | --- |
| *IWL* | 2×*IWL* | 2×*IWL* |

### **mean** — 最近完成的输入帧的均值 标量

最近完成的输入帧的均值，以标量形式返回。**mean** 的数据类型与 **pixel** 的数据类型相同。

**数据类型：** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

### **var** — 最近完成的输入帧的方差 标量

最近完成的输入帧的方差，以标量形式返回。**var** 的数据类型与 **pixel** 的数据类型相同。

**数据类型：** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

### **stdDev** — 最近完成的输入帧的标准差 标量

最近完成的输入帧的标准差，以标量形式返回。**stdDev** 的数据类型与 **pixel** 的数据类型相同。

**数据类型：** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

### **validOut** — 计算完成 布尔值

当某一帧的统计输出准备就绪时，该模块将此输出设置为 `true`。

**数据类型：** `Boolean`

## 参数

### **Enable mean output** — 计算每个输入帧的均值 on（默认）| off

选择此参数以启用 **mean** 端口并计算每个输入帧的均值。

### **Enable variance output** — 计算每个输入帧的方差 on（默认）| off

选择此参数以启用 **var** 端口并计算每个输入帧的方差。

### **Enable std. deviation** — 计算每个输入帧的标准差 on（默认）| off

选择此参数以启用 **stdDev** 端口并计算每个输入帧的标准差。

## 所属库

Vision HDL Toolbox / Statistics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015a 中引入**

### R2023b: 多像素流

Image Statistics 模块现在支持多像素流。对于多像素流，该模块支持 2、4 或 8 像素的输入列向量。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号应用于向量中的所有像素。表示图像统计信息的输出端口保持标量。

## 描述

计算均值、方差和标准差

Image Statistics 模块计算流视频数据的均值、方差和标准差。每个计算都在输入感兴趣区域 (ROI) 中的所有像素上执行。该模块通过使用硬件高效的算法来实现这些计算。
