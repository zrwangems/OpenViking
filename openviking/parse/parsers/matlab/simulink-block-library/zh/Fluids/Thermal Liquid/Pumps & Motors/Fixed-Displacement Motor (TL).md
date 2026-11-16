---
type: simulink-block
title: 'Fixed-Displacement Motor (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pumps & Motors'
documentation_page: 'fixeddisplacementmotortl'
documentation_source_path: 'ref/fixeddisplacementmotortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Displacement Motor (TL)

## 端口

### 输入

### **EV** — 容积效率，无量纲物理信号

容积效率系数的物理信号输入端口。
输入信号的上限为 **Maximum volumetric efficiency** 参数值，下限为 **Minimum volumetric efficiency** 参数值。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率，无量纲物理信号

机械效率系数的物理信号输入端口。
输入信号的上限为 **Maximum mechanical efficiency** 参数值，下限为 **Minimum mechanical efficiency** 参数值。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 容积损失，m^3/s 物理信号

容积损失的物理信号输入端口，定义为马达入口之间的内部泄漏流量。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 机械损失，N\*m 物理信号

机械损失的物理信号输入端口，定义为旋转马达轴上的摩擦力矩。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### 守恒

### **A** — 马达入口热液体

与马达入口关联的热液体守恒端口。

### **B** — 马达出口热液体

与马达出口关联的热液体守恒端口。

### **C** — 马达壳体机械旋转

与马达壳体关联的机械旋转守恒端口。

### **R** — 马达轴机械旋转

与旋转马达轴关联的机械旋转守恒端口。

## 参数

### 参数

### **Leakage and friction parameterization** — 泄漏流量和摩擦力矩的参数化 `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Tabulated data - torque and speed` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

用于计算由内部泄漏和摩擦引起的流量和扭矩损失的方法。当您选择 `Analytical` 时，模块参数通常可从组件数据表中获得。当您选择 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 时，模块使用查找表将压降、角速度和排量映射到组件效率或损失。当您选择 `Tabulated data - torque and speed` 时，可以使用 **Torque table T(q,dp)** 和 **Shaft speed table w(q,dp)** 参数，将扭矩和轴转速输入为流量和压降的函数。

当您选择 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses` 时，模块执行的泄漏流量和摩擦力矩计算分别与 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 设置相同。当您选择 `Input signal - volumetric and mechanical efficiencies` 时，模块启用物理信号端口 **EV** 和 **EM**。您可以使用这些端口指定容积效率和机械效率。当您选择 `Input signal - volumetric and mechanical losses` 时，模块启用物理信号端口 **LV** 和 **LM**。您可以使用这些端口指定容积损失和机械损失。

### **Displacement** — 每轴旋转所排出的流体体积 `30` `cm^3/rev` (default) | 正标量

每轴旋转所排出的流体体积。模块在整个仿真过程中保持此值。

### **Nominal shaft angular velocity** — 给定容积效率下的轴角速度 `1800` `rpm` (default) | 标量

与给定容积效率相对应的旋转轴角速度。这些值通常可在制造商数据表中的标准工况下获得。模块使用此参数计算泄漏流量和摩擦力矩。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure drop** — 对应容积效率的压降 `10` `MPa` (default) | 标量

与给定容积效率相对应的压降。这些值通常可在制造商数据表中的标准工况下获得。模块使用此参数计算内部泄漏流量。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal dynamic viscosity** — 用于指定容积效率的动态粘度 `0.9` `cP` (default) | 标量

给定容积效率下液压流体的动态粘度。这些值通常可在制造商数据表中的标准工况下获得。模块使用此参数计算内部泄漏流量。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 指定标称条件下的容积效率 `0.92` (default) | 正标量

给定条件下的容积效率。模块将容积效率定义为实际容积流量与理想容积流量之比。这些值通常可在制造商数据表中的标准工况下获得。模块使用此参数计算内部泄漏流量。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 实际机械功率与理想机械功率之比 `0.88` (default) | 正标量

标称条件下实际机械功率与理想机械功率之比。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 引起轴旋转所需的最小扭矩 `0` `N*m` (default) | 标量

克服密封摩擦并引起机械轴旋转的扭矩。此扭矩是总摩擦力矩中与负载无关的分量。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure drop vector, dp** — 用于表格数据参数化的压力数据向量 `[.1, 1, 2] MPa` (default) | 1×*n* 向量

用于泄漏和扭矩摩擦表格参数化的压差向量。此向量与 **Shaft angular velocity vector, w** 参数或 **Flow rate vector, q** 参数一起，为三维相关参数 **Volumetric efficiency table, e\_v(dp,w)**、**Mechanical efficiency table, e\_m(dp,w)**、**Torque table, T(q,dp)** 和 **Shaft speed table, w(q,dp)** 形成一个独立轴。向量元素必须按升序列出。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`
- `Tabulated data - torque and speed`

