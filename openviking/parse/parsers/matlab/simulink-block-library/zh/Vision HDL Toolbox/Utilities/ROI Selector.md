---
type: simulink-block
title: 'ROI Selector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'roiselector'
documentation_source_path: 'ref/roiselector.html'
language: zh-CN
chinese_source: worker-translation
---

# ROI Selector

## 端口
```yaml
ports:
- name: pixel
  summary: 输入像素流 标量 | 向量 | 矩阵
  direction: input
  data_types: uint | int | fixed point | Boolean | double | single
- name: ctrl
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: input
  data_types: bus
- name: region1,...,regionR
  summary: 感兴趣区域 四元素行向量
  direction: input
  data_types: int | uint
- name: pixel1,...,pixelR
  summary: 输出像素流 标量 | 向量 | 矩阵
  direction: output
  data_types: uint | int | fixed point | Boolean | double | single
- name: ctrl1,...,ctrlR
  summary: 控制信号 pixelcontrol 总线
  direction: output
  data_types: bus
```

### 输入

### **pixel** — 输入像素流 标量 | 向量 | 矩阵

对于单像素流，将 **pixel** 指定为标量或 1×**Number of components** 个值的向量。对于多像素流，将 **pixel** 指定为 **Number of pixels**×**Number of components** 个像素强度值的矩阵。**Number of pixels** 可以为二、四或八。

从 R2025a 开始，该软件支持 `single` 数据类型用于仿真和 HDL 代码生成。要在您的模型中为 `single` 数据类型启用 HDL 代码生成，请打开 **HDL Coder** 应用，转到 **Floating Point** 窗格，然后选中 **Use Floating Point** 复选框。`double` 数据类型仅支持仿真，不支持 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

对于多像素流，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

### **region1,...,regionR** — 感兴趣区域 四元素行向量

感兴趣区域，指定为四个正整数的行向量，用于定义每个所需输出帧左上角的坐标和尺寸。该向量必须具有 `[hPos vPos hSize vSize]` 的形式。该模块具有 *R* 个区域端口，其中 *R* 是 **Number of regions** 参数值。

对于多像素流，区域必须满足以下条件，其中 *M* 是 **Number of pixels**。

- `mod(hPos, M) = 1` — 例如，如果您的像素流每周期有四个像素，则 `129` 是 *hPos* 的有效值（`mod(129,4) = 1`），而 `128` 无效（`mod(128,4) = 0`）。
- `mod(hSize, M) = 0` — 例如，如果您的像素流每周期有四个像素，则 `120` 是 *hSize* 的有效值（`mod(120,4) = 0`），而 `118` 无效（`mod(118,4) = 2`）。

#### 依赖关系

要启用此端口，请清除 **Reuse output ports for vertically aligned regions** 参数，并将 **Regions source** 参数设置为 `Input port`。

**数据类型：** `int` | `uint`
### 输出

### **pixel1,...,pixelR** — 输出像素流 标量 | 向量 | 矩阵

输出像素，以单像素或多像素流形式返回。输出维度和数据类型与输入 **pixel** 端口匹配。默认情况下，该模块具有 *R* 个输出 **pixel** 端口，其中 *R* 是 **Number of regions** 参数，或 **Regions** 参数矩阵中的行数。

当您选中 **Reuse output ports for vertically aligned regions** 时，该模块为每一列垂直对齐的区域提供一个输出 **pixel** 端口。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl1,...,ctrlR** — 控制信号 `pixelcontrol` 总线

控制信号，以包含五个信号的 `pixelcontrol` 总线形式返回。默认情况下，该模块具有 *R* 个输出 **ctrl** 端口，其中 *R* 是 **Number of regions** 参数，或 **Regions** 参数矩阵中的行数。

当您选中 **Reuse output ports for vertically aligned regions** 时，该模块为每一列对齐的区域提供一个输出 **ctrl** 端口。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Reuse output ports for vertically aligned regions
  summary: 为垂直对齐的区域返回单个像素流的选项 off（默认）| on
  group: ''
- name: Regions source
  summary: 输出区域定义的位置 Property（默认）| Input port
  group: ''
- name: Regions
  summary: 要从输入帧中选择的矩形 ROI *R*×4 矩阵
  group: ''
- name: Number of regions
  summary: 区域输入端口数量 [1, 16] 范围内的整数
  group: ''
