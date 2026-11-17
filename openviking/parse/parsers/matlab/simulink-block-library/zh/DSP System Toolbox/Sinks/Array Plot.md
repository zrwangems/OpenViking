---
type: simulink-block
title: 'Array Plot'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'arrayplot'
documentation_source_path: 'ref/arrayplot.html'
language: zh-CN
chinese_source: worker-translation
---

# Array Plot

## 端口

### 输入

### **Port\_1** — 要可视化的信号或信号组 标量 | 向量 | 矩阵 | 数组

连接您想要可视化的信号。您最多可以有 96 个输入端口。输入信号必须具有以下特征：

- 固定通道数，但大小可以可变
- 离散、连续或常量采样时间
- 实数值或复数值
- 浮点或定点数据类型
- 二维且非标量

Array Plot 模块支持具有不同帧长度的输入。

此模块接受定点输入，但会将其转换为 `double` 以进行显示。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** 是

## 参数

R2025b 中未记录。

## 所属库

DSP System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可视化，但不会包含在生成的代码中。

## 版本历史

**在 R2015b 中引入**

### R2025a：单独控制每条线的绘图类型

您现在可以单独控制每条线的绘图类型。要控制一条线的绘图类型，请选择该线并相应地设置 **Plot Type** 参数。

### R2024b：支持条形图

Array Plot 模块现在支持条形图。要使用条形图查看数据，请在 Array Plot 设置 > **Color and Styling** 中将 **Plot Type** 设置为 `Bar`。

### R2024b：支持多个显示

单击 **Scope** 选项卡中新增的 **Display Grid** 属性，以指定 Array Plot 示波器显示的布局。例如，当您选择 2×2 布局时，示波器会显示排列为 2×2 矩阵的四个显示。显示网格最多可以有五行五列。

### R2024b：指定活动显示

您现在可以使用 Array Plot 设置 > **Display and Labels** 中的 **Active Display** 属性指定活动显示。**Y-Limits**、**X-Label**、**Y-Label**、**Show Legend**、**Show Grid**、**Title** 和 **Magnitude Phase Plot** 属性中的设置仅影响活动显示。

### R2024b：示波器 UI 中更高的显示精度

您现在可以使用 **Display and Labels** 下的示波器设置中的 **Display Precision** 属性将显示精度提高到 15 位数字。此精度会影响示波器在其状态栏上显示的所有测量值和数据。

### R2024b：**Preserve Colors** 现在可在示波器工具条中使用

**Preserve colors for copy to clipboard** 属性已重命名为 **Preserve Colors**，现在可在 **Copy Display** 下的示波器工具条中使用。

### R2024b：**Magnitude Phase** 属性现在可在 Array Plot 设置中使用

**Magnitude Phase** 属性已重命名为 **Magnitude Phase Plot**，现在可在 Array Plot 设置 > **Display and Labels** 中使用。

### R2024b：**Show Legend** 属性现在也可在 Array Plot 设置中使用

**Show Legend** 属性现在也可在 Array Plot 设置 > **Display and Labels** 中使用。要控制图例显示，您可以在 Array Plot 工具条的 **Scope** 选项卡中选择 **Legend**，或选择 **Show Legend** 属性。

### R2024a：**Plot** 选项卡已重命名为 **Scope** 选项卡

Array Plot 中的 **Plot** 选项卡已重命名为 **Scope** 选项卡。

## 描述

显示向量或数组

Array Plot 模块绘制数据向量或数组。

Array Plot 模块窗口

Array Plot 是一种向量图，其中数据沿 *x* 轴均匀分布。要修改间距，请更改 `Sample Increment` 属性。

可用的测量：

- 数据光标 — 使用垂直和水平光标测量信号值。
- 信号统计 — 显示所选信号的最大值、最小值、峰峰值差、均值、中位数和 RMS 值。
- 峰值查找器 — 查找最大值，并显示它们出现时的 *x* 轴值。
