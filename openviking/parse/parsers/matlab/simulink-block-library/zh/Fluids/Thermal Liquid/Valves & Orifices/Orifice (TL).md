---
type: simulink-block
title: 'Orifice (TL)'
family: 'hydro'
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

### **S** — 控制构件位移，m 物理信号

阀控制构件的瞬时位移。
### 守恒

### **A** — 流动通道热液体

与开口关联的热液体守恒端口，流体可通过该开口进入或离开阀。

### **B** — 流动通道热液体

与开口关联的热液体守恒端口，流体可通过该开口进入或离开阀。

## 参数

### 参数

### **Orifice type** — 孔口类型 `Variable`（默认）| `Constant`

孔口类型，由孔口面积定义。当设置为
`Variable` 时，孔口面积根据端口
**S** 接收的输入信号而变化。

- `Orifice area`—指定的面积
  在仿真过程中不发生变化。
- `Tabulated data - Volumetric flow rate vs.
  pressure drop`—面积保持不变，
  但通过孔口的体积流量可以变化。
  该值直接从
  **Volumetric flow rate vector** 和
  **Pressure drop vector**
  数据集插值得到。
- `Tabulated data - Mass flow rate vs. pressure
  drop`—面积保持不变，但
  通过孔口的体积流量可以变化。该
  值直接从 **Mass flow
  rate vector** 和 **Pressure drop
  vector** 数据集插值得到。

当将 **Orifice type** 设置为
`Variable` 时，有四个选项。

- `Linear - Area vs. control member
  position`。面积由与控制构件位置相对于
  孔口全开或全关的线性关系确定。位置由
  端口 **S** 处变化的物理信号
  设置。
- `Tabulated data - Area vs. control member
  position`。开口面积根据端口
  **S** 接收的控制构件位置，从 **Control member position vector**
  和 **Orifice area vector** 插值得到。
- `Tabulated data - Volumetric flow rate vs.
  control member position and pressure drop`。
  体积流量根据端口 **S** 接收的控制
  构件位置以及端口 **A** 和
  **B** 之间的压降，直接从用户
  提供的 **Control member position vector,
  s**、**Pressure drop vector,
  dp** 和 **Volumetric flow rate table,
  q(s,dp)** 参数插值得到。
- `Tabulated data - Mass flow rate vs. control
  member position and pressure drop`。质
  量流量根据端口 **S** 接收的控制
  构件位置以及端口 **A** 和
  **B** 之间的压降，直接从用户
  提供的 **Control member position vector,
  s**、**Pressure drop vector,
  dp** 和 **Mass flow rate table,
  mdot(s,dp)** 参数插值得到。

### **Orifice parameterization** — 恒定孔口参数化 `Orifice area`（默认）| `Tabulated data - Volumetric flow rate vs. pressure drop` | `Tabulated data - Mass flow rate vs. pressure drop`

用于对孔口开口特性进行建模的方法。
默认设置规定孔口开口面积与孔口开度之间为线性关系。
替代设置允许以表格形式指定一般的非线性关系，
一种情况是开口面积与孔口开度之间的关系，另一种
情况是质量流量与孔口开度以及端口之间
压降之间的关系。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`。

### **Orifice parameterization** — 可变孔口参数化 `Linear - Area vs. control member position`（默认）| `Tabulated data - Area vs. control member position` | `表格数据 - 体积流量与控制构件位置和 pressure drop` | `表格数据 - 质量流量与控制构件位置和压力 drop`

当将 **Orifice type** 设置为
`Variable` 时，有四个选项。

- `Linear - Area vs. control member
  position`。面积由与控制构件位置相对于
  孔口全开或全关的线性关系确定。位置由
  端口 **S** 处变化的物理信号
  设置。
- `Tabulated data - Area vs. control member
  position`。开口面积根据端口
  **S** 接收的控制构件位置，从 **Control member position vector**
  和 **Orifice area vector** 插值得到。
- `Tabulated data - Volumetric flow rate vs.
  control member position and pressure drop`。
  体积流量根据端口 **S** 接收的控制
  构件位置以及端口 **A** 和
  **B** 之间的压降，直接从用户
  提供的 **Control member position vector,
  s**、**Pressure drop vector,
  dp** 和 **Volumetric flow rate table,
  q(s,dp)** 参数插值得到。
- `Tabulated data - Mass flow rate vs. control
  member position and pressure drop`。质
  量流量根据端口 **S** 接收的控制
  构件位置以及端口 **A** 和
  **B** 之间的压降，直接从用户
  提供的 **Control member position vector,
  s**、**Pressure drop vector,
  dp** 和 **Mass flow rate table,
  mdot(s,dp)** 参数插值得到。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`。

