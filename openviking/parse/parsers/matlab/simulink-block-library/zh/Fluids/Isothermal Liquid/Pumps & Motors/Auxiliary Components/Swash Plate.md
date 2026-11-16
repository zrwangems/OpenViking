---
type: simulink-block
title: 'Swash Plate'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors / Auxiliary Components'
documentation_page: 'swashplate'
documentation_source_path: 'ref/swashplate.html'
language: zh-CN
chinese_source: worker-translation
---

# Swash Plate

## 端口

### 守恒

### **A** — 与执行器机械平移相关的机械端口

斜盘执行器速度和力。

### **P** — 与活塞机械平移相关的机械端口

活塞端速度和力。

### **S** — 与轴机械旋转相关的机械端口

驱动轴角速度和转矩。旋转是相对于环境的。

## 参数

### **Swash plate actuator arm** — 执行器延伸长度 `0.065 m`（默认）| positive scalar

完全伸展的执行器臂长度。

### **Cylinder block pitch radius** — 缸体节圆半径 `0.05 m`（默认）| positive scalar

旋转缸体的节圆半径。

### **Piston offset from the plate** — 静止活塞偏移 `0 m`（默认）| scalar

执行器处于中立位置时的活塞偏移。正值且非零表示活塞部分缩回。负值且非零表示在初始执行器远离缸体位移期间，伸出的活塞仍保持在缸体内。

### **Viscous friction coefficient** — 转矩粘性摩擦系数 `50 N/(m/s)`（默认）| positive scalar

用于粘性摩擦引起的转矩方程中的系数。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors / Auxiliary Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

单活塞、等温轴向柱塞泵中的斜盘

Swash Plate 模块对轴向柱塞泵内的单个活塞驱动的斜盘进行建模。它将线性执行转换为旋转运动，当连接到 Valve Plate Orifice (IL) 模块时，会周期性地将活塞与泵的进油口和排油口连通。您可以将多个斜盘模块连接到多个活塞。

**轴向柱塞泵单元内斜盘的示意图**

### 力平衡

如果活塞、执行器和斜盘所做的净功为零，则斜盘处于动态平衡：

FPδP+FAδA+(τ−τres)δy=0,

其中：

- *F*P*δ*P
  是由于活塞位移所做的功。
- *F*A*δ*A
  是由于执行器位移所做的功。
- *(τ-τ*res*)δ*y
  是由于与斜盘运动相切的净斜盘转矩所做的功。

斜盘转矩为：

τ=−rPrAxAFPsinγ+τres,

其中：

- *r*P 是 **Cylinder block pitch radius**。
- *r*A 是 **Swash plate actuator arm**。
- *X*A 是执行器位移。
- *F*P 是活塞力。
- *γ* 是斜盘角位移。

粘性摩擦转矩，即由于斜盘-活塞接触引起的运动阻力，为：

τres=μviscousωrP2,

其中：

- *μ*viscous 是 **Viscous friction coefficient**。
- *ω* 是转子角速度。

### 活塞动力学

活塞位移 *x* 与执行器位移成正比：

x=−hoff(1+xA2rA2−1)−rPrAxAcosγ,

其中 *h*off 是 **Piston offset from the plate**。如果位移朝向缸体移动，则为正。

活塞速度为：

VP=rPrAxAωsin(γ)−rPrAVAcosγ−hoffrA2xAVA1+xA2rA2,

其中 *V*A 是执行器速度。

### 假设和限制

本模块考虑活塞与斜盘之间粘性摩擦的影响，但忽略斜盘和流体惯性。
