---
type: simulink-block
title: 'Single-Acting Actuator (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Actuators'
documentation_page: 'singleactingactuatorma'
documentation_source_path: 'ref/singleactingactuatorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Single-Acting Actuator (MA)

## 端口

### 输入

### **p** — 多体活塞位置输入，m 物理信号

与活塞位置相关联的物理信号输入，单位为 m。
将此端口连接到 Simscape
Multibody™ 网络，使用 Translational Multibody
Interface 模块。

#### 依赖

要启用此端口，请将 **Piston displacement**
设置为 `Provide input signal from Multibody
joint`。
### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置相关联的物理信号输出，单位为
m。

#### 依赖

要启用此端口，请将 **Piston displacement**
设置为 `Calculate from velocity of port R relative to port
C`。
### 守恒

### **A** — 液体端口湿空气

与腔室 A 相关联的湿空气守恒端口。

### **C** — 执行器壳体平移机械

与执行器壳体相关联的平移机械守恒端口。

### **R** — 执行器活塞平移机械

与执行器活塞相关联的平移机械守恒端口。

### **H** — 传热热

与湿空气体积的热质量相关联的热守恒端口。

## 参数

### 执行器

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C`，当端口
  **A** 处湿空气体积膨胀时，活塞位移
  为正。此运动
  对应于活塞杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C`，当端口
  **A** 处湿空气体积膨胀时，活塞位移
  为负。此运动
  对应于活塞杆缩回。

### **Piston cross-sectional area** — 活塞杆横截面积 `0.01` `m^2`（默认）| 正标量

活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1` `m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume** — 活塞完全缩回时的流体体积 `1e-5` `m^3`（默认）| 正标量

活塞位移为
`0` 时的湿空气体积。此参数为
活塞抵靠执行器端盖时的湿空气体积。

### **Cross-sectional area at port A** — 端口 A 处的面积 `0.01 m^2`（默认）| 正标量

端口 **A** 的横截面积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。当您选择
`Atmospheric pressure` 时，该模块假定
压力为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325` `MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖

要启用此参数，请将 **Environment pressure
specification** 设置为 `Specified
pressure`。

### 硬限位

### **Hard stop model** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全缩回时使用的硬限位模型。有关更多
信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。当活塞的最大伸出或缩回
超出此范围时，该模块不应用硬限位模型。在这种
情况下，活塞上没有
附加力。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位器之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹回后滑块与限位器之间最终相对速度与初始相对速度
之比。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位器之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位器之间的阈值相对速度。
当滑块以小于 **Static contact speed threshold** 参数值的
速度撞击壳体时，它们
保持接触。否则，滑块弹回。为避免对滑块与壳体之间的静态
接触进行建模，请将此参数设置为
`0`。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### 初始条件

### **Piston displacement** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input
signal from Multibody joint` 时，该模块可以从 Multibody 模块接收
位置，或者可以在内部计算
位置并在端口
**p** 处报告位置。当机械方向为正时，位置介于 `0`
和 **Piston stroke** 参数值之间；当机械方向为负时，位置介于 `0`
和 **Piston stroke**
参数的负值之间。

### **Initial piston displacement** — 仿真开始时的活塞位置 `0` `m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖

要启用此参数，请将 **Piston
displacement** 设置为 `Calculate from velocity
of port R relative to port C`。

### **Initial moist air pressure** — 仿真开始时的湿空气压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时的湿空气压力。

### **Initial moist air temperature** — 仿真开始时的湿空气温度 `293.15` `K`（默认）| 标量

仿真开始时的湿空气温度。

### **Initial humidity specification** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或
湿度比来描述初始湿空气湿度水平。

### **Initial moist air relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

仿真开始时的湿空气相对湿度。

#### 依赖

要启用此参数，请将 **Initial humidity
specification** 设置为 `Relative
humidity`。

### **Initial moist air specific humidity** — 仿真开始时的比湿度 `0.01`（默认）| [0,1] 范围内的标量

