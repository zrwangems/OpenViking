---
type: simulink-block
title: 'Double-Acting Actuator (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'doubleactingactuatoril'
documentation_source_path: 'ref/doubleactingactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (IL)

## 端口

### 输入

### **p** — 活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入端口，该活塞位置由您使用 Simscape Multibody 模块指定。

#### 依赖关系

要显示此端口，请将 **Piston displacement from chamber A cap** 设置为 `Provide input signal from Multibody joint`。
### 输出

### **p** — 活塞位置输出，m 物理信号

与活塞位置关联的物理信号端口。

#### 依赖关系

要显示此端口，请将 **Piston displacement from chamber A cap** 设置为 `Calculate from velocity of port R relative to port C`。
### 守恒

### **A** — 腔室 A 入口等温液体

与腔室 A 入口关联的等温液体守恒端口。

### **B** — 腔室 B 入口等温液体

与腔室 B 入口关联的等温液体守恒端口。

### **C** — 执行器外壳机械平移

与外壳关联的机械平移守恒端口。

### **R** — 执行器活塞机械平移

与活塞关联的机械平移守恒端口。

## 参数

### Actuator

### **Same fluid on both sides** — 在两个腔室中建模相同流体的选项 `on`（默认）| `off`

是否在两个执行器腔室中建模相同流体。如果您选择此参数，则执行器通过两个腔室传播流体属性。清除此参数以将每个腔室建模为不同的流体，其中每个腔室连接到隔离的流体网络。

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

设置活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为正。这对应于杆伸出。
- `Pressure at A causes negative displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为负。这对应于杆缩回。

### **Piston cross-sectional area in chamber A** — 腔室 A 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 A 侧活塞杆的横截面积。

### **Piston cross-sectional area in chamber B** — 腔室 B 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 B 侧活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume in chamber A** — 活塞完全缩回时的腔室 A 流体体积 `1e-5 m^3`（默认）| 正标量

腔室 A 中活塞位移为 `0` 时的液体体积。这是活塞抵住执行器端盖时的液体体积。

### **Dead volume in chamber B** — 活塞完全缩回时的腔室 B 流体体积 `1e-5 m^3`（默认）| 正标量

腔室 B 中活塞位移为 `0` 时的液体体积。这是活塞抵住执行器端盖时的液体体积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric pressure` 选项将环境压力设置为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

### **Breakaway to Coulomb friction force ratio** — 分离力与库仑摩擦力之比 `1.2`（默认）| 正标量

分离力与库仑摩擦力之比。

#### 依赖关系

要启用此参数，请在 **Friction** 选项卡中，选择 **Cylinder friction effect**。

### **Breakaway friction velocity** — 运动阈值 `0.1 m/s`（默认）| 正标量

克服摩擦力开始运动的阈值速度。

#### 依赖关系

要启用此参数，请在 **Friction** 选项卡中，选择 **Cylinder friction effect**。

### Hard Stop

### **Hard stop model** — 选择硬停止模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时的力模型选择。有关更多信息，请参阅 Translational Hard Stop 模块。

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

### **Transition region** — 硬停止力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬停止力模型的应用范围。在活塞最大伸出和活塞最大缩回的这个范围之外，不应用 **Hard stop model**，并且活塞上没有额外的力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与停止件之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与停止件之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与停止件之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与停止件之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击外壳时，它们保持接触。否则，滑块弹跳。要避免建模滑块与外壳之间的静态接触，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### Converter Cushion A

### **Cylinder A end cushioning** — 是否建模活塞在最大伸出时的减速 `off`（默认）| `on`

