---
type: simulink-block
title: 'Double-Acting Actuator (TL-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Actuators'
documentation_page: 'doubleactingactuatortlg'
documentation_source_path: 'ref/doubleactingactuatortlg.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (TL-G)

## 端口

### 输出

### **P** — 活塞位置，m physical signal

与活塞位置关联的 physical signal 输出端口。测量值是绝对量。第一个读数是 **Piston initial displacement** 参数的值。

### 守恒

### **A** — 腔 A 热液体入口

与腔 A 入口关联的热液体守恒端口。

### **B** — 腔 B 气体入口

表示腔 B 入口的气体守恒端口。

### **R** — 执行器活塞机械平动

表示执行器活塞的机械平动守恒端口。

### **C** — 执行器壳体机械平动

表示执行器壳体的机械平动守恒端口。

### **HA** — 腔 A 热流热

与可在热液体体积和执行器环境之间发生热交换的表面关联的热守恒端口。此端口处的热过程会影响热液体腔中的温度，因而影响端口 **A** 处的温度。

### **HB** — 腔 B 热流热

与可在气体体积和执行器环境之间发生热交换的表面关联的热守恒端口。此端口处的热过程会影响气体腔中的温度，因而影响端口 **A** 处的温度。

## 参数

### 热液体侧

### **Mechanical orientation** — 活塞运动方向相对于流体流动方向 `Positive` | `Negative`

执行器活塞相对于流体流动方向的方向。正方向会使活塞响应通过端口 A 的正流量而相对于执行器壳体沿正方向运动。机械方向会影响活塞硬限位的位置。有关硬限位放置的更多信息，请参见模块描述。

### **Piston cross-sectional area in chamber A** — 热液体腔中流体体积的横截面积 `0.01 m^2`（默认） | scalar in units of area

热液体腔主体中垂直于流动方向的面积。模块使用此面积计算由热液体腔中流体压力产生的液压力。此参数必须大于零。

### **Piston stroke** — 活塞从一个硬限位到另一个硬限位的行进距离 `0.2 m`（默认） | scalar in units of length

活塞从一个硬限位到另一个硬限位可用的总行进距离。硬限位限制活塞运动，使活塞被约束在活塞行程内。有关硬限位位置的更多信息，请参见模块描述。

### **Piston initial displacement** — 仿真开始时活塞的位置 `0 m`（默认） | scalar in units of length

仿真开始时活塞的绝对位置。如果机械方向为正，则零位置与下硬限位重合；如果机械方向为负，则零位置与上硬限位重合。

### **Dead volume in chamber A** — 处于完全压紧位置时热液体腔中的流体体积 `1e-4 m^3`（默认） | scalar in units of volume

当活塞压靠在最靠近热液体入口的硬限位上时，热液体腔中剩余的热液体体积。该死区体积使模块能够在此体积最小时捕获热液体体积的内部状态（其压力和温度）。此参数必须大于零。

### **Enable dynamic compressibility** — 选择是否对热液体腔内的动态可压缩性效应建模 `On`（默认） | `Off`

对热液体腔内的动态可压缩性效应建模的选项。如果此参数设置为 `On`，则将热液体视为可压缩；如果设置为 `Off`，则视为不可压缩。如果选择 `Off`，模块会忽略热液体密度对压力和温度的依赖性。

### **Initial liquid pressure in chamber A (absolute)** — 热液体腔中的绝对压力 `0.101325 Pa`（默认） | scalar in units of pressure

仿真时间为零时热液体腔内的压力，相对于绝对零压。此参数有助于设置热液体体积的初始状态。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Initial liquid temperature in chamber A** — 仿真开始时热液体腔中的温度 `293.15 K`（默认） | scalar in units of temperature

仿真开始时热液体腔内的平均温度。此参数有助于设置热液体体积的初始状态。

### **Nominal liquid pressure in chamber A (absolute)** — 腔 A 中额定工况下的压力 `0.101325 MPa`（默认） | scalar

腔 A 中额定工况下的液体压力。当禁用动态可压缩性时，模块使用此值计算质量守恒方程中要使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid temperature in chamber A** — 腔 A 中额定工况下的温度 `293.15` `K`（默认） | scalar

腔 A 中额定工况下的液体温度。当禁用动态可压缩性时，模块使用此值计算质量守恒方程中要使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Environment pressure specification** — 热液体侧选择大气压还是自定义环境压力 `Atmospheric pressure`（默认） | `Specified pressure`

用于将热液体腔的环境压力设置为一个地球大气压的典型值或自定义值的选项。选择 `Specified pressure` 会显示附加参数 **Environment pressure**，您可以用它指定自定义压力。

### **Environment pressure** — 热液体腔外部环境的绝对压力 `0.101325 MPa`（默认） | scalar in units of pressure

热液体腔外部相对于绝对零压的压力。此压力对抗热液体腔内的压力。压力为零对应于完美真空。

#### 依赖关系

