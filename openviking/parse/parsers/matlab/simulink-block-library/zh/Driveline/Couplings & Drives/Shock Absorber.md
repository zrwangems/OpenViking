---
type: simulink-block
title: 'Shock Absorber'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'shockabsorber'
documentation_source_path: 'ref/shockabsorber.html'
language: zh-CN
chinese_source: worker-translation
---

# Shock Absorber

## 端口
```yaml
ports:
- name: C
  summary: 壳体机械平移
  direction: conserving
- name: R
  summary: 杆机械平移
  direction: conserving
```

### 守恒端口

### **C** — 壳体机械平移

与减震器一端相关联的机械平移守恒端口。正力从端口 **R** 作用于端口 **C**。

### **R** — 杆机械平移

与减震器一端相关联的机械平移守恒端口。正力从端口 **R** 作用于端口 **C**。
## 参数
```yaml
parameters:
- name: Spring stiffness
  summary: 弹簧刚度 1e4 N/m（默认）| 非负标量
  group: 弹簧-阻尼器
- name: Viscous friction coefficient
  summary: 粘性摩擦系数 1e2 N*s/m（默认）| 非负标量
  group: 弹簧-阻尼器
- name: Coulomb friction force
  summary: 库仑摩擦力 0 N（默认）| 非负标量
  group: 弹簧-阻尼器
- name: Ratio of static to kinetic friction
  summary: 静摩擦与动摩擦之比 1.1（默认）| 大于或等于 1 的标量
  group: 弹簧-阻尼器
- name: Velocity tolerance
  summary: 滑移速度阈值 0.001 m/s（默认）| 正标量
  group: 弹簧-阻尼器
- name: Hard stop
  summary: 硬限位选项 No hard stops - Suitable for HIL simulation（默认）| Compliant hard stops
  group: 硬限位
- name: Upper bound
  summary: 滑块与上限之间的间隙 0.1 m（默认）| 标量
  group: 硬限位
- name: Lower bound
  summary: 滑块与下限之间的间隙 -0.1 m（默认）| 标量
  group: 硬限位
- name: Contact stiffness
  summary: 接触刚度常数 1e6 N/m（默认）| 非负标量
  group: 硬限位
- name: Contact damping
  summary: 接触阻尼常数 1e4 N*s/m（默认）| 正标量
  group: 硬限位
- name: Hard stop model
  summary: 硬限位过渡行为 Stiffness and damping applied smoothly through transition region, damped rebound（默认）| ...
  group: 硬限位
- name: Transition region
  summary: 硬限位过渡距离 0.1 mm（默认）| 正标量
  group: 硬限位
- name: Coefficient of restitution
  summary: 碰撞后滑块与限位之间最终相对速度与初始相对速度之比 0.7（默认）| 0 到 1 之间的无量纲值
  group: 硬限位
- name: Static contact speed threshold
  summary: 碰撞前滑块与限位之间的阈值相对速度 0.001 m/s（默认）| 非负标量
  group: 硬限位
- name: Static contact release force threshold
  summary: 从接触模式过渡到自由模式所需的阈值力矩 0.001 N（默认）
  group: 硬限位
```

### 弹簧-阻尼器

### **Spring stiffness** — 弹簧刚度 `1e4` `N/m`（默认）| 非负标量

弹簧刚度常数的值，*k*。

### **Viscous friction coefficient** — 粘性摩擦系数 `1e2` `N*s/m`（默认）| 非负标量

粘性阻尼常数的值，*b*。

### **Coulomb friction force** — 库仑摩擦力 `0` `N`（默认）| 非负标量

库仑摩擦力的值。将该值设置为 `0` 可消除库仑摩擦力贡献，从而提高仿真速度并使模型更适合 HIL 测试。

### **Ratio of static to kinetic friction** — 静摩擦与动摩擦之比 `1.1`（默认）| 大于或等于 1 的标量

静摩擦力与动摩擦力之比的值，*Fs*/*Fk*。

### **Velocity tolerance** — 滑移速度阈值 `0.001` `m/s`（默认）| 正标量

相对速度的值，低于该值时端口 **R** 和 **C** 锁定并一起平移。当相对速度大于该值时，端口之间相对滑动。

### 硬限位

### **Hard stop** — 硬限位选项 `No hard stops - Suitable for HIL simulation`（默认）| `Compliant hard stops`

是否对平移硬限位进行建模。从以下选项中选择：

- `No hard stops — Suitable for HIL simulation` — 通过排除硬限位力贡献来提高仿真速度。
- `Compliant hard stops` — 通过包含硬限位力贡献来提高模型保真度。

### **Upper bound** — 滑块与上限之间的间隙 `0.1` `m`（默认）| 标量

上限硬限位位置，*UB*。超过上限的正位移会激活硬限位接触力。该值必须大于 **Lower bound** 参数。

#### 依赖关系

要启用此参数，请将 **Hard Stop** 设置为 `Compliant hard stops`。

### **Lower bound** — 滑块与下限之间的间隙 `-0.1` `m`（默认）| 标量

下限硬限位位置，*LB*。超过下限的负位移会激活硬限位接触力。该值必须小于 **Upper bound** 参数。

#### 依赖关系

要启用此参数，请将 **Hard Stop** 设置为 `Compliant hard stops`。

### **Contact stiffness** — 接触刚度常数 `1e6` `N/m`（默认）| 非负标量

硬限位刚度常数的值，*kHS*。

#### 依赖关系

要启用此参数，请将 **Hard Stop** 设置为 `Compliant hard stops`。

### **Contact damping** — 接触阻尼常数 `1e4` `N*s/m`（默认）| 正标量

硬限位阻尼常数的值，*bHS*。此参数指定碰撞物体的耗散特性。该参数值越大，硬限位在交互过程中耗散的能量越多。

#### 依赖关系

要启用此参数，请将 **Hard Stop** 设置为 `Compliant hard stops`。

### **Hard stop model** — 硬限位过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| ...

硬限位模型的刚度和回弹选项。该模块使用 Translational Hard Stop 模块的复合实现。您可以从以下选项中选择：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`
- `Based on coefficient of restitution`

### **Transition region** — 硬限位过渡距离 `0.1` `mm`（默认）| 正标量

力从零逐渐增大到满值的区域。在过渡区域末端，模块施加满刚度和阻尼。

#### 依赖关系

要启用此参数，请将 **Hard Stop** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无量纲值

滑块弹回后，滑块与限位之间最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001` `m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于该参数值的速度撞击壳体时，它们保持接触。否则，滑块弹回。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力矩 `0.001` `N`（默认）

将滑块从静态接触模式释放所需的最小力矩。

#### 依赖关系

要启用此参数，请将 **Hard stop** 设置为 `Compliant hard stops`，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

### R2023a：复合硬限位更新

由于 Translational Hard Stop 模块的更新，**Hard stop model** 参数现在具有 `Coefficient of restitution` 选项。

## 描述

吸收平移冲击的弹簧和阻尼器系统

Shock Absorber 模块表示一个吸收振动的弹簧-阻尼器系统。内力作用于端口 **R** 和 **C** 之间。该力是弹簧刚度、阻尼、库仑摩擦和硬限位贡献之和。所有力贡献均为可选。

减震器示意图，端口 R 位于端口 C 的另一端。

该模块是以下模块的复合：

| 模块 | 功能 | 所属库 |
| --- | --- | --- |
| Loaded-Contact Translational Friction | 库仑摩擦 | **Simscape** / **Driveline** / **Brakes & Detents** / **Translational** |
| Translational Damper | 阻尼 | **Simscape** / **Foundation Library** / **Mechanical** / **Translational Elements** |
| Translational Spring | 弹簧 |
| Translational Hard Stop | 硬限位 |

### 假设和限制

- 将 **Hard stop** 设置为 `Compliant hard stop` 或将 **Coulomb friction force** 设置为非零值可提高模型保真度，但会降低仿真速度。有关详细信息，请参阅 Driveline Simulation Performance。
