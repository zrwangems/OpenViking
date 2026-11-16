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

### 守恒

### **C** — 壳体机械平移

与减震器一端关联的机械平移守恒端口。正力从端口 **R** 作用到端口 **C**。

### **R** — 活塞杆机械平移

与减震器一端关联的机械平移守恒端口。正力从端口 **R** 作用到端口 **C**。

## 参数

### 弹簧-阻尼器

### **弹簧刚度** — 弹簧的刚度 `1e4` `N/m`（默认）| 非负标量

弹簧刚度常数的值，*k*。

### **粘性摩擦系数** — 粘性摩擦系数 `1e2` `N*s/m`（默认）| 非负标量

粘性阻尼常数的值，*b*。

### **库仑摩擦力** — 库仑摩擦力 `0` `N`（默认）| 非负标量

库仑摩擦力的值。将该值设置为 `0` 可消除库仑摩擦力贡献，这会提高仿真速度并使模型更适合 HIL 测试。

### **静摩擦与动摩擦之比** — 静摩擦与动摩擦之比 `1.1`（默认）| 大于或等于 1 的标量

静摩擦与动摩擦之比的值，*Fs*/*Fk*。

### **速度容差** — 滑移速度阈值 `0.001` `m/s`（默认）| 正标量

相对速度的值，低于该值时端口 **R** 和 **C** 锁定并一起平移。当相对速度大于该值时，端口彼此相对滑动。

### 硬限位

### **硬限位** — 硬限位选项 `No hard stops - Suitable for HIL simulation`（默认）| `Compliant hard stops`

是否对平移硬限位建模。从以下选项中选择：

- `No hard stops — Suitable for HIL simulation` — 通过排除硬限位力贡献来提高仿真速度。
- `Compliant hard stops` — 通过包含硬限位力贡献来提高模型保真度。

### **上限** — 滑块与上限之间的间隙 `0.1` `m`（默认）| 标量

上限硬限位位置，*UB*。超过上限的正位移会激活硬限位接触力。该值必须大于 **下限** 参数。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Compliant hard stops`。

### **下限** — 滑块与下限之间的间隙 `-0.1` `m`（默认）| 标量

下限硬限位位置，*LB*。超过下限的负位移会激活硬限位接触力。该值必须小于 **上限** 参数。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Compliant hard stops`。

### **接触刚度** — 接触刚度常数 `1e6` `N/m`（默认）| 非负标量

硬限位刚度常数的值，*kHS*。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Compliant hard stops`。

### **接触阻尼** — 接触阻尼常数 `1e4` `N*s/m`（默认）| 正标量

硬限位阻尼常数的值，*bHS*。此参数指定碰撞物体的耗散属性。该参数的值越大，硬限位在一次相互作用期间耗散的能量就越多。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Compliant hard stops`。

### **硬限位模型** — 硬限位过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| ...

硬限位模型的刚度和反弹选项。该模块使用 Translational Hard Stop 模块的复合实现。您可以从以下选项中选择：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`
- `Based on coefficient of restitution`

### **过渡区域** — 硬限位过渡距离 `0.1` `mm`（默认）| 正标量

力从零逐渐增大到完整值的区域。在过渡区域末端，模块施加完整刚度和阻尼。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 介于 0 和 1 之间的无量纲值

滑块弹跳后，滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Compliant hard stops`，并将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位之间的阈值相对速度 `0.001` `m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于此参数值的速度撞击壳体时，它们保持接触。否则，滑块会弹跳。为避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Compliant hard stops`，并将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

### **静态接触释放力阈值** — 从接触模式转换为自由模式所需的阈值扭矩 `0.001` `N`（默认）

使滑块从静态接触模式释放所需的最小扭矩。

#### 依赖关系

要启用此参数，请将 **硬限位** 设置为 `Compliant hard stops`，并将 **硬限位模型** 设置为 `Based on coefficient of restitution`。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中推出**

### R2023a：复合硬限位更新

由于 Translational Hard Stop 模块的更新，**硬限位模型** 参数现在提供 `Coefficient of restitution` 选项。

## 描述

吸收平移冲击的弹簧和阻尼器系统

Shock Absorber 模块表示一个吸收振动的弹簧-阻尼器系统。内力作用在端口 **R** 和 **C** 之间。该力是弹簧刚度、阻尼、库仑摩擦和硬限位贡献之和。所有力贡献都是可选的。

减震器示意图，其中端口 R 位于端口 C 的对端。

该模块由以下模块复合而成：

| 模块 | 功能 | 所属库 |
| --- | --- | --- |
| Loaded-Contact Translational Friction | 库仑摩擦 | **Simscape** / **Driveline** / **Brakes & Detents** / **Translational** |
| Translational Damper | 阻尼 | **Simscape** / **Foundation Library** / **Mechanical** / **Translational Elements** |
| Translational Spring | 弹簧 |
| Translational Hard Stop | 硬限位 |

### 假设和限制

- 将 **硬限位** 设置为 `Compliant hard stop` 或将 **库仑摩擦力** 设置为非零值，可提高模型保真度，但会降低仿真速度。有关详细信息，请参阅 Driveline Simulation Performance。
