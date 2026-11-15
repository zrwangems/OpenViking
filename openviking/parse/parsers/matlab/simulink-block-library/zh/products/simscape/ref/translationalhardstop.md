---
type: simulink-block
title: 'Translational Hard Stop'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Translational Elements'
documentation_page: 'translationalhardstop'
documentation_source_path: 'ref/translationalhardstop.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Hard Stop

## 端口

### 守恒

### **R** — 滑块机械平移

与滑块关联的机械平移守恒端口，该滑块在安装于壳体上的止挡之间移动。

### **C** — 壳体机械平移

与壳体关联的机械平移守恒端口。

## 参数

### **上限** — 滑块与上限之间的间隙 `0.1 m`（默认）| 标量

滑块与上限之间的间隙。以滑块位于原点为参考，指定相对于局部坐标系的方向。正值指定滑块与上限之间的间隙。负值将滑块设置为侵入上限。

### **下限** — 滑块与下限之间的间隙 `-0.1 m`（默认）| 标量

滑块与下限之间的间隙。以滑块位于原点为参考，指定相对于局部坐标系的方向。负值指定滑块与下限之间的间隙。正值将滑块设置为侵入下限。

### **硬止挡模型** — 选择硬止挡模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

选择硬止挡模型：

- `Stiffness and damping applied smoothly through transition region, damped rebound` — 指定一个过渡区域，在该区域中力从零开始逐渐增加。在过渡区域末端，模块施加完整的刚度和阻尼。此模型在回弹时施加阻尼，但阻尼限制为刚度力的值。因此，阻尼可以减少或消除刚度提供的力，但永远不会超过它。所有方程都是平滑的，不会产生过零。
- `Full stiffness and damping applied at bounds, undamped rebound` — 此模型在上限和下限处施加完整刚度和阻尼并产生冲击，回弹时无阻尼。当速度改变符号时，方程不产生过零，但在边界处存在基于位置的过零。回弹时无阻尼有助于快速将滑块推过此位置。此模型具有非线性方程。
- `Full stiffness and damping applied at bounds, damped rebound` — 此模型在上限和下限处施加完整刚度和阻尼并产生冲击，回弹时也施加阻尼。方程是切换线性的，但会产生基于位置的过零。如果 `simscape.findNonlinearBlocks` 指示此模块阻止整个网络成为切换线性，则使用此硬止挡模型。
- `Based on coefficient of restitution` — 此模型使用包含常规模式和瞬时模式的模式图来表示硬止挡行为。所有方程都是平滑的，不会产生过零。此建模选项可提高仿真性能。有关详细信息，请参阅基于恢复系数的模型。

### **上限处接触刚度** — 上限处碰撞的弹性 `1e6 N/m`（默认）| 正标量

当滑块撞击上限时碰撞体的弹性属性。此参数值越大，物体相互侵入越少，冲击越刚性。将此参数设置为较小值会使接触更软，但通常会改善收敛性和计算效率。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Stiffness and damping applied smoothly through transition region, damped rebound`

### **下限处接触刚度** — 下限处碰撞的弹性 `1e6 N/m`（默认）| 正标量

当滑块撞击下限时碰撞体的弹性属性。此参数值越大，物体相互侵入越少，冲击越刚性。将此参数设置为较小值会使接触更软，但通常会改善收敛性和计算效率。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Stiffness and damping applied smoothly through transition region, damped rebound`

### **上限处接触阻尼** — 上限处的耗散特性 `150 N/(m/s)`（默认）| 正标量

当滑块撞击上限时碰撞体的耗散特性。此参数值越大，相互作用期间耗散的能量越多。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Stiffness and damping applied smoothly through transition region, damped rebound`

### **下限处接触阻尼** — 下限处的耗散特性 `150 N/(m/s)`（默认）| 正标量

当滑块撞击下限时碰撞体的耗散特性。此参数值越大，相互作用期间耗散的能量越多。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Stiffness and damping applied smoothly through transition region, damped rebound`

### **过渡区域** — 力逐渐增加的区域 `0.1 mm`（默认）| 正标量

力从零逐渐增加到满值的区域。在过渡区域末端，模块施加完整的刚度和阻尼。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为
`Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **恢复系数** — 滑块与止挡碰撞后最终相对速度与初始相对速度之比 `0.7`（默认）| 介于 0 和 1 之间的无单位值

滑块弹跳后，滑块与止挡之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为
`Based on coefficient of
restitution`。

### **静态接触速度阈值** — 碰撞前滑块与止挡之间的相对速度阈值 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与止挡之间的相对速度阈值。当滑块以小于此参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为
`Based on coefficient of
restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的力阈值 `0.001 N`（默认）| 正标量

从静态接触模式释放滑块所需的最小力。

#### 依赖关系

要启用此参数，请将 **硬止挡模型** 设置为
`Based on coefficient of
restitution`。

## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a: 基于恢复系数的建模选项

**硬止挡模型** 参数的新选项 `Based on coefficient of restitution` 通过使用模式图对硬止挡建模，该模式图包括自由模式（滑块和壳体之间没有力传递）和静态接触模式（滑块和壳体之间的速度差为零）。

在以前的版本中，仅提供基于刚度和阻尼的建模选项。

此更改不会影响兼容性。

## 描述

双面平移硬止挡