当 **Environment pressure specification** 设置为 `Specified pressure` 时，此参数启用。

### 气体侧

### **Piston cross-sectional area in chamber B** — 气体腔中流体体积的横截面积 `1e-3 m^2`（默认） | positive scalar in units of area

气体腔主体中垂直于流动方向的面积。模块使用此面积计算由气体腔中流体压力产生的气动力。此参数必须大于零。

### **Cross-sectional area at port B** — 气体腔入口的横截面积 `1e-3 m^2`（默认） | positive scalar in units of area

气体腔入口处垂直于流动方向的面积。入口处的横截面积可以不同于腔主体中的横截面积。将两个横截面积设置为不同值，以对入口处面积突变的影响建模。此参数必须大于零。

### **Dead volume in chamber B** — 处于完全压紧状态时气体腔中的流体体积 `1e-4 m^3`（默认） | positive scalar in units of volume

当活塞压靠在最靠近气体入口的硬限位上时，气体腔中剩余的气体体积。该死区体积使模块能够在此体积最小时捕获气体体积的内部状态（其压力和温度）。此参数必须大于零。

### **Initial gas pressure in chamber B (absolute)** — 仿真开始时气体腔内的绝对压力 `0.101325 MPa`（默认） | scalar in units of pressure

仿真时间为零时气体腔内的压力，相对于绝对零压。此压力有助于设置气体体积的初始状态。

### **Initial gas temperature in chamber B** — 仿真开始时气体腔中的温度 `293.15 K`（默认） | scalar in units of temperature

仿真开始时气体腔内的平均温度。此参数有助于设置气体体积的初始状态。

### **Environment pressure specification** — 气体侧选择大气压还是自定义环境压力 `Atmospheric pressure`（默认） | `Specified pressure`

用于将气体腔的环境压力设置为一个地球大气压的典型值或自定义值的选项。选择 `Specified pressure` 会显示附加参数 **Environment pressure**，您可以用它指定自定义压力。

### **Environment pressure** — 气体腔外部环境的绝对压力 `0.101325 MPa`（默认） | scalar in units of pressure

气体腔外部相对于绝对零压的压力。此压力对抗气体腔内的压力。压力为零对应于完美真空。

#### 依赖关系

当 **Environment pressure specification** 设置为 `Specified pressure` 时，此参数启用。

### 硬限位

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认） | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时所受力的模型选择。有关更多信息，请参见 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e6` `N/m`（默认） | positive scalar

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

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认） | positive scalar

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

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认） | positive scalar

硬限位力模型的应用范围。在活塞最大伸出和活塞最大缩回的这一范围之外，不应用 **Hard stop model**，并且活塞上没有额外力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认） | unitless value between 0 and 1

滑块弹跳后，滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的相对速度阈值 `0.001 m/s`（默认） | nonnegative scalar

碰撞前滑块与限位之间的相对速度阈值。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块会弹跳。为避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式转换到自由模式所需的力阈值 `0.001 N`（默认） | positive scalar

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of
restitution`。

## 所属库

Simscape / Fluids / Thermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。此选项名为 `Based on coefficient of restitution`，通过使用模式图对硬限位建模。

## 描述

具有相对的热液体腔和气体腔的线性执行器

Double-Acting Actuator (TL-G) 模块对具有相对的热液体腔和气体腔的线性执行器建模。可以分别对各腔加压，以在伸出和缩回行程中为执行器提供动力。腔之间的活塞将跨腔压差转换为执行力。

该图将模块的守恒端口映射到执行器部件。端口 **A** 和 **B** 是热液体腔和气体腔的入口。端口 **R** 和 **C** 是平动活塞和壳体。各腔可以与环境交换热量，并为此配备端口 **HA** 和 **HB**。活塞完全绝热。热液体腔和气体腔彼此不交换热量。

活塞相对于壳体的位移符号取决于执行器的机械方向。使用 **Mechanical orientation** 参数指定此设置。如果机械方向为正，则当热液体腔（端口 **A**）中的压力最高时，活塞位移为正。如果机械方向为负，则（在相同压力条件下）活塞位移为负。

使用端口 **P** 输出活塞的瞬时位置。测量值是绝对量（相对于零）。硬限位将活塞运动限制在壳体长度内。限位建模为弹簧-阻尼器，并具有弹簧和阻尼系数以捕获材料柔量。一个位于活塞行程底部，另一个位于顶部：

- 如果 **Mechanical orientation** 设置为 `Positive`，则底部限位在零处，顶部限位在等于活塞行程的距离处。
- 如果 **Mechanical orientation** 设置为 `Negative`，则顶部限位在零处，底部限位在等于活塞行程的距离处。

该模块是由 Simscape™ Foundation 模块构建的复合组件。有关 Double-Acting Actuator (TL-G) 模块工作原理的更多信息，请参见组成模块的参考页：

- Translational Mechanical Converter
  (TL)
- Translational Mechanical Converter
  (G)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor
