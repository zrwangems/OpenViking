---
type: simulink-block
title: 'Single-Acting Actuator (TL)'
family: 'thermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Actuators'
documentation_page: 'singleactingactuatortl'
documentation_source_path: 'ref/singleactingactuatortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Single-Acting Actuator (TL)

## 端口

### 输入

### **p** — 多体活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入，单位为 m。将此端口连接到 Simscape Multibody™ 网络，使用 Translational Multibody Interface 模块。

#### 依赖关系

要启用此端口，请将 **活塞位移** 设置为 `Provide input signal from Multibody joint`。

### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置关联的物理信号输出，单位为 m。

#### 依赖关系

要启用此端口，请将 **活塞位移** 设置为 `Calculate from velocity of port R relative to port C`。

### 守恒

### **A** — 液体端口 热液体

与腔室 A 关联的热液体守恒端口。

### **C** — 执行器壳体 平移机械

与执行器壳体关联的平移机械守恒端口。

### **R** — 执行器活塞 平移机械

与执行器活塞关联的平移机械守恒端口。

### **H** — 热传递 热

与液体体积的热质量关联的热守恒端口。

## 参数

### 执行器

### **机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C` (默认) | `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。将此参数设置为：

- `Pressure at A causes positive displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为正。此运动对应于杆伸出。
- `Pressure at A causes negative displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为负。此运动对应于杆缩回。

### **活塞横截面积** — 活塞杆横截面积 `0.01` `m^2` (默认) | 正标量

活塞杆的横截面积。

### **活塞行程** — 最大活塞行程距离 `0.1` `m` (默认) | 正标量

最大活塞行程距离。

### **死区容积** — 活塞完全缩回时的流体体积 `1e-5` `m^3` (默认) | 正标量

活塞位移为 `0` 时的液体体积。此参数是活塞抵靠执行器端盖时的液体体积。

### **环境压力规格** — 参考环境压力 `Atmospheric pressure` (默认) | `Specified pressure`

环境参考压力。当选择 `Atmospheric pressure` 时，模块假定压力为 0.101325 MPa。

### **环境压力** — 用户定义的环境压力 `0.101325` `MPa` (默认) | 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **环境压力规格** 设置为 `Specified pressure`。

### 硬限位

### **硬限位模型** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound` (默认) | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全缩回时使用的硬限位模型。有关详细信息，请参阅 Translational Hard Stop 模块。

### **硬限位刚度系数** — 刚度系数 `1e10` `N/m` (默认) | 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **硬限位阻尼系数** — 阻尼系数 `150` `N*s/m` (默认) | 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **过渡区域** — 硬限位力模型的应用范围 `0.1` `mm` (默认) | 正标量

