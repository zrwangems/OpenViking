---
type: simulink-block
title: 'Orifice (TL)'
family: 'thermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices'
documentation_page: 'orificetl'
documentation_source_path: 'ref/orificetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Orifice (TL)

## 端口

### 输入

### **S** — 控制构件位移，m physical signal

阀控制构件的瞬时位移。
### 守恒

### **A** — Flow passage thermal liquid

与流体可进入或离开阀的开口相关联的热液体守恒端口。

### **B** — Flow passage thermal liquid

与流体可进入或离开阀的开口相关联的热液体守恒端口。

## 参数

### 参数

### **Orifice type** — 孔口类型 `Variable` (default) | `Constant`

孔口类型，由孔口面积定义。当设置为 `Variable` 时，孔口面积根据端口 **S** 处接收的输入信号而变化。

- `Orifice area`—分配的面积在整个仿真过程中不变。
- `Tabulated data - Volumetric flow rate vs. pressure drop`—面积保持不变，但通过孔口的体积流量可以变化。该值直接从 **Volumetric flow rate vector** 和 **Pressure drop vector** 数据集插值得到。
- `Tabulated data - Mass flow rate vs. pressure drop`—面积保持不变，但通过孔口的体积流量可以变化。该值直接从 **Mass flow rate vector** 和 **Pressure drop vector** 数据集插值得到。

当将 **Orifice type** 设置为 `Variable` 时，有四个选项。

- `Linear - Area vs. control member position`. 面积由相对于完全打开或完全关闭孔口的控制构件位置的线性关系确定。该位置由端口 **S** 处的可变 physical signal 设置。
- `Tabulated data - Area vs. control member position`. 开口面积根据端口 **S** 处接收的控制构件位置，从 **Control member position vector** 和 **Orifice area vector** 插值得到。
- `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`. 体积流量根据端口 **S** 处接收的控制构件位置以及端口 **A** 和 **B** 之间的压降，直接从用户提供的 **Control member position vector, s**、**Pressure drop vector, dp** 和 **Volumetric flow rate table, q(s,dp)** 参数插值得到。
- `Tabulated data - Mass flow rate vs. control member position and pressure drop`. 质量流量根据端口 **S** 处接收的控制构件位置以及端口 **A** 和 **B** 之间的压降，直接从用户提供的 **Control member position vector, s**、**Pressure drop vector, dp** 和 **Mass flow rate table, mdot(s,dp)** 参数插值得到。

### **Orifice parameterization** — 恒定孔口参数化 `Orifice area` (default) | `Tabulated data - Volumetric flow rate vs. pressure drop` | `Tabulated data - Mass flow rate vs. pressure drop`

对孔口开度特性进行建模所采用的方法。默认设置规定孔口开口面积与孔口开度之间为线性关系。其他设置允许以表格形式指定一般非线性关系：其中一种情况是在开口面积与孔口开度之间，另一种情况是在质量流量与孔口开度及端口间压降之间。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Constant`。

### **Orifice parameterization** — 可变孔口参数化 `Linear - Area vs. control member position` (default) | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` | `Tabulated data - Mass flow rate vs. control member position and pressure drop`

当将 **Orifice type** 设置为 `Variable` 时，有四个选项。