### **Shaft angular velocity vector, w** — 用于指定容积效率和机械效率的角速度 `[250, 500, 1000, 2000, 3000, 4000]` `rpm` | 向量

对应于表格效率数据的轴角速度。该向量必须至少包含两个元素，且按严格递增顺序排列。

您可以为单个象限 (*ɷ*, *Δp*) 指定数据。有关各象限对应的工作模式，请参阅模块描述。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses`。

### **Flow rate vector, q** — 流量数据向量 `[.125, .25, .5, 1, 1.5, 2] * 1e-3 m^3/s` (default) | 1×*n* 向量

用于扭矩和速度表格参数化的流量数据向量。此向量与 **Pressure drop vector, dp** 参数一起，为三维相关参数 **Torque table, T(q,dp)** 和 **Shaft speed table, w(q,dp)** 形成一个独立轴。向量元素必须按升序列出。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Volumetric efficiency table, e\_v(dp,w)** — 给定压降和角速度下的容积效率 `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]` | 矩阵

给定流体压降和轴角速度下的容积效率。效率必须在范围 (0,1] 内。*M* 和 *N* 是指定查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的向量元素数。
- *N* 是 **Shaft angular velocity vector, w** 参数中的向量元素数。

您可以为单个象限 (*ɷ*, *Δp*) 指定数据。有关各象限对应的工作模式，请参阅模块描述。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w)** — 给定压降和角速度下的机械效率 `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]` | 矩阵

给定流体压降和轴角速度下的机械效率。效率必须在范围 (0,1] 内。*M* 和 *N* 是指定查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的向量元素数。
- *N* 是 **Shaft angular velocity vector, w** 参数中的向量元素数。

您可以为单个象限 (*ɷ*, *Δp*) 指定数据。有关各象限对应的工作模式，请参阅模块描述。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w)** — 对应压降和角速度下的内部泄漏流量 `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3` `m^3/s`

指定流体压降和轴角速度下的容积损失。此处容积损失定义为端口 A 和端口 B 之间的内部泄漏容积流量。*M* 和 *N* 是指定查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的向量元素数。
- *N* 是 **Shaft angular velocity vector, w** 参数中的向量元素数。

您可以为单个象限 (*ɷ*, *Δp*) 指定数据。有关各象限对应的工作模式，请参阅模块描述。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w)** — 对应压降和角速度下的摩擦力矩 `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626]` `N*m`

给定压降和轴角速度下的机械损失。模块将机械损失定义为由密封和内部组件引起的摩擦力矩。*M* 和 *N* 是指定查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的向量元素数。
- *N* 是 **Shaft angular velocity vector, w** 参数中的向量元素数。

您可以为单个象限 (*ɷ*, *Δp*) 指定数据。有关各象限对应的工作模式，请参阅模块描述。机械损失的表格数据必须遵循图中的约定：在正角速度下为正值，在负角速度下为负值。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Torque table, T(q,dp)** — 用于表格数据参数化的扭矩值 `[.47, 4.72, 9.35; .47, 4.7, 9.36; .47, 4.7, 9.4; .47, 4.7, 9.41; .47, 4.7, 9.46; .47, 4.68, 9.5] N*m` (default) | *M*×*N* 矩阵

指定流体压降和流量下的 *M*×*N* 扭矩值矩阵。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Flow rate vector, q** 参数中的元素数。
- *N* 是 **Pressure drop vector, dp** 参数中的向量元素数。

如果您的表在四个角中的任意一个角有未知数据点，请在这些值的位置使用 `NaN`。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Shaft speed table, w(q,dp)** — 用于表格数据参数化的轴转速 `[205, 80, 35; 455, 330, 285; 955, 831, 780; 1950, 1830, 1780; 2940, 2775, 2680; 3940, 3780, 3640] rpm` (default) | *M*×*N* 矩阵

指定流体压降和流量下的 *M*×*N* 轴转速值矩阵。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Flow rate vector, q** 参数中的元素数。
- *N* 是 **Pressure drop vector, dp** 参数中的向量元素数。

如果您的表在四个角中的任意一个角有未知数据点，请在这些值的位置使用 `NaN`。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Minimum volumetric efficiency** — 容积效率输入信号的下饱和界限 `1e-3` (default) | 范围 (0,1) 内的标量

容积效率允许的最小值。来自物理信号端口 **EV** 的输入会将低于此值的输入饱和。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率输入信号的上饱和界限 `1` (default) | 正标量

容积效率允许的最大值。来自物理信号端口 **EV** 的输入会将高于此值的输入饱和。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 容积效率输入信号的下饱和界限 `1e-3` (default) | 范围 (0,1) 内的标量

机械效率允许的最小值。来自物理信号端口 **EM** 的输入会将低于此值的输入饱和。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦力参数化** 设为 `Input signal - volumetric and mechanical efficiencies`。

### **最大机械效率** — 容积效率输入信号的上饱和界限 `1`（默认） | scalar，范围为 (0,1)

机械效率允许的最大值。来自物理信号端口 **EM** 的输入会将高于此值的输入饱和。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦力参数化** 设为 `Input signal - volumetric and mechanical efficiencies`。

### **马达-泵转换的压降阈值** — 用于启动马达和泵模式之间平滑转换的压降 `1e-3` `MPa`（默认） | scalar

从入口到出口的压降低于该值时，模块开始在马达和泵模式之间转换。模块使用双曲正切函数平滑泄漏流量和摩擦扭矩。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦力参数化** 设为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **马达-泵转换的角速度阈值** — 用于启动泵和马达模式之间平滑转换的角速度 `100` `rpm`（默认） | scalar

轴角速度低于该值时，模块开始在马达和泵模式之间转换。模块使用双曲正切函数平滑泄漏流量和摩擦扭矩。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦力参数化** 设为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **端口 A 和 B 处的横截面积** — 组件入口和出口处的流通面积 `0.01` `m^2`（默认） | positive scalar

组件入口和出口处的流通面积。假定这些面积相等。

### **检查是否超出所提供的表格数据范围** — 是否在超出所提供数据的范围时发出通知 `None`（默认） | `Warning` | `Error`

是否在超出所提供数据的范围时发出通知。选择 `Warning` 以在模块使用超出所提供数据范围的值时收到通知。选择 `Error` 以在模块使用超出所提供数据范围的值时停止仿真。

当 **泄漏和摩擦力参数化** 为 `Tabulated data - torque and speed` 时，此参数还会检查模块是否在所提供的 `NaN` 值区域内运行。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦力参数化** 设为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`
- `Tabulated data - torque and speed`

