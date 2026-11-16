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

### 守恒

### **A** — 液体入口端口 等温液体

与缓冲腔的液体入口端口关联的等温液体守恒端口。

### **B** — 液体出口端口 等温液体

与缓冲腔的出口液体端口关联的等温液体守恒端口。

### **R** — 杆 机械平移

与活塞柱塞速度和力关联的机械平移守恒端口。

### **C** — 壳体 机械平移

与液压缸参考结构关联的机械平移守恒端口。

## 参数

### 缓冲柱塞

### **缓冲柱塞横截面积** — 缓冲柱塞的横截面积 `1e-4 m^2`（默认）| positive scalar

缓冲柱塞横截面的面积。该面积为 πDplunger2/4，其中 *Dplunger* 是圆形柱塞的直径。

### **缓冲柱塞长度** — 缓冲柱塞的长度 `1e-3 m`（默认）| positive scalar

缓冲柱塞的长度。

### **初始执行机构活塞位移** — 连接的活塞的初始位移 `0 m`（默认）| scalar

仿真开始时活塞在液压缸中的位移。此位移确定可变节流孔的初始面积，该节流孔对柱塞和端盖之间的可变间隙建模。

#### 依赖关系

如果 **执行机构机械方向** 模块参数设置为 `Pressure at A causes positive displacement of R relative to C`，则活塞初始位移的值必须为正或零。

如果 **执行机构机械方向** 模块参数设置为 `Pressure at A causes negative displacement of R relative to C`，则活塞初始位移的值必须为负或零。

### **执行机构机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

连接的执行机构模块的活塞位移方向。如果此参数设置为 `Pressure at A causes positive displacement of R relative to C`，则当 **R** – **C** 为正时活塞伸出。如果此参数设置为 `Pressure at A causes negative displacement of R relative to C`，则当 **R** – **C** 为正时活塞回缩。

### 阀

### **缓冲节流孔面积** — 缓冲阀的节流孔面积 `1e-6 m^2`（默认）| positive scalar

流体流经的阀的恒定节流孔面积。当柱塞位于端盖中的开口内时，流体从缸腔流向端盖腔。

### **柱塞与缓冲套之间的泄漏面积** — 柱塞位于端盖开口内时的总泄漏面积 `1e-7 m^2`（默认）| positive scalar

当柱塞位于端盖开口或缓冲套内时可能泄漏的总面积。当活塞的位移小于或等于 **缓冲柱塞长度** 参数的值时，对柱塞与缓冲套之间的间隙建模的可变节流孔面积等于此参数的值。

### **单向阀开启压力差** — 单向阀开始打开时的压力差 `0.01 MPa`（默认）| positive scalar

单向阀两端使阀开始打开的最小压力差。单向阀允许液体从缓冲腔自由流到活塞腔，但不允许沿相反方向流动。

### **单向阀最大压力差** — 完全打开单向阀所需的压力差 `0.1 MPa`（默认）| positive scalar

完全打开单向阀所需的单向阀两端压力差。此参数的值必须大于 **单向阀开启压力差** 参数。单向阀允许液体从缓冲腔自由流到活塞腔，但不允许沿相反方向流动。

### **单向阀最大面积** — 单向阀完全打开时的开口面积 `1e-4 m^2`（默认）| positive scalar

单向阀完全打开时的通道面积。

### **单向阀泄漏面积** — 单向阀完全关闭时的总泄漏面积 `1e-10 m^2`（默认）| positive scalar

单向阀完全关闭时可能泄漏的总面积。

### **平滑因子** — 应用于单向阀和可变节流孔开口面积函数的平滑量 `0.01`（默认）| positive scalar

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层逐渐变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators / Auxiliary Components

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中的液压缸缓冲

Cylinder Cushion (IL) 模块对等温液体网络中的液压缸缓冲建模。缓冲通过限制离开缸腔的流量，使液压缸杆在接近行程末端时减速。下面的图显示了一个典型的液压缸缓冲设计 [1]。

液压缸缓冲示意图

