---
type: simulink-block
title: 'Rotating Single-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'rotatingsingleactingactuatoril'
documentation_source_path: 'ref/rotatingsingleactingactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotating Single-Acting Actuator (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体腔入口端口 等温液体
  direction: conserving
- name: C
  summary: 执行器壳体 机械平移
  direction: conserving
- name: R
  summary: 活塞杆速度 机械平移
  direction: conserving
- name: W
  summary: 执行器旋转速度 物理信号
  direction: input
- name: p
  summary: 活塞位置，m 物理信号
  direction: input
- name: p
  summary: 活塞位置，m 物理信号
  direction: output
```

### 守恒端口

### **A** — 液体腔入口端口 等温液体

液体腔的入口端口。

### **C** — 执行器壳体 机械平移

执行器速度和力的参考端口。

### **R** — 活塞杆速度 机械平移

与活塞速度和力关联的端口。
### 输入

### **W** — 执行器旋转速度 物理信号

执行器旋转速度，以物理信号形式接收，单位为
rad/s。

### **p** — 活塞位置，m 物理信号

活塞位置，单位为 m，以物理信号形式从 Simscape
Multibody 模块接收。

#### 依赖关系

要显示此端口，请将 **Piston displacement**
设置为 `Provide input signal from Multibody
joint`。
### 输出

### **p** — 活塞位置，m 物理信号

活塞位置，单位为 m，以物理信号形式返回。

#### 依赖关系

要显示此端口，请将 **Piston displacement**
设置为 `Calculate from velocity of port R relative to port
C`。
## 参数
```yaml
parameters:
- name: Piston outer radius
  summary: 活塞外半径 0.1 m（默认）| 正标量
  group: 执行器
- name: Piston inner radius
  summary: 活塞内半径 0.05 m（默认）| 正标量
  group: 执行器
- name: Mechanical orientation
  summary: 活塞位移方向 Pressure at A causes positive displacement of R relative to C（默认）| Pressure at A causes negative displacement
    of R relative to C
  group: 执行器
- name: Piston stroke
  summary: 最大活塞行程距离 0.1 m（默认）| 正标量
  group: 执行器
- name: Dead volume
  summary: 活塞完全缩回时的流体体积 1e-5 m^3（默认）| 正标量
  group: 执行器
- name: Environment pressure specification
  summary: 参考环境压力 Atmospheric pressure（默认）| Specified pressure
  group: 执行器
- name: Environment pressure
  summary: 用户定义的环境压力 0.101325 MPa（默认）| 正标量
  group: 执行器
- name: Fluid entry radius
  summary: 流体通道半径 0.06 m（默认）| 正标量
  group: 流体通道
- name: Fluid channel cross-sectional area
  summary: 流体横截面积 1e-3 m^2（默认）| 正标量
  group: 流体通道
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: 流体通道
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: 流体通道
- name: Hard stop model
  summary: 选择硬限位模型 Stiffness and damping applied smoothly through transition region, damped rebound（默认）| Full stiffness and
    damping applied at bounds, undamped rebound | Full stiffness and damping applied at bounds, damped rebound | Based on
    coefficient of restitution
  group: 硬限位
- name: Hard-stop stiffness coefficient
  summary: 刚度系数 1e10 N/m（默认）| 正标量
  group: 硬限位
- name: Hard-stop damping coefficient
  summary: 阻尼系数 150 N*s/m（默认）| 正标量
  group: 硬限位
- name: Transition region
  summary: 硬限位力模型的应用范围 0.1 mm（默认）| 正标量
  group: 硬限位
- name: Coefficient of restitution
  summary: 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 0.7（默认）| 0 到 1 之间的无单位值
  group: 硬限位
- name: Static contact speed threshold
  summary: 碰撞前滑块与限位之间的阈值相对速度 0.001 m/s（默认）| 非负标量
  group: 硬限位
- name: Static contact release force threshold
  summary: 从接触模式过渡到自由模式所需的阈值力 0.001 N（默认）| 正标量
  group: 硬限位
- name: Piston displacement
  summary: 确定活塞位置的方法 Calculate from velocity of port R relative to port C（默认）| Provide input signal from Multibody joint
  group: 初始条件
- name: Initial piston displacement
  summary: 仿真开始时的活塞位置 0 m（默认）| 标量
  group: 初始条件
- name: Enable dynamic compressibility
  summary: 是否对流体可压缩性进行建模 on（默认）| off
  group: 初始条件
- name: Initial liquid pressure
  summary: 可压缩流体的起始液体压力 0.101325 MPa（默认）| 正标量
  group: 初始条件
- name: Nominal liquid pressure
  summary: 标称工况下的压力 0.101325 MPa（默认）| 标量
  group: 初始条件
