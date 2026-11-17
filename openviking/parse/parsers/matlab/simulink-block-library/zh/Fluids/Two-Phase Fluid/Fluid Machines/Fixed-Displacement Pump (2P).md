---
type: simulink-block
title: 'Fixed-Displacement Pump (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Fluid Machines'
documentation_page: 'fixeddisplacementpump2p'
documentation_source_path: 'ref/fixeddisplacementpump2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Displacement Pump (2P)

## 端口

### 输入

### **EV** — 容积效率，无量纲物理信号

容积效率系数的物理信号输入端口。输入信号的上限为 **Maximum volumetric efficiency** 参数值，下限为 **Minimum volumetric efficiency** 参数值。

#### 依赖

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率，无量纲物理信号

机械效率系数的物理信号输入端口。输入信号的上限为 **Maximum mechanical efficiency** 参数值，下限为 **Minimum mechanical efficiency** 参数值。

#### 依赖

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 容积损失，m^3/s 物理信号

容积损失的物理信号输入端口，容积损失是泵入口之间的内部泄漏流量。

#### 依赖

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 机械损失，N\*m 物理信号

机械损失的物理信号输入端口，机械损失是旋转泵轴上的摩擦扭矩。

#### 依赖

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。
### 守恒

### **A** — 泵入口两相流体

与泵入口相关联的两相流体守恒端口。

### **B** — 泵出口两相流体

与泵出口相关联的两相流体守恒端口。

### **C** — 泵壳体机械旋转

与泵壳体相关联的机械旋转守恒端口。

### **R** — 泵轴机械旋转

与旋转泵轴相关联的机械旋转守恒端口。

## 参数

### 参数

### **Leakage and friction parameterization** — 泄漏流量和摩擦扭矩的参数化方法 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

计算由内部泄漏和摩擦引起的流量和扭矩损失的方法。如果模块参数通常可从组件数据表中获得，请使用 `Analytical`。当您选择 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 时，模块使用查找表将压差和轴角速度映射到组件效率或损失。

当您选择 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses` 时，模块分别执行与 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 设置相同的泄漏流量和摩擦扭矩计算。当您选择 `Input signal - volumetric and mechanical efficiencies` 时，模块启用 **EV** 和 **EM** 端口。您可以使用这些端口指定容积效率和机械效率。当您选择 `Input signal - volumetric and mechanical losses` 时，模块启用 **LV** 和 **LM** 端口。您可以使用这些端口指定容积损失和机械损失。

### **Displacement** — 每轴旋转排出的流体体积 `30` `cm^3/rev`（默认）| 正标量

每轴旋转排出的流体体积。模块在整个仿真过程中保持此值不变。

### **Nominal shaft angular velocity** — 给定容积效率对应的轴角速度 `1800` `rpm`（默认）| 标量

与给定容积效率对应的旋转轴角速度。制造商数据表中的标准工作条件通常会列出这些值。模块使用此参数计算泄漏流量和摩擦扭矩。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure gain** — 对应容积效率的压差 `10` `MPa`（默认）| 标量

与给定容积效率对应的压差。制造商数据表中的标准工作条件通常会列出这些值。模块使用此参数计算内部泄漏流量。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal dynamic viscosity** — 指定容积效率时的动态粘度 `0.9` `cP`（默认）| 标量

给定容积效率下液压流体的动态粘度。制造商数据表中的标准工作条件通常会列出这些值。模块使用此参数计算内部泄漏流量。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 指定标称条件下的容积效率 `0.92`（默认）| 正标量

给定条件下的容积效率。模块将容积效率定义为实际体积流量与理想体积流量之比。制造商数据表中的标准工作条件通常会列出这些值。模块使用此参数计算内部泄漏流量。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 理想机械功率与实际机械功率之比 `0.88`（默认）| 正标量

标称条件下理想机械功率与实际机械功率之比。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 引起轴旋转所需的最小扭矩 `0` `N*m`（默认）| 标量

克服密封摩擦并引起机械轴旋转所需的扭矩。此扭矩是总摩擦扭矩中与负载无关的分量。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure gain vector, dp** — 给定容积和机械效率或损失对应的压差 `[.1, 1, 2]` `MPa`（默认）| 向量

对应表格效率或损失数据的压差。该向量必须至少包含两个元素，且严格递增。

指定单个象限（*ɷ*，*Δp*）的数据。有关参数规格对应的操作模式及所得象限，请参阅 Operating Modes。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses`。

