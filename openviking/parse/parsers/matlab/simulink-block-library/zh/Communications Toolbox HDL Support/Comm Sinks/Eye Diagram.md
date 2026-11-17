---
type: simulink-block
title: 'Eye Diagram'
family: 'communications-toolbox-hdl-support'
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
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 列向量
  direction: input
  data_types: double
```

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Samples per symbol
  summary: 每符号采样数 8（默认）| 正整数
  group: 显示与轨迹
- name: Sample offset
  summary: 采样偏移 0（默认）| 非负整数
  group: 显示与轨迹
- name: Symbols per trace
  summary: 每轨迹符号数 2（默认）| 正整数
  group: 显示与轨迹
- name: Traces to display
  summary: 要显示的轨迹数 40（默认）| 正整数
  group: 显示与轨迹
- name: Color fading
  summary: 颜色渐隐 off（默认）| on
  group: 显示与轨迹
- name: Plot Imaginary Axes
  summary: 绘制虚轴 on（默认）| off
  group: 显示与轨迹
- name: Real axes label
  summary: 实轴标签 Real Amplitude（默认）
  group: 坐标轴与标签
- name: Title
  summary: 标题标签 *None*（默认）
  group: 坐标轴与标签
- name: Imaginary axes label
  summary: 虚轴标签 Imaginary Amplitude（默认）
  group: 坐标轴与标签
- name: Y-limits
  summary: 上下限值 [-1.1,1 1]（默认）| 标量
  group: 坐标轴与标签
- name: Show grid
  summary: 在绘图上显示网格 on（默认）| off
  group: 坐标轴与标签
- name: Preserve colors for copy to clipboard
  summary: 复制到剪贴板时保留颜色 off（默认）| on
  group: 颜色与样式
- name: Background
  summary: 背景颜色 black（默认）
  group: 颜色与样式
- name: Axes
  summary: 坐标轴颜色 black（默认）
  group: 颜色与样式
- name: Labels
  summary: 标签颜色 grey（默认）
  group: 颜色与样式
- name: Style
  summary: 线型 continuous（默认）
  group: 颜色与样式
- name: Width
  summary: 线图粗细 1.5（默认）
  group: 颜色与样式
- name: Marker
  summary: 数据点标记 None（默认）| ...
  group: 颜色与样式
- name: Color
  summary: 线条颜色 yellow（默认）
  group: 颜色与样式
```

### 显示与轨迹

### **Samples per symbol** — 每符号采样数 8（默认）| 正整数

每符号的采样数，指定为正整数。与 **Symbols per trace** 一起使用以确定每条轨迹的采样数。

**可调：** 是

### **Sample offset** — 采样偏移 0（默认）| 非负整数

采样偏移，指定为小于 **Samples per symbol** 与 **Symbols per trace** 乘积的非负整数。该偏移提供了在绘制第一个点之前要省略的采样数。

**可调：** 是

### **Symbols per trace** — 每轨迹符号数 2（默认）| 正整数

每条轨迹绘制的符号数，指定为正整数。

**可调：** 是

### **Traces to display** — 要显示的轨迹数 40（默认）| 正整数

绘制的轨迹数，指定为正整数。

**可调：** 是

#### 依赖关系

### **Color fading** — 颜色渐隐 `off`（默认）| `on`

选中此复选框可在点首次绘制后的时间间隔增加时使显示中的点渐隐。

### **Plot Imaginary Axes** — 绘制虚轴 `on`（默认）| `off`

选中此复选框可显示眼图的虚部图。

### 坐标轴与标签

### **Real axes label** — 实轴标签 `Real Amplitude`（默认）

示波器沿实轴显示的文本。

**可调：** 是

### **Title** — 标题标签 *None*（默认）

显示在眼图绘图上方的标签。

**可调：** 是

### **Imaginary axes label** — 虚轴标签 `Imaginary Amplitude`（默认）

示波器沿虚轴显示的文本。

**可调：** 是

### **Y-limits** — 上下限值 `[-1.1,1 1]`（默认）| 标量

*y* 轴的上下限值。

**可调：** 是

### **Show grid** — 在绘图上显示网格 `on`（默认）| `off`

选择此单选按钮可在示波器窗口上显示网格。

### 颜色与样式

使用此选项卡可自定义活动显示的样式。您可以更改包含显示的图窗颜色、显示坐标轴的背景色和前景色，以及显示中线条的属性。

### **Preserve colors for copy to clipboard** — 复制到剪贴板时保留颜色 `off`（默认）| `on`

选择此单选按钮可在复制到剪贴板时保留颜色。

### **Background** — 背景颜色 `black`（默认）

指定绘图的背景颜色。

### **Axes** — 坐标轴颜色 `black`（默认）

指定坐标轴的填充和线条颜色。

### **Labels** — 标签颜色 `grey`（默认）

指定坐标轴上标签的颜色。

### **Style** — 线型 `continuous`（默认）

指定所显示信号的线型。

### **Width** — 线图粗细 `1.5`（默认）

指定所显示信号线条的粗细。

### **Marker** — 数据点标记 `None`（默认）| ...

所选信号的数据点标记，指定为此表数据点标记中的选项之一。此参数类似于 MATLAB® Handle Graphics® 绘图对象的 `Marker` 属性。

| 符号 | 标记类型 |
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

### **Color** — 线条颜色 `yellow`（默认）

指定所显示信号线条的颜色。
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

当对包含此模块的系统执行代码生成时，此模块将从生成的代码中排除。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可视化，但不包含在硬件实现中。

## 版本历史

**在 R2023b 中引入**

## 描述

显示时域信号的眼图

Eye Diagram 模块显示调制信号的多个轨迹以生成眼图。您可以使用该模块揭示信号的调制特性，例如脉冲整形或信道失真的影响。

Eye Diagram 模块有一个输入端口。此模块接受列向量或标量输入信号。该模块接受具有以下数据类型的信号：double、single、基整数和定点。在模块显示结果之前，所有数据类型都被转换为 double。

要修改眼图显示，请选择 **SCOPE** 并单击 **CONFIGURATION** 中的 **Settings** 按钮（）。
