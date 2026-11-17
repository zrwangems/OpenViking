---
type: simulink-block
title: 'Wheel and Axle'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanisms'
documentation_page: 'wheelandaxle'
documentation_source_path: 'ref/wheelandaxle.html'
language: zh-CN
chinese_source: worker-translation
---

# Wheel and Axle

## 端口
```yaml
ports:
- name: A
  summary: 车轴机械旋转
  direction: conserving
- name: P
  summary: 车轮周边机械平移
  direction: conserving
```

### 守恒端口

### **A** — 车轴机械旋转

与车轴关联的机械旋转守恒端口。

### **P** — 车轮周边机械平移

与车轮周边关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Wheel radius
  summary: 车轮半径 0.05 m（默认值）
  group: ''
- name: Mechanism orientation
  summary: 车轴旋转与平移运动方向之间的关系 Drives in positive direction（默认值） | Drives in negative direction
  group: ''
```

### **Wheel radius** — 车轮半径 `0.05 m`（默认值）

车轮的半径。

### **Mechanism orientation** — 车轴旋转与平移运动方向之间的关系 `Drives in positive direction`（默认值） | `Drives in negative direction`

值 `Drives in positive direction` 指定一种机构，其中车轴沿全局指定的正方向旋转被转换为正方向的平移运动。值 `Drives in negative direction` 指定一种机构，其中车轴沿全局指定的正方向旋转被转换为负方向的平移运动。
## 所属库

Simscape / Foundation Library / Mechanical / Mechanisms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械系统中的轮轴机构

Wheel and Axle 模块表示下图所示的轮轴机构。

车轮和车轴具有相同的轴线，且假定该轴线与机架刚性连接，从而使该机构成为将机械旋转运动转换为机械平移运动的理想转换器。该机构有两个连接：机械旋转端口 A，对应车轴；机械平移端口 P，对应车轮周边。该机构由以下方程描述：

T=r·F·or

v=r·ω·or

其中

- *T* 是车轴上的扭矩。
- *F* 是车轮周边上的力。
- *ω* 是角速度。
- *v* 是车轮周边上的线速度。
- *r* 是车轮半径。
- *or* 是机构方向指示符。如果车轴沿全局指定的正方向旋转被转换为正方向的平移运动，则该值为 +1。如果正方向旋转导致负方向的平移运动，则该值为 –1。

在齿条-小齿轮、转向轮、起重装置、绞车等的仿真中使用该模块。

该模块的正方向为从 A 到参考点，以及从参考点到 P。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
