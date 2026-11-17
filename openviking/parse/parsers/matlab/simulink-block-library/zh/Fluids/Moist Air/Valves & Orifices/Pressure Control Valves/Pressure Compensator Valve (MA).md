---
type: simulink-block
title: 'Pressure Compensator Valve (MA)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 湿空气端口 湿空气
  direction: input
- name: B
  summary: 湿空气端口 湿空气
  direction: input
- name: X
  summary: 压力参考 湿空气
  direction: input
- name: Y
  summary: 压力参考 湿空气
  direction: input
- name: Ps
  summary: 受控压差，Pa 物理信号
  direction: input
```

### 守恒

### **A** — 湿空气端口 湿空气

与阀入口相关联的湿空气守恒端口。

### **B** — 湿空气端口 湿空气

与阀出口相关联的湿空气守恒端口。

### **X** — 压力参考 湿空气

与感测 X 点压力 *Px* 相关联的湿空气守恒端口。

### **Y** — 压力参考 湿空气

与感测 Y 点压力 *P*y 相关联的湿空气守恒端口。
### 输入

### **Ps** — 受控压差，Pa 物理信号

用于阀受控运行的压差，单位为 Pa。

#### 依赖关系

要启用此端口，请将 **设置压力控制** 设置为 `Controlled`。
## 参数
```yaml
parameters:
- name: 阀参数化
  summary: 阀参数化模型 Cv flow coefficient (默认) | Kv flow coefficient | Sonic conductance | Orifice area
  group: ''
- name: 开度特性
  summary: 将控制信号转换为流通能力度量的方法 Linear (默认) | Tabulated
  group: ''
- name: 阀规格
  summary: 阀偏置 Normally open (默认) | Normally closed
  group: ''
- name: Set pressure control
  summary: 恒定或受控的阀门运行 Constant（默认） | Controlled
  group: ''
- name: Set pressure differential
  summary: 超出后触发恒定阀门运行的范围 0 MPa（默认） | scalar
  group: ''
- name: Pressure regulation range
  summary: 阀门工作压力范围 0.1 MPa（默认） | scalar
  group: ''
- name: Opening pressure differential vector
  summary: '用于表格化参数设置的压差值 [0.2 : 0.2 : 1.2] MPa（默认） | 1-by*n* vector'
  group: ''
- name: Maximum Cv flow coefficient
  summary: 组件处于最大开启状态时对应的 *Cv* 系数 4（默认） | positive scalar
  group: ''
- name: Cv 流量系数向量
  summary: 与构件位置向量中的值对应的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认值）| 1×*n* 向量
  group: ''
- name: 最大 Kv 流量系数
  summary: 组件完全打开时对应的 *Kv* 系数 3.6（默认值）| 正标量
  group: ''
- name: Kv 流量系数向量
  summary: 与构件位置向量中的值对应的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认值）| 1×*n* 向量
  group: ''
- name: 最大声速流导
  summary: 组件开度最大时对应的声速流导 12 l/(bar*s)（默认）| 正标量
  group: ''
- name: 临界压力比
  summary: 流动首次发生壅塞时下游压力与上游压力之比 0.3（默认）| 正标量
  group: ''
- name: 亚声速指数
  summary: 用于表征亚声速流动状态下质量流量的指数 0.5（默认）| 正标量
  group: ''
- name: ISO 参考温度
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: ''
- name: ISO 参考密度
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认值）| 正标量
  group: ''
- name: 声速流导向量
  summary: 与控制件位置向量中的值对应的声速流导 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认值）| 正值向量
  group: ''
- name: 临界压力比向量
  summary: 与控制件位置向量中的值对应的临界压力比 0.3 * ones(1,6)（默认值）| 正数向量
  group: ''
- name: 阻塞流时的 xT 压差比系数
  summary: 压差比 0.7（默认值）| 正标量
  group: ''
- name: 最大孔口面积
  summary: 最大阀门开口面积 1e-4 m^2（默认） | 正标量
  group: ''
- name: 孔口面积向量
  summary: 阀门开口面积值向量 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认） | 1×*n* 向量
  group: ''
