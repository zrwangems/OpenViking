---
type: simulink-block
title: 'Orifice (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices'
documentation_page: 'orificema'
documentation_source_path: 'ref/orificema.html'
language: zh-CN
chinese_source: worker-translation
---

# Orifice (MA)

## 端口

### 守恒端口

### **A** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。

### **B** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。

### 输入

### **S** — 控制构件位置，m 物理信号

设定节流孔开度的控制构件位置。

#### 依赖关系

要启用此端口，请将 **Orifice type** 设置为 `Variable`。

## 参数

### **Orifice type** — 恒定或可变节流孔 `Variable`（默认）| `Constant`

节流孔类型。当您将此参数设置为 `Variable` 时，节流孔面积根据端口 **S** 接收的输入信号而变化。

### **Orifice parameterization** — 可变或恒定节流孔参数化 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据节流孔两端的压差计算质量流量，或根据质量流量计算压差的方法。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`。

### **Control member position at closed orifice** — 控制构件偏移量 `0` m（默认）| 正标量

控制构件偏移量，即节流孔完全关闭时 **S** 处的值。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear`。

### **Control member travel between closed and open orifice** — 控制构件行程 `5e-3` m（默认）| 正标量

控制构件在节流孔关闭和打开之间移动的距离。当您将 **Opening orientation** 设置为 `Positive control member displacement opens orifice` 时，节流孔在 **Control member position at closed orifice** 和 **Control member travel between closed and open orifice** 参数之和处完全打开。当您将 **Opening orientation** 设置为 `Negative control member displacement opens orifice` 时，节流孔在 **Control member position at closed orifice** 和 **Control member travel between closed and open orifice** 参数之差处完全打开。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear`。

### **Opening orientation** — 打开节流孔的位移方向 `Positive control member displacement opens orifice`（默认）| `Negative control member displacement opens orifice`

打开可变节流孔的构件位移方向。正方向表示 **S** 处信号的增加打开节流孔。负方向表示 **S** 处信号的减小打开节流孔。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

恒定 *Cv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Cv flow coefficient`。

### **Maximum Cv flow coefficient** — 对应于组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

节流孔完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，将 **Orifice
parameterization** 设置为 `Cv flow
coefficient`，并将 **Opening
characteristic** 设置为
`Linear`。

### **Control member position vector** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于表格化节流孔参数化的控制构件位置向量。向量元素与 **Orifice area vector**、**Cv flow
coefficient vector** 或 **Kv flow coefficient
vector** 参数中的值一一对应。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，并将 **Opening
characteristic** 设置为
`Tabulated`。

### **Cv flow coefficient vector** — 与构件位置向量中的值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。
每个系数对应 **Control member
position vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。向量的大小必须与
**Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，将 **Orifice
parameterization** 设置为 `Cv flow
coefficient`，并将 **Opening
characteristic** 设置为
`Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 阻塞流时的压差比系数 `0.7`（默认）| 正标量

入口压力
*pin* 与出口压力
*pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞时的值。

#### 依赖关系

要启用此参数，请将 **Orifice
parameterization** 设置为 `Cv flow
coefficient` 或 `Kv flow
coefficient`。

### **Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

常数 *Kv* 流量系数的值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Kv flow
coefficient`。

### **Maximum Kv flow coefficient** — 对应最大开启状态的 *Kv* 系数 `3.6`（默认）| 正标量

节流孔完全打开且可用流通面积最大时的 *Kv* 流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，将 **Orifice
parameterization** 设置为 `Kv flow
coefficient`，并将 **Opening
characteristic** 设置为
`Linear`。

### **Kv flow coefficient vector** — 与构件位置向量中的值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。
每个系数对应 **Control member
position vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。向量的大小必须与
**Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Variable`，将 **Orifice
parameterization** 设置为 `Kv flow
coefficient`，并将 **Opening
characteristic** 设置为
`Tabulated`。

### **Sonic conductance** — 阻塞流工况下流率能力的度量 `12 l/(bar*s)`（默认）| 正标量

在阻塞起始点测得的通过阻力元件的质量流率与上游压力和 ISO 8778 中定义的标准条件下质量密度之积的比值。此参数决定给定上游压力下允许的最大流率。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为
`Constant`，并将 **Orifice
parameterization** 设置为 `Sonic
conductance`。

