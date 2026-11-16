---
type: simulink-block
title: 'Mass With Friction (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Elements'
documentation_page: 'masswithfrictionpb'
documentation_source_path: 'ref/masswithfrictionpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Mass With Friction (PB)

## 端口

### 输入

### **N** — 外部法向力控制信号，N 物理信号

用于指定外部法向力的控制信号的物理信号输入端口。模块将总法向力计算为外部法向力与重力加速度法向分量成比例的力之和。

如果信号变为负值，模块将输入值饱和到 0。

#### 依赖项

要启用此端口，请将 **External normal force specification** 参数设置为 `Variable`。

### 守恒

### **R** — 将质量连接到回路的基于位置的机械平动端口

基于位置的机械平动守恒端口，将质量连接到物理网络。

## 参数

### **Mass** — 恒定质量 `1 kg`（默认）| 正标量

质量值。质量在仿真期间恒定。

### **External normal force specification** — 外部法向力是恒定还是可变 `Constant`（默认）| `Variable`

选择施加到模块上的外部法向力是恒定还是可变：

- `Constant` — 使用 **Constant external normal force** 参数值指定法向力。
- `Variable` — 使用端口 **N** 处的物理信号指定法向力。

### **Constant external normal force** — 垂直于运动的力 `0 N`（默认）| 非负标量

沿垂直于运动方向施加到模块上的力。模块将总法向力计算为此值与重力加速度法向分量成比例的力之和。然后，模块基于总法向力以及比例系数 **Breakaway friction coefficient** 和 **Coulomb friction coefficient** 计算脱离摩擦力和库仑摩擦力。

#### 依赖项

要启用此参数，请将 **External normal force specification** 设置为 `Constant`。

### **Breakaway friction coefficient** — 法向力与脱离摩擦力之间的比例系数 `2.5`（默认）| 非负标量

用于基于法向力计算脱离摩擦力的系数，该力是库仑摩擦与静摩擦之和。参数值必须大于或等于 **Coulomb friction coefficient** 值。

### **Breakaway friction velocity** — Stribeck 摩擦的峰值速度 `0.1 m/s`（默认）| 正标量

Stribeck 摩擦达到峰值时的速度。此时，Stribeck 摩擦与库仑摩擦之和为脱离摩擦力。此参数指定速度阈值，该阈值影响仿真精度与速度之间的权衡。

### **Coulomb friction coefficient** — 法向力与阻碍运动的摩擦力之间的比例系数 `2`（默认）| 非负标量

用于基于法向力计算库仑摩擦力的系数，该力是阻碍运动的摩擦力。

### **Viscous friction coefficient** — 粘性损耗比例系数 `0 N/(m/s)`（默认）| 非负标量

摩擦力与相对速度之间的比例系数。粘性损耗不依赖于法向力。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

具有摩擦和重力效应的质点

Mass With Friction (PB) 模块表示一个具有摩擦和重力效应的质量，该质量沿倾斜导轨运动。重力可沿导轨诱发运动。重力和可选附加法向力引发与静止导轨之间的摩擦。

Mass With Friction (PB) 模块本质上是一个结构组件，由连接到 Translational Friction (PB) 模块端口 **F** 的 Mass (PB) 模块组成。Translational Friction (PB) 模块的端口 **B** 连接到隐式参考。

带摩擦的质量示意图

摩擦力是相对速度的函数，并且假定为 Stribeck、库仑和粘性分量之和，如图所示。

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

- *f*acc 是与质量加速度成比例的力。正方向的力使质量沿正方向加速。
- *f* 是网络中作用在质量上的其他机械组件的净力。
- *f*gp 是与重力加速度平行分量成比例的力，即沿导轨作用的重力加速度对应的力。
- *f*gn 是与重力加速度法向分量成比例的力，即在垂直于导轨方向作用的重力加速度对应的力。
- *f*friction 是摩擦力。
- *m* 是质量。
- *v* 是质量速度。端口 **B** 和 **F** 具有相同速度，*v*B = *v*F。
- *g* 是重力加速度。
- *θ* 是导轨倾角。
- *F*N 是法向力，沿垂直于导轨方向（即垂直于运动方向）作用在质量上。该力是外部法向力与重力加速度法向分量成比例的力之和。
- *F*N,ext 是外部法向力，沿垂直于导轨方向作用在质量上。这是由外部负载引起的可选力。可以将其指定为输入信号或模块参数。
- *F*C 是库仑摩擦。
- *K*C 是库仑摩擦系数。
- *F*brk 是脱离摩擦。
- *K*brk 是脱离摩擦系数。
- *f*v 是粘性摩擦系数。
- *v*brk 是脱离摩擦速度。
- *v*St 是 Stribeck 速度阈值。
- *v*Coul 是库仑速度阈值。
- *power\_dissipated* 是通过摩擦耗散的功率。

可以通过将 **Breakaway friction coefficient**、**Coulomb friction coefficient** 和 **Viscous friction coefficient** 参数设置为 0 来禁用摩擦效应。

Mechanical Translational Properties (PB) 模块指定网络中的重力加速度和导轨倾角。有关详细信息，请参阅 Interpreting Logged Forces in Mass Blocks。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
