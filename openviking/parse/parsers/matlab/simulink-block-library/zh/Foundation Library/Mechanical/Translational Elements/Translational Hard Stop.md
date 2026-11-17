---
type: simulink-block
title: 'Translational Hard Stop'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalhardstop'
documentation_source_path: 'ref/translationalhardstop.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Hard Stop

## 端口
```yaml
ports:
- name: R
  summary: 滑块机械平移
  direction: conserving
- name: C
  summary: 壳体机械平移
  direction: conserving
```

### 守恒端口

### **R** — 滑块机械平移

与滑块关联的机械平移守恒端口，滑块在安装于壳体上的限位之间运动。

### **C** — 壳体机械平移

与壳体关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Upper bound
  summary: 滑块与上限之间的间隙 0.1 m（默认）| 标量
  group: ''
- name: Lower bound
  summary: 滑块与下限之间的间隙 -0.1 m（默认）| 标量
  group: ''
- name: Hard stop model
  summary: 选择硬限位模型 Stiffness and damping applied smoothly through transition region, damped rebound（默认）| Full stiffness and
    damping applied at bounds, undamped rebound | Full stiffness and damping applied at bounds, damped rebound | Based on
    coefficient of restitution
  group: ''
- name: Contact stiffness at upper bound
  summary: 上限处碰撞的弹性 1e6 N/m（默认）| 正标量
  group: ''
- name: Contact stiffness at lower bound
  summary: 下界处的碰撞弹性 1e6 N/m（默认）| 正标量
  group: ''
- name: Contact damping at upper bound
  summary: 上界处的耗散属性 150 N/(m/s)（默认）| 正标量
  group: ''
- name: Contact damping at lower bound
  summary: 下界处的耗散属性 150 N/(m/s)（默认）| 正标量
  group: ''
- name: Transition region
  summary: 力逐渐增大的区域 0.1 mm（默认）| 正标量
  group: ''
- name: Coefficient of restitution
  summary: 碰撞后滑块与挡块之间最终相对速度与初始相对速度之比 0.7（默认）| 0 到 1 之间的无量纲值
  group: ''
- name: Static contact speed threshold
  summary: 碰撞前滑块与挡块之间的阈值相对速度 0.001 m/s（默认）| 非负标量
  group: ''
- name: Static contact release force threshold
  summary: 从接触模式过渡到自由模式所需的阈值力 0.001 N（默认）| 正标量
  group: ''
