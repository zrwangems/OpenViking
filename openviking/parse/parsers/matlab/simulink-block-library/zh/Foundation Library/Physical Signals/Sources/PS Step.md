---
type: simulink-block
title: 'PS Step'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'psstep'
documentation_source_path: 'ref/psstep.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Step

## 端口

### 输出

### **O** — 输出物理信号，其类型由模块参数值和单位决定

输出物理信号。信号大小与 **Initial value** 和 **Final value** 参数值的大小匹配。信号单位由 **Initial value** 和 **Final value** 参数的单位确定。

端口名称在模块图标中不可见，但您可以单击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中查看此名称。

## 参数

### **Step time** — 阶跃发生的时间 `1 s`（默认） | 标量

信号改变值的时间。在仿真开始到 **Step time** 之间，模块输出保持在 **Initial value**，然后瞬时变为 **Final value**，并保持该值直到仿真结束。

### **Initial value** — 阶跃前的输出 `0 1`（默认） | 标量 | 向量 | 矩阵

在仿真时间达到 **Step time** 之前，模块输出。第一个编辑框表示参数值。您可以指定标量、向量或矩阵。默认情况下，该值为标量 `0`。如果指定向量或矩阵，则 **Final value** 也必须为相同大小的向量或矩阵，或者为标量。

第二个组合框表示参数单位。指定的单位必须与 **Final value** 参数的单位可换算。默认情况下，单位为 `1`（无单位）。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `Pa`）或有效表达式（如 `m^2`）。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

### **Final value** — 阶跃后的输出 `1 1`（默认） | 标量 | 向量 | 矩阵

当仿真时间达到并超过 **Step time** 时的模块输出。第一个编辑框表示参数值。您可以指定标量、向量或矩阵。默认情况下，该值为标量 `1`。如果指定向量或矩阵，则 **Initial value** 也必须为相同大小的向量或矩阵，或者为标量。

第二个组合框表示参数单位。指定的单位必须与 **Initial value** 参数的单位可换算。默认情况下，单位为 `1`（无单位）。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `Pa`）或有效表达式（如 `m^2`）。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

生成形状为阶跃函数的物理信号

PS Step 模块生成一个物理信号，该信号从指定的初始值开始，并在指定时间瞬时变为新值。**Step time**、**Initial value** 和 **Final value** 参数决定输出信号的特征：

- **Step time** 参数确定信号值从 **Initial value** 变为 **Final value** 的时间。
- **Initial value** 和 **Final value** 参数值确定输出信号是标量、向量还是矩阵。如果其中一个参数是向量或矩阵，则另一个必须是相同大小的向量或矩阵，或者标量。此时输出信号也是相同大小的向量或矩阵。
- **Initial value** 和 **Final value** 参数必须具有可换算的单位。输出端口处的单位由单位传播规则确定。如果两个参数具有相同单位，则输出信号单位也相同。如果参数单位不同，则输出信号单位是与参数单位可换算的基本单位。有关更多信息，请参阅物理信号单位传播。
