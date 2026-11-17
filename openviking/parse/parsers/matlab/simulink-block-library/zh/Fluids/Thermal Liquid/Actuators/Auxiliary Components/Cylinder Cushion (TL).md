---
type: simulink-block
title: 'Cylinder Cushion (TL)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 进液口 热液体
  direction: unspecified
- name: B
  summary: 出液口 热液体
  direction: unspecified
- name: R
  summary: 活塞杆 机械平动
  direction: unspecified
- name: C
  summary: 缸体 机械平动
  direction: unspecified
```

### 守恒

### **A** — 进液口 热液体

与通向缓冲腔的进液口相关联的热液体守恒端口。

### **B** — 出液口 热液体

与缓冲腔的出液口相关联的热液体守恒端口。

### **R** — 活塞杆 机械平动

与活塞柱塞速度和力相关联的机械平动守恒端口。

### **C** — 缸体 机械平动

与液压缸参考结构相关联的机械平动守恒端口。
## 参数
```yaml
parameters:
- name: 缓冲柱塞横截面积
  summary: 缓冲柱塞的横截面积 1e-4 m^2（默认） | 正标量
  group: 缓冲柱塞
- name: 缓冲柱塞长度
  summary: 缓冲柱塞的长度 1e-3 m（默认） | 正标量
  group: 缓冲柱塞
- name: 执行器活塞初始位移
  summary: 所连接活塞的初始位移 0 m（默认） | 标量
  group: 缓冲柱塞
- name: 执行器机械方向
  summary: 活塞位移方向 Pressure at A causes positive displacement of R relative to C（默认值）| Pressure at A causes negative displacement
    of R relative to C
  group: 缓冲柱塞
- name: 活塞横截面积
  summary: 活塞的横截面积 0.01 m^2（默认值）| 正标量
  group: 缓冲柱塞
- name: 缓冲节流孔面积
  summary: 缓冲阀的节流孔面积 1e-6 m^2（默认值）| 正标量
  group: 阀
- name: 柱塞与缓冲套筒之间的泄漏面积
  summary: 柱塞位于端盖开口内时的总泄漏面积 1e-7 m^2（默认值）| 正标量
  group: 阀
- name: 单向阀开启压差
  summary: 单向阀开始开启时的压差 0.01 MPa（默认值） | 正标量
  group: 阀
- name: 单向阀最大压差
  summary: 完全打开单向阀所需的压差 0.1 MPa（默认值） | 正标量
  group: 阀
- name: 单向阀最大面积
  summary: 单向阀完全打开时的开口面积 1e-4 m^2（默认值） | 正标量
  group: 阀
- name: 单向阀泄漏面积
  summary: 单向阀完全关闭时的总泄漏面积 1e-10 m^2（默认值） | 正标量
  group: 阀
- name: 平滑因子
  summary: 应用于单向阀和可变孔口开口面积函数的平滑量 0.01（默认值） | 正标量
  group: 阀
