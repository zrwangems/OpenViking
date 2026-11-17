---
type: simulink-block
title: 'Double-Acting Actuator (MA)'
family: 'moist-air'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Actuators'
documentation_page: 'doubleactingactuatorma'
documentation_source_path: 'ref/doubleactingactuatorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (MA)

## 端口

### 输入

### **p** — 活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入，单位为 m。
使用 Translational Multibody Interface 模块将此端口连接到 Simscape Multibody™ 网络。

#### 依赖关系

要启用此端口，请将 **自腔 A 端盖的活塞位移** 设置为 `Provide input signal from Multibody joint`。
### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **自腔 A 端盖的活塞位移** 设置为 `Calculate from velocity of port R relative to port C`。
### 守恒

### **A** — 湿空气液体端口

与腔 A 入口关联的湿空气守恒端口。

### **B** — 湿空气液体端口

与腔 B 入口关联的湿空气守恒端口。

### **R** — 执行器活塞机械平移

与执行器活塞关联的机械平移守恒端口。

### **C** — 执行器壳体机械平移

与执行器壳体关联的机械平移守恒端口。

### **HA** — 传热 热

与腔 A 关联的热守恒端口。

### **HB** — 传热 热

与腔 B 关联的热守恒端口。

## 参数

### 执行器

### **两侧使用相同流体** — 用于对两个腔室中的相同流体进行建模的选项 `on`（默认）| `off`

是否在两个执行器腔室中对相同流体建模。如果选择此参数，执行器将在两个腔室中传播流体属性。清除此参数可将每个腔室建模为不同流体，其中每个腔室连接到隔离的流体网络。

### **机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。将此参数设置为：

- `Pressure at A causes positive displacement of R relative to C` 时，当端口 **A** 处的湿空气体积膨胀时，活塞位移为正。此运动对应于杆伸出。
- `Pressure at A causes negative displacement of R relative to C` 时，当端口 **A** 处的湿空气体积膨胀时，活塞位移为负。此运动对应于杆缩回。

### **腔 A 中活塞横截面积** — 腔 A 活塞面积 `0.01 m^2`（默认）| 正标量

腔 A 侧活塞杆的横截面积。

### **腔 B 中活塞横截面积** — 腔 B 活塞面积 `0.01 m^2`（默认）| 正标量

腔 B 侧活塞杆的横截面积。

### **活塞行程** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **腔 A 中死区体积** — 活塞完全缩回时的腔 A 流体体积 `1e-5 m^3`（默认）| 正标量

腔 A 中活塞位移为 `0` 时的湿空气体积。此参数是活塞紧靠执行器端盖时的湿空气体积。

### **腔 B 中死区体积** — 活塞完全缩回时的腔 B 流体体积 `1e-5 m^3`（默认）| 正标量

腔 B 中活塞位移为 `0` 时的湿空气体积。此参数是活塞紧靠执行器端盖时的湿空气体积。

### **端口 A 处横截面积** — 端口 A 处面积 `0.01 m^2`（默认）| 正标量

端口 **A** 的横截面积。

### **端口 B 处横截面积** — 端口 B 处面积 `0.01 m^2`（默认）| 正标量

端口 **B** 的横截面积。

### **环境压力规格** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。选择 `Atmospheric pressure` 时，模块假定压力为 0.101325 MPa。

### **环境压力** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **环境压力规格** 设置为 `Specified pressure`。

### 硬限位

### **硬限位模型** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞完全伸出或完全缩回时使用的硬限位模型。有关详细信息，请参阅 Translational Hard Stop 模块。

### **硬限位刚度系数** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **硬限位阻尼系数** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为以下设置之一：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **过渡区域** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。当活塞的最大伸出或缩回超出此范围时，模块不应用硬限位模型。在这种情况下，活塞上不会产生额外力。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位器之间最终相对速度与初始相对速度之比 `0.7`（默认）| 介于 0 和 1 之间的无量纲值

滑块反弹后，滑块与限位器之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位器之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位器之间的阈值相对速度。当滑块以小于 **静态接触速度阈值** 参数值的速度撞击壳体时，二者保持接触。否则，滑块反弹。为避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的力 `0.001 N`（默认）| 正标量

使滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### 腔 A 初始条件

### **自腔 A 端盖的活塞位移** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，模块可以从 Multibody 模块接收位置，也可以在内部计算位置并在端口 **p** 报告位置。当机械方向为正时，位置介于 `0` 与 **活塞行程** 参数值之间；当机械方向为负时，位置介于 `0` 与 **活塞行程** 参数的负值之间。

### **自腔 A 端盖的初始活塞位移** — 仿真开始时的活塞位移 `0` `m`（默认）| 标量

仿真开始时相对于腔 A 端盖的活塞位置。

