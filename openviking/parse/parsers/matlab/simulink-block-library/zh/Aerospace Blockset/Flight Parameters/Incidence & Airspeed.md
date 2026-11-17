---
type: simulink-block
title: 'Incidence & Airspeed'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'incidenceairspeed'
documentation_source_path: 'incidenceairspeed.html'
language: zh-CN
chinese_source: worker-translation
---

# Incidence & Airspeed

## 端口

### 输入

### **U, w** — 速度二元素向量

机体的速度，指定为二元素向量，并分解到机体固定坐标系中。

**数据类型：** `double`
### 输出

### **ɑ** — 迎角标量

迎角，以标量形式返回，单位为弧度。

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

## 描述

计算迎角和空速

Incidence & Airspeed 模块通过计算速度向量与机体之间的夹角，以及根据机体固定坐标系中的速度分量计算总空速，来支持 3DoF 运动方程模型。

α=atan(wu)V=u2+w2

**注意**

- 对于固定翼飞机，Incidence & Airspeed 模块计算的角度 α 是相对风与机体纵轴之间的夹角。在许多航空航天工程参考文献中，该角度被称为攻角。Incidence & Airspeed 将该角度称为迎角。
- 对于垂直起降（VTOL）构型，用于计算的方程与固定翼飞机相同 [1]。然而，在涉及巡航与悬停之间转换的机动中，可能会出现速度值较低或为零的场景，从而导致迎角和侧滑角计算不正确。因此，不建议使用该模块分析 VTOL 构型。作为替代方案，可使用 6DOF Wind (Quaternion) 或 6DOF Wind (Wind Angles) 模块，它们可提供 α 和 β 作为输出。
