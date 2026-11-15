---
type: simulink-block
title: 'Single-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Actuators'
documentation_page: 'singleactingactuatoril'
documentation_source_path: 'ref/singleactingactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Single-Acting Actuator (IL)

## 端口

### 输入

### **p** — Multibody 活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入端口，单位为 m。
将此端口连接到 Simscape Multibody 模块。

#### 依赖关系

要启用此端口，请将 **Piston displacement** 设置为 `Provide input signal from Multibody joint`。

### 输出

### **p** — 活塞位置，m 物理信号

活塞位置，单位为 m，作为物理信号返回。

#### 依赖关系

要显示此端口，请将 **Piston displacement** 设置为 `Calculate from velocity of port R relative to port C`。

### 守恒

### **A** — 液体端口 isothermal liquid

与腔室 A 关联的 Thermal liquid 守恒端口。

### **C** — 执行器壳体 translational mechanical

与执行器壳体关联的 translational mechanical 守恒端口。

### **R** — 执行器活塞 translational mechanical

与执行器活塞关联的 translational mechanical 守恒端口。

## 参数

### 执行器

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

设置活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C` 当端口 **A** 处液体体积膨胀时，活塞位移为正。这对应杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C` 当端口 **A** 处液体体积膨胀时，活塞位移为负。这对应杆收缩。

### **Piston cross-sectional area** — 活塞杆横截面积 `0.01` `m^2`（默认）| 正标量

活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程 `0.1``m`（默认）| 正标量

最大活塞行程。

### **Dead volume** — 活塞完全缩回时的流体体积 `1e-5` `m^3`（默认）| 正标量

当活塞位移为 `0` 时的液体体积。这是活塞抵靠执行器端盖时的液体体积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric pressure` 选项将环境压力设置为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325` `MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

### 硬止动

### **Hard stop model** — 选择硬止动模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞完全伸出或完全缩回时作用力的模型选择。有关详细信息，请参见 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

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

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — 硬止动力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬止动力模型的应用范围。在活塞最大伸出和活塞最大缩回的这个范围之外，不应用 **Hard stop model**，并且对活塞没有额外作用力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与止动件之间最终相对速度与初始相对速度之比 `0.7`（默认）| 介于 0 和 1 之间的无单位值

滑块弹跳后，滑块与止动件之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与止动件之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与止动件之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式转换为自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 缓冲

### **Cylinder end cushioning** — 是否对最大伸出时的活塞减速建模 `off`（默认）| `on`

是否对最大伸出时的活塞减速建模。有关详细信息，请参见 Cylinder Cushion (IL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4` `m^2`（默认）| 正标量

执行器缓冲元件内柱塞的面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3` `m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Cushion orifice area** — 缓冲腔之间的节流孔面积 `1e-6` `m^2`（默认）| 正标量

缓冲腔之间的节流孔面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与套筒之间的间隙 `1e-7` `m^2`（默认）| 正标量

缓冲柱塞与套筒之间的间隙面积。此值通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01` `MPa`（默认）| 正标量

超过该压力时，阀门操作触发。当端口 **A** 与 *P*env 之间的压力差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Check valve maximum pressure differential** — 缓冲压差最大值 `0.1` `MPa`（默认）| 正标量

缓冲阀最大压差。此参数提供压力上限，以使系统压力保持真实。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Check valve maximum area** — 完全打开的缓冲阀面积 `1e-4` `m^2`（默认）| 正标量

缓冲阀在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Check valve leakage area** — 完全关闭位置时缓冲阀间隙面积 `1e-10` `m^2`（默认）| 正标量

当缓冲单向阀处于完全关闭位置时所有间隙之和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当可变节流孔和单向阀处于接近打开或接近关闭位置时，该因子为流量响应引入一层渐变。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### 摩擦

### **Cylinder friction** — 是否对阻碍活塞运动的摩擦建模 `off`（默认）| `on`

是否对阻碍活塞运动的摩擦建模。该模块考虑 Coulomb、Stribeck 和黏性摩擦。有关详细信息，请参见 Cylinder Friction 模块。

### **Breakaway to Coulomb friction force ratio** — 分离力与 Coulomb 摩擦力之比 `1.2`（默认）| 正标量

分离力与 Coulomb 摩擦力之比。

#### 依赖关系

要启用此参数，请选中 **Cylinder friction**。

### **Breakaway friction velocity** — 运动阈值 `0.1` `m/s`（默认）| 正标量

克服摩擦力开始运动的速度阈值。

#### 依赖关系

要启用此参数，请选中 **Cylinder friction**。

### **Preload force** — 由于密封组件在缸体中产生的初始力 `20` `N`（默认）| 标量

由于密封组件在缸体中产生的初始力。

#### 依赖关系

要启用此参数，请选中 **Cylinder friction**。

### **Coulomb friction force coefficient** — Coulomb 摩擦力系数 `1e-6` `N/Pa`（默认）| 正标量

Coulomb 摩擦力系数。

#### 依赖关系

要启用此参数，请选中 **Cylinder friction**。

### **Viscous friction coefficient** — 黏性摩擦系数 `100` `N*s/m`（默认）| 正标量

黏性摩擦系数。

#### 依赖关系

要启用此参数，请选中 **Cylinder friction**。

### 泄漏

### **Leakage** — 是否对环形泄漏建模 `off`（默认）| `on`

是否对参考环境条件下流体腔与活塞储液腔之间的环形泄漏建模。该泄漏视为层流。有关详细信息，请参见 Laminar Leakage (IL) 模块。

### **Piston-cylinder clearance** — 径向间隙 `1e-4` `m`（默认）| 正标量

活塞杆与缸体壳体之间的径向距离。

#### 依赖关系

要启用此参数，请选中 **Leakage**。

### **Piston head length** — 活塞安装的环形长度 `0.01` `m`（默认）| 正标量

活塞头的长度。

#### 依赖关系

要启用此参数，请选中 **Leakage**。

### 初始条件

### **Piston displacement** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，该模块可以从 Multibody 模块接收位置；或者内部计算位置并在端口 **p** 报告位置。当机械方向为正时，位置介于 `0` 与 **Piston stroke** 之间；当机械方向为负时，位置介于 `0` 与 –**Piston stroke** 之间。

### **Initial piston displacement** — 仿真开始时的活塞位置 `0` `m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston displacement** 设置为 `Calculate from velocity of port R relative to port C`。

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对由流体可压缩性引起的流体密度变化建模。当您选中 **Enable dynamic compressibility** 时，除压力变化引起的密度变化外，还会计算流入模块的质量流量引起的变化。在 Isothermal Liquid 库中，所有模块都将密度计算为压力的函数。

