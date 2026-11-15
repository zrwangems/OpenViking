---
type: simulink-block
title: 'Translational Friction'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Translational Elements'
documentation_page: 'translationalfriction'
documentation_source_path: 'ref/translationalfriction.html'
language: zh-CN
chinese_source: official
---

# Translational Friction

## 端口

### 守恒

### **R** — 杆 机械平移

与杆（即运动实体）相关联的机械平移守恒端口。

### **C** — 外壳 机械平移

与外壳（即静止实体）相关联的机械平移守恒端口。

## 参数

### **起动摩擦力** — 库仑摩擦和静磨擦的总和 `25 N` (默认) | 标量

起动摩擦力，即库仑摩擦和静摩擦的总和。它必须大于或等于**库仑摩擦力**值。

### **起动摩擦速度** — 斯特里贝克摩擦的峰值速度 `0.1 m/s` (默认) | 正标量

斯特里贝克摩擦达到其峰值时的速度。此时，斯特里贝克摩擦和库仑摩擦的总和为**起动摩擦力**。此参数指定速度阈值，它影响仿真准确性和速度之间的权衡。

### **库仑摩擦力** — 抵抗运动的摩擦 `20 N` (默认) | 标量

库仑摩擦力，即在任何速度下以恒定力抵抗运动的摩擦。

### **粘性摩擦系数** — 比例系数 `100 N/(m/s)` (默认) | 非负标量

摩擦力与相对速度之间的比例系数。此参数值必须大于或等于零。

## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

运动实体之间接触时的摩擦

Translational Friction 模块表示运动实体之间接触时的摩擦。摩擦力被仿真为相对速度的函数，并假定为斯特里贝克分量、库仑分量和粘性分量的总和，如下图所示。

斯特里贝克摩擦 *F*S 是发生在低速时的负倾斜特性[1]。库仑摩擦 *F*C 在任何速度下都会产生恒定的力。粘性摩擦 *F*V 以与相对速度成正比的力来抵抗运动。零速度附近的库仑摩擦与斯特里贝克摩擦的总和通常称为起动摩擦 *F*brk。此摩擦可通过以下方程进行近似计算：

F=2e(Fbrk−FC)⋅exp(−(vvSt)2)⋅vvSt+FC⋅tanh(vvCoul)+fv

vSt=vbrk2

vCoul=vbrk/10

v=vR−vC

其中

- *F* 是摩擦力。
- *F*C 是库仑摩擦。
- *F*brk 是起动摩擦。
- *v*brk 是起动摩擦速度。
- *v*St 是斯特里贝克速度阈值。
- *v*Coul 是库仑速度阈值。
- *v*R 和 *v*C 分别是端口 **R** 和 **C** 的绝对速度。
- *v* 是相对速度。
- *f* 是粘性摩擦系数。

力方程的斯特里贝克部分中使用的指数函数是连续的，并且在速度模大于起动摩擦速度时衰减。

力方程的库仑部分中使用的双曲正切函数可确保方程在 *v* = 0 时是平滑且连续的，但在非零速度下可快速达到其满值。

此模块的正方向是从端口 **R** 到端口 **C**。这意味着，如果端口 **R** 的速度大于端口 **C** 的速度，则此模块将力从端口 **R** 传递到端口 **C**。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