是否建模活塞在最大伸出时的减速。有关更多信息，请参阅 Cylinder Cushion (IL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4 m^2`（默认）| 正标量

执行器缓冲元件内柱塞的面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3 m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Cushion orifice area** — 缓冲腔室之间的节流孔面积 `1e-6 m^2`（默认）| 正标量

缓冲腔室之间节流孔的面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与套筒之间的间隙 `1e-7 m^2`（默认）| 正标量

缓冲柱塞与套筒之间的间隙面积。此值通过保持流动的连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01 MPa`（默认）| 正标量

触发阀门操作的压力。当端口 **A** 与 *P*env 之间的压力差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve maximum pressure differential** — 最大缓冲压差 `0.1 MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持真实。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve maximum area** — 完全打开的缓冲阀面积 `1e-4 m^2`（默认）| 正标量

缓冲阀在完全打开位置的横截面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve leakage area** — 完全关闭位置时的缓冲阀间隙面积 `1e-10 m^2`（默认）| 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动的连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder A end cushioning**。

### Converter Cushion B

### **Cylinder B end cushioning** — 是否建模活塞在最大伸出时的减速 `off`（默认）| `on`

是否建模活塞在最大伸出时的减速。有关更多信息，请参阅 Cylinder Cushion (IL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4 m^2`（默认）| 正标量

执行器缓冲元件内柱塞的面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3 m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Cushion orifice area** — 缓冲腔室之间的节流孔面积 `1e-6 m^2`（默认）| 正标量

缓冲腔室之间节流孔的面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与套筒之间的间隙 `1e-7 m^2`（默认）| 正标量

缓冲柱塞与套筒之间的间隙面积。此值通过保持流动的连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01 MPa`（默认）| 正标量

触发阀门操作的压力。当端口 **A** 与 *P*env 之间的压力差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve maximum pressure differential** — 最大缓冲压差 `0.1 MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持真实。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve maximum area** — 完全打开的缓冲阀面积 `1e-4 m^2`（默认）| 正标量

缓冲阀在完全打开位置的横截面积。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve leakage area** — 完全关闭位置时的缓冲阀间隙面积 `1e-10 m^2`（默认）| 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动的连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当可变节流孔和单向阀处于接近打开或接近关闭位置时，引入一层逐渐变化的流动响应。将此值设置为小于 1 的非零值，以提高您在这些情况下的仿真稳定性。

#### 依赖关系

要启用此参数，请选择 **Cylinder B end cushioning**。

### Friction

### **Cylinder friction effect** — 是否建模对抗活塞运动的摩擦 `off`（默认）| `on`

是否建模对抗活塞运动的摩擦。该模块考虑库仑摩擦、Stribeck 摩擦和粘性摩擦。有关更多信息，请参阅 Cylinder Friction 模块。

### **Breakaway to Coulomb friction force ratio** — 分离力与库仑摩擦力之比 `1.2`（默认）| 正标量

分离力与库仑摩擦力之比。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Breakaway friction velocity** — 运动阈值 `0.1` `m/s`（默认）| 正标量

克服摩擦力开始运动的阈值速度。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction**。

### **Preload force** — 缸体上的初始力 `20 N`（默认）| 标量

缸体处于中立位置时施加在缸体上的力。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction effect**。

### **Coulomb friction force coefficient** — 库仑摩擦力系数 `1e-6 N/Pa`（默认）| 正标量

库仑摩擦力系数。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction effect**。

### **Viscous friction coefficient** — 粘性摩擦系数 `100 N/(m/s)`（默认）| 正标量

粘性摩擦系数。

#### 依赖关系

要启用此参数，请选择 **Cylinder friction effect**。

### Leakage

### **Internal leakage** — 是否建模环形泄漏 `off`（默认）| `on`

是否建模在参考环境条件下流体腔室与活塞储液器之间的环形泄漏。该泄漏被视为层流。有关更多信息，请参阅 Laminar Leakage (IL) 模块。

#### 依赖关系

要启用此参数，请选择 **Same fluid on both sides**。

### **Piston-cylinder clearance** — 径向间隙 `1e-4 m`（默认）| 正标量

活塞杆与缸体外壳之间的径向距离。

#### 依赖关系

要启用此参数，请选择 **Same fluid on both sides** 和 **Internal leakage**。

### **Piston head length** — 活塞安装的环形长度 `0.01 m`（默认）| 正标量

活塞头的长度。

#### 依赖关系

要启用此参数，请选择 **Same fluid on both sides** 和 **Internal leakage**。

### Initial Conditions

### **从腔室 A 端盖开始的活塞位移** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

用于确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，该模块可以从 Multibody 模块接收位置，或者在内部计算位置并在端口 **p** 报告位置。当机械方向为正时，位置介于 `0` 和 **活塞行程** 之间；当机械方向为负时，位置介于 `0` 和 –**活塞行程** 之间。

### **从腔室 A 端盖开始的初始活塞位移** — 仿真开始时从腔室 A 端盖测量的活塞位置 `0 m`（默认）| 标量

仿真开始时相对于腔室 A 端盖的活塞位置。

#### 依赖关系

要启用此参数，请将 **从腔室 A 端盖开始的活塞位移** 设置为 `Calculate from velocity of port R relative to port C`。

### **启用动态可压缩性** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对由流体可压缩性引起的任何流体密度变化进行建模。当您选中 **启用动态可压缩性** 时，除压力变化引起的密度变化外，还会计算因流入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **腔室 A 中的初始液体压力** — 腔室 A 中的起始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**。

### **腔室 B 中的初始液体压力** — 腔室 B 中的起始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**。

### **腔室 A 中的标称液体压力** — 腔室 A 中名义工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 A 中名义工况下的液体压力。当动态可压缩性禁用时，该模块使用此值计算用于质量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **腔室 B 中的标称液体压力** — 腔室 B 中名义工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 B 中名义工况下的液体压力。当动态可压缩性禁用时，该模块使用此值计算用于质量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a: 在执行器两侧对不同的流体建模

清除新的 **两侧相同流体** 参数，以阻止流体属性传播，并将每个腔室建模为连接到其自身隔离流体网络的不同流体。

### R2023a: 新的硬限位参数化选项

该模块为 **硬限位模型** 参数提供了新选项。此选项称为 `Based on coefficient of restitution`，通过使用模式图对硬限位建模。

## 描述

等温液体系统中压差到致动的线性转换

Double-Acting Actuator (IL) 模块表示将两个腔室之间的压差线性转换为活塞运动。活塞致动由作用在分隔腔室的活塞板上的压差控制。当活塞接近完全伸出或完全缩回时，其运动受到四种硬限位模型之一的限制。可选择在两个活塞腔室中对流体可压缩性建模。

端口 **A** 和 **B** 是等温液体入口。端口 **C** 表示执行器壳体，而活塞速度在端口 **R** 返回。当活塞位置在内部计算时，会在端口 **p** 报告；当位置通过连接到 Simscape™ Multibody™ 关节设置时，会在端口 **p** 作为物理信号接收。

您可以使用 **机械方向** 参数定义活塞位移方向。如果机械方向设置为 `Pressure at A causes positive displacement of R relative to C`，则当压差 *p_A* – *p_B* 为正时，活塞伸出。如果 **机械方向** 设置为 `Pressure at A causes negative displacement of R relative to C`，则对于液体腔室和气体腔室之间的正压差，活塞缩回。

### 位移

活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**机械方向** 标识活塞位移的方向。当腔室 A 体积等于腔室死区体积时，活塞位移为中性，即 `0`。当位移作为输入接收时，请确保位置的导数等于活塞速度。当输入来自连接到 Simscape Multibody 关节的 Translational Multibody Interface 模块连接时，会自动如此。

### 硬限位模型

为避免执行器在完全伸出或完全缩回时发生机械损坏，当活塞接近这些极限时，执行器通常表现出非线性行为。Double-Acting Actuator (IL) 模块通过四种硬限位模型的选择对此行为建模，这些模型通过弹簧-阻尼器系统对材料柔度建模。硬限位模型包括：

- `Stiffness and damping applied smoothly through transition region, damped rebound`.
- `Full stiffness and damping applied at bounds, undamped rebound`.
- `Full stiffness and damping applied at bounds, damped rebound`.
- `Based on coefficient of restitution`

当活塞处于其上限或下限时，对硬限位力建模。边界区域位于 **活塞行程** 或活塞初始位移的 **过渡区域** 内。在该区域之外，FHardStop=0。

有关这些设置的详细信息，请参阅 Translational Hard Stop 模块页面。

### 缓冲

该模块可以对活塞行程两端附近的缓冲建模。选择 **缸端缓冲** 以在活塞接近由 **活塞行程** 参数定义的最大伸出时减慢活塞运动。有关缸缓冲功能的详细信息，请参阅 Cylinder Cushion (IL) 模块。

### 摩擦

该模块可以对阻碍活塞运动的摩擦建模。当您选择 **缸摩擦** 时，产生的摩擦是 Stribeck、Coulomb 和黏性效应的组合。该模块测量腔室压力和环境压力之间的压差。有关摩擦模型及其限制的详细信息，请参阅 Cylinder Friction (IL) 模块。

### 泄漏

您可以选择对腔室 A 和腔室 B 之间的泄漏建模。当两个腔室中的流体相同且您选择 **内部泄漏** 时，会在活塞和缸之间对 Poiseuille 流建模。该模块使用 Simscape Foundation Library Laminar Leakage (IL) 模块。流量计算如下：

\[
\dot m = \frac{\pi}{128 \nu L} \left[ d_0^4 - d_i^4 - \frac{(d_0^2 - d_i^2)^2}{\log(d_0/d_i)} \right] (p_A - p_B)
\]

其中：

- *ν* 是流体运动黏度。
- *L* 是活塞长度，**p** – *P*0。
- *p_A* 是端口 **A** 处的压力。
- *p_B* 是端口 **B** 处的压力。

缸直径 *d_0* 为 \(d_0=d_i+2c\)，其中 *c* 是 **活塞-缸间隙**，活塞直径 *d_i* 为 \(d_i=\sqrt{\frac{4A_P}{\pi}}\)，其中 *A_P* 是 **腔室 A 中的活塞横截面积** 和 **腔室 B 中的活塞横截面积** 参数的平均值。

### 数值平滑面积和压力

您可以通过调整 **平滑因子** 参数来保持仿真中的数值稳健性。如果 **平滑因子** 参数非零，该模块会平滑缓冲 A 和 B 的孔口面积以及单向阀压力范围。孔口面积在缓冲 A 和缓冲 B 的 **柱塞与缓冲套筒之间的泄漏面积** 和 **缓冲柱塞横截面积** 参数之间平滑饱和，而阀压力在缓冲 A 和缓冲 B 的 **单向阀开启压力差** 和 **单向阀最大压力差** 参数之间饱和。有关详细信息，请参阅 Numerical Smoothing。

### 模块原理图

Double-Acting Actuator (IL) 模块包含四个 Simscape Foundation 模块：

- Laminar Leakage (IL)
- Translational Mechanical Converter (IL)
- Translational Hard Stop
- Ideal Translational Motion Sensor

以及两个 Isothermal Liquid 库模块：

- Cylinder Cushion (IL)
- Cylinder Friction (IL)

### 动量平衡

该执行器的动量守恒方程为

\[
F = \varepsilon (S_A p_A - S_B p_B - S_{Rod} p_{env})
\]

其中：

- *F* 是液体施加在转换器接口上的力。此力表达式未考虑硬限位、缸缓冲或缸摩擦子组件引起的力贡献。要查看这些对转换器接口的力贡献，请参阅这些子组件的文档页面。
- *ε* 取决于转换器的 **机械方向**。如果 **机械方向** 为 `Pressure at A causes positive displacement of R relative to C`，则 *ε* `= 1`。如果 **机械方向** 为 `Pressure at A causes negative displacement of R relative to C`，则 *ε* `= -1`。
- *S_Rod* 是杆横截面积，其中 \(S_{Rod}=S_A-S_B\)。
- *S_A* 是 **腔室 A 中的活塞横截面积** 参数的值。
- *S_B* 是 **腔室 B 中的活塞横截面积** 参数的值。
- *p_A* 是腔室 A 内的压力。
- *p_B* 是腔室 B 内的压力。
- *p_env* 是环境压力。
