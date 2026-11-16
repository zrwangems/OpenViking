---
type: simulink-block
title: 'Loaded-Contact Rotational Friction'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Brakes and Detents'
documentation_page: 'loadedcontactrotationalfriction'
documentation_source_path: 'ref/loadedcontactrotationalfriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Loaded-Contact Rotational Friction

## 端口

### 输入

### **N** — 法向力物理信号

与法向力关联的物理信号端口。此信号为正或零。小于零的信号被解释为零。

### 守恒

### **B** — 底座机械旋转

与驱动（底座）表面关联的旋转守恒端口。

### **F** — 从动机械旋转

与从动（跟随）表面关联的旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

仅当在 **摩擦**设置中，将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此端口才可见。有关详细信息，请参阅摩擦模型和摩擦参数依赖关系。

## 参数

### 几何

### **几何模型** — 参数化方法 `Define effective radius`（默认）| `Define annular region`

加载接触摩擦模型的参数化方法：

- `Define effective radius` — 为摩擦有效半径提供一个值。
- `Define annular region` — 根据摩擦表面的内径和外径定义摩擦有效半径。如果选择此选项，面板将从默认状态更改。

#### 依赖关系

此参数的值会影响 **几何**设置中其他参数的可见性。

### **有效转矩半径** — 有效摩擦表面半径 `130` `mm`（默认）| 正标量

有效半径 *r*eff。该值必须大于零。

#### 依赖关系

仅当 **几何模型** 参数设置为 `Define effective radius` 时，此参数才可见。

### **摩擦表面外径** — 摩擦表面外径 `150` `mm`（默认）| 正标量

摩擦表面的外径，2 \* *ro*。必须大于零。

#### 依赖关系

仅当 **几何模型** 参数设置为 `Define annular region` 时，此参数才可见。

### **摩擦表面内径** — 摩擦表面内径 `100` `mm`（默认）| 小于外径的正标量

摩擦表面的内径，2 \* *ri*。必须大于零，但小于摩擦表面外径。

#### 依赖关系

仅当 **几何模型** 参数设置为 `Define annular region` 时，此参数才可见。

### 摩擦

下表显示某些端口、参数和设置的可见性如何取决于你为其他参数选择的选项。

**摩擦参数依赖关系**

| **摩擦** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **摩擦模型** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 公开：  - 守恒端口   **H** - **摩擦**设置中的热参数 - **热端口**设置 | | 公开：  - 守恒端口   **H** - **摩擦**设置中的热参数 - **热端口**设置 | |
| - | - | | **温度向量** | | **温度向量** | |
| - | **相对速度向量** | | - | | **相对速度向量** | |
| **静摩擦系数** | **静摩擦系数** | | **静摩擦系数向量** | | **静摩擦系数向量** | |
| **动摩擦系数** | **动摩擦系数向量** | | **动摩擦系数向量** | | **动摩擦系数矩阵** | |
| - | **摩擦系数插值方法** | | **摩擦系数插值方法** | | **摩擦系数插值方法** | |
| - | **摩擦系数外推方法** | | **摩擦系数外推方法** | | **摩擦系数外推方法** | |
| **速度容差** | **速度容差** | | **速度容差** | | **速度容差** | |
| **阈值力** | **阈值力** | | **阈值力** | | **阈值力** | |
| **黏性摩擦系数** | **黏性摩擦系数** | | **黏性摩擦系数** | | **黏性摩擦系数** | |

### **摩擦模型** — 摩擦模型 `Fixed kinetic friction coefficient`（默认）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于你为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供一个固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

摩擦模型设置会影响其他参数、设置和端口的可见性。有关详细信息，请参阅摩擦参数依赖关系。

### **相对速度向量** — 相对速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

作为向量输入相对速度值。向量中的值必须从左到右递增。最小值数量取决于你选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

作为向量输入温度值。最小值数量取决于你选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **静摩擦系数** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静摩擦值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **静摩擦系数向量** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

作为向量的摩擦系数静摩擦值或峰值。该向量必须与温度向量具有相同数量的元素。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **动摩擦系数** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Fixed kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **动摩擦系数向量** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

作为向量的动摩擦系数输出值。所有值都必须大于零。

如果 **摩擦模型** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量必须与相对速度向量具有相同数量的元素。
- `Temperature-dependent friction coefficients` — 该向量必须与温度向量具有相同数量的元素。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **动摩擦系数矩阵** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

作为矩阵的动摩擦系数输出值。所有值都必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **摩擦系数插值方法** — 外推方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **摩擦系数外推方法** — 插值方法 `Linear`（默认）| `Nearest` | `Error`

当输入值位于参数列表指定范围之外时，用于确定输出值的外推方法：

