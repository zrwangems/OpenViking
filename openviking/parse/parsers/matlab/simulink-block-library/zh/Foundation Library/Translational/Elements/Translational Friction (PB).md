---
type: simulink-block
title: 'Translational Friction (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalfrictionpb'
documentation_source_path: 'ref/translationalfrictionpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Friction (PB)

## 端口
```yaml
ports:
- name: N
  summary: 法向力控制信号，N 物理信号
  direction: input
- name: B
  summary: 基座端口 基于位置的机械平移
  direction: input
- name: F
  summary: 从动端口 基于位置的机械平移
  direction: input
```

### 输入

### **N** — 法向力控制信号，N 物理信号

用于指定法向力的控制信号的物理信号输入端口。
如果信号变为负值，该模块会将输入值饱和为 0。

#### 依赖关系

要启用此端口，请将 **Normal force specification**
参数设置为 `Variable`。
### 守恒

### **B** — 基座端口 基于位置的机械平移

基于位置的机械平移守恒端口，表示基座
连接。

### **F** — 从动端口 基于位置的机械平移

基于位置的机械平移守恒端口，表示
从动连接。对于正长度，端口 **F** 的位置
比端口 **B** 更正。
## 参数
```yaml
parameters:
- name: Normal force specification
  summary: 法向力是恒定的还是可变的 Constant（默认）| Variable
  group: ''
- name: Normal force
  summary: 垂直于运动方向的力 10 N（默认）| 非负标量
  group: ''
- name: Breakaway friction coefficient
  summary: 法向力与分离摩擦力之间的比例系数 2.5（默认）| 正标量
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

### **Normal force specification** — 法向力是恒定的还是可变的 `Constant`（默认）| `Variable`

选择施加到该模块的法向力是恒定的还是可变的：

- `Constant` — 使用
  **Normal force** 参数值指定法向力。
- `Variable` — 使用端口 **N** 处的物理
  信号指定法向力。

### **Normal force** — 垂直于运动方向的力 `10 N`（默认）| 非负标量

沿垂直于运动方向施加到该模块的力。该模块
基于此值以及比例系数 **Breakaway friction
coefficient** 和 **Coulomb friction coefficient** 计算分离摩擦力
和库仑摩擦力。

#### 依赖关系

要启用此参数，请将 **Normal force specification** 设置为
`Constant`。

### **Breakaway friction coefficient** — 法向力与分离摩擦力之间的比例系数 `2.5`（默认）| 正标量

用于基于法向力计算分离摩擦力的系数，分离摩擦力是
库仑摩擦力和静摩擦力之和。该参数值必须
大于或等于 **Coulomb friction coefficient** 值。

### **Breakaway friction velocity** — Stribeck 摩擦的峰值速度 `0.1 m/s`（默认）| 正标量

Stribeck 摩擦达到峰值时的速度。此时，Stribeck
摩擦力和库仑摩擦力之和即为分离摩擦力。该参数
指定速度阈值，这会影响仿真
精度和速度之间的权衡。

### **Coulomb friction coefficient** — 法向力与阻碍运动的摩擦力之间的比例系数 `2`（默认）| 非负标量

用于基于法向力计算库仑摩擦力的系数，库仑摩擦力是
阻碍运动的摩擦力。

### **Viscous friction coefficient** — 粘性损耗比例系数 `0 N/(m/s)`（默认）| 非负标量

摩擦力与相对速度之间的比例系数。
粘性损耗不依赖于法向力。
## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于位置机械平动系统中表面之间的电阻性摩擦接触

平动摩擦 (PB) 模块表示表面之间的电阻性摩擦接触。

摩擦力是相对速度的函数，并假定为 Stribeck、库仑和粘性分量之和，如图所示。

摩擦力示意图

Stribeck 摩擦 *F*S 是在低速下发生的负斜率特性 [1]。库仑摩擦 *F*C 在任何速度下产生恒定力。粘性摩擦 *F*V 阻碍运动，其力与相对速度成正比。在零速度附近，库仑摩擦和 Stribeck 摩擦之和即为分离摩擦力 *F*brk。

您指定法向力 *F*N，它沿垂直于导轨的方向（即垂直于运动方向）作用于模块。该模块根据法向力以及您同样指定的比例系数计算分离摩擦力和库仑摩擦力。法向力可以是恒定的，也可以是变化的。

摩擦力用以下方程近似：

ffriction=−2e(Fbrk−FC)⋅exp(−(vvSt)2)⋅vvSt−FC⋅tanh(vvCoul)−fvv

Fbrk=FN⋅Kbrk

FC=FN⋅KC

vSt=vbrk2

vCoul=vbrk/10

v=vF−vB

length=xF−xB

power\_dissipated=−ffriction⋅v

其中：

- *f*friction 是摩擦力。
- *F*N 是法向力，它沿垂直于导轨的方向（即垂直于运动方向）作用于模块。
- *F*C 是库仑摩擦。
- *K*C 是库仑摩擦系数。
- *F*brk 是分离摩擦。
- *K*brk 是分离摩擦系数。
- *f*v 是粘性摩擦系数。
- *v*brk 是分离摩擦速度。
- *v*St 是 Stribeck 速度阈值。
- *v*Coul 是库仑速度阈值。
- *v* 是相对速度。
- *v*B 和 *v*F 分别是端口 **B** 和 **F** 的绝对速度。
- *length* 是摩擦长度。
- *x*B 和 *x*F 分别是端口 **B** 和 **F** 的绝对位置。
- *power\_dissipated* 是通过摩擦耗散的功率。

第一个方程中的负号反映了基于位置机械平动域中使用的力流约定。除非端口反转，否则 *f*friction 的正值表示模块处于压缩状态，*f*friction 的负值表示模块处于拉伸状态。有关详细信息，请参阅双端口模块方向和力流约定。

力方程中 Stribeck 部分使用的指数函数是连续的，并且在速度幅值大于分离摩擦速度时衰减。

力方程中库仑部分使用的双曲正切函数确保方程在 *v* = 0 处光滑且连续，但在非零速度下会迅速达到其完整值。

连接 **B** 和 **F** 是基于位置的机械平动守恒端口。摩擦力从端口 **B** 作用于端口 **F**。正摩擦力驱动端口 **F** 沿正方向运动。您可以通过 **Normal force** 参数或物理信号端口 **N** 指定法向力。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
