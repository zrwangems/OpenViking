---
type: simulink-block
title: 'Pressure Compensator Valve (MA)'
family: 'moist-air'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurecompensatorvalvema'
documentation_source_path: 'ref/pressurecompensatorvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Compensator Valve (MA)

## 端口

### 守恒

### **A** — 湿空气端口 湿空气

与阀入口关联的湿空气守恒端口。

### **B** — 湿空气端口 湿空气

与阀出口关联的湿空气守恒端口。

### **X** — 压力参考 湿空气

与感测点 X 处的压力 *Px* 相关联的湿空气守恒端口。

### **Y** — 压力参考 湿空气

与感测点 Y 处的压力 *P*y 相关联的湿空气守恒端口。
### 输入

### **Ps** — 受控压差，Pa 物理信号

用于受控阀运行的压差，单位为 Pa。

#### 依赖关系

要启用此端口，请将 **设定压力控制** 设置为 `Controlled`。

## 参数

### **阀参数化** — 阀参数化模型 `Cv flow coefficient` (默认) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块根据阀两端的压差计算质量流量，或根据质量流量计算压差时所使用的方法。

### **开启特性** — 将控制信号转换为流通能力度量的方法 `Linear` (默认) | `Tabulated`

对所选的流通能力度量进行参数化的方法。

### **阀规格** — 阀偏置 `Normally open` (默认) | `Normally closed`

压力补偿阀的正常工作状态。对于减压阀，请选择 `Normally open` 阀。对于溢流阀，请选择 `Normally closed`。

### **设定压力控制** — 恒定或受控阀运行 `Constant` (默认) | `Controlled`

阀的运行方式。将此参数设置为：

- `Controlled`，并将压力信号连接到端口 **Ps** 时，模块保持压力调节范围恒定。当 *Pcontrol* 大于端口 **Ps** 处的信号值且小于 *Pmax* 时，阀会调节压力。
- `Constant` 时，**设定压差** 参数定义恒定的设定压力。

### **设定压差** — 超出此范围时触发阀的恒定运行 `0` `MPa` (默认) | scalar

触发压力补偿的压差幅值。

#### 依赖关系

要启用此参数，请将 **设定压力控制** 设置为 `Constant`。

### **压力调节范围** — 阀的工作压力范围 `0.1` `MPa` (默认) | scalar

阀的工作压力范围。压力调节范围定义了 **设定压差** 参数与阀最大工作压力之间的差值。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **开启压差向量** — 用于表格参数化的压差值 `[0.2 : 0.2 : 1.2]` `MPa` (默认) | 1-by*n* vector

用于开口面积表格参数化的压差值向量。压力值必须按升序排列。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Tabulated`。

### **最大 Cv 流量系数** — 与组件最大开度对应的 *Cv* 系数 `4` (默认) | positive scalar

当可用于流动的节流面积达到最大值时的 *Cv* 流量系数值。该参数衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Cv 流量系数向量** — 与构件位置向量中的值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认值）| 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **开启压力（表压）向量** 参数中的一个值。该参数用于衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开口特性** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 组件完全打开时对应的 *Kv* 系数 `3.6`（默认值）| positive scalar

当可用于流通的节流面积最大时的 *Kv* 流量系数值。该参数用于衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开口特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 与构件位置向量中的值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认值）| 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **开启压力（表压）向量** 参数中的一个值。该参数用于衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开口特性** 设置为 `Tabulated`。

### **最大声速流导** — 组件完全打开时对应的声速流导 `12 l/(bar*s)`（默认值）| positive scalar

当端口 **S** 处指定的控制信号为 `1` 且可用于流通的横截面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`，并将 **开口特性** 设置为 `Linear`。

### **临界压力比** — 流动首次发生壅塞时的下游压力与上游压力之比 `0.3`（默认值）| positive scalar