### **检查是否在马达模式之外运行** — 用于马达模式之外的运行工况的仿真警告模式 `None`（默认） | `Warning`

用于马达模式之外的运行工况的仿真警告模式。如果马达转换到泵模式，模块会生成警告。选择 `Warning` 以在此转换发生时收到通知。该警告不会导致仿真停止。

### **检查压力是否低于马达最小压力** — 是否在流体出口压力过低时发出通知 `None`（默认） | `Warning` | `Error`

是否在端口 **A** 或 **B** 处的流体压力过低时发出通知。选择 `Warning` 以在出口压力降至指定的最小值以下时收到通知。选择 `Error` 以在出口压力降至指定的最小值以下时停止仿真。

当流体压力降至流体蒸气压以下时，此参数有助于识别可能的空化条件。

### **马达最小压力** — 马达出口可接受压力的下限阈值 `0.101325 MPa`（默认） | positive scalar

马达入口或出口处可接受压力的下限阈值。

#### 依赖关系

要启用此参数，请将 **检查压力是否低于马达最小压力** 设为以下任一值：

- `Warning`
- `Error`

### 故障

### **排量故障** — 用于对排量故障建模的选项 `Add fault`

用于在模块中对排量故障建模的选项。发生故障时，排量按 **故障排量系数** 参数的值缩放。要添加故障，请单击 **Add fault** 超链接。

