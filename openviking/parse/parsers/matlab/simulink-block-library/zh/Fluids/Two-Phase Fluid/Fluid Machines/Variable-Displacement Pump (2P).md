---
type: simulink-block
title: 'Variable-Displacement Pump (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Fluid Machines'
documentation_page: 'variabledisplacementpump2p'
documentation_source_path: 'ref/variabledisplacementpump2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable-Displacement Pump (2P)

## 端口

### 输入

### **D** — 排量体积，cm^3/rev 物理信号

用于旋转所排出流体体积的物理信号输入端口。平滑函数可缓解正负输入值之间的过渡。

### **EV** — 容积效率，unitless 物理信号

用于容积效率系数的物理信号输入端口。输入信号上限为 **最大容积效率** 参数值，下限为 **最小容积效率** 参数值。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率，unitless 物理信号

用于机械效率系数的物理信号输入端口。输入信号上限为 **最大机械效率** 参数值，下限为 **最小机械效率** 参数值。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 容积损失，m^3/s 物理信号

用于容积损失的物理信号输入端口，容积损失是泵入口之间的内部泄漏流量。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 机械损失，N\*m 物理信号

用于机械损失的物理信号输入端口，机械损失是旋转泵轴上的摩擦扭矩。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses`。

### 守恒

### **A** — 泵入口两相流体

与泵入口关联的两相流体守恒端口。

### **B** — 泵出口两相流体

与泵出口关联的两相流体守恒端口。

### **C** — 泵壳体机械旋转

与泵壳体关联的机械旋转守恒端口。

### **R** — 泵轴机械旋转

与旋转泵轴关联的机械旋转守恒端口。

## 参数

### **泄漏和摩擦参数化** — 泄漏流量和摩擦扭矩的参数化 `Analytical`（默认） | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

用于计算由内部泄漏和摩擦引起的流量和扭矩损失的方法。如果模块参数通常可从组件数据表中获得，则使用 `Analytical`。当您选择 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 时，模块使用查找表将压力增益、角速度和排量映射到组件效率或损失。

当您选择 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses` 时，模块分别执行与 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 设置相同的泄漏流量和摩擦扭矩计算。当您选择 `Input signal - volumetric and mechanical efficiencies` 时，模块启用 **EV** 和 **EM** 端口。您使用这些端口指定容积效率和机械效率。当您选择 `Input signal - volumetric and mechanical losses` 时，模块启用 **LV** 和 **LM** 端口。您使用这些端口指定容积损失和机械损失。

### **标称排量** — 指定容积效率时的排量 `30` `cm^3/rev`（默认） | positive scalar

给定容积效率下的流体排量。制造商数据表中的标准工况通常会列出这些值。模块使用此参数计算泄漏流量和摩擦扭矩。

### **标称轴角速度** — 给定容积效率下的轴角速度 `1800` `rpm`（默认） | scalar

与给定容积效率对应的旋转轴角速度。制造商数据表中的标准工况通常会列出这些值。模块使用此参数计算泄漏流量和摩擦扭矩。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **标称压力增益** — 对应容积效率的压力增益 `10` `MPa`（默认） | scalar

与给定容积效率对应的压力增益。制造商数据表中的标准工况通常会列出这些值。模块使用此参数计算内部泄漏流量。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **标称动力粘度** — 指定容积效率时的动力粘度 `0.9` `cP`（默认） | scalar

给定容积效率下液压流体的动力粘度。这些值通常可在制造商数据表的标准工况下获得。模块使用此参数计算内部泄漏流量。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **标称工况下的容积效率** — 指定标称工况下的容积效率 `0.92`（默认） | scalar in the range (0,1)

给定工况下的容积效率。模块将容积效率定义为实际体积流量与理想体积流量之比。制造商数据表中的标准工况通常会列出这些值。模块使用此参数计算内部泄漏流量。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **标称工况下的机械效率** — 理想机械功率与实际机械功率之比 `0.88`（默认） | positive scalar

标称工况下理想机械功率与实际机械功率之比。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **空载扭矩** — 引起轴旋转所需的最小扭矩 `0` `N*m`（默认） | scalar

克服密封摩擦并使机械轴旋转所需的扭矩。此扭矩是总摩擦扭矩中与负载无关的分量。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **压力增益向量, dp** — 给定容积和机械效率或损失下的压力增益 `[.1, 1, 2]` `MPa`（默认） | vector

