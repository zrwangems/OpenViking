---
type: simulink-block
title: 'Double-Acting Actuator (G-IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Actuators'
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

与腔室 A 的入口关联的等温液体守恒端口。

### **B** — 腔室 B 的入口，气体

与腔室 B 的入口关联的气体守恒端口。

### **C** — 执行器壳体，机械平移

与壳体关联的机械平移守恒端口。

### **R** — 执行器活塞杆，机械平移

与活塞杆关联的机械平移守恒端口。

### **H** — 热流，热

与向气体腔室传入或从气体腔室传出热量关联的热守恒端口。

## 参数

### 配置

### **机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。当腔室 A 与 B 之间的压差为正时，`Pressure at A causes positive displacement
of R relative to C` 对应于活塞伸出。当腔室 A 与 B 之间的压差为正时，`Pressure at A causes negative displacement of R
relative to C` 对应于活塞回缩。

### **活塞行程** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **活塞从腔室 A 端盖的初始位移** — 仿真开始时的活塞位置 `0 m`（默认）| 标量

仿真开始时的活塞位置。

### **硬止动模型** — 选择硬止动模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞完全伸出或完全回缩时作用在活塞上的力的模型选择。有关详细信息，请参阅 Translational Hard Stop 模块。

### **硬止动刚度系数** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **硬止动模型** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **硬止动阻尼系数** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **硬止动模型** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **过渡区域** — 硬止动力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬止动力模型的应用范围。在活塞最大伸出量和活塞最大回缩量的此范围之外，不应用 **硬止动模型**，并且活塞上没有附加力。

#### 依赖关系

要启用此参数，请将 **硬止动模型** 设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与止挡之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹回后滑块与止挡之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **硬止动模型** 设置为 `Based on coefficient of
restitution`。

### **静态接触速度阈值** — 碰撞前滑块与止挡之间的相对速度阈值 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与止挡之间的相对速度阈值。当滑块以小于 **静态接触速度阈值** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹回。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **硬止动模型** 设置为 `Based on coefficient of
restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **硬止动模型** 设置为 `Based on coefficient of
restitution`。

### 等温液体侧

### **腔室 A 中活塞横截面积** — 活塞杆横截面积 `0.01 m^2`（默认）| 正标量

腔室 A 中活塞杆的横截面积。

### **腔室 A 中的死区容积** — 活塞完全回缩时的腔室容积 `1e-5 m^3`（默认）| 正标量

活塞完全回缩时流体腔室中的开放容积。

### **启用动态可压缩性** — 是否对流体可压缩性建模 `On`（默认）| `Off`

是否对由流体可压缩性引起的任何流体密度变化建模。当 **流体可压缩性** 设置为 `On` 时，除了压力变化引起的密度变化外，还会计算由于流入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **腔室 A 中的初始液体压力** — 可压缩流体的初始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的初始液体压力。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**。

### **腔室 A 中的标称液体压力** — 腔室 A 中标称工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 A 中标称工况下的液体压力。当动态可压缩性禁用时，模块使用此值计算质量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **环境压力设定** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric
pressure` 选项将环境压力设置为 0.101325 MPa。

### **环境压力** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **环境压力设定** 设置为 `Specified
pressure`。

### 气体侧

### **腔室 B 中活塞横截面积** — 活塞杆横截面积 `0.01 m^2`（默认）| 正标量

腔室 B 中活塞杆的横截面积。

### **端口 B 处横截面积** — 端口横截面积 `1e-3 m^2`（默认）| 正标量

端口 **B** 处的横截面积。

### **腔室 B 中的死区容积** — 活塞完全回缩时的腔室容积 `1e-5 m^3`（默认）| 正标量

活塞完全回缩时气体腔室中的开放容积。

### **腔室 B 中的初始气体压力** — 起始气体腔室压力 `0.101325 MPa`（默认）| 正标量

气体腔室中的初始压力。

### **腔室 B 中的初始气体温度** — 起始气体腔室温度 `293.15 K`（默认）| 正标量

气体腔室中的初始温度。

### **环境压力设定** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric
pressure` 选项将环境压力设置为 0.101325 MPa。

### **环境压力** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **环境压力设定** 设置为 `Specified
pressure`。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a: 新的硬止动参数化选项

该模块为 **硬止动模型** 参数提供了一个新选项。此选项名为 `Based on coefficient of restitution`，使用模式图对硬止动进行建模。

## 描述

具有等温液体腔室和气体腔室的线性执行器

Double-Acting Actuator (G-IL) 模块表示由活塞板隔开的等温液体腔室和气体腔室。活塞驱动由腔室之间的压差控制。当活塞接近完全伸出或完全回缩时，其运动受四种硬止动模型之一限制。

端口 **A** 是等温液体入口，端口 **B** 是气体入口。将用于气体腔室与环境之间热传递的元件连接到端口 **H**。端口 **C** 用作执行器壳体的机械平移参考。端口 **R** 与执行器活塞关联。活塞位置在端口 **P** 处报告。

### 位移

活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**机械方向** 标识活塞位移的方向。当腔室容积等于腔室死区容积时，活塞位移为中性，即 `0`。当位移作为输入接收时，请确保位置的导数等于活塞速度。当输入从与 Simscape™
Multibody™ 关节连接的 Translational Multibody Interface 模块连接接收时，会自动如此。

### 硬止动模型

为避免活塞在完全伸出或完全回缩时发生机械损坏，执行器通常会在活塞接近这些限位时表现出非线性行为。Double-Acting Actuator (G-IL) 模块通过四种硬止动模型的选择来对此行为建模，这些模型通过弹簧-阻尼器系统对材料柔度进行建模。硬止动模型包括：

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`.
- `Full stiffness and damping applied at bounds, undamped
  rebound`.
- `Full stiffness and damping applied at bounds, damped
  rebound`.
- `Based on coefficient of restitution`

当活塞位于其上限或下限时，对硬止动力进行建模。边界区域位于 **活塞行程** 或活塞初始位移的 **过渡区域** 内。在此区域之外，FHardStop=0。

有关这些设置的详细信息，请参阅 Translational Hard Stop 模块页面。

### 模块原理图

Double-Acting Actuator (G-IL) 模块是四个 Simscape Foundation 模块的复合模块：

- Translational Mechanical
  Converter (G)
- Translational Mechanical Converter (IL)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor
