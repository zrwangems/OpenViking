---
type: simulink-block
title: 'Tire (Friction Parameterized)'
family: 'tires-vehicles'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'tirefrictionparameterized'
documentation_source_path: 'ref/tirefrictionparameterized.html'
language: zh-CN
chinese_source: worker-translation
---

# Tire (Friction Parameterized)

## 端口

### 输入

### **N** — 法向力，N 物理信号

与作用在轮胎上的法向力关联的物理信号输入端口，单位为 N。如果法向力向下作用在轮胎上，将轮胎压向路面，则为正。

### **M** — 摩擦系数，无量纲物理信号 | 二元素向量

与无量纲静摩擦系数和动摩擦系数（分别为 *μs* 和 *μk*）关联的物理信号输入端口。请以二元素向量形式提供摩擦系数，按 [*μs*, *μk*] 的顺序指定。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Physical signal friction coefficients`。

### 输出

### **S** — 滑移，无量纲或单位为 rad/s 的物理信号

与轮胎和道路之间的滑移关联的物理信号输出端口，无量纲或单位为 rad/s。当您将 **Output type** 设置为：

- `Relative` 时，该端口输出无量纲的相对滑移。
- `Absolute` 时，该端口输出以 rad/s 为单位的绝对滑移。

### 守恒

### **A** — 车轴机械旋转

与车轴关联的机械旋转守恒端口。

### **H** — 轮毂机械旋转

与轮毂关联的机械旋转端口。

## 参数

### 主要

### **Rolling radius** — 空载轮胎-车轮半径 `0.3` `m` (默认) | 正标量

路面与轮胎中心之间的距离。

### **Slip output type** — 相对或绝对切换选项 `Relative` (默认) | `Absolute`

模块使用相对滑移还是绝对滑移摩擦参数化。

### **Friction model** — 摩擦模型 `Fixed kinetic friction coefficient` (默认) | `Table lookup kinetic friction coefficient` | `Physical signal friction coefficients`

模块在仿真期间使用的摩擦模型。当您选择：

- `Fixed kinetic friction coefficient` 时，模块使用您指定的恒定静摩擦系数和动摩擦系数。
- `Table lookup kinetic friction coefficient` 时，您可以使用查表指定摩擦。模块将静摩擦系数视为常数，并将动摩擦系数视为常数或轮胎滑移的函数。使用此设置可仿真恒定路面条件下的轮胎动力学。
- `Physical signal friction coefficients` 时，模块启用端口 **M**，供您提供 [*μs*, *μk*]。使用此设置可仿真可变路面条件下的轮胎动力学。

### **Static friction coefficient** — 静摩擦系数 `0.90` (默认) | 正标量

在轮胎开始滑移之前，允许的纵向力与法向力之比，*μs*。此参数的值必须大于 **Kinetic friction coefficient** 参数或 **Kinetic friction coefficient vector** 参数中的最大值。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Table lookup kinetic friction coefficient`。

### **Kinetic friction coefficient** — 动摩擦系数 `0.70` (默认) | 正标量

在轮胎滑移期间，传递到路面的纵向力与法向力之比，*μk*。该比值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Fixed kinetic friction coefficient`。

### **Tire slip vector** — 轮胎滑移 `[0, .02, .06, .15, .6, 1]` `rad/s` (默认) | 向量

参考轮胎滑移。此向量中的元素与 **Kinetic friction coefficient vector** 参数一一对应。如果 **Tire slip vector** 参数仅包含非负值，则模块假定滑移-摩擦函数关于滑移轴对称。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.89, .88, .8, .75, .7, .7]` (默认) | 向量

给定轮胎滑移下的动摩擦系数。此向量中的元素与 **Tire slip vector** 参数一一对应。这些向量的大小必须相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### **Interpolation method** — 插值方法 `Linear` (默认) | `Smooth`

查表用于处理轮胎滑移-动摩擦系数特性的插值方法。为优先考虑性能，请选择 `Linear`。为生成具有连续一阶导数的连续曲线，请选择 `Smooth`。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### **Extrapolation method** — 外插方法 `Linear` (默认) | `Nearest` | `Error`

查表用于处理轮胎滑移-动摩擦系数特性的外插方法。为生成：

- `Linear` — 选择此选项可生成在外插区域以及与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点且不低于数据中最低点的外插。
- `Error` — 当您希望数据位于表范围内时，选择此选项可避免进入外插模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### 动力学

### **Compliance** — 动力学柔量模型 `No compliance - Suitable for HIL simulation` (默认) | `Specify stiffness and damping`

轮胎动力学柔量的模型。

- `No compliance - Suitable for HIL simulation` — 模块忽略动力学柔量。
- `Specify stiffness and damping` — 模块将轮胎视为在载荷下变形的刚性、阻尼弹簧。

### **Longitudinal stiffness** — 纵向刚度 `1e6` `N/m` (默认) | 正标量

轮胎纵向刚度，*CFx*。

#### 依赖关系

要启用此参数，请将 **Compliance** 设置为 `Specify stiffness and damping`。

### **Longitudinal damping** — 纵向阻尼 `1000` `N/(m/s)` (默认) | 正标量

轮胎纵向阻尼，*bFx*。

#### 依赖关系

要启用此参数，请将 **Compliance** 设置为 `Specify stiffness and damping`。

### **Inertia** — 惯量选项 `No inertia` (默认) | `Specify inertia and initial velocity`

是否仿真轮胎转动惯量。当您选择

- `No inertia` — 模块忽略惯量。
- `Specify inertia and initial velocity` — 模块将轮胎视为在载荷下变形的刚性、阻尼弹簧。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Tire inertia** — 轮胎转动惯量 `1` `kg*m^2` (默认) | 正标量