对应表格效率或损失数据的压力增益。向量必须至少包含两个元素，且严格递增。

为单个八分象限指定数据，(*ɷ*, *Δp*, *D*)。有关与参数指定和所得八分象限对应的运行模式，请参阅运行模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses`。

### **轴角速度向量, w** — 指定容积和机械效率或损失时的角速度 `[250, 500, 1000, 2000, 3000, 4000]` `rpm`（默认） | vector

对应表格效率或损失数据的轴角速度。向量必须至少包含两个元素，且严格递增。

为单个八分象限指定数据，(*ɷ*, *Δp*, *D*)。有关与参数指定和所得八分象限对应的运行模式，请参阅运行模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses`。

### **排量向量, D** — 指定容积和机械效率或损失时的排量 `[-30, -19, 19, 30]` `cm^3/rev`（默认） | vector

指定效率或损失表格数据时的排量。向量必须至少包含两个元素，且严格递增。

为单个八分象限指定数据，(*ɷ*, *Δp*, *D*)。有关与参数指定和所得八分象限对应的运行模式，请参阅运行模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses`。

### **容积效率表, e\_v(dp,w,D)** — 给定压力增益、角速度和排量下的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)`（默认） | matrix

在指定流体压力增益、轴角速度和排量下的容积效率。效率必须在 `0`–`1` 范围内。*M*、*N* 和 *L* 是指定查找表向量的大小：

- *M* 是 **压力增益向量, dp** 参数中向量元素的数量。
- *N* 是 **轴角速度向量, w** 参数中向量元素的数量。
- *L* 是 **排量向量, D** 参数中向量元素的数量。

