---
type: simulink-block
title: 'Torsional Spring-Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'torsionalspringdamper'
documentation_source_path: 'ref/torsionalspringdamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Torsional Spring-Damper

## 端口
```yaml
ports:
- name: C
  summary: 从动端口机械旋转
  direction: conserving
- name: R
  summary: 基础端口机械旋转
  direction: conserving
```

### 守恒端口

### **C** — 从动端口机械旋转

与在安装于壳体上的限位挡块之间移动的滑块相关联的机械旋转端口。

### **R** — 基础端口机械旋转

与杆相关联的机械旋转端口。
## 参数
```yaml
parameters:
- name: Spring stiffness
  summary: 扭转弹簧刚度 1000 N*m/rad（默认）| 非负标量
  group: 弹簧-阻尼器
- name: Viscous friction coefficient
  summary: 扭转粘性摩擦 10 N*m/(rad/s)（默认）| 非负标量
  group: 弹簧-阻尼器
- name: Coulomb friction torque
  summary: 动摩擦力矩 0 N*m（默认）| 非负标量
  group: 弹簧-阻尼器
- name: Ratio of static to kinetic friction
  summary: 静摩擦相对于动摩擦 1.1（默认）| 正标量
  group: 弹簧-阻尼器
- name: Velocity tolerance
  summary: 配合传动轴差速容差 0.001 rad/s（默认）| 正标量
  group: 弹簧-阻尼器
- name: Hard stop
  summary: 模拟边界硬限位 No hard stops - Suitable for HIL simulation（默认）| Compliant hard stops
  group: 硬限位
- name: Upper bound
  summary: 上限硬限位位置 10 deg（默认）| 标量
  group: 硬限位
- name: Lower bound
  summary: 下限硬限位位置 -10 deg（默认）| 标量
  group: 硬限位
- name: Contact stiffness
  summary: 硬限位比例弹簧常数 1e6 N*m/(rad/s)（默认）| 非负标量
  group: 硬限位
- name: Contact damping
  summary: 硬限位比例阻尼 10 (N*m)/(rad/s)（默认）| 正标量
  group: 硬限位
- name: Hard stop model
  summary: 硬限位过渡行为 Stiffness and damping applied smoothly through transition region, damped rebound（默认）| ...
  group: 硬限位
- name: Transition region
  summary: 部分硬限位效应区域 0.001 rad（默认）| 正标量
  group: 硬限位
- name: Coefficient of restitution
  summary: 碰撞后滑块与挡块之间最终相对速度与初始相对速度之比 0.7（默认）| 介于 0 和 1 之间的无量纲值
  group: 硬限位
- name: Static contact speed threshold
  summary: 碰撞前滑块与挡块之间的阈值相对速度 0.1 rad/s（默认）| 非负标量
  group: 硬限位
- name: Static contact release torque threshold
  summary: 从接触模式过渡到自由模式所需的阈值力 0.001 N*m（默认）
  group: 硬限位
- name: Initial deformation
  summary: 起始变形值 0 deg（默认）| 标量
  group: 初始条件
```

### 弹簧-阻尼器

### **Spring stiffness** — 扭转弹簧刚度 `1000` `N*m/rad`（默认）| 非负标量

作用于所连接传动轴的扭转弹簧刚度。

### **Viscous friction coefficient** — 扭转粘性摩擦 `10` `N*m/(rad/s)`（默认）| 非负标量

作用于所连接传动轴的扭转摩擦。

### **Coulomb friction torque** — 动摩擦力矩 `0` `N*m`（默认）| 非负标量

作用于所连接传动轴的恒定动摩擦力矩。该恒定力矩在任何速度下均阻碍旋转。

### **Ratio of static to kinetic friction** — 静摩擦相对于动摩擦 `1.1`（默认）| 正标量

作用于所连接传动轴的静库仑摩擦力矩与动库仑摩擦力矩的恒定比值。该值必须大于或等于一。

