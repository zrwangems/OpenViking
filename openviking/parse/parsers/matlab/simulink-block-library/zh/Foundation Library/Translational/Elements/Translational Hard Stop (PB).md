---
type: simulink-block
title: 'Translational Hard Stop (PB)'
family: 'translational'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalhardstoppb'
documentation_source_path: 'ref/translationalhardstoppb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Hard Stop (PB)

## 端口

### 守恒

### **B** — 基础端口：基于位置的机械平移

表示基础连接的基于位置的机械平移守恒端口。

### **F** — 从动端口：基于位置的机械平移

表示从动连接的基于位置的机械平移守恒端口。当硬停止未接合时，端口 **F** 的位置比端口 **B** 更正。

## 参数

### **硬停止模型** — 选择硬停止模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

选择硬停止模型：

- `Stiffness and damping applied smoothly through transition region,
  damped rebound` — 指定一个过渡区域，在该区域中，力从零开始逐渐增大。在过渡区域末端，模块施加完整刚度和阻尼。此模型在反弹时施加阻尼，但阻尼受限于刚度力的值。因此，阻尼可以减小或消除刚度提供的力，但绝不会超过它。所有方程都是光滑的，并且不产生零穿越。
- `Full stiffness and damping applied at bounds, undamped
  rebound` — 此模型在冲击时施加完整刚度和阻尼，反弹时不施加阻尼。当速度改变符号时，方程不产生零穿越，但存在基于位置的零穿越。此模型具有非线性方程。
- `Full stiffness and damping applied at bounds, damped
  rebound` — 此模型在冲击时施加完整刚度和阻尼，反弹时也施加阻尼。方程是切换线性的，但会产生基于位置的零穿越。如果 `simscape.findNonlinearBlocks` 指示此模块阻止整个网络成为切换线性，请使用此硬停止模型。
- `Based on coefficient of restitution` — 此模型使用具有常规模式和瞬时模式的模式图来表示硬停止行为。所有方程都是光滑的，并且不产生零穿越。此建模选项可提高仿真性能。

### **接触刚度** — 碰撞的弹性 `1e6 N/m`（默认）| 正标量

碰撞物体的弹性属性。此参数值越大，物体相互穿透越少，冲击越刚硬。将此参数设置为较小值会使接触更软，但通常会改善收敛性和计算效率。

#### 依赖关系

要启用此参数，请将 **硬停止模型** 设置为

- `Stiffness and damping applied smoothly through transition region,
  damped rebound`
- `Full stiffness and damping applied at bounds, undamped
  rebound`
- `Full stiffness and damping applied at bounds, damped
  rebound`

### **接触阻尼** — 碰撞期间的耗散属性 `150 N/(m/s)`（默认）| 正标量

碰撞物体的耗散属性。此参数值越大，冲击期间耗散的能量越多。

#### 依赖关系

要启用此参数，请将 **硬停止模型** 设置为

- `Stiffness and damping applied smoothly through transition region,
  damped rebound`
- `Full stiffness and damping applied at bounds, undamped
  rebound`
- `Full stiffness and damping applied at bounds, damped
  rebound`

### **过渡区域** — 力逐渐增大的区域 `0.1 mm`（默认）| 正标量

力从零逐渐增大到完整值的区域。在过渡区域末端，模块施加完整刚度和阻尼。

#### 依赖关系

要启用此参数，请将 **硬停止模型** 设置为
`Stiffness and damping applied smoothly through transition region,
damped rebound`。

### **恢复系数** — 碰撞后两物体之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

碰撞后两物体之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **硬停止模型** 设置为
`Based on coefficient of restitution`。

### **初始状态** — 硬停止初始状态是自由还是接触 `Free`（默认）| `In contact`

选择硬停止初始状态：

- `Free` — 硬停止两侧之间没有力传递。通过指定相对速度和间隙长度来初始化硬停止。
- `In contact` — 硬停止两侧之间的间隙闭合。通过指定力来初始化硬停止。

#### 依赖关系