为单个八分象限指定数据，(*ɷ*, *Δp*, *D*)。有关与参数指定和所得八分象限对应的运行模式，请参阅运行模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **机械效率表, e\_m(dp,w,D)** — 给定压力增益、角速度和排量下的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)`（默认） | matrix

与指定流体压力增益、轴角速度和排量对应的机械效率。效率必须在 `0`–`1` 范围内。*M*、*N* 和 *L* 是指定查找表向量的大小：

- *M* 是 **压力增益向量, dp** 参数中向量元素的数量。
- *N* 是 **轴角速度向量, w** 参数中向量元素的数量。
- *L* 是 **排量向量, D** 参数中向量元素的数量。

为单个八分象限指定数据，(*ɷ*, *Δp*, *D*)。有关与参数指定和所得八分象限对应的运行模式，请参阅运行模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **容积损失表, q\_loss(dp,w,D)** — 对应压力增益、角速度和排量下的内部泄漏流量 `repmat([.0282, .0253, .0241, .0235, .0291, .0325; .2596, .1271, .1017, .0917, .1216, .1142; .7874, .1901, .141, .1211, .1797, .1978] * 1e-3, 1, 1, 4)` `m^3/s`（默认） | matrix

在指定流体压力增益、轴角速度和排量下的容积损失。模块将容积损失定义为端口 **A** 和端口 **B** 之间的内部泄漏体积流量。*M* 和 *N* 是指定查找表向量的大小：

- *M* 是 **压力增益向量, dp** 参数中向量元素的数量。
- *N* 是 **轴角速度向量, w** 参数中向量元素的数量。
- *L* 是 **排量向量, D** 参数中向量元素的数量。

为单个八分象限指定数据，(*ɷ*, *Δp*, *D*)。有关与参数指定和所得八分象限对应的运行模式，请参阅运行模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **机械损失表, torque\_loss(dp,w,D)** — 对应压力增益、角速度和排量下的摩擦扭矩 `repmat([.002, .002, .002, .002, .002, .002; .06, .055, .055, .055, .055, .05; .19, .19, .18, .18, .17, .16], 1, 1, 4)` `N*m`（默认） | matrix

给定压力增益、轴角速度和排量下的机械损失。模块将机械损失定义为由密封和内部组件引起的摩擦扭矩。*M* 和 *N* 是指定查找表向量的大小：

- *M* 是 **压力增益向量, dp** 参数中向量元素的数量。
- *N* 是 **轴角速度向量, w** 参数中向量元素的数量。
- *L* 是 **排量向量, D** 参数中向量元素的数量。

为单个八分象限指定数据，(*ɷ*, *Δp*, *D*)。有关与参数指定和所得八分象限对应的运行模式，请参阅运行模式。机械损失的表格数据必须遵循图中的约定，即在正角速度下为正值，在负角速度下为负值。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **最小容积效率** — 容积效率输入信号的下饱和界限 `1e-3`（默认） | scalar in the range (0,1)

容积效率的最小允许值。来自物理信号端口 **EV** 的输入将在低于此值时饱和。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最大容积效率** — 容积效率输入信号的上饱和界限 `1`（默认） | scalar in the range (0,1)

容积效率的最大允许值。来自物理信号端口 **EV** 的输入将在高于此值时饱和。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最小机械效率** — 容积效率输入信号的下饱和界限 `1e-3`（默认） | scalar in the range (0,1)

机械效率的最小允许值。来自物理信号端口 **EM** 的输入将在低于此值时饱和。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最大机械效率** — 容积效率输入信号的上饱和界限 `1`（默认） | scalar in the range (0,1)

机械效率的最大允许值。来自物理信号端口 **EM** 的输入将在高于此值时饱和。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **马达-泵转换的压力增益阈值** — 开始马达和泵模式之间平滑转换的压力增益 `1e-3` `MPa`（默认） | scalar

从入口到出口的压力增益，低于该值时模块开始在马达和泵模式之间转换。模块使用双曲正切函数平滑泄漏流量和摩擦扭矩。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **电机-泵转换的角速度阈值** — 启动泵与电机模式之间平滑转换的角速度 `100` `rpm` (默认) | scalar

轴角速度，低于该值时模块开始电机模式与泵模式之间的转换。该模块使用双曲正切函数平滑泄漏流量和摩擦扭矩。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **端口 A 和 B 处的横截面积** — 组件入口和出口处的流通面积 `0.01` `m^2` (默认) | positive scalar

组件入口和出口处的流通面积。假定这些面积相等。

### **当流体未完全为液体时报告** — 当流体未完全为液体时的通知 `None` (默认) | `Warning` | `Error`

当蒸汽质量分数大于 0（表明流体未完全为液体）时，模块是不执行任何操作、生成警告还是生成错误。

### **检查是否超出提供的表格数据范围运行** — 用于工作条件超出表格数据范围时的仿真警告模式 `None` (默认) | `Warning` | `Error`

用于工作条件超出表格数据范围时的仿真警告模式。如果您选择 `Warning`，当流体压力增益或轴角速度超出指定的表格数据时，模块会生成警告。该警告不会导致仿真停止。如果您选择 `Error`，对于超出表格数据范围的条件，仿真将停止。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为：

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **检查是否在泵模式之外运行** — 用于工作条件超出泵模式时的仿真警告模式 `None` (默认) | `Warning` | `Error`

用于工作条件超出泵模式时的仿真警告模式。当您将此参数设置为 `Warning` 时，如果泵转换到电机模式，模块会生成警告。该警告不会导致仿真停止。如果您选择 `Error`，对于超出泵模式的条件，仿真将停止。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses`。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2024a：检查模块是否在计算数据范围之外运行

参数 **检查是否超出提供的表格数据的八分区运行** 已重命名为 **检查是否超出提供的表格数据范围运行**。您可以启用 **检查是否超出提供的表格数据范围运行** 参数来检查模块是否在模块参数指定的数据之外运行，也就是说，在模块已扩展数据的区域内运行。

## 描述

可变排量双向两相流体泵

Variable-Displacement Pump (2P) 模块表示从机械旋转网络提取功率并将其输送到两相流体网络的设备。泵排量在仿真期间根据端口 **D** 处的物理输入信号而变化。

端口 **A** 和 **B** 表示泵入口。端口 **R** 和 **C** 表示驱动轴和壳体。在正常运行期间，如果端口 **R** 相对于端口 **C** 的角速度为正，则从端口 **A** 到端口 **B** 的压力增益为正。

Variable-Displacement Pump (2P) 模块假定液体进入泵入口。您可以使用 **当流体未完全为液体时报告** 参数来选择当流体不满足液体条件时模块执行的操作。要在两相流体网络中输送蒸汽，请使用压缩机。

### 工作模式

该模块有四种工作模式，如下图所示。

工作模式取决于从端口 **A** 到端口 **B** 的压力增益 *Δp = p*B – *p*A；角速度 *ω = ω*R – *ω*C；以及端口 **D** 处的流体体积排量。上图将这些模式映射到 *Δp*-*ω*-*D* 图的八分区：

