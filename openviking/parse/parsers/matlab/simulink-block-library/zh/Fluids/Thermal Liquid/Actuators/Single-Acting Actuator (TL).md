---
type: simulink-block
title: 'Single-Acting Actuator (TL)'
family: 'hydro'
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

与活塞位置相关联的物理信号输入，单位为 m。将此端口连接至
Simscape
Multibody™ 网络，使用 Translational Multibody
Interface 模块。

#### 依赖关系

要启用此端口，请将 **Piston displacement** 设置为
`Provide input signal from Multibody joint`。
### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置相关联的物理信号输出，单位为 m。

#### 依赖关系

要启用此端口，请将 **Piston displacement** 设置为
`根据端口 R 相对于端口的速度计算
C`。
### 守恒端口

### **A** — 液体端口 热液体

与腔室 A 相关联的热液体守恒端口。

### **C** — 执行器壳体 平移机械

与执行器壳体相关联的平移机械守恒端口。

### **R** — 执行器活塞 平移机械

与执行器活塞相关联的平移机械守恒端口。

### **H** — 热传递 热

与液体体积的热质量相关联的热守恒端口。

## 参数

### 执行器

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of R relative to
  C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为正。此运动对应于活塞杆伸出。
- `Pressure at A causes negative displacement of R relative to
  C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为负。此运动对应于活塞杆缩回。

### **Piston cross-sectional area** — 活塞杆横截面积 `0.01` `m^2`（默认）| 正标量

活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1` `m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume** — 活塞完全缩回时的流体体积 `1e-5` `m^3`（默认）| 正标量

活塞位移为 `0` 时的液体体积。此参数为活塞抵靠执行器端盖时的液体体积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。当您选择 `Atmospheric
pressure` 时，模块假定压力为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325` `MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure
specification** 设置为 `Specified pressure`。

### 硬限位

### **Hard stop model** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全缩回时使用的硬限位模型。
有关详细信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped
  rebound`
- `Full stiffness and damping applied at bounds, damped
  rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped
  rebound`
- `Full stiffness and damping applied at bounds, damped
  rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。当活塞的最大伸出或缩回超出此范围时，模块不应用硬限位模型。在这种情况下，活塞上不会产生额外的力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Stiffness and damping applied smoothly through transition region,
damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位器之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与限位器之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位器之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位器之间的阈值相对速度。当滑块以小于 **Static contact
speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为
`Based on coefficient of restitution`。

### 缓冲

### **Cylinder end cushioning** — 是否对活塞在最大伸出时进行减速建模 `off`（默认）| `on`

是否对活塞在最大伸出时进行减速建模。有关详细信息，请参阅 Cylinder Cushion
(TL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4` `m^2`（默认）| 正标量

执行器缓冲元件内部柱塞的面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3` `m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Cushion orifice area** — 缓冲腔之间的节流孔面积 `1e-6` `m^2`（默认）| 正标量

缓冲腔之间节流孔的面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与套筒之间的间隙 `1e-7` `m^2`（默认）| 正标量

缓冲柱塞与套筒之间的间隙面积。此值通过保持流动的连续性来有助于数值稳定性。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01` `MPa`（默认）| 正标量

触发阀门操作的压力阈值。当端口 **A** 与
*P*env 之间的压力差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Check valve maximum pressure differential** — 缓冲阀最大压差 `0.1` `MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持真实。

#### 依赖关系

要启用此参数，请选择 **Cylinder end cushioning**。

### **Check valve maximum area** — 完全打开的缓冲阀面积 `1e-4` `m^2`（默认）| 正标量

缓冲阀在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder end cushioning**。

### **Check valve leakage area** — 完全关闭位置时的缓冲阀间隙面积 `1e-10` `m^2`（默认）| 正标量

当缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动的连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder end cushioning**。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当可变节流口和单向阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder end cushioning**。

### Friction

### **Cylinder friction** — 是否对活塞运动建模摩擦力 `off`（默认）| `on`

是否对活塞运动建模摩擦力。该模块考虑库仑摩擦、Stribeck 摩擦和粘性摩擦。有关更多信息，请参阅 Cylinder Friction (TL) 模块。

### **Breakaway to Coulomb friction force ratio** — 启动力与库仑摩擦力之比 `1.2`（默认）| 正标量

启动力与库仑摩擦力之比。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Breakaway friction velocity** — 运动阈值 `0.1` `m/s`（默认）| 正标量

开始克服摩擦力运动的速度阈值。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Preload force** — 由密封组件引起的缸内初始力 `20` `N`（默认）| 标量