#### 依赖关系

要启用此参数，请将 **活塞位移** 设置为 `Calculate from velocity of port R relative to port C`。

### **腔 A 中初始湿空气压力** — 仿真开始时的湿空气压力 `0.101325` `MPa`（默认）| 正标量

腔 A 中仿真开始时的湿空气压力。

### **腔 A 中初始湿空气温度** — 仿真开始时的湿空气温度 `293.15` `K`（默认）| 标量

腔 A 中仿真开始时的湿空气温度。

### **腔 A 中初始湿度规格** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述腔 A 中初始湿空气湿度水平。

### **腔 A 中初始湿空气相对湿度** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的标量

腔 A 中仿真开始时的湿空气相对湿度。

#### 依赖关系

要启用此参数，请将 **腔 A 中初始湿度规格** 设置为 `Relative humidity`。

### **腔 A 中初始湿空气比湿度** — 仿真开始时的比湿度 `0.01`（默认）| 范围 [0,1] 内的标量

腔 A 中仿真开始时的湿空气比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **腔 A 中初始湿度规格** 设置为 `Specific humidity`。

### **腔 A 中初始湿空气水蒸气摩尔分数** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量

腔 A 中仿真开始时湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将 **腔 A 中初始湿度规格** 设置为 `Mole fraction`。

### **腔 A 中初始湿空气湿度比** — 仿真开始时的湿度比 `0.01`（默认）| 范围 [0,1] 内的标量

腔 A 中仿真开始时的湿空气湿度比，定义为水蒸气与干空气和示踪气体的质量比。

#### 依赖关系

要启用此参数，请将 **腔 A 中初始湿度规格** 设置为 `Humidity ratio`。

### **腔 A 中初始湿空气湿球温度** — 仿真开始时的湿球温度 `287` `K`（默认）| 正标量

仿真开始时湿空气混合物的湿球温度。

#### 依赖关系

要启用此参数，请将 **腔 A 中初始湿度规格** 设置为 `Wet-bulb temperature`。

### **腔 A 中初始示踪气体规格** — 用于描述初始示踪气体水平的量 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数来描述仿真开始时腔 A 中的示踪气体水平。

### **腔 A 中初始示踪气体质量分数** — 仿真开始时示踪气体的质量分数 `0.001`（默认）| 范围 [0,1] 内的标量

腔 A 中仿真开始时湿空气混合物中示踪气体的质量分数。

#### 依赖关系

要启用此参数，请将 **初始示踪气体规格** 设置为 `Mass fraction`。

### **腔 A 中初始示踪气体摩尔分数** — 仿真开始时示踪气体的摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量

腔 A 中仿真开始时湿空气混合物中示踪气体的摩尔分数。

#### 依赖关系

要启用此参数，请将 **腔 A 中初始示踪气体规格** 设置为 `Mole fraction`。

### **腔 A 中水滴与湿空气的初始质量比** — 水滴与湿空气的比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

### **腔 A 中饱和时的相对湿度** — 发生冷凝时高于的相对湿度 `1`（默认）| 正标量

腔 A 中发生冷凝时高于的相对湿度。

### **腔 A 中水蒸气冷凝时间常数** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝析出多余湿度而返回到饱和状态的特征时间尺度。

### **腔 A 中水滴蒸发时间常数** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **腔 A 中作为水滴夹带的冷凝物分数** — 水滴中冷凝物的分数 `1`（默认）| 范围 [0,1] 内的标量

湿空气中作为水滴夹带的冷凝物分数。

### 腔 B 初始条件

### **腔 B 中初始湿空气压力** — 仿真开始时的湿空气压力 `0.101325` `MPa`（默认）| 正标量

腔 B 中仿真开始时的湿空气压力。

### **腔 B 中初始湿空气温度** — 仿真开始时的湿空气温度 `293.15` `K`（默认）| 标量

腔 B 中仿真开始时的湿空气温度。

### **腔 B 中初始湿度规格** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述腔 B 中初始湿空气湿度水平。

### **腔 B 中初始湿空气相对湿度** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的标量

腔 B 中仿真开始时的湿空气相对湿度。

#### 依赖关系

要启用此参数，请将 **腔 B 中初始湿度规格** 设置为 `Relative humidity`。

### **腔 B 中初始湿空气比湿度** — 仿真开始时的比湿度 `0.01`（默认）| 范围 [0,1] 内的标量

腔 B 中仿真开始时的湿空气比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **腔 B 中初始湿度规格** 设置为 `Specific humidity`。

### **腔 B 中初始湿空气水蒸气摩尔分数** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量

腔 B 中仿真开始时湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将 **腔 B 中初始湿度规格** 设置为 `Mole fraction`。