### **故障排量系数** — 用于缩放故障排量的系数 `0.5`（默认） | positive scalar

发生故障时模块用于缩放排量的系数。

#### 依赖关系

要启用此参数，请单击 **排量故障** 参数的 **Add fault** 超链接。

### **泄漏故障** — 用于对泄漏故障建模的选项 `Add fault`

用于在模块中对泄漏故障建模的选项。发生故障时，容积效率或损失按 **故障泄漏系数** 参数的值缩放。要添加故障，请单击 **Add fault** 超链接。

### **故障泄漏系数** — 用于缩放泄漏故障的系数 `2.0`（默认） | positive scalar

发生故障时模块用于缩放容积效率或损失的系数。

#### 依赖关系

要启用此参数，请单击 **泄漏故障** 参数的 **Add fault** 超链接。

### **轴摩擦力矩故障** — 用于对轴摩擦力矩故障建模的选项 `Add fault`

用于在模块中对轴摩擦力矩故障建模的选项。发生故障时，机械效率或损失按 **故障轴摩擦力矩系数** 参数的值缩放。要添加故障，请单击 **Add fault** 超链接。

### **故障轴摩擦力矩系数** — 用于缩放轴摩擦力矩故障的系数 `2.0`（默认） | positive scalar

发生故障时模块用于缩放机械效率或损失的系数。

#### 依赖关系

要启用此参数，请单击 **轴摩擦力矩故障** 参数的 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Pumps & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

