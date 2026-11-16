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

### 守恒

### **A** — 液体端口 isothermal liquid

孔口的液体入口或出口点。

### **B** — 液体端口 isothermal liquid

孔口的液体入口或出口点。
### 输入

### **S** — 控制构件位移物理信号

设定孔口开度的控制构件位移。

## 参数

### 参数

### **Orifice type** — 孔口类型 `Variable`（默认）| `Constant`

孔口类型，由孔口面积定义。当设置为
`Variable` 时，孔口面积根据端口
**S** 接收的输入信号而变化。

### **Orifice parameterization** — 计算孔口面积的方法 `Orifice Area`（默认）| `Tabulated data - volumetric flow rate vs. pressure drop` | `Linear - area vs. control member position` | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

在仿真过程中计算孔口面积的方法。当
**Orifice type** 设置为
`Constant` 时，有两个参数化选项。

- `Orifice area`（默认）。指定的面积在仿真过程中不变。
- `Tabulated data - Volumetric flow rate vs. pressure drop`。面积保持不变，
  但通过孔口的体积流量可以变化。
  该值直接从
  **Volumetric flow rate vector** 和
  **Pressure drop vector**
  数据集插值得到。

当 **Orifice type** 设置为
`Variable` 时，有三个
参数化选项。

- `Linear - Area vs. control member position`。面积由相对于
  完全打开或完全关闭孔口的控制构件位置的线性关系确定。该位置由
  端口 **S** 处的变化物理信号设定。
- `Tabulated data - Area vs. control member position`。开口面积根据
  端口 **S** 接收的控制构件位置，从
  **Control member position vector**
  和 **Orifice area vector** 插值得到。
- `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`。
  体积流量根据端口 **S** 接收的控制构件位置以及
  端口 **A** 和 **B** 两端的压降，直接从
  用户提供的 **Control member position vector, s**、
  **Pressure drop vector, dp** 和
  **Volumetric flow rate table, q(s,dp)** 参数插值得到。

### **Orifice area** — 孔口开口的面积 `1e-3 m^2`（默认）| 正标量

孔口开口的横截面积。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Orifice
area`。

### **Pressure drop vector** — 表格参数化的压差值向量 `[-4, -3, -2, -1, -.5, 0, .5, 1, 2, 3, 4] MPa`（默认）| 1×*n* 向量

用于体积流量表格参数化的压差值向量。此向量中的值
与 **Volumetric flow rate vector**
参数中的值一一对应。压降向量值
按升序列出。体积流量直接从
**Volumetric flow rate vector** 插值得到，
而该向量取决于 **Pressure drop vector**
参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure drop`。

### **Volumetric flow rate vector** — 体积流量值向量 `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] .* 1e-3 m^3/s`（默认）| 1×*n* 向量

用于体积流量表格参数化的体积流量值向量。此向量中的值与
**Pressure drop vector** 中的值一一对应。体积流量
直接从提供的 **Volumetric flow
rate vector** 插值得到，而该向量取决于 **Pressure drop
vector** 参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure drop`。

### **Control member position at closed orifice** — 控制构件偏移 `0 m`（默认）| 标量

可变孔口完全关闭时的初始控制构件偏移。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`。

### **Control member travel between closed and open orifice** — 控制构件最大行程 `5e-3 m`（默认）| 正标量

控制构件在关闭与打开孔口之间行进的最大距离。孔口在 **Control
member position at closed orifice** 与 **Control
member travel between closed and open orifice** 之和处完全开启，

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Maximum orifice area** — 最大孔口开口面积 `1e-4 m^2`（默认）| 正标量

仿真过程中经历的最大孔口面积。使用
`Tabulated data - Area vs. control member
position` 时，最大孔口面积是
**Orifice area vector** 的最后一个元素。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Leakage area** — 完全关闭位置时的孔口间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积
都保持为指定的泄漏面积。
此参数通过保持流动连续性来帮助提高数值稳定性。

#### 依赖项

要启用此参数，请将 **Orifice** type 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Linear - Area vs.
control member position`。

### **Control member position vector** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于孔口面积表格参数化的控制构件位置向量。
向量元素与
**Orifice area vector** 中的值一一对应。向量元素必须
严格单调递增或递减。孔口
开口面积从 **Orifice area
vector** 插值得到，而该向量取决于 **Control member
position vector** 参数。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Area vs. control member position`。

### **Orifice area vector** — 孔口开口面积值向量 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2`（默认）| 1×*n* 向量

