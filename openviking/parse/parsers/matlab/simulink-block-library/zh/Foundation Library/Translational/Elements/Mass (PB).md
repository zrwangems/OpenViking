---
type: simulink-block
title: 'Mass (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'masspb'
documentation_source_path: 'ref/masspb.html'
language: zh-CN
chinese_source: worker-translation
---

# Mass (PB)

## 端口

### 守恒

### **R** — 将质量块连接到基于位置的机械平移电路的端口

基于位置的机械平移守恒端口，用于将质量块连接到物理网络。

## 参数

### **Mass** — 恒定质量 `1 kg`（默认）| 正标量

质量值。质量在仿真期间保持恒定。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

具有重力效应的质点

Mass (PB) 模块表示一个具有重力效应的质点，沿倾斜轨道运动。重力可以引起沿轨道的运动。力流方程为：

facc=m⋅v˙

facc=f+fgp

fgp=−m⋅g⋅sin(θ)

其中：

- *f*acc 是与质量加速度成正比的力。正力沿正方向加速质量块。
- *f* 是网络中其他机械组件作用在质量块上的净力。
- *f*gp 是与重力加速度平行分量成正比的力，即沿轨道方向作用的重力加速度。
- *m* 是质量。
- *v* 是质量块速度。
- *g* 是重力加速度。
- *θ* 是轨道倾角。

Mechanical Translational Properties (PB) 模块指定网络中的重力加速度和轨道倾角。有关详细信息，请参阅 Interpreting Logged Forces in Mass Blocks。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
