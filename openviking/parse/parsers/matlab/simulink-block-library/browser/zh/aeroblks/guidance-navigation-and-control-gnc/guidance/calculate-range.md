---
type: simulink-block
title: 'Calculate Range'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Guidance'
documentation_page: 'calculaterange'
documentation_source_path: 'calculaterange.html'
language: zh-CN
chinese_source: worker-translation
---

# Calculate Range

## 端口

### 输入

### **x1** — 车辆 1 位置三元素向量

包含车辆 1 的 (*x*、*y* 和 *z*) 位置，指定为三元素向量。这些值的数据类型为 double。

**数据类型：** `double`

### **x2** — 车辆 2 位置三元素向量

车辆 2 的 (*x*、*y* 和 *z*) 位置，指定为三元素向量。这些值的数据类型为 double。

**数据类型：** `double`
### 输出

### **R2-1** — 距离标量

车辆 2 与车辆 1 之间的距离，以 double 数据类型的标量返回。计算得到的距离是距离的幅值，而不是方向。它始终为正或零。

**数据类型：** `double`

## 参数

未在 R2025b 中记录。

## 所属库

Aerospace Blockset / GNC / Guidance

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

计算给定各自位置的两辆车之间的距离

Calculate Range 模块计算两辆车之间的距离。用于距离计算的方程为

Range=(x1−x2)2+(y1−y2)2+(z1−z2)2
