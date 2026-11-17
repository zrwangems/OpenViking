---
type: simulink-block
title: 'Double-Acting Actuator (TL-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Actuators'
documentation_page: 'doubleactingactuatortlg'
documentation_source_path: 'ref/doubleactingactuatortlg.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (TL-G)

## 端口

### 输出

### **P** — 活塞位置，m 物理信号

与活塞位置关联的物理信号输出端口。测量值为绝对值。第一个读数为 **Piston initial displacement** 参数的值。
### 守恒

### **A** — 腔室 A 热流体入口

与腔室 A 入口关联的热流体守恒端口。

### **B** — 腔室 B 气体入口

表示腔室 B 入口的气体守恒端口。

### **R** — 执行器活塞机械平移

表示执行器活塞的机械平移守恒端口。

### **C** — 执行器壳体机械平移

表示执行器壳体的机械平移守恒端口。

### **HA** — 腔室 A 热流热端口

与热流体体积和执行器周围环境之间可发生热交换的表面关联的热守恒端口。该端口处的热过程影响热流体腔室中的温度，从而影响端口 **A** 处的温度。

### **HB** — 腔室 B 热流热端口

与气体体积和执行器周围环境之间可发生热交换的表面关联的热守恒端口。该端口处的热过程影响气体腔室中的温度，从而影响端口 **A** 处的温度。

## 参数

### 热流体侧

### **Mechanical orientation** — 活塞运动方向相对于流体流动方向 `Positive` | `Negative`

执行器活塞相对于流体流动方向的方向。正方向使活塞响应于通过端口 A 的正流量而相对于执行器壳体沿正方向移动。机械方向影响活塞硬限位的位置。有关硬限位位置的更多信息，请参阅模块描述。

### **Piston cross-sectional area in chamber A** — 热流体腔室中流体体积的横截面积 `0.01 m^2`（默认）| 面积单位的标量

热流体腔室主体中垂直于流动方向的面积。模块使用此面积计算热流体腔室中流体压力产生的液压力。此参数必须大于零。

### **Piston stroke** — 活塞从一个硬限位到另一个硬限位的行程距离 `0.2 m`（默认）| 长度单位的标量

活塞可用的总行程距离，从一个硬限位到另一个硬限位。硬限位限制活塞运动，使活塞被限制在活塞行程内。有关硬限位位置的更多信息，请参阅模块描述。

### **Piston initial displacement** — 仿真开始时活塞的位置 `0 m`（默认）| 长度单位的标量

仿真开始时活塞的绝对位置。如果机械方向为正，零位置与下限位重合；如果机械方向为负，零位置与上限位重合。

### **Dead volume in chamber A** — 活塞处于底部位置时热流体腔室中的流体体积 `1e-4 m^3`（默认）| 体积单位的标量

当活塞压靠在最靠近热流体入口的硬限位上时，热流体腔室中剩余的热流体体积。死区体积使模块能够在该体积最小时捕获热流体体积的内部状态——其压力和温度。此参数必须大于零。

### **Enable dynamic compressibility** — 选择是否对热流体腔室内的动态可压缩性效应进行建模 `On`（默认）| `Off`

对热流体腔室内的动态可压缩性效应进行建模的选项。如果此参数设置为 `On`，热流体被视为可压缩；如果设置为 `Off`，则被视为不可压缩。如果选择 `Off`，模块忽略热流体密度对压力和温度的依赖性。

### **Initial liquid pressure in chamber A (absolute)** — 热流体腔室中的绝对压力 `0.101325 Pa`（默认）| 压力单位的标量

仿真时间零时热流体腔室内部相对于绝对零度的压力。此参数有助于设置热流体体积的初始状态。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Initial liquid temperature in chamber A** — 仿真开始时热流体腔室中的温度 `293.15 K`（默认）| 温度单位的标量

仿真开始时热流体腔室内的平均温度。此参数有助于设置热流体体积的初始状态。

### **Nominal liquid pressure in chamber A (absolute)** — 腔室 A 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 A 中额定工况下的液体压力。当动态可压缩性禁用时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid temperature in chamber A** — 腔室 A 中额定工况下的温度 `293.15` `K`（默认）| 标量

腔室 A 中额定工况下的液体温度。当动态可压缩性禁用时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Environment pressure specification** — 热流体侧大气压或自定义环境压力的选择 `Atmospheric pressure`（默认）| `Specified pressure`

将热流体腔室的环境压力设置为一个地球大气压的典型值或自定义值的选项。选择 `Specified pressure` 会显示一个附加参数 **Environment pressure**，用于指定自定义压力。

### **Environment pressure** — 热流体腔室外部环境的绝对压力 `0.101325 MPa`（默认）| 压力单位的标量

