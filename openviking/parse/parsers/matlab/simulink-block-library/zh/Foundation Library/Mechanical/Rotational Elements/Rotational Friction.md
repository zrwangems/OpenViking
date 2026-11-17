---
type: simulink-block
title: 'Rotational Friction'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationalfriction'
documentation_source_path: 'ref/rotationalfriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Friction

## 端口

### 守恒

### **R** — 杆机械旋转

与杆（即运动体）关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与壳体（即静止体）关联的机械旋转守恒端口。

## 参数

### **Breakaway friction torque** — 库仑摩擦与静摩擦之和 `25 N*m`（默认）| 标量

启动力矩，即库仑摩擦与静摩擦之和。其值必须大于或等于 **Coulomb friction torque** 的值。

### **Breakaway friction velocity** — Stribeck 摩擦的峰值角速度 `0.1 rad/s`（默认）| 正标量

Stribeck 摩擦达到峰值时的角速度。此时，Stribeck 摩擦与库仑摩擦之和即为 **Breakaway friction torque**。该参数指定速度阈值，影响仿真精度与速度之间的权衡。

### **Coulomb friction torque** — 阻碍旋转的摩擦 `20 N*m`（默认）| 标量

库仑摩擦力矩，即在任何速度下以恒定力矩阻碍旋转的摩擦。

### **Viscous friction coefficient** — 比例系数 `0.001 N*m/(rad/s)`（默认）| 非负标量

摩擦力矩与相对角速度之间的比例系数。该参数值必须大于或等于零。

## 所属库

Simscape / Foundation Library / Mechanical / Rotational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

旋转体之间接触的摩擦

Rotational Friction 模块表示旋转体之间接触的摩擦。摩擦力矩被模拟为相对速度的函数，并假定为 Stribeck、库仑和粘性分量之和，如下图所示。

Stribeck 摩擦 *T*S 是在低速下出现的负斜率特性 [1]。库仑摩擦 *T*C 在任何速度下产生恒定力矩。粘性摩擦 *T*V 以与相对速度成正比的力矩阻碍运动。在零速度附近，库仑摩擦与 Stribeck 摩擦之和通常称为启动力矩 *T*brk。摩擦用以下方程近似：

T=2e(Tbrk−TC)⋅exp(−(ωωSt)2)⋅ωωSt+TC⋅tanh(ωωCoul)+fω

ωSt=ωbrk2

ωCoul=ωbrk/10

ω=ωR−ωC

其中

- *T* 是摩擦力矩。
- *T*C 是库仑摩擦力矩。
- *T*brk 是启动力矩。
- *ω*brk 是启动角速度。
- *ω*St 是 Stribeck 速度阈值。
- *ω*Coul 是库仑速度阈值。
- *ω*R 和 *ω*C 分别是端口 **R** 和 **C** 的绝对角速度。
- *ω* 是相对速度。
- *f* 是粘性摩擦系数。

力方程中 Stribeck 部分使用的指数函数是连续的，并在速度幅值大于启动角速度时衰减。

力方程中库仑部分使用的双曲正切函数确保方程在 *ω* = 0 处光滑连续，但在非零速度下迅速达到其完整值。

模块正方向为从端口 **R** 到端口 **C**。这意味着如果端口 **R** 的速度大于端口 **C** 的速度，则模块将力矩从 **R** 传递到 **C**。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