车轮-轮胎总成的转动惯量，*Iw*。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Initial velocity** — 初始转动速度 `0` `rad/s` (默认) | 标量

轮胎的初始角速度，*Ω(0)*。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### 滚动阻力

### **Rolling resistance** — 滚动阻力选项 `off` (默认) | `on`

是否仿真滚动阻力。

### **Resistance model** — 滚动阻力选项 `Constant coefficient` (默认) | `Pressure and velocity dependent`

是否仿真轮胎的滚动阻力。当您选择

- `Constant coefficient` — 模块忽略滚动阻力。
- `Pressure and velocity dependent` — 包括滚动阻力。

### **Constant coefficient** — 比例常数 `0.015` (默认) | 正标量

设置法向力与滚动阻力之间比例关系的系数。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**，并将 **Resistance model** 设置为 `Constant coefficient`。

### **Tire pressure** — 轮胎压力 `250e3` `Pa` (默认) | 正标量

轮胎的充气压力。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**，并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Alpha** — 轮胎压力方程指数 `-0.003` (默认) | 标量

模型方程中轮胎压力的指数。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**，并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Beta** — 法向力方程指数 `0.97` (默认) | 标量

模型方程中法向力的指数。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**，并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Coefficient A** — 速度无关的力分量 *A* `84e-4` (默认) | 正标量

模型方程中与速度无关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**，并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Coefficient B** — 速度相关的力分量 *B* `6.2e-4` `s/m` (默认) | 正标量

模型方程中与速度相关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**，并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Coefficient C** — 速度相关的力分量 *C* `1.6e-4` `s^2/m^2` (默认) | 正标量

模型方程中取决于速度项平方的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**，并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Velocity threshold** — 用于数学滑移模型的轮毂速度阈值 `0.001` `m/s` (默认) | 正标量

模块施加全滚动阻力时的速度。此参数确保在速度方向改变期间力保持连续，从而提高仿真的数值稳定性。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**。

### 高级

### **Traction velocity tolerance** — 牵引速度容差 `0.01` `m/s` (默认) | 正标量

轮胎重新获得牵引力时轮胎与地面之间相对速度的大小。如果此值过低，轮胎无法获得牵引力。如果此值过高，轮胎获得牵引力时轮胎速度会突然变化，这可能导致仿真不稳定。该参数必须大于零。

### **Engagement threshold force** — 接合阈值力 `10` `N` (默认) | 正标量

模块对轮胎施加法向力时的阈值力。如果此值过低，轮胎会快速获得和失去牵引力。如果此值过高，模块会产生低得不切实际的静摩擦力和动摩擦力。该参数必须大于零。

### **Initial traction state** — 初始牵引状态 `Tire is initially slipping` (默认) | `Tire is initially in traction`

在仿真开始时让轮胎处于牵引还是滑移状态的选项。

## 所属库

Simscape / Driveline / Tires & Vehicles

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a: 枚举更新

**Rolling resistance** 参数现在使用复选框。在之前的版本中，此参数使用下拉列表。

### R2024b: 改进柔量和惯量

该模块对惯量和柔量的位置进行设置，以便在加速期间更准确。该模块使用绝对滑移和相对滑移的新定义，以更贴近 Tire (Magic Formula) 模块。包含 Tire (Friction Parameterized) 模块的模型在 R2024b 中生成的输出与之前版本不同。

### R2022b: 选择滑移输出类型

现在可以对相对轮胎滑移进行建模，这与 Tire (Magic Formula) 模块一致。要在相对滑移和绝对滑移之间选择，请将 **Output type** 设置为 `Relative` 或 `Absolute`。与 R2024b 之前的版本相比，端口 **S** 处的输出现在乘以 `-1`。

## 描述

摩擦以静摩擦系数和动摩擦系数参数化的轮胎

Tire (Friction Parameterized) 模块表示摩擦以静摩擦系数和动摩擦系数参数化的轮胎。静摩擦系数 *μs* 决定轮胎失去牵引力并开始滑移时所施加的扭矩。动摩擦系数 *μk* 决定轮胎开始滑移后传递到路面的扭矩量。当轮胎相对路面的相对速度低于指定的牵引速度容差时，轮胎重新获得牵引力。

为提高轮胎模型的保真度，请指定轮胎柔量、惯量和滚动阻力等属性。请注意，这些属性会增加轮胎模型的复杂度，并可能减慢仿真速度。如果在实时仿真模型或为硬件在环 (HIL) 仿真准备模型，请考虑忽略轮胎柔量和惯量。

### 车轮滑移

当您将 **Slip output type** 设置为 `Relative` 时，模块在端口 **S** 输出无量纲物理信号的相对滑移速度，如下所示

S=−Vx−rwΩ−rwu˙|Vx|,

其中：

- *Vx* 是端口 **H** 处的轮毂纵向速度。
- *rw* 是滚动半径。
- *Ω* 是端口 **A** 处的车轴角速度。

当您将 **Slip output type** 设置为 `Absolute` 时，端口 **S** 以旋转形式输出绝对接触点滑移速度，如下所示

S=−Vx−rwΩ−rwu˙rw,

其中 *u* 是纵向变形的时间变化率，*u/rw* 等效于记录的仿真结果中弹簧和阻尼器的旋转速度。

当您将 **Slip output type** 设置为 `Absolute` 时，模块使用 Fundamental Friction Clutch 模块的摩擦模型。下图演示了模块如何实现滑移：

描述模块如何实现滑移的模型图。

当您将 **Compliance** 设置为 `No compliance - Suitable for HIL simulation` 时，模块设置 u˙=0。
