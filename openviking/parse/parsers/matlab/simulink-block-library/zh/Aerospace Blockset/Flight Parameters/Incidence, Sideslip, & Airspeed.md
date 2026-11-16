---
type: simulink-block
title: 'Incidence, Sideslip, & Airspeed'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'incidencesideslipairspeed'
documentation_source_path: 'incidencesideslipairspeed.html'
language: zh-CN
chinese_source: worker-translation
---

# Incidence, Sideslip, & Airspeed

## 端口

### 输入

### **Vb** — 机体速度三元素向量

机体的速度，指定为三元素向量，并分解到机体固定坐标系中。

**数据类型：** `double`
### 输出

### **ɑ** — 入射角标量

入射角，以标量形式返回，单位为 radians。

**数据类型：** `double`

### **β** — 侧滑角标量

侧滑角，以标量形式返回，单位为 radians。

**数据类型：** `double`

### **V** — 空速标量

机体的空速，以标量形式返回。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2022b：更新以减少除零问题

Incidence, Sideslip, & Airspeed 模块现在降低了因飞机在无前向运动悬停时引起的除零问题的可能性。在以前的版本中，无前向运动悬停可能会导致除零问题。

## 描述

计算入射角、侧滑角和空速

Incidence, Sideslip, & Airspeed 模块根据机体固定坐标系中的速度分量计算速度向量与机体之间的角度，以及总空速。有关计算中使用的方程，参见算法。

**注意**

- 对于固定翼飞机，由 Incidence, Sideslip, & Airspeed 模块计算的角 α 是相对风与机体纵轴之间的夹角。在许多航空航天工程参考文献中，该角被称为攻角。Incidence, Sideslip, & Airspeed 将该角称为入射角。
- 对于垂直起降 (VTOL) 配置，用于计算的方程与固定翼飞机 [1] 相同。然而，在涉及巡航与悬停之间过渡的机动中，可能会出现速度值低或为零的情形，从而导致错误的入射角和侧滑角。因此，不建议使用该模块分析 VTOL 配置。作为替代，可使用 6DOF Wind (Quaternion) 或 6DOF Wind (Wind Angles) 模块，它们提供 α 和 β 作为输出。
