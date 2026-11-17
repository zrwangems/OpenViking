---
type: simulink-block
title: 'Loaded-Contact Rotational Friction'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Rotational'
documentation_page: 'loadedcontactrotationalfriction'
documentation_source_path: 'ref/loadedcontactrotationalfriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Loaded-Contact Rotational Friction

## 端口

### 输入

### **N** — 法向力物理信号

与法向力关联的物理信号端口。该信号为正值或零。小于零的信号被解释为零。

### 守恒

### **B** — 基础机械旋转

与驱动（基础）表面关联的旋转守恒端口。

### **F** — 从动机械旋转

与从动（从动）表面关联的旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

该端口仅在 **Friction** 设置中 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction model 和 Friction Parameter Dependencies。

## 参数

### 几何

### **Geometry model** — 参数化方法 `Define effective radius`（默认）| `Define annular region`

接触载荷摩擦模型的参数化方法：

- `Define effective radius` — 为摩擦有效半径提供值。
- `Define annular region` — 根据摩擦表面的内径和外径定义摩擦有效半径。如果选择此选项，面板将从默认状态更改。

#### 依赖关系

该参数的值会影响 **Geometry** 设置中其他参数的可见性。

### **Effective torque radius** — 有效摩擦表面半径 `130` `mm`（默认）| 正标量

有效半径 *r*eff。该值必须大于零。

#### 依赖关系

该参数仅在 **Geometry model** 参数设置为 `Define effective radius` 时可见。

### **Friction surface outside diameter** — 摩擦表面外径 `150` `mm`（默认）| 正标量

摩擦表面的外径 2 \* *ro*。必须大于零。

#### 依赖关系

该参数仅在 **Geometry model** 参数设置为 `Define annular region` 时可见。

### **Friction surface inside diameter** — 摩擦表面内径 `100` `mm`（默认）| 小于外径的正标量

摩擦表面的内径 2 \* *ri*。必须大于零，但小于摩擦表面外径。

#### 依赖关系

该参数仅在 **Geometry model** 参数设置为 `Define annular region` 时可见。

### Friction

该表显示了某些端口、参数和设置的可见性如何取决于你为其他参数选择的选项。

**Friction 参数依赖关系**

| **Friction** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Friction model** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 显示：  - 守恒端口   **H** - **Friction** 设置中的热参数 - **Thermal Port** 设置 | | 显示：  - 守恒端口   **H** - **Friction** 设置中的热参数 - **Thermal Port** 设置 | |
| - | - | | **Temperature vector** | | **Temperature vector** | |
| - | **Relative velocity vector** | | - | | **Relative velocity vector** | |
| **Static friction coefficient** | **Static friction coefficient** | | **Static friction coefficient vector** | | **Static friction coefficient vector** | |
| **Kinetic friction coefficient** | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient matrix** | |
| - | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | |
| - | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | |
| **Velocity tolerance** | **Velocity tolerance** | | **Velocity tolerance** | | **Velocity tolerance** | |
| **Threshold force** | **Threshold force** | | **Threshold force** | | **Threshold force** | |
| **Viscous friction coefficient** | **Viscous friction coefficient** | | **Viscous friction coefficient** | | **Viscous friction coefficient** | |

### **Friction model** — Friction model `Fixed kinetic friction coefficient`（默认）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于你为该模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供一个固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度以及圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

Friction model 设置会影响其他参数、设置和端口的可见性。有关更多信息，请参阅 Friction 参数依赖关系。

### **Relative velocity vector** — Relative velocity `[0, 100, 1000]` `rad/s`（默认）| vector

相对速度的输入值，以向量形式表示。向量中的值必须从左到右递增。最小值数量取决于你选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关更多信息，请参阅 Friction 参数依赖关系。

### **Temperature vector** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度作为向量的输入值。
最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

此参数仅在将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Static friction coefficient** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

此参数仅在将 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Static friction coefficient vector** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静态值或峰值，以向量形式表示。该向量的元素数量必须与温度向量相同。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

此参数仅在将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

此参数仅在将 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，以向量形式表示。所有值必须大于零。

如果 **Friction model** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量的元素数量必须与相对速度向量相同。
- `Temperature-dependent friction coefficients` — 该向量的元素数量必须与温度向量相同。

#### 依赖关系

此参数仅在将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient matrix** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值，以矩阵形式表示。所有值必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

此参数仅在将 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **摩擦系数插值方法** — 外推方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于近似输出值的插值方法：

- `Linear` —
  选择此选项以获得最佳性能。
- `Smooth` —
  选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当您将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **摩擦系数外推方法** — 插值方法 `Linear`（默认）| `Nearest` | `Error`