### **腔 B 中初始湿空气湿度比** — 仿真开始时的湿度比 `0.01`（默认）| 范围 [0,1] 内的标量

腔 B 中仿真开始时的湿空气湿度比，定义为水蒸气与干空气和示踪气体的质量比。

#### 依赖关系

要启用此参数，请将 **腔 B 中初始湿度规格** 设置为 `Humidity ratio`。

### **腔 B 中初始湿空气湿球温度** — 仿真开始时的湿球温度 `287` `K`（默认）| 正标量

仿真开始时湿空气混合物的湿球温度。

#### 依赖关系

要启用此参数，请将 **腔 B 中初始湿度规格** 设置为 `Wet-bulb temperature`。

### **腔室 B 中的初始示踪气体规格** — 用于描述初始示踪气体水平的量 `Mass fraction`（默认值） | `Mole fraction`

是否使用质量分数或摩尔分数来描述仿真开始时腔室 B 中的示踪气体水平。

### **腔室 B 中的初始示踪气体质量分数** — 仿真开始时示踪气体的质量分数 `0.001`（默认值） | 范围 [0,1] 中的标量

仿真开始时腔室 B 中湿空气混合物内示踪气体的质量分数。

#### 依赖关系

要启用此参数，请将 **初始示踪气体规格** 设置为 `Mass fraction`。

### **腔室 B 中的初始示踪气体摩尔分数** — 仿真开始时示踪气体的摩尔分数 `0.001`（默认值） | 范围 [0,1] 中的标量

仿真开始时腔室 B 中湿空气混合物内示踪气体的摩尔分数。

#### 依赖关系

要启用此参数，请将 **腔室 B 中的初始示踪气体规格** 设置为 `Mole fraction`。

### **腔室 B 中水滴与湿空气的初始质量比** — 水滴与湿空气之比 `0`（默认值） | 正标量

水滴与湿空气的初始质量比。

### **腔室 B 中饱和时的相对湿度** — 发生凝结所高于的相对湿度 `1`（默认值） | 正标量

腔室 B 中发生凝结所高于的相对湿度。

### **腔室 B 中水蒸气凝结时间常数** — 凝结的时间尺度 `1e-3 s`（默认值） | 正标量

过饱和湿空气体积通过凝结析出多余湿气而恢复到饱和状态的特征时间尺度。

### **腔室 B 中水滴蒸发时间常数** — 蒸发的时间尺度 `1e-3 s`（默认值） | 正标量

水滴蒸发为蒸气的特征时间尺度。

### **腔室 B 中以水滴形式夹带的冷凝物分数** — 冷凝物中作为水滴夹带的分数 `1`（默认值） | 范围 [0,1] 中的标量

湿空气中以水滴形式夹带的冷凝物分数。

## 所属库

Simscape / Fluids / Moist Air / Actuators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气领域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **启用夹带水滴**。

## 描述

湿空气网络中的双作用线性执行器

Double-Acting Actuator (MA) 模块对具有由两个相对湿空气腔室控制的活塞的线性执行器建模。执行器在伸出和缩回冲程中生成力。生成的力取决于两个腔室之间的压力差。

该图显示执行器的关键组件。端口 **A** 和 **B** 表示湿空气腔室入口。端口 **R** 表示平移的执行器活塞，端口 **C** 表示执行器壳体。端口 **HA** 和 **HB** 表示每个湿空气腔室与环境之间的热接口。运动的活塞是绝热的。

Double-Acting Actuator 示意图

### 位移

模块将活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**机械方向** 参数标识活塞位移的方向。当腔室 A 容积等于 **腔室 A 中的死区容积** 参数的值时，活塞位移为中性，即 `0`。当 **从腔室 A 端盖算起的活塞位移** 参数为 `Provide input signal from Multibody joint` 时，您使用端口 **p** 输入活塞位移。确保位置信号的导数等于活塞速度。您可以使用 Translational Multibody Interface 模块提供活塞位移，以确保位置信号的导数等于活塞速度。

活塞运动的方向取决于 **机械方向** 参数。如果机械方向为正，则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平移为正。当机械方向为负时，运动方向反转。

### 硬限位

一组硬限位限制活塞的运动范围。该模块使用 Translational Hard Stop 模块的实现，将硬限位视为弹簧-阻尼器系统。弹簧刚度系数控制硬限位接触力的恢复分量，阻尼系数控制耗散分量。

硬限位位于活塞冲程的两端。如果机械方向为正，则下限位在 *x* = 0 处，上限位在 *x* = +*stroke* 处。如果机械方向为负，则下限位在 *x* = -*stroke* 处，上限位在 *x* = 0 处。

### 模块组合

该模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter (MA)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor

构成该模块的元素的示意图。
