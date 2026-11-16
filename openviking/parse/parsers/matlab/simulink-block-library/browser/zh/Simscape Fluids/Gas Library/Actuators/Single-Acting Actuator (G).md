---
type: simulink-block
title: 'Single-Acting Actuator (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Gas Library / Actuators'
documentation_page: 'singleactingactuatorg'
documentation_source_path: 'ref/singleactingactuatorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Single-Acting Actuator (G)

## 端口

### 输入

### **p** — Multibody 活塞位置输入，m 物理信号

与活塞位置相关联的物理信号输入，单位为 m。
使用 Translational Multibody Interface 模块将此端口连接到 Simscape
Multibody™ 网络。

#### 依赖关系

要启用此端口，请将 **Piston displacement**
设置为 `Provide input signal from Multibody
joint`。

### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置相关联的物理信号输出，单位为
m。

#### 依赖关系

要启用此端口，请将 **Piston displacement**
设置为 `Calculate from velocity of port R relative to port
C`。

### 守恒

### **A** — 液体端口 gas

与气室 A 相关联的气体守恒端口。

### **C** — 执行器壳体平动机械

与执行器壳体相关联的平动机械守恒端口。

### **R** — 执行器活塞平动机械

与执行器活塞相关联的平动机械守恒端口。

### **H** — 热传递 thermal

与气体体积的热质量相关联的热守恒端口。

## 参数

### 执行器

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C` 时，当端口
  **A** 处的气体体积正在膨胀时，活塞位移
  为正。此运动对应于杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C` 时，当端口
  **A** 处的气体体积正在膨胀时，活塞位移
  为负。此运动对应于杆缩回。

### **Piston cross-sectional area** — 活塞杆横截面积 `0.01` `m^2`（默认）| 正标量

活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程 `0.1` `m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume** — 活塞完全缩回时的流体体积 `1e-5` `m^3`（默认）| 正标量

当活塞位移为 `0` 时的气体体积。此参数是活塞抵靠执行器端盖时的气体体积。

### **Cross-sectional area at port A** — 端口 A 处的面积 `0.01 m^2`（默认）| 正标量

端口 **A** 的横截面积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。选择
`Atmospheric pressure` 时，模块假定压力为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325` `MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure
specification** 设置为 `Specified
pressure`。

### 硬停止

### **Hard stop model** — 硬停止模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全抽出时使用的硬停止模型。有关详细信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — 硬停止力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬停止力模型的应用范围。当活塞的最大伸出或缩回超过此范围时，模块不应用硬停止模型。在这种情况下，活塞上没有附加力。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位件之间最终相对速度与初始相对速度之比 `0.7`（默认）| 介于 0 和 1 之间的无单位值

滑块反弹后，滑块与限位件之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位件之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位件之间的阈值相对速度。当滑块以小于 **Static
contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。
否则，滑块反弹。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为
`0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式转换到自由模式所需的力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### 初始条件

### **Piston displacement** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input
signal from Multibody joint` 时，模块可以从 Multibody 模块接收位置，或者可以在内部计算位置并在端口
**p** 报告该位置。当机械方向为正时，位置介于 `0`
与 **Piston stroke** 参数的值之间；当机械方向为负时，位置介于 `0`
与 **Piston stroke** 参数的负值之间。

### **Initial piston displacement** — 仿真开始时的活塞位置 `0` `m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston
displacement** 设置为 `Calculate from velocity
of port R relative to port C`。

### **Initial gas pressure** — 起始气体压力 `0.101325` `MPa`（默认）| 正标量

执行器中气体体积的初始压力。

### **Initial gas temperature** — 起始气体温度 `293.15` `K`（默认）| 标量

执行器中气体体积的初始温度。

## 所属库

Simscape / Fluids / Gas / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

气体网络中的单作用线性执行器

Single-Acting Actuator (G) 模块对由单个气室控制的活塞线性执行器进行建模。该执行器在伸出和缩回行程中产生力，但作用力取决于单个气室处的表压。

该图显示了执行器的关键组件。端口 **A**
表示气室入口。端口 **R** 表示平动执行器活塞，端口 **C** 表示执行器
壳体。端口 **H** 表示气室与环境之间的热接口。

单作用执行器示意图

### 位移

模块测量活塞位移为端口 **R**
相对于端口 **C** 的位置。**Mechanical
orientation** 参数标识活塞位移方向。当气室体积等于 **Dead volume**
参数的值时，活塞位移为中性，即 `0`。当 **Piston displacement** 参数为
`Provide input signal from Multibody joint` 时，您使用端口 **p** 输入
活塞位移。通过使用 Translational Multibody Interface 模块提供活塞位移，可以确保位置信号的
导数等于活塞速度。

活塞运动方向取决于 **Mechanical
orientation** 参数。如果机械方向为正，
则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平动为正。当机械方向为负时，运动方向
反转。

### 硬停止

一组硬停止限制活塞的运动范围。模块使用
Translational Hard Stop 模块的实现，将硬停止视为
弹簧-阻尼系统。弹簧刚度系数控制硬停止接触力的恢复
分量，阻尼系数控制耗散分量。

硬停止位于活塞行程的远端。如果
机械方向为正，则下限位硬停止位于 *x* = 0，上限位硬停止位于 *x* = +*stroke*。如果机械方向为负，则下限位硬停止位于
*x* = -*stroke*，上限位硬停止位于 *x* = 0。

### 模块组成

此模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical
  Converter (G)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor

组成该模块的元素的示意图。
