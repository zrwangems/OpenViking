---
type: simulink-block
title: 'Cylinder Cushion (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'cylindercushionil'
documentation_source_path: 'ref/cylindercushionil.html'
language: zh-CN
chinese_source: worker-translation
---

# Cylinder Cushion (IL)

## 端口

### 守恒端口

### **A** — 液体入口等温液体

与缓冲腔液体入口相关联的等温液体守恒端口。

### **B** — 液体出口等温液体

与缓冲腔液体出口相关联的等温液体守恒端口。

### **R** — 活塞杆机械平移

与活塞柱塞速度和力相关联的机械平移守恒端口。

### **C** — 壳体机械平移

与气缸参考结构相关联的机械平移守恒端口。

## 参数

### 缓冲柱塞

### **Cushion plunger cross-sectional area** — 缓冲柱塞横截面积 `1e-4 m^2`（默认）| 正标量

缓冲柱塞的横截面积。该面积为 πDplunger2/4，其中 *Dplunger* 为圆形柱塞的直径。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3 m`（默认）| 正标量

缓冲柱塞的长度。

### **Initial actuator piston displacement** — 连接活塞的初始位移 `0 m`（默认）| 标量

仿真开始时活塞在气缸中的位移。该位移决定了可变节流口的初始面积，该节流口用于模拟柱塞与端盖之间的可变间隙。

#### 依赖关系

如果 **Actuator mechanical orientation** 模块参数设置为 `Pressure at A causes positive displacement of R relative to C`，则活塞初始位移的值必须为正或零。

如果 **Actuator mechanical orientation** 模块参数设置为 `Pressure at A causes negative displacement of R relative to C`，则活塞初始位移的值必须为负或零。

### **Actuator mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

所连接执行器模块的活塞位移方向。如果该参数设置为 `Pressure at A causes positive displacement of R relative to C`，则当 **R** – **C** 为正时活塞伸出。如果该参数设置为 `Pressure at A causes negative displacement of R relative to C`，则当 **R** – **C** 为正时活塞缩回。

### 阀

### **Cushion orifice area** — 缓冲阀节流口面积 `1e-6 m^2`（默认）| 正标量

流体流经的阀的恒定节流口面积。当柱塞位于端盖开口内时，流体从气缸腔流向端盖腔。

### **Leakage area between plunger and cushion sleeve** — 柱塞位于端盖开口内时的总泄漏面积 `1e-7 m^2`（默认）| 正标量

当柱塞位于端盖开口或缓冲套内时可能泄漏的总面积。当活塞位移小于或等于 **Cushion plunger length** 参数的值时，用于模拟柱塞与缓冲套之间间隙的可变节流口面积等于该参数的值。

### **Check valve cracking pressure differential** — 单向阀开始开启时的压差 `0.01 MPa`（默认）| 正标量

单向阀开始开启时阀两端的最小压差。单向阀允许液体从缓冲腔自由流向活塞腔，但不允许反向流动。

### **Check valve maximum pressure differential** — 单向阀完全开启所需的压差 `0.1 MPa`（默认）| 正标量

单向阀完全开启时阀两端所需的压差。该参数的值必须大于 **Check valve cracking pressure differential** 参数。单向阀允许液体从缓冲腔自由流向活塞腔，但不允许反向流动。

### **Check valve maximum area** — 单向阀完全开启时的开口面积 `1e-4 m^2`（默认）| 正标量

单向阀完全开启时的通流面积。

### **Check valve leakage area** — 单向阀完全关闭时的总泄漏面积 `1e-10 m^2`（默认）| 正标量

单向阀完全关闭时可能泄漏的总面积。

### **Smoothing factor** — 应用于单向阀和可变节流口开口面积函数的平滑量 `0.01`（默认）| 正标量

连续平滑因子，在阀接近开启或接近关闭位置时为流量响应引入一层渐变。将该值设置为小于 1 的非零值，以提高仿真在这些工况下的稳定性。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators / Auxiliary Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中的气缸缓冲

Cylinder Cushion (IL) 模块用于对等温液体网络中的气缸缓冲进行建模。缓冲通过限制离开气缸腔的流量，在气缸杆接近行程末端时使其减速。下图显示了典型的气缸缓冲设计 [1]。

气缸缓冲示意图

当活塞向端盖（图中左侧）移动时，缓冲套（即柱塞）进入端盖中的腔室，并对离开气缸腔的流体产生额外阻力。当柱塞进入端盖开口并关闭主流体出口时，活塞开始减速。在此状态下，流体通过气缸与端盖之间间隙中的单向阀流动。该阀限制离开气缸腔的流量，并降低活塞的初始速度。

气缸缓冲由可变节流口、局部阻力和单向阀组成。可变节流口提供柱塞与端盖腔之间的可变开口。局部阻力连接活塞腔与缓冲腔。单向阀仅在活塞缩回期间提供缓冲腔与活塞腔之间的流动路径。

Cylinder Cushion (IL) 模块是由以下模块组成的复合组件：

- 一个 Local Restriction (IL) 模块，用于对缓冲阀进行建模。
- 一个 Check Valve (IL) 模块，用于对单向阀进行建模。
- 一个 Orifice (IL) 模块，用于对柱塞与端盖之间的可变间隙进行建模。
- 一个 Ideal Translational Motion Sensor 模块，用于将柱塞与端盖腔之间的间距转换为物理信号。该信号控制 Orifice (IL) 模块的开口。

您可以使用 Cylinder Cushion (IL) 模块对执行器进行建模。单作用或双作用执行器可以包含气缸缓冲，以在行程末端附近减慢活塞运动。气缸缓冲可防止活塞被端盖停止时产生极端冲击。

端口 **A** 和 **B** 分别是与腔室入口和出口相关联的等温液体守恒端口。端口 **R** 是与活塞柱塞连接的机械平移守恒端口。端口 **C** 是对应于气缸夹紧结构的机械平移守恒端口。该模块对从端口 **B** 到端口 **A** 的流量进行缓冲。模块中的单向阀方向为从端口 **A** 到端口 **B**。

### 可变节流口面积

在可变节流口中，模块假设当柱塞远离缓冲时，节流口面积完全打开并等于 πDplunger2/4，其中 *Dplunger* 为圆形柱塞的直径。当柱塞位于缓冲中时，节流口完全关闭，节流口面积等于泄漏面积。当柱塞向缓冲移动时，流体通过柱塞与端盖开口之间的间隙从气缸腔径向流向端盖腔。模块假设节流口面积在最大面积与泄漏面积之间随活塞位移线性变化。给定活塞位置下的节流口面积为

S={Sleak,εxpiston≤LplungerSmax,εxpiston≥Lplunger+Dplunger4Smax−SleakDplunger4(εxpiston−Lplunger)+Sleak,Lplunger<εxpiston<Lplunger+Dplunger4

其中：

- *S* 是给定活塞位置下的节流口面积。
- *Sleak* 是 **Leakage area between plunger and cushion sleeve** 参数的值。
- *Smax* 是节流口的最大尺寸，等于 **Cushion plunger cross-sectional area** 参数的值。
- *xpiston* 是活塞的位移。活塞的初始位移 *x0,piston* 是 **Actuator piston initial displacement** 参数的值。
- 当 **Actuator mechanical orientation** 参数为 `Pressure at A causes positive displacement of R relative to C` 时，*ε* 为 `1`；当 **Actuator mechanical orientation** 参数为 `Pressure at A causes negative displacement of R relative to C` 时，*ε* 为 `-1`。
- *Lplunger* 是 **Cushion plunger length** 参数的值。
- *Dplunger* 是 **Cushion plunger diameter** 参数的值。

### 数值平滑面积与压力

您可以通过调整 **Smoothing factor** 参数来保持仿真的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会对节流口面积和单向阀压力范围进行平滑。模块在 **Leakage area between plunger and cushion sleeve** 和 **Cushion plunger cross-sectional area** 参数之间平滑地饱和节流口面积。阀压力在 **Check valve cracking pressure differential** 和 **Check valve maximum pressure differential** 参数之间饱和。有关详细信息，请参阅 Numerical Smoothing。
