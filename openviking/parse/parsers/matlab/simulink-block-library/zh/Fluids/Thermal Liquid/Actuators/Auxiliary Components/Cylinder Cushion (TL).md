---
type: simulink-block
title: 'Cylinder Cushion (TL)'
family: 'thermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'cylindercushiontl'
documentation_source_path: 'ref/cylindercushiontl.html'
language: zh-CN
chinese_source: worker-translation
---

# Cylinder Cushion (TL)

## 端口

### 守恒

### **A** — 液体入口端口 热液体

与缓冲腔的液体入口端口关联的热液体守恒端口。

### **B** — 液体出口端口 热液体

与缓冲腔的出口液体端口关联的热液体守恒端口。

### **R** — 杆机械平动

与活塞柱塞速度和力关联的机械平动守恒端口。

### **C** — 壳体机械平动

与缸参考结构关联的机械平动守恒端口。

## 参数

### 缓冲柱塞

### **缓冲柱塞横截面积** — 缓冲柱塞的横截面积 `1e-4 m^2`（默认） | 正标量

缓冲柱塞的横截面积。该面积为 πDplunger2/4，其中 *Dplunger* 是圆形柱塞的直径。

### **缓冲柱塞长度** — 缓冲柱塞的长度 `1e-3 m`（默认） | 正标量

缓冲柱塞的长度。

### **初始执行机构活塞位移** — 相连活塞的初始位移 `0 m`（默认） | 标量

仿真开始时缸内活塞的位移。该位移确定可变孔口的初始面积，该孔口用于对柱塞与端盖之间的可变间隙进行建模。

如果 **执行机构机械方向** 参数为 `Pressure at A causes positive displacement of R relative to C`，则 **执行机构活塞初始位移** 参数的值必须为正或零。

如果 **执行机构机械方向** 参数为 `Pressure at A causes negative displacement of R relative to C`，则 **执行机构活塞初始位移** 参数的值必须为负或零。

### **执行机构机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认） | `Pressure at A causes negative displacement of R relative to C`

相连执行机构模块的活塞位移方向。如果该参数为 `Pressure at A causes positive displacement of R relative to C`，则当端口 **R** 处的信号值减去端口 **C** 处的信号值为正时，活塞伸出。如果该参数为 `Pressure at A causes negative displacement of R relative to C`，则当端口 **R** 处的信号值减去端口 **C** 处的信号值为正时，活塞回缩。

### **活塞横截面积** — 活塞的横截面积 `0.01 m^2`（默认） | 正标量

缸活塞的横截面积。

### 阀

### **缓冲孔口面积** — 缓冲阀的孔口面积 `1e-6 m^2`（默认） | 正标量

流体流经的阀的恒定孔口面积。当柱塞位于端盖内的开口中时，流体从缸腔流向端盖腔。

### **柱塞与缓冲套之间的泄漏面积** — 柱塞位于端盖开口内时的总泄漏面积 `1e-7 m^2`（默认） | 正标量

当柱塞位于端盖开口或缓冲套内时可能泄漏的总面积。当活塞位移小于或等于 **缓冲柱塞长度** 参数的值时，用于对柱塞与缓冲套之间间隙进行建模的可变孔口面积等于该参数的值。

### **单向阀开启压差** — 单向阀开始打开时的压差 `0.01 MPa`（默认） | 正标量

单向阀两端使阀开始打开的最小压差。单向阀允许液体从缓冲腔自由流向活塞腔，但不允许沿相反方向流动。

### **单向阀最大压差** — 使单向阀完全打开所需的压差 `0.1 MPa`（默认） | 正标量

使阀完全打开所需的单向阀两端压差。该参数的值必须大于 **单向阀开启压差** 参数。单向阀允许液体从缓冲腔自由流向活塞腔，但不允许沿相反方向流动。

### **单向阀最大面积** — 单向阀完全打开时的开口面积 `1e-4 m^2`（默认） | 正标量

阀完全打开时单向阀的通道面积。

### **单向阀泄漏面积** — 单向阀完全关闭时的总泄漏面积 `1e-10 m^2`（默认） | 正标量

单向阀完全关闭时可能泄漏的总面积。

### **平滑因子** — 应用于单向阀和可变孔口开口面积函数的平滑量 `0.01`（默认） | 正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，该因子为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高仿真在这些工况下的稳定性。

