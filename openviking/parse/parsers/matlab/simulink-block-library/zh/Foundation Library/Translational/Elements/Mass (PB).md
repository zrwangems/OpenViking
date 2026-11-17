---
type: simulink-block
title: 'Mass (PB)'
family: 'translational'
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

### **R** — 将质量连接到网络的基于位置的机械平移端口

基于位置的机械平移守恒端口，将质量连接到物理网络。

## 参数

### **Mass** — 常量质量 `1 kg`（默认）| 正标量

质量值。质量在仿真期间保持恒定。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

具有重力效应的质点

Mass (PB) 模块表示一个具有重力效应的质点，它沿倾斜轨道移动。重力可导致沿轨道的运动。力流方程为：

facc=m⋅v˙

facc=f+fgp

fgp=−m⋅g⋅sin(θ)

其中：

- *f*acc 是与质量加速度成比例的力。正力沿正方向加速质量。
- *f* 是网络中其他机械组件作用在质量上的净力。
- *f*gp 是与重力加速度的平行分量成比例的力，即沿轨道作用的重力加速度。
- *m* 是质量。
- *v* 是质量速度。
- *g* 是重力加速度。
- *θ* 是轨道倾角。

Mechanical Translational Properties (PB) 模块指定网络中的重力加速度和轨道倾角。有关详细信息，请参阅《解释质量模块中记录的力》。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
