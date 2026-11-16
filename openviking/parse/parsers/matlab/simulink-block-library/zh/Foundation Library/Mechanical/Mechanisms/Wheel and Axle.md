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

### 守恒

### **A** — 轴机械旋转

与轴关联的机械旋转守恒端口。

### **P** — 车轮外缘机械平移

与车轮外缘关联的机械平移守恒端口。

## 参数

### **Wheel radius** — 车轮半径 `0.05 m`（默认）

车轮半径。

### **Mechanism orientation** — 轴旋转与平移运动方向之间的关系 `Drives in positive direction`（默认）| `Drives in negative direction`

值 `Drives in positive direction` 指定一种机构，其中轴沿全局分配的正方向旋转转换为正方向的平移运动。值 `Drives in negative direction` 指定一种机构，其中轴沿全局分配的正方向旋转转换为负方向的平移运动。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanisms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械系统中的轮轴机构

Wheel and Axle 模块表示以下示意图所示的轮轴机构。

车轮和轴具有相同的轴线，并且假定该轴线与框架刚性连接，从而使该机构成为将机械旋转运动转换为机械平移运动的理想转换器。该机构有两个连接：一个机械旋转端口 A，对应轴；一个机械平移端口 P，对应车轮外缘。该机构由以下方程描述：

T=r·F·or

v=r·ω·or

其中

- *T* 是轴上的扭矩。
- *F* 是车轮外缘上的力。
- *ω* 是角速度。
- *v* 是车轮外缘上的线速度。
- *r* 是车轮半径。
- *or* 是机构方向指示符。如果轴沿全局分配的正方向旋转转换为正方向的平移运动，则该值为 +1。如果正旋转导致负方向的平移运动，则该值为 –1。

在齿条-小齿轮、方向盘、起重设备、绞盘等仿真中使用该模块。

该模块的正方向为从 A 到参考点以及从参考点到 P。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