### **Shaft angular velocity vector, w** — 指定容积和机械效率或损失时的角速度 `[250, 500, 1000, 2000, 3000, 4000]` `rpm`（默认）| 向量

对应表格效率或损失数据的轴角速度。该向量必须至少包含两个元素，且严格递增。

指定单个象限（*ɷ*，*Δp*）的数据。有关参数规格对应的操作模式及所得象限，请参阅 Operating Modes。

#### 依赖

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses`。

### **Volumetric efficiency table, e\_v(dp,w)** — 给定压力增益和角速度下的容积效率 `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]`（默认）| 矩阵

给定流体压力增益和轴角速度下的容积效率。效率必须在 (0,1] 范围内。*M* 和
*N* 是指定查找表向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

指定单象限 (*ɷ*, *Δp*) 的数据。有关参数规格对应的运行模式及由此产生的象限，请参阅 Operating Modes。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w)** — 给定压力增益和角速度下的机械效率 `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]`（默认）| 矩阵

给定流体压力增益和轴角速度下的机械效率。效率必须在 (0,1] 范围内。*M* 和
*N* 是指定查找表向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

指定单象限 (*ɷ*, *Δp*) 的数据。有关参数规格对应的运行模式及由此产生的象限，请参阅 Operating Modes。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w)** — 对应压力增益和角速度下的内部泄漏流量 `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3` `m^3/s`（默认）| 矩阵

指定流体压力增益和轴角速度下的容积损失。容积损失是端口 **A** 和端口 **B** 之间的内部泄漏体积流量。*M* 和
*N* 是指定查找表向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

指定单象限 (*ɷ*, *Δp*) 的数据。有关参数规格对应的运行模式及由此产生的象限，请参阅 Operating Modes。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w)** — 对应压力增益和角速度下的摩擦力矩 `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626]` `N*m`（默认）| 矩阵

给定压力增益和轴角速度下的机械损失。该模块将机械损失定义为由于密封件和内部组件产生的摩擦力矩。*M* 和 *N* 是指定查找表向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

指定单象限 (*ɷ*, *Δp*) 的数据。有关参数规格对应的运行模式及由此产生的象限，请参阅 Operating Modes。机械损失的表格数据必须遵循图中的约定，即在正角速度下为正值，在负角速度下为负值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Minimum volumetric efficiency** — 容积效率输入信号的下饱和边界 `1e-3`（默认）| (0,1) 范围内的标量

容积效率允许的最小值。来自物理信号端口 **EV** 的输入将在低于此值时饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率输入信号的上饱和边界 `1`（默认）| 正标量

容积效率允许的最大值。来自物理信号端口 **EV** 的输入将在高于此值时饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 容积效率输入信号的下饱和边界 `1e-3`（默认）| (0,1) 范围内的标量

机械效率允许的最小值。来自物理信号端口 **EM** 的输入将在低于此值时饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum mechanical efficiency** — 容积效率输入信号的上饱和边界 `1`（默认）| (0,1) 范围内的标量

机械效率允许的最大值。来自物理信号端口 **EM** 的输入将在高于此值时饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Pressure gain threshold for motor-pump transition** — 启动马达与泵模式之间平滑过渡的压力增益 `1e-3` `MPa`（默认）| 标量

从入口到出口的压力增益，低于该值时模块开始在马达和泵模式之间过渡。该模块使用双曲正切函数来平滑泄漏流量和摩擦力矩。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **Angular velocity threshold for motor-pump transition** — 启动泵与马达模式之间平滑过渡的角速度 `100` `rpm`（默认）| 标量

轴角速度，低于该值时模块开始在泵和马达模式之间过渡。该模块使用双曲正切函数来平滑泄漏流量和摩擦力矩。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **Cross-sectional area at ports A and B** — 组件入口和出口处的流通面积 `0.01` `m^2`（默认）| 正标量

组件入口和出口处的流通面积。假设各面积相等。

### **Report when fluid is not fully liquid** — 流体未完全为液体时的通知 `None`（默认）| `Warning` | `Error`

当蒸汽质量大于 0（表明流体未完全为液体）时，模块是不执行任何操作、生成警告还是生成错误。

### **检查是否超出所提供表格数据的范围** — 超出表格数据范围工况的仿真警告模式 `None`（默认）| `Warning` | `Error`

超出表格数据范围工况的仿真警告模式。如果选择 `Warning`，当流体压力增益或轴角速度超出指定的表格数据时，模块会生成警告。该警告不会导致仿真停止。如果选择 `Error`，当工况超出表格数据范围时，仿真将停止。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **检查是否在泵模式之外运行** — 泵模式之外工况的仿真警告模式 `None`（默认）| `Warning` | `Error`

泵模式之外工况的仿真警告模式。当将此参数设置为 `Warning` 时，如果泵转变为马达模式，模块会生成警告。该警告不会导致仿真停止。如果选择 `Error`，当工况超出泵模式时，仿真将停止。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### 故障

### **排量故障** — 用于对排量故障建模的选项 `Add fault`

用于对模块中的排量故障建模的选项。发生故障时，排量按 **Faulted displacement factor** 参数的值进行缩放。要添加故障，请点击 **Add fault** 超链接。

### **故障排量因子** — 用于缩放故障排量的因子 `0.5`（默认）| 正标量

模块在发生故障时用于缩放排量的因子。

#### 依赖关系

要启用此参数，请点击 **Displacement fault** 参数的 **Add fault** 超链接。

### **泄漏故障** — 用于对泄漏故障建模的选项 `Add fault`

用于对模块中的泄漏故障建模的选项。发生故障时，容积效率或损失按 **Faulted leakage factor** 参数的值进行缩放。要添加故障，请点击 **Add fault** 超链接。

### **故障泄漏因子** — 用于缩放泄漏故障的因子 `2.0`（默认）| 正标量

模块在发生故障时用于缩放容积效率或损失的因子。

#### 依赖关系

要启用此参数，请点击 **Leakage fault** 参数的 **Add fault** 超链接。

### **轴摩擦扭矩故障** — 用于对轴摩擦扭矩故障建模的选项 `Add fault`

用于对模块中的轴摩擦扭矩故障建模的选项。发生故障时，机械效率或损失按 **Faulted shaft friction torque factor** 参数的值进行缩放。要添加故障，请点击 **Add fault** 超链接。

### **故障轴摩擦扭矩因子** — 用于缩放轴摩擦扭矩故障的因子 `2.0`（默认）| 正标量

模块在发生故障时用于缩放机械效率或损失的因子。

#### 依赖关系

要启用此参数，请点击 **Shaft friction torque fault** 参数的 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2024b：使用 Simscape faults 接口对故障建模

Fixed-Displacement Pump (2P) 模块现在支持 Simscape faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2024a：检查模块是否在计算数据范围之外运行

**Check if operating beyond the quadrants of supplied tabulated data** 参数已重命名为 **Check if operating beyond the range of supplied tabulated data**。您可以启用 **Check if operating beyond the range of supplied tabulated data** 参数来检查模块是否在模块参数中指定的数据之外运行，即在模块已扩展数据的区域中运行。

## 描述

机械-液压功率转换装置

Fixed-Displacement Pump (2P) 模块表示一个泵，它从机械旋转网络提取功率并将其输送到两相流体网络。泵排量固定为您通过 **Displacement** 参数指定的常数值。

端口 **A** 和 **B** 表示泵入口。端口 **R** 和 **C** 表示驱动轴和壳体。在正常运行期间，如果端口 **R** 相对于端口 **C** 的角速度为正，则从端口 **A** 到端口 **B** 的压力增益为正。

Fixed-Displacement Pump (2P) 模块假定液体进入泵入口。您可以使用 **Report when fluid is not fully liquid** 参数来选择当流体不满足液体条件时模块的行为。要在两相流体网络中输送蒸汽，请使用压缩机。

### 运行模式

该模块有四种运行模式，如下图所示。

工作模式取决于从端口 **A** 到端口 **B** 的压力增益 *Δp = p*B – *p*A 以及角速度 *ω = ω*R – *ω*C：

- 标记为 **1** 的象限表示正向泵模式。在此模式下，正的轴角速度导致从端口 **A** 到端口 **B** 的压力升高，以及从端口 **A** 到端口 **B** 的流量
- 标记为 **2** 的象限表示反向马达模式。在此模式下，从端口 **B** 到端口 **A** 的流量导致从 **B** 到 **A** 的压力降低以及负的轴角速度。
- 标记为 **3** 的象限表示反向泵模式。在此模式下，负的轴角速度导致从端口 **B** 到端口 **A** 的压力升高，以及从端口 **B** 到端口 **A** 的流量
- 标记为 **4** 的象限表示正向马达模式。在此模式下，从端口 **A** 到端口 **B** 的流量导致从 **A** 到 **B** 的压力降低以及正的轴角速度。

与系统响应时间相比，泵的响应时间可以忽略不计。泵几乎瞬间达到稳态，并被视为准稳态组件。

### 能量平衡

该模块将泵所做的机械功与能量交换相关联。控制能量平衡方程为

ϕA+ϕB+Phydro=0,

其中：

- *Φ*A 和 *Φ*B 分别是端口 **A** 和 **B** 处的能量流率。
- *P*hydro 是泵液压功率，它是泵端口之间压力差的函数：Phydro=Δpm˙ρ。

模块由于扭矩 *τ* 和角速度 *ω* 产生机械功率：

Pmech=τω。

### 流量和驱动力矩

泵处生成的质量流量率为

m˙=m˙Ideal−m˙Leak,

其中：

- m˙ 是实际质量流量率。
- m˙Ideal 是理想质量流量率。
- m˙Leak 是内部泄漏质量流量率。

为泵提供动力所需的驱动力矩为

τ=τIdeal+τFriction,

其中：

- *τ* 是实际驱动力矩。
- *τ*Ideal 是理想驱动力矩。
- *τ*Friction 是摩擦力矩。

**理想流量率和理想扭矩**

理想质量流量率为

m˙Ideal=ρDω,

理想所需扭矩为

τIdeal=DΔp,

其中：

- *ρ* 是端口 **A** 和 **B** 处流体密度的平均值。
- *D* 是 **Displacement** 参数。
- *ω* 是轴角速度。
- *Δp* 是从入口到出口的压力增益。

### 泄漏与摩擦参数化

您可以通过使用表格化的效率或损失，或者通过使用输入效率或输入损失，以解析方式对泄漏和摩擦进行参数化。

**解析**

当您将 **Leakage and friction parameterization** 参数设置为 `Analytical` 时，泄漏流量为

m˙Leak=KHPρAvgΔpμAvg，

摩擦力矩为

τFriction=(τ0+KTP|Δp|)tanh(4ω(5⋅10−5)ωNom)，

其中：

- *K*HP 是层流管道流的 Hagen-Poiseuille 系数。该模块根据指定的标称参数计算此系数。
- *μ* 是流体的动力粘度，即各端口处值的平均值。
- *K*TP 是标称排量下的摩擦力矩与压力增益系数，该模块根据 **Mechanical efficiency at nominal conditions** 参数 *ηm* 确定：

  k=τfr,nom−τ0Δpnom。

  *τfr,nom* 是标称条件下的摩擦力矩：

  τfr,nom=(1−ηm,nomηm,nom)DΔpnom。
- *Δp*Nom 是 **Nominal pressure gain** 参数的值。该值是指定标称容积效率时的压力增益。
- *τ*0 是 **No-load torque** 参数的值。
- *ω*Nom 是 **Nominal shaft angular velocity** 参数的值。

该模块根据标称流体和组件参数确定 Hagen-Poiseuille 系数

KHP=DωNomμNom(1−ηv,Nom)ΔpNom，

其中：

- *ω*Nom 是 **Nominal shaft angular velocity** 参数的值。该值是模块指定标称容积效率时的角速度。
- *μ*Nom 是 **Nominal Dynamic viscosity** 参数的值。该值是模块指定标称容积效率时的动力粘度。
- *η*v,Nom 是 **Volumetric efficiency at nominal conditions** 参数的值。这是对应于指定标称条件的容积效率。

**表格化效率**

当您将 **Leakage and friction parameterization** 参数设置为 `Tabulated data - volumetric and mechanical efficiencies` 时，泄漏流量为

m˙Leak=m˙Leak,Pump(1+α)2+m˙Leak,Motor(1−α)2，

摩擦力矩为

τFriction=τFriction,Pump1+α2+τFriction,Motor1−α2，

其中：

- *α* 是用于电机-泵过渡的数值平滑参数。
- m˙Leak,Motor 是电机模式下的泄漏流量。
- m˙Leak,Pump 是泵模式下的泄漏流量。
- *τ*Friction,Motor 是电机模式下的摩擦力矩。
- *τ*Friction,Pump 是泵模式下的摩擦力矩。

此双曲函数描述了平滑参数 *α*

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold)，

其中：

- *Δp*Threshold 是 **Pressure gain threshold for motor-pump transition** 参数的值。
- *ω*Threshold 是 **Angular velocity threshold for motor-pump transition** 参数的值。

该模块根据容积效率计算泄漏流量，**Volumetric efficiency table** 参数在 *Δp*–*ɷ* 域上指定该效率。在泵模式下运行时，泄漏流量为：

m˙Leak,Pump=(1−ηv)m˙Ideal，

其中 *η*v 是容积效率，该模块通过插值或外推表格化数据获得。类似地，在电机模式下运行时，泄漏流量为：

m˙Leak,Motor=−(1−ηv)m˙。

该模块根据机械效率计算摩擦力矩，**Mechanical efficiency table** 参数在 *Δp*–*ɷ* 域上指定该效率。在泵模式下运行时，摩擦力矩为

τFriction,Pump=(1−ηm)τ，

其中 *η*m 是机械效率，该模块通过插值或外推表格化数据获得。类似地，在电机模式下运行时，摩擦力矩为

τFriction,Motor=−(1−ηm)τIdeal。

**表格化损失**

当您将 **Leakage and friction parameterization** 参数设置为 `Tabulated data - volumetric and mechanical losses` 时，该模块以表格形式在 *Δp*–*ɷ* 域上指定泄漏体积流量：

qLeak=qLeak(Δp,ω)。

该模块根据体积流量计算由泄漏引起的质量流量：

m˙Leak=ρqLeak。

该模块以表格形式计算摩擦力矩：

τFriction=τLoss(Δp,ω)tanh(4ωωthreshold)，

其中 *q*Leak(*Δp*,*ω*) 和 *τ*Loss(*Δp*,*ω*) 是通过插值或外推 **Volumetric loss table** 和 **Mechanical loss table** 参数中的表格化数据所指定的体积损失和机械损失。

**输入效率**

当您将 **Leakage and friction parameterization** 参数设置为 `Input signal - volumetric and mechanical efficiencies` 时，泄漏流量和摩擦力矩的计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。该模块将容积效率和机械效率查找表替换为物理信号输入端口 **EV** 和 **EM**。

效率是正值量，其值介于 `0` 和 `1` 之间。该模块将超出这些边界的输入值设置为 `0`（对于小于 `0` 的输入）或 `1`（对于大于 `1` 的输入）。该模块将效率信号饱和在 **Minimum volumetric efficiency** 或 **Minimum mechanical efficiency** 参数的值以及 **Maximum volumetric efficiency** 或 **Maximum mechanical efficiency** 参数的值处。

**输入损失**

当您将 **Leakage and friction parameterization** 参数设置为 `Input signal - volumetric and mechanical losses` 时，泄漏流量和摩擦力矩的计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。该模块将容积损失和机械损失查找表替换为物理信号输入端口 **LV** 和 **LM**。

该模块期望输入为正值，并根据组件运行的 *Δp*–*ɷ* 象限自动设置符号。如果您提供负信号，该模块将返回零损失。

### 故障

要对故障建模，请在**故障**部分中，单击要建模的故障旁边的**添加故障**超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

您可以对位移故障、泄漏或轴摩擦扭矩故障建模。

当启用**位移故障**参数时，模块会在故障触发时按**故障位移因子**参数的值缩放位移，

DFault=fDD，

其中 *fD* 是**故障位移因子**参数的值。当**泄漏和摩擦参数化**参数为 `Analytical` 时，模块不使用故障位移值来计算 Hagen-Poiseuille 系数或标称条件下的摩擦力矩。

当启用**泄漏故障**参数且**泄漏和摩擦参数化**为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障容积效率为

ηv,Fault=ηvfLeak，

其中 *fLeak* 是**故障泄漏因子**参数的值，*ηv* 是容积效率。当**泄漏和摩擦参数化**为 `Analytical` 时，模块使用故障容积效率来计算 Hagen-Poiseuille 系数。

当**泄漏和摩擦参数化**为 `Tabulated data - volumetric and mechanical losses` 或 `Input signal - volumetric and mechanical losses` 时，故障泄漏体积流量为

qLeak,Fault=fLeakqLeak。

当启用**轴摩擦扭矩故障**参数且**泄漏和摩擦参数化**为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障机械效率为

ηm,Fault=ηmfFriction，

其中 *fFriction* 是**故障轴摩擦扭矩因子**参数的值，*ηm* 是机械效率。当**泄漏和摩擦参数化**为 `Analytical` 时，模块使用故障机械效率来计算标称条件下的摩擦力矩。

当**泄漏和摩擦参数化**为 `Tabulated data - volumetric and mechanical losses` 或 `Input signal - volumetric and mechanical losses` 时，故障摩擦力矩为

τFriction,Fault=fFrictionτFriction。

### 假设和限制

- 模块将泵视为准稳态组件。
- 模块忽略流体惯性和高度的影响。
- 泵壁是刚性的。
- 模块忽略外部泄漏。
