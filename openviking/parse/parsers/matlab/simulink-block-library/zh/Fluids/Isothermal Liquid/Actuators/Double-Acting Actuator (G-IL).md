---
type: simulink-block
title: 'Double-Acting Actuator (G-IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'doubleactingactuatorgil'
documentation_source_path: 'ref/doubleactingactuatorgil.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (G-IL)

## 端口

### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置关联的物理信号端口。
### 守恒

### **A** — 腔室 A 的入口，等温液体

与腔室 A 入口关联的等温液体守恒端口。

### **B** — 腔室 B 的入口，气体

与腔室 B 入口关联的气体守恒端口。

### **C** — 执行器壳体，机械平移

与壳体关联的机械平移守恒端口。

### **R** — 执行器活塞杆，机械平移

与活塞杆关联的机械平移守恒端口。

### **H** — 热流，热

与气体腔室的热传递关联的热守恒端口。

## 参数

### 配置

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。`Pressure at A causes positive displacement of R relative to C` 对应于当腔室 A 和 B 之间的压差为正时活塞伸出。`Pressure at A causes negative displacement of R relative to C` 对应于当腔室 A 和 B 之间的压差为正时活塞缩回。

### **Piston stroke** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **Initial piston displacement from chamber A cap** — 仿真开始时的活塞位置 `0 m`（默认）| 标量

仿真开始时的活塞位置。

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时力的模型选择。有关更多信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。在活塞最大伸出和活塞最大缩回的这一范围之外，**Hard stop model** 不适用，活塞上没有额外的力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 等温液体侧

### **Piston cross-sectional area in chamber A** — 活塞杆的横截面积 `0.01 m^2`（默认）| 正标量

腔室 A 中活塞杆的横截面积。

### **Dead volume in chamber A** — 活塞完全缩回时的腔室体积 `1e-5 m^3`（默认）| 正标量

活塞完全缩回时流体腔室中的开放体积。

### **Enable dynamic compressibility** — 是否对流体可压缩性进行建模 `On`（默认）| `Off`

是否对由流体可压缩性引起的任何流体密度变化进行建模。当 **Fluid compressibility** 设置为 `On` 时，除了由压力变化引起的密度变化外，还会计算由进入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **Initial liquid pressure in chamber A** — 可压缩流体的初始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的初始液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Nominal liquid pressure in chamber A** — 腔室 A 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 A 中额定工况下的液体压力。当动态可压缩性被禁用时，模块使用此值来计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric pressure` 选项将环境压力设置为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

### 气体侧

### **Piston cross-sectional area in chamber B** — 活塞杆的横截面积 `0.01 m^2`（默认）| 正标量

腔室 B 中活塞杆的横截面积。

### **Cross-sectional area at port B** — 端口横截面积 `1e-3 m^2`（默认）| 正标量

端口 **B** 处的横截面积。

### **Dead volume in chamber B** — 活塞完全缩回时的腔室体积 `1e-5 m^3`（默认）| 正标量

活塞完全缩回时气体腔室中的开放体积。

### **Initial gas pressure in chamber B** — 气体腔室起始压力 `0.101325 MPa`（默认）| 正标量

气体腔室中的初始压力。

### **Initial gas temperature in chamber B** — 气体腔室起始温度 `293.15 K`（默认）| 正标量

气体腔室中的初始温度。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric pressure` 选项将环境压力设置为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。此选项称为 `Based on coefficient of restitution`，通过使用模式图对硬限位进行建模。

## 描述

具有等温液体腔室和气体腔室的线性执行器

Double-Acting Actuator (G-IL) 模块表示由活塞板隔开的等温液体腔室和气体腔室。活塞的驱动由腔室之间的压差控制。活塞在接近完全伸出或完全缩回时的运动受到四种硬限位模型之一的限制。

端口 **A** 是等温液体入口，端口 **B** 是气体入口。将气体腔室与环境之间的热传递元件连接到端口 **H**。端口 **C** 用作执行器壳体的机械平移参考。端口 **R** 与执行器活塞关联。活塞位置在端口 **P** 处报告。

### 位移

活塞位移以端口 **R** 相对于端口 **C** 的位置来测量。**Mechanical orientation** 标识活塞位移的方向。当腔室体积等于腔室死区体积时，活塞位移为中性，即 `0`。当位移作为输入接收时，确保位置的导数等于活塞速度。当输入来自 Translational Multibody Interface 模块与 Simscape™ Multibody™ 关节的连接时，情况自动如此。

### 硬限位模型

为避免活塞在完全伸出或完全缩回时发生机械损坏，执行器通常在活塞接近这些限位时表现出非线性行为。Double-Acting Actuator (G-IL) 模块通过四种硬限位模型的选择来对此行为进行建模，这些模型通过弹簧-阻尼器系统对材料柔度进行建模。硬限位模型包括：

- `Stiffness and damping applied smoothly through transition region, damped rebound`。
- `Full stiffness and damping applied at bounds, undamped rebound`。
- `Full stiffness and damping applied at bounds, damped rebound`。
- `Based on coefficient of restitution`

硬限位力在活塞处于其上限或下限时进行建模。边界区域位于 **Piston stroke** 或活塞初始位移的 **Transition region** 内。在此区域之外，FHardStop=0。

有关这些设置的更多信息，请参阅 Translational Hard Stop 模块页面。

### 模块原理图

Double-Acting Actuator (G-IL) 模块是四个 Simscape Foundation 模块的复合：

- Translational Mechanical Converter (G)
- Translational Mechanical Converter (IL)
- Translational Hard Stop
- Ideal Translational Motion Sensor
