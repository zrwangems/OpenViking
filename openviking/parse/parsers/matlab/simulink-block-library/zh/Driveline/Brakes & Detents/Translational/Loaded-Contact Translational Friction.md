---
type: simulink-block
title: 'Loaded-Contact Translational Friction'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Translational'
documentation_page: 'loadedcontacttranslationalfriction'
documentation_source_path: 'ref/loadedcontacttranslationalfriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Loaded-Contact Translational Friction

## 端口

### 输入

### **N** — 法向力物理信号

与法向力关联的物理信号端口。该信号为正值或零。小于零的信号被解释为零。

### 守恒

### **B** — 基座机械平移

与驱动表面关联的平移守恒端口。

### **F** — 从动机械平移

与从动表面关联的平移守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 参数

### 摩擦

下表显示了某些端口、参数和设置的可见性如何取决于您为其他参数选择的选项。

**摩擦参数依赖关系**

| **Friction** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Friction model** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 暴露：  - 守恒端口   **H** - **Friction** 设置中的热参数 - **Thermal Port** 设置 | | 暴露：  - 守恒端口   **H** - **Friction** 设置中的热参数 - **Thermal Port** 设置 | |
| - | - | | **Temperature vector** | | **Temperature vector** | |
| - | **Relative velocity vector** | | - | | **Relative velocity vector** | |
| **Static friction coefficient** | **Static friction coefficient** | | **Static friction coefficient vector** | | **Static friction coefficient vector** | |
| **Kinetic friction coefficient** | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient matrix** | |
| - | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | |
| - | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | |
| **Velocity tolerance** | **Velocity tolerance** | | **Velocity tolerance** | | **Velocity tolerance** | |
| **Threshold force** | **Threshold force** | | **Threshold force** | | **Threshold force** | |
| **Viscous friction coefficient** | **Viscous friction coefficient** | | **Viscous friction coefficient** | | **Viscous friction coefficient** | |

### **Friction model** — 摩擦模型 `Fixed kinetic friction coefficient`（默认） | `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于您为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

摩擦模型设置会影响其他参数、设置和端口的可见性。有关详细信息，请参阅摩擦参数依赖关系。

### **Relative velocity vector** — 相对速度 `[0, .1, 1]` `m/s`（默认）| 向量

相对速度的输入值，以向量形式表示。向量中的值必须从左到右递增。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

仅当您将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Temperature vector** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度的输入值，以向量形式表示。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

仅当您将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Static friction coefficient** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Static friction coefficient vector** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静态值或峰值，以向量形式表示。该向量必须与温度向量具有相同数量的元素。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

仅当您将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

仅当您将 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，以向量形式表示。所有值必须大于零。

如果 **Friction model** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量必须与相对速度向量具有相同数量的元素。
- `Temperature-dependent friction coefficients` — 该向量必须与温度向量具有相同数量的元素。

#### 依赖关系

仅当您将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient matrix** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值，以矩阵形式表示。所有值必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Friction coefficient interpolation method** — 外推方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` —
  选择此选项以获得最佳性能。
- `Smooth` —
  选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Friction coefficient extrapolation method** — 插值方法 `Linear`（默认）| `Nearest` | `Error`

当输入值位于参数列表中指定的范围之外时，用于确定输出值的外推方法：

- `Linear` —
  选择此选项以生成在外推区域中以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` —
  选择此选项以生成不高于数据中最高点或低于数据中最低点的外推。
- `Error` —
  当希望数据位于表格范围内时，选择此选项以避免进入外推模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Velocity tolerance** — 相对速度锁定阈值 `0.001` `m/s`（默认）| 标量

两个表面可以锁定的相对速度下限。如果 **B** 和 **F** 平动端口上的扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则表面锁定。

### **Threshold force** — 法向接触力阈值 `1` `N`（默认）| 标量

施加到物理信号端口 **N** 的法向力仅在力的量值超过 **Threshold force** 参数的值时才施加到接触。低于 **Threshold force** 的力不会施加，因此不会传递摩擦扭矩。

### Viscous Losses

### **Viscous drag torque coefficient** — 粘性阻力矩 `0` `N/(m/s)`（默认）| 非负标量

用于计算阻力矩的粘性阻力系数，
*μvisc*。该系数取决于工作流体类型、流体温度以及表面之间的最大距离。

### 初始条件

### **Initial state** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时内部 Fundamental Friction Clutch 模块的状态。

- `Locked` —
  平移端口 **B** 和
  **F** 初始时锁定
  在一起。
- `Unlocked` —
  平移端口 **B** 和
  **F** 初始时相对
  彼此滑动。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击