热流体腔室外部相对于绝对零度的压力。此压力作用于热流体腔室内的压力。压力为零对应于完美真空。

#### 依赖关系

当 **Environment pressure specification** 设置为 `Specified pressure` 时，此参数启用。

### 气体侧

### **Piston cross-sectional area in chamber B** — 气体腔室中流体体积的横截面积 `1e-3 m^2`（默认）| 面积单位的正标量

气体腔室主体中垂直于流动方向的面积。模块使用此面积计算气体腔室中流体压力产生的气动力。此参数必须大于零。

### **Cross-sectional area at port B** — 气体腔室入口的横截面积 `1e-3 m^2`（默认）| 面积单位的正标量

气体腔室入口处垂直于流动方向的面积。入口处的横截面积可以与腔室主体中的横截面积不同。将两个横截面积设置为不同的值，以模拟入口处面积突变的影响。此参数必须大于零。

### **B 腔死区容积** — 在完全压缩状态下气腔中的流体体积 `1e-4 m^3`（默认）| 以体积为单位的正标量

当活塞压紧在最靠近气体入口的硬限位时，气腔中剩余的气体体积。死区容积使该模块能够在此体积最小时捕获气体体积的内部状态——其压力和温度。此参数必须大于零。

### **B 腔初始气体压力（绝对）** — 仿真开始时气腔内的绝对压力 `0.101325 MPa`（默认）| 以压力为单位的标量

仿真时间为零时气腔内相对于绝对零度的压力。此压力有助于设置气体体积的初始状态。

### **B 腔初始气体温度** — 仿真开始时气腔内的温度 `293.15 K`（默认）| 以温度为单位的标量

仿真开始时气腔内的平均温度。此参数有助于设置气体体积的初始状态。

### **环境压力设定** — 气体侧大气压或自定义环境压力的选择 `Atmospheric pressure`（默认）| `Specified pressure`

将气腔的环境压力设置为一个地球大气压的典型值或自定义值的选项。选择 `Specified pressure` 会显示一个附加参数 **Environment pressure**，用于指定自定义压力。

### **环境压力** — 气腔外部环境的绝对压力 `0.101325 MPa`（默认）| 以压力为单位的标量

气腔外部相对于绝对零度的压力。此压力作用于气腔内部的压力。压力为零对应于完美真空。

#### 依赖关系

当 **Environment pressure specification** 设置为 `Specified pressure` 时，此参数启用。

### 硬限位

### **硬限位模型** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时力的模型选择。有关更多信息，请参阅 Translational Hard Stop 模块。

### **硬限位刚度系数** — 刚度系数 `1e6` `N/m`（默认）| 正标量

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

### **硬限位阻尼系数** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

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

### **过渡区域** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。在活塞最大伸出量和活塞最大缩回量的此范围之外，**Hard stop model** 不适用，活塞上没有附加力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无量纲值

滑块弹回后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹回。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

## 所属库

Simscape / Fluids / Thermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。此选项称为 `Based on coefficient of restitution`，使用模式图对硬限位进行建模。

## 描述

具有对置热液体腔和气腔的线性执行器

Double-Acting Actuator (TL-G) 模块对具有对置热液体腔和气腔的线性执行器进行建模。各腔可单独加压，以在伸出和缩回行程中驱动执行器。腔之间的活塞将跨腔压差转换为驱动力。

该图将模块的守恒端口映射到执行器部件。端口 **A** 和 **B** 是热液体腔和气腔的入口。端口 **R** 和 **C** 是平移活塞和壳体。各腔可与环境交换热量，为此配备了端口 **HA** 和 **HB**。活塞完全绝热。热液体腔和气腔之间不交换热量。

活塞相对于壳体的位移符号取决于执行器的机械方向。使用 **Mechanical orientation** 参数指定此设置。如果机械方向为正，则当热液体腔（端口 **A**）中的压力最高时，活塞位移为正。如果机械方向为负，则活塞位移（在相同压力条件下）为负。

使用端口 **P** 输出瞬时活塞位置。该测量是绝对的（相对于零）。硬限位将活塞的运动限制在壳体的长度范围内。限位建模为弹簧-阻尼器，具有弹簧和阻尼系数以捕获材料柔量。一个位于活塞行程底部，另一个位于顶部：

- 如果 **Mechanical orientation** 设置为 `Positive`，则底部限位在零处，顶部限位在等于活塞行程的距离处。
- 如果 **Mechanical orientation** 设置为 `Negative`，则顶部限位在零处，底部限位在等于活塞行程的距离处。

该模块是由 Simscape™ Foundation 模块构建的复合组件。有关 Double-Acting Actuator (TL-G) 模块工作原理的更多信息，请参阅组成模块的参考页：

- Translational Mechanical Converter
  (TL)
- Translational Mechanical Converter
  (G)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor
