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

### **Port\_1** — 要可视化的一个或多个信号 scalar | vector | matrix | array

连接要可视化的信号。最多可以有 96 个输入端口。输入信号必须具有以下特征：

- 通道数固定，但大小可以可变
- 离散、连续或恒定采样时间
- 实数或复数值
- 浮点或定点数据类型
- 二维且非标量

Array Plot 模块支持具有不同帧长度的输入。

此模块接受定点输入，但会将其转换为 `double` 以进行显示。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** 是

## 参数

未在 R2025b 中记录。

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

在生成代码的系统中，此模块可用于仿真可视化，但不会包含在生成的代码中。

## 版本历史

**在 R2015b 中推出**

### R2025a：单独控制每条线的绘图类型

现在可以单独控制每条线的绘图类型。要控制某条线的绘图类型，请选择该线，并相应地设置 **Plot Type** 参数。

### R2024b：支持条形图

Array Plot 模块现在支持条形图。要使用条形图查看数据，请在 Array Plot 设置 > **Color and Styling** 中将 **Plot Type** 设置为 `Bar`。

### R2024b：支持多个显示区

点击 **Scope** 选项卡中新增的 **Display Grid** 属性，指定 Array Plot 示波器显示区的布局。例如，选择 2×2 布局时，示波器会显示四个按 2×2 矩阵排列的显示区。显示网格最多可包含五行五列。

### R2024b：指定活动显示区

现在，可以使用 Array Plot 设置 > **Display and Labels** 中的 **Active Display** 属性指定活动显示区。**Y-Limits**、**X-Label**、**Y-Label**、**Show Legend**、**Show Grid**、**Title** 和 **Magnitude Phase Plot** 属性中的设置仅影响活动显示区。

### R2024b：示波器 UI 中更高的显示精度

现在，可以使用示波器设置中 **Display and Labels** 下的 **Display Precision** 属性，将显示精度提高到 15 位数字。此精度会影响示波器在其状态栏上显示的所有测量值和数据。

### R2024b：**Preserve Colors** 现已在示波器工具条中提供

**Preserve colors for copy to clipboard** 属性已重命名为 **Preserve Colors**，现在可在示波器工具条的 **Copy Display** 下找到。

### R2024b：**Magnitude Phase** 属性现已在 Array Plot 设置中提供

**Magnitude Phase** 属性已重命名为 **Magnitude Phase Plot**，现在可在 Array Plot 设置 > **Display and Labels** 中找到。

### R2024b：**Show Legend** 属性现在也可在 Array Plot 设置中找到

**Show Legend** 属性现在也可在 Array Plot 设置 > **Display and Labels** 中找到。要控制图例显示，可以在 Array Plot 工具条的 **Scope** 选项卡中选择 **Legend**，也可以选择 **Show Legend** 属性。

### R2024a：**Plot** 选项卡已重命名为 **Scope** 选项卡

Array Plot 中的 **Plot** 选项卡已重命名为 **Scope** 选项卡。

## 描述

显示向量或数组

Array Plot 模块绘制数据向量或数组。

Array Plot 模块窗口

Array Plot 是一种向量图，其中数据沿 *x* 轴均匀间隔分布。要修改此间距，请更改 `Sample Increment` 属性。

可用的测量功能：

- 数据游标 — 使用垂直和水平游标测量信号值。
- 信号统计信息 — 显示所选信号的最大值、最小值、峰峰值、均值、中位数和 RMS 值。
- 峰值查找器 — 查找极大值，并显示这些极大值出现位置对应的 *x* 轴值。
