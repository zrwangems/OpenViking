---
type: simulink-block
title: 'Color Space Converter'
family: 'conversions'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'colorspaceconverter'
documentation_source_path: 'ref/colorspaceconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Color Space Converter

## 端口

### 输入

### **pixel** — 输入像素流 向量 | 矩阵

对于标量像素流，将 **pixel** 指定为 1×3 值的向量。对于多像素流，将 **pixel** 指定为 **Number of pixels**×3 的像素强度值矩阵。**Number of pixels** 可以为 2、4 或 8。

像素流必须采用 Y'CbCr 或 R'G'B' 色彩空间。整数和定点数据类型必须介于 8 到 16 位之间。这些值必须是无符号的。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `fi(0,N,0), where N = 8,9,...,16` | `single` | `double`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

对于多像素流传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号应用于该向量中索引最低的像素。`hEnd` 和 `vEnd` 信号应用于该向量中索引最高的像素。

**数据类型：** `bus`
### 输出

### **pixel** — 新色彩空间中的输出像素流 标量 | 向量 | 矩阵

以强度、Y'CbCr 或 R'G'B' 色彩空间返回的输出像素流，以单像素流或多像素流形式返回。输出流的数据类型和 **Number of pixels** 与输入像素流相同。如果输出是强度值，则每个像素有一个分量。如果输出是 Y'CbCr 或 R'G'B'，则每个像素有三个分量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `fixed point`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

对于多像素流传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号应用于该向量中索引最低的像素。`hEnd` 和 `vEnd` 信号应用于该向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### **Conversion** — 色彩空间转换类型 `RGB to YCbCr`（默认） | `YCbCr to RGB` | `RGB to intensity`

该模块接受的输入像素是表示单个像素的三个值组成的向量。如果选择 `RGB to intensity`，则每个输出像素是标量。否则，每个输出像素是三个值的向量。

### **Use conversion specified by** — 转换方程 `Rec. 601 (SDTV)`（默认） | `Rec. 709 (HDTV)`

用于 R'G'B' 和 Y'CbCr 色彩空间之间的转换方程。

#### 依赖关系

仅当将 **Conversion** 设置为 `RGB to YCbCr` 或 `YCbCr to RGB` 时，此参数才适用。

### **Scanning standard** — HDTV 扫描标准 `1250/50/2:1`（默认） | `1125/60/2:1`

用于在 HDTV 格式下在 R'G'B' 和 Y'CbCr 色彩空间之间进行转换的扫描标准。

#### 依赖关系

当将 **Use conversion specified by** 设置为 `Rec. 709 (HDTV)` 时，此参数适用。

## 所属库

Vision HDL Toolbox / Conversions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015a 中引入**

### R2022a: 每时钟两个像素的流传输

此模块现在支持每时钟周期具有 2 个像素的多像素流。

### R2021b: 多像素流传输

Color Space Converter 模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

该模块支持 *NumPixels*×3 值的输入矩阵，以及 *NumPixels*×*NumComponents* 值的输出矩阵，其中 *NumComponents* 为 3 或 1。**ctrl** 端口保持标量，并且 `pixelcontrol` 总线中的控制信号应用于矩阵中的所有像素。

## 描述

在色彩空间之间转换颜色信息

Color Space Converter 模块在 R'G'B' 和 Y'CbCr 色彩空间之间转换，还可将 R'G'B' 转换为强度。

**注意**

Color Space Converter 模块作用于伽马校正后的色彩空间，通常用撇号表示法 (') 表示。但是，为简单起见，模块和掩码标签不包括撇号表示法。