Fixed-Displacement Motor (TL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Simscape 故障简介。

### R2024b：使用扭矩和轴转速对模块进行参数化

现在，您可以通过将 **泄漏和摩擦力参数化** 参数设为 `Tabulated data - torque and speed` 来指定扭矩和轴转速，从而对模块进行参数化。制造商通常以此格式提供马达数据表。

### R2024b：检查端口压力是否低于泵最小压力

使用 **检查压力是否低于泵最小压力** 参数来确定当端口 **A** 或 **B** 处的流体低于 **泵压力最小值** 参数的值时会发生什么。

### R2024a：检查模块是否在计算数据范围之外运行

**检查是否超出所提供的表格数据的象限** 参数已重命名为 **检查是否超出所提供的表格数据范围**。您可以启用 **检查是否超出所提供的表格数据范围** 参数，以检查模块是否在模块参数指定的数据之外运行，即模块在已扩展数据的区域内运行。

## 描述

液压-机械功率转换装置

Fixed-Displacement Motor (TL) 模块表示一种从热液体网络提取功率并将其输送到机械旋转网络的装置。马达排量固定为通过 **排量** 参数指定的恒定值。

端口 **A** 和 **B** 表示马达入口。端口 **R** 和 **C** 表示马达驱动轴和壳体。在正常运行期间，从端口 **A** 到端口 **B** 的压降会导致从端口 **A** 到端口 **B** 的正流量，以及马达轴相对于马达壳体的正旋转。此运行模式在本文中称为 *正向马达*。

**运行模式**

模块有四种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压降 *Δp = p*A – *p*B 和角速度 *ω = ω*R – *ω*C：

- 模式 1，*正向马达*：从端口 **A** 到端口 **B** 的流量导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 2，*反向泵*：负轴角速度导致从端口 **B** 到端口 **A** 的压力升高以及从 **B** 到端口 **A** 的流量。
- 模式 3，*反向马达*：从端口 **B** 到端口 **A** 的流量导致从 **B** 到 **A** 的压力降低以及负轴角速度。
- 模式 4，*正向泵*：正轴角速度导致从端口 **A** 到端口 **B** 的压力升高以及从 **A** 到 **B** 的流量。

与系统响应时间相比，马达的响应时间可忽略不计。假定马达几乎瞬时达到稳态，并将其视为准稳态组件。

### 能量平衡

泵所做的机械功与能量交换相关。控制能量平衡方程为：

ϕA+ϕB−Phydro=0,

其中：

- *Φ*A 和 *Φ*B 分别是端口 **A** 和 **B** 处的能量流率。
- *P*hydro 是马达液压功率。它是马达端口之间压力差的函数：Phydro=Δpm˙ρ

马达机械功率由马达扭矩 *τ* 和角速度 *ω* 生成：

Pmech=Tω.

### 流量和驱动力矩

马达处生成的质量流量为

m˙=m˙Ideal+m˙Leak,

其中：

- m˙ 是实际质量流量。
- m˙Ideal 是理想质量流量。
- m˙Leak 是内部泄漏质量流量。

马达处生成的扭矩为

τ=τIdeal−τFriction,

其中：

- *τ* 是实际扭矩。
- *τ*Ideal 是理想扭矩。
- *τ*Friction 是摩擦扭矩。

**理想流量和理想扭矩**

理想质量流量为

m˙Ideal=ρDω,

理想生成的扭矩为

τIdeal=DΔp,

其中：

- *ρ* 是热液体端口 **A** 和 **B** 处流体密度的平均值。
- *D* 是 **排量** 参数。
- *ω* 是轴角速度。
- *Δp* 是从入口到出口的压降。

### 解析泄漏和摩擦力参数化

如果将 **泄漏和摩擦力参数化** 设为 `Analytical`，模块会根据轴速度、压降和摩擦扭矩的恒定值计算泄漏和摩擦。泄漏流量与马达上的压差相关，其计算公式为：

m˙leak=KρavgΔp,

其中：

- *Δp* 是 *pA* – *pB*。
- *ρ*avg 是平均流体密度。
- *K* 是用于解析损失的 Hagen-Poiseuille 系数，

  K=Dωnom(1ηv,nom−1)Δpnom,

  其中：

  - *D* 是 **排量** 参数的值。
  - *ωnom* 是 **标称轴角速度** 参数的值。
  - *ηv, nom* 是 **标称条件下的容积效率** 参数的值。
- *Δpnom* 是 **标称压降** 参数的值。

摩擦扭矩与轴角速度相关，其计算公式为：

τfr=(τ0+k|Δp|)tanh(4ω5×10−5ωnom),

其中：

- *τ*0 是 **空载扭矩** 参数的值。
- *k* 是标称排量下的摩擦扭矩与压力增益系数，它由 **标称条件下的机械效率** 参数的值 *ηm* 确定：

  k=τfr,nom−τ0Δpnom.

  *τfric* 是标称条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nom)DΔpnom.
- *Δp* 是端口 **A** 和 **B** 之间的压降。
- *ω* 是相对轴角速度，即 ωR−ωC。

### 表格化泄漏和摩擦参数化

当使用表格化数据表示电机效率或损失时，可以为电机的一个或多个运行模式提供数据。表格化数据的符号确定模块的运行工况。当为一个或多个但少于四个运行模式提供数据时，模块通过将给定数据扩展到其余象限来计算其他模式或模式的补充数据。

**Tabulated Data - Volumetric and Mechanical Efficiencies**

当将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 时，泄漏流量为

m˙Leak=m˙Leak,Motor(1+α)2+m˙Leak,Pump(1−α)2,

摩擦扭矩为

τFriction=τFriction,Motor1+α2+τFriction,Pump1−α2,

其中：