### **Orifice area** — 孔口开口面积 `1e-3` `m^2`（默认）| 正标量

孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Orifice
area`。

### **Pressure drop vector** — 用于表格参数化的压差值向量 `[-4, -3, -2, -1, -.5, 0, .5, 1, 2, 3, 4] MPa`（默认）| 1×*n* 向量

用于体积流量表格参数化的压差值
向量。此向量中的值与 **Volumetric flow rate
vector** 参数中的值一一对应。压降向量值
按升序列出。体积流量直接从
**Volumetric flow rate vector**
参数插值得到，该参数取决于 **Pressure drop
vector** 参数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure drop`。

### **Volumetric flow rate vector** — 体积流量值向量 `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] .* 1e-3 m^3/s`（默认）| 1×*n* 向量

用于体积流量表格参数化的体积流量值
向量。此向量中的值与 **Pressure drop
vector** 参数中的值一一对应。体积流量
直接从提供的 **Volumetric flow rate
vector** 参数插值得到，该参数取决于 **Pressure
drop vector** 参数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure drop`。

### **Mass flow rate vector** — 质量流量值向量 `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] kg/s`（默认）| 向量 | 1×*n* 向量

用于体积流量表格参数化的质量流量值
向量。此向量中的值与
**Pressure drop vector** 参数中的值一一对应。
质量流量直接从提供的 **Mass
flow rate vector** 参数插值得到，该参数取决于
**Pressure drop vector** 参数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Mass flow rate vs. pressure drop`。

### **Control member position at closed orifice** — 控制构件偏移 `0 m`（默认）| 标量

可变孔口完全关闭时的初始控制构件偏移。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear – Area vs.
control member position`。

### **Control member travel between closed and open orifice** — 节流构件在关闭和打开节流孔之间的最大行程 `5e-3 m`（默认）| 正标量

节流构件在关闭和打开节流孔之间移动的最大距离。当节流构件位置达到 **Control
member position at closed orifice** 和 **Control
member travel between closed and open orifice**
参数之和时，节流孔完全打开。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Opening orientation** — 打开节流孔的构件移动方向 `Positive control member displacement opens orifice`（默认）| `Negative control member displacement opens orifice`

打开可变节流孔的构件位移方向。正方向表示
**S** 处的正信号打开节流孔。负方向
表示 **S** 处的负信号打开节流孔。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

仿真过程中经历的最大节流孔面积。当使用
`Tabulated data - Area vs. control member
position` 时，最大节流孔面积为 **Orifice area vector** 参数的最后一个元素。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Leakage area** — 完全关闭位置时的节流孔间隙面积 `1e-10 m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。
此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice** type 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Control member position vector** — 节流构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于节流孔面积表格化参数化的节流构件位置向量。向量元素与
**Orifice area vector** 参数中的值一一对应。
向量元素必须严格单调递增或递减。
节流孔开口面积从 **Orifice area
vector** 插值得到，该向量取决于 **Control member
position vector** 参数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Area vs. control member position`。

### **Orifice area vector** — 节流孔开口面积值向量 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2`（默认）| 1×*n* 向量

