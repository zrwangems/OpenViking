---
type: simulink-block
title: 'Tire (Friction Parameterized)'
family: 'sdl'
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
```yaml
ports:
- name: N
  summary: 法向力，N 物理信号
  direction: input
- name: M
  summary: 摩擦系数，无量纲物理信号 | 二元素向量
  direction: input
- name: S
  summary: 滑移，无量纲或 rad/s 物理信号
  direction: output
- name: A
  summary: 车轴机械旋转
  direction: output
- name: H
  summary: 轮毂机械旋转
  direction: output
```

### 输入

### **N** — 法向力，N 物理信号

与作用在轮胎上的法向力相关联的物理信号输入端口，单位为 N。如果法向力向下作用在轮胎上，将轮胎压向路面，则为正值。

### **M** — 摩擦系数，无量纲物理信号 | 二元素向量

与无量纲的静摩擦系数和动摩擦系数（分别为 *μs* 和 *μk*）相关联的物理信号输入端口。将摩擦系数以二元素向量的形式提供，按 [*μs*, *μk*] 的顺序指定。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Physical signal friction coefficients`。
### 输出

### **S** — 滑移，无量纲或 rad/s 物理信号

与轮胎和道路之间的滑移相关联的物理信号输出端口，无量纲或单位为 rad/s。当您将 **Output type** 设置为：

- `Relative` 时，端口输出无量纲的相对滑移。
- `Absolute` 时，端口输出绝对滑移，单位为 rad/s。
### 守恒

### **A** — 车轴机械旋转

与车轴相关联的机械旋转守恒端口。

### **H** — 轮毂机械旋转

与轮毂相关联的机械旋转端口。
## 参数
```yaml
parameters:
- name: Rolling radius
  summary: 空载轮胎-车轮半径 0.3 m（默认）| 正标量
  group: 主要
- name: Slip output type
  summary: 相对或绝对切换选项 Relative（默认）| Absolute
  group: 主要
- name: Friction model
  summary: 摩擦模型 Fixed kinetic friction coefficient（默认）| Table lookup kinetic friction coefficient | Physical signal friction
    coefficients
  group: 主要
- name: Static friction coefficient
  summary: 静摩擦系数 0.90（默认）| 正标量
  group: 主要
- name: Kinetic friction coefficient
  summary: 动摩擦系数 0.70（默认）| 正标量
  group: 主要
- name: Tire slip vector
  summary: 轮胎滑移 [0, .02, .06, .15, .6, 1] rad/s（默认）| 向量
  group: 主要
- name: Kinetic friction coefficient vector
  summary: 动摩擦系数 [.89, .88, .8, .75, .7, .7]（默认）| 向量
  group: 主要
- name: Interpolation method
  summary: 插值方法 Linear（默认）| Smooth
  group: 主要
- name: Extrapolation method
  summary: 外插方法 Linear（默认）| Nearest | Error
  group: 主要
- name: Compliance
  summary: 动力学柔量模型 No compliance - Suitable for HIL simulation（默认）| Specify stiffness and damping
  group: 动力学
- name: Longitudinal stiffness
  summary: 纵向刚度 1e6 N/m（默认）| 正标量
  group: 动力学
- name: Longitudinal damping
  summary: 纵向阻尼 1000 N/(m/s)（默认）| 正标量
  group: 动力学
- name: Inertia
  summary: 惯量选项 No inertia（默认）| Specify inertia and initial velocity
  group: 动力学
- name: Tire inertia
  summary: 轮胎转动惯量 1 kg*m^2（默认）| 正标量
  group: 动力学
- name: Initial velocity
  summary: 初始转动速度 0 rad/s（默认）| 标量
  group: 动力学
- name: Rolling resistance
  summary: 滚动阻力选项 off（默认）| on
  group: 滚动阻力
- name: Resistance model
  summary: 滚动阻力选项 Constant coefficient（默认）| Pressure and velocity dependent
  group: 滚动阻力
- name: Constant coefficient
  summary: 比例常数 0.015（默认）| 正标量
  group: 滚动阻力
- name: Tire pressure
  summary: 轮胎压力 250e3 Pa（默认）| 正标量
  group: 滚动阻力
- name: Alpha
  summary: 轮胎压力方程指数 -0.003（默认）| 标量
  group: 滚动阻力
- name: Beta
  summary: 法向力方程指数 0.97（默认）| 标量
  group: 滚动阻力
- name: Coefficient A
  summary: 速度无关力分量 *A* 84e-4（默认）| 正标量
  group: 滚动阻力
- name: Coefficient B
  summary: 速度相关力分量 *B* 6.2e-4 s/m（默认）| 正标量
  group: 滚动阻力
- name: Coefficient C
  summary: 速度相关力分量 *C* 1.6e-4 s^2/m^2（默认）| 正标量
  group: 滚动阻力
- name: Velocity threshold
  summary: 数学滑移模型的轮毂速度阈值 0.001 m/s（默认）| 正标量
  group: 滚动阻力
- name: Traction velocity tolerance
  summary: 牵引速度容差 0.01 m/s（默认）| 正标量
  group: 高级