- *α* 是用于 motor-pump 过渡的数值平滑参数。
- m˙Leak,Motor 是电机模式下的泄漏流量。
- m˙Leak,Pump 是泵模式下的泄漏流量。
- *τ*Friction,Motor 是电机模式下的摩擦扭矩。
- *τ*Friction,Pump 是泵模式下的摩擦扭矩。

平滑参数 *α* 由双曲函数给出

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold)·tanh(4DDThreshold),

其中：

- *Δp*Threshold 是 **Pressure drop threshold for motor-pump transition** 模块参数的指定值。
- *ω*Threshold 是 **Angular velocity threshold for motor-pump transition** 模块参数的指定值。
- *D*Threshold 是 **Angular velocity threshold for motor-pump transition** 模块参数的指定值。

泄漏流量根据容积效率计算，该量通过 **Volumetric efficiency table** 模块参数以表格形式在 *Δp*–*ɷ*–*D* 域上指定。当在电机模式下运行（运行模式图中所示的 *Δp*–*ɷ*–*D* 图的象限 **1** 和 **3**）时，泄漏流量为：

m˙Leak,Motor=(1−ηv)m˙,

其中 *η*v 是容积效率，通过表格化数据的插值或外推获得。类似地，当在泵模式下运行（*Δp*–*ɷ*–*D* 图的象限 **2** 和 **4**）时，泄漏流量为：

m˙Leak,Pump=−(1−ηv)m˙Ideal.

摩擦扭矩类似地根据机械效率计算，该量通过 **Mechanical efficiency table** 模块参数以表格形式在 *Δp*–*ɷ*–*D* 域上指定。当在电机模式下运行（*Δp*–*ɷ*–*D* 图的象限 **1** 和 **3**）时：

τFriction,Motor=(1−ηm)τIdeal,

其中 *η*m 是机械效率，通过表格化数据的插值或外推获得。类似地，当在泵模式下运行（*Δp*–*ɷ*–*D* 图的象限 **2** 和 **4**）时：

τFriction,Pump=−(1−ηm)τ.

**Tabulated Data - Volumetric and Mechanical Losses**

当将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses` 时，泄漏（容积）流量通过表格形式直接在 *Δp*–*ɷ* 域上指定：

qLeak=qLeak(Δp,ω).

由泄漏引起的质量流量根据体积流量计算：

m˙Leak=ρqLeak.

摩擦扭矩为

τFriction=τLoss(Δp,ω)tanh(4ωωthreshold),

其中 *q*Leak(*Δp*,*ω*) 和 *τ*Loss(*Δp*,*ω*) 是容积损失和机械损失，通过对由 **Volumetric loss table** 和 **Mechanical loss table** 模块参数指定的表格化数据进行插值或外推获得。

**Tabulated Data - Torque and Speed Parameterization**

当将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed` 时，模块按如下方式计算容积损失表 *qloss,TLU* 和机械损失表 *τloss,TLU*：

qloss,TLU=qTLU−DωTLUτloss,TLU=DΔpTLU−TTLU

其中：

- *qTLU* 是 **Flow rate vector, q** 参数的值。
- *ωTLU* 是 **Shaft speed table, w(q,dp)** 参数的值。
- *ΔpTLU* 是 **Pressure drop vector, dp** 参数的值。
- *TTLU* 是 **Torque table, T(q,dp)** 参数的值。

如果为 **Shaft speed table, w(q,dp)** 和 **Torque table, T(q,dp)** 参数提供的值未覆盖所有四个象限，则模块通过以下方式扩展数据：

- 对称镜像 **Pressure drop vector, dp** 和 **Flow rate vector, q** 参数的值，使其包含负值。
- 将容积损失表 *qloss,TLU* 的值对称扩展到其他象限。这些扩展值的符号与每个象限中的 *ΔpTLU* 符号匹配。
- 根据流量向量和容积损失表的扩展值计算轴转速向量 *ωTLU* 的扩展值，ωTLU=qTLU−qloss,TLUD。
- 将机械损失表 *τloss,TLU* 的值对称扩展到其他象限。这些扩展值的符号与每个象限中的 *ωTLU* 符号匹配。

