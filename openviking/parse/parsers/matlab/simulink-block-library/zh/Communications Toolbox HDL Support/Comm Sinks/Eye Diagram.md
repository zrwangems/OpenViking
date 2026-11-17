---
type: simulink-block
title: 'Eye Diagram'
family: 'comm-sinks'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Comm Sinks'
documentation_page: 'eyediagramscope'
documentation_source_path: '../comm/ref/eyediagramscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Eye Diagram

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。

**数据类型：** `double`

## 参数

### 显示和迹线

### **每符号样本数** — 每符号样本数 8 (默认) | 正整数

每个符号的样本数，指定为正整数。与 **每迹线符号数** 一起使用以确定每条迹线的样本数。

**可调：** 是

### **样本偏移** — 样本偏移 0 (默认) | 非负整数

样本偏移，指定为小于 **每符号样本数** 与 **每迹线符号数** 乘积的非负整数。该偏移提供了在绘制第一个点之前要省略的样本数。

**可调：** 是

### **每迹线符号数** — 每迹线符号数 2 (默认) | 正整数

每条迹线绘制的符号数，指定为正整数。

**可调：** 是

### **要显示的迹线数** — 要显示的迹线数 40 (默认) | 正整数

绘制的迹线数，指定为正整数。

**可调：** 是

#### 依赖关系

### **颜色淡化** — 颜色淡化 `off` (默认) | `on`

选中此复选框可在点首次绘制后的时间间隔增加时淡化显示中的点。

### **绘制虚轴** — 绘制虚轴 `on` (默认) | `off`

选中此复选框可显示眼图的虚部绘图。

### 坐标轴和标签

### **实轴标签** — 实轴标签 `Real Amplitude` (默认)

示波器沿实轴显示的文本。

**可调：** 是

### **标题** — 标题标签 *None* (默认)

显示在眼图绘图上方的标签。

**可调：** 是

### **虚轴标签** — 虚轴标签 `Imaginary Amplitude` (默认)

示波器沿虚轴显示的文本。

**可调：** 是

### **Y 轴范围** — 上下限值 `[-1.1,1 1]` (默认) | 标量

*y* 轴的上下限值。

**可调：** 是

### **显示网格** — 在绘图上显示网格 `on` (默认) | `off`

选中此单选按钮可在示波器窗口中显示网格。

### 颜色和样式

使用此选项卡可自定义活动显示的样式。您可以更改包含显示的图窗颜色、显示坐标轴背景色和前景色，以及显示中线条的属性。

### **复制到剪贴板时保留颜色** — 复制到剪贴板时保留颜色 `off` (默认) | `on`

选中此单选按钮可在复制到剪贴板时保留颜色。

### **背景** — 背景颜色 `black` (默认)

指定绘图背景颜色。

### **坐标轴** — 坐标轴颜色 `black` (默认)

指定坐标轴的填充和线条颜色。

### **标签** — 标签颜色 `grey` (默认)

指定坐标轴上标签的颜色。

### **样式** — 线型 `continuous` (默认)

指定显示信号的线型。

### **宽度** — 线图粗细 `1.5` (默认)

指定显示信号上线条的线宽。

### **标记** — 数据点标记 `None` (默认) | ...

所选信号的数据点标记，指定为此表格数据点标记中的一个选项。此参数类似于 MATLAB® Handle Graphics® 绘图对象的 `Marker` 属性。

| 说明符 | 标记类型 |
| --- | --- |
| none | 无标记（默认） |
|  | 圆形 |
|  | 方形 |
|  | 十字 |
|  | 点 |
|  | 加号 |
|  | 星号 |
|  | 菱形 |
|  | 向下三角形 |
|  | 向上三角形 |
|  | 向左三角形 |
|  | 向右三角形 |
|  | 五角星（五芒星） |
|  | 六角星（六芒星） |

### **颜色** — 线条颜色 `yellow` (默认)

指定显示信号上线条的颜色。

## 所属库

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks Mixed-Signal Blockset / Utilities SerDes Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当对包含此模块的系统执行代码生成时，此模块会从生成的代码中排除。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于在生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2023b 中引入**

## 描述

显示时域信号的眼图

Eye Diagram 模块显示调制信号的多条迹线以生成眼图。您可以使用该模块揭示信号的调制特性，例如脉冲成形或信道失真的影响。

Eye Diagram 模块有一个输入端口。此模块接受列向量或标量输入信号。该模块接受具有以下数据类型的信号：double、single、base integer 和 fixed point。所有数据类型在模块显示结果之前都会转换为 double。

要修改眼图显示，请选择 **SCOPE**，然后在 **CONFIGURATION** 中点击 **Settings** 按钮 ()。