- `Linear - Area vs. control member position`. 面积由相对于完全打开或完全关闭孔口的控制构件位置的线性关系确定。该位置由端口 **S** 处的可变 physical signal 设置。
- `Tabulated data - Area vs. control member position`. 开口面积根据端口 **S** 处接收的控制构件位置，从 **Control member position vector** 和 **Orifice area vector** 插值得到。
- `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`. 体积流量根据端口 **S** 处接收的控制构件位置以及端口 **A** 和 **B** 之间的压降，直接从用户提供的 **Control member position vector, s**、**Pressure drop vector, dp** 和 **Volumetric flow rate table, q(s,dp)** 参数插值得到。
- `Tabulated data - Mass flow rate vs. control member position and pressure drop`. 质量流量根据端口 **S** 处接收的控制构件位置以及端口 **A** 和 **B** 之间的压降，直接从用户提供的 **Control member position vector, s**、**Pressure drop vector, dp** 和 **Mass flow rate table, mdot(s,dp)** 参数插值得到。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`。

### **Orifice area** — 孔口开口面积 `1e-3` `m^2` (default) | positive scalar

孔口开口的横截面积。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### **Pressure drop vector** — 用于表格化参数化的压差值的向量 `[-4, -3, -2, -1, -.5, 0, .5, 1, 2, 3, 4] MPa` (default) | 1-by-*n* vector

用于体积流量表格化参数化的压差值向量。此向量中的值与 **Volumetric flow rate vector** 参数中的值一一对应。压降向量值按升序列出。体积流量直接从 **Volumetric flow rate vector** 参数插值得到，而该参数取决于 **Pressure drop vector** 参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure drop`。

### **Volumetric flow rate vector** — 体积流量值的向量 `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] .* 1e-3 m^3/s` (default) | 1-by-*n* vector

用于体积流量表格化参数化的体积流量值向量。此向量中的值与 **Pressure drop vector** 参数中的值一一对应。体积流量直接从提供的 **Volumetric flow rate vector** 参数插值得到，而该参数取决于 **Pressure drop vector** 参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure drop`。

### **Mass flow rate vector** — 质量流量值的向量 `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] kg/s` (default) | vector | 1-by-*n* vector

用于体积流量表格化参数化的质量流量值向量。此向量中的值与 **Pressure drop vector** 参数中的值一一对应。质量流量直接从提供的 **Mass flow rate vector** 参数插值得到，而该参数取决于 **Pressure drop vector** 参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. pressure drop`。

### **Control member position at closed orifice** — 控制构件偏移 `0 m` (default) | scalar

可变孔口完全关闭时的初始控制构件偏移。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear – Area vs. control member position`。

### **Control member travel between closed and open orifice** — 控制构件最大行程 `5e-3 m` (default) | positive scalar

控制构件在关闭和打开孔口之间移动的最大距离。当达到 **Control member position at closed orifice** 与 **Control member travel between closed and open orifice** 参数之和时，孔口完全打开。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Opening orientation** — 使孔口打开的控制构件位移方向 `Positive control member displacement opens orifice` (default) | `Negative control member displacement opens orifice`

使可变孔口打开的控制构件位移方向。正方向表示 **S** 处的正信号打开孔口。负方向表示 **S** 处的负信号打开孔口。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Maximum orifice area** — 最大孔口开口面积 `1e-4 m^2` (default) | positive scalar

仿真期间经历的最大孔口面积。使用 `Tabulated data - Area vs. control member position` 时，最大孔口面积是 **Orifice area vector** 参数的最后一个元素。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Leakage area** — 完全关闭位置时的孔口间隙面积 `1e-10 m^2` (default) | positive scalar

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持在指定的泄漏面积。此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖项

要启用此参数，请将 **Orifice** type 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Control member position vector** — 控制构件位置的向量 `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

