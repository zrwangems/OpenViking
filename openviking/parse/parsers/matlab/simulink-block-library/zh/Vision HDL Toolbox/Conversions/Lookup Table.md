---
type: simulink-block
title: 'Lookup Table'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'lookuptable'
documentation_source_path: 'ref/lookuptable.html'
language: zh-CN
chinese_source: worker-translation
---

# Lookup Table

## 端口
```yaml
ports:
- name: pixel
  summary: 输入像素流 标量 | 向量
  direction: input
  data_types: uint8 | uint16 | fixdt(0,N,F), N <= 16 | Boolean
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: input
  data_types: bus
- name: pixel
  summary: 输出像素流 标量 | 向量
  direction: output
  data_types: uint8 | uint16 | int8 | int16 | fixed point | Boolean | double | single
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: output
  data_types: bus
```

### 输入

### **pixel** — 输入像素流 标量 | 向量

对于单像素流，将 **pixel** 指定为标量强度值或 **Number of components** 个值的行向量。对于多像素流，将 **pixel** 指定为 **Number of pixels** 个像素强度值的列向量。**Number of pixels** 可以为二、四或八。此模块不支持多像素多分量流。

不支持大于 16 位的整数和定点数据类型。不支持有符号数据类型。

**数据类型：** `uint8` | `uint16` | `fixdt(0,N,F), N <= 16` | `Boolean`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`
### 输出

### **pixel** — 输出像素流 标量 | 向量

输出 **pixel** 的维度与输入 **pixel** 的维度匹配。该模块将输出 **pixel** 返回为标量、**Number of components** 个值的行向量或 **Number of pixels** 个值的列向量。

数据类型由 **Table data** 参数指定。

**数据类型：** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量有一组控制信号。由于该向量只有一个 `valid` 信号，向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Table data
  summary: 输入像素与输出像素之间的映射 uint8(0:1:255)（默认）| 向量
  group: ''
```

### **Table data** — 输入像素与输出像素之间的映射 `uint8(0:1:255)`（默认）| 向量

输入像素与输出像素之间的映射，指定为任意数据类型的行向量或列向量。表数据的数据类型决定输出 **pixel** 的数据类型。此映射决定输入 **pixel** 值与输出 **pixel** 值之间的一一对应关系。

- 向量的长度必须为 2*WordLength*，其中 *WordLength* 是输入 **pixel** 的大小（以位为单位）。Lookup Table 模块不执行插值。每个输入值必须在表中具有对应的输出值。
- 输入数据类型的最小可表示值映射到表的第一个元素，第二个最小值映射到第二个元素，依此类推。例如，如果输入 **pixel** 的数据类型为 `fixdt(0,3,1)`，则输入值 0 映射到表的第一个元素，0.5 映射到第二个元素，1 映射到第三个元素，依此类推。

当输入 **pixel** 为向量时，模块为向量的每个元素复制查找表。在这种情况下，表使用 *VectorSize*×2*WordLength* 个存储位置。

从 R2025a 开始，软件支持 `single` 数据类型用于仿真和 HDL 代码生成。要在您的模型中为 `single` 数据类型启用 HDL 代码生成，请打开 **HDL Coder** 应用，转到 **Floating Point** 窗格，然后选中 **Use Floating Point** 复选框。`double` 数据类型仅支持仿真，不支持 HDL 代码生成。

**示例：** `uint8(linspace(255,0,256))`

**数据类型：** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `Boolean` | `double` | `single`
## 所属库

Vision HDL Toolbox / Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **LUTRegisterResetType** | 查找表输出寄存器的复位类型。当您的目标为 FPGA 时，选择 `none` 将查找表综合为 ROM。另请参阅 LUTRegisterResetType (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015a 中引入**

### R2025a：支持 `single` 数据类型用于 HDL 代码生成

此模块现在支持使用 `single` 数据类型对 **Table data** 值进行 HDL 代码生成。

### R2023a：每时钟两像素流式传输

此模块现在支持每时钟周期 2 个像素的多像素流。

### R2020b：多像素流式传输

查找表模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。不能同时使用多分量和多像素。

对于多像素流式传输，这些模块支持 4 或 8 像素的输入和输出列向量。**ctrl** 端口仍为标量，`pixelcontrol` 总线中的控制信号适用于该向量中的所有像素。

## 描述

使用自定义规则将输入像素映射为输出像素

查找表模块提供输入像素值与输出像素值之间的自定义一对一映射。
