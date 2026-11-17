---
type: simulink-block
title: 'Translational Spring'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalspring'
documentation_source_path: 'ref/translationalspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Spring

## 端口

### 守恒端口

### **R** — 杆机械平移

与杆（即运动体）关联的机械平移守恒端口。

### **C** — 壳体机械平移

与壳体（即静止体）关联的机械平移守恒端口。

## 参数

### **Spring rate** — 弹簧刚度 `1000 N/m`（默认）| 标量

弹簧刚度。

## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械平移系统中的理想弹簧

Translational Spring 模块表示一个理想机械线性弹簧，用以下方程描述：

F=Kx

x=xinit+xR−xC

v=dxdt

其中

- *F* 是通过弹簧传递的力。
- *K* 是弹簧刚度。
- *x* 是相对位移，即弹簧变形。
- *x*init 是初始位移，即初始弹簧变形。如果 *`xinit >
  0`*，则弹簧初始处于压缩状态。如果
  *`xinit < 0`*，则弹簧初始处于拉伸状态。
- *x*R 和
  *x*C 分别是端口 **R** 和 **C** 的绝对位移。
- *v* 是相对速度。
- *t* 是时间。

模块正方向是从端口 **R** 到端口 **C**。这意味着如果力沿从 **R** 到 **C** 的方向作用，则该力为正。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
