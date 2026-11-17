---
type: simulink-block
title: 'Double-Acting Servo Valve Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces'
documentation_page: 'doubleactingservovalveactuatoril'
documentation_source_path: 'ref/doubleactingservovalveactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Servo Valve Actuator (IL)

## 端口

### 守恒端口

### **A** — 腔 A 的液体端口，等温液体

与腔 A 的液体入口关联的等温液体守恒端口。

### **B** — 腔 B 的液体端口，等温液体

与腔 B 的液体入口关联的等温液体守恒端口。
### 输出

### **S** — 阀芯位置，m，物理信号

与阀芯位置关联的物理信号，单位为 m。位置为零表示阀芯处于行程中间的中位。

## 参数

### 执行器

### **Spool cross-sectional area** — 面积测量 `1e-4 m^2`（默认）| 正标量

阀芯的横截面积

### **Spool stroke** — 距离 `5e-3 m`（默认）| 正标量

阀芯在一次行程中移动的距离。

### **Spring stiffness** — 弹簧的力变化率 `1e3 N/m`（默认）| 标量

对中弹簧的弹簧刚度。

### **Damping coefficient** — 阻尼系数 `150 N/(m/s)`（默认）| 正标量

活塞与壳体之间接触的阻尼系数。

### 硬限位

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时的力模型选择。有关更多信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

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

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

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

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。在活塞最大伸出量和活塞最大缩回量的此范围之外，不应用 **Hard stop model**，并且活塞上没有附加力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 效应和初始条件

### **Spool initial displacement** — 阀芯的初始位置 `0 m`（默认）| 标量

当阀芯的初始位移设置为 0 时，阀芯直接位于腔 A 和腔 B 之间。正距离使阀芯远离腔 A，而负值使阀芯朝向腔 A 移动。

### **Enable dynamic compressibility** — 流体可压缩性 `On`（默认）| `Off`

是否对由流体可压缩性引起的任何流体密度变化进行建模。当 **Enable dynamic compressibility** 设置为 `On` 时，除了由压力变化引起的密度变化外，还会计算由流入模块的质量流量引起的变化。在等温液体库中，所有模块都将密度计算为压力的函数。

### **Nominal liquid pressure in chamber A** — 腔 A 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔 A 中额定工况下的液体压力。当禁用动态可压缩性时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid pressure in chamber B** — 腔 B 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔 B 中额定工况下的液体压力。当禁用动态可压缩性时，模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial liquid pressure in chamber A** — 液体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时执行器腔 A 中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Initial liquid pressure in chamber B** — 液体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时执行器腔 B 中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数新增了一个选项。此选项称为 `Based on coefficient of restitution`，使用模式图对硬限位进行建模。

## 描述

等温液体系统中带弹簧对中阀芯的双作用伺服缸

Double-Acting Servo Valve Actuator (IL) 模块对布置为弹簧对中阀芯的双作用伺服缸进行建模。弹簧中性位置是阀芯位于行程中间的位置。活塞在接近完全伸出或完全缩回时的运动受到四种硬限位模型之一的限制。可选地对两个活塞腔中的流体可压缩性进行建模。

物理信号输出 **S** 报告阀芯位置。

### 硬限位模型

为避免执行器在完全伸出或完全缩回时发生机械损坏，执行器通常在活塞接近这些限位时表现出非线性行为。Double-Acting Servo Valve Actuator (IL) 模块通过选择四种硬限位模型之一来对此行为进行建模，这些模型通过弹簧-阻尼器系统对材料柔度进行建模。硬限位模型包括：

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`。
- `Full stiffness and damping applied at bounds, undamped
  rebound`。
- `Full stiffness and damping applied at bounds, damped
  rebound`。
- `Based on coefficient of restitution`

当活塞处于其上限或下限时，对硬限位力进行建模。边界区域位于 **Spool stroke** 或活塞初始位移的 **Transition region** 内。在此区域之外，FHardStop=0。

有关这些设置的更多信息，请参阅 Translational Hard Stop 模块页面。

### 模块原理图

Double-Acting Servo Actuator 模块由一个等温液体库模块和两个 Simscape Foundation 模块组成：

- Double-Acting Actuator (IL)
- Translational Spring
- Translational Damper