如果数据表在四个角中的任一个存在未知数据点，或者 **Shaft speed table, w(q,dp)** 或 **Torque table, T(q,dp)** 参数中存在未知数据点，请在这些值的位置使用 `NaN`。模块使用关于压力降的最近外推来填充结果容积损失表和机械损失表中的 `NaN` 元素。模块调整外推机械损失表中的符号，以匹配轴转速向量 *ωTLU* 中对应元素的符号，其中 ωTLU=qTLU−qloss,TLUD。

在扩展或填充未知数据后，模块在仿真期间使用线性插值和最近外推来计算容积损失表和机械损失表

qloss=tablelookup(qTLU,ΔpTLU,qloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)τloss=tablelookup(qTLU,ΔpTLU,τloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)

其中 Q=m˙Aρavg。

### 输入信号参数化

当将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies` 时，泄漏流量和摩擦扭矩计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。容积效率和机械效率查找表替换为通过端口 **EV** 和 **EM** 指定的物理信号输入。

效率是介于 `0` 和 `1` 之间的正值。超出这些边界的输入值设置为最接近的边界（小于 `0` 的输入为 `0`，大于 `1` 的输入为 `1`）。效率信号在 **Minimum volumetric efficiency** 或 **Minimum mechanical efficiency** 以及 **Maximum volumetric efficiency** 或 **Maximum mechanical efficiency** 处饱和。

当将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses` 时，泄漏流量和摩擦扭矩计算与 `Tabulated data - volumetric and mechanical losses` 设置相同。容积损失和机械损失查找表替换为通过端口 **LV** 和 **LM** 指定的物理信号输入。

模块期望输入为正值。它根据仿真期间建立的运行工况自动设置符号——更准确地说，根据组件恰好运行所在的 *Δp*–*ɷ* 象限设置。

### 故障

要对故障建模，在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

可以对排量故障、泄漏或轴摩擦扭矩故障建模。

当启用 **Displacement fault** 参数时，模块在故障触发时按 **Faulted displacement factor** 参数的值缩放排量，

DFault=fDD,

其中 *fD* 是 **Faulted displacement factor** 参数的值。当 **Leakage and friction parameterization** 参数为 `Analytical` 时，模块不使用故障排量值计算 Hagen-Poiseuille 系数或摩擦扭矩。

当启用 **Leakage fault** 参数且 **Leakage and friction parameterization** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障容积效率为

ηv,Fault=ηvfLeak,

其中 *fLeak* 是 **Faulted leakage factor** 参数的值，*ηv* 是容积效率。当 **Leakage and friction parameterization** 为 `Analytical` 时，模块使用故障容积效率计算 Hagen-Poiseuille 系数。

当 **Leakage and friction parameterization** 为 `Tabulated data - volumetric and mechanical losses`、`Input signal - volumetric and mechanical losses` 或 `Tabulated data - torque and speed` 时，故障泄漏体积流量为

qLeak,Fault=fLeakqLeak.

当 **Leakage and friction parameterization** 为 `Tabulated data - torque and speed` 时，模块根据轴转速和扭矩参数计算 *qLeak*。

当启用 **Shaft friction torque fault** 参数且 **Leakage and friction parameterization** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障机械效率为

ηm,Fault=ηmfFriction,

其中 *fFriction* 是 **Shaft friction torque fault** 参数的值，*ηm* 是机械效率。当 **Leakage and friction parameterization** 为 `Analytical` 时，模块使用故障机械效率计算摩擦扭矩。

当 **Leakage and friction parameterization** 为 `Tabulated data - volumetric and mechanical losses`、`Input signal - volumetric and mechanical losses` 或 `Tabulated data - torque and speed` 时，故障摩擦扭矩为

τFriction,Fault=fFrictionτFriction.

当 **Leakage and friction parameterization** 为 `Tabulated data - torque and speed` 时，模块根据轴转速和扭矩参数计算 *τLeak*。

### 假设和限制

- 电机被视为准稳态组件。
- 忽略流体惯性和高度的影响。
- 电机壁是刚性的。
- 忽略外部泄漏。