仿真开始时湿空气的比湿度，定义为湿空气混合物中水蒸气的
质量分数。

#### 依赖

要启用此参数，请将 **Initial humidity
specification** 设置为 `Specific
humidity`。

### **Initial moist air water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

仿真开始时湿空气混合物中水蒸气的
摩尔分数。

#### 依赖

要启用此参数，请将 **Initial humidity
specification** 设置为 `Mole
fraction`。

### **Initial moist air humidity ratio** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的标量

仿真开始时湿空气的湿度比，定义为水蒸气与
干空气和痕量气体的质量比。

#### 依赖

要启用此参数，请将 **Initial humidity
specification** 设置为 `Humidity
ratio`。

### **Initial moist air wet-bulb temperature** — 仿真开始时的湿球温度 `287` `K`（默认）| 正标量

仿真开始时湿空气混合物的湿球温度。

#### 依赖

要启用此参数，请将 **Initial humidity
specification** 设置为 `Wet-bulb
temperature`。

### **Initial trace gas specification** — 用于描述初始痕量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数来描述仿真开始时的
痕量气体水平。

### **Initial trace gas mass fraction** — 仿真开始时痕量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量

仿真开始时湿空气混合物中痕量气体的
质量分数。

#### 依赖

要启用此参数，请将 **Initial trace gas
specification** 设置为 `Mass
fraction`。

### **Initial trace gas mole fraction** — 仿真开始时痕量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

仿真开始时湿空气混合物中痕量气体的
摩尔分数。

#### 依赖

要启用此参数，请将 **Initial trace gas
specification** 设置为 `Mole
fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气之比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

### **Relative humidity at saturation** — 发生冷凝时的相对湿度阈值 `1`（默认）| 正标量

腔室中发生冷凝时的相对湿度阈值。

### **Water vapor condensation time constant** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝出多余湿度而恢复到
饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为
蒸气的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的分数 `1`（默认）| [0,1] 范围内的标量

湿空气中作为水滴夹带的冷凝物
分数。

## 所属库

Simscape / Fluids / Moist Air / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴
进行建模，请在连接到湿空气网络的 Moist Air Properties
(MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的单作用线性执行器

Single-Acting Actuator (MA) 模块对由单个湿空气腔室控制活塞的线性
执行器进行建模。该执行器在
伸出和缩回行程中产生力，但驱动力取决于
腔室中的表压。

该图显示了执行器的关键组件。端口 **A**
表示湿空气腔室入口，端口 **R** 表示
平移执行器活塞，端口 **C** 表示执行器
壳体。端口 **H** 表示湿空气
腔室与环境之间的热接口。

单作用执行器示意图

### 位移

该模块将活塞位移测量为端口
**R** 相对于端口 **C** 的位置。**Mechanical orientation** 参数标识活塞位移的
方向。当腔室体积等于 **Dead
volume** 参数值时，活塞位移为中性，即 `0`。
当 **Piston displacement**
参数为 `Provide input signal from Multibody joint` 时，
您使用端口 **p** 输入活塞位移。您可以通过使用
Translational Multibody Interface 模块
提供活塞位移，来确保位置信号的导数等于活塞速度。

活塞运动的方向取决于 **Mechanical
orientation** 参数。如果机械方向为正，
则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平移
为正。当机械方向为负时，运动方向
反转。

### 硬限位

一组硬限位限制活塞的运动范围。该模块使用
Translational Hard Stop 模块的实现，将硬限位视为
弹簧-阻尼器系统。弹簧刚度系数控制硬限位接触力的恢复
分量，阻尼系数控制耗散
分量。

硬限位位于活塞行程的远端。如果
机械方向为正，则下限位在 *x* = 0 处，上限位在 *x* = +*stroke* 处。如果机械方向为负，则下限位
在 *x* = -*stroke* 处，上限位在 *x* = 0 处。

### 模块组合

此模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter (MA)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor

构成该模块的元件图。
