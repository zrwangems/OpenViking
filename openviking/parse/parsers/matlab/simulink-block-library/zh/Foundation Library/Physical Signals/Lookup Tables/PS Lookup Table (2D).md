---
type: simulink-block
title: 'PS Lookup Table (2D)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Lookup Tables'
documentation_page: 'pslookuptable2d'
documentation_source_path: 'ref/pslookuptable2d.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Lookup Table (2D)

## 端口
```yaml
ports:
- name: x1
  summary: 沿第一个轴的输入查询点或查询点的 N 维数组，无类型物理信号
  direction: input
- name: x2
  summary: 沿第二个轴的输入查询点或查询点的 N 维数组，无类型物理信号
  direction: input
- name: f
  summary: 输出函数值，无类型物理信号
  direction: output
```

### 输入

### **x1** — 沿第一个轴的输入查询点或查询点的 N 维数组，无类型物理信号

沿第一个轴的输入查询点或查询点。信号大小可以是标量（表示单个查询点），也可以是表示沿第一个轴的查询点坐标的 N 维数组。

### **x2** — 沿第二个轴的输入查询点或查询点的 N 维数组，无类型物理信号

沿第二个轴的输入查询点或查询点。信号大小必须与沿第一个轴的信号大小匹配。
### 输出

### **f** — 输出函数值，无类型物理信号

输出函数值，基于将查找表应用于两个输入值。输出信号大小与沿第一个轴的输入信号大小匹配。输出信号单位由 **2D array of table values** 参数的单位决定。
## 参数
```yaml
parameters:
- name: Table grid vector 1
  summary: 沿第一个轴的数据值向量 [1, 2, 3, 4, 5] 1（默认）
  group: ''
- name: Table grid vector 2
  summary: 沿第二个轴的数据值向量 [1, 2, 3, 4, 5] 1（默认）
  group: ''
- name: 2D array of table values
  summary: 表网格顶点处函数值的二维数组 [0, 1, 2, 3, 4; 1, 2, 3, 4, 5; 2, 3, 4, 5, 6; 3, 4, 5, 6, 7; 4, 5, 6, 7, 8] 1（默认）
  group: ''
- name: Interpolation method
  summary: 选择插值方法 Linear（默认）| Smooth
  group: ''
- name: 外插方法
  summary: 选择外插方法 Linear（默认）| Nearest | Error
  group: ''
```

### **Table grid vector 1** — 沿第一个轴的数据值向量 `[1, 2, 3, 4, 5] 1`（默认）

将沿第一个轴的数据值向量指定为 1×`m` 数组。该向量必须严格单调，递增或递减均可。各值可以是非均匀间隔的。对于平滑插值，该向量必须至少包含三个值。对于线性插值，两个值就足够了。

参数单位必须与端口 **x1** 处输入信号的单位一致。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称（如 `rpm`），或键入有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Table grid vector 2** — 沿第二个轴的数据值向量 `[1, 2, 3, 4, 5] 1`（默认）

将沿第二个轴的数据值向量指定为 1×`n` 数组。该向量必须严格单调，递增或递减均可。各值可以是非均匀间隔的。对于平滑插值，该向量必须至少包含三个值。对于线性插值，两个值就足够了。

参数单位必须与端口 **x2** 处输入信号的单位一致。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称（如 `rpm`），或键入有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **2D array of table values** — 表网格顶点处函数值的二维数组 `[0, 1, 2, 3, 4; 1, 2, 3, 4, 5; 2, 3, 4, 5, 6; 3, 4, 5, 6, 7; 4, 5, 6, 7, 8] 1`（默认）

将输出值指定为 `m`×`n` 矩阵，定义数据网格顶点处的函数值。矩阵大小必须与数据向量定义的维度匹配。

参数单位决定端口 **f** 处输出信号的单位。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称（如 `rpm`），或键入有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Interpolation method** — 选择插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，选择以下插值方法之一来近似输出值：

- `Linear` — 使用多维插值的线性算法扩展。该方法首先沿 *`x1`* 方向进行线性插值，然后沿 *`x2`* 方向进行线性插值。选择此选项可获得最佳性能。
- `Smooth` — 使用改进的 Akima 插值算法。有关详细信息，请参见 `tablelookup`。选择此选项可生成具有连续一阶导数的连续曲面。

### **外插方法** — 选择外插方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，选择以下外插方法之一来确定输出值：

- `Linear` — 从插值区域的边缘进行线性延伸。线性外插的斜率等于插值区域边缘处插值曲面的斜率。
- `Nearest` — 从插值区域的边缘以常数方式延伸。最近外插的值等于插值区域边缘处插值曲面的值。选择此选项可生成不会高于数据中最高点或低于数据中最低点的外插。
- `Error` — 如果任何输入信号超出表的范围，则发出错误。当您希望数据位于表范围内时，选择此选项可避免进入外插模式。
## 所属库

Simscape / Foundation Library / Physical Signals / Lookup Tables

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

使用指定的查找方法近似二维函数

PS Lookup Table (2D) 模块通过将输入查询点坐标与二维查找表进行插值，计算某个函数 `f=f(x1,x2)` 的近似值。

您通过指定 **Table grid vector 1** 参数（沿第一个轴的数据点向量）、**Table grid vector 2** 参数（沿第二个轴的数据点向量）以及 **2D array of table values**（输出函数值数组）来定义查找表。该模块在笛卡尔网格上工作，即函数值必须在矩形数组的顶点处指定。

数据向量 **Table grid vector 1** 和 **Table grid vector 2** 必须严格单调，即递增或递减。表格函数值的数组大小必须与数据向量定义的维度匹配。也就是说，如果输入数据点是 1×`m` 向量和 1×`n` 向量，则提供 `m`×`n` 的输出函数值矩阵。

该模块的两个输入和输出是大小匹配的物理信号。该模块基于输入查询和表网格查找，使用选定的插值方法和外插方法生成输出。您可以选择两种插值方法和两种外插方法。您还可以选择让模块在任何输入信号值超出相应表网格向量范围时发出错误。

### 绘制表数据

绘制查找表可以让您在仿真模型之前可视化数据，以确保表是正确的。绘图反映为模块指定的表格数据，以及选定的插值和外插选项。

要绘制数据，请在模型中右键单击该模块，然后从上下文菜单中选择 **Foundation Library** > **Plot Table**。有关详细信息，请参阅 Plot Lookup Tables。
