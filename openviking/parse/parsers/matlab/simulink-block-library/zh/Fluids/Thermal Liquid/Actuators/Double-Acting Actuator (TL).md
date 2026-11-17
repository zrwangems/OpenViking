---
type: simulink-block
title: 'Double-Acting Actuator (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Actuators'
documentation_page: 'doubleactingactuatortl'
documentation_source_path: 'ref/doubleactingactuatortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (TL)

## 端口

### 输入

### **p** — 活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入，单位为 m。使用 Translational Multibody Interface 模块将此端口连接到 Simscape Multibody™ 网络。

#### 依赖

要启用此端口，请将 **Piston displacement from chamber A cap** 设置为 `Provide input signal from Multibody joint`。
### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置关联的物理信号端口。

#### 依赖

要启用此端口，请将 **Piston displacement from chamber A cap** 设置为 `根据端口 R 相对于端口的计算速度 C`。
### 守恒

### **A** — 腔室 A 入口热液体

与腔室 A 入口关联的热液体守恒端口。

### **B** — 腔室 B 入口热液体

与腔室 B 入口关联的热液体守恒端口。

### **R** — 执行器活塞机械平移

与执行器活塞关联的机械平移守恒端口。

### **C** — 执行器壳体机械平移

与执行器壳体关联的机械平移守恒端口。

### **HA** — 腔室 A 热流热

与腔室 A 关联的热守恒端口。

### **HB** — 腔室 B 热流热

与腔室 B 关联的热守恒端口。

## 参数

### 执行器

### **Same fluid on both sides** — 在两个腔室中建模相同流体的选项 `on`（默认）| `off`

是否在两个执行器腔室中建模相同的流体。如果选择此参数，执行器将通过两个腔室传播流体属性。清除此参数可将每个腔室建模为不同的流体，其中每个腔室连接到隔离的流体网络。

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of R relative to C`，当端口 **A** 处的液体体积膨胀时，活塞位移为正。此运动对应于活塞杆伸出。
- `Pressure at A causes negative displacement of R relative to C`，当端口 **A** 处的液体体积膨胀时，活塞位移为负。此运动对应于活塞杆缩回。

### **Piston cross-sectional area in chamber A** — 腔室 A 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 A 侧活塞杆的横截面积。

### **Piston cross-sectional area in chamber B** — 腔室 B 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 B 侧活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume in chamber A** — 活塞完全缩回时腔室 A 的流体体积 `1e-5 m^3`（默认）| 正标量

腔室 A 中活塞位移为 `0` 时的液体体积。此参数是活塞抵靠执行器端盖时的液体体积。

### **Dead volume in chamber B** — 活塞完全缩回时腔室 B 的流体体积 `1e-5 m^3`（默认）| 正标量

腔室 B 中活塞位移为 `0` 时的液体体积。此参数是活塞抵靠执行器端盖时的液体体积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric pressure` 选项将环境压力设置为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

### 硬限位

### **Hard stop model** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全缩回时使用的硬限位模型。有关更多信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。当活塞的最大伸出或缩回超出此范围时，模块不应用硬限位模型。在这种情况下，活塞上没有额外的力。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免建模滑块与壳体之间的静态接触，请将此参数设置为 `0`。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 缓冲 A

### **Cylinder A end cushioning** — 是否建模活塞在最大伸出时的减速 `off`（默认）| `on`

