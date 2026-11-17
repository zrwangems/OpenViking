---
type: simulink-block
title: 'Color Space Converter'
family: 'visionhdl'
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
```yaml
ports:
- name: pixel
  summary: 输入像素流 向量 | 矩阵
  direction: input
  data_types: uint8 | uint16 | fi(0,N,0), where N = 8,9,...,16 | single | double
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: input
  data_types: bus
- name: pixel
  summary: 新颜色空间中的输出像素流 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | uint8 | uint16 | fixed point
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: output
  data_types: bus
```

### 输入

### **pixel** — 输入像素流 向量 | 矩阵

对于标量像素流，将 **pixel** 指定为 1×3 值的向量。对于多像素流，将 **pixel** 指定为 **Number of pixels**×3 像素强度值的矩阵。**Number of pixels** 可以为二、四或八。

像素流必须处于 Y'CbCr 或 R'G'B' 颜色空间。整数和定点数据类型必须介于 8 到 16 位之间。值必须为无符号。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `fi(0,N,0), where N = 8,9,...,16` | `single` | `double`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`
### 输出

### **pixel** — 新颜色空间中的输出像素流 标量 | 向量 | 矩阵

以强度、Y'CbCr 或 R'G'B' 颜色空间返回的输出像素流，以单像素流或多像素流形式返回。输出流的数据类型和 **Number of pixels** 与输入像素流相同。如果输出为强度值，则每个像素有一个分量。如果输出为 Y'CbCr 或 R'G'B'，则每个像素有三个分量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `fixed point`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Conversion
  summary: 颜色空间转换类型 RGB to YCbCr（默认）| YCbCr to RGB | RGB to intensity
  group: ''
- name: Use conversion specified by
  summary: 转换方程 Rec. 601 (SDTV)（默认）| Rec. 709 (HDTV)
  group: ''
- name: Scanning standard
  summary: HDTV 扫描标准 1250/50/2:1（默认）| 1125/60/2:1
  group: ''
```

### **Conversion** — 颜色空间转换类型 `RGB to YCbCr`（默认）| `YCbCr to RGB` | `RGB to intensity`

该模块接受输入像素为表示单个像素的三个值的向量。如果选择 `RGB to intensity`，则每个输出像素为标量。否则，每个输出像素为三个值的向量。

### **Use conversion specified by** — 转换方程 `Rec. 601 (SDTV)`（默认）| `Rec. 709 (HDTV)`

用于 R'G'B' 和 Y'CbCr 颜色空间之间的转换方程。

#### 依赖关系

此参数仅在将 **Conversion** 设置为 `RGB to YCbCr` 或 `YCbCr to RGB` 时适用。

### **Scanning standard** — HDTV 扫描标准 `1250/50/2:1`（默认）| `1125/60/2:1`

用于在 HDTV 格式下 R'G'B' 和 Y'CbCr 颜色空间之间转换的扫描标准。

#### 依赖关系

此参数在将 **Use conversion specified by** 设置为 `Rec. 709 (HDTV)` 时适用。
## 所属库

Vision HDL Toolbox / Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015a 中引入**

### R2022a: 每时钟两像素流式传输

该模块现在支持每时钟周期 2 个像素的多像素流。

### R2021b: 多像素流式传输

Color Space Converter 模块现在支持多像素流。HDL 实现为每个像素并行复制算法。

该模块支持 *NumPixels*×3 值的输入矩阵，以及 *NumPixels*×*NumComponents* 值的输出矩阵，其中 *NumComponents* 为 3 或 1。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号应用于矩阵中的所有像素。

## 描述

在颜色空间之间转换颜色信息

Color Space Converter 模块在 R'G'B' 和 Y'CbCr 颜色空间之间转换，并且还将 R'G'B' 转换为强度。

**注意**

Color Space Converter 模块对经过伽马校正的颜色空间进行操作，通常用撇号表示法（'）表示。但是，为简单起见，模块和掩码标签不包含撇号表示法。
