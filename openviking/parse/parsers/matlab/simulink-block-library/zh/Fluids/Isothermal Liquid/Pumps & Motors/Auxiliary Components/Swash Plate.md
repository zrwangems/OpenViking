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
```yaml
ports:
- name: A
  summary: 与执行器机械平移相关联的机械端口
  direction: conserving
- name: P
  summary: 与活塞机械平移相关联的机械端口
  direction: conserving
- name: S
  summary: 与轴机械旋转相关联的机械端口
  direction: conserving
```

### 守恒端口

### **A** — 与执行器机械平移相关联的机械端口

斜盘执行器速度和力。

### **P** — 与活塞机械平移相关联的机械端口

活塞端速度和力。

### **S** — 与轴机械旋转相关联的机械端口

驱动轴角速度和扭矩。旋转相对于环境。
## 参数
```yaml
parameters:
- name: Swash plate actuator arm
  summary: 执行器延伸长度 0.065 m（默认）| 正标量
  group: ''
- name: Cylinder block pitch radius
  summary: 缸体节圆半径 0.05 m（默认）| 正标量
  group: ''
- name: Piston offset from the plate
  summary: 静止活塞偏移 0 m（默认）| 标量
  group: ''
- name: Viscous friction coefficient
  summary: 扭矩粘性摩擦系数 50 N/(m/s)（默认）| 正标量
  group: ''
```

### **Swash plate actuator arm** — 执行器延伸长度 `0.065 m`（默认）| 正标量

完全延伸的执行器臂长度。

### **Cylinder block pitch radius** — 缸体节圆半径 `0.05 m`（默认）| 正标量

旋转缸体的节圆半径。

### **Piston offset from the plate** — 静止活塞偏移 `0 m`（默认）| 标量

执行器处于中立位置时的活塞偏移。正的、非零值表示活塞部分缩回。负的、非零值表示在执行器初始远离缸体位移期间，活塞保持伸出并仍在缸体内。

### **Viscous friction coefficient** — 扭矩粘性摩擦系数 `50 N/(m/s)`（默认）| 正标量

用于计算粘性摩擦扭矩方程中的系数。
## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors / Auxiliary Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

单活塞等温轴向柱塞泵中的斜盘

Swash Plate 模块对轴向柱塞泵内的单个活塞驱动斜盘进行建模。它将线性驱动转换为旋转运动，当连接到 Valve Plate Orifice (IL) 模块时，该旋转运动周期性地将活塞与泵的吸入口和排出口连通。您可以将多个斜盘模块连接到多个活塞。

**轴向柱塞泵单元中斜盘的示意图**

### 力平衡

如果活塞、执行器和斜盘所做的净功为零，则斜盘处于动态平衡：

FPδP+FAδA+(τ−τres)δy=0，

其中：

- *F*P*δ*P
  是由于活塞位移所做的功。
- *F*A*δ*A
  是由于执行器位移所做的功。
- *(τ-τ*res*)δ*y*
  是由于与斜盘运动相切的净斜盘扭矩所做的功。

斜盘扭矩为：

τ=−rPrAxAFPsinγ+τres，

其中：

- *r*P 是 **Cylinder
  block pitch radius**。
- *r*A 是 **Swash
  plate actuator arm**。
- *X*A 是执行器
  位移。
- *F*P 是活塞
  力。
- *γ* 是斜盘角位移。

粘性摩擦扭矩，即由于斜盘-活塞接触对运动产生的阻力，为：

τres=μviscousωrP2，

其中：

- *μ*viscous 是
  **Viscous friction coefficient**。
- *ω* 是转子角速度。

### 活塞动力学

活塞位移 *x* 与执行器位移成正比：

x=−hoff(1+xA2rA2−1)−rPrAxAcosγ，

其中 *h*off 是 **Piston
offset from the plate**。如果活塞向缸体方向移动，则位移为正。

活塞速度为：

VP=rPrAxAωsin(γ)−rPrAVAcosγ−hoffrA2xAVA1+xA2rA2，

其中 *V*A 是
执行器速度。

### 假设和限制

此模块考虑了活塞与斜盘之间粘性摩擦的影响，但忽略了斜盘和流体的惯性。
