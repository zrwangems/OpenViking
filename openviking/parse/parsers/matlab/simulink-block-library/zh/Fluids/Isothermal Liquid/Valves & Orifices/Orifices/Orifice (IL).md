---
type: simulink-block
title: 'Orifice (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Orifices'
documentation_page: 'orificeil'
documentation_source_path: 'ref/orificeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Orifice (IL)

## 端口

### 守恒端口

### **A** — 等温液体端口

节流孔的液体入口或出口点。

### **B** — 等温液体端口

节流孔的液体入口或出口点。

### 输入

### **S** — 控制构件位移物理信号

设置节流孔开度的控制构件位移。

## 参数

### 参数

### **Orifice type** — 节流孔类型 `Variable`（默认）| `Constant`

节流孔类型，由节流孔面积定义。当设置为
`Variable` 时，节流孔面积根据端口
**S** 接收的输入信号而变化。

### **Orifice parameterization** — 节流孔面积计算方法 `Orifice Area`（默认）| `Tabulated data - volumetric flow rate vs. pressure drop` | `Linear - area vs. control member position` | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

仿真过程中节流孔面积的计算方法。当
**Orifice type** 设置为
`Constant` 时，有两种参数化选项。

- `Orifice area`（默认）。指定的面积在仿真过程中不发生变化。
- `Tabulated data - Volumetric flow rate vs.
  pressure drop`。面积保持不变，
  但通过节流孔的体积流量可以变化。
  该值直接从
  **Volumetric flow rate vector** 和
  **Pressure drop vector**
  数据集插值得到。

当 **Orifice type** 设置为
`Variable` 时，有三种参数化选项。

- `Linear - Area vs. control member
  position`。面积由控制构件位置相对于
  全开或全闭节流孔的线性关系确定。位置由端口
  **S** 处变化的物理信号设置。
- `Tabulated data - Area vs. control member
  position`。开度面积根据端口
  **S** 接收的控制构件位置，从 **Control member position vector**
  和 **Orifice area vector** 插值得到。
- `Tabulated data - Volumetric flow rate vs.
  control member position and pressure drop`。
  体积流量根据端口 **S** 接收的控制构件位置
  以及端口 **A** 和
  **B** 之间的压降，直接从用户提供的
  **Control member position vector,
  s**、**Pressure drop vector,
  dp** 和 **Volumetric flow rate table,
  q(s,dp)** 参数插值得到。

### **Orifice area** — 节流孔开度面积 `1e-3 m^2`（默认）| 正标量

节流孔开度的横截面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Orifice
area`。

### **Pressure drop vector** — 用于表格参数化的压差值向量 `[-4, -3, -2, -1, -.5, 0, .5, 1, 2, 3, 4] MPa`（默认）| 1×*n* 向量

用于体积流量表格参数化的压差值向量。该向量中的值与
**Volumetric flow rate
vector** 参数中的值一一对应。压降向量值按升序列出。
体积流量直接从 **Volumetric flow rate vector**
插值得到，该向量取决于 **Pressure drop vector**
参数。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure drop`。

### **Volumetric flow rate vector** — 体积流量值向量 `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] .* 1e-3 m^3/s`（默认）| 1×*n* 向量

用于体积流量表格化参数化的体积流量值向量。此向量中的值与 **Pressure drop vector** 中的值一一对应。体积流量直接根据提供的 **Volumetric flow rate vector** 插值得到，该向量取决于 **Pressure drop vector** 参数。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure drop`。

### **Control member position at closed orifice** — 关闭孔口时的控制构件偏移 `0 m`（默认）| 标量

可变孔口完全关闭时的初始控制构件偏移。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`。

### **Control member travel between closed and open orifice** — 控制构件最大行程 `5e-3 m`（默认）| 正标量

控制构件在关闭孔口和打开孔口之间移动的最大距离。孔口在 **Control member position at closed orifice** 与 **Control member travel between closed and open orifice** 之和处完全打开，

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Maximum orifice area** — 最大孔口开口面积 `1e-4 m^2`（默认）| 正标量

仿真过程中经历的最大孔口面积。当使用 `Tabulated data - Area vs. control member position` 时，最大孔口面积是 **Orifice area vector** 的最后一个元素。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Leakage area** — 完全关闭位置时的孔口间隙面积 `1e-10 m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。此参数通过保持流量连续性来增强数值稳定性。

#### 依赖

要启用此参数，请将 **Orifice** type 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Control member position vector** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于孔口面积表格化参数化的控制构件位置向量。向量元素与 **Orifice area vector** 中的值一一对应。向量元素必须严格单调递增或递减。孔口开口面积根据 **Orifice area vector** 插值得到，该向量取决于 **Control member position vector** 参数。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Orifice area vector** — 孔口开口面积值向量 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2`（默认）| 1×*n* 向量