Translational Hard Stop 模块表示一个双面机械平移硬止挡，用于限制物体在上限和下限之间的运动。

机械平移硬止挡的示意图

滑块连接到端口 **R**，壳体连接到端口 **C**。当间隙沿正方向闭合时，模块将力从端口 **R** 传递到端口 **C**。

模块根据滑块速度 *v* = *v*R - *v*C 计算滑块位置 *x*。

*L* 是滑块长度，*y* 是负方向上的滑块位置，*L* = |*x* - *y*|。模块假设滑块长度为 0，并且不对 *L* 和 *y* 建模，但示意图使用这些符号来解释硬止挡的基本设计。

*g*p 是正方向上的初始间隙，从 *x* 测量：

- 要使正间隙打开，*g*p 必须为正。
- *g*p 为负值表示滑块正在侵入上限。
- 当 *g*p - *x* ≤ 0 时，间隙闭合。

*g*n 是负方向上的初始间隙，从 *y* 测量：

- 要使负间隙打开，*g*n 必须为负。
- *g*n 为正值表示滑块正在侵入下限。
- 当 *y* - *g*n ≤ 0 时，间隙闭合。

模块提供多种建模选项：

- 基于刚度和阻尼的三个选项。这些模型使用相似的底层方程，区别在于如何在边界处施加刚度和阻尼。
- 基于恢复系数的建模选项。此模型与其他三个不同，因为它使用模式图来表示硬止挡行为。

### 基于刚度和阻尼的模型

在基于刚度和阻尼的硬止挡模型中，假设滑块与止挡之间的冲击相互作用是弹性的。此假设意味着模块将止挡表示为弹簧，当间隙清除时该弹簧与滑块接触，并以与侵入量线性成正比的力阻止滑块侵入止挡。模块使用 **上限处接触刚度** 和 **下限处接触刚度** 参数对该弹性进行建模。为了考虑能量耗散和非弹性效应，模块使用 **上限处接触阻尼** 和 **下限处接触阻尼** 参数。

基本硬止挡模型 `Full stiffness and damping applied at bounds, damped rebound` 使用以下方程：

F={Kp⋅(x−gp)+Dp⋅vfor x≥gp0for gn<x<gpKn⋅(x−gn)+Dn⋅vfor x≤gn

v=dxdt

其中：

- *F* 是滑块与壳体之间的相互作用力。
- *g*p 是滑块与上限之间的初始间隙。
- *g*n 是滑块与下限之间的初始间隙。
- *x* 是滑块位置。
- *K*p 是上限处的接触刚度。
- *K*n 是下限处的接触刚度。
- *D*p 是上限处的阻尼系数。
- *D*n 是下限处的阻尼系数。
- *v* 是滑块速度。
- *t* 是时间。

在 `Full stiffness and damping applied at bounds, undamped rebound` 硬止挡模型中，方程包含附加项 `ge`(*v*,0) 和 `le`(*v*,0)。这些项确保模块在回弹时不施加阻尼。

F={Kp⋅(x−gp)+Dp⋅v⋅ge(v,0)for x≥gp0for gn<x<gpKn⋅(x−gn)+Dn⋅v⋅le(v,0)for x≤gn

关系函数 `ge`（大于或等于）和 `le`（小于或等于）在速度改变符号时不生成过零。有关详细信息，请参阅 Enabling and Disabling Zero-Crossing Conditions in Simscape Language。但是，求解器将 `ge` 和 `le` 函数视为非线性。因此，如果 `simscape.findNonlinearBlocks` 指示您的网络其余部分是线性或切换线性的，则使用 `Full stiffness and damping applied at bounds, damped rebound` 模型来提高性能。

默认硬止挡模型 `Stiffness and damping applied smoothly through transition region, damped rebound` 在方程中添加两个过渡区域，每个边界处一个。当滑块穿过过渡区域时，模块将力从零平滑增加到满值。在过渡区域末端，模块施加完整的刚度和阻尼。在回弹时，模块将刚度和阻尼力都平滑减小到零。这些方程也使用 `ge` 和 `le` 关系函数，它们不产生过零。

### 基于恢复系数的模型

与基于刚度和阻尼的模型不同，此模型不允许滑块侵入硬止挡。硬止挡行为由包含三个常规模式和三个瞬时模式的模式图表示：

- `FREE` — 滑块和壳体之间没有力传递。
- `CONTACT_UPPER` — 正间隙闭合。
- `CONTACT_LOWER` — 负间隙闭合。
- `RELEASE_UPPER` — 从 `CONTACT_UPPER` 过渡到 `FREE` 所需的瞬时模式。
- `RELEASE_LOWER` — 从 `CONTACT_LOWER` 过渡到 `FREE` 所需的瞬时模式。
- `IMPACT` — 滑块弹跳时使用的瞬时模式。

当滑块缓慢撞击壳体，且速度小于静态接触速度阈值时，滑块和壳体保持接触。否则，滑块弹跳。当滑块弹跳时，由于恢复系数而损失速度。在任一接触模式下，滑块速度 *v* = 0。要从接触模式过渡到自由模式，必须对滑块施加大于静态接触释放力阈值的力，并且过渡必须经过瞬时释放模式以设置初始速度。

此建模选项可提高仿真性能，因为当模块处于接触模式时，静态接触模式不要求模块持续计算硬止挡力。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