```

### 执行器

### **Piston outer radius** — 活塞外半径 `0.1 m`（默认）| 正标量

活塞外半径。

### **Piston inner radius** — 活塞内半径 `0.05 m`（默认）| 正标量

活塞内半径。

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

设置活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C` 时，当端口
  **A** 处的液体体积膨胀时，活塞位移为
  正值。这对应于活塞杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C` 时，当端口
  **A** 处的液体体积膨胀时，活塞位移为
  负值。这对应于活塞杆缩回。

### **Piston stroke** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume** — 活塞完全缩回时的流体体积 `1e-5 m^3`（默认）| 正标量

活塞位移为 `0` 时的液体体积。
这是活塞紧靠执行器端盖时的液体体积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric
pressure` 选项将环境压力设置为
0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure
specification** 设置为 `Specified
pressure`。

### 流体通道

### **Fluid entry radius** — 流体通道半径 `0.06 m`（默认）| 正标量

旋转轴中流体开口的半径。此值必须大于或等于 **Piston inner radius**
且小于或等于 **Piston outer
radius**。

### **Fluid channel cross-sectional area** — 流体横截面积 `1e-3 m^2`（默认）| 正标量

流体通道的横截面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

流动排放损失系数。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

### 硬限位

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时力的模型选择。有关更多信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。在活塞最大伸出和活塞最大缩回的这一范围之外，
不应用 **Hard stop model**，并且活塞上没有
额外的力。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。
当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们
保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态
接触进行建模，请将此参数设置为
`0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### 初始条件

### **Piston displacement** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input
signal from Multibody joint` 时，模块可以从 Multibody 模块接收
位置，或者内部计算位置并在端口
**p** 报告位置。当机械方向为正时，位置介于 `0`
和 **Piston stroke** 之间；当机械方向为
负时，位置介于 `0` 和 –**Piston
stroke** 之间。

### **Initial piston displacement** — 仿真开始时的活塞位置 `0 m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston
displacement** 设置为 `Calculate from velocity
of port R relative to port C`。

### **Enable dynamic compressibility** — 是否对流体可压缩性进行建模 `on`（默认）| `off`

是否对由流体可压缩性引起的任何流体密度变化进行建模。当您选中 **Enable dynamic
compressibility** 时，除了由压力变化引起的密度变化外，还会计算由流入模块的质量流量引起的
变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为
压力的函数。

### **Initial liquid pressure** — 可压缩流体的起始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic
compressibility**。

### **Nominal liquid pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的液体压力。当禁用动态可压缩性时，模块使用此
值计算用于质量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic
compressibility** 复选框。
## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。
此选项称为 `Based on coefficient of restitution`，
使用模式图对硬限位进行建模。

## 描述

等温液体网络中旋转轴上的执行器

Rotating Single-Acting Actuator (IL) 模块对等温液体网络中绕其中心轴旋转的执行器进行建模。旋转执行器用于
旋转轴控制组件，例如摩擦离合器或制动器。流体在端口 **A** 进入
执行器。角速度在端口
**W** 设置。端口 **C** 与执行器
壳体关联，活塞速度和力在端口 **R** 设置。

当活塞位置在内部计算时，它在端口
**p** 报告；当位置通过与 Simscape™
Multibody™ 关节的连接设置时，它作为物理信号在端口 **p**
接收。
活塞在接近完全伸出或完全缩回时的运动受到
四种硬限位模型之一的限制。可以选择性地对 **Enable dynamic compressibility** 进行建模。

### 位移

活塞位移以端口 **R**
相对于端口 **C** 的位置来测量。**Mechanical
orientation** 标识活塞位移的方向。当腔室体积等于
**Dead volume** 时，活塞位移为中性，即 `0`。当位移作为
输入接收时，确保位置的导数等于活塞速度。
当输入从 Translational Multibody Interface 模块
连接到 Simscape Multibody 关节接收时，会自动满足此条件。

### 硬限位模型

为避免执行器在完全伸出或完全
缩回时发生机械损坏，执行器通常在活塞
接近这些限位时表现出非线性行为。Double-Acting Actuator (IL) 模块通过
四种硬限位模型的选择对此行为进行建模，这些模型通过
弹簧-阻尼器系统对材料柔度进行建模。硬限位模型包括：

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`。
- `Full stiffness and damping applied at bounds, undamped
  rebound`。
- `Full stiffness and damping applied at bounds, damped
  rebound`。
- `Based on coefficient of restitution`

硬限位力在活塞处于其上限或下限时进行建模。
边界区域位于 **Piston stroke** 或活塞初始位移的 **Transition region** 内。在此区域之外，FHardStop=0。

有关这些设置的更多信息，请参阅 Translational Hard Stop 模块页面。

### 模块子组件

Rotating Single-Acting Actuator (IL) 模块包含三个 Isothermal Liquid
库模块：

- Rotating Channel (IL)
- Single-Acting Actuator (IL)
- Rotating Cylinder Force (IL)

**执行器示意图**
