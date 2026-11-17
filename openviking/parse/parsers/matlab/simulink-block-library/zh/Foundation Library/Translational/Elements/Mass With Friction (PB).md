---
type: simulink-block
title: 'Mass With Friction (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'masswithfrictionpb'
documentation_source_path: 'ref/masswithfrictionpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Mass With Friction (PB)

## 端口
```yaml
ports:
- name: N
  summary: 外部法向力控制信号，N 物理信号
  direction: input
- name: R
  summary: 将质量块连接到基于位置的机械平移电路的端口
  direction: input
```

### 输入

### **N** — 外部法向力控制信号，N 物理信号

用于指定外部法向力的控制信号的物理信号输入端口。该模块将总法向力计算为外部法向力与正比于重力加速度法向分量的力之和。

如果信号变为负值，该模块将输入值饱和为 0。

#### 依赖关系

要启用此端口，请将 **External normal force specification** 参数设置为 `Variable`。

### 守恒

### **R** — 将质量块连接到基于位置的机械平移电路的端口

基于位置的机械平移守恒端口，用于将质量块连接到物理网络。
## 参数
```yaml
parameters:
- name: Mass
  summary: 恒定质量 1 kg（默认）| 正标量
  group: ''
- name: External normal force specification
  summary: 外部法向力是恒定还是可变 Constant（默认）| Variable
  group: ''
- name: Constant external normal force
  summary: 垂直于运动的力 0 N（默认）| 非负标量
  group: ''
- name: Breakaway friction coefficient
  summary: 法向力与分离摩擦力之间的比例系数 2.5（默认）| 非负标量
  group: ''
- name: Breakaway friction velocity
  summary: Stribeck 摩擦的峰值速度 0.1 m/s（默认）| 正标量
  group: ''
- name: Coulomb friction coefficient
  summary: 法向力与阻碍运动的摩擦力之间的比例系数 2（默认）| 非负标量
  group: ''
- name: Viscous friction coefficient
  summary: 粘性损耗比例系数 0 N/(m/s)（默认）| 非负标量
  group: ''
```

### **Mass** — 恒定质量 `1 kg`（默认）| 正标量

质量值。质量在仿真期间保持恒定。

### **External normal force specification** — 外部法向力是恒定还是可变 `Constant`（默认）| `Variable`

选择施加到模块上的外部法向力是恒定还是可变：

- `Constant` — 使用 **Constant external normal force** 参数值指定法向力。
- `Variable` — 使用端口 **N** 处的物理信号指定法向力。

### **Constant external normal force** — 垂直于运动的力 `0 N`（默认）| 非负标量

沿垂直于运动方向施加到模块上的力。该模块将总法向力计算为此值与正比于重力加速度法向分量的力之和。然后，该模块基于总法向力和比例系数 **Breakaway friction coefficient** 与 **Coulomb friction coefficient** 计算分离摩擦力和库仑摩擦力。

#### 依赖关系

要启用此参数，请将 **External normal force specification** 设置为 `Constant`。

### **Breakaway friction coefficient** — 法向力与分离摩擦力之间的比例系数 `2.5`（默认）| 非负标量

用于基于法向力计算分离摩擦力的系数，分离摩擦力是库仑摩擦力和静摩擦力之和。该参数值必须大于或等于 **Coulomb friction coefficient** 值。

### **Breakaway friction velocity** — Stribeck 摩擦的峰值速度 `0.1 m/s`（默认）| 正标量

Stribeck 摩擦达到峰值时的速度。此时，Stribeck 摩擦力和库仑摩擦力之和即为分离摩擦力。该参数指定速度阈值，它影响仿真精度与速度之间的权衡。

### **Coulomb friction coefficient** — 法向力与阻碍运动的摩擦力之间的比例系数 `2`（默认）| 非负标量

用于基于法向力计算库仑摩擦力的系数，库仑摩擦力是阻碍运动的摩擦力。

### **Viscous friction coefficient** — 粘性损耗比例系数 `0 N/(m/s)`（默认）| 非负标量

摩擦力与相对速度之间的比例系数。粘性损耗不依赖于法向力。
## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

带摩擦和重力效应的质点

带摩擦的质量（PB）模块表示一个具有摩擦和重力效应的质量块，它沿倾斜导轨运动。重力可以引起沿导轨方向的运动。重力和可选的外部法向力会与静止导轨产生摩擦。

带摩擦的质量（PB）模块本质上是一个结构组件，由一个质量（PB）模块连接到平移摩擦（PB）模块的端口 **F** 组成。平移摩擦（PB）模块的端口 **B** 连接到一个隐式参考。

带摩擦的质量示意图

摩擦力是相对速度的函数，假定为 Stribeck、库仑和粘性分量之和，如下图所示。

摩擦力示意图

力流方程为：

facc=m⋅v˙

facc=f+fgp+ffriction

fgp=−m⋅g⋅sin(θ)

ffriction=−2e(Fbrk−FC)⋅exp(−(vvSt)2)⋅vvSt−FC⋅tanh(vvCoul)−fvv

FN=FN,ext+fgn

fgn=m⋅g⋅|cos(θ)|

Fbrk=FN⋅Kbrk

FC=FN⋅KC

vSt=vbrk2

vCoul=vbrk/10

power\_dissipated=−ffriction⋅v

其中：

- *f*acc 是与质量加速度成正比的力。正力沿正方向加速质量。
- *f* 是网络中其他机械组件作用在质量上的净力。
- *f*gp 是与重力加速度平行分量成正比的力，即沿导轨方向作用的重力加速度。
- *f*gn 是与重力加速度法向分量成正比的力，即沿垂直于导轨方向作用的重力加速度。
- *f*friction 是摩擦力。
- *m* 是质量。
- *v* 是质量速度。端口 **B** 和 **F** 具有相同的速度，*v*B = *v*F。
- *g* 是重力加速度。
- *θ* 是导轨倾角。
- *F*N 是法向力，沿垂直于导轨的方向，即垂直于运动方向，作用在质量上。该力是外部法向力与重力加速度法向分量对应的力之和。
- *F*N,ext 是外部法向力，沿垂直于导轨的方向作用在质量上。这是由外部负载引起的可选力。您可以将其指定为输入信号或模块参数。
- *F*C 是库仑摩擦力。
- *K*C 是库仑摩擦系数。
- *F*brk 是启动力。
- *K*brk 是启动力摩擦系数。
- *f*v 是粘性摩擦系数。
- *v*brk 是启动力摩擦速度。
- *v*St 是 Stribeck 速度阈值。
- *v*Coul 是库仑速度阈值。
- *power\_dissipated* 是通过摩擦耗散的功率。

您可以通过将 **Breakaway friction coefficient**、**Coulomb friction coefficient** 和 **Viscous friction coefficient** 参数设置为 0 来禁用摩擦效应。

机械平移属性（PB）模块指定网络中的重力加速度和导轨倾角。有关详细信息，请参阅 Interpreting Logged Forces in Mass Blocks。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可以提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
