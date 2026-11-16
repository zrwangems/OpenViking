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

与法向力关联的物理信号端口。此信号为正或零。小于零的信号按零处理。
### 守恒

### **B** — 基础机械平移

与驱动表面关联的平移守恒端口。

### **F** — 从动机械平移

与从动表面关联的平移守恒端口。

### **H** — 热流

与热流关联的热守恒端口。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 参数

### 摩擦

该表显示了某些端口、参数和设置的可见性如何取决于为其他参数选择的选项。

**摩擦参数依赖关系**

| **摩擦** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Friction model** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 公开：  - 守恒端口   **H** - **摩擦**设置中的热参数 - **Thermal Port** 设置 | | 公开：  - 守恒端口   **H** - **摩擦**设置中的热参数 - **Thermal Port** 设置 | |
| - | - | | **Temperature vector** | | **Temperature vector** | |
| - | **Relative velocity vector** | | - | | **Relative velocity vector** | |
| **Static friction coefficient** | **Static friction coefficient** | | **Static friction coefficient vector** | | **Static friction coefficient vector** | |
| **Kinetic friction coefficient** | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient matrix** | |
| - | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | |
| - | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | |
| **Velocity tolerance** | **Velocity tolerance** | | **Velocity tolerance** | | **Velocity tolerance** | |
| **Threshold force** | **Threshold force** | | **Threshold force** | | **Threshold force** | |
| **Viscous friction coefficient** | **Viscous friction coefficient** | | **Viscous friction coefficient** | | **Viscous friction coefficient** | |

### **Friction model** — 摩擦模型 `Fixed kinetic friction coefficient` (default) | `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

**Friction model** 设置会影响其他参数、设置和端口的可见性。有关详细信息，请参阅摩擦参数依赖关系。

### **Relative velocity vector** — 相对速度 `[0, .1, 1]` `m/s` (default) | vector

以 vector 形式输入相对速度的值。vector 中的值必须从左到右递增。最小值数量取决于所选的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Temperature vector** — 温度 `[280, 300, 320]` `K` (default) | increasing vector

以 vector 形式输入温度的值。最小值数量取决于所选的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。vector 中的值必须从左到右递增。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Static friction coefficient** — 静摩擦系数 `0.35` (default) | scalar

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Static friction coefficient vector** — 静摩擦系数 `[.4, .38, .36]` (default) | vector

作为 vector 的摩擦系数静态值或峰值。该 vector 必须与温度 vector 具有相同的元素数量。每个值必须大于动摩擦系数 vector 中对应元素的值。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Kinetic friction coefficient** — 动摩擦系数 `0.3` (default) | positive scalar

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.3, .22, .19]` (default) | `[.3, .28, .25]` | vector

作为 vector 的动摩擦系数输出值。所有值都必须大于零。

如果 **Friction model** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该 vector 必须与相对速度 vector 具有相同的元素数量。
- `Temperature-dependent friction coefficients` — 该 vector 必须与温度 vector 具有相同的元素数量。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Kinetic friction coefficient matrix** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]` (default) | matrix

作为 matrix 的动摩擦系数输出值。所有值都必须大于零。该 matrix 的大小必须等于温度 vector × 动摩擦系数相对速度 vector 所得 matrix 的大小。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Friction coefficient interpolation method** — 外推方法 `Linear` (default) | `Smooth`

