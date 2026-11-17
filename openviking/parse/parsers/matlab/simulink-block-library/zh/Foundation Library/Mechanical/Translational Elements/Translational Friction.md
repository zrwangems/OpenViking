---
type: simulink-block
title: 'Translational Friction'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalfriction'
documentation_source_path: 'ref/translationalfriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Friction

## 端口

### 守恒端口

### **R** — 杆机械平移

与杆（即运动体）关联的机械平移守恒端口。

### **C** — 壳体机械平移

与壳体（即静止体）关联的机械平移守恒端口。

## 参数

### **Breakaway friction force** — 库仑摩擦与静摩擦之和 `25 N`（默认）| 标量

启动力，即库仑摩擦与静摩擦之和。其值必须大于或等于 **Coulomb friction force** 的值。

### **Breakaway friction velocity** — Stribeck 摩擦的峰值速度 `0.1 m/s`（默认）| 正标量

Stribeck 摩擦达到峰值时的速度。此时，Stribeck 摩擦与库仑摩擦之和即为 **Breakaway friction force**。该参数指定速度阈值，影响仿真精度与速度之间的权衡。

### **Coulomb friction force** — 阻碍运动的摩擦力 `20 N`（默认）| 标量

库仑摩擦力，即在任何速度下以恒定力阻碍运动的摩擦力。

### **Viscous friction coefficient** — 比例系数 `100 N/(m/s)`（默认）| 非负标量

摩擦力与相对速度之间的比例系数。该参数值必须大于或等于零。

## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

运动体之间接触的摩擦

Translational Friction 模块表示运动体之间接触的摩擦。摩擦力被模拟为相对速度的函数，并假定为 Stribeck、库仑和粘性分量之和，如下图所示。

Stribeck 摩擦 *F*S 是在低速时出现的负斜率特性 [1]。库仑摩擦 *F*C 在任何速度下产生恒定力。粘性摩擦 *F*V 以与相对速度成正比的力阻碍运动。在零速度附近，库仑摩擦与 Stribeck 摩擦之和通常称为启动力 *F*brk。摩擦力用以下方程近似：

F=2e(Fbrk−FC)⋅exp(−(vvSt)2)⋅vvSt+FC⋅tanh(vvCoul)+fv

vSt=vbrk2

vCoul=vbrk/10

v=vR−vC

其中

- *F* 是摩擦力。
- *F*C 是库仑摩擦。
- *F*brk 是启动力。
- *v*brk 是启动力速度。
- *v*St 是 Stribeck 速度阈值。
- *v*Coul 是库仑速度阈值。
- *v*R 和 *v*C 分别是端口 **R** 和 **C** 的绝对速度。
- *v* 是相对速度。
- *f* 是粘性摩擦系数。

力方程中 Stribeck 部分使用的指数函数是连续的，并在速度幅值大于启动力速度时衰减。

力方程中库仑部分使用的双曲正切函数确保方程在 *v* = 0 处光滑连续，但在非零速度下迅速达到其完整值。

模块正方向为从端口 **R** 到端口 **C**。这意味着如果端口 **R** 的速度大于端口 **C** 的速度，则模块将力从 **R** 传递到 **C**。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