- 标记为 **1** 的象限表示正向泵模式。在此模式下，正的轴角速度导致从端口 **A** 到端口 **B** 的压力升高，以及从端口 **A** 到端口 **B** 的流量
- 标记为 **2** 的象限表示反向电机模式。在此模式下，从端口 **B** 到端口 **A** 的流量导致从 **B** 到 **A** 的压力降低以及负的轴角速度。
- 标记为 **3** 的象限表示反向泵模式。在此模式下，负的轴角速度导致从端口 **B** 到端口 **A** 的压力升高，以及从端口 **B** 到端口 **A** 的流量
- 标记为 **4** 的象限表示正向电机模式。在此模式下，从端口 **A** 到端口 **B** 的流量导致从 **A** 到 **B** 的压力降低以及正的轴角速度。
- 标记为 **5** 的象限表示反向电机模式。在此模式下，从端口 **B** 到端口 **A** 的流量导致从 **B** 到 **A** 的压力降低以及正的轴角速度。
- 标记为 **6** 的象限表示正向泵模式。在此模式下，负的轴角速度导致从端口 **A** 到端口 **B** 的压力升高，以及从端口 **A** 到端口 **B** 的流量
- 标记为 **7** 的象限表示正向电机模式。在此模式下，从端口 **A** 到端口 **B** 的流量导致从 **A** 到 **B** 的压力降低以及负的轴角速度。
- 标记为 **8** 的象限表示反向泵模式。在此模式下，正的轴角速度导致从端口 **B** 到端口 **A** 的压力升高，以及从端口 **B** 到端口 **A** 的流量

与系统响应时间相比，泵的响应时间可忽略不计。泵几乎瞬时达到稳态，并被视作准稳态组件。

### 能量平衡

该模块将泵所做的机械功与能量交换相关联。支配性的能量平衡方程为：

ϕA+ϕB+Phydro=0,

其中：

- *Φ*A 和 *Φ*B 分别是端口 **A** 和 **B** 处的能量流率。
- *P*hydro 是泵液压功率，它是泵端口之间压力差的函数：Phydro=Δpm˙ρ。

该模块因扭矩 *τ* 和角速度 *ω* 产生机械功率：

Pmech=τω.

### 流量和驱动扭矩

泵处生成的质量流量为

m˙=m˙Ideal−m˙Leak,

其中：

- m˙ 是实际质量流量。
- m˙Ideal 是理想质量流量。
- m˙Leak 是内部泄漏质量流量。

驱动泵所需的驱动扭矩为

τ=τIdeal+τFriction,

其中：

- *τ* 是实际驱动扭矩。
- *τ*Ideal 是理想驱动扭矩。
- *τ*Friction 是摩擦扭矩。

**理想流量和理想扭矩**

理想质量流量为

m˙Ideal=ρDω,

理想所需扭矩为

τIdeal=DΔp,

其中：

- *ρ* 是端口 **A** 和 **B** 处流体密度的平均值。
- *ω* 是轴角速度。
- *Δp* 是从入口到出口的压力增益。
- *D* 是在物理信号端口 **D** 处指定的 **排量**。

### 泄漏和摩擦参数化

您可以通过解析方法、使用表格化效率或损耗，或使用输入效率或输入损耗来参数化泄漏和摩擦。

**解析**

当您将 **泄漏和摩擦参数化** 参数设置为 `Analytical` 时，泄漏流量为

m˙Leak=KHPρAvgΔpμAvg,

摩擦扭矩为

τFriction=(τ0+KTP|Δp||D|DNomtanh4ω(5e−5)ωNom),

其中：

- *K*HP 是层流管道流的 Hagen-Poiseuille 系数。该模块根据指定的额定参数计算此系数。
- *μ* 是流体的动力黏度，它是各端口值的平均值。
- *k* 是额定排量下的摩擦扭矩与压力增益系数，该模块根据 **额定条件下的机械效率** 参数 *ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* 是额定条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nomηm,nom)DnomΔpnom.
- *Δp*Nom 是 **额定压力增益** 参数的值。该值是规定额定容积效率时的压力增益。
- *D*Nom 是 **额定排量** 参数的值。
- *τ*0 是 **空载扭矩** 参数的值。
- *ω*Nom 是 **额定轴角速度** 参数的值。

该模块根据额定流体和组件参数确定 Hagen-Poiseuille 系数