用于孔口面积表格化参数化的控制构件位置向量。向量元素与 **Orifice area vector** 参数中的值一一对应。向量元素必须严格单调递增或递减。孔口开口面积从 **Orifice area vector** 插值得到，而该向量取决于 **Control member position vector** 参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Orifice area vector** — 孔口开口面积值的向量 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2` (default) | 1-by-*n* vector

用于孔口面积表格化参数化的孔口面积值向量。此向量中的值与 **Control member position vector** 参数中的元素一一对应。如果向量递增，则此向量的第一个元素是孔口泄漏面积，最后一个元素是最大孔口面积。如果向量递减，则此向量的第一个元素是孔口最大孔口面积，最后一个元素是泄漏面积。孔口开口面积从 **Orifice area vector** 参数插值得到，而该参数取决于 **Control member position vector** 参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Discharge coefficient** — 流量系数 `0.64` (default) | positive scalar

用于考虑理论流动中排放损失的修正系数。

#### 依赖项

要启用此参数，请设置以下任一项：

- 将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。
- 将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### **Critical Reynolds number** — 层流雷诺数上限 `150` (default) | positive scalar

通过孔口的层流雷诺数上限。

#### 依赖项

要启用此参数，请设置以下任一项：

- 将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。
- 将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### **Smoothing factor** — 数值平滑因子 `0.01` (default) | positive scalar in the range [0,1]

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入渐变层。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `on` (default) | `off`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。清除 **Pressure recovery** 复选框时，不会捕捉到该压力增加。

#### 依赖项

要启用此参数，请设置以下任一项：

- 将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。
- 将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### **Control member position vector, s** — 开度值的向量 `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

用于体积流量表格化参数化的控制构件位置向量。控制构件位置向量与 **Pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **Volumetric flow rate table, q(s,dp)** 参数。正位移对应于阀打开。值按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 或 `Tabulated data - Mass flow rate vs. control member position and pressure drop`。

### **Pressure drop vector, dp** — 压降值的向量 `[.3, .5, .7] MPa` (default) | 1-by-*n* vector

用于体积流量表格化参数化的压降值向量。压降向量与 **Control member position vector, s** 参数构成独立轴，用于二维因变量 **Volumetric flow rate table, q(s,dp)** 参数。值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 或 `Tabulated data - Mass flow rate vs. control member position and pressure drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认） | *M*×*N* 矩阵

基于压降和控制构件位置的独立值的体积流量 *M*×*N* 矩阵。*M* 和 *N* 是对应向量的长度：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数。
- *N* 是 **Control member position vector, s** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`。

### **Mass flow rate table, mdot(s,dp)** — 质量流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `kg/s`（默认） | *M*×*N* 矩阵

基于压降和控制构件位置的独立值的质量流量。*M* 和 *N* 是对应向量的长度：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数。
- *N* 是 **Control member position vector, s** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. control member position and pressure drop`。

### **Reference inflow temperature** — 用于指定表格数据的入口温度 `293.15 K`（默认） | 以温度单位表示的正标量

相对于绝对零度的标称入口温度，用于指定表格数据。此参数用于根据仿真期间测得的温度调整质量流量。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. opening and pressure drop`。

### **Reference inflow pressure** — 用于指定表格数据的入口压力 `0.101325 MPa`（默认） | 以压力单位表示的正标量

相对于绝对零度的标称入口压力，用于指定表格数据。此参数用于根据仿真期间测得的压力调整质量流量。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. opening and pressure drop`。

### **Cross-sectional area at ports A and B** — 节流孔入口或出口处的面积 `0.01 m^2`（默认） | 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。此面积用于确定通过节流孔的质量流量的压力-流量方程。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- 将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。
- 将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### 故障

### **Orifice Area fault** — 对节流孔面积故障建模的选项 `Add fault`

对模块中的节流孔面积故障建模的选项。发生故障时，通常由开口参数化设置的阀门面积将基于 **Opening area when faulted** 参数中指定的值进行设置。要添加故障，请单击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`。

### **Opening area when faulted** — 故障时节流孔特性 `Closed`（默认） | `Open` | `Maintain at last value`

故障时节流孔面积。您可以选择让节流孔卡在完全关闭或完全打开位置，或在故障触发时卡在阀门面积处。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，然后单击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024b：使用 Simscape faults 接口对故障建模

Orifice (TL) 模块现在支持 Simscape™ faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2023b：对非单调的面积和体积流量参数建模

该模块不再要求 **Orifice area vector**、**Volumetric flow rate table, q(s,dp)** 或 **Mass flow rate table, mdot(s,dp)** 参数相对于 **Control member position vector, s** 参数单调递增或递减。