```

### **Upper bound** — 滑块与上限之间的间隙 `0.1 m`（默认）| 标量

滑块与上限之间的间隙。以滑块位于原点为基准，相对于局部坐标系指定方向。正值表示滑块与上限之间的间隙。负值表示滑块侵入上限。

### **Lower bound** — 滑块与下限之间的间隙 `-0.1 m`（默认）| 标量

滑块与下限之间的间隙。以滑块位于原点为基准，相对于局部坐标系指定方向。负值表示滑块与下限之间的间隙。正值表示滑块侵入下限。

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

选择硬限位模型：

- `Stiffness and damping applied smoothly through
  transition region, damped rebound` — 指定一个过渡区域，在该区域内力从零逐渐增大。在过渡区域末端，模块施加完整的刚度和阻尼。该模型在回弹时施加阻尼，但阻尼被限制为刚度力的大小。因此，阻尼可以减小或消除刚度提供的力，但绝不会超过它。所有方程均为光滑的，不产生零穿越。
- `Full stiffness and damping applied at bounds,
  undamped rebound` — 该模型在上限和下限处施加完整的刚度和阻尼，回弹时无阻尼。当速度改变符号时，方程不产生零穿越，但在限位处存在基于位置的零穿越。回弹时无阻尼有助于快速推动滑块越过该位置。该模型具有非线性方程。
- `Full stiffness and damping applied at bounds, damped
  rebound` — 该模型在上限和下限处施加完整的刚度和阻尼，回弹时也施加阻尼。方程为切换线性，但会产生基于位置的零穿越。如果 `simscape.findNonlinearBlocks` 指示该模块阻止整个网络成为切换线性，请使用此硬限位模型。
- `Based on coefficient of restitution`
  — 该模型使用包含常规模式和瞬时模式的模式图来表示硬限位行为。所有方程均为光滑的，不产生零穿越。此建模选项可提高仿真性能。有关详细信息，请参阅 Model Based on Coefficient of Restitution。

### **Contact stiffness at upper bound** — 上限处碰撞的弹性 `1e6 N/m`（默认）| 正标量

滑块撞击上限时碰撞体的弹性属性。该参数值越大，碰撞体相互侵入越少，冲击越刚性。将该参数设置为较小值会使接触更软，但通常能改善收敛性和计算效率。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Contact stiffness at lower bound** — 下界处的碰撞弹性 `1e6 N/m`（默认）| 正标量

当滑块撞击下界时，碰撞体的弹性属性。该参数值越大，碰撞体相互穿透越少，冲击越刚性。将该参数设置为较小值会使接触更软，但通常能改善收敛性和计算效率。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Contact damping at upper bound** — 上界处的耗散属性 `150 N/(m/s)`（默认）| 正标量

当滑块撞击上界时，碰撞体的耗散属性。该参数值越大，交互过程中耗散的能量越多。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Contact damping at lower bound** — 下界处的耗散属性 `150 N/(m/s)`（默认）| 正标量

当滑块撞击下界时，碰撞体的耗散属性。该参数值越大，交互过程中耗散的能量越多。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Transition region** — 力逐渐增大的区域 `0.1 mm`（默认）| 正标量

力从零逐渐增大到完整值的区域。在过渡区域末端，模块施加完整的刚度和阻尼。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与挡块之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无量纲值

滑块弹回后，滑块与挡块之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前滑块与挡块之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与挡块之间的阈值相对速度。当滑块以小于该参数值的速度撞击壳体时，它们保持接触。否则，滑块弹回。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Based on coefficient of
restitution`。
## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a：基于恢复系数的建模选项

**Hard stop model** 参数的新选项 `Based on coefficient of restitution` 通过使用模式图来对硬限位建模，该模式图包括自由模式（滑块与壳体之间没有力传递）和静态接触模式（滑块与壳体之间的速度差为零）。

在之前的版本中，仅提供基于刚度和阻尼的建模选项。

此更改没有兼容性影响。

## 描述

双面平动硬限位

Translational Hard Stop 模块表示一个双面机械平动硬限位，用于将物体的运动限制在上下界之间。

机械平动硬限位示意图

滑块连接到端口 **R**，壳体连接到端口 **C**。当间隙在正方向上闭合时，该模块将力从端口 **R** 传递到端口 **C**。

该模块根据滑块速度 *v* = *v*R - *v*C 计算滑块位置 *x*。

*L* 是滑块长度，*y* 是滑块在负方向上的位置，*L* = |*x* - *y*|。该模块假设滑块长度为 0，并且不对 *L* 和 *y* 建模，但示意图使用这些符号来说明硬限位的基本设计。

*g*p 是正方向上的初始间隙，从 *x* 测量：

- 要使正间隙打开，*g*p 必须为正。
- *g*p 为负值表示滑块正在侵入上界。
- 当 *g*p - *x* ≤ 0 时，间隙闭合。

*g*n 是负方向上的初始间隙，从 *y* 测量：

- 要使负间隙打开，*g*n 必须为负。
- *g*n 为正值表示滑块正在侵入下界。
- 当 *y* - *g*n ≤ 0 时，间隙闭合。

该模块提供多个建模选项：

- 三个基于刚度和阻尼的选项。这些模型使用相似的基础方程，区别在于刚度和阻尼在边界处的应用方式。
- 一个基于恢复系数的建模选项。该模型与其他三个不同，因为它使用模式图来表示硬限位行为。