用于孔口面积表格参数化的孔口面积值向量。此向量中的
值与 **Control member position vector** 中的元素一一对应。如果向量
递增，则此向量的第一个元素是孔口泄漏
面积，最后一个元素是最大孔口面积。如果向量
递减，则此向量的第一个元素是孔口最大
孔口面积，最后一个元素是泄漏面积。孔口
开口面积从 **Orifice area
vector** 插值得到，而该向量取决于 **Control member
position vector**。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Area vs. control member position`。

### **Cross-sectional area at ports A and B** — 孔口入口或出口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口
**A** 和 **B** 处的横截面积。该面积
用于确定通过孔口质量流量的压力-流量方程中。

#### 依赖项

要启用此参数，请执行以下任一设置：

- 将 **Orifice type** 设置为
  `Variable`，并将
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- 将 **Orifice type** 设置为
  `Constant`，并将
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Opening orientation** — 开启孔口的构件移动方向 `Positive control member displacement opens orifice`（默认）| `Negative control member displacement opens orifice`

开启可变孔口的构件位移方向。正方向表示
**S** 处的正信号开启孔口。负方向
表示 **S** 处的负信号开启孔口。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于考虑理论流动中排放损失的修正因子。

#### 依赖项

要启用此参数，请执行以下任一设置：

- 将 **Orifice type** 设置为
  `Variable`，并将
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- 将 **Orifice type** 设置为
  `Constant`，并将
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

#### 依赖项

要启用此参数，请执行以下任一设置：

- 将 **Orifice type** 设置为
  `Variable`，并将
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- 将 **Orifice type** 设置为
  `Constant`，并将
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入一层
渐变变化。将此值设置为大于零且小于一的值，可提高
这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `on`（默认）| `off`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。清除
**Pressure recovery** 复选框时，不会捕获此
压力增加。

#### 依赖项

要启用此参数，请执行以下任一设置：

- 将 **Orifice type** 设置为
  `Variable`，并将
  **Orifice parameterization** 设置为
  `Linear - Area vs. control member
  position` 或 `Tabulated
  data - Area vs. control member
  position`。
- 将 **Orifice type** 设置为
  `Constant`，并将
  **Orifice parameterization** 设置为
  `Orifice area`。

### **Control member position vector, s** — 开口值向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于体积流量表格参数化的控制构件位置向量。控制构件位置向量与
**Pressure drop vector, dp** 参数一起构成二维因变量
**Volumetric flow rate table, q(s,dp)**
参数的独立轴。正位移对应于阀开启。这些值
按升序列出，且第一个元素必须为 0。
表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop`。

### **Pressure drop vector, dp** — 压降值向量 `[.3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格参数化的压降值向量。
压降向量与 **Control member position vector, s** 参数一起构成
二维因变量 **Volumetric flow rate table,
q(s,dp)** 参数的独立轴。这些值按升序
列出，且必须大于 0。表数据点之间采用线性
插值。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认）| *M*×*N* 矩阵

基于压降和控制构件位置独立值的
*M*×*N* 体积流量矩阵。*M* 和 *N* 是
相应向量的大小：

- *M* 是
  **Pressure drop vector, dp**
  参数中的元素数量。
- *N* 是
  **Control member position vector, s**
  参数中的元素数量。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop`。

### 故障

### **Orifice Area fault** — 对孔口面积故障建模的选项 `Add fault`

对模块中的孔口面积故障建模的选项。发生故障时，通常由开口参数化设置的阀面积
将基于 **Opening area when faulted**
参数中指定的值设置。要添加故障，请点击 **Add fault**
超链接。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`。

### **Opening area when faulted** — 发生故障时的孔口特性 `Closed`（默认）| `Open` | `Maintain at last value`

发生故障时的孔口面积。您可以选择让孔口卡在
完全关闭或完全打开位置，或在故障
触发时卡在阀面积处。

#### 依赖项

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并点击 **Add
fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape faults 接口对故障建模

Orifice (IL) 模块现在支持 Simscape™ faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2023b：对非单调面积和体积流量参数建模

该模块不再要求 **Orifice area vector** 和
**Volumetric flow rate table, q(s,dp)** 参数
相对于 **Control member
position vector, s** 参数单调增加或减少。

## 描述

等温液体系统中的恒定面积或可变面积孔口

Orifice (IL) 模块对通过具有恒定或可变开口面积的局部
限制的流动进行建模。对于可变孔口，连接到端口 **S** 的控制
构件设定开启位置。开口
面积通过线性方式或查找表进行参数化。

对于根据中心滑阀位移开启和关闭的孔口，请参阅
Spool Orifice (IL)。

该模块质量守恒，因此

m˙A+m˙B=ρvAAA+ρvBAB=0.

此质量平衡意味着，当面积减小时速度增加，当流动排入较大面积时
速度减小。根据伯努利原理，这种速度变化导致孔口内出现
较低压力区域，并在膨胀区出现较高压力。由此产生的
压力增加称为 *压力恢复*，它取决于孔口的流量系数以及
孔口面积与端口面积之比。

### 恒定节流孔

对于恒定节流孔，节流孔面积 *A*orifice 在仿真过程中不会改变。

**使用 `Constant` 面积参数化**

该模块计算质量流量如下

m˙=CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB≈CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB[(pA−pB)2+Δpcrit]1/4,

其中：

- *C*d 是
  **流量系数**。
- *A*orifice 是
  瞬时节流孔开启面积。
- *A*port 是
  **端口 A 和 B 处的横截面积**。
- ρ¯ 是平均流体密度。

*PR*loss 和
*Δp*crit 对恒定节流孔和可变节流孔按相同方式计算，并在下面的压力损失和临界压力章节中定义。

