---
type: simulink-block
title: 'PS Lookup Table (1D)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Lookup Tables'
documentation_page: 'pslookuptable1d'
documentation_source_path: 'ref/pslookuptable1d.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Lookup Table (1D)

## 端口
```yaml
ports:
- name: x
  summary: 输入查询点或沿 *x* 轴的 N 维查询点数组，无类型物理信号
  direction: input
- name: f
  summary: 输出函数值，无类型物理信号
  direction: output
```

### 输入

### **x** — 输入查询点或沿 *x* 轴的 N 维查询点数组，无类型物理信号

沿 *x* 轴的输入查询点。信号大小可以是标量（用于单个查询点），也可以是 N 维数组（表示沿 *x* 轴的查询点坐标）。
### 输出

### **f** — 输出函数值，无类型物理信号

基于将查找表应用于输入查询的输出函数值。输出信号大小与输入信号大小匹配。输出信号单位由 **Table values** 参数的单位决定。
## 参数
```yaml
parameters:
- name: Table grid vector
  summary: 沿 *x* 轴的数据点向量 [1, 2, 3, 4, 5] 1（默认值）
  group: ''
- name: Table values
  summary: 沿 *f* 轴的输出值向量 [0, 1, 2, 3, 4] 1（默认值）
  group: ''
- name: Interpolation method
  summary: 选择插值方法 Linear（默认值） | Smooth
  group: ''
- name: Extrapolation method
  summary: 选择外推方法 Linear（默认值） | Nearest | Error
  group: ''
```

### **Table grid vector** — 沿 *x* 轴的数据点向量 `[1, 2, 3, 4, 5] 1`（默认值）

指定沿 *x* 轴的数据点向量。该向量必须严格单调，递增或递减均可。各值可以非均匀间隔。对于平滑插值，该向量必须至少包含三个值。对于线性插值，两个值即可。

参数单位必须与端口 **x** 处输入信号的单位一致。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称（如 `rpm`），或有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Table values** — 沿 *f* 轴的输出值向量 `[0, 1, 2, 3, 4] 1`（默认值）

指定输出函数值的向量。函数值向量的大小必须与数据点向量的大小相同。

参数单位决定端口 **f** 处输出信号的单位。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称（如 `rpm`），或有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Interpolation method** — 选择插值方法 `Linear`（默认值） | `Smooth`

当输入值位于两个连续网格点之间时，选择以下插值方法之一来近似输出值：

- `Linear` — 使用线性函数。选择此选项可获得最佳性能。
- `Smooth` — 使用改进的 Akima 插值算法。有关详细信息，请参见 `tablelookup`。选择此选项可生成具有连续一阶导数的连续曲线。

### **Extrapolation method** — 选择外推方法 `Linear`（默认值） | `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，选择以下外推方法之一来确定输出值：

- `Linear` — 从插值区域的边缘进行线性延伸。线性外推的斜率等于插值区域边缘处插值曲线的斜率。
- `Nearest` — 从插值区域的边缘以常数方式延伸。最近外推的值等于插值区域边缘处插值曲线的值。选择此选项可产生不会高于数据中最高点或低于数据中最低点的外推。
- `Error` — 如果输入信号超出表的范围，则发出错误。当您希望数据位于表范围内时，选择此选项可避免进入外推模式。
## 所属库

Simscape / Foundation Library / Physical Signals / Lookup Tables

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2019a: 单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用升级顾问将模块升级到最新版本。有关详细信息，请参阅使用旧版物理信号模块升级模型。

## 描述

使用指定的查找方法近似一维函数

PS Lookup Table (1D) 模块通过将输入查询点坐标与一维查找表进行插值，计算对某个函数 `f=f(x)` 的近似值。

您通过指定 **Table grid vector** 参数（沿 *x* 轴的数据点向量）和 **Table values** 参数（对应函数值向量）来定义查找表。这两个向量的长度必须匹配。此外，`x` 数据向量必须严格单调，即递增或递减。

模块输入和输出是大小匹配的物理信号。模块根据输入查询和表网格查找，使用选定的插值和外推方法生成输出。您可以选择两种插值方法和两种外推方法。您还可以选择让模块在输入信号值超出表网格向量范围时发出错误。

### 绘制表数据

绘制查找表可以让您在仿真模型之前可视化数据，以确保表是正确的。绘图反映为模块指定的表格数据，以及选定的插值和外推选项。

要绘制数据，请在模型中右键单击该模块，然后从上下文菜单中选择 **Foundation Library** > **Plot Table**。有关详细信息，请参阅绘制查找表。
