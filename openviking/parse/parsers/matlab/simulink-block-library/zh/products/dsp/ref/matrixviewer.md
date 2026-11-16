---
type: simulink-block
title: 'Matrix Viewer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Scopes and Data Logging'
documentation_page: 'matrixviewer'
documentation_source_path: 'ref/matrixviewer.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Viewer

## 端口

R2025b 中未提供文档。

## 参数

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可在生成 HDL 代码的子系统中用于仿真可视化，但不会包含在硬件实现中。

## 版本历史

**在 R2006a 之前引入**

### R2020b：Matrix Viewer 模块将被移除

Matrix Viewer 模块将在未来版本中移除。请改用其他示波器，请参阅“示波器和数据记录”。

## 描述

（将被移除）以彩色图像形式显示矩阵

Matrix Viewer 模块通过将矩阵元素值映射到指定的颜色范围来显示 *M*×*N* 矩阵输入。每接收到一个新的输入，显示就会更新。此模块将长度为 *M* 的无方向向量输入视为 *M*×1 矩阵。

您可以在以 Normal 或 Accelerator 仿真模式运行的模型中使用 Matrix Viewer 模块。该软件不支持在以 Rapid Accelerator 或 External 模式运行的模型中使用此模块。有关这些模式的详细信息，请参阅《Simulink® 用户指南》中的 How Acceleration Modes Work (Simulink)。

### 图像属性

选择 **Image Properties** 选项卡可显示图像属性参数，这些参数控制颜色图和显示。

您可以通过 **Colormap matrix**、**Minimum input value** 和 **Maximum input value** 参数指定矩阵元素值到颜色的映射。对于包含 *L* 种颜色的颜色图，颜色图矩阵的维度为 *L*×3，每种颜色对应一行，定义该颜色的 RGB 三元组中的每个元素对应一列。RGB 三元组示例如下：

```
[ 1   0   0 ]   (red)
[ 0   0   1 ]   (blue)
[0.8 0.8 0.8]   (light gray)
```

MATLAB® 提供了许多用于生成预定义颜色图的函数，例如 `hot`、`cool`、`bone` 和 `autumn`。这些函数都接受颜色图大小作为参数，并可用于 **Colormap matrix** 参数。例如，当您在 **Colormap matrix** 参数中指定 `gray(128)` 时，矩阵将以 128 种灰度显示。颜色图矩阵第一行中的颜色表示 **Minimum input value** 参数指定的值，最后一行中的颜色表示 **Maximum input value** 参数指定的值。最小值和最大值之间的值会被量化，并映射到颜色图矩阵的中间行。

MATLAB `colormap` 函数的文档提供了有关指定颜色图矩阵的完整信息，并包含可用颜色图函数的完整列表。

### 坐标轴属性

选择 **Axis Properties** 选项卡可显示坐标轴属性参数，这些参数控制标注和定位。

**Axis origin** 参数确定输入矩阵的第一个元素 *U*(1,1) 的显示位置。指定为 `Upper left corner` 时，矩阵按矩阵方向显示，*U*(1,1) 位于左上角。

[U11U12U13U14U21U22U23U24U31U32U33U34U41U42U43U44]

指定为 `Lower left corner` 时，矩阵将垂直翻转为图像方向，*U*(1,1) 位于左下角。

[U41U42U43U44U31U32U33U34U21U22U23U24U11U12U13U14]

选中 **Axis zoom** 后，图像显示将完全填满图窗，并且不显示坐标轴标题。也可以通过在图窗中右键单击时显示的弹出菜单选择此选项。取消选中 **Axis zoom** 后，坐标轴标签和标题将显示在围绕图像坐标轴的灰色边框内。

要自定义坐标轴刻度范围，请将 **Axis tick mode** 设置为 `User-defined`，并在 **X-tick range** 和 **Y-tick range** 中指定一个二元素行向量 [`Minvalue Maxvalue`]。即使坐标轴刻度发生变化，矩阵数据也不会改变。例如，假设在刻度范围为 0 到 10 的坐标轴上显示一个矩阵。当您将 **X-tick range** 和 **Y-tick range** 设置为 [0 1] 时，刻度范围会从 [0 10] 变为 [0 1]。

### 图窗

图窗标题栏中的图像标题与模块标题相同。坐标轴刻度反映输入矩阵的大小；*x* 轴的编号范围为 1 到 *N*（列数），*y* 轴的编号范围为 1 到 *M*（行数）。

在图窗中右键单击图像可访问以下菜单项：

- **Refresh** 会擦除示波器显示区中除最新图像之外的所有数据。
- **Autoscale** 会重新计算最小和最大输入值，以适应在连续 10 个输入中观测到的值范围。自动缩放功能选择的数值限值显示在 **Minimum input value** 和 **Maximum input value** 参数中，您可以在其中进一步手动调整这些值。
- 选中 **Axis zoom** 后，图像将完全填满图窗，并且不显示坐标轴标题。取消选中 **Axis zoom** 后，坐标轴标签和标题将显示在围绕示波器坐标轴的灰色边框内。也可以在参数对话框的 **Axis Properties** 窗格中设置此选项。
- 选中 **Colorbar** 后，会在图像坐标轴右侧显示一个采用指定颜色图的颜色条。
- **Save Position** 会自动更新 **Axis Properties** 窗格中的 **Figure position** 参数，以反映图窗当前在屏幕上的位置和大小。要使示波器窗口在仿真运行时于屏幕上的特定位置打开，请将窗口拖动到所需位置、调整其大小，然后选择 **Save Position**。选择 **Save Position** 时必须关闭参数对话框，**Figure position** 参数才会更新。