## 所属库

Simscape / Fluids / Thermal Liquid / Actuators / Auxiliary Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

热液体网络中的缸缓冲

Cylinder Cushion (TL) 模块对热液体网络中的缸缓冲进行建模。缓冲通过限制离开缸腔的流量，在缸杆接近行程末端时使其减速。下图显示了典型的缸缓冲设计 [1]。

缸缓冲示意图

当活塞朝端盖（图中左侧）移动时，缓冲衬套（即柱塞）进入端盖中的腔室，并对离开缸腔的流体产生附加阻力。当柱塞进入端盖开口并关闭主流体出口时，活塞开始减速。在此状态下，流体通过缸与端盖之间间隙中的单向阀流动。该阀限制离开缸腔的流量，并降低活塞的初始速度。

缸缓冲由可变孔口、局部阻力和单向阀组成。可变孔口提供柱塞与端盖腔之间的可变开口。局部阻力连接活塞腔与缓冲腔。单向阀仅在活塞回缩期间提供缓冲腔与活塞腔之间的流路。

Cylinder Cushion (TL) 模块是由以下模块组成的复合组件：

- 一个 Local Restriction (TL) 模块，用于对缓冲阀进行建模。
- 一个 Check Valve (TL) 模块，用于对单向阀进行建模。
- 一个 Orifice (TL) 模块，用于对柱塞与端盖之间的可变间隙进行建模。
- 一个 Ideal Translational Motion Sensor 模块，用于将柱塞与端盖中腔体之间的间距转换为物理信号。该信号控制 Orifice (TL) 模块的开口。

您可以使用 Cylinder Cushion (TL) 模块对执行机构进行建模。单作用或双作用执行机构可包含缸缓冲，以在行程末端附近减慢活塞运动。当活塞被端盖止动时，缸缓冲可防止极端冲击。

端口 **A** 和 **B** 是分别与腔入口和出口关联的热液体守恒端口。端口 **R** 是与活塞柱塞相连的机械平动守恒端口。端口 **C** 是对应于缸夹紧结构的机械平动守恒端口。该模块对从端口 **B** 到端口 **A** 的流量进行缓冲。该模块中的单向阀方向为从端口 **A** 到端口 **B**。

### 可变孔口面积

在可变孔口中，模块假设当柱塞远离缓冲时，孔口面积完全打开并等于 πDplunger2/4，其中 *Dplunger* 是圆形柱塞的直径。当柱塞位于缓冲中时，孔口完全关闭，孔口面积等于泄漏面积。当柱塞朝缓冲移动时，流体通过柱塞与端盖开口之间的间隙从缸腔径向流向端盖腔。模块假设孔口面积在最大面积与泄漏面积之间随活塞位移线性变化。给定活塞位置时的孔口面积为

S={Sleak,εxpiston≤LplungerSmax,εxpiston≥Lplunger+Dplunger4Smax−SleakDplunger4(εxpiston−Lplunger)+Sleak,Lplunger<εxpiston<Lplunger+Dplunger4

其中：

- *S* 是给定活塞位置时的孔口面积。
- *Sleak* 是 **柱塞与缓冲套之间的泄漏面积** 参数的值。
- *Smax* 是孔口最大尺寸，等于 **缓冲柱塞横截面积** 参数的值。
- *xpiston* 是活塞的位移。活塞的初始位移 *x0,piston* 是 **执行机构活塞初始位移** 参数的值。
- 当 **执行机构机械方向** 参数为 `Pressure at A causes positive displacement of R relative to C` 时，*ε* 为 `1`；当 **执行机构机械方向** 参数为 `Pressure at A causes negative displacement of R relative to C` 时，*ε* 为 `-1`。
- *Lplunger* 是 **缓冲柱塞长度** 参数的值。
- *Dplunger* 是 **缓冲柱塞直径** 参数的值。

### 数值平滑后的面积和压力

您可以通过调整 **平滑因子** 参数来保持仿真的数值稳健性。如果 **平滑因子** 参数非零，模块会平滑孔口面积和单向阀压力范围。模块在 **柱塞与缓冲套之间的泄漏面积** 和 **缓冲柱塞横截面积** 参数之间对孔口面积进行平滑饱和。阀压力在 **单向阀开启压差** 和 **单向阀最大压差** 参数之间饱和。有关详细信息，请参阅数值平滑。