```

### **Reuse output ports for vertically aligned regions** — 为垂直对齐的区域返回单个像素流的选项 `off`（默认）| `on`

当您选择此参数时，必须指定没有垂直重叠且按列对齐的区域。该模块为每一列区域提供一个输出像素流。这种安排使得每一列可以并行处理，并且可以复用一列中每个区域的下游处理逻辑。使用 `visionhdlframetoregions` 函数将帧划分为用于垂直复用的平铺区域。

#### 依赖关系

要启用此参数，请将 **Regions source** 参数设置为 `Property`。

### **Regions source** — 输出区域定义的位置 `Property`（默认）| `Input port`

指定输出区域定义的位置。您可以将 **Regions source** 设置为以下值之一：

- `Property` — 使用 **Regions** 参数指定区域。
- `Input port` — 使用输入端口指定区域。每个输入端口对应一个区域。当输入控制总线中的 `vStart` 为 `true` 时，该模块对 **region** 输入端口进行采样。

#### 依赖关系

要启用此参数，请清除 **Reuse output ports for vertically aligned regions** 参数。

### **Regions** — 要从输入帧中选择的矩形 ROI *R*×4 矩阵

指定要从输入帧中选择的矩形 ROI，形式为 *R*×4 矩阵。

*R* 是区域数量。定义每个区域的四个元素是左上角起始坐标以及区域的尺寸，必须采用 `[hPos
vPos
hSize
vSize]` 的形式。坐标从活动帧的左上角开始计数，定义为 [1,1]。*hSize* 必须大于 1。

对于多像素流式传输，区域必须满足以下条件，其中 *M* 是 **Number of pixels**。

- `mod(hPos, M) = 1` — 例如，如果您的像素流每个周期有四个像素，则 `129` 是 *hPos* 的有效值（`mod(129,4) = 1`），而 `128` 无效（`mod(128,4) = 0`）。
- **`mod(hSize, M) =
  0`** — 例如，如果您的像素流每个周期有四个像素，则 `120` 是 *hSize* 的有效值（`mod(120,4)
  = 0`），而 `118` 无效（`mod(118,4) =
  2`）。

当您清除 **Reuse output ports for vertically aligned regions** 参数时，区域可以重叠，并且 *R* 不得大于 16。

当您选择 **Reuse output ports for vertically aligned regions** 时，此矩阵中的区域不得有垂直重叠，并且必须按列对齐。此图显示了两个用蓝色虚线轮廓标出的无效区域示例。左侧的区域与另一个区域垂直重叠。底部的两个区域与其所在列中的其他区域不对齐。区域不必覆盖整个帧。平铺区域之外的像素被标记为非活动像素。列数不得大于 16。

#### 依赖关系

要启用此参数，请将 **Regions source** 参数设置为 `Property`。

### **Number of regions** — 区域输入端口数量 [1, 16] 范围内的整数

将区域输入端口数量指定为 [1, 16] 范围内的整数。

#### 依赖关系

要启用此参数，请将 **Regions source** 参数设置为 `Input port`。
## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2016a 中引入**

### R2025a：支持 `single` 数据类型用于 HDL 代码生成

该模块现在支持使用 `single` 数据类型像素输入进行 HDL 代码生成。

### R2023a：每时钟两像素流式传输

该模块现在支持每时钟周期 2 像素的多像素流。

### R2021a：多像素多分量流式传输

该模块现在支持同时为多像素和多分量的流。HDL 实现会为每个像素和分量并行复制该算法。

该模块支持 *NumPixels*-乘-*NumComponents* 像素的输入和输出矩阵。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号应用于矩阵中的所有像素。

### R2021a：资源共享

该模块现在提供在您选择垂直对齐区域时共享硬件资源的选项。同一列中的区域共享相同的 `pixelcontrol` 总线输出。

选中 **Reuse output ports for vertically aligned regions** 复选框，并提供一组按列对齐且在每个列内垂直方向不重叠的区域。您可以为每列指定最多 1024 个区域。要将帧划分为与垂直复用兼容的平铺区域，请使用 `visionhdlframetoregions` 函数。

## 描述

从像素流中选择感兴趣区域（ROI）

ROI Selector 模块从视频流的活动帧中选择一部分。非活动帧的大小保持不变。输出控制信号指示帧的新活动区域。您可以将此模块用于单像素、多像素或多像素多分量像素流。下图以蓝色显示非活动像素区域，并以橙色轮廓显示所请求的输出区域。

将输入帧的指定区域作为像素流返回，该区域之外的像素被标记为非活动。

您可以为 ROI 指定固定的大小和位置，也可以通过输入端口动态选择区域位置。您可以选择多个区域。通过指定每个区域的左上角坐标和尺寸来定义每个区域。默认情况下，该模块为您指定的每个区域返回一组像素和控制信号。该模块将输出帧中的非活动像素设置为零。

各区域彼此独立，因此它们可以重叠。如果您指定的区域包含活动帧的边缘，则该模块仅返回该区域的活动部分。下图显示了三个所请求区域的输出帧。第二个输出区域不包括图像上方的非活动区域。

三个区域（一个部分落在活动帧之外，一个与另一个重叠）作为三个像素流返回。

该模块还提供了一种垂直复用模式。在此模式下，您必须指定没有垂直重叠且按列对齐的区域。每一列区域共享一个输出像素流。控制信号定义流中的每个区域。这种安排使得每一列可以并行处理，并且可以为一列中的每个区域复用下游处理逻辑。要使用此模式，请选择 **Reuse output ports for vertically aligned regions** 参数。使用 `visionhdlframetoregions` 函数将帧划分为用于垂直复用的平铺区域。

八个平铺区域作为两个输出像素流返回，每个输出像素流包含四个垂直对齐的区域。