用于节流孔面积表格化参数化的节流孔面积值向量。此向量中的值与
**Control member position vector**
参数中的元素一一对应。如果向量递增，则此向量的第一个元素为节流孔泄漏面积，最后一个元素为最大节流孔
面积。如果向量递减，则此向量的第一个元素为节流孔最大节流孔面积，最后一个元素为泄漏
面积。节流孔开口面积从
**Orifice area vector** 参数插值得到，该参数取决于
**Control member position vector**
参数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Area vs. control member position`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正因子。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Orifice type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 为
  `Constant`，且
  **Orifice parameterization** 为
  `Orifice area`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过节流孔的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Orifice type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 为
  `Constant`，且
  **Orifice parameterization** 为
  `Orifice area`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当节流孔处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。
将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Pressure recovery** — 是否考虑面积扩大处的压力增加 `on`（默认）| `off`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。当您
清除 **Pressure recovery** 复选框时，不会捕获此压力增加。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Orifice type** 为
  `Variable`，且
  **Orifice parameterization** 为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 为
  `Constant`，且
  **Orifice parameterization** 为
  `Orifice area`。

### **Control member position vector, s** — 开口值向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的节流构件位置向量。节流构件位置向量与
**Pressure drop vector, dp** 参数构成独立轴，用于二维因变量
**Volumetric flow rate table, q(s,dp)**
参数。正位移对应于阀门打开。这些值按升序列出，且第一个元素必须为 0。
表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop` 或 `Tabulated data - Mass flow
rate vs. control member position and pressure
drop`。

### **Pressure drop vector, dp** — 压降值向量 `[.3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。
压降向量与
**Control member position vector, s** 参数构成独立轴，用于
二维因变量 **Volumetric flow rate table,
q(s,dp)** 参数。这些值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop`。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `表格数据 - 体积流量与控制构件位置和 pressure drop` 或 `表格数据 - 质量流量与控制构件位置和压力 drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认）| *M*×*N* 矩阵

基于压降和控制构件位置独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数量。
- *N* 是 **Control member position vector, s** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `表格数据 - 体积流量与控制构件位置和 pressure drop`。

### **Mass flow rate table, mdot(s,dp)** — 质量流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `kg/s`（默认）| *M*×*N* 矩阵

基于压降和控制构件位置独立值的质量流量。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数量。
- *N* 是 **Control member position vector, s** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `表格数据 - 质量流量与控制构件位置和压力 drop`。

### **Reference inflow temperature** — 用于指定表格数据的入口温度 `293.15 K`（默认）| 以温度单位为单位的正标量

以绝对零度为参考的标称入口温度，用于指定表格数据。此参数用于根据仿真期间测量的温度调整质量流量。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. opening and pressure drop`。

### **Reference inflow pressure** — 用于指定表格数据的入口压力 `0.101325 MPa`（默认）| 以压力单位为单位的正标量

以绝对零度为参考的标称入口压力，用于指定表格数据。此参数用于根据仿真期间测量的压力调整质量流量。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. opening and pressure drop`。

### **Cross-sectional area at ports A and B** — 孔口入口或出口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。该面积用于确定通过孔口质量流量的压力-流量方程中。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Orifice type** 为 `Variable`，且 **Orifice parameterization** 为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。
- **Orifice type** 为 `Constant`，且 **Orifice parameterization** 为 `Orifice area`。

### 故障

### **Orifice Area fault** — 用于对孔口面积故障建模的选项 `Add fault`