- name: Engagement threshold force
  summary: 接合阈值力 10 N（默认）| 正标量
  group: 高级
- name: Initial traction state
  summary: 初始牵引状态 Tire is initially slipping（默认）| Tire is initially in traction
  group: 高级
```

### 主要

### **Rolling radius** — 空载轮胎-车轮半径 `0.3` `m`（默认）| 正标量

路面与轮胎中心之间的距离。

### **Slip output type** — 相对或绝对切换选项 `Relative`（默认）| `Absolute`

模块使用相对滑移还是绝对滑移摩擦参数化。

### **Friction model** — 摩擦模型 `Fixed kinetic friction coefficient`（默认）| `Table lookup kinetic friction coefficient` | `Physical signal friction coefficients`

模块在仿真期间使用的摩擦模型。当您选择：

- `Fixed kinetic friction coefficient` 时，模块使用您指定的恒定静摩擦系数和动摩擦系数。
- `Table lookup kinetic friction coefficient` 时，您可以使用查表来指定摩擦。模块将静摩擦系数视为常数，将动摩擦系数视为常数或轮胎滑移的函数。使用此设置可在恒定路面条件下模拟轮胎动力学。
- `Physical signal friction coefficients` 时，模块启用端口 **M**，供您提供 [*μs*, *μk*]。使用此设置可在可变路面条件下模拟轮胎动力学。

### **Static friction coefficient** — 静摩擦系数 `0.90`（默认）| 正标量

轮胎开始滑移之前允许的纵向力与法向力之比，*μs*。此参数的值必须大于 **Kinetic friction coefficient** 参数或 **Kinetic friction coefficient vector** 参数中的最大值。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Table lookup kinetic friction coefficient`。

### **Kinetic friction coefficient** — 动摩擦系数 `0.70`（默认）| 正标量

轮胎滑移期间传递到道路的纵向力与法向力之比，*μk*。该比值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Fixed kinetic friction coefficient`。

### **Tire slip vector** — 轮胎滑移 `[0, .02, .06, .15, .6, 1]` `rad/s`（默认）| 向量

参考轮胎滑移。此向量中的元素与 **Kinetic friction coefficient vector** 参数一一对应。如果 **Tire slip vector** 参数仅包含非负值，则模块假定滑移-摩擦函数关于滑移轴对称。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.89, .88, .8, .75, .7, .7]`（默认）| 向量

给定轮胎滑移下的动摩擦系数。此向量中的元素与 **Tire slip vector** 参数一一对应。向量必须大小相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

查表用于处理轮胎滑移-动摩擦系数特性的插值方法。要优先考虑性能，请选择 `Linear`。要生成具有连续一阶导数的连续曲线，请选择 `Smooth`。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### **Extrapolation method** — 外插方法 `Linear`（默认）| `Nearest` | `Error`

查表用于处理轮胎滑移-动摩擦系数特性的外插方法。要生成：

