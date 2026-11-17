---
type: simulink-block
title: 'Translational Inerter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalinerter'
documentation_source_path: 'ref/translationalinerter.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Inerter

## 端口

### 守恒端口

### **R** — 杆机械平移

与杆（即运动体）关联的机械平移守恒端口。

### **C** — 壳体机械平移

与壳体（即静止体）关联的机械平移守恒端口。

## 参数

### **Inertance** — 力与端口间相对速度变化率之间的比例系数 `1 kg`（默认）| 标量

力与端口间相对速度变化率之间的比例系数。

## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

机械平移系统中的双端口惯性

Translational Inerter 模块表示一种设备，其力与端口间相对速度的变化率成正比。它本质上是一个双端口惯性元件，作用于端口之间的速度差，而非绝对速度。惯性元件（inerter）是电容器的机械等效物。一个端口接地的惯性元件，其行为本质上等同于一个质量等于该惯性元件惯容值的质量块。

可将此模块用于高性能悬架系统，以解耦摆动和侧倾模态，或用于需要对被动调谐质量-弹簧-阻尼器响应进行建模的应用中。

该模块由以下方程描述：

f=Bdvdt

v=vR−vC

其中

- *f* 是通过惯性元件传递的力。
- *B* 是惯容。
- *v* 是相对速度。
- *v*R 和 *v*C 分别是端口 **R** 和 **C** 的绝对速度。

模块正方向为从端口 **R** 到端口 **C**。这意味着如果力沿从 **R** 到 **C** 的方向作用，则该力为正。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