流动首次开始发生壅塞且流速达到最大值（即当地声速）时的压力比。该压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`，并将 **开口特性** 设置为 `Linear`。

### **亚声速指数** — 用于表征亚声速流状态下质量流量的指数 `0.5`（默认值）| positive scalar

用于更准确地计算亚声速流状态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认值）| scalar

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数的值。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认值）| positive scalar

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数的值。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`。

### **声速流导向量** — 与控制构件位置向量中的值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)` (默认) | vector of positive values

阻性元件内的声速流导向量。此向量中的值与 **开启压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **临界压力比向量** — 与控制构件位置向量中的值对应的临界压力比 `0.3 * ones(1,6)` (默认) | vector of positive numbers

流动首次发生阻塞时的临界压力比向量。临界压力比是流速达到当地声速时的下游压力与上游压力之比。此向量中的值与 **开启压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **阻塞流下的 xT 压差比因子** — 压差比 `0.7` (默认) | positive scalar

首次发生阻塞时，入口压力 *pin* 与出口压力 *pout* 之间的压差比，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大孔口面积** — 最大阀门开启面积 `1e-4 m^2` (默认) | positive scalar

阀门完全打开时的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Linear`。

### **孔口面积向量** — 阀门开启面积值的向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (默认) | 1-by-*n* vector

用于对蒸气阀面积进行表格参数化的孔口面积值向量。此向量中的值与 **开启压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Tabulated`。

### **流量系数** — 流量系数 `0.64` (默认) | positive scalar

实际流量与理想流量之比。此参数用于考虑孔口方程未体现的实际损失。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Orifice area`。

### **泄漏流量比** — 流量之比 `1e-6` (默认) | positive scalar

阀门关闭时的流量与阀门打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01` (默认) | positive scalar in the range [0,1]

连续平滑因子，在阀门处于接近打开或接近关闭位置时，为流量响应引入一个逐渐变化的过渡层。将此参数设置为小于 1 的非零值，以提高仿真在这些区域的稳定性。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **层流压力比** — 层流-湍流转变压力比 `0.999` (默认) | positive scalar

流体在层流和湍流状态之间转变时，阀门出口压力与阀门入口压力之比。在层流中，压力损失与质量流量呈线性关系；在湍流中，压力损失与质量流量呈二次关系。

### **端口 A 和 B 的横截面积** — 阀门端口面积 `0.01` m^2 (默认) | positive scalar

端口 **A** 和 **B** 的面积。

### **开启动态特性** — 是否考虑流量对阀开启的响应 `off`（默认值） | `on`

是否考虑阀开启在流体系统中引起的瞬态效应。选择此参数后，通过在流量响应中引入一阶滞后来近似开启条件。

### **开启时间常数** — 阀开启时间常数 `0.1` s（默认值） | 正标量

用于计算开启动态特性中滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **开启动态特性**。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2025a 中推出**

## 描述

湿空气网络中的压力补偿阀

Pressure Compensator Valve (MA) 模块表示湿空气网络中的压力补偿器，例如泄压阀或减压阀。使用该阀可根据系统其他部分的信号来维持阀处的压力。有关阀参数化方式和模块计算的详细信息，请参阅 Orifice (MA) 模块。

端口 **X** 和 **Y** 之间的压差为控制压力 *Pcontrol*。当该值达到或超过设定压力时，阀口打开还是关闭取决于 **阀规格** 参数。压力调节范围始于设定压力 *Pset*。可以选择恒定设定压力调节或受控设定压力调节。端口 **Ps** 处的物理信号提供可变的设定压力。

### 压力控制

当 *Pcontrol* 超过 *Pset* 时，模块会调节压力。模块会持续调节压力，直至 *Pmax*，即 *Pset* 与压力调节范围之和。模块支持两种调节模式：

- 当您将 **设定压力控制** 设置为
  `Controlled` 并将压力信号连接到端口 **Ps** 时，模块会保持压力调节范围不变。当 *Pcontrol* 大于端口 **Ps** 处的信号值且小于 *Pmax* 时，阀会调节压力。
- 当您将 **设定压力控制** 设置为
  `Constant` 时，**设定压差** 参数用于定义恒定的设定压力。