- `Linear` — 选择此选项可生成在外插区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点或低于数据中最低点的外插。
- `Error` — 当您希望数据在表格范围内时，选择此选项可避免进入外插模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Table lookup kinetic friction coefficient`。

### 动力学

### **Compliance** — 动力学柔量模型 `No compliance - Suitable for HIL simulation`（默认）| `Specify stiffness and damping`

轮胎动力学柔量的模型。

- `No compliance - Suitable for HIL simulation` — 模块忽略动力学柔量。
- `Specify stiffness and damping` — 模块将轮胎视为在载荷下变形的刚性阻尼弹簧。

### **Longitudinal stiffness** — 纵向刚度 `1e6` `N/m`（默认）| 正标量

轮胎纵向刚度，*CFx*。

#### 依赖关系

要启用此参数，请将 **Compliance** 设置为 `Specify stiffness and damping`。

### **Longitudinal damping** — 纵向阻尼 `1000` `N/(m/s)`（默认）| 正标量

轮胎纵向阻尼，*bFx*。

#### 依赖关系

要启用此参数，请将 **Compliance** 设置为 `Specify stiffness and damping`。

### **Inertia** — 惯量选项 `No inertia`（默认）| `Specify inertia and initial velocity`

是否模拟轮胎转动惯量。当您选择

- `No inertia` — 模块忽略惯量。
- `Specify inertia and initial velocity` — 模块将轮胎视为在载荷下变形的刚性阻尼弹簧。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Tire inertia** — 轮胎转动惯量 `1` `kg*m^2`（默认）| 正标量

车轮-轮胎组件的转动惯量，*Iw*。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Initial velocity** — 初始转动速度 `0` `rad/s`（默认）| 标量

轮胎的初始角速度，*Ω(0)*。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### 滚动阻力

### **Rolling resistance** — 滚动阻力选项 `off`（默认）| `on`

是否模拟滚动阻力。

### **Resistance model** — 滚动阻力选项 `Constant coefficient`（默认）| `Pressure and velocity dependent`

是否模拟轮胎的滚动阻力。当您选择

- `Constant coefficient` — 模块忽略滚动阻力。
- `Pressure and velocity dependent` — 包含滚动阻力。

### **Constant coefficient** — 比例常数 `0.015`（默认）| 正标量

设置法向力与滚动阻力之间比例关系的系数。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance** 并将 **Resistance model** 设置为 `Constant coefficient`。

### **Tire pressure** — 轮胎压力 `250e3` `Pa`（默认）| 正标量

轮胎的充气压力。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance** 并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Alpha** — 轮胎压力方程指数 `-0.003`（默认）| 标量

模型方程中轮胎压力的指数。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance** 并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Beta** — 法向力方程指数 `0.97`（默认）| 标量

法向力模型方程的指数。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance** 并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Coefficient A** — 速度无关力分量 *A* `84e-4`（默认）| 正标量

模型方程中与速度无关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance** 并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Coefficient B** — 速度相关力分量 *B* `6.2e-4` `s/m`（默认）| 正标量

模型方程中与速度相关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance** 并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Coefficient C** — 速度相关力分量 *C* `1.6e-4` `s^2/m^2`（默认）| 正标量

模型方程中取决于速度项平方的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance** 并将 **Resistance model** 设置为 `Pressure and velocity dependent`。

### **Velocity threshold** — 数学滑移模型的轮毂速度阈值 `0.001` `m/s`（默认）| 正标量

模块施加全部滚动阻力时的速度。此参数确保力在速度方向变化期间保持连续，从而提高仿真的数值稳定性。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Rolling resistance**。

### 高级

### **Traction velocity tolerance** — 牵引速度容差 `0.01` `m/s`（默认）| 正标量

轮胎重新获得牵引力时轮胎与地面之间相对速度的大小。如果此值太低，轮胎不会获得牵引力。如果此值太高，轮胎在获得牵引力时速度会突然变化，这可能导致仿真不稳定。该参数必须大于零。

### **Engagement threshold force** — 接合阈值力 `10` `N`（默认）| 正标量

模块向轮胎施加法向力时的阈值力。如果此值太低，轮胎会快速获得和失去牵引力。如果此值太高，模块会产生不切实际的低静摩擦力和动摩擦力。该参数必须大于零。

### **Initial traction state** — 初始牵引状态 `Tire is initially slipping`（默认）| `Tire is initially in traction`

在仿真开始时使轮胎处于牵引或滑移状态的选项。
## 所属库

Simscape / Driveline / Tires & Vehicles

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：枚举更新

**Rolling resistance** 参数现在使用复选框。此参数在之前的版本中使用下拉菜单。

### R2024b：改进柔量和惯量

模块在加速期间对惯量和柔量的定位更加准确。模块使用新的绝对滑移和相对滑移定义，以更贴近 Tire (Magic Formula) 模块。包含 Tire (Friction Parameterized) 模块的模型在 R2024b 中生成的输出与之前版本不同。

### R2022b：选择滑移输出类型

您现在可以对相对轮胎滑移进行建模，这与 Tire (Magic Formula) 模块一致。要在相对滑移和绝对滑移之间选择，请将 **Output type** 设置为 `Relative` 或 `Absolute`。与 R2024b 之前的版本相比，端口 **S** 的输出现在乘以 `-1`。

## 描述

以静摩擦系数和动摩擦系数参数化的轮胎摩擦

Tire (Friction Parameterized) 模块表示以静摩擦系数和动摩擦系数参数化的轮胎摩擦。静摩擦系数 *μs* 确定轮胎失去牵引力并开始滑移时所施加的扭矩。动摩擦系数 *μk* 确定轮胎开始滑移后传递到路面的扭矩量。当轮胎在路面上的相对速度降至指定的牵引速度容差以下时，轮胎重新获得牵引力。

为提高轮胎模型的保真度，请指定轮胎柔量、惯量和滚动阻力等属性。请注意，这些属性会增加轮胎模型的复杂度，并可能减慢仿真速度。如果在实时仿真模型或为硬件在环（HIL）仿真准备模型时，请考虑忽略轮胎柔量和惯量。

### 车轮滑移

当您将 **Slip output type** 设置为 `Relative` 时，模块在端口 **S** 输出相对滑移速度，作为无量纲物理信号，使得

S=−Vx−rwΩ−rwu˙|Vx|,

其中：

- *Vx* 是端口 **H** 处的轮毂纵向速度。
- *rw* 是滚动半径。
- *Ω* 是端口 **A** 处的车轮车轴角速度。

当您将 **Slip output type** 设置为 `Absolute` 时，端口 **S** 以旋转形式输出绝对接触点滑移速度，使得

S=−Vx−rwΩ−rwu˙rw,

其中 *u* 是纵向变形的时间变化率，*u/rw* 等效于记录的仿真结果中弹簧和阻尼器的旋转速度。

当您将 **Slip output type** 设置为 `Absolute` 时，模块使用 Fundamental Friction Clutch 模块的摩擦模型。该图展示了模块如何实现滑移：

展示模块如何实现滑移的模型图。

当您将 **Compliance** 设置为 `No compliance - Suitable for HIL simulation` 时，模块设置 u˙=0。