用于在模块中对孔口面积故障建模的选项。发生故障时，通常由开度参数化设置的阀面积将根据 **Opening area when faulted** 参数中指定的值进行设置。要添加故障，请点击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`。

### **Opening area when faulted** — 故障时的孔口特性 `Closed`（默认）| `Open` | `Maintain at last value`

故障时的孔口面积。您可以选择孔口卡在全关或全开位置，或者卡在故障触发时的阀面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，然后点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

Orifice (TL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2023b：对非单调面积和体积流量参数建模

该模块不再要求 **Orifice area vector**、**Volumetric flow rate table, q(s,dp)** 或 **Mass flow rate table, mdot(s,dp)** 参数相对于 **Control member position vector, s** 参数单调递增或递减。

## 描述

热液体系统中的恒定面积或可变面积孔口

Orifice (TL) 模块对通过具有恒定或可变开口面积的局部限流装置的流动进行建模。对于可变孔口，连接到端口 **S** 的控制构件设置开度位置。开口面积通过线性方式或查找表进行参数化。

该模块守恒质量，使得

m˙A+m˙B=ρvAAA+ρvBAB=0。

该质量平衡意味着当面积减小时速度增加，而当流体排入较大面积时速度减小。根据伯努利原理，这种速度变化导致孔口内出现低压区域，而在膨胀区出现较高压力。由此产生的压力升高称为*压力恢复*，取决于孔口的流量系数以及孔口面积与端口面积之比。

### 恒定孔口

对于恒定孔口，孔口面积 *A*orifice 在仿真过程中不发生变化。

**使用 `Constant` 面积参数化**

该模块按如下方式计算质量流量

m˙=CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB≈CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB[(pA−pB)2+Δpcrit]1/4，

其中：

- *C*d 是 **Discharge coefficient** 参数。
- *A*orifice 是瞬时孔口开口面积。
- *A*port 是 **Cross-sectional area at ports A and B** 参数。
- ρ¯ 是平均流体密度。

*PR*loss 和 *Δp*crit 对于恒定孔口和可变孔口的计算方式相同。

该 m˙ 近似与 Local Resistance (TL) 模块相同。

**使用 `Tabulated data - Volumetric flow rate vs. pressure drop` 参数化**

体积流量由压差 *Δp* 的表格值确定，您可以提供这些值。如果您仅为体积流量和压降向量提供非负值，则该模块会外推表格以包含负值。体积流量从此扩展表中插值得到。

如果 **Volumetric flow rate vector** 和 **Pressure drop vector** 参数同时包含负值和正值但不包含 0，则该模块会在向量中插入原点，以确保当压降为 0 时阀不具有非零流量，这是非物理的。

### Variable Orifices

对于可变节流口，当您将 **Opening orientation** 设置为
`Positive control member displacement opens orifice`
时，节流口在 **S** 处的信号为正时打开，而
`Negative control member displacement opens orifice`
方向则在 **S** 处的信号为负时打开节流口。
在两种情况下，信号均为正，节流口开度由信号的幅值设定。

**使用 `Linear - Area vs. control member
position` 参数化**

节流口面积 *A*orifice 基于控制构件位置以及节流口面积与控制构件最大位置的比值：

Aorifice=(Amax−Aleak)ΔS(S−Smin)ε+Aleak，

其中：

- *S*min 是
  **Control member position at closed orifice**
  参数。
- *ΔS* 是 **Control member travel
  between closed and open orifice** 参数。
- *A*max 是
  **Maximum orifice area** 参数。
- *A*leak 是
  **Leakage area** 参数。
- *ε* 是 **Opening
  orientation** 参数。

体积流量由压力-流量方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4，

其中 *A* 是 **Cross-sectional
端口 A 和 B 处的面积**。

当节流口在线性参数化中处于接近打开或
接近关闭位置时，您可以通过调整 **Smoothing
factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor**
参数非零，该模块会在
*Aleak* 和
*Amax* 之间平滑地饱和开度面积。有关更多信息，
请参阅 Numerical Smoothing。

**使用 `Tabulated data - Area vs. control member
position` 参数化**

当您使用 `Tabulated data - Area vs. control member
position` 参数化时，节流口面积
*A*orifice 由开度面积和控制构件位置
*ΔS* 的表格值插值得到，这些值可由您提供。与
`Linear - Area vs. control member position`
参数化一样，体积流量由压力-流量
方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4，

其中 *A*orifice 为：

- *Amax*，即 **Orifice area vector** 参数的最后一个元素，
  如果端口 **S** 处的物理信号大于
  **Control member position
  vector** 参数的最后一个元素。
- *Aleak*，即 **Orifice area vector** 参数的第一个元素，
  如果端口 **S** 处的物理信号小于
  **Control member position
  vector** 参数的第一个元素。
- 如果计算得到的面积介于 **Control
  member position vector** 参数的第一个和最后一个元素限值之间，则为 **Orifice area
  vector** 参数的线性插值值。

*Aorifice* 是端口 **S** 处接收到的控制构件位置的函数。该
模块在数据点之间进行线性插值查询，并对超出表格边界的点使用最近
外推。

**使用 `Tabulated data - Volumetric flow rate vs. control
member position and pressure drop` 参数化**

`表格数据 - 体积流量与控制构件位置和
pressure drop` 参数化直接从用户提供的体积流量表插值体积
流量，该表基于控制构件位置和节流口上的压降。该
模块在数据点之间进行线性插值查询，并针对控制构件位置使用
最近
外推，针对压降使用线性外推。

该数据可以包含负压降和负开度值。如果
数据集中包含负压降，体积流量将改变方向。但是，对于负
开度值，流量将保持不变。

如果 **Pressure drop vector, dp** 参数不包含 0，并且
**Volumetric flow rate table, q(s,dp)** 参数不
包含相应的 0 列，则该模块会插入它们，以确保
当压降为 0 时阀门没有非零流量，因为这是
非物理的。

**使用 `Tabulated data - Mass flow rate vs. control member
position and pressure drop` 参数化**

`表格数据 - 质量流量与控制构件位置和压力
drop` — 直接从控制构件位置和阀门上的压降计算质量流量。这三个变量之间的关系
可以是非线性的，并且由 **Control member position vector, s**、**Pressure
drop vector, dp** 和 **Mass flow rate table,
mdot(s,dp)** 模块参数中的表格数据给出：

m˙Tab=ρAvgρRefm˙(ΔS,Δp)，

其中 m˙ 是质量流量的表格形式，是控制构件位置 *h* 和节流口上的压降 *Δp* 的函数。质量流量通过比值 *ρAvg*/*ρRef* 根据
温度和压力进行调整，其中 *ρAvg* 是
节流口中的平均流体密度，
*ρref* 是 **Reference inflow temperature** 和
**Reference inflow pressure** 参数值的参考密度。

### Pressure Loss

*Pressure loss* 描述由于
面积减小而导致的阀门压力降低。该模块计算压力损失项
*PR*loss 如下：

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport。

*Pressure recovery* 描述由于
面积增加而导致的阀门正压力变化。如果您不希望捕获这种压力增加，
请清除 **Pressure recovery** 复选框。在这种情况下，
*PR*loss 为 1。

### Critical Pressure

临界压差 *Δp*crit 是与 **Critical Reynolds
number** 参数 *Re*crit 相关的
压差，该参数是
流体中层流和湍流之间的转变点：

Δpcrit=πρ¯8Aorifice(νRecritCd)2。

### Energy Balance

该模块将节流口视为绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口
穿过时，不对流体做功，也不由流体做功。基于这些假设，能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口
能量流之和必须始终等于零：

ϕA+ϕB=0，

其中 *ϕ* 定义为通过其中一个端口（**A** 或 **B**）*进入*节流口的能量流率。

### 故障

当 **Orifice type** 参数为 `Variable` 时，该模块可以对故障建模。

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Opening area when faulted** 参数有三个故障选项：

- `Closed` — 节流孔冻结在其最小值，具体取决于 **Orifice parameterization**：

  - 当 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **Leakage area**。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **Orifice area vector** 的第一个元素。
  - 当 **Orifice parameterization** 设置为 `表格数据 - 体积流量与控制构件位置和 pressure drop` 时，节流孔冻结在 **Volumetric flow rate table, q(s,dp)** 的第一行。
  - 当 **Orifice parameterization** 设置为 `表格数据 - 质量流量与控制构件位置和压力 drop` 时，节流孔冻结在 **Mass flow rate table, mdot(s,dp)** 的第一行。
- `Open` — 节流孔冻结在其最大值，具体取决于 **Orifice parameterization**：

  - 当 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **Maximum orifice area**。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **Orifice area vector** 的最后一个元素。
  - 当 **Orifice parameterization** 设置为 `表格数据 - 体积流量与控制构件位置和 pressure drop` 时，节流孔冻结在 **Volumetric flow rate table, q(s,dp)** 的最后一行。
  - 当 **Orifice parameterization** 设置为 `表格数据 - 质量流量与控制构件位置和压力 drop` 时，节流孔冻结在 **Mass flow rate table, mdot(s,dp)** 的最后一行。
- `Maintain at last value` — 节流孔在触发发生时卡在开口面积或体积流量处。
