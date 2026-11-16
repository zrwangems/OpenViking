---
type: simulink-block
title: 'Double-Acting Rotary Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'doubleactingrotaryactuatoril'
documentation_source_path: 'ref/doubleactingrotaryactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Rotary Actuator (IL)

## 端口

### 输入

### **q** — 轴角度物理信号

轴角度，作为来自 Simscape Multibody 模块的物理信号接收。

#### 依赖关系

要显示此端口，请将 **Shaft rotation from chamber A** 设置为 `Provide input signal from Multibody joint`。

### 输出

### **q** — 执行器角度物理信号

与轴角位置关联的物理信号输出端口。

#### 依赖关系

要显示此端口，请将 **Shaft rotation from chamber A** 设置为 `Calculate from angular velocity of port R relative to port C`。

### 守恒

### **A** — 腔室 A 入口等温液体

与执行器腔室 A 关联的等温液体守恒端口。

### **B** — 腔室 B 入口等温液体

与执行器腔室 B 关联的等温液体守恒端口。

### **R** — 执行器轴机械旋转

与轴关联的机械旋转守恒端口。

### **C** — 执行器壳体机械旋转

与缸体壳体关联的机械旋转守恒端口。

## 参数

### 执行器

### **Same fluid on both sides** — 在两个腔室中建模相同流体的选项 `on`（默认）| `off`

是否在两个执行器腔室中建模相同流体。如果选中此参数，执行器将通过两个腔室传播流体属性。清除此参数以将每个腔室建模为不同流体，其中每个腔室连接到隔离的流体网络。

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

设置活塞位移方向。将此参数设置为：

- `Pressure at A causes positive displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为正。这对应于杆伸出。
- `Pressure at A causes negative displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为负。这对应于杆缩回。

### **Volume displacement in chamber A** — 容积排量 `1e-4 m^3/rad`（默认）| 正标量

腔室 A 中执行器的有效排量。

### **Volume displacement in chamber B** — 容积排量 `1e-4 m^3/rad`（默认）| 正标量

腔室 B 中执行器的有效排量。

### **Stroke** — 角度 `5.0 rad`（默认）| 正标量

止挡之间的轴最大行程。

### **Dead volume in chamber A** — 流体体积 `1e-5 m^3`（默认）| 正标量

腔室 A 中活塞位移为 `0` 时的液体体积。这是活塞紧靠执行器端盖时的液体体积。

### **Dead volume in chamber B** — 流体体积 `1e-5 m^3`（默认）| 正标量

腔室 B 中活塞位移为 `0` 时的液体体积。这是活塞紧靠执行器端盖时的液体体积。

### **Environment pressure specification** — 压力参考源 `Atmospheric pressure`（默认）| `Specified pressure`

环境压力的选择。选项包括 `Atmospheric pressure` 和 `Specified pressure`。

### **Environment pressure** — 用户定义的压力参考 `0.101325 MPa`（默认）| 正标量

执行器壳体外的压力。此压力抵抗执行器腔室内的压力。值为零对应于真空。

#### 依赖关系

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

### 硬限位

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

在完全伸出或完全缩回时作用于活塞的力的模型选择。有关详细信息，请参阅 Rotational Hard Stop 模块。

### **Hard stop stiffness coefficient** — 刚度系数 `1e6` N\*m/rad（默认）| 正标量

为 Rotational Hard Stop 模块指定碰撞体的弹性属性。参数值越大，活塞与止挡之间的冲击越刚性。较低的值使接触更软，并且通常可改善收敛性和计算效率。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Hard stop damping coefficient** — 阻尼系数 `150` N\*m(rad/s)（默认）| 正标量

为 Rotational Hard Stop 模块指定碰撞体的耗散属性。当阻尼为零时，冲击是弹性的。参数值越大，活塞与止挡相互作用期间的能耗散越大。只要滑块与止挡接触，阻尼就会影响滑块运动，包括滑块从接触处被拉回的时段。将此参数设置为非零值以提高仿真的效率和收敛性。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Transition region** — 过渡区域 `0.001 rad`（默认）| 正标量

低于该距离时，对硬限位力应用缩放。当到硬限位的距离等于此参数值时，接触力为零。当到硬限位的距离为零时，接触力达到其完整值。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与止挡之间最终相对速度与初始相对速度的比值 `0.7`（默认）| 介于 0 和 1 之间的无单位值

滑块弹跳后，滑块与止挡之间最终相对速度与初始相对速度的比值。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与止挡之间的阈值相对速度 `0.1 rad/s`（默认）| 非负标量

碰撞前滑块与止挡之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块会弹跳。为避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release torque threshold** — 从接触模式转换到自由模式所需的阈值扭矩 `0.001 N*m`（默认）| 正标量

使滑块从静态接触模式释放所需的最小扭矩。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 初始条件