当输入值位于参数列表中指定的范围之外时，用于确定输出值的外推方法：

- `Linear` —
  选择此选项以生成在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` —
  选择此选项以生成不会高于数据中最高点或低于数据中最低点的外推。
- `Error` —
  当您希望数据位于表格范围内时，选择此选项以避免进入外推模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当您将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **速度容差** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 标量

两个表面可以锁定的相对速度下限。如果 **B** 和 **F** 旋转端口上的扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则表面锁定。

### **阈值力** — 法向接触力阈值 `1` `N`（默认）| 标量

施加到物理信号端口 **N** 的法向力仅在力的大小超过 **Threshold force** 参数值时才会施加到接触上。低于 **Threshold force** 的力不会施加，因此不会传递摩擦力矩。

### 粘性损耗

### **粘性阻力矩系数** — 粘性阻力矩 `0` `N*m/(rad/s)`（默认）| 非负标量

用于计算阻力矩的粘性阻力系数 *μvisc*。该系数取决于工作流体类型、流体温度以及表面之间的最大距离。

### 初始条件

### **初始状态** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时内部 Fundamental Friction Clutch 模块状态的状态。

- `Locked` —
  旋转端口 **B** 和 **F** 初始时锁定在一起。
- `Unlocked` —
  旋转端口 **B** 和 **F** 初始时相对彼此滑动。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。在 Property Inspector 中，点击 **Fault behavior** 链接以打开故障。

### **摩擦故障** — 用于对摩擦故障建模的选项 `Add fault`

是否在模块中对故障建模。要添加故障，请点击 **Add fault** 超链接。

### **发生故障时的行为** — 对故障触发的响应 `Cannot transmit power`（默认）| `Cannot unlock`

触发故障时的行为。您可以将表面之间的故障选择为：

- `Cannot transmit power`
- `Cannot unlock`

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接以启用模块的故障。

### 热端口

**Thermal Port** 设置仅在 **Friction** 设置中的 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。

### **热质量** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **初始温度** — 初始温度 `300` `K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 所属库

Simscape / Driveline / Brakes & Detents / Rotational

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：参数名称变更

**Viscous drag torque coefficient** 参数现在为 **Viscous friction coefficient** 参数。

### R2024a：使用 Simscape faults 接口对故障建模

Loaded-Contact Rotational Friction 模块现在支持 Simscape faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

两个旋转表面之间的加载接触摩擦

Loaded-Contact Rotational Friction 模块模拟承受法向力加载的两个旋转表面之间的摩擦。

该模块作为基于 Fundamental Friction Clutch 模块的结构组件实现。从锁定状态开始，如果传递的扭矩超过静摩擦（由静摩擦系数和当前法向力定义），则两个表面解锁。有关锁定和解锁建模方式的详细信息，请参阅 Fundamental Friction Clutch 模块参考页。

对于大于 **Threshold force** 参数的法向力，会传递扭矩。

### 方程

该模块模拟承受法向力加载的两个旋转表面之间的摩擦。当两个旋转表面未锁定时，传递的扭矩由以下方程确定：

τ = N· μ· reff · sign(ω) + τvisc ,

reff= 23⋅ro3−ri3ro2−ri2 ,

τvisc = μvisc· ω ,

其中：

- *τ* 是传递的扭矩。
- *N* 是法向力。
- *μ* 是摩擦系数。
- *reff* 是有效半径。
- *ro* 是表面外半径。
- *ri* 是表面内半径。
- *ω* 是相对角速度。
- *τvisc* 是粘性阻力扭矩。
- *μvisc* 是粘性摩擦系数。

### 速度相关模型

您可以通过选择速度相关模型来模拟旋转速度变化的影响。要选择速度相关模型，请在 **Friction** 设置中将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`。有关同时取决于速度和温度的摩擦模型的信息，请参阅 Thermal, Velocity-Dependent Model。

### Thermal Model

您可以通过选择温度相关模型来对热流和温度变化的影响进行建模。要选择温度相关模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients`。有关同时依赖于速度和温度的摩擦模型的信息，请参阅 Thermal, Velocity-Dependent Model。

### Thermal, Velocity-Dependent Model

您可以通过选择速度相关且温度相关的模型来对旋转速度变化和热流的影响进行建模。要选择同时依赖于速度和温度的模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients`。

### 故障

要对 Loaded-Contact Rotational Friction 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，离合器将在仿真的剩余时间内根据 **Behavior when faulted** 设置进行响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`

### Limitations and Assumptions

- 该模型不考虑惯性。请根据需要在 **B** 和 **F** 端口外部添加惯性项。
- 该模型在假设法向力均匀分布的情况下计算扭矩。
