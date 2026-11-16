---
type: simulink-block
title: 'Inverse Park Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inverseparktransform'
documentation_source_path: 'ref/inverseparktransform.html'
language: zh-CN
chinese_source: official
---

# Inverse Park Transform

## 端口

### 输入

### **dq0** — *d*-*q* 轴分量和零轴分量 向量

系统在旋转参考系中的直轴和交轴分量以及零轴分量。

**数据类型:** `single` | `double`

### **θelec** — 旋转角度，弧度 标量

旋转参考系的角位置。此参数的值等于 *abc* 参考系中 *a* 相向量到 *dq0* 参考系初始对齐轴的极距。

**数据类型:** `single` | `double`
### 输出

### **abc** — *a* 相、*b* 相和 *c* 相分量 向量

*abc* 参考系中三相系统的分量。

**数据类型:** `single` | `double`

## 参数

### **功率不变** — 功率不变变换 off (默认) | on

用于保留 *a**b**c* 参考系中的有功功率和无功功率的选项。

### **a 相轴对齐** — *dq0* 参考系对齐 **Q 轴** (默认) | **D 轴**

将 *abc* 参考系的 *a* 相向量与旋转参考系的 *d* 轴或 *q* 轴对齐。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

实现 dq0 到 abc 的变换

Inverse Park Transform 模块将旋转参考系中的时域直轴、交轴和零轴分量转换为 *a**b**c* 参考系中三相系统的分量。通过实现一种不变版本的帕克变换，此模块可以保持与旋转参考系中的系统功率相等的有功功率和无功功率。对于平衡系统，零轴分量等于零。

您可以将此模块配置为在时间 *t* = 0 时，使三相系统的 *a* 轴与旋转参考系的 *d* 轴或 *q* 轴对齐。下面的图显示了 *a**b**c* 参考系和 *d*-*q* 旋转参考系中定子绕组磁轴的方向，其中：

- *a* 轴和 *q* 轴初始对齐。
- *a* 轴和 *d* 轴初始对齐。

在这两种情况下，角度 *θ* = *ω**t*，其中

- *θ* 是 *a* 轴与 *q* 轴之间的角度（对于 *q* 轴对齐），或是 *a* 轴与 *d* 轴之间的角度（对于 *d* 轴对齐）。
- *ω* 是 *d*-*q* 参考系的转速。
- *t* 是从初始对齐算起的时间，以秒为单位。

下面的图显示了等效平衡 *dq0* 和 *abc* 各分量在以下情况下的时间响应：

- *a* 相向量与 *q* 轴对齐
- *a* 相向量与 *d* 轴对齐

### 定义方程

Inverse Park Transform 模块按如下方程实现 *a* 相与 *q* 轴对齐的变换：

[abc]=[sin(θ)cos(θ)1sin(θ−2π3)cos(θ−2π3)1sin(θ+2π3)cos(θ+2π3)1][dq0],

其中：

- *d* 和 *q* 是旋转参考系中双轴系统的分量。
- *a*、*b* 和 *c* 是 *a**b**c* 参考系中三相系统的分量。
- *0* 是静止参考系中双轴系统的零轴分量。

对于功率不变的 *a* 相与 *q* 轴对齐，此模块使用以下方程实现变换：

[abc]=23[sin(θ)cos(θ)12sin(θ−2π3)cos(θ−2π3)12sin(θ+2π3)cos(θ+2π3)12][dq0].

对于 *a* 相与 *d* 轴对齐，此模块使用以下方程实现变换：

[abc]=[cos(θ)−sin(θ)1cos(θ−2π3)−sin(θ−2π3)1cos(θ+2π3)−sin(θ+2π3)1][dq0].

此模块按如下方程实现功率不变的 *a* 相与 *d* 轴对齐的变换：

[abc]=23[cos(θ)−sin(θ)12cos(θ−2π3)−sin(θ−2π3)12cos(θ+2π3)−sin(θ+2π3)12][dq0].
