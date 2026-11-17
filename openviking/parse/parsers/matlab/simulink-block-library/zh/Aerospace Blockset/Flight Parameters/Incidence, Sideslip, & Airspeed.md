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
```yaml
ports:
- name: Vb
  summary: 机体三元素速度矢量
  direction: input
  data_types: double
- name: ɑ
  summary: 迎角标量
  direction: output
  data_types: double
- name: β
  summary: 侧滑角标量
  direction: output
  data_types: double
- name: V
  summary: 空速标量
  direction: output
  data_types: double
```

### 输入

### **Vb** — 机体三元素速度矢量

机体的速度，指定为三元素矢量，在机体固定坐标系中分解。

**数据类型：** `double`
### 输出

### **ɑ** — 迎角标量

迎角，以标量形式返回，单位为弧度。

**数据类型：** `double`

### **β** — 侧滑角标量

侧滑角，以标量形式返回，单位为弧度。

**数据类型：** `double`

### **V** — 空速标量

机体的空速，以标量形式返回。

**数据类型：** `double`
## 参数
```yaml
parameters: []
```

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

Incidence, Sideslip, & Airspeed 模块现在减少了由飞机无前向运动悬停引起的除零问题的可能性。在之前的版本中，无前向运动悬停可能会导致除零问题。

## 描述

计算迎角、侧滑角和空速

Incidence, Sideslip, & Airspeed 模块计算速度矢量与机体之间的角度，以及从机体固定坐标系中的速度分量计算总空速。有关计算中使用的方程，请参阅算法。

**注意**

- 对于固定翼飞机，Incidence, Sideslip, & Airspeed 模块计算的角 α 是相对风与机体纵轴之间的角度。该角度在许多航空航天工程参考文献中称为迎角。Incidence, Sideslip, & Airspeed 将此角称为 incidence angle。
- 对于垂直起降（VTOL）构型，用于计算的方程与固定翼飞机的方程相同 [1]。然而，在涉及巡航与悬停之间过渡的机动中，可能存在速度低或为零的情况，导致迎角和侧滑角不正确。因此，不建议使用此模块分析 VTOL 构型。作为替代方案，请使用 6DOF Wind (Quaternion) 或 6DOF Wind (Wind Angles) 模块，它们提供 α 和 β 作为输出。