- name: 流量系数
  summary: 流量系数 0.64（默认） | 正标量
  group: ''
- name: 泄漏流量比例
  summary: 流量比 1e-6（默认） | 正标量
  group: ''
- name: 平滑因子
  summary: 数值平滑因子 0.01（默认） | 范围 [0,1] 内的正标量
  group: ''
- name: 层流压力比
  summary: 层流-湍流转变压力比 0.999（默认值）| 正标量
  group: ''
- name: 端口 A 和 B 的横截面积
  summary: 阀门端口面积 0.01 m^2（默认值）| 正标量
  group: ''
- name: 开启动态特性
  summary: 是否考虑流量对阀门开启的响应 off（默认值）| on
  group: ''
- name: 开启时间常数
  summary: 阀门开启时间常数 0.1 s（默认值）| 正标量
  group: ''
```

### **阀参数化** — 阀参数化模型 `Cv flow coefficient` (默认) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据阀两端的压差计算质量流率，或根据质量流率计算压差的方法。

### **开度特性** — 将控制信号转换为流通能力度量的方法 `Linear` (默认) | `Tabulated`

对所选的流通能力度量进行参数化的方法。

### **阀规格** — 阀偏置 `Normally open` (默认) | `Normally closed`

压力补偿阀的正常工作状态。对于减压阀，选择 `Normally open` 阀。对于溢流阀，选择 `Normally closed`。

### **Set pressure control** — 恒定或受控的阀门运行 `Constant`（默认） | `Controlled`

阀门运行方式。将此参数设置为以下值时：

- `Controlled` 并将压力信号连接到端口 **Ps** 时，模块保持压力调节范围恒定。当 *Pcontrol* 大于端口 **Ps** 处的信号值且小于 *Pmax* 时，阀门调节压力。
- `Constant` 时，**Set pressure differential** 参数定义恒定的设定压力。

### **Set pressure differential** — 超出后触发恒定阀门运行的范围 `0` `MPa`（默认） | scalar

触发压力补偿的压差大小。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Pressure regulation range** — 阀门工作压力范围 `0.1` `MPa`（默认） | scalar

阀门的工作压力范围。压力调节范围定义了 **Set pressure differential** 参数与阀门最大工作压力之间的差值。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Opening pressure differential vector** — 用于表格化参数设置的压差值 `[0.2 : 0.2 : 1.2]` `MPa`（默认） | 1-by*n* vector

用于开启面积表格化参数设置的压差值向量。压力值必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 组件处于最大开启状态时对应的 *Cv* 系数 `4`（默认） | positive scalar

当可供流动的节流面积达到最大时，*Cv* 流量系数的值。该参数衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Cv 流量系数向量** — 与构件位置向量中的值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认值）| 1×*n* 向量

由 *Cv* 流量系数组成的向量。每个系数都对应于 **开启压力（表压）向量** 参数中的一个值。此参数用于衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 组件完全打开时对应的 *Kv* 系数 `3.6`（默认值）| 正标量

当可供流动的节流面积达到最大值时的 *Kv* 流量系数值。此参数用于衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 与构件位置向量中的值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认值）| 1×*n* 向量

由 *Kv* 流量系数组成的向量。每个系数都对应于 **开启压力（表压）向量** 参数中的一个值。此参数用于衡量在压差驱动下，蒸气通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大声速流导** — 组件开度最大时对应的声速流导 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 处指定的控制信号为 `1`，且可供流通的横截面积达到最大值时的声速流导值。

#### 依赖关系

要启用此参数，请将**阀参数化方式**设置为 `Sonic conductance`，并将**开启特性**设置为 `Linear`。

### **临界压力比** — 流动首次发生壅塞时下游压力与上游压力之比 `0.3`（默认）| 正标量

流动首次开始壅塞且流速达到最大值（由当地声速确定）时的压力比。该压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将**阀参数化方式**设置为 `Sonic conductance`，并将**开启特性**设置为 `Linear`。

### **亚声速指数** — 用于表征亚声速流动状态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流动状态下质量流率的经验值。

#### 依赖关系

要启用此参数，请将**阀参数化方式**设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当所使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将**阀参数化方式**设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认值）| 正标量

标准参考大气条件下的密度，ISO 8778 将其定义为 1.185 kg/m3。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`。