### **Shaft rotation from chamber A** — 确定轴角度的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定轴角度的方法。当设置为 `Provide input signal from Multibody joint` 时，模块可以从 Multibody 模块接收角度；或者在内部计算该角度，并在端口 **q** 报告。

### **Initial shaft rotation from chamber A** — 初始旋转 `0 rad`（默认）| 标量

仿真开始时执行器的位置。在正方向上，此值介于 `0` 与 **Stroke** 的值之间；在负方向上，此值介于 `0` 与 **Stroke** 的负值之间。

#### 依赖关系

要启用此参数，请将 **Shaft rotation from chamber A** 设置为 `Calculate from velocity of port R relative to port C`。

### **Enable dynamic compressibility** — 流体可压缩性 `On`（默认）| `Off`

是否对由于流体可压缩性引起的流体密度变化建模。当 **Fluid compressibility** 设置为 `On` 时，除了由于压力变化引起的密度变化外，还会计算由于进入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **Initial liquid pressure in chamber A** — 液体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时执行器腔室 A 中的压力。

#### 依赖关系

要启用此参数，请将 **Enable dynamic compressibility** 设置为 `On`。

### **Initial liquid pressure in chamber B** — 液体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时执行器腔室 B 中的压力。

#### 依赖关系

要启用此参数，请将 **Enable dynamic compressibility** 设置为 `On`。

### **Nominal liquid pressure in chamber A** — 腔室 A 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 A 中额定工况下的液体压力。当动态可压缩性禁用时，模块使用此值计算质量守恒方程中要使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid pressure in chamber B** — 腔室 B 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 B 中额定工况下的液体压力。当动态可压缩性禁用时，模块使用此值计算质量守恒方程中要使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a: 在执行器每一侧建模不同流体

清除新的 **Same fluid on both sides** 参数，以阻止流体属性传播，并将每个腔室建模为连接到其自身隔离流体网络的不同流体。

### R2023a: 新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。此选项称为 `Based on coefficient of restitution`，使用模式图对硬限位建模。

## 描述

等温液体系统中的双作用旋转执行器

Double-Acting Rotary Actuator (IL) 模块对等温液体网络中的旋转执行器建模。该执行器将两个腔室之间的压差转换为机械扭矩。当活塞接近完全伸出或完全缩回时，其运动受到四种硬限位模型之一的限制。

端口 **A** 和 **B** 是分别与腔室 A 和腔室 B 的入口关联的等温液体守恒端口。端口 **R** 与执行器轴关联，端口 **C** 与参考执行器壳体关联。如果 **Mechanical orientation** 设置为 `Pressure at A causes positive rotation of R relative to C`，则腔室 A 中的压力会使端口 **R** 处的轴相对于端口 **C** 产生正旋转。当轴角度在内部计算时，物理信号端口 **q** 报告轴角度。当角度通过连接到 Simscape™ Multibody™ 关节设置时，它作为物理信号在端口 **q** 接收。

### 位移

活塞位移以端口 **R** 相对于端口 **C** 的位置来测量。**Mechanical orientation** 标识活塞位移的方向。当腔室容积等于腔室死区容积时，活塞位移为中性，即 `0`。当位移作为输入接收时，确保位置的导数等于活塞速度。当输入来自连接到 Simscape Multibody 关节的 Rotational Multibody Interface 模块时，会自动满足此条件。

### 硬限位模型

为避免执行器在完全伸出或完全缩回时发生机械损坏，当活塞接近这些限位时，执行器通常表现出非线性行为。Single-Acting Rotary Actuator (IL) 模块通过四种硬限位模型的选择来对此行为建模，这些模型通过弹簧-阻尼器系统对材料柔度建模。硬限位模型包括：

- `Stiffness and damping applied smoothly through transition region, damped rebound`。
- `Full stiffness and damping applied at bounds, undamped rebound`。
- `Full stiffness and damping applied at bounds, damped rebound`。
- `Based on coefficient of restitution`。

当活塞处于其上限或下限时，对硬限位力建模。边界区域位于 **Stroke** 或活塞初始位移的 **Transition region** 内。在此区域之外，FHardStop=0。

有关这些设置的详细信息，请参阅 Rotational Hard Stop 模块页面。

### 模块示意图

Double-Acting Rotary Actuator (IL) 模块包含三个 Foundation Library 模块：

- Ideal Rotational Motion Sensor
- Rotational Hard Stop
- Rotational Mechanical Converter (IL)

**底层模块组件**

### 泄漏

Double-Acting Rotary Actuator (IL) 模块中未考虑层流泄漏。要在仿真中包含泄漏，请将 **Cross-sectional geometry** 参数设置为 `Custom`，并将端口 **A** 和 **B** 连接到 Laminar Leakage (IL) 模块的端口 **A** 和 **B**。

**将泄漏添加到仿真中**
