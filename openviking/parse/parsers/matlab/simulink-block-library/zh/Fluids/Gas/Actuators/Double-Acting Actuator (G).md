---
type: simulink-block
title: 'Double-Acting Actuator (G)'
family: 'gas'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Actuators'
documentation_page: 'doubleactingactuatorg'
documentation_source_path: 'ref/doubleactingactuatorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (G)

## 端口

### 输入

### **p** — 活塞位置输入，m physical signal

与活塞位置相关联的物理信号输入，单位为 m。
将此端口连接到 Simscape Multibody™ 网络，使用 Translational Multibody Interface 模块。

#### 依赖关系

要启用此端口，请将 **Piston displacement from chamber A cap** 设置为 `Provide input signal from Multibody joint`。

### 输出

### **p** — 活塞位置，m physical signal

与活塞位置相关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Piston displacement from chamber A cap** 设置为 `Calculate from velocity of port R relative to port C`。

### 守恒端口

### **A** — Liquid port gas

与腔 A 入口相关联的气体守恒端口。

### **B** — Liquid port gas

与腔 B 入口相关联的气体守恒端口。

### **R** — 执行器活塞机械平移

与执行器活塞相关联的机械平移守恒端口。

### **C** — 执行器壳体机械平移

与执行器壳体相关联的机械平移守恒端口。

### **HA** — 传热热

与腔 A 相关联的热守恒端口。

### **HB** — 传热热

与腔 B 相关联的热守恒端口。

## 参数

### 执行器

### **Same fluid on both sides** — 用于对两个腔室中的相同流体建模的选项 `on`（默认） | `off`

是否对两个执行器腔室中的相同流体进行建模。如果选择此参数，执行器将通过两个腔室传播流体属性。清除此参数以将每个腔室建模为不同流体，其中每个腔室连接到隔离的流体网络。

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认） | `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of R relative to C`，当端口 **A** 处的气体体积膨胀时，活塞位移为正。此运动对应于杆伸出。
- `Pressure at A causes negative displacement of R relative to C`，当端口 **A** 处的气体体积膨胀时，活塞位移为负。此运动对应于杆缩回。

### **Piston cross-sectional area in chamber A** — 腔 A 活塞面积 `0.01 m^2`（默认） | positive scalar

腔 A 侧活塞杆的横截面积。

### **Piston cross-sectional area in chamber B** — 腔 B 活塞面积 `0.01 m^2`（默认） | positive scalar

腔 B 侧活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1 m`（默认） | positive scalar

最大活塞行程距离。

### **Dead volume in chamber A** — 活塞完全缩回时腔 A 的流体体积 `1e-5 m^3`（默认） | positive scalar

腔 A 中活塞位移为 `0` 时的气体体积。此参数是活塞抵靠执行器端盖时的气体体积。

### **Dead volume in chamber B** — 活塞完全缩回时腔 B 的流体体积 `1e-5 m^3`（默认） | positive scalar

腔 B 中活塞位移为 `0` 时的气体体积。此参数是活塞抵靠执行器端盖时的气体体积。

### **Cross-sectional area at port A** — 端口 A 的面积 `0.01 m^2`（默认） | positive scalar

端口 **A** 的横截面积。

### **Cross-sectional area at port B** — 端口 B 的面积 `0.01 m^2`（默认） | positive scalar

端口 **B** 的横截面积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认） | `Specified pressure`

环境参考压力。当您选择 `Atmospheric pressure` 时，模块假定压力为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认） | positive scalar

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

### 硬限位

### **Hard stop model** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认） | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全缩回时使用的硬限位模型。有关详细信息，请参见 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认） | positive scalar

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认） | positive scalar

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认） | positive scalar

硬限位力模型的应用范围。当活塞的最大伸出或缩回超出此范围时，模块不应用硬限位模型。在这种情况下，活塞上没有附加力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认） | unitless value between 0 and 1

滑块弹回后，滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认） | nonnegative scalar

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞到壳体时，它们保持接触。否则，滑块弹回。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的力 `0.001 N`（默认） | positive scalar

使滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 初始条件

### **Piston displacement from chamber A cap** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认） | `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，模块可以从 Multibody 模块接收位置；或者可以在内部计算位置并在端口 **p** 报告位置。当机械方向为正时，位置在 `0` 与 **Piston stroke** 参数的值之间；当机械方向为负时，位置在 `0` 与 **Piston stroke** 参数的负值之间。

### **Initial piston displacement from chamber A cap** — 仿真开始时的活塞位移 `0` `m`（默认） | scalar

仿真开始时相对于腔 A 端盖的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston displacement** 设置为 `Calculate from velocity of port R relative to port C`。

### **Initial gas pressure in chamber A** — 腔 A 中的起始气体压力 `0.101325` `MPa`（默认） | positive scalar

腔 A 中的起始气体压力。

### **Initial gas pressure in chamber B** — 腔 B 中的起始气体压力 `0.101325` `MPa`（默认） | positive scalar

腔 B 中的起始气体压力。

### **Initial gas temperature in chamber A** — 腔 A 中的起始气体温度 `293.15` `K`（默认） | scalar

执行器中气体体积的初始温度。

### **Initial gas temperature in chamber B** — 腔 B 中的起始气体温度 `293.15` `K`（默认） | scalar

执行器中气体体积的初始温度。

## 所属库

Simscape / Fluids / Gas / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2024a：对执行器每一侧的不同流体进行建模

清除新的 **Same fluid on both sides** 参数，以阻止流体属性传播，并将每个腔室建模为连接到其自身隔离流体网络的不同流体。

## 描述

气体网络中的双作用线性执行器

Double-Acting Actuator (G) 模块对由两个相对气体腔控制的活塞线性执行器进行建模。该执行器在伸出和缩回行程中产生力。产生的力取决于两个腔之间的压差。

图显示了执行器的关键组件。端口 **A** 和 **B** 表示气体腔入口。端口 **R** 表示平动执行器活塞，端口 **C** 表示执行器壳体。端口 **HA** 和 **HB** 表示每个气体腔与环境之间的热接口。移动活塞是绝热的。

双作用执行器示意图

### 位移

该模块将活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**Mechanical orientation** 参数标识活塞位移的方向。当腔 A 体积等于 **Dead volume in chamber A** 参数的值时，活塞位移为中性，即 `0`。当 **Piston displacement from chamber A cap** 参数为 `Provide input signal from Multibody joint` 时，您使用端口 **p** 输入活塞位移。确保位置信号的导数等于活塞速度。您可以通过使用 Translational Multibody Interface 模块提供活塞位移，来确保位置信号的导数等于活塞速度。

活塞运动方向取决于 **Mechanical orientation** 参数。如果机械方向为正，则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平移为正。当机械方向为负时，运动方向相反。

### 硬限位

一组硬限位限制活塞运动范围。该模块使用 Translational Hard Stop 模块的实现，该实现将硬限位视为弹簧-阻尼系统。弹簧刚度系数控制硬限位接触力的恢复分量，阻尼系数控制耗散分量。

硬限位位于活塞行程的远端。如果机械方向为正，则下限位在 *x* = 0，上限位在 *x* = +*stroke*。如果机械方向为负，则下限位在 *x* = -*stroke*，上限位在 *x* = 0。

### 模块组合

该模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter (G)
- Translational Hard Stop
- Ideal Translational Motion Sensor

构成该模块的元素的示意图。
