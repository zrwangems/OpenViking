---
type: simulink-block
title: 'PS Scattered Lookup Table (3D)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Lookup Tables'
documentation_page: 'psscatteredlookuptable3d'
documentation_source_path: 'ref/psscatteredlookuptable3d.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Scattered Lookup Table (3D)

## 端口
```yaml
ports:
- name: x1
  summary: 沿第一个方向的输入查询点或查询点的 N 维数组，无类型物理信号
  direction: input
- name: x2
  summary: 沿第二个方向的输入查询点或查询点的 N 维数组，无类型物理信号
  direction: input
- name: x3
  summary: 沿第三个方向的输入查询点或查询点的 N 维数组，无类型物理信号
  direction: input
- name: f
  summary: 输出函数值，无类型物理信号
  direction: output
```

### 输入

### **x1** — 沿第一个方向的输入查询点或查询点的 N 维数组，无类型物理信号

沿第一个方向的查询输入值，指定为标量或 N 维数组。

### **x2** — 沿第二个方向的输入查询点或查询点的 N 维数组，无类型物理信号

沿第二个方向的查询输入值，指定为标量或 N 维数组。信号大小必须与沿第一个方向的信号大小一致。

### **x3** — 沿第三个方向的输入查询点或查询点的 N 维数组，无类型物理信号

沿第三个方向的查询输入值，指定为标量或 N 维数组。信号大小必须与沿第一个方向的信号大小一致。
### 输出

### **f** — 输出函数值，无类型物理信号

输出函数值，基于对两个输入值应用散点查找方法得到。输出信号大小与沿第一个方向的输入信号大小一致。输出信号单位由 **Data points function value** 参数的单位决定。
## 参数
```yaml
parameters:
- name: Data points coordinate 1
  summary: 沿第一个方向的输入值数据集 [1, 2, 3, 4, 5] 1（默认）
  group: ''
- name: Data points coordinate 2
  summary: 沿第二个方向的输入值数据集 [5, 4, 3, 3, 1] 1（默认）
  group: ''
- name: Data points coordinate 3
  summary: 沿第三个方向的输入值数据集 [8, 2, 5, 7, 0] 1（默认）
  group: ''
- name: Data points function value
  summary: 用于查找的函数值数据集 [1, 2, 3, 4, 5] 1（默认）
  group: ''
- name: Extrapolation method
  summary: 选择外推方法 Linear（默认）| Nearest
  group: ''
```

### **Data points coordinate 1** — 沿第一个方向的输入值数据集 `[1, 2, 3, 4, 5] 1`（默认）

沿第一个方向的输入值数据集，指定为一维数组。至少指定四个值。

参数单位必须与端口 **x1** 处输入信号的单位一致。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称，例如 `rpm`，或有效表达式，例如 `rad/s`。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Data points coordinate 2** — 沿第二个方向的输入值数据集 `[5, 4, 3, 3, 1] 1`（默认）

沿第二个方向的输入值数据集，指定为与 **Data points coordinate 1** 大小相同的一维数组。

参数单位必须与端口 **x2** 处输入信号的单位一致。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称，例如 `rpm`，或有效表达式，例如 `rad/s`。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Data points coordinate 3** — 沿第三个方向的输入值数据集 `[8, 2, 5, 7, 0] 1`（默认）

沿第三个方向的输入值数据集，指定为与 **Data points coordinate 1** 大小相同的一维数组。

参数单位必须与端口 **x3** 处输入信号的单位一致。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称，例如 `rpm`，或有效表达式，例如 `rad/s`。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Data points function value** — 用于查找的函数值数据集 `[1, 2, 3, 4, 5] 1`（默认）

用于查找的函数值数据集，指定为与 **Data points coordinate 1** 大小相同的一维数组。

参数单位决定端口 **f** 处输出信号的单位。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择不同的单位，或键入所需的单位名称，例如 `rpm`，或有效表达式，例如 `rad/s`。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Extrapolation method** — 选择外推方法 `Linear`（默认）| `Nearest`

选择当输入值位于数据集凸包之外时用于计算输出值的近似方法：

- `Linear` — 基于边界梯度的线性外推。
- `Nearest` — 最近邻外推。此方法计算为边界上最近邻的值。
## 所属库

Simscape / Foundation Library / Physical Signals / Lookup Tables

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

使用散点数据查找近似三维函数

PS Scattered Lookup Table (3D) 模块在给定三维空间中一组散点输入数据点的坐标以及每个数据点处的函数值的情况下，计算对某个函数 `f=f(x1,x2,x3)` 的近似。三个输入和输出均为物理信号。输入指定查询点沿三个方向的坐标。输出是对应于输入查询点的计算函数值。

该模块通过使用 Delaunay 三角剖分将查询输入值针对非结构化（即散点）数据集进行插值来计算输出值。您通过指定 **Data points coordinate 1** 参数（沿第一个方向的数据点坐标向量）、**Data points coordinate 2** 参数（相同数据点沿第二个方向的坐标向量）、**Data points coordinate 3** 参数（相同数据点沿第三个方向的坐标向量）以及 **Data points function value**（对应于每个这些数据点的函数值向量）来定义查找表。所有四个向量必须具有相同的大小。