**Open fault properties**。在 Property
Inspector 中，点击 **Fault behavior** 链接以
打开故障。

### **Friction fault** — 用于对摩擦故障建模的选项 `Add fault`

是否在模块中对故障建模。要添加
故障，请点击 **Add fault**
超链接。

### **Behavior when faulted** — 对故障触发的响应 `Cannot transmit power`（默认）| `Cannot unlock`

故障触发时的行为。您
可以将表面之间的故障选择为：

- `Cannot transmit
  power`
- `Cannot
  unlock`

#### 依赖关系

要启用此参数，请先通过点击
**Add fault** 超链接为模块启用
故障。

### Thermal Port

**Thermal Port** 设置仅在
**Friction** 设置中的 **Friction
model** 参数设置为
`Temperature-dependent friction
coefficients` 或 `Temperature and
velocity-dependent friction coefficients` 时可见。有关
更多信息，请参阅 Friction Parameter Dependencies。

### **Thermal mass** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热
能量。热质量越大，组件
对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将
**Friction model** 设置为
`Temperature-dependent friction
coefficients` 或
`Temperature and velocity-dependent
friction coefficients`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

使组件温度变化一度所需的热
能量。热质量越大，组件
对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将
**Friction model** 设置为
`Temperature-dependent friction
coefficients` 或
`Temperature and velocity-dependent
friction coefficients`。

## 所属库

Simscape / Driveline / Brakes & Detents / Translational

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a: Parameter name change

**Viscous drag torque coefficient** 参数
现在为 **Viscous friction coefficient**
参数。

### R2024a: 使用 Simscape faults 接口对故障建模

Loaded-Contact Translational Friction 模块现在支持 Simscape faults 接口。要
了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

两个滑动表面之间的承载接触摩擦

Loaded-Contact Translational Friction
模块模拟承受法向力的两个滑动表面之间的摩擦。

该模块基于
Fundamental Friction Clutch 模块实现为结构组件。
从锁定状态开始，如果施加的力超过
静摩擦，则两个表面解锁，静摩擦由静摩擦系数和
当前法向力定义。有关锁定和解锁如何建模的详细信息，请参阅 Fundamental Friction Clutch
模块参考页。

对于大于 **Threshold
force** 参数的法向力，力会被传递。

### 方程

该模块模拟两个受法向力作用的滑动表面之间的摩擦。当两个滑动表面未锁止时，摩擦力由以下方程确定：

F = N· μ · sign(vrel)+Fvisc ，

Fvisc = μvisc· vrel ，

其中：

- *F* 是传递的力。
- *N* 是法向力。
- *μ* 是摩擦系数。
- *vrel* 是相对速度。
- *Fvisc* 是粘性阻力。
- *μvisc* 是粘性阻力系数。

### 速度相关模型

您可以通过选择速度相关模型来模拟平移速度变化的影响。要选择速度相关模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`。

对于速度相关模型，以下相关参数将在 **Friction** 设置中可见：

- **Relative velocity vector**
- **Kinetic friction coefficient vector**
- **Friction coefficient interpolation method**
- **Friction coefficient extrapolation method**

### 热模型

您可以通过选择温度相关模型来模拟热流和温度变化的影响。要选择温度相关模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients`。

对于温度相关模型，热端口 **H** 以及以下设置可见：

- 在 **Friction** 设置中：

  - **Temperature vector**
  - **Static friction coefficient vector**
  - **Kinetic friction coefficient vector**
  - **Friction coefficient interpolation method**
  - **Friction coefficient extrapolation method**
- 在 **Thermal Port** 设置中：

  - **Thermal mass**
  - **Initial Temperature**

### 热、速度相关模型

您可以通过选择速度相关且温度相关模型来模拟平移速度变化和热流的影响。要选择同时取决于速度和温度的模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients`。

对于速度相关且温度相关模型，热端口 **H** 以及以下相关设置和参数将可见：

- 在 **Friction** 设置中：

  - **Relative velocity vector**
  - **Temperature vector**
  - **Static friction coefficient vector**
  - **Kinetic friction coefficient matrix**
  - **Friction coefficient interpolation method**
  - **Friction coefficient extrapolation method**
- 在 **Thermal Port** 设置中：

  - **Thermal mass**
  - **Initial Temperature**

### 故障

要对 Loaded-Contact Translational Friction 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，离合器将在仿真的剩余时间内根据 **Behavior when faulted** 设置进行响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`

### 限制与假设

- 该模型不考虑体质量。请根据需要将质量项外部添加到 **B** 和 **F** 端口。
- 该模型在假设法向力均匀分布的情况下计算传递的力。