由密封组件引起的缸内初始力。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Coulomb friction force coefficient** — 库仑摩擦力系数 `1e-6` `N/Pa`（默认）| 正标量

库仑摩擦力系数。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Viscous friction coefficient** — 粘性摩擦系数 `100` `N*s/m`（默认）| 正标量

粘性摩擦系数。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### 初始条件

### **Piston displacement** — 确定活塞位置的方法 `根据端口 R 相对于端口的速度计算 C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，该模块可以从 Multibody 模块接收位置；或者可以在内部计算位置，并在端口 **p** 处报告位置。当机械方向为正时，位置介于 `0` 和 **Piston stroke** 参数的值之间；当机械方向为负时，位置介于 `0` 和 **Piston stroke** 参数的负值之间。

### **Initial piston displacement** — 仿真开始时的活塞位置 `0` `m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston displacement** 设置为 `根据端口 R 相对于端口的速度计算 C`。

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对由流体可压缩性引起的任何流体密度变化建模。当选择 **Fluid compressibility** 时，除了由压力变化引起的密度变化外，还会计算由进入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **Initial liquid temperature** — 起始液体温度 `293.15` `K`（默认）| 标量

执行器中液体体积的初始温度。

### **Initial liquid pressure** — 可压缩流体的起始液体压力 `0.101325` `MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Nominal liquid temperature** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的液体温度。当禁用动态可压缩性时，该模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的液体压力。当禁用动态可压缩性时，该模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

## 所属库

Simscape / Fluids / Thermal Liquid / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：对气缸摩擦或缓冲建模

该模块新增了用于对气缸摩擦或缓冲建模的选项。选择 **Cylinder friction** 参数以包含摩擦力对活塞运动的影响。选择 **Cylinder end cushioning** 参数以对最大伸出时的活塞减速建模。

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。此选项称为 `Based on coefficient of restitution`，使用模式图对硬限位建模。

## 描述

热液体网络中的单作用线性执行器

Single-Acting Actuator (TL) 模块对由单个热液体腔控制的带活塞线性执行器建模。执行器在伸出和回缩行程中产生力，但执行力取决于单个腔的表压。

该图显示了执行器的关键组件。端口 **A** 表示热液体腔入口。端口 **R** 表示平移的执行器活塞，端口 **C** 表示执行器壳体。端口 **H** 表示热液体腔与环境之间的热接口。

Single-Acting Actuator Schematic

### Displacement

该模块将活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**Mechanical orientation** 参数用于确定活塞位移的方向。当腔室容积等于 **Dead volume** 参数的值时，活塞位移为中性，即 `0`。当 **Piston displacement** 参数为 `Provide input signal from Multibody joint` 时，您通过端口 **p** 输入活塞位移。您可以使用 Translational Multibody Interface 模块提供活塞位移，以确保位置信号的导数等于活塞速度。

活塞运动的方向取决于 **Mechanical orientation** 参数。如果机械方向为正，则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平移为正。当机械方向为负时，运动方向反转。

### Hard Stop

一组硬限位限制活塞的运动范围。该模块使用 Translational Hard Stop 模块的一种实现，将硬限位视为弹簧-阻尼系统。弹簧刚度系数控制硬限位接触力的恢复分量，阻尼系数控制耗散分量。

硬限位位于活塞行程的远端。如果机械方向为正，则下限位位于 *x* = 0，上限位位于 *x* = +*stroke*。如果机械方向为负，则下限位位于 *x* = -*stroke*，上限位位于 *x* = 0。

### Cushion

该模块可以建模活塞行程两端附近的缓冲。选择 **Cylinder end cushioning** 可在活塞运动接近由 **Piston stroke** 参数定义的最大伸出量时减缓其运动。有关气缸缓冲功能的更多信息，请参阅 Cylinder Cushion (TL) 模块。

### Friction

该模块可以建模阻碍活塞运动的摩擦力。当您选择 **Cylinder friction** 时，所产生的摩擦是 Stribeck、Coulomb 和黏性效应的组合。该模块测量腔室压力与环境压力之间的压差。有关摩擦模型及其限制的更多信息，请参阅 Cylinder Friction (TL) 模块。

### Block Composite

该模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter (TL)
- Translational Hard Stop
- Ideal Translational Motion Sensor

组成该模块的元件图。

如果您选择 **Cylinder friction** 或 **Cylinder end cushioning**，则该模块复合体还包括 Cylinder Friction (TL) 模块或 Cylinder Cushion (TL) 模块。

包含摩擦和缓冲的模块组成元件图。