当输入值位于两个连续网格点之间时，用于近似输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Friction coefficient extrapolation method** — 插值方法 `Linear` (default) | `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外推方法：

- `Linear` — 选择此选项以生成在外推区域以及与外推区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不超过数据中最高点或不低于数据中最低点的外推。
- `Error` — 当您希望数据在表格范围内时，选择此选项可避免进入外推模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Velocity tolerance** — 相对速度锁定阈值 `0.001` `m/s` (default) | scalar

两个表面可以锁定时的相对速度下限。如果 **B** 和 **F** 平移端口上的扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则这些表面锁定。

### **Threshold force** — 法向接触力阈值 `1` `N` (default) | scalar

施加到物理信号端口 **N** 的法向力仅当力的大小超过 **Threshold force** 参数的值时才会施加到接触。低于 **Threshold force** 的力不会施加，因此没有传递的摩擦力矩。

### 黏性损耗

### **Viscous drag torque coefficient** — 黏性阻力矩 `0` `N/(m/s)` (default) | nonnegative scalar

用于计算阻力矩的黏性阻力系数 *μvisc*。该系数取决于操作流体的类型、流体温度以及表面之间的最大距离。

### 初始条件

### **Initial state** — 初始离合器状态 `Unlocked` (default) | `Locked`

仿真开始时内部 Fundamental Friction Clutch 模块状态的状态。

- `Locked` — 平移端口 **B** 和 **F** 初始时锁定在一起。
- `Unlocked` — 平移端口 **B** 和 **F** 初始时相对彼此滑动。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。在 Property Inspector 中，点击 **Fault behavior** 链接以打开故障。

### **Friction fault** — 用于对摩擦故障建模的选项 `Add fault`

是否在模块中对故障建模。要添加故障，请点击 **Add fault** 超链接。

### **Behavior when faulted** — 对故障触发的响应 `Cannot transmit power` (default) | `Cannot unlock`

触发故障时的行为。您可以将表面之间的故障选择为：

- `Cannot transmit power`
- `Cannot unlock`

#### 依赖关系

要启用此参数，请先点击 **Add fault** 超链接为模块启用故障。

### 热端口

**Thermal Port** 设置仅在 **摩擦** 设置中，**Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Thermal mass** — 热质量 `50` `kJ/K` (default) | scalar

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Initial temperature** — 初始温度 `300` `K` (default) | scalar

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 所属库

Simscape / Driveline / Brakes & Detents / Translational

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：参数名称更改

**Viscous drag torque coefficient** 参数现在为 **Viscous friction coefficient** 参数。

### R2024a：使用 Simscape faults interface 对故障建模

Loaded-Contact Translational Friction 模块现在支持 Simscape faults interface。要了解详细信息，请参阅 Introduction to Simscape Faults。

## 描述

两个滑动表面之间的载荷接触摩擦

Loaded-Contact Translational Friction 模块模拟承受法向力载荷的两个滑动表面之间的摩擦。

该模块基于 Fundamental Friction Clutch 模块实现为结构组件。
从锁定状态开始，如果施加的力超过静摩擦（由静摩擦系数和当前法向力定义），则两个表面会解锁。有关如何对锁定和解锁建模的详细信息，请参阅 Fundamental Friction Clutch 模块参考页。

对于大于 **Threshold force** 参数的法向力，会传递力。

### 方程

该模块模拟承受法向力载荷的两个滑动表面之间的摩擦。当两个滑动表面未锁定时，摩擦力由以下方程确定：

F = N· μ · sign(vrel)+Fvisc ,

Fvisc = μvisc· vrel ,

其中：

- *F* 是传递的力。
- *N* 是法向力。
- *μ* 是摩擦系数。
- *vrel* 是相对速度。
- *Fvisc* 是黏性阻力。
- *μvisc* 是黏性阻力系数。

### 速度相关模型

可以通过选择速度相关模型来对平移速度变化的影响建模。要选择速度相关模型，请在 **摩擦** 设置中，将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`。

对于速度相关模型，这些相关参数将在 **摩擦** 设置中变为可见：

- **Relative velocity vector**
- **Kinetic friction coefficient vector**
- **Friction coefficient interpolation method**
- **Friction coefficient extrapolation method**

### 热模型

通过选择温度相关模型，可以对热流和温度变化的影响进行建模。要选择温度相关模型，请在 **摩擦** 设置中，将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients`。

对于温度相关模型，热端口 **H** 以及以下设置可见：

- 在 **摩擦** 设置中：

  - **温度向量**
  - **静摩擦系数向量**
  - **动摩擦系数向量**
  - **摩擦系数插值方法**
  - **摩擦系数外推方法**
- 在 **热端口** 设置中：

  - **热质量**
  - **初始温度**

### 热、速度相关模型

通过选择速度相关且温度相关模型，可以对平移速度变化和热流的影响进行建模。要选择同时取决于速度和温度的模型，请在 **摩擦** 设置中，将 **摩擦模型** 参数设置为 `Temperature and velocity-dependent friction coefficients`。

对于速度相关且温度相关模型，热端口 **H** 以及以下相关设置和参数变为可见：

- 在 **摩擦** 设置中：

  - **相对速度向量**
  - **温度向量**
  - **静摩擦系数向量**
  - **动摩擦系数矩阵**
  - **摩擦系数插值方法**
  - **摩擦系数外推方法**
- 在 **热端口** 设置中：

  - **热质量**
  - **初始温度**

### 故障

要对 Loaded-Contact Translational Friction 模块中的故障进行建模，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障** 超链接。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

当触发故障时，离合器会在仿真剩余时间内根据 **故障时的行为** 设置作出响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`

### 限制和假设

- 该模型不考虑物体质量。请根据需要在 **B** 和 **F** 端口外部添加质量项。
- 该模型在假设法向力均匀分布的情况下计算传递力。
