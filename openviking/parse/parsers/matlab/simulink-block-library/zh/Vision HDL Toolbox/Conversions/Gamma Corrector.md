---
type: simulink-block
title: 'Gamma Corrector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'gammacorrector'
documentation_source_path: 'ref/gammacorrector.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamma Corrector

## 端口
```yaml
ports:
- name: pixel
  summary: 输入像素流 标量 | 向量
  direction: input
  data_types: uint8 | uint16 | int8 | int16 | fixed point | double | single
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: input
  data_types: bus
- name: pixel
  summary: 输出像素流 标量 | 向量
  direction: output
  data_types: uint8 | uint16 | int8 | int16 | fixed point | double | single
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: output
  data_types: bus
```

### 输入

### **pixel** — 输入像素流 标量 | 向量

对于单像素流，将 **pixel** 指定为标量强度值。对于多像素流，将 **pixel** 指定为 **Number of pixels**×1 的像素强度值向量。**Number of pixels** 可以为 2、4 或 8。不支持大于 16 位的整数和定点数据类型。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### 输出

### **pixel** — 输出像素流 标量 | 向量

图像像素，以标量值或值向量形式返回。输出 **pixel** 流的数据类型和维度与输入 **pixel** 流匹配。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Operation
  summary: 像素值调整方向 Gamma（默认）| De-gamma
  group: ''
- name: Gamma
  summary: 目标伽马值 2.2（默认）| 大于或等于 1 的标量
  group: ''
- name: Linear segment
  summary: 在伽马曲线中包含线性段 on（默认）| off
  group: ''
- name: Break point
  summary: 伽马曲线与线性段相交的点 0.018（默认）| 0 到 1 之间的标量
  group: ''
```

### **Operation** — 像素值调整方向 `Gamma`（默认）| `De-gamma`

像素值调整方向，指定为以下选项之一：

- `Gamma` — 应用伽马校正。
- `De-gamma` — 移除伽马校正。

### **Gamma** — 目标伽马值 `2.2`（默认）| 大于或等于 1 的标量

目标伽马值，指定为大于或等于 1 的标量。

- 当将 **Operation** 设置为 `Gamma` 时，**Gamma** 是输出视频流的目标伽马值。
- 当将 **Operation** 设置为 `De-gamma` 时，**Gamma** 是输入视频流的伽马值。

### **Linear segment** — 在伽马曲线中包含线性段 on（默认）| off

在伽马曲线中包含线性段的选项。选中此复选框时，伽马曲线在原点附近具有线性部分。

### **Break point** — 伽马曲线与线性段相交的点 `0.018`（默认）| 0 到 1 之间的标量

对应于伽马曲线与线性段相交点的像素值，指定为 0 到 1 之间（不含端点）的标量值。

#### 依赖关系

此参数仅在选中 **Linear segment** 复选框时适用。
## 所属库

Vision HDL Toolbox / Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式的 C/C++ 代码生成，以及用于 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **LUTRegisterResetType** | 查找表输出寄存器的复位类型。当目标为 FPGA 时，选择 `none` 将查找表综合为 ROM。另请参阅 LUTRegisterResetType (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015a 中引入**

### R2022b: 多像素流

该模块现在支持多像素流。HDL 实现会为每个像素并行复制该算法。

对于多像素流，该模块支持 2、4 或 8 像素的输入和输出列向量。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号适用于向量中的所有像素。

## 描述

对像素流应用或移除伽马校正

Gamma Corrector 对像素流应用或移除伽马校正。伽马校正调整线性像素值，使修改后的值拟合一条曲线。去伽马操作执行相反操作以获得线性像素值。
