---
type: simulink-block
title: 'Rotational Inerter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationalinerter'
documentation_source_path: 'ref/rotationalinerter.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Inerter

## 端口

### 守恒

### **R** — 杆机械旋转

与杆（即运动体）关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与壳体（即静止体）关联的机械旋转守恒端口。

## 参数

### **旋转惯容** — 端口间转矩与相对速度变化率之间的比例系数 `1 kg*m^2`（默认） | 标量

端口间转矩与相对角速度变化率之间的比例系数。

## 所属库

Simscape / Foundation Library / Mechanical / Rotational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

机械旋转系统中的双端口惯性

Rotational Inerter 模块表示一种器件，其转矩与端口间相对角速度的变化率成正比。它本质上是一个双端口惯性元件，作用于端口之间的速度差，而不是绝对速度。

在高性能悬架系统中使用此模块，以解耦摆振和侧倾模态；或者在需要对被动调谐的质量-弹簧-阻尼器响应进行建模的应用中使用。

该模块由以下方程描述：

T=Bdωdt

ω=ωR−ωC

其中

- *T* 是通过惯容器传递的转矩。
- *B* 是惯容。
- *ω* 是相对角速度。
- *ω*R 和
  *ω*C 分别是端口
  **R** 和 **C** 的绝对角速度。

该模块的正方向是从端口 **R** 到端口 **C**。这意味着，如果端口 **R** 的速度大于端口 **C** 的速度，则该模块将转矩从 **R** 传递到 **C**。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。基于标称值使用系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