要启用此参数，请将 **硬停止模型** 设置为
`Based on coefficient of restitution`。

### **静态接触速度阈值** — 碰撞前物体之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前两个物体之间的阈值相对速度。当两个物体以小于此参数值的速度碰撞时，它们保持接触。为避免对两个物体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **硬停止模型** 设置为
`Based on coefficient of restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将两个物体从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **硬停止模型** 设置为
`Based on coefficient of restitution`。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于位置的机械平移系统中的硬停止

Translational Hard Stop (PB) 模块表示一个机械平移硬停止，它将两个物体的相对位置限制为大于或等于 0 m。您可以将两个物体之间的接触建模为连续弹簧和阻尼器，或基于恢复系数的瞬时冲量。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。当硬停止未接合时，端口 **F** 的位置比端口 **B** 更正。力从端口 **B** 作用到端口 **F**。正力用于使硬停止脱离。长度是硬停止两侧之间的间隙：

length=xF−xB

其中 *x*B 和 *x*F 分别是端口 **B** 和 **F** 的绝对位置。

### 基于刚度和阻尼的模型

在基于刚度和阻尼的硬停止模型中，假设两侧之间的冲击相互作用是弹性的。该模块使用 **接触刚度** 参数对此弹性进行建模。为了考虑能量耗散和非弹性效应，该模块使用 **接触阻尼** 参数。

基本硬停止模型 `Full stiffness and damping applied at bounds, damped rebound` 使用以下方程：

f={−K⋅length−D⋅vfor length≤00for length>0

v=vF−vB

其中：

- *f* 是两侧之间的相互作用力。
- *K* 是接触刚度。
- *D* 是阻尼系数。
- *v* 是相对速度。
- *v*F 和 *v*B 分别是端口 **B** 和 **F** 的绝对速度。

在 `Full stiffness and damping applied at bounds, undamped rebound` 硬停止模型中，方程包含一个附加项 `ge`(*v*,0)。该项确保模块在反弹时不施加阻尼。

f={−K⋅length−D⋅v⋅ge(v,0)for length≤00for length>0

关系函数 `ge`（大于或等于）在速度改变符号时不生成零穿越。有关详细信息，请参阅 Enabling and Disabling Zero-Crossing Conditions in Simscape Language。但是，求解器将 `ge` 函数视为非线性。因此，如果 `simscape.findNonlinearBlocks` 指示您的网络其余部分是线性或切换线性的，请使用 `Full stiffness and damping applied at bounds, damped rebound` 模型以提高性能。

默认硬停止模型 `Stiffness and damping applied smoothly through transition region, damped rebound` 在方程中添加了一个过渡区域。在过渡区域中，模块将力从零平滑增加到完整值。在过渡区域末端，模块施加完整刚度和阻尼。在反弹时，模块将刚度和阻尼力都平滑减小到零。这些方程也使用 `ge` 关系函数，它不产生零穿越。

### 基于恢复系数的模型

与基于刚度和阻尼的模型不同，此模型不允许硬停止两侧穿透。硬停止行为由具有两个常规模式和两个瞬时模式的模式图表示：

- `FREE` — 硬停止两侧之间没有力传递。在此模式下，*f* = 0，*length* >= 0。
- `CONTACT` — 间隙闭合。在此模式下，*v* = 0，*length* < 0。
- `RELEASE` — 从 `CONTACT` 过渡到 `FREE` 所需的瞬时模式。
- `IMPACT` — 当硬停止两侧弹跳时使用的瞬时模式。

当硬停止两侧缓慢相互碰撞，且相对速度小于静态接触速度阈值时，两侧保持接触。否则，两侧弹跳。当两侧弹跳时，由于恢复系数，它们会损失速度。在接触模式下，相对速度为 0。要从接触模式过渡到自由模式，必须向硬停止施加大于静态接触释放力阈值的拉力，并且过渡必须经过瞬时释放模式以设置初始速度。

此建模选项提高了仿真性能，因为在接触模式下，静态接触模式不要求模块持续计算硬停止力。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 节。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 节。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