KHP=DNomωNomμNom(1−ηv,Nom)ΔpNom,

其中：

- *ω*Nom 是 **额定轴角速度** 参数的值。该值是模块规定额定容积效率时的角速度。
- *μ*Nom 是 **额定动力黏度** 参数的值。该值是模块规定额定容积效率时的动力黏度。
- *η*v,Nom 是 **额定条件下的容积效率** 参数的值。这是与指定额定条件对应的容积效率。

**表格化效率**

当您将 **泄漏和摩擦参数化** 参数设置为 `Tabulated data - volumetric and mechanical efficiencies` 时，泄漏流量为

m˙Leak=m˙Leak,Pump(1+α)2+m˙Leak,Motor(1−α)2,

摩擦扭矩为

τFriction=τFriction,Pump1+α2+τFriction,Motor1−α2,

其中：

- *α* 是用于电机-泵转换的数值平滑参数。
- m˙Leak,Motor 是电机模式下的泄漏流量。
- m˙Leak,Pump 是泵模式下的泄漏流量。
- *τ*Friction,Motor 是电机模式下的摩擦扭矩。
- *τ*Friction,Pump 是泵模式下的摩擦扭矩。

此双曲函数描述平滑参数 *α*

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold)·tanh(4DDThreshold),

其中：

- *Δp*Threshold 是 **泵-电机转换的压力增益阈值** 模块参数的值。
- *ω*Threshold 是 **泵-电机转换的角速度阈值** 模块参数的值。
- *D*Threshold 是 **电机-泵转换的角速度阈值** 模块参数的值。

该模块根据容积效率计算泄漏流量，**容积效率表** 参数在 *Δp*–*ɷ*–*D* 域上指定该效率。在泵模式下运行时，泄漏流量为：

m˙Leak,Pump=(1−ηv)m˙Ideal,

其中 *η*v 是容积效率，该模块通过表格数据的插值或外推获得该效率。类似地，在电机模式下运行时，泄漏流量为：

m˙Leak,Motor=−(1−ηv)m˙.

该模块根据机械效率计算摩擦扭矩，**机械效率表** 参数在 *Δp*–*ɷ*–*D* 域上指定该效率。在泵模式下运行时，摩擦扭矩为

τFriction,Pump=(1−ηm)τ,

其中 *η*m 是机械效率，该模块通过表格数据的插值或外推获得该效率。类似地，在电机模式下运行时，摩擦扭矩为

τFriction,Motor=−(1−ηm)τIdeal.

**表格化损耗**

当您将 **泄漏和摩擦参数化** 参数设置为 `Tabulated data - volumetric and mechanical losses` 时，该模块以表格形式在 *Δp*–*ɷ*–*D* 域上指定泄漏体积流量：

qLeak=qLeak(Δp,ω,D).

该模块根据体积流量计算由泄漏引起的质量流量：

m˙Leak=ρqLeak.

该模块以表格形式计算摩擦扭矩：

τFriction=τFriction(Δp,ω,D),

其中 *q*Leak(*Δp*,*ω*,*D*) 和 *τ*Friction(*Δp*,*ω*,*D*) 是体积损耗和机械损耗，通过在 **体积损耗表** 和 **机械损耗表** 参数中表格数据的插值或外推来指定。

**输入效率**

当您将 **泄漏和摩擦参数化** 参数设置为 `Input signal - volumetric and mechanical efficiencies` 时，泄漏流量和摩擦扭矩计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。该模块将容积效率和机械效率查找表替换为物理信号输入端口 **EV** 和 **EM**。

当您将 **泄漏和摩擦参数化** 参数设置为 `Input signal - volumetric and mechanical losses` 时，泄漏流量和摩擦扭矩计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。该模块将体积损耗和机械损耗查找表替换为物理信号输入端口 **LV** 和 **LM**。

**输入损耗**

当您将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies` 时，泄漏流量和摩擦扭矩计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。体积损耗和机械损耗查找表被替换为您通过端口 **LV** 和 **LM** 指定的物理信号输入。

该模块期望输入为正，并根据组件运行所在的 *Δp*–*ɷ* 象限自动设置符号。如果您提供负信号，该模块返回零损耗。

### 假设和限制

- 该模块将泵视为准稳态组件。
- 该模块忽略流体惯性和高度的影响。
- 泵壁为刚性。
- 该模块忽略外部泄漏。