m˙ 的这种近似与 Local Restriction (IL) 模块相同。

**使用 `Tabulated data - Volumetric flow rate vs. pressure drop` 参数化**

体积流量根据您可提供的压差 *Δp* 的表格值确定。如果您为体积流量向量和压降向量都只提供非负值，该模块会外推表以包含负值。体积流量从该扩展表插值得到。

如果 **体积流量向量** 和 **压降向量** 参数同时包含负值和正值但没有 0，该模块会向向量中插入原点，以确保当压降为 0 时阀不具有非零流量，这是非物理的。

### 可变节流孔

对于可变节流孔，将 **开启方向** 设置为 `Positive control member displacement opens orifice` 时，当 **S** 处信号为正时节流孔开启；而 `Negative control member displacement opens orifice` 方向则在 **S** 处信号为负时节流孔开启。在两种情况下，信号均为正，且节流孔开度由信号幅值设定。

**使用 `Linear - Area vs. control member position` 参数化**

节流孔面积 *A*orifice 基于控制构件位置以及节流孔面积与最大控制构件位置之比：

Aorifice=(Amax−Aleak)ΔS(S−Smin)ε+Aleak,

其中：

- *S*min 是节流孔完全关闭时的控制构件位置。
- *ΔS* 是 **关闭和打开节流孔之间的控制构件行程**。
- *A*max 是 **最大节流孔面积**。
- *A*leak 是 **泄漏面积**。
- *ε* 是 **开启方向**。

当在线性参数化中阀处于接近打开或接近关闭位置时，您可以通过调整 **平滑因子** 参数来保持仿真的数值稳健性。如果 **平滑因子** 参数非零，该模块会在 *Aleak* 和 *Amax* 之间平滑地饱和节流孔面积。有关详细信息，请参阅 Numerical Smoothing。

体积流量由压力-流量方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中 *A* 是 **端口 A 和 B 处的横截面积**。

**使用 `Tabulated data - Area vs. control member position` 参数化**

当您使用 `Tabulated data - Area vs. control member position` 参数化时，节流孔面积 *A*orifice 从您可提供的开启面积和控制构件位置 *ΔS* 的表格值插值得到。与 `Linear - Area vs. control member position` 参数化一样，体积流量由压力-流量方程确定：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中 *A*orifice 为：

- *A*max，即 **节流孔面积向量** 的最后一个元素，如果开度大于指定的最大开度。
- *A*leak，即 **节流孔面积向量** 的第一个元素，如果节流孔开度小于最小开度。
- *A*orifice，如果计算面积处于 **节流孔面积向量** 的限值之间。

*A*open 是端口 **S** 处接收到的控制构件位置的函数。该模块使用线性插值在数据点之间查询，并对超出表边界的点使用最近邻外推。

**使用 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 参数化**

`Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 参数化直接从用户提供的体积流量表插值体积流量，该表基于控制构件位置和节流孔上的压降。该模块使用线性插值在数据点之间查询，并对超出表边界的点使用线性外推。

该数据可以包含负压降和负开度值。如果数据集中包含负压降，体积流量将改变方向。但是，对于负开度值，流量将保持不变。

如果 **压降向量, dp** 参数不包含 0，且 **体积流量表, q(s,dp)** 参数不包含相应的 0 列，该模块会插入它们，以确保当压降为 0 时阀不具有非零流量，这是非物理的。

### 压力损失

*压力损失* 描述由于面积减小而导致阀中压力降低。压力损失项 *PR*loss 计算如下：

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport.

*压力恢复* 描述由于面积增加而导致阀中压力正向变化。如果您不希望捕获此压力增加，请清除 **压力恢复** 复选框。在这种情况下，*PR*loss 为 1。

### 临界压力

临界压差 *Δp*crit 是与 **临界雷诺数** *Re*crit 相关的压差，后者是流体中层流与湍流之间的转变点：

Δpcrit=πρ¯8Aorifice(νRecritCd)2.

### 故障

当 **节流孔类型** 参数为 `Variable` 时，该模块可以对故障建模。

要对故障建模，请在 **故障** 部分中，单击要建模故障旁边的 **添加故障** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**故障时的开启面积** 参数有三个故障选项：

- `Closed` — 节流孔冻结在其最小值，具体取决于 **节流孔参数化**：

  - 当 **节流孔参数化** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **泄漏面积**。
  - 当 **节流孔参数化** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **节流孔面积向量** 的第一个元素。
  - 当 **节流孔参数化** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **体积流量表, q(s,dp)** 的第一行。
- `Open` — 节流孔冻结在其最大值，具体取决于 **节流孔参数化**：

  - 当 **节流孔参数化** 设置为 `Linear - Area vs. control member position` 时，节流孔冻结在 **最大节流孔面积**。
  - 当 **节流孔参数化** 设置为 `Tabulated data - Area vs. control member position` 时，节流孔冻结在 **节流孔面积向量** 的最后一个元素。
  - 当 **节流孔参数化** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 时，节流孔冻结在 **体积流量表, q(s,dp)** 的最后一行。
- `Maintain at last value` — 当触发发生时，节流孔卡在开启面积或体积流量处。