### **声速流导向量** — 与控制件位置向量中的值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认值）| 正值向量

阻性元件内部的声速流导向量。此向量中的值与 **开启压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **临界压力比向量** — 与控制件位置向量中的值对应的临界压力比 `0.3 * ones(1,6)`（默认值）| 正数向量

流动首次发生阻塞时的临界压力比向量。临界压力比是下游压力与上游压力之比，在该比值下，流速达到当地声速。此向量中的值与 **开启压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认值）| 正标量

首次发生阻塞时，入口压力 *pin* 与出口压力 *pout* 之间的压差比，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请将 **阀参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大孔口面积** — 最大阀门开口面积 `1e-4 m^2`（默认） | 正标量

阀门完全打开时的最大阀口面积。

#### 依存关系

要启用此参数，请将**阀门参数化**设置为 `Orifice area`，并将**开启特性**设置为 `Linear`。

### **孔口面积向量** — 阀门开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认） | 1×*n* 向量

用于蒸汽阀面积表格化参数化的孔口面积值向量。此向量中的值与**开启压力（表压）向量**参数中的元素一一对应。

#### 依存关系

要启用此参数，请将**阀门参数化**设置为 `Orifice area`，并将**开启特性**设置为 `Tabulated`。

### **流量系数** — 流量系数 `0.64`（默认） | 正标量

实际流量与理想流量之比。此参数用于考虑孔口方程未涵盖的实际工况损耗。

#### 依存关系

要启用此参数，请将**阀门参数化**设置为 `Orifice area`。

### **泄漏流量比例** — 流量比 `1e-6`（默认） | 正标量

阀门关闭时的流量与阀门打开时的流量之比。

#### 依存关系

要启用此参数，请将**开启特性**设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，在阀门处于接近全开或接近全闭位置时，为流量响应引入一个渐变层。将此参数设置为小于 1 的非零值，以提高仿真在这些区域中的稳定性。

#### 依存关系

要启用此参数，请将**开启特性**设置为 `Linear`。

### **层流压力比** — 层流-湍流转变压力比 `0.999`（默认值）| 正标量

流体在层流与湍流状态之间转换时的阀门出口压力与阀门入口压力之比。层流时，压力损失与质量流量呈线性关系；湍流时，压力损失与质量流量呈二次关系。

### **端口 A 和 B 的横截面积** — 阀门端口面积 `0.01` m^2（默认值）| 正标量

端口 **A** 和 **B** 的面积。

### **开启动态特性** — 是否考虑流量对阀门开启的响应 `off`（默认值）| `on`

是否考虑阀门开启对流体系统造成的瞬态影响。选择此参数后，将通过在流量响应中引入一阶滞后来近似开启条件。

### **开启时间常数** — 阀门开启时间常数 `0.1` s（默认值）| 正标量

用于计算开启动态特性中滞后的时间常数。

#### 依赖关系

要启用此参数，请选择**开启动态特性**。
## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Pressure Control Valves

## 模块特性

未在 R2025b 中提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的压力补偿阀

Pressure Compensator Valve (MA) 模块表示湿空气网络中的压力补偿器，例如溢流阀或减压阀。使用该阀可根据系统其他部分的信号来维持阀处的压力。有关阀参数化和模块计算的详细信息，请参阅 Orifice (MA) 模块。

端口 **X** 和 **Y** 之间的压差为控制压力 *Pcontrol*。当该值达到或超过设定压力时，阀的通流开口会打开或关闭，具体取决于 **Valve specification** 参数。压力调节范围从设定压力 *Pset* 开始。可以在恒定设定压力调节和受控设定压力调节之间进行选择。端口 **Ps** 处的物理信号提供可变的设定压力。

### 压力控制

当 *Pcontrol* 超过 *Pset* 时，模块会调节压力。模块会持续调节压力，直至达到 *Pmax*，即 *Pset* 与压力调节范围之和。模块支持两种调节模式：

