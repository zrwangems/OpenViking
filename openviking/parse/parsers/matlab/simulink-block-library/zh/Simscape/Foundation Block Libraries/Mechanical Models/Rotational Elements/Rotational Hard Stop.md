---
type: simulink-block
title: 'Rotational Hard Stop'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Rotational Elements'
documentation_page: 'rotationalhardstop'
documentation_source_path: 'ref/rotationalhardstop.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Hard Stop

## 端口

### 守恒

### **R** — 滑块机械旋转

与滑块关联的机械旋转守恒端口，该滑块在安装于壳体上的限位之间运动。

### **C** — 壳体机械旋转

与壳体关联的机械旋转守恒端口。

## 参数

### **上边界** — 滑块与上边界之间的间隙 `0.1 rad`（默认）| scalar

滑块与上边界之间的间隙。相对于局部坐标系指定方向，其中滑块位于原点。正值指定滑块与上边界之间的间隙。负值将滑块设置为穿入上边界。

### **下边界** — 滑块与下边界之间的间隙 `-0.1 rad`（默认）| scalar

滑块与下边界之间的间隙。相对于局部坐标系指定方向，其中滑块位于原点。负值指定滑块与下边界之间的间隙。正值将滑块设置为穿入下边界。

### **硬限位模型** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

选择硬限位模型：

- `Stiffness and damping applied smoothly through
  transition region, damped rebound` — 指定一个过渡区域，在该区域中扭矩从零开始增加。在过渡区域末端，模块施加完整刚度和阻尼。该模型在回弹时施加阻尼，但阻尼限制为刚度扭矩的值。因此，阻尼可以减少或消除刚度提供的扭矩，但绝不会超过它。所有方程都是平滑的，不产生过零。
- `Full stiffness and damping applied at bounds,
  undamped rebound` — 该模型在上边界和下边界处施加完整刚度和阻尼并产生冲击，回弹时无阻尼。当速度改变符号时，方程不产生过零，但在边界处存在基于位置的过零。回弹时无阻尼有助于快速将滑块推过该位置。该模型具有非线性方程。
- `Full stiffness and damping applied at bounds, damped
  rebound` — 该模型在上边界和下边界处施加完整刚度和阻尼并产生冲击，回弹时也施加阻尼。方程是切换线性的，但会产生基于位置的过零。如果 `simscape.findNonlinearBlocks` 指示此模块阻止整个网络成为切换线性，请使用此硬限位模型。
- `Based on coefficient of restitution` — 该模型使用具有常规模式和瞬时模式的模式图来表示硬限位行为。所有方程都是平滑的，不产生过零。该建模选项提高了仿真性能。有关详细信息，请参阅 基于恢复系数的模型。

### **上边界接触刚度** — 上边界处碰撞的弹性 `1e6 N*m/rad`（默认）| positive scalar

当滑块撞击上边界时，碰撞体的弹性属性。该参数值越大，物体彼此穿入越少，冲击越刚硬。将此参数设置为较小值会使接触更软，但通常会改善收敛性和计算效率。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **下边界接触刚度** — 下边界处碰撞的弹性 `1e6 N*m/rad`（默认）| positive scalar

当滑块撞击下边界时，碰撞体的弹性属性。该参数值越大，物体彼此穿入越少，冲击越刚硬。将此参数设置为较小值会使接触更软，但通常会改善收敛性和计算效率。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **上边界接触阻尼** — 上边界处的耗散属性 `0.01 N*m/(rad/s)`（默认）| positive scalar

当滑块撞击上边界时，碰撞体的耗散属性。该参数值越大，相互作用期间耗散的能量越多。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **下边界接触阻尼** — 下边界处的耗散属性 `0.01 N*m/(rad/s)`（默认）| positive scalar

当滑块撞击下边界时，碰撞体的耗散属性。该参数值越大，相互作用期间耗散的能量越多。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **过渡区域** — 扭矩增加所在的区域 `0.001 rad`（默认）| positive scalar

扭矩从零增加到完整值的区域。在过渡区域末端，模块施加完整刚度和阻尼。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为
`Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| unitless value between 0 and 1

滑块弹跳后，滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为
`Based on coefficient of
restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位之间的阈值相对速度 `0.1 rad/s`（默认）| nonnegative scalar

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于此参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为
`Based on coefficient of
restitution`。

### **静态接触释放扭矩阈值** — 从接触模式转换到自由模式所需的阈值扭矩 `0.001 N*m`（默认）| positive scalar

将滑块从静态接触模式释放所需的最小扭矩。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为
`Based on coefficient of
restitution`。

## 所属库

Simscape / Foundation Library / Mechanical / Rotational Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a：基于恢复系数的建模选项

**硬限位模型** 参数的新选项 `Based on coefficient of restitution` 通过使用模式图来对硬限位建模，该模式图包括自由模式（滑块与壳体之间没有扭矩传递）和静态接触模式（滑块与壳体之间的速度差为零）。

在以前的版本中，仅提供基于刚度和阻尼的建模选项。

此更改没有兼容性影响。

## 描述

双面旋转硬限位

Rotational Hard Stop 模块表示一个双面机械旋转硬限位，将物体的运动限制在上边界和下边界之间。

机械旋转硬限位的示意图