### **Velocity tolerance** — 配合传动轴差速容差 `0.001` `rad/s`（默认）| 正标量

两个所连接传动轴可以锁定并一起旋转的最小相对角速度。

### 硬限位

### **Hard stop** — 模拟边界硬限位 `No hard stops - Suitable for HIL simulation`（默认）| `Compliant hard stops`

通过选择以下选项之一来包含或排除硬限位力矩：

- `No hard stops - Suitable for HIL
  simulation` — 选择此选项可通过排除硬限位力矩贡献来提高仿真速度。
- `Compliant hard stops` — 选择此选项可通过包含硬限位力矩贡献来提高模型保真度。

### **Upper bound** — 上限硬限位位置 `10` `deg`（默认）| 标量

相对于零力矩参考角的上限硬限位角位移。该值必须大于 **Lower bound** 参数。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`。

### **Lower bound** — 下限硬限位位置 `-10` `deg`（默认）| 标量

相对于零弹簧力参考角的下限硬限位角位移。该值必须小于 **Upper bound** 参数。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`。

### **Contact stiffness** — 硬限位比例弹簧常数 `1e6` `N*m/(rad/s)`（默认）| 非负标量

硬限位刚度。仅当相对角度进入硬限位区域时，此值才适用。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`。

### **Contact damping** — 硬限位比例阻尼 `10` `(N*m)/(rad/s)`（默认）| 正标量

硬限位阻尼。仅当相对角度进入硬限位区域时，此值才适用。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`。

### **Hard stop model** — 硬限位过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| ...

硬限位模型的刚度和回弹选项。该模块使用 Rotational Hard Stop 模块的复合实现。您可以从以下选项中选择：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`
- `Based on coefficient of
  restitution`

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`。

### **Transition region** — 部分硬限位效应区域 `0.001` `rad`（默认）| 正标量

距完全压缩或完全伸长的距离，在该距离内部分施加刚度和阻尼效应。当您将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound` 时，该模块会在弹簧接近完全伸长或完全压缩时平滑过渡刚度和阻尼的起始。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`，并将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与挡块之间最终相对速度与初始相对速度之比 `0.7`（默认）| 介于 0 和 1 之间的无量纲值

滑块弹跳后滑块与挡块之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与挡块之间的阈值相对速度 `0.1` `rad/s`（默认）| 非负标量

碰撞前滑块与挡块之间的阈值相对速度。当滑块以小于此参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release torque threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001` `N*m`（默认）

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 初始条件

### **Initial deformation** — 起始变形值 `0` `deg`（默认）| 标量

扭转弹簧相对于零力矩参考角的初始变形。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2023a：复合硬限位更新

由于 Rotational Hard Stop 模块的更新，**Hard stop model** 参数现在具有 `Coefficient of restitution` 选项。

## 描述

具有库仑摩擦、锁定和硬限位的旋转弹簧和阻尼器耦合

Torsional Spring-Damper 模块表示一个旋转弹簧和阻尼器，它在两个所连接的传动轴轴线（杆和壳体）之间施加内部生成的力矩组合。该模块使用以下行为定义力矩：

- 线性阻尼弹簧
- 库仑摩擦（包括锁定静摩擦）
- 硬限位柔顺性

该模块是一个复合组件，由以下模块组成：

| 模块 | 贡献 | 库 |
| --- | --- | --- |
| Loaded-Contact Rotational Friction | 库仑摩擦 | **Simscape** / **Driveline** / **Brakes & Detents** / **Rotational** |
| Rotational Damper | 阻尼 | **Simscape** / **Foundation Library** / **Mechanical** / **Rotational Elements** |
| Rotational Spring | 弹簧 |
| Rotational Hard Stop | 硬限位 |

有关详细信息，请参阅 Composite Components。

### 假设和限制

- 包含硬限位和库仑摩擦可提高模型保真度，但会降低仿真速度。有关详细信息，请参阅 Driveline Simulation Performance。