- 当您将 **Set pressure control** 设置为
  `Controlled` 并将压力信号连接到端口 **Ps** 时，模块会保持压力调节范围不变。当 *Pcontrol* 大于端口 **Ps** 处的信号值且小于 *Pmax* 时，阀会调节压力。
- 当您将 **Set pressure control** 设置为
  `Constant` 时，**Set pressure differential** 参数会定义一个恒定的设定压力。

当您将 **Opening characteristic** 设置为 `Linear` 时，通流能力的度量值在 *Pset* 和 *Pmax* 之间线性变化。

当您将 **Opening characteristic** 设置为 `Tabulated` 时，通流能力的度量值根据 **Opening pressure differential vector** 参数而变化。

### 开启动态特性

当您将**开启动态特性**设置为 `On` 时，模块会引入控制压力滞后，并用动态控制压力 *pdyn* 替换 *pcontrol*。模块根据**开启时间常数**参数 *τ* 计算动态控制压力

p˙dyn=pcontrol−pdynτ.

默认情况下，模块不对**开启动态特性**建模。对于线性参数化，当节流孔处于接近关闭或接近打开的位置时，**平滑因子**参数的非零值可提供额外的数值稳定性。

模块根据**开启特性**参数计算稳态动态特性，且该计算基于控制压力 *pcontrol*。

### 动量平衡

模块方程取决于 **Valve parameterization** 参数。当您将 **Valve parameterization** 设置为 `Cv flow coefficient` 时，质量流率 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：

- *Cv* 为 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 为阀的开启面积。
- *SMax* 为阀完全打开时的最大阀面积。
- *N6* 是一个常数；当质量流率以 kg/hr 为单位、压力以 bar 为单位、密度以 kg/m3 为单位时，其值等于 27.3。
- *Y* 为膨胀因子。
- *pin* 为入口压力。
- *pout* 为出口压力。
- *ρin* 为入口密度。

膨胀因子为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 为等熵指数与 1.4 的比值。
- *xT* 为 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升高并超过 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块会平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，节流孔进入阻塞状态，模块改用以下方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当您将 **Valve parameterization** 设置为 `Kv flow coefficient` 时，模块使用相同的方程，但利用关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关 **Valve parameterization** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时质量流率方程的详细信息，请参阅 [2][3]。

当您将 **Valve parameterization** 设置为 `Sonic conductance` 时，质量流率 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是 **最大声速流导** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **亚声速指数** 参数的值。
- *Tref* 是 **ISO 参考温度** 参数的值。
- *ρref* 是 **ISO 参考密度** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至高于 **层流压力比** 参数的值 *Blam* 时，模块会平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至低于临界压力比 *Bcrit* 时，节流孔发生壅塞，模块切换为以下方程

m˙=CSopenSMaxρrefpinTrefTin。

**阀参数化** 参数的 `Sonic conductance` 设置适用于气动应用。如果对痕量气体含量较高的湿空气使用此设置，或者要对空气以外的流体建模，则可能需要按混合物比重的平方根对声速流导进行缩放。

有关 **阀参数化** 参数为 `Sonic conductance` 时的质量流量方程的更多信息，请参阅 [1]。

当将 **阀参数化** 设置为 `Orifice area` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ]，

其中：

- *Sopen* 是阀开口面积。
- *S* 是 **端口 A 和 B 的横截面积** 参数的值。
- *Cd* 是 **流量系数** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至高于 **层流压力比** 参数的值 *Blam* 时，模块会平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至(2γ+1)γγ−1 以下时，节流孔进入壅塞状态，模块改用以下方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关 **Valve parameterization** 参数为 `Orifice area` 时质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

该模块使通过阀的质量守恒

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中，*ṁ* 为质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### 能量平衡

该模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口流向出口时，外界不对流体做功，流体也不对外做功。能量只能通过平流方式经端口 **A** 和 **B** 传输。根据能量守恒原理，各端口能量流之和始终等于零

ϕA+ϕB=0,

其中，*ϕ* 是通过端口 **A** 或 **B** 流入阀的能量流率。