## 描述

热液体系统中的恒定面积或可变面积节流孔

Orifice (TL) 模块对通过局部限流处的流动进行建模，该限流处具有恒定或可变开口面积。对于可变节流孔，连接到端口 **S** 的控制构件设置开口位置。开口面积通过线性方式或查找表进行参数化。

该模块保持质量守恒，使得

m˙A+m˙B=ρvAAA+ρvBAB=0.

该质量平衡意味着，当面积减小时速度会增加，而当流动排入更大面积时速度会降低。根据伯努利原理，这种速度变化会导致节流孔中出现较低压力区域，并在膨胀区中出现较高压力。由此产生的压力升高称为*压力恢复*，它取决于节流孔的流量系数以及节流孔面积与端口面积之比。

### 恒定节流孔

对于恒定节流孔，节流孔面积 *A*orifice 在仿真过程中不会改变。

**使用 `Constant` 面积参数化**

该模块按以下公式计算质量流量

m˙=CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB≈CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB[(pA−pB)2+Δpcrit]1/4,

其中：

- *C*d 是 **Discharge coefficient** 参数。
- *A*orifice 是瞬时节流孔开口面积。
- *A*port 是 **Cross-sectional area at ports A and B** 参数。
- ρ¯ 是平均流体密度。

*PR*loss 和 *Δp*crit 对于恒定节流孔和可变节流孔的计算方式相同。

m˙ 的这种近似与 Local Resistance (TL) 模块相同。

**使用 `Tabulated data - Volumetric flow rate vs. pressure drop` 参数化**

体积流量由您可提供的压差 *Δp* 的表格值确定。如果您为体积流量向量和压降向量都只提供非负值，则该模块会外推表以包含负值。体积流量从此扩展表中插值得到。

如果 **Volumetric flow rate vector** 和 **Pressure drop vector** 参数同时包含负值和正值但没有 0，则该模块会向向量中插入原点，以确保当压降为 0 时阀门没有非零流量，这是非物理的。

### 可变节流孔

对于可变节流孔，当您将 **Opening orientation** 设置为 `Positive control member displacement opens orifice` 时，节流孔在 **S** 处信号为正时打开；而 `Negative control member displacement opens orifice` 方向则在 **S** 处信号为负时打开节流孔。在两种情况下，信号为正，并且节流孔开度由信号的幅值设置。

**使用 `Linear - Area vs. control member position` 参数化**

节流孔面积 *A*orifice 基于控制构件位置以及节流孔面积与最大控制构件位置之比：

Aorifice=(Amax−Aleak)ΔS(S−Smin)ε+Aleak,

其中：

- *S*min 是 **Control member position at closed orifice** 参数。
- *ΔS* 是 **Control member travel between closed and open orifice** 参数。
- *A*max 是 **Maximum orifice area** 参数。
- *A*leak 是 **Leakage area** 参数。
- *ε* 是 **Opening orientation** 参数。

体积流量由压力-流量方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中 *A* 是 **Cross-sectional area at ports A and B**。

当节流孔在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来维持仿真的数值鲁棒性。如果 **Smoothing factor** 参数非零，则该模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关更多信息，请参阅 Numerical Smoothing。

**使用 `Tabulated data - Area vs. control member position` 参数化**

当您使用 `Tabulated data - Area vs. control member position` 参数化时，节流孔面积 *A*orifice 由您可提供的开口面积和控制构件位置 *ΔS* 的表格值插值得到。与 `Linear - Area vs. control member position` 参数化一样，体积流量由压力-流量方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中 *A*orifice 为：

- *Amax*，即当端口 **S** 处的物理信号大于 **Control member position vector** 参数的最后一个元素时，**Orifice area vector** 参数的最后一个元素。
- *Aleak*，即当端口 **S** 处的物理信号小于 **Control member position vector** 参数的第一个元素时，**Orifice area vector** 参数的第一个元素。
- 如果计算出的面积在 **Control member position vector** 参数第一个和最后一个元素的界限之间，则为 **Orifice area vector** 参数的线性插值。

