---
type: simulink-block
title: 'Torsional Spring-Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Coupling and Drive Assemblies'
documentation_page: 'torsionalspringdamper'
documentation_source_path: 'ref/torsionalspringdamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Torsional Spring-Damper

## 端口

### 守恒

### **C** — 随动端口机械旋转

与在安装于壳体上的限位之间移动的滑块关联的机械旋转端口。

### **R** — 基座端口机械旋转

与杆关联的机械旋转端口。

## 参数

### 弹簧-阻尼器

### **弹簧刚度** — 作用在连接传动轴上的扭转弹簧刚度 `1000` `N*m/rad`（默认）| 非负标量

作用在连接传动轴上的扭转弹簧刚度。

### **粘性摩擦系数** — 作用在连接传动轴上的扭转粘性摩擦 `10` `N*m/(rad/s)`（默认）| 非负标量

作用在连接传动轴上的扭转摩擦。

### **库仑摩擦力矩** — 动摩擦力矩 `0` `N*m`（默认）| 非负标量

作用在连接传动轴上的恒定动摩擦力矩。该恒定扭矩在任何速度下都阻碍旋转。

### **静摩擦与动摩擦之比** — 相对于动摩擦的静摩擦 `1.1`（默认）| 正标量

作用在连接传动轴上的静态库仑摩擦力矩与动态库仑摩擦力矩的恒定比值。该值必须大于或等于一。

### **速度容差** — 配合传动轴差速容差 `0.001` `rad/s`（默认）| 正标量

两个连接的传动轴可以锁定并一起旋转的最小相对角速度。

### 硬停止

### **硬停止** — 模拟边界硬停止 `No hard stops - Suitable for HIL simulation`（默认）| `Compliant hard stops`

通过选择以下选项之一来包含或排除硬停止扭矩：

- `No hard stops - Suitable for HIL simulation` — 选择此选项可通过排除硬停止扭矩贡献来提高仿真速度。
- `Compliant hard stops` — 选择此选项可通过包含硬停止扭矩贡献来提高模型保真度。

### **上界** — 上硬停止的位置 `10` `deg`（默认）| 标量

相对于零扭矩参考角的上硬停止角位移。该值必须大于 **下界** 参数。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`。

### **下界** — 下硬停止的位置 `-10` `deg`（默认）| 标量

相对于零弹簧力参考角的下硬停止角位移。该值必须小于 **上界** 参数。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`。

### **接触刚度** — 硬停止比例弹簧常数 `1e6` `N*m/(rad/s)`（默认）| 非负标量

硬停止刚度。仅当相对角度进入硬停止区域时，此值才适用。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`。

### **接触阻尼** — 硬停止比例阻尼 `10` `(N*m)/(rad/s)`（默认）| 正标量

硬停止阻尼。仅当相对角度进入硬停止区域时，此值才适用。该值必须大于零。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`。

### **硬停止模型** — 硬停止过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| ...

硬停止模型的刚度和回弹选项。该模块使用 Rotational Hard Stop 模块的复合实现。您可以从以下选项中选择：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`
- `Based on coefficient of restitution`

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`。

### **过渡区域** — 部分硬停止效应的区域 `0.001` `rad`（默认）| 正标量

距离完全压缩或完全伸长的距离，在此距离内部分施加刚度和阻尼效应。当您将 **硬停止模型** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound` 时，随着弹簧接近完全伸长或完全压缩，该模块会平滑过渡刚度和阻尼的起始。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`，并将 **硬停止模型** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **恢复系数** — 碰撞后滑块与限位之间最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无量纲值

滑块弹跳后，滑块与限位之间最终相对速度与初始相对速度之比。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`，并将 **硬停止模型** 设置为 `Based on coefficient of restitution`。

### **静态接触速度阈值** — 碰撞前滑块与限位之间的阈值相对速度 `0.1` `rad/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于此参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。要避免对滑块与壳体之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`，并将 **硬停止模型** 设置为 `Based on coefficient of restitution`。

### **静态接触释放扭矩阈值** — 从接触模式过渡到自由模式所需的阈值力 `0.001` `N*m`（默认）

将滑块从静态接触模式释放所需的最小力。

#### 依赖项

要启用此参数，请将 **硬停止** 设置为 `Compliant hard stops`，并将 **硬停止模型** 设置为 `Based on coefficient of restitution`。

### 初始条件

### **初始变形** — 起始变形值 `0` `deg`（默认）| 标量

扭转弹簧相对于零扭矩参考角的初始变形。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2023a：复合硬停止更新

由于 Rotational Hard Stop 模块的更新，**硬停止模型**参数现在具有 `Coefficient of restitution` 选项。

## 描述

具有库仑摩擦、锁定和硬停止的旋转弹簧和阻尼器耦合

Torsional Spring-Damper 模块表示一个旋转弹簧和阻尼器，它在两个连接的传动轴轴线（杆和壳体）之间施加内部生成的扭矩组合。该模块使用以下行为定义扭矩：

- 线性阻尼弹簧
- 库仑摩擦（包括锁定静摩擦）
- 硬停止柔度

该模块是一个复合组件，由以下模块组成：

| 模块 | 作用 | 所属库 |
| --- | --- | --- |
| Loaded-Contact Rotational Friction | 库仑摩擦 | **Simscape** / **Driveline** / **Brakes & Detents** / **Rotational** |
| Rotational Damper | 阻尼 | **Simscape** / **Foundation Library** / **Mechanical** / **Rotational Elements** |
| Rotational Spring | 弹簧 |
| Rotational Hard Stop | 硬停止 |

有关更多信息，请参阅复合组件。

### 假设和限制

- 包含硬停止和库仑摩擦可提高模型保真度，但会降低仿真速度。有关更多信息，请参阅传动系统仿真性能。