```

### 缓冲柱塞

### **缓冲柱塞横截面积** — 缓冲柱塞的横截面积 `1e-4 m^2`（默认） | 正标量

缓冲柱塞横截面的面积。该面积为 πDplunger2/4，其中 *Dplunger* 是圆形柱塞的直径。

### **缓冲柱塞长度** — 缓冲柱塞的长度 `1e-3 m`（默认） | 正标量

缓冲柱塞的长度。

### **执行器活塞初始位移** — 所连接活塞的初始位移 `0 m`（默认） | 标量

仿真开始时液压缸内活塞的位移。此位移决定可变节流孔的初始面积，该可变节流孔用于对柱塞与端盖之间的可变间隙进行建模。

如果 **执行器机械方向** 参数为 `Pressure at A causes positive displacement of R relative to C`，则 **执行器活塞初始位移** 参数的值必须为正数或零。

如果 **执行器机械方向** 参数为 `Pressure at A causes negative displacement of R relative to C`，则 **执行器活塞初始位移** 参数的值必须为负数或零。

### **执行器机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认值）| `Pressure at A causes negative displacement of R relative to C`

所连接执行器模块的活塞位移方向。如果此参数为
`Pressure at A causes positive displacement of R
relative to C`，则当端口 **R** 处的信号值减去端口 **C** 处的信号值所得结果为正时，活塞伸出。如果此参数为
`Pressure at A causes negative displacement of R
relative to C`，则当端口 **R** 处的信号值减去端口 **C** 处的信号值所得结果为正时，活塞缩回。

### **活塞横截面积** — 活塞的横截面积 `0.01 m^2`（默认值）| 正标量

液压缸活塞的横截面积。

### 阀

### **缓冲节流孔面积** — 缓冲阀的节流孔面积 `1e-6 m^2`（默认值）| 正标量

该阀中供流体流经的节流孔的恒定面积。当柱塞位于端盖开口内时，流体从液压缸腔流向端盖腔。

### **柱塞与缓冲套筒之间的泄漏面积** — 柱塞位于端盖开口内时的总泄漏面积 `1e-7 m^2`（默认值）| 正标量

当柱塞位于端盖开口或缓冲套筒内时，可能泄漏区域的总面积。当活塞位移小于或等于**缓冲柱塞长度**参数的值时，用于对柱塞与缓冲套筒之间的间隙进行建模的可变节流孔的面积等于此参数的值。

### **单向阀开启压差** — 单向阀开始开启时的压差 `0.01 MPa`（默认值） | 正标量

单向阀开始开启时，该阀两端所需的最小压差。
单向阀允许液体从缓冲腔自由流向活塞腔，但不允许液体沿相反方向流动。

### **单向阀最大压差** — 完全打开单向阀所需的压差 `0.1 MPa`（默认值） | 正标量

完全打开单向阀所需的阀两端压差。此参数的值必须大于**单向阀开启压差**参数。单向阀允许液体从缓冲腔自由流向活塞腔，但不允许液体沿相反方向流动。

### **单向阀最大面积** — 单向阀完全打开时的开口面积 `1e-4 m^2`（默认值） | 正标量

单向阀完全打开时的通流面积。

### **单向阀泄漏面积** — 单向阀完全关闭时的总泄漏面积 `1e-10 m^2`（默认值） | 正标量

单向阀完全关闭时所有可能泄漏的总面积。

### **平滑因子** — 应用于单向阀和可变孔口开口面积函数的平滑量 `0.01`（默认值） | 正标量

连续平滑因子，在阀处于接近全开或接近全关位置时，为流量响应引入渐进变化。将此值设置为小于 1 的非零值，以提高仿真在这些工况下的稳定性。
## 所属库

Simscape / Fluids / Thermal Liquid / Actuators / Auxiliary Components

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中推出**

## 描述

热液网络中的液压缸缓冲装置

Cylinder Cushion (TL) 模块对热液网络中的液压缸缓冲装置进行建模。当活塞杆接近行程末端时，该缓冲装置通过限制流出液压缸腔室的流量来使活塞杆减速。下图显示了一种典型的液压缸缓冲装置设计 [1]。

液压缸缓冲装置示意图

当活塞向端盖（图中左侧）移动时，缓冲衬套（或称柱塞）进入端盖内的腔室，并对流出液压缸腔室的流体产生附加阻力。当柱塞进入端盖中的开口并关闭主流体出口时，活塞开始减速。在此状态下，流体流经位于液压缸与端盖之间间隙中的单向阀。该阀限制流出液压缸腔室的流量，并降低活塞的初始速度。

液压缸缓冲装置由可变节流孔、局部节流件和单向阀组合而成。可变节流孔在柱塞与端盖空腔之间提供可变开口。局部节流件将活塞腔连接到缓冲腔。单向阀仅在活塞回缩期间提供缓冲腔与活塞腔之间的流路。

Cylinder Cushion (TL) 模块是由以下模块组成的复合组件：

- 一个 Local Restriction (TL)
  模块，用于对缓冲阀建模。
- 一个 Check Valve (TL) 模块，用于对单向阀建模。
- 一个 Orifice (TL) 模块，用于对柱塞与端盖之间的可变间隙建模。
- 一个 Ideal Translational Motion Sensor 模块，用于将柱塞与端盖内空腔之间的间距转换为物理信号。该信号控制 Orifice (TL) 模块的开度。

可以使用 Cylinder Cushion (TL) 模块对执行器进行建模。单作用或双作用执行器可以包含液压缸缓冲装置，以减缓活塞在行程末端附近的运动。当活塞被端盖挡住而停止时，液压缸缓冲装置可防止产生剧烈冲击。

端口 **A** 和 **B** 是分别与腔室入口和出口相关联的热液体守恒端口。端口 **R** 是与活塞柱塞相连的机械平动守恒端口。端口 **C** 是与液压缸夹紧结构对应的机械平动守恒端口。该模块对从端口 **B** 到端口 **A** 的流量进行缓冲。模块中的单向阀取向为从端口 **A** 到端口 **B**。

### 可变节流孔面积

在可变节流孔中，模块假设当柱塞远离缓冲装置时，节流孔完全打开，其面积等于 πDplunger2/4，其中 *Dplunger* 是圆形柱塞的直径。当柱塞位于缓冲装置内时，节流孔完全关闭，节流孔面积等于泄漏面积。随着柱塞向缓冲装置移动，流体通过柱塞与端盖开口之间的间隙，从缸筒腔径向流向端盖腔。模块假设，在最大面积与泄漏面积之间，节流孔面积随活塞位移线性变化。对于给定的活塞位置，节流孔面积为

S={Sleak,εxpiston≤LplungerSmax,εxpiston≥Lplunger+Dplunger4Smax−SleakDplunger4(εxpiston−Lplunger)+Sleak,Lplunger<εxpiston<Lplunger+Dplunger4

其中：

- *S* 是给定活塞位置下的节流孔面积。
- *Sleak* 是 **柱塞与缓冲套筒之间的泄漏面积** 参数的值。
- *Smax* 是节流孔的最大面积，其值等于 **缓冲柱塞横截面积** 参数的值。
- *xpiston* 是活塞的位移。活塞的初始位移 *x0,piston* 是 **执行器活塞初始位移** 参数的值。
- *ε* 在 **执行器机械方向** 参数为 `Pressure at A causes positive displacement of R relative to C` 时为 `1`，在 **执行器机械方向** 参数为 `Pressure at A causes negative displacement of R relative to C` 时为 `-1`。
- *Lplunger* 是 **缓冲柱塞长度** 参数的值。
- *Dplunger* 是 **缓冲柱塞直径** 参数的值。

### 数值平滑的面积和压力

您可以通过调整 **Smoothing factor** 参数来保持仿真的数值稳健性。如果 **Smoothing factor** 参数非零，模块会对节流孔面积和单向阀压力范围进行平滑处理。模块会使节流孔面积在 **Leakage area between plunger and cushion sleeve** 和 **Cushion plunger cross-sectional area** 参数之间平滑饱和。阀门压力在 **Check valve cracking pressure differential** 和 **Check valve maximum pressure differential** 参数之间进行饱和处理。有关详细信息，请参阅数值平滑。
