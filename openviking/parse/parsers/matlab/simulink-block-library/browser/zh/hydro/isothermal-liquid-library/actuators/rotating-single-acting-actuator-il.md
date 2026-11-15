---
type: simulink-block
title: 'Rotating Single-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Actuators'
documentation_page: 'rotatingsingleactingactuatoril'
documentation_source_path: 'ref/rotatingsingleactingactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotating Single-Acting Actuator (IL)

## 端口

### 守恒

### **A** — 液体腔入口端口 等温液体

到液体腔的入口端口。

### **C** — 执行器外壳 机械平移

用于执行器速度和力的参考端口。

### **R** — 活塞杆速度 机械平移

与活塞速度和力相关的端口。
### 输入

### **W** — 执行器旋转速度 物理信号

执行器旋转速度，以 rad/s 为单位的物理信号接收。

### **p** — 活塞位置，m 物理信号

活塞位置，以 m 为单位，从 Simscape Multibody 模块作为物理信号接收。

#### 依赖关系

要显示此端口，请将 **活塞位移** 设置为 `Provide input signal from Multibody
joint`。
### 输出

### **p** — 活塞位置，m 物理信号

活塞位置，以 m 为单位，作为物理信号返回。

#### 依赖关系

要显示此端口，请将 **活塞位移** 设置为 `Calculate from velocity of port R relative to port
C`。

## 参数

### 执行器

### **活塞外半径** — 活塞外半径 `0.1 m`（默认）| 正标量

活塞外半径。

### **活塞内半径** — 活塞内半径 `0.05 m`（默认）| 正标量

活塞内半径。

### **机械方向** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

设置活塞位移方向。将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为正。这对应于活塞杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为负。这对应于活塞杆缩回。

### **活塞行程** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **死区容积** — 活塞完全缩回时的流体体积 `1e-5 m^3`（默认）| 正标量

活塞位移为 `0` 时的液体体积。这是当活塞抵住执行器端盖时的液体体积。

### **环境压力规格** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric pressure` 选项将环境压力设置为 0.101325 MPa。

### **环境压力** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **环境压力规格** 设置为 `Specified
pressure`。

### 流体通道

### **流体入口半径** — 流体通道半径 `0.06 m`（默认）| 正标量

旋转轴中流体开口的半径。此值必须大于或等于 **活塞内半径**，且小于或等于 **活塞外半径**。

### **流体通道横截面积** — 流体横截面积 `1e-3 m^2`（默认）| 正标量

流体通道的横截面积。

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

流动排放损失系数。

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流上限雷诺数。

### 硬限位

### **硬限位模型** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞完全伸出或完全缩回时作用力的模型选择。更多信息，请参阅 Translational Hard Stop 模块。

### **硬限位刚度系数** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为

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

要启用此参数，请将 **硬限位模型** 设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **过渡区域** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。在活塞最大伸出和活塞最大缩回的这个范围之外，不应用 **硬限位模型**，并且活塞上没有附加力。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位器之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后，滑块与限位器之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of
restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位器之间的相对速度阈值 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位器之间的相对速度阈值。当滑块以小于 **静态接触速度阈值** 参数值的速度撞击外壳时，它们保持接触。否则，滑块弹跳。为避免对滑块与外壳之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of
restitution`。

### **静态接触释放力阈值** — 从接触模式过渡到自由模式所需的力阈值 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **硬限位模型** 设置为 `Based on coefficient of
restitution`。

### 初始条件

### **活塞位移** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from Multibody joint` 时，模块可以从 Multibody 模块接收位置；或者内部计算位置并在端口 **p** 报告该位置。当机械方向为正时，位置介于 `0` 和 **活塞行程** 之间；当机械方向为负时，位置介于 `0` 和 –**活塞行程** 之间。

### **初始活塞位移** — 仿真开始时的活塞位置 `0 m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **活塞位移** 设置为 `Calculate from velocity of port R relative to port C`。

### **启用动态可压缩性** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对由流体可压缩性引起的任何流体密度变化建模。当您选择 **启用动态可压缩性** 时，除了由压力变化引起的密度变化外，还会计算由进入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **初始液体压力** — 可压缩流体的起始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

### **标称液体压力** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的液体压力。当禁用动态可压缩性时，模块使用此值计算质量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：新的硬限位参数化选项

该模块为 **硬限位模型** 参数新增了一个选项。此选项名为 `Based on coefficient of restitution`，使用模式图对硬限位建模。

## 描述

等温液体网络中旋转轴上的执行器

Rotating Single-Acting Actuator (IL) 模块对等温液体网络中绕其中心轴旋转的执行器进行建模。旋转执行器用于旋转轴控制组件，例如摩擦离合器或制动器。流体在端口 **A** 进入执行器。角速度在端口 **W** 设置。端口 **C** 与执行器外壳关联，活塞速度和力在端口 **R** 设置。

当活塞位置在内部计算时，它会在端口 **p** 报告；当位置通过连接到 Simscape™ Multibody™ 关节设置时，它会在端口 **p** 作为物理信号接收。活塞接近完全伸出或完全缩回时的运动由四种硬限位模型之一限制。可以选择对 **启用动态可压缩性** 建模。

### 位移

活塞位移以端口 **R** 相对于端口 **C** 的位置来测量。**机械方向** 标识活塞位移的方向。当腔室体积等于 **死区容积** 时，活塞位移为中性，即 `0`。当位移作为输入接收时，确保位置的导数等于活塞速度。当输入来自 Translational Multibody Interface 模块与 Simscape Multibody 关节的连接时，会自动如此。

### 硬限位模型

为避免执行器完全伸出或完全缩回时发生机械损坏，当活塞接近这些限位时，执行器通常表现出非线性行为。Double-Acting Actuator (IL) 模块通过四种硬限位模型的选择来对该行为建模，这些模型通过弹簧-阻尼器系统对材料顺应性建模。硬限位模型包括：

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`.
- `Full stiffness and damping applied at bounds, undamped
  rebound`.
- `Full stiffness and damping applied at bounds, damped
  rebound`.
- `Based on coefficient of restitution`

当活塞处于上限或下限时，对硬限位力建模。边界区域位于 **活塞行程** 或活塞初始位移的 **过渡区域** 内。在该区域之外，FHardStop=0。

有关这些设置的详细信息，请参阅 Translational Hard Stop 模块页面。

### 模块子组件

Rotating Single-Acting Actuator (IL) 模块包含三个 Isothermal Liquid 库模块：

- Rotating Channel (IL)
- Single-Acting Actuator (IL)
- Rotating Cylinder Force (IL)

**执行器示意图**
