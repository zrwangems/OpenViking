---
type: simulink-block
title: 'Single-Acting Actuator (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Actuators'
documentation_page: 'singleactingactuatorma'
documentation_source_path: 'ref/singleactingactuatorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Single-Acting Actuator (MA)

## 端口

### 输入

### **p** — Multibody 活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入，单位为 m。
使用 Translational Multibody Interface 模块将此端口连接到 Simscape Multibody™ 网络。

#### 依赖项

要启用此端口，请将 **活塞位移** 设置为 `Provide input signal from Multibody
joint`。

### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置关联的物理信号输出，单位为 m。

#### 依赖项

要启用此端口，请将 **活塞位移** 设置为 `Calculate from velocity of port R relative to port
C`。

### 守恒

### **A** — 湿空气液体端口

与腔室 A 关联的湿空气守恒端口。

### **C** — 执行器壳体平移机械

与执行器壳体关联的平移机械守恒端口。

### **R** — 执行器活塞平移机械

与执行器活塞关联的平移机械守恒端口。

### **H** — 热传递热

与湿空气体积热质量关联的热守恒端口。

## 参数

### 执行器

### **机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认） | `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C`，当端口 **A** 处湿空气体积膨胀时，活塞位移为正。此运动对应杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C`，当端口 **A** 处湿空气体积膨胀时，活塞位移为负。此运动对应杆缩回。

### **活塞横截面积** — 活塞杆横截面积 `0.01` `m^2`（默认） | 正标量

活塞杆的横截面积。

### **活塞行程** — 最大活塞行进距离 `0.1` `m`（默认） | 正标量

最大活塞行进距离。

### **死区容积** — 活塞完全缩回时的流体体积 `1e-5` `m^3`（默认） | 正标量

活塞位移为 `0` 时的湿空气体积。此参数为活塞抵靠执行器端盖时的湿空气体积。

### **端口 A 处横截面积** — 端口 A 处面积 `0.01 m^2`（默认） | 正标量

端口 **A** 的横截面积。

### **环境压力设定** — 参考环境压力 `Atmospheric pressure`（默认） | `Specified pressure`

环境参考压力。选择 `Atmospheric pressure` 时，模块假定压力为 0.101325 MPa。

### **环境压力** — 用户定义的环境压力 `0.101325` `MPa`（默认） | 正标量

用户定义的环境压力。

#### 依赖项

要启用此参数，请将 **环境压力设定** 设置为 `Specified
pressure`。

### 硬限位

### **硬限位模型** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认） | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全缩回时要使用的硬限位模型。有关详细信息，请参阅 Translational Hard Stop 模块。

### **硬限位刚度系数** — 刚度系数 `1e10` `N/m`（默认） | 正标量

活塞刚度系数。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **硬限位阻尼系数** — 阻尼系数 `150` `N*s/m`（默认） | 正标量

活塞阻尼系数。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **过渡区域** — 硬限位力模型的应用范围 `0.1` `mm`（默认） | 正标量

硬限位力模型的应用范围。当活塞的最大伸出或缩回超出此范围时，模块不应用硬限位模型。在这种情况下，活塞上没有附加力。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位件之间最终相对速度与初始相对速度之比 `0.7`（默认） | 介于 0 和 1 之间的无量纲值

滑块弹跳后，滑块与限位件之间最终相对速度与初始相对速度之比。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of
restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位件之间的阈值相对速度 `0.001 m/s`（默认） | 非负标量

碰撞前滑块与限位件之间的阈值相对速度。当滑块以小于 **静态接触速度阈值** 参数值的速度撞击外壳时，它们保持接触。否则，滑块弹跳。为避免对滑块与外壳之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of
restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的力 `0.001 N`（默认） | 正标量

释放滑块使其脱离静态接触模式所需的最小力。

#### 依赖项

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of
restitution`。

### 初始条件

### **活塞位移** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认） | `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input
signal from Multibody joint` 时，模块可以从 Multibody 模块接收位置；也可以内部计算位置，并在端口 **p** 报告位置。当机械方向为正时，位置介于 `0` 和 **活塞行程** 参数的值之间；当机械方向为负时，位置介于 `0` 和 **活塞行程** 参数的负值之间。

### **初始活塞位移** — 仿真开始时的活塞位置 `0` `m`（默认） | 标量

仿真开始时的活塞位置。

#### 依赖项

要启用此参数，请将 **活塞位移** 设置为 `Calculate from velocity
of port R relative to port C`。

### **初始湿空气压力** — 仿真开始时的湿空气压力 `0.101325` `MPa`（默认） | 正标量

仿真开始时的湿空气压力。

### **初始湿空气温度** — 仿真开始时的湿空气温度 `293.15` `K`（默认） | 标量

仿真开始时的湿空气温度。

### **初始湿度设定** — 用于描述初始湿度水平的量 `Relative humidity`（默认） | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述初始湿空气湿度水平。

### **初始湿空气相对湿度** — 仿真开始时的相对湿度 `0.5`（默认） | 范围 [0,1] 内的标量

仿真开始时的湿空气相对湿度。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Relative
humidity`。