### **Initial liquid pressure** — 可压缩流体的起始液体压力 `0.101325` `MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Nominal liquid pressure** — 标称工作条件下的压力 `0.101325 MPa`（默认）| 标量

标称工作条件下的液体压力。当禁用动态可压缩性时，该模块使用此值计算质量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：新的硬止动参数化选项

该模块为 **Hard stop model** 参数提供了一个新选项。此选项称为 `Based on coefficient of restitution`，使用模式图对硬止动进行建模。

## 描述

等温液体系统中的单作用线性执行器

Single-Acting Actuator (IL) 模块表示一个执行器，它通过伸缩活塞将端口 **A** 处的液体压力转换为端口 **R** 处的机械力。活塞运动受硬止动模型限制。当内部计算活塞位置时，会在端口 **p** 报告该位置；当位置通过连接到 Simscape™ Multibody™ 关节设置时，会在端口 **p** 作为物理信号接收该位置。

可以修改 **Initial piston displacement**、**Enable dynamic compressibility** 和参考环境压力。不对流体惯性和机械惯性建模。

### 位移

活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**Mechanical orientation** 标识活塞位移的方向。当腔室体积等于 **Dead volume** 时，活塞位移为中性，或 `0`。当位移作为输入接收时，确保位置的导数等于活塞速度。当输入来自 Translational Multibody Interface 模块与 Simscape Multibody 关节的连接时，会自动满足此条件。

### 硬止动模型

有四种模型可用于对执行器活塞的伸出限位建模。此模块使用与 Translational Hard Stop 模块类似的公式，并对活塞行程两端的均匀阻尼和刚度系数建模。有关硬止动模型选项的详细信息，请参见 Translational Hard Stop 模块。

当活塞处于其上限或下限时会建模硬止动力。边界区域在 **Piston stroke** 或 **Piston initial displacement** 的 **Transition region** 内。在此区域之外，FHardStop=0。

### 缓冲

该模块可对活塞行程两端极限位置附近的缓冲进行建模。选择 **Cylinder end cushioning** 可在活塞运动接近由 **Piston stroke** 参数定义的最大伸出位置时减慢活塞运动。有关气缸缓冲功能的详细信息，参见 Cylinder Cushion (IL) 模块。

### 摩擦

该模块可对阻碍活塞运动的摩擦进行建模。选择 **Cylinder friction** 时，所得摩擦是 Stribeck、Coulomb 和黏性效应的组合。该模块测量腔室压力与环境压力之间的压力差。有关摩擦模型及其限制的详细信息，参见 Cylinder Friction (IL) 模块。

### 泄漏

您可以选择性地对液体腔与活塞储液腔之间的泄漏进行建模。当您选择 **Leakage** 时，会在活塞与气缸之间对泊肃叶流进行建模。该模块使用 Simscape Foundation Library 的 Laminar Leakage (IL) 模块。流量计算如下：

m˙=π128(d04−di4−(d02−di2)2log(d0/di))υL(pA−penv),

其中：

- *ν* 是流体运动黏度。
- *L* 是活塞长度，**p** – *P*0。
- *p*A 是端口 **A** 处的压力。
- *p*env 是环境压力，其在 **Environment pressure specification** 参数中选择。

气缸直径 *d*0 为 d0=di+2c，其中 *c* 是 **Piston-cylinder clearance**，而活塞直径 *d*i 为 di=4APπ，其中 *A*P 是 **Piston cross-sectional area**。

### 数值平滑的面积和压力

您可以通过调整 **Smoothing factor** 参数来在仿真中保持数值稳健性。如果 **Smoothing factor** 参数非零，则该模块会平滑缓冲孔口面积和单向阀压力范围。孔口面积在 **Leakage area between plunger and cushion sleeve** 和 **Cushion plunger cross-sectional area** 参数之间平滑饱和，而阀压力在 **Check valve cracking pressure differential** 和 **Check valve maximum pressure differential** 参数之间饱和。有关详细信息，参见数值平滑。

### 模块子组件

Single-Acting Actuator (IL) 模块由四个 Simscape Foundation 模块和两个 Fluids Library 模块组成：

- Translational Hard Stop
- Laminar Leakage (IL)
- Translational Mechanical Converter (IL)
- Ideal Translational Motion Sensor
- Cylinder Cushion (IL)
- Cylinder Friction (IL)

**执行器结构图**