### **Maximum sonic conductance** — 最大开启组件对应的声导 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 处指定的控制信号为 `1` 且可用于流动的横截面积最大时的声导值。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Sonic conductance`。
- **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 控制构件位置向量中各值对应的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声导向量。每个声导对应 **Control member position vector** 参数中的一个值。该向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 控制构件位置向量中各值对应的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应 **Control member position vector** 参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。该向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Orifice area** — 孔口开口面积 `1e-4` `m^2`（默认）| 正标量

孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### **Maximum orifice area** — 最大节流孔开度面积 `1e-4 m^2`（默认）| 正标量

节流孔完全打开时的面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Orifice area vector** — 节流孔开度面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1×*n* 向量

用于节流孔面积表格化参数化的节流孔面积值向量。此向量中的值与 **Control member position vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

实际流量与理想流量的比值。此参数用于考虑节流孔方程中未涵盖的实际损失。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时的流量与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在节流孔接近打开或接近关闭位置时为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，可提高仿真在这些区域中的稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间过渡时的节流孔出口压力与节流孔入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Cross-sectional area at ports A and B** — 阀端口面积 `0.01` m^2（默认）| 正标量

节流孔端口 **A** 和 **B** 的面积。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的节流孔

Orifice (MA) 模块用于建模湿空气网络中由恒定或可变面积节流孔引起的压力损失。该模块根据入口条件计算阀内流体特性。流体与环境之间不存在热交换，因此节流孔内部的相变仅由压降或从模型其他部分传播的相变引起。

节流孔可以是恒定的或可变的。当 **Orifice type** 参数为 `Variable` 时，端口 **S** 处的物理信号设置控制构件的位置，从而打开和关闭节流孔。

### 孔口参数化

模块行为取决于 **Orifice parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Sonic conductance` — 阻性元件在稳态下的声速导决定模块参数化。声速导衡量湿空气在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，就会发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 可变孔口

当您将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear` 时，模块使用端口 **S** 处的输入来计算孔口开度，

λ=ε(1−fleak)(S−Smin)ΔS+fleak，

其中 *S* 是端口 **S** 处信号的值，*Smin* 和 *ΔS* 分别是 **Control member position at closed orifice** 和 **Control member travel between closed and open orifice** 参数的值。

当您将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Tabulated` 时，模块根据 **Control member position vector** 参数和端口 **S** 处的输入对孔口特性进行插值。

对于可变孔口，孔口中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量与端口 **S** 处的控制信号成正比。随着控制信号增大，流量能力的度量从指定的最小值按比例变化到指定的最大值。

  当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为与控制信号无关的常数。
- `Tabulated` — 模块将流量能力的度量计算为端口 **S** 处控制信号的函数。该函数使用一维查找表。

  当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为控制信号的函数。

### Momentum Balance

模块方程取决于 **Orifice parametrization** 参数。

**Cv Flow Coefficient Parameterization**

当您将 **Orifice parametrization** 设置为 `Cv
flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin，

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *vin* 是入口比容。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked
  flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞状态，模块使用方程

m˙=23CvN6FγxTpinvin。

**Kv Flow Coefficient Parameterization**

当您将 **Orifice parametrization** 设置为 `Kv
flow coefficient` 时，模块使用与
`Cv flow coefficient` 参数化相同的方程，但使用关系式 Kv=0.865Cv 将
*Cv* 替换为
*Kv*。

**Sonic Conductance Parameterization**

当您将 **Orifice parametrization** 设置为 `Sonic
conductance` 时，质量流量为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是声速导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic
  index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比
*Bcrit* 以下时，孔口变为阻塞状态，模块切换到方程

m˙=CρrefpinTrefTin。

**Orifice parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能需要按混合气体比重的平方根来缩放声速导。

**Orifice Area Parameterization**

当您将 **Orifice parametrization** 设置为
`Orifice area` 时，质量流量为

m˙=CdAorifice2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AorificeAport)2(poutpin)2γ]，

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow
pressure ratio** 参数
*Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAorifice2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AorificeAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞状态，模块使用方程

m˙=CdAorifice2γγ+1pin1vin1(γ+12)2γ−1−(AorificeAport)2。

### Mass Balance

模块通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标
*g* 表示痕量气体，下标 *d*
表示水滴。

### Energy Balance

能量在孔口中守恒，

ΦA+ΦB=0，

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间没有热交换。