当活塞朝端盖（图中位于左侧）移动时，缓冲衬套（即柱塞）进入端盖中的腔体，并对离开缸腔的流体产生额外阻力。当柱塞进入端盖中的开口并关闭主流体出口时，活塞开始减速。在此状态下，流体通过液压缸与端盖之间间隙中的单向阀流动。该阀限制离开缸腔的流量，并降低活塞的初始速度。

液压缸缓冲由可变节流孔、局部阻力和单向阀组成。可变节流孔在柱塞和端盖腔之间提供可变开口。局部阻力连接活塞腔和缓冲腔。单向阀仅在活塞回缩期间提供缓冲腔和活塞腔之间的流动路径。

Cylinder Cushion (IL) 模块是由以下模块组成的复合组件：

- 一个 Local Restriction (IL) 模块，用于对缓冲阀建模。
- 一个 Check Valve (IL) 模块，用于对单向阀建模。
- 一个 Orifice (IL) 模块，用于对柱塞和端盖之间的可变间隙建模。
- 一个 Ideal Translational Motion Sensor 模块，用于将柱塞与端盖中腔体之间的间距转换为物理信号。此信号控制 Orifice (IL) 模块的开口。

您可以使用 Cylinder Cushion (IL) 模块对执行机构建模。单作用或双作用执行机构可以包含液压缸缓冲，以在行程末端附近减慢活塞运动。液压缸缓冲可防止活塞被端盖止动时发生极端冲击。

端口 **A** 和 **B** 是与腔体入口和出口分别关联的等温液体守恒端口。端口 **R** 是与活塞柱塞连接的机械平移守恒端口。端口 **C** 是对应于液压缸夹持结构的机械平移守恒端口。该模块缓冲从端口 **B** 到端口 **A** 的流量。该模块中的单向阀方向为从端口 **A** 到端口 **B**。

### 可变节流孔面积

在可变节流孔中，模块假设当柱塞远离缓冲时，节流孔面积完全打开并等于 πDplunger2/4，其中 *Dplunger* 是圆形柱塞的直径。当柱塞位于缓冲中时，节流孔完全关闭，节流孔面积等于泄漏面积。当柱塞朝缓冲移动时，流体通过柱塞与端盖开口之间的间隙，从缸腔径向流向端盖腔。模块假设节流孔面积在最大面积和泄漏面积之间随活塞位移线性变化。给定活塞位置下的节流孔面积为

S={Sleak,εxpiston≤LplungerSmax,εxpiston≥Lplunger+Dplunger4Smax−SleakDplunger4(εxpiston−Lplunger)+Sleak,Lplunger<εxpiston<Lplunger+Dplunger4

其中：

- *S* 是给定活塞位置下的节流孔面积。
- *Sleak* 是 **柱塞与缓冲套之间的泄漏面积** 参数的值。
- *Smax* 是节流孔的最大尺寸，等于 **缓冲柱塞横截面积** 参数的值。
- *xpiston* 是活塞的位移。活塞的初始位移 *x0,piston* 是 **执行机构活塞初始位移** 参数的值。
- 当 **执行机构机械方向** 参数为 `Pressure at A causes positive displacement of R relative to C` 时，*ε* 为 `1`；当 **执行机构机械方向** 参数为 `Pressure at A causes negative displacement of R relative to C` 时，*ε* 为 `-1`。
- *Lplunger* 是 **缓冲柱塞长度** 参数的值。
- *Dplunger* 是 **缓冲柱塞直径** 参数的值。

### 数值平滑的面积和压力

您可以通过调整 **平滑因子** 参数来保持仿真中的数值稳健性。如果 **平滑因子** 参数非零，该模块会平滑节流孔面积和单向阀压力范围。该模块将节流孔面积平滑饱和在 **柱塞与缓冲套之间的泄漏面积** 和 **缓冲柱塞横截面积** 参数之间。阀压力饱和在 **单向阀开启压力差** 和 **单向阀最大压力差** 参数之间。有关详细信息，请参阅数值平滑。