- `Linear` — 选择此选项以生成在外推区域以及与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不会高于数据中最高点或低于数据中最低点的外推。
- `Error` — 当你希望数据位于表范围内时，选择此选项以避免进入外推模式。如果输入信号在表范围之外，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当将 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **速度容差** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 标量

两个表面可以锁定的相对速度下限。如果 **B** 和 **F** 旋转端口上的转矩小于有效半径、静摩擦系数和所施加法向力的乘积，则这些表面锁定。

### **阈值力** — 法向接触力阈值 `1` `N`（默认）| 标量

施加到物理信号端口 **N** 的法向力仅在力的大小超过 **阈值力** 参数的值时才会施加到接触处。低于 **阈值力** 的力不会施加，因此不会传递摩擦力矩。

### 黏性损耗

### **黏性阻力转矩系数** — 黏性阻力转矩 `0` `N*m/(rad/s)`（默认）| 非负标量

用于计算阻力转矩的黏性阻力系数 *μvisc*。该系数取决于工作流体的类型、流体温度以及表面之间的最大距离。

### 初始条件

### **初始状态** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时内部 Fundamental Friction Clutch 模块的状态。

- `Locked` — 旋转端口 **B** 和 **F** 初始锁在一起。
- `Unlocked` — 旋转端口 **B** 和 **F** 初始相对彼此滑动。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **打开故障属性**。在属性检查器中，点击 **故障行为** 链接以打开故障。

### **摩擦故障** — 用于对摩擦故障建模的选项 `Add fault`

是否在模块中对故障建模。要添加故障，请点击 **添加故障** 超链接。

### **故障时的行为** — 对故障触发的响应 `Cannot transmit power`（默认）| `Cannot unlock`

故障触发时的行为。你可以将表面之间的故障选择为：

- `Cannot transmit power`
- `Cannot unlock`

#### 依赖关系

要启用此参数，请通过点击 **添加故障** 超链接为模块启用故障。

### 热端口

**热端口**设置仅在 **摩擦**设置中，将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。

### **热质量** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度改变一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **初始温度** — 初始温度 `300` `K`（默认）| 标量

使组件温度改变一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 所属库

Simscape / Driveline / Brakes & Detents / Rotational

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2011a 中引入**

### R2025a：参数名称更改

**黏性阻力转矩系数** 参数现在为 **黏性摩擦系数** 参数。

### R2024a：使用 Simscape 故障接口对故障建模

Loaded-Contact Rotational Friction 模块现在支持 Simscape 故障接口。要了解详细信息，请参阅 Simscape 故障简介。

## 描述

两个旋转表面之间的负载接触摩擦

Loaded-Contact Rotational Friction 模块模拟两个承受法向力的旋转表面之间的摩擦。

该模块基于 Fundamental Friction Clutch 模块实现为结构组件。从锁定状态开始，如果传递扭矩超过静摩擦，则两个表面解锁；静摩擦由静摩擦系数和当前法向力定义。有关锁定和解锁建模方式的详细信息，请参阅 Fundamental Friction Clutch 模块参考页。

当法向力大于 **Threshold force** 参数时，传递扭矩。

### 方程

该模块模拟两个承受法向力的旋转表面之间的摩擦。当两个旋转表面未锁定时，传递扭矩由以下方程确定：

τ = N· μ· reff · sign(ω) + τvisc ,

reff = 2/3 ⋅ (ro^3 − ri^3) / (ro^2 − ri^2) ,

τvisc = μvisc· ω ,

其中：

- *τ* 是传递扭矩。
- *N* 是法向力。
- *μ* 是摩擦系数。
- *reff* 是有效半径。
- *ro* 是表面外半径。
- *ri* 是表面内半径。
- *ω* 是相对角速度。
- *τvisc* 是粘性阻力扭矩。
- *μvisc* 是粘性摩擦系数。

### 速度相关模型

通过选择速度相关模型，可以建模旋转速度变化的影响。要选择速度相关模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`。有关同时取决于速度和温度的摩擦模型的信息，请参阅热、速度相关模型。

### 热模型

通过选择温度相关模型，可以建模热流和温度变化的影响。要选择温度相关模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients`。有关同时取决于速度和温度的摩擦模型的信息，请参阅热、速度相关模型。

### 热、速度相关模型

通过选择速度相关且温度相关模型，可以建模旋转速度变化和热流的影响。要选择同时取决于速度和温度的模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients`。

### 故障

要为 Loaded-Contact Rotational Friction 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

当触发故障时，离合器根据 **Behavior when faulted** 设置在剩余仿真中响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`

### 限制和假设

- 该模型不考虑惯性。请根据需要将惯性项从外部添加到 **B** 和 **F** 端口。
- 该模型在假设法向力均匀分布的情况下计算扭矩。
