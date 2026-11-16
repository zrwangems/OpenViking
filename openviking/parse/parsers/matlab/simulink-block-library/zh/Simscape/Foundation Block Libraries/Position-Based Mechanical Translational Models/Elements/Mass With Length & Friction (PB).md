---
type: simulink-block
title: 'Mass With Length & Friction (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Position-Based Mechanical Translational Models / Elements'
documentation_page: 'masswithlengthfrictionpb'
documentation_source_path: 'ref/masswithlengthfrictionpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Mass With Length & Friction (PB)

## 描述

具有长度、摩擦和重力效应的质量块

Mass With Length & Friction (PB) 模块表示具有长度、重力效应和摩擦的质量块，该质量块沿倾斜轨道运动。重力可以引起沿轨道的运动。重力以及可选附加法向力会引起与静止轨道之间的摩擦。

Mass With Length & Friction (PB) 模块本质上是一个结构组件，由连接到 Spacer (PB) 模块的 Mass (PB) 模块组成。Mass (PB) 模块还连接到 Translational Friction (PB) 模块的端口 **F**。Translational Friction (PB) 模块的端口 **B** 连接到隐式参考。

具有长度和摩擦的质量块示意图

摩擦力是相对速度的函数，并假定为 Stribeck、库仑和黏性分量之和，如图所示。

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

length=xF−xB

xLog=xB+fractionLog⋅length

power\_dissipated=−ffriction⋅v

其中：

- *f*acc 是与质量加速度成正比的力。正力沿正方向加速质量块。
- *f* 是网络中其他机械组件作用在质量块上的净力。
- *f*gp 是与重力加速度的平行分量，即沿轨道作用的重力加速度，成正比的力。
- *f*gn 是与重力加速度的法向分量，即沿垂直于轨道方向作用的重力加速度，成正比的力。
- *f*friction 是摩擦力。
- *m* 是质量。
- *v* 是质量块速度。端口 **B** 和 **F** 具有相同的速度，*v*B = *v*F。
- *g* 是重力加速度。
- *θ* 是轨道倾角。
- *F*N 是法向力，它沿垂直于轨道的方向，即垂直于运动方向，作用在质量块上。该力是外部法向力与正比于重力加速度法向分量的力之和。
- *F*N,ext 是外部法向力，它沿垂直于轨道的方向作用在质量块上。这是由外部载荷引起的可选力。您可以将其指定为输入信号或模块参数。
- *F*C 是库仑摩擦。
- *K*C 是库仑摩擦系数。
- *F*brk 是启动摩擦。
- *K*brk 是启动摩擦系数。
- *f*v 是黏性摩擦系数。
- *v*brk 是启动摩擦速度。
- *v*St 是 Stribeck 速度阈值。
- *v*Coul 是库仑速度阈值。
- *length* 是质量块长度。
- *x*B 和 *x*F 分别是端口 **B** 和 **F** 的绝对位置。
- *x*Log 是中间点的绝对位置（如果您启用 **Log the position of an intermediate point** 选项）。
- *fraction*Log 是从端口 **B** 到中间点的分数长度。
- *power\_dissipated* 是通过摩擦耗散的功率。

例如，要记录质量块中心的位置，请选中 **Log the position of an intermediate point** 复选框，并将 **Intermediate point fractional length from B** 参数设置为 `0.5`。

您可以通过将 **Breakaway friction coefficient**、**Coulomb friction coefficient** 和 **Viscous friction coefficient** 参数设置为 0 来禁用摩擦效应。

Mechanical Translational Properties (PB) 模块指定网络中的重力加速度和轨道倾角。有关详细信息，请参阅解释质量块中记录的力。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。

## 端口

### 输入

### **N** — 外部法向力控制信号，N 物理信号

用于指定外部法向力的控制信号的物理信号输入端口。该模块将总法向力计算为外部法向力与正比于重力加速度法向分量的力之和。

如果信号变为负值，该模块会将输入值饱和到 0。

#### 依赖关系

要启用此端口，请将 **External normal force specification** 参数设置为 `Variable`。

### 守恒

### **B** — 基座端口，基于位置的机械平动

基于位置的机械平动守恒端口，表示基座连接。

### **F** — 从动端口，基于位置的机械平动

基于位置的机械平动守恒端口，表示从动连接。对于非零长度，端口 **F** 的位置比端口 **B** 更正。

## 参数

### **Mass** — 恒定质量 `1 kg`（默认）| 正标量

质量值。质量在仿真期间恒定。

### **Length** — 质量块长度 `0 m`（默认）| 非负标量

质量块长度，即端口 **B** 和 **F** 之间的距离。该距离在仿真期间恒定。

### **Log the position of an intermediate point** — 是否记录中间点的位置 `off`（默认）| `on`

选中此复选框可记录端口 **B** 和 **F** 之间某个中间点的位置，例如质量块中心的位置。有关详细信息，请参阅数据记录。

### **Intermediate point fractional length from B** — 从端口 B 到被记录点的分数长度 `0.5`（默认）| 0 到 1 之间的无量纲标量

端口 **B** 与所记录的中间点之间的分数距离。

#### 依赖关系

要启用此参数，请选中 **Log the position of an intermediate point** 复选框。

### **External normal force specification** — 外部法向力是恒定还是可变 `Constant`（默认）| `Variable`

选择施加到模块的外部法向力是恒定还是可变：

- `Constant` — 使用 **Constant external normal force** 参数值指定法向力。
- `Variable` — 使用端口 **N** 处的物理信号指定法向力。

### **Constant external normal force** — 垂直于运动的力 `0 N`（默认）| 非负标量

沿垂直于运动方向施加到模块的力。该模块将总法向力计算为此值与正比于重力加速度法向分量的力之和。然后，该模块基于总法向力和比例系数 **Breakaway friction coefficient** 与 **Coulomb friction coefficient** 计算启动摩擦力和库仑摩擦力。

#### 依赖关系

要启用此参数，请将 **External normal force specification** 设置为 `Constant`。

### **Breakaway friction coefficient** — 法向力与启动摩擦力之间的比例系数 `2.5`（默认）| 非负标量

用于基于法向力计算启动摩擦力的系数，该力是库仑摩擦与静摩擦之和。该参数值必须大于或等于 **Coulomb friction coefficient** 值。

### **Breakaway friction velocity** — Stribeck 摩擦的峰值速度 `0.1 m/s`（默认）| 正标量

Stribeck 摩擦达到峰值时的速度。此时，Stribeck 摩擦与库仑摩擦之和为启动摩擦力。该参数指定速度阈值，它会影响仿真精度与速度之间的权衡。

### **Coulomb friction coefficient** — 法向力与阻碍运动的摩擦之间的比例系数 `2`（默认）| 非负标量

用于基于法向力计算库仑摩擦力的系数，该力是阻碍运动的摩擦。

### **Viscous friction coefficient** — 黏性损耗比例系数 `0 N/(m/s)`（默认）| 非负标量

摩擦力与相对速度之间的比例系数。黏性损耗不依赖于法向力。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**