### 基于刚度和阻尼的模型

在基于刚度和阻尼的硬止点模型中，假设滑块与止点之间的冲击相互作用是弹性的。这一假设意味着该模块将止点表示为一个弹簧，当间隙消除时弹簧与滑块接触，并以与穿透量线性成正比的力阻止滑块穿透止点。该模块使用**上边界接触刚度**和**下边界接触刚度**参数来建模这种弹性。为了考虑能量耗散和非弹性效应，该模块使用**上边界接触阻尼**和**下边界接触阻尼**参数。

基本硬止点模型 `Full stiffness and damping applied at bounds, damped rebound` 使用以下方程：

F={Kp⋅(x−gp)+Dp⋅vfor x≥gp0for gn<x<gpKn⋅(x−gn)+Dn⋅vfor x≤gn

v=dxdt

其中：

- *F* 是滑块与壳体之间的相互作用力。
- *g*p 是滑块与上边界之间的初始间隙。
- *g*n 是滑块与下边界之间的初始间隙。
- *x* 是滑块位置。
- *K*p 是上边界的接触刚度。
- *K*n* 是下边界的接触刚度。
- *D*p 是上边界的阻尼系数。
- *D*n* 是下边界的阻尼系数。
- *v* 是滑块速度。
- *t* 是时间。

在 `Full stiffness and damping applied at bounds, undamped rebound` 硬止点模型中，方程包含附加项 `ge`(*v*,0) 和 `le`(*v*,0)。这些项确保该模块在回弹时不施加阻尼。

F={Kp⋅(x−gp)+Dp⋅v⋅ge(v,0)for x≥gp0for gn<x<gpKn⋅(x−gn)+Dn⋅v⋅le(v,0)for x≤gn

关系函数 `ge`（大于或等于）和 `le`（小于或等于）在速度改变符号时不会生成过零点。有关详细信息，请参阅 Simscape Language 中的 Enabling and Disabling Zero-Crossing Conditions。但是，求解器将 `ge` 和 `le` 函数视为非线性。因此，如果 `simscape.findNonlinearBlocks` 表明网络的其余部分是线性或分段线性的，请使用 `Full stiffness and damping applied at bounds, damped rebound` 模型以提高性能。

默认硬止点模型 `Stiffness and damping applied smoothly through transition region, damped rebound` 在方程中增加了两个过渡区域，每个边界各一个。当滑块经过过渡区域时，该模块将力从零平滑增加到完整值。在过渡区域末端，该模块施加完整的刚度和阻尼。在回弹时，该模块将刚度和阻尼力都平滑减小到零。这些方程也使用 `ge` 和 `le` 关系函数，它们不会产生过零点。

### 基于恢复系数的模型

与基于刚度和阻尼的模型不同，此模型不允许滑块穿透硬限位。硬限位行为由包含三个常规模式和三个瞬时模式的模式图表示：

- `FREE` — 滑块与壳体之间没有力传递。
- `CONTACT_UPPER` — 正间隙闭合。
- `CONTACT_LOWER` — 负间隙闭合。
- `RELEASE_UPPER` — 从 `CONTACT_UPPER` 过渡到 `FREE` 所需的瞬时模式。
- `RELEASE_LOWER` — 从 `CONTACT_LOWER` 过渡到 `FREE` 所需的瞬时模式。
- `IMPACT` — 滑块弹跳时使用的瞬时模式。

当滑块以低于静态接触速度阈值的速度缓慢撞击壳体时，滑块和壳体保持接触。否则，滑块弹跳。当滑块弹跳时，由于恢复系数而损失速度。在任一接触模式下，滑块速度 *v* = 0。要从接触模式过渡到自由模式，必须对滑块施加大于静态接触释放力阈值的力，并且过渡必须经过瞬时释放模式以设置初始速度。

此建模选项提高了仿真性能，因为静态接触模式不要求模块在处于接触模式时持续计算硬限位力。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
