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
```yaml
ports:
- name: O
  summary: 输出物理信号，其类型由模块参数值和单位物理信号决定
  direction: output
```

### 输出

### **O** — 输出物理信号，其类型由模块参数值和单位物理信号决定

输出物理信号。信号大小与 **Initial value** 和 **Final value** 参数值的大小一致。信号单位由 **Initial value** 和 **Final value** 参数的单位决定。

端口名称在模块图标中不可见，但你可以通过点击模块对话框 **Description** 选项卡中的 **Source code** 链接，在底层源文件中看到此名称。
## 参数
```yaml
parameters:
- name: Step time
  summary: 发生阶跃的时间 1 s（默认）| 标量
  group: ''
- name: Initial value
  summary: 阶跃前的输出 0 1（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: Final value
  summary: 阶跃后的输出 1 1（默认）| 标量 | 向量 | 矩阵
  group: ''
```

### **Step time** — 发生阶跃的时间 `1 s`（默认）| 标量

信号发生变化值的时间。从仿真开始到 **Step time** 之间，模块的输出保持在 **Initial value**，然后瞬时变化到 **Final value**，并保持该值直到仿真结束。

### **Initial value** — 阶跃前的输出 `0 1`（默认）| 标量 | 向量 | 矩阵

在仿真时间达到 **Step time** 之前模块的输出。第一个编辑框表示参数值。你可以指定标量、向量或矩阵。默认情况下，该值为标量 `0`。如果你指定向量或矩阵，**Final value** 也必须是相同大小的向量或矩阵，或者是一个标量。

第二个组合框表示参数单位。指定的单位必须与 **Final value** 参数的单位可公度。默认情况下，单位为 `1`（无单位）。你可以从下拉列表中选择一个单位，或输入所需的单位名称，例如 `Pa`，或有效表达式，例如 `m^2`。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Final value** — 阶跃后的输出 `1 1`（默认）| 标量 | 向量 | 矩阵

当仿真时间达到并超过 **Step time** 时模块的输出。第一个编辑框表示参数值。你可以指定标量、向量或矩阵。默认情况下，该值为标量 `1`。如果你指定向量或矩阵，**Initial value** 也必须是相同大小的向量或矩阵，或者是一个标量。

第二个组合框表示参数单位。指定的单位必须与 **Initial value** 参数的单位可公度。默认情况下，单位为 `1`（无单位）。你可以从下拉列表中选择一个单位，或输入所需的单位名称，例如 `Pa`，或有效表达式，例如 `m^2`。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。
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

PS Step 模块生成一个物理信号，该信号从指定的初始值开始，并在指定时间瞬时变为新值。**阶跃时间**、**初始值**和**最终值**参数决定输出信号的特性：

- **阶跃时间**参数决定信号值从**初始值**变为**最终值**的时间。
- **初始值**和**最终值**参数值决定输出信号是标量、向量还是矩阵。如果其中一个参数是向量或矩阵，则另一个必须是相同大小的向量或矩阵或标量。此时输出信号也是相同大小的向量或矩阵。
- **初始值**和**最终值**参数必须具有 commensurate 单位。输出端口的单位由单位传播规则决定。如果两个参数具有相同的单位，则输出信号单位也相同。如果参数单位不同，则输出信号的单位是与参数单位 commensurate 的基本单位。有关详细信息，请参阅物理信号单位传播。
