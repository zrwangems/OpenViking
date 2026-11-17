---
type: simulink-block
title: 'Rotational Spring'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationalspring'
documentation_source_path: 'ref/rotationalspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Spring

## 端口

### 守恒端口

### **R** — 杆机械旋转

与杆（即运动体）关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与壳体（即静止体）关联的机械旋转守恒端口。

## 参数

### **Spring rate** — 弹簧刚度 `10 N*m/rad`（默认）| 标量

弹簧刚度。

## 所属库

Simscape / Foundation Library / Mechanical / Rotational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械旋转系统中的理想弹簧

Rotational Spring 模块表示一个理想的机械旋转线性弹簧，用以下方程描述：

T=K·φ

φ=φinit+φR−φC

ω=dφdt

其中

- *T* 是通过弹簧传递的扭矩。
- *K* 是弹簧刚度。
- *φ* 是相对位移角，即弹簧变形。
- *φ*init 是弹簧预紧圈数。
- *φ*R 和 *φ*C 分别是端口 **R** 和 **C** 的绝对角位移。
- *ω* 是相对角速度。
- *t* 是时间。

模块正方向是从端口 **R** 到端口 **C**。这意味着如果端口 **R** 的速度大于端口 **C** 的速度，则模块将扭矩从 **R** 传递到 **C**。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