滑块连接到端口 **R**，壳体连接到端口 **C**。当正方向上的间隙闭合时，模块将扭矩从端口 **R** 传递到端口 **C**。

模块根据滑块角速度 *ω* = *ω*R - *ω*C 计算滑块角位置 *φ*。

*θ* 是滑块弧角，*ψ* 是负侧的滑块角位置，*θ* = |*φ* - *ψ*|。模块假设滑块弧角为 0，并且不对 *θ* 和 *ψ* 建模，但示意图使用这些符号来解释硬限位的基本设计。

*g*p 是正侧的初始间隙，从 *x* 测量：

- 要使正间隙打开，*g*p 必须为正。
- *g*p 的负值意味着滑块正在穿入上边界。
- 当 *g*p - *φ* ≤ 0 时，间隙闭合。

*g*n 是负侧的初始间隙，从 *y* 测量：

- 要使负间隙打开，*g*n 必须为负。
- *g*n 的正值意味着滑块正在穿入下边界。
- 当 *ψ* - *g*n ≤ 0 时，间隙闭合。

模块提供若干建模选项：

- 三个基于刚度和阻尼的选项。这些模型使用相似的基础方程，不同之处在于边界处刚度和阻尼的应用方式。
- 一个基于恢复系数的建模选项。该模型与其他三个不同，因为它使用模式图来表示硬限位行为。

### 基于刚度和阻尼的模型

在基于刚度和阻尼的硬限位模型中，假设滑块与限位之间的冲击相互作用是弹性的。该假设意味着模块将限位表示为一个弹簧，当间隙清除时该弹簧与滑块接触，并以与穿入量成线性比例的扭矩阻止滑块穿入限位。模块使用 **上边界接触刚度** 和 **下边界接触刚度** 参数来建模这种弹性。为了考虑能量耗散和非弹性效应，模块使用 **上边界接触阻尼** 和 **下边界接触阻尼** 参数。

基本硬限位模型 `Full stiffness and damping applied at bounds, damped rebound` 使用以下方程：

T={Kp⋅(φ−gp)+Dp⋅ωfor φ≥gp0for gn<φ<gpKn⋅(φ−gn)+Dn⋅ωfor φ≤gn

ω=dφdt

其中：

- *T* 是滑块与壳体之间的相互作用扭矩。
- *g*p 是滑块与上边界之间的初始间隙。
- *g*n 是滑块与下边界之间的初始间隙。
- *φ* 是滑块角位置。
- *K*p 是上边界处的接触刚度。
- *K*n 是下边界处的接触刚度。
- *D*p 是上边界处的阻尼系数。
- *D*n 是下边界处的阻尼系数。
- *ω* 是滑块角速度。
- *t* 是时间。

在 `Full stiffness and damping applied at bounds, undamped rebound` 硬限位模型中，方程包含附加项 `ge`(*ω*,0) 和 `le`(*ω*,0)。这些项确保模块在回弹时不施加阻尼。

T={Kp⋅(φ−gp)+Dp⋅ω⋅ge(ω,0)for φ≥gp0for gn<φ<gpKn⋅(φ−gn)+Dn⋅ω⋅le(ω,0)for φ≤gn

关系函数 `ge`（大于或等于）和 `le`（小于或等于）在角速度改变符号时不生成过零。有关详细信息，请参阅 Enabling and Disabling Zero-Crossing Conditions in Simscape Language。但是，求解器将 `ge` 和 `le` 函数视为非线性。因此，如果 `simscape.findNonlinearBlocks` 指示网络的其余部分为线性或切换线性，请使用 `Full stiffness and damping applied at bounds, damped rebound` 选项以提高性能。

默认硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound` 在方程中增加两个过渡区域，每个边界一个。当滑块穿过过渡区域时，模块将扭矩从零平滑增加到完整值。在过渡区域末端，模块施加完整刚度和阻尼。在回弹时，模块将刚度和阻尼扭矩平滑减小到零。这些方程也使用 `ge` 和 `le` 关系函数，它们不产生过零。

### 基于恢复系数的模型

与基于刚度和阻尼的模型不同，该模型不允许滑块穿入硬限位。硬限位行为由具有三个常规模式和三个瞬时模式的模式图表示：

- `FREE` — 滑块与壳体之间没有扭矩传递。
- `CONTACT_UPPER` — 正间隙闭合。
- `CONTACT_LOWER` — 负间隙闭合。
- `RELEASE_UPPER` — 从 `CONTACT_UPPER` 转换到 `FREE` 所需的瞬时模式。
- `RELEASE_LOWER` — 从 `CONTACT_LOWER` 转换到 `FREE` 所需的瞬时模式。
- `IMPACT` — 滑块弹跳时使用的瞬时模式。

当滑块以低于静态接触速度阈值的速度缓慢撞击壳体时，滑块和壳体保持接触。否则，滑块弹跳。当滑块弹跳时，它会因恢复系数而损失速度。在任一接触模式下，滑块速度 *ω* = 0。要从接触模式转换到自由模式，必须向滑块施加大于静态接触释放扭矩阈值的扭矩，并且转换必须经过瞬时释放模式以设置初始速度。

该建模选项提高了仿真性能，因为当模块处于接触模式时，静态接触模式不要求模块持续计算硬限位扭矩。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