用于孔口面积表格化参数化的孔口面积值向量。此向量中的值与 **Control member position vector** 中的元素一一对应。如果向量递增，则此向量的第一个元素是孔口泄漏面积，最后一个元素是最大孔口面积。如果向量递减，则此向量的第一个元素是孔口最大孔口面积，最后一个元素是泄漏面积。孔口开口面积根据 **Orifice area vector** 插值得到，该向量取决于 **Control member position vector**。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Area vs. control member position`。

### **Cross-sectional area at ports A and B** — 节流口入口或出口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。该面积用于确定通过节流口的质量流量的压力-流量方程中。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice type** 设置为
  `Variable`，且
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 设置为
  `Constant`，且
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Opening orientation** — 打开节流口的构件运动方向 `Positive control member displacement opens orifice`（默认）| `Negative control member displacement opens orifice`

打开可变节流口的构件位移方向。正方向表示 **S** 处的正信号打开节流口。负方向表示 **S** 处的负信号打开节流口。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于修正理论流量中排放损失的修正系数。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice type** 设置为
  `Variable`，且
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 设置为
  `Constant`，且
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过节流口的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice type** 设置为
  `Variable`，且
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 设置为
  `Constant`，且
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当节流口处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `on`（默认）| `off`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。当您清除 **Pressure recovery** 复选框时，不会捕获此压力增加。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice type** 设置为
  `Variable`，且
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- **Orifice type** 设置为
  `Constant`，且
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Control member position vector, s** — 开度值向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的控制构件位置向量。控制构件位置向量与 **Pressure drop vector, dp** 参数共同构成二维因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。正位移对应于阀门打开。值按升序排列，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`。

### **Pressure drop vector, dp** — 压降值向量 `[.3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **Control member position vector, s** 参数共同构成二维因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认）| *M*×*N* 矩阵

基于压降和控制构件位置独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数量。
- *N* 是 **Control member position vector, s** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`。

### 故障

### **Orifice Area fault** — 用于对孔口面积故障建模的选项 `Add fault`

用于在模块中对孔口面积故障建模的选项。当故障发生时，通常由开度参数化设置的阀门面积将根据 **Opening area when faulted** 参数中指定的值进行设置。要添加故障，请点击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`。

### **Opening area when faulted** — 故障时的孔口特性 `Closed`（默认）| `Open` | `Maintain at last value`