*Aorifice* 是端口 **S** 处接收到的控制构件位置的函数。该模块在数据点之间进行线性插值查询，并对表边界之外的点使用最近邻外推。

**使用 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 参数化**

`Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 参数化直接从用户提供的体积流量表插值体积流量，该表基于控制构件位置和节流孔上的压降。该模块在数据点之间进行线性插值查询，并相对于控制构件位置使用最近邻外推，相对于压降使用线性外推。

此数据可以包含负压降和负开口值。如果数据集中包含负压降，体积流量将改变方向。但是，对于负开口值，流量将保持不变。

如果 **Pressure drop vector, dp** 参数不包含 0，且 **Volumetric flow rate table, q(s,dp)** 参数不包含相应的 0 列，则该模块会插入它们，以确保当压降为 0 时阀门没有非零流量，这是非物理的。

**使用 `Tabulated data - Mass flow rate vs. control member position and pressure drop` 参数化**

`Tabulated data - Mass flow rate vs. control member position and pressure drop` — 根据控制构件位置和阀门上的压降直接计算质量流量。这三个变量之间的关系可以是非线性的，并由 **Control member position vector, s**、**Pressure drop vector, dp** 和 **Mass flow rate table, mdot(s,dp)** 模块参数中的表格数据给出：

m˙Tab=ρAvgρRefm˙(ΔS,Δp),

其中 m˙ 是质量流量的表格形式，是控制构件位置 *h* 以及节流孔上的压降 *Δp* 的函数。质量流量通过比值 *ρAvg*/*ρRef* 针对温度和压力进行调整，其中 *ρAvg* 是节流孔中的平均流体密度，*ρref* 是 **Reference inflow temperature** 和 **Reference inflow pressure** 参数值的参考密度。

### 压力损失

*压力损失*描述由于面积减小而导致的阀门压力降低。该模块计算压力损失项 *PR*loss 如下：

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport.

*压力恢复*描述由于面积增加而导致的阀门正压力变化。如果您不希望捕获此压力升高，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。

### 临界压力

临界压差 *Δp*crit 是与 **Critical Reynolds number** 参数 *Re*crit 相关联的压差，*Re*crit 是流体中层流和湍流之间的过渡点：

Δpcrit=πρ¯8Aorifice(νRecritCd)2.

### 能量平衡

该模块将节流孔视为绝热组件。流体与其周围壁之间不会发生热交换。流体从入口到出口的过程中，不对流体做功，也不由流体做功。基于这些假设，能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和必须始终等于零：

ϕA+ϕB=0,

其中 *ϕ* 定义为通过其中一个端口（**A** 或 **B**）*进入*节流孔的能量流率。

### 故障

当 **Orifice type** 参数为 `Variable` 时，该模块可以对故障建模。

要对故障建模，请在 **Faults** 部分中，单击您要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Introduction to Simscape Faults。

**Opening area when faulted** 参数有三个故障选项：

- `Closed` — 节流孔冻结在其最小值，具体取决于 **Orifice parameterization**：

  - 当 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **Leakage area**。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **Orifice area vector** 的第一个元素。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **Volumetric flow rate table, q(s,dp)** 的第一行。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **Mass flow rate table, mdot(s,dp)** 的第一行。
- `Open` — 节流孔冻结在其最大值，具体取决于 **Orifice parameterization**：

  - 当 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **Maximum orifice area**。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **Orifice area vector** 的最后一个元素。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **Volumetric flow rate table, q(s,dp)** 的最后一行。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **Mass flow rate table, mdot(s,dp)** 的最后一行。
- `Maintain at last value` — 触发发生时，节流孔卡在开口面积或体积流量处。