### **初始湿空气比湿度** — 仿真开始时的比湿度 `0.01`（默认） | 范围 [0,1] 内的标量

仿真开始时的湿空气比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Specific
humidity`。

### **初始湿空气水蒸气摩尔分数** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认） | 范围 [0,1] 内的标量

仿真开始时湿空气混合物中水蒸气的摩尔分数。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Mole
fraction`。

### **初始湿空气湿度比** — 仿真开始时的湿度比 `0.01`（默认） | 范围 [0,1] 内的标量

仿真开始时的湿空气湿度比，定义为水蒸气与干空气和微量气体的质量比。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Humidity
ratio`。

### **初始湿空气湿球温度** — 仿真开始时的湿球温度 `287` `K`（默认） | 正标量

仿真开始时湿空气混合物的湿球温度。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Wet-bulb
temperature`。

### **初始微量气体设定** — 用于描述初始微量气体水平的量 `Mass fraction`（默认） | `Mole fraction`

是否使用质量分数或摩尔分数来描述仿真开始时的微量气体水平。

### **初始微量气体质量分数** — 仿真开始时微量气体的质量分数 `0.001`（默认） | 范围 [0,1] 内的标量

仿真开始时湿空气混合物中微量气体的质量分数。

#### 依赖项

要启用此参数，请将 **初始微量气体设定** 设置为 `Mass
fraction`。

### **初始微量气体摩尔分数** — 仿真开始时微量气体的摩尔分数 `0.001`（默认） | 范围 [0,1] 内的标量

仿真开始时湿空气混合物中微量气体的摩尔分数。

#### 依赖项

要启用此参数，请将 **初始微量气体设定** 设置为 `Mole
fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气之比 `0`（默认） | 正标量

水滴与湿空气的初始质量比。

### **饱和时的相对湿度** — 高于该值时发生冷凝的相对湿度 `1`（默认） | 正标量

高于该值时腔室中发生冷凝的相对湿度。

### **水蒸气冷凝时间常数** — 冷凝时间尺度 `1e-3 s`（默认） | 正标量

过饱和湿空气体积通过冷凝析出多余湿度而返回到饱和状态的特征时间尺度。

### **水滴蒸发时间常数** — 蒸发时间尺度 `1e-3 s`（默认） | 正标量

水滴蒸发为蒸气的特征时间尺度。

### **作为水滴夹带的冷凝物分数** — 水滴中冷凝物的分数 `1`（默认） | 范围 [0,1] 内的标量

湿空气中被夹带为水滴的冷凝物分数。

## 所属库

Simscape / Fluids / Moist Air / Actuators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **启用夹带水滴**。

## 描述

湿空气网络中的单作用线性执行器

Single-Acting Actuator (MA) 模块对具有由单个湿空气腔室控制的活塞的线性执行器建模。执行器在伸出和缩回行程中产生力，但致动力取决于腔室中的表压。

图中显示了执行器的关键组件。端口 **A** 表示湿空气腔室入口，端口 **R** 表示平移的执行器活塞，端口 **C** 表示执行器外壳。端口 **H** 表示湿空气腔室与环境之间的热接口。

Single-Acting Actuator 示意图

### 位移

模块将活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**机械方向** 参数标识活塞位移的方向。当腔室体积等于 **死区容积** 参数的值时，活塞位移为中性，即 `0`。当 **活塞位移** 参数为 `Provide input signal from Multibody joint` 时，使用端口 **p** 输入活塞位移。您可以通过使用 Translational Multibody Interface 模块提供活塞位移，来确保位置信号的导数等于活塞速度。

活塞运动的方向取决于 **机械方向** 参数。如果机械方向为正，则当端口 **A** 处的表压为正时，活塞相对于执行器外壳的平移为正。当机械方向为负时，运动方向反转。

### 硬限位

一组硬限位限制活塞的运动范围。模块使用 Translational Hard Stop 模块的实现，将硬限位视为弹簧-阻尼系统。弹簧刚度系数控制硬限位接触力的恢复分量，阻尼系数控制耗散分量。

硬限位位于活塞行程的远端。如果机械方向为正，则下限位在 *x* = 0，上限位在 *x* = +*stroke*。如果机械方向为负，则下限位在 *x* = -*stroke*，上限位在 *x* = 0。

### 模块复合

此模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter (MA)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor

构成该模块的元素示意图。