故障时的孔口面积。您可以选择孔口卡死在完全关闭或完全打开位置，或者卡死在故障触发时的阀门面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Orifice (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2023b：对非单调面积和体积流量参数建模

该模块不再要求 **Orifice area vector** 和 **Volumetric flow rate table, q(s,dp)** 参数相对于 **Control member position vector, s** 参数单调递增或递减。

## 描述

等温液体系统中的定面积或变面积节流孔

Orifice (IL) 模块对通过具有恒定或可变开口面积的局部节流孔的流动进行建模。对于可变节流孔，连接到端口 **S** 的控制构件设定开口位置。开口面积可通过线性方式或查找表进行参数化。

对于根据中心滑阀位移进行开闭的节流孔，请参阅 Spool Orifice (IL)。

该模块保持质量守恒，使得

m˙A+m˙B=ρvAAA+ρvBAB=0。

该质量平衡意味着当面积减小时速度增加，而当流体排入较大面积时速度降低。根据伯努利原理，这种速度变化导致节流孔内出现低压区域，而在膨胀区出现较高压力。由此产生的压力升高称为*压力恢复*，取决于节流孔的流量系数以及节流孔面积与端口面积之比。

### 定节流孔

对于定节流孔，节流孔面积 *A*orifice 在仿真过程中不发生变化。

**使用 `Constant` 面积参数化**

该模块按如下方式计算质量流量

m˙=CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB≈CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB[(pA−pB)2+Δpcrit]1/4，

其中：

- *C*d 是 **Discharge coefficient**。
- *A*orifice 是瞬时节流孔开口面积。
- *A*port 是 **Cross-sectional 端口 A 和 B 处的面积**。
- ρ¯ 是平均流体密度。

*PR*loss 和 *Δp*crit 对于定节流孔和变节流孔的计算方式相同，并在下文“压力损失”和“临界压力”部分中定义。

该 m˙ 近似与 Local Restriction (IL) 模块相同。

**使用 `Tabulated data - Volumetric flow rate vs. pressure drop` 参数化**

体积流量由您提供的压差 *Δp* 的表格值确定。如果您仅为体积流量和压降向量提供非负值，则该模块会外推该表以包含负值。体积流量从该扩展表中插值得到。

如果 **Volumetric flow rate vector** 和 **Pressure drop vector** 参数同时包含负值和正值但不包含 0，则该模块会向这些向量中插入原点，以确保当压降为 0 时阀门没有非零流量，因为这是非物理的。

### Variable Orifices

对于可变节流口，将 **Opening orientation** 设置为
`Positive control member displacement opens orifice`
时，当 **S** 处的信号为正时打开节流口，而
`Negative control member displacement opens orifice`
方向则在 **S** 处的信号为负时打开节流口。
在这两种情况下，信号均为正，节流口开度由信号的幅值设定。

**使用 `Linear - Area vs. control member position`
参数化**

节流口面积 *A*orifice 基于控制构件位置以及节流口面积与控制构件最大位置之比：

Aorifice=(Amax−Aleak)ΔS(S−Smin)ε+Aleak,

其中：

- *S*min 是节流口完全关闭时的控制构件位置。
- *ΔS* 是 **Control member
  travel between closed and open orifice**。
- *A*max 是
  **Maximum orifice area**。
- *A*leak 是
  **Leakage area**。
- *ε* 是 **Opening
  orientation**。

当阀门在线性参数化中处于接近打开或
接近关闭的位置时，你可以通过调整 **Smoothing
factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor**
参数非零，模块会在
*Aleak* 和
*Amax* 之间平滑地饱和节流口面积。有关更多信息，
请参阅 Numerical Smoothing。

体积流量由压力-流量方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中 *A* 是 **Cross-sectional
端口 A 和 B 处的面积**。

**使用 `Tabulated data - Area vs. control member position`
参数化**

当你使用 `Tabulated data - Area vs. control member
position` 参数化时，节流口面积
*A*orifice 由开口面积和控制构件位置
*ΔS* 的表格值插值得到，这些值可由你提供。与
`Linear - Area vs. control member position`
参数化一样，体积流量由压力-流量方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中 *A*orifice 为：

- *A*max，即 **Orifice area vector** 的最后一个元素，
  如果开口大于指定的最大开口。
- *A*leak，即 **Orifice area vector** 的第一个元素，
  如果节流口开口小于最小开口。
- *A*orifice，如果
  计算得到的面积位于 **Orifice area
  vector** 的限值之间。

*A*open 是端口 **S** 处接收到的控制构件位置的函数。模块在数据点之间进行线性插值查询，并对超出表格边界的点使用最近邻外推。

**使用 `Tabulated data - Volumetric flow rate vs. control
member position and pressure drop` 参数化**

`Tabulated data - Volumetric flow rate vs. control member
position and pressure drop` 参数化直接从用户提供的体积流量表插值体积流量，
该表基于控制构件位置和节流口两端的压降。模块在数据点之间进行线性插值查询，并对超出表格边界的点使用线性外推。

该数据可以包含负压降和负开口值。如果
数据集中包含负压降，体积流量将改变方向。但是，对于负
开口值，流量将保持不变。

如果 **Pressure drop vector, dp** 参数不
包含 0，并且 **Volumetric flow rate table, q(s,dp)**
参数不包含相应的 0 列，模块会插入它们，
以确保阀门在压降为 0 时没有非零流量，
这是非物理的。

### Pressure Loss

*压力损失*描述由于面积减小而导致阀门中的压力降低。压力损失项 *PR*loss 计算如下：

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport。

*压力恢复*描述由于面积增大而导致阀门中的正压力变化。如果您不希望捕获此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。

### Critical Pressure

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 相关的压差，该雷诺数是流体中层流与湍流之间过渡的点：

Δpcrit=πρ¯8Aorifice(νRecritCd)2。

### 故障

当 **Orifice type** 参数为 `Variable` 时，该模块可以对故障进行建模。

要对故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Opening area when faulted** 参数有三个故障选项：

- `Closed` — 节流孔冻结在其最小值，具体取决于 **Orifice parameterization**：

  - 当 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **Leakage area**。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **Orifice area vector** 的第一个元素。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **Volumetric flow rate table, q(s,dp)** 的第一行。
- `Open` — 节流孔冻结在其最大值，具体取决于 **Orifice parameterization**：

  - 当 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **Maximum orifice area**。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **Orifice area vector** 的最后一个元素。
  - 当 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **Volumetric flow rate table, q(s,dp)** 的最后一行。
- `Maintain at last value` — 节流孔在触发发生时卡在开口面积或体积流量处。