当您将 **开启特性** 设置为 `Linear` 时，流通能力度量值在 *Pset* 和 *Pmax* 之间呈线性变化。

当您将 **开启特性** 设置为 `Tabulated` 时，流通能力度量值随 **开启压差向量** 参数而变化。

### 开启动态特性

当您将 **开启动态特性** 设置为 `On` 时，模块会引入控制压力滞后，并用动态控制压力 *pdyn* 代替 *pcontrol*。模块根据 **开启时间常数** 参数（*τ*）计算动态控制压力：

p˙dyn=pcontrol−pdynτ.

默认情况下，模块不对 **开启动态特性** 建模。对于线性参数化，当节流孔处于接近全闭或接近全开位置时，**平滑因子** 参数的非零值可提供额外的数值稳定性。

模块根据 **开启特性** 参数计算稳态动态特性，且该计算基于控制压力 *pcontrol*。

### 动量平衡

模块方程取决于 **Valve parameterization** 参数。当您将 **Valve parameterization** 设置为 `Cv flow coefficient` 时，质量流率 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：

- *Cv* 为 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 为阀口开启面积。
- *SMax* 为阀门完全打开时的最大阀口面积。
- 当质量流率以 kg/hr 为单位、压力以 bar 为单位、密度以 kg/m3 为单位时，*N6* 为等于 27.3 的常数。
- *Y* 为膨胀系数。
- *pin* 为入口压力。
- *pout* 为出口压力。
- *ρin* 为入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 为等熵指数与 1.4 的比值。
- *xT* 为 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升高并超过 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块将平滑过渡到方程的线性化形式：

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 低于 1−FγxT 时，节流孔进入阻塞状态，模块切换为以下方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当您将 **Valve parameterization** 设置为 `Kv flow coefficient` 时，模块使用相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关 **Valve parameterization** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Valve parameterization** 设置为 `Sonic conductance` 时，质量流率 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 为 **Maximum sonic conductance** 参数的值。
- *Bcrit* 为临界压力比。
- *m* 为 **Subsonic index** 参数的值。
- *Tref* 为 **ISO reference temperature** 参数的值。
- *ρref* 为 **ISO reference density** 参数的值。
- *Tin* 为入口温度。

当压力比 pout/pin 升高并超过 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块将平滑过渡到方程的线性化形式：

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 低于临界压力比 *Bcrit* 时，节流孔进入阻塞状态，模块切换为以下方程

m˙=CSopenSMaxρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您对痕量气体含量较高的湿空气使用此设置，或者对空气以外的流体进行建模，则可能需要将声速流导乘以混合物比重的平方根。

有关 **Valve parameterization** 参数为 `Sonic conductance` 时质量流量方程的更多信息，请参阅 [1]。

当您将 **Valve parameterization** 设置为 `Orifice area` 时，质量流率 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

其中：

- *Sopen* 为阀口开启面积。
- *S* 为 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 为 **Discharge coefficient** 参数的值。
- *γ* 为等熵指数。

当压力比 pout/pin 升高并超过 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块将平滑过渡到方程的线性化形式：

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 低于 (2γ+1)γγ−1 时，节流孔进入阻塞状态，模块切换为以下方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关 **Valve parameterization** 参数为 `Orifice area` 时质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

该模块使流经阀门的质量守恒

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中，*ṁ* 为质量流量，下标 *w* 表示水蒸气，下标
*g* 表示痕量气体，下标 *d*
表示水滴。

### 能量平衡

该模块的阻性元件是一个绝热组件。流体与包围它的壁面之间不能发生热交换。
流体从入口流向出口时，既不外界对流体做功，也不流体对外做功。能量只能通过平流方式，
经端口 **A** 和 **B** 流动。根据能量守恒原理，各端口
能量流之和始终等于零

ϕA+ϕB=0,

其中，*ϕ* 为通过端口 **A** 或 **B**
流入阀门的能量流率。