是否建模活塞在最大伸出时的减速。有关更多信息，请参阅 Cylinder Cushion (TL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4 m^2`（默认）| 正标量

执行器缓冲元件内柱塞的面积。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3 m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Cushion orifice area** — 缓冲腔之间的节流孔面积 `1e-6 m^2`（默认）| 正标量

缓冲腔之间节流孔的面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与缓冲套之间的间隙 `1e-7 m^2`（默认）| 正标量

缓冲柱塞与缓冲套之间的间隙面积。该值通过保持流动的连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01 MPa`（默认）| 正标量

触发阀操作的压差阈值。当端口 **A** 与 *Penv* 之间的压差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve maximum pressure differential** — 最大缓冲压差 `0.1 MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持在实际范围内。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve maximum area** — 缓冲阀完全打开时的面积 `1e-4 m^2`（默认）| 正标量

缓冲阀在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve leakage area** — 缓冲阀完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。该值通过保持流动的连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当可变节流孔和单向阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### Cushion B

### **Cylinder B end cushioning** — 是否对活塞在最大伸出位置进行减速建模 `off`（默认）| `on`

是否对活塞在最大伸出位置进行减速建模。有关详细信息，请参阅 Cylinder Cushion (TL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4 m^2`（默认）| 正标量

执行器缓冲元件内部柱塞的面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3 m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Cushion orifice area** — 缓冲腔之间的节流孔面积 `1e-6 m^2`（默认）| 正标量

缓冲腔之间节流孔的面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与缓冲套之间的间隙 `1e-7 m^2`（默认）| 正标量

缓冲柱塞与缓冲套之间的间隙面积。该值通过保持流动的连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01 MPa`（默认）| 正标量

触发阀操作的压差阈值。当端口 **A** 与 *P*env 之间的压差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve maximum pressure differential** — 最大缓冲压差 `0.1 MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持在实际范围内。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve maximum area** — 缓冲阀完全打开时的面积 `1e-4 m^2`（默认）| 正标量

缓冲阀在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve leakage area** — 缓冲阀完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。该值通过保持流动的连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当可变节流孔和单向阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### Friction

### **Cylinder friction** — 是否对活塞运动进行摩擦建模 `off`（默认）| `on`

是否对活塞运动进行摩擦建模。该模块考虑库仑摩擦、Stribeck 摩擦和粘性摩擦。有关详细信息，请参阅 Cylinder Friction (TL) 模块。

### **Breakaway to Coulomb friction force ratio** — 脱离力与库仑摩擦力之比 `1.2`（默认）| 正标量

脱离力与库仑摩擦力之比。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Breakaway friction velocity** — 运动阈值 `0.1` `m/s`（默认）| 正标量

克服摩擦力开始运动的速度阈值。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Preload force** — 缸体上的初始力 `20 N`（默认）| 标量

缸体处于中位时施加在其上的力。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Coulomb friction force coefficient** — 库仑摩擦力系数 `1e-6 N/Pa`（默认）| 正标量

库仑摩擦力系数。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Viscous friction coefficient** — 粘性摩擦系数 `100 N*s/m`（默认）| 正标量

粘性摩擦系数。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### 初始条件

### **Piston displacement from chamber A cap** — 确定活塞位置的方法 `根据端口 R 相对于端口的计算速度 C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，该模块可以从 Multibody 模块接收位置，也可以内部计算位置并在端口 **p** 处报告位置。当机械方向为正时，位置介于 `0` 与 **Piston stroke** 参数的值之间；当机械方向为负时，位置介于 `0` 与 **Piston stroke** 参数的负值之间。

### **Initial piston displacement from chamber A cap** — 仿真开始时的活塞位置 `0` `m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston displacement** 设置为
`根据端口 R 相对于端口的计算速度
C`。

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对流体可压缩性导致的流体密度变化进行建模。当您选择 **Fluid compressibility** 时，除了因压力变化引起的密度变化外，还会计算因流入模块的质量流量引起的密度变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **Initial liquid temperature in chamber A** — 腔室 A 中的起始液体温度 `293.15` `K`（默认）| 标量

执行器中液体体积的初始温度。

### **Initial liquid temperature in chamber B** — 腔室 B 中的起始液体温度 `293.15` `K`（默认）| 标量

执行器中液体体积的初始温度。

### **Initial liquid pressure in chamber A** — 腔室 A 中可压缩流体的起始液体压力 `0.101325` `MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic
compressibility**。

### **Initial liquid pressure in chamber B** — 腔室 B 中可压缩流体的起始液体压力 `0.101325` `MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic
compressibility**。

### **Nominal liquid pressure in chamber A** — 腔室 A 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 A 中额定工况下的液体压力。当动态可压缩性被禁用时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic
compressibility** 复选框。

### **Nominal liquid pressure in chamber B** — 腔室 B 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 B 中额定工况下的液体压力。当动态可压缩性被禁用时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic
compressibility** 复选框。

### **Nominal liquid temperature in chamber A** — 腔室 A 中额定工况下的温度 `293.15` `K`（默认）| 标量

腔室 A 中额定工况下的液体温度。当动态可压缩性被禁用时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic
compressibility** 复选框。

### **Nominal liquid temperature in chamber B** — 腔室 B 中额定工况下的温度 `293.15` `K`（默认）| 标量

腔室 B 中额定工况下的液体温度。当动态可压缩性被禁用时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic
compressibility** 复选框。

## 所属库

Simscape / Fluids / Thermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024a：对执行器两侧的不同流体建模

清除新的 **Same fluid on both sides** 参数，以阻止流体属性传播，并将每个腔室建模为连接到其自身隔离流体网络的不同流体。

### R2023b：对气缸摩擦或缓冲建模

该模块新增了用于对气缸摩擦或缓冲建模的选项。选择 **Cylinder friction effect** 参数以包含摩擦对活塞运动的影响。选择 **Cylinder A end cushioning** 或 **Cylinder B end cushioning** 参数，以对任一气缸在最大伸出时的活塞减速进行建模。

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。此选项称为 `Based on coefficient of restitution`，使用模式图对硬限位进行建模。

## 描述

热液体网络中的双作用线性执行器

Double-Acting Actuator (TL) 模块对由两个相对的热液体腔室控制的活塞线性执行器进行建模。执行器在伸出和回缩行程中产生力。所产生的力取决于两个腔室之间的压差。

该图显示了执行器的关键组件。端口 **A** 和 **B** 表示热液体腔室入口。端口 **R** 表示平移的执行器活塞，端口 **C** 表示执行器壳体。端口 **HA** 和 **HB** 表示每个腔室与环境之间的热接口。移动活塞是绝热的。

双作用执行器示意图

### 位移

模块将活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**Mechanical orientation** 参数确定活塞位移的方向。当腔室 A 体积等于 **Dead volume in chamber A** 参数的值时，活塞位移为中性，即 `0`。当 **Piston displacement from chamber A cap** 参数为 `Provide input signal from Multibody joint` 时，您使用端口 **p** 输入活塞位移。您可以通过使用 Translational Multibody Interface 模块提供活塞位移，以确保位置信号的导数等于活塞速度。

活塞运动的方向取决于 **Mechanical orientation** 参数。如果机械方向为正，则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平移为正。当机械方向为负时，运动方向反转。

### 硬限位

一组硬限位限制活塞的运动范围。该模块使用 Translational Hard Stop 模块的实现，将硬限位视为弹簧-阻尼系统。弹簧刚度系数控制硬限位接触力的恢复分量，阻尼系数控制耗散分量。

硬限位位于活塞行程的远端。如果机械方向为正，则下限位在 *x* = 0 处，上限位在 *x* = +*stroke* 处。如果机械方向为负，则下限位在 *x* = -*stroke* 处，上限位在 *x* = 0 处。

### 缓冲

该模块可以对活塞行程两端的缓冲进行建模。选择 **Cylinder end cushioning**，以在活塞接近由 **Piston stroke** 参数定义的最大伸出时减慢其运动。有关气缸缓冲功能的更多信息，请参见 Cylinder Cushion (TL) 模块。

### 摩擦

该模块可以对阻碍活塞运动的摩擦进行建模。当您选择 **Cylinder friction** 时，所产生的摩擦是 Stribeck、Coulomb 和粘性效应的组合。该模块测量腔室压力与环境压力之间的压差。有关摩擦模型及其限制的更多信息，请参见 Cylinder Friction (TL) 模块。

### Block Composite

此模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter
  (TL)
- Translational Hard Stop
- Ideal Translational Motion Sensor

构成该模块的元件图。

如果选择 **Cylinder friction**、**Cylinder A end
cushioning** 或 **Cylinder B end cushioning**，则该模块
复合组件还包括 Cylinder Friction
(TL) 模块或两个 Cylinder Cushion
(TL) 模块。

包含摩擦和缓冲的模块构成元件图。