硬限位力模型的应用范围。当活塞的最大伸出或缩回超出此范围时，模块不应用硬限位模型。在这种情况下，活塞上没有附加力。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7` (默认) | 0 到 1 之间的无单位值

滑块弹跳后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位之间的相对速度阈值 `0.001 m/s` (默认) | 非负标量

碰撞前滑块与限位之间的相对速度阈值。当滑块以小于 **静态接触速度阈值** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的力 `0.001 N` (默认) | 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### 缓冲

### **缸端缓冲** — 是否对最大伸出时的活塞减速建模 `off` (默认) | `on`

是否对最大伸出时的活塞减速建模。有关详细信息，请参阅 Cylinder Cushion (TL) 模块。

### **缓冲柱塞横截面积** — 缸缓冲柱塞面积 `1e-4` `m^2` (默认) | 正标量

执行器缓冲元件内柱塞的面积。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **缓冲柱塞长度** — 缓冲柱塞长度 `1e-3` `m` (默认) | 正标量

缓冲柱塞的长度。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **缓冲孔口面积** — 缓冲腔之间的孔口面积 `1e-6` `m^2` (默认) | 正标量

缓冲腔之间孔口的面积。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **柱塞与缓冲套筒之间的泄漏面积** — 缓冲柱塞与套筒之间的间隙 `1e-7` `m^2` (默认) | 正标量

缓冲柱塞与套筒之间的间隙面积。此值通过保持流动连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **单向阀开启压力差** — 缓冲阈值压力 `0.01` `MPa` (默认) | 正标量

触发阀操作的压力。当端口 **A** 与 *P*env 之间的压力差达到或超过此参数值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **单向阀最大压力差** — 缓冲最大压差 `0.1` `MPa` (默认) | 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持真实。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **单向阀最大面积** — 完全打开的缓冲阀面积 `1e-4` `m^2` (默认) | 正标量

缓冲阀在完全打开位置的横截面积。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **单向阀泄漏面积** — 完全关闭位置的缓冲阀间隙面积 `1e-10` `m^2` (默认) | 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### **平滑因子** — 数值平滑因子 `0.01` (默认) | 正标量

连续平滑因子，当可变孔口和单向阀处于接近打开或接近关闭位置时，为流动响应引入一层逐渐变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请选择 **缸端缓冲**。

### 摩擦

### **缸摩擦** — 是否对活塞运动摩擦建模 `off` (默认) | `on`

是否对活塞运动摩擦建模。模块考虑库仑摩擦、Stribeck 摩擦和粘性摩擦。有关详细信息，请参阅 Cylinder Friction (TL) 模块。

### **分离力与库仑摩擦力之比** — 分离力与库仑摩擦力之比 `1.2` (默认) | 正标量

分离力与库仑摩擦力之比。

#### 依赖关系

要启用此参数，请选择 **缸摩擦**。

### **分离摩擦速度** — 运动阈值 `0.1` `m/s` (默认) | 正标量

开始克服摩擦力运动的速度阈值。

#### 依赖关系

要启用此参数，请选择 **缸摩擦**。

### **预紧力** — 密封组件在缸中产生的初始力 `20` `N` (默认) | 标量

密封组件在缸中产生的初始力。

#### 依赖关系

要启用此参数，请选择 **缸摩擦**。

### **库仑摩擦力系数** — 库仑摩擦力系数 `1e-6` `N/Pa` (默认) | 正标量

库仑摩擦力系数。

#### 依赖关系

要启用此参数，请选择 **缸摩擦**。

### **粘性摩擦系数** — 粘性摩擦系数 `100` `N*s/m` (默认) | 正标量

粘性摩擦系数。

#### 依赖关系

要启用此参数，请选择 **缸摩擦**。

### 初始条件

### **活塞位移** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C` (默认) | `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，模块可以从 Multibody 模块接收位置；或者可以在内部计算位置并在端口 **p** 报告位置。当机械方向为正时，位置介于 `0` 和 **活塞行程** 参数值之间；当机械方向为负时，位置介于 `0` 和 **活塞行程** 参数值的负值之间。

### **初始活塞位移** — 仿真开始时的活塞位置 `0` `m` (默认) | 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **活塞位移** 设置为 `Calculate from velocity of port R relative to port C`。

### **启用动态可压缩性** — 是否对流体可压缩性建模 `on` (默认) | `off`

是否对流体可压缩性引起的任何流体密度变化建模。当选择 **流体可压缩性** 时，除了压力变化引起的密度变化外，还会计算流入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **初始液体温度** — 起始液体温度 `293.15` `K` (默认) | 标量

执行器中液体体积的初始温度。

### **初始液体压力** — 可压缩流体的起始液体压力 `0.101325` `MPa` (默认) | 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

### **标称液体温度** — 标称工况下的温度 `293.15 K` (默认) | 标量

标称工况下的液体温度。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **标称液体压力** — 标称工况下的压力 `0.101325 MPa` (默认) | 标量

标称工况下的液体压力。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

## 所属库

Simscape / Fluids / Thermal Liquid / Actuators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：对缸摩擦或缓冲建模

模块新增了用于对缸摩擦或缓冲建模的选项。选择 **缸摩擦** 参数以包含摩擦对活塞运动的影响。选择 **缸端缓冲** 参数以对最大伸出时的活塞减速建模。

### R2023a：新的硬限位参数化选项

模块为 **硬限位模型** 参数新增了一个选项。此选项称为 `Based on coefficient of restitution`，使用模式图对硬限位进行建模。

## 描述

热液体网络中的单作用线性执行器

Single-Acting Actuator (TL) 模块对由单个热液体腔室控制的活塞线性执行器建模。执行器在伸出和缩回行程中产生力，但致动力取决于单个腔室处的表压。

图中显示了执行器的关键组件。端口 **A** 表示热液体腔室入口。端口 **R** 表示平移执行器活塞，端口 **C** 表示执行器壳体。端口 **H** 表示热液体腔室与环境之间的热接口。

单作用执行器示意图

### 位移

模块将活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**机械方向** 参数标识活塞位移的方向。当腔室体积等于 **死区容积** 参数值时，活塞位移为中性，即 `0`。当 **活塞位移** 参数为 `Provide input signal from Multibody joint` 时，使用端口 **p** 输入活塞位移。您可以使用 Translational Multibody Interface 模块提供活塞位移，以确保位置信号的导数等于活塞速度。

活塞运动的方向取决于 **机械方向** 参数。如果机械方向为正，则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平移为正。当机械方向为负时，运动方向相反。

### 硬限位

一组硬限位限制活塞的运动范围。该模块使用 Translational Hard Stop 模块的一种实现，它将硬限位视为弹簧-阻尼系统。弹簧刚度系数控制硬限位接触力的恢复分量，阻尼系数控制耗散分量。

硬限位位于活塞行程的两端。如果机械方向为正，则下硬限位位于 *x* = 0，上硬限位位于 *x* = +*stroke*。如果机械方向为负，则下硬限位位于 *x* = -*stroke*，上硬限位位于 *x* = 0。

### 缓冲

该模块可以对活塞行程两端附近的缓冲进行建模。选择 **气缸末端缓冲** 以在活塞接近由 **活塞行程** 参数定义的最大伸出时减缓活塞运动。有关气缸缓冲功能的详细信息，请参阅 Cylinder Cushion (TL) 模块。

### 摩擦

该模块可以对阻碍活塞运动的摩擦进行建模。当选择 **气缸摩擦** 时，产生的摩擦是 Stribeck、Coulomb 和黏性效应的组合。该模块测量腔室压力与环境压力之间的压差。有关摩擦模型及其限制的详细信息，请参阅 Cylinder Friction (TL) 模块。

### 复合模块

该模块是一个基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter
  (TL)
- Translational Hard Stop
- Ideal Translational Motion Sensor

构成该模块的元素的示意图。

如果选择 **气缸摩擦** 或 **气缸末端缓冲**，复合模块还会包括 Cylinder Friction (TL) 模块或 Cylinder Cushion (TL) 模块。

包含摩擦和缓冲时构成该模块的元素的示意图。
