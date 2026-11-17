---
type: simulink-block
title: 'Thyristor (Piecewise Linear)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'thyristorpiecewiselinear'
documentation_source_path: 'ref/thyristorpiecewiselinear.html'
language: zh-CN
chinese_source: worker-translation
---

# Thyristor (Piecewise Linear)

## 端口
```yaml
ports:
- name: G
  summary: 门极端子电气
  direction: conserving
- name: A
  summary: 阳极端子电气
  direction: conserving
- name: K
  summary: 阴极端子电气
  direction: conserving
- name: H
  summary: 热端口热
  direction: conserving
```

### 守恒端口

### **G** — 门极端子电气

与门极端子关联的端口。您可以将该端口设置为物理信号端口或电气端口。

### **A** — 阳极端子电气

与阳极端子关联的电气守恒端口。

### **K** — 阴极端子电气

与阴极端子关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 热端口可见性 No thermal port（默认）| Show thermal port
  group: ''
- name: Gate-control port
  summary: 是否指定物理或电气控制端口 PS（默认）| Electrical
  group: 主要
- name: On-state behavior and switching losses
  summary: 用于开关损耗数据的通态电流 Specify constant values（默认）| Tabulate
  group: 主要
- name: Forward voltage, Vf
  summary: 正向电压 0.8 V（默认）
  group: 主要
- name: On-state resistance
  summary: 通态电阻 0.001 Ohm（默认）
  group: 主要
- name: Off-state conductance
  summary: 断态电导 1e-5 1/Ohm（默认）
  group: 主要
- name: Gate trigger voltage, Vgt
  summary: 门极触发电压 6 V（默认）
  group: 主要
- name: Holding current
  summary: 维持电流 1 A（默认）
  group: 主要
- name: On-state voltage, Vak(Tj,Iak)
  summary: 通态电压 [0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8] V（默认）| 非负标量矩阵
  group: 主要
- name: Temperature vector, Tj
  summary: 温度值 [298.15, 398.15] K（默认）| 向量
  group: 主要
- name: Anode-cathode current vector, Iak
  summary: 阳极-阴极电流向量 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）
  group: 主要
- name: Switch-on loss
  summary: 开通损耗 22.86e-3 J（默认）| 正标量
  group: 开关损耗
- name: Natural commutation rectification loss
  summary: 自然换流整流损耗 10e-3 J（默认）| 正标量
  group: 开关损耗
- name: Off-state voltage for switching loss data
  summary: 用于损耗数据的断态电压 300 V（默认）| 正标量
  group: 开关损耗
- name: On-state current for switching loss data
  summary: 输出电流 600 A（默认）| 正标量
  group: 开关损耗
- name: Switch-on loss, Eon(Tj,Iak)
  summary: 开通损耗 [0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3 J（默认）|
    非负标量矩阵
  group: 开关损耗
- name: Temperature vector for switching losses, Tj
  summary: 开关损耗温度 [298.15, 398.15] K（默认）| 向量
  group: 开关损耗
- name: Anode-cathode current vector for switching losses, Iak
  summary: 开关损耗阳极-阴极电流向量 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）| 非负标量向量
  group: 开关损耗
- name: Wait time before switch-on current measurement
  summary: 测量通态电流之前的时间 1e-4 s（默认）| 非负标量
  group: 开关损耗
- name: Integral protection diode
  summary: 集成保护二极管 External diode（默认）| Protection diode with no dynamics | Protection diode with charge dynamics
  group: 积分二极管
- name: Diode model
  summary: 二极管模型 Piecewise Linear（默认）| Tabulated I-V curve
  group: 积分二极管
- name: Table type
  summary: 表格化函数 Table in If(Tj,Vf) form（默认）| Table in Vf(Tj,If) form
  group: 积分二极管
- name: Forward voltage
  summary: 正向电压 0.8 V（默认）
  group: 积分二极管
- name: On resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 积分二极管
- name: Forward currents, If(Tj,Vf)
  summary: 正向电流向量 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12] A（默认）| 非负向量
  group: 积分二极管
- name: Junction temperatures, Tj
  summary: 结温向量 [25, 125] degC（默认）
  group: 积分二极管
- name: Forward voltages, Vf
  summary: 正向电压向量 [.5, .7, .9, 1.3, 1.7, 2.1, 2.5] V（默认）
  group: 积分二极管
- name: Forward voltages, Vf(Tj,If)
  summary: 正向电压向量 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7] V（默认）| 非负向量
  group: 积分二极管
- name: Forward currents, If
  summary: 正向电流向量 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认）
  group: 积分二极管
- name: Off conductance
  summary: 关断电导 1e-5 1/Ohm（默认）
  group: 积分二极管
- name: Reverse recovery loss model
  summary: 反向恢复损耗模型 Fixed loss（默认）| Tabulated loss
  group: 积分二极管
- name: Reverse recovery loss
  summary: 反向恢复损耗 0 J（默认）| 非负标量
  group: 积分二极管
- name: Scale reverse recovery loss with current and voltage
  summary: 随电流和电压缩放反向恢复损耗的选项 On（默认）| Off
  group: 积分二极管
- name: Reverse recovery loss table, Erect(Tj), If
  summary: 反向恢复损耗表 zeros(2,3) J（默认）| 非负标量向量
  group: 积分二极管
- name: Temperature vector for recovery loss table, Tj
  summary: 恢复损耗表的温度向量 [298.15 398.15] K（默认）| 向量
  group: 积分二极管
- name: Forward current vector for recovery loss table, If
  summary: 恢复损耗表的正向电流向量 [.1, 1, 10] K（默认）| 非负标量向量
  group: 积分二极管
- name: Forward current when measuring recovery loss, Irec
  summary: 测量恢复损耗时的正向电流 10 A（默认）| 正标量
  group: 积分二极管
- name: Turn-off voltage when measuring recovery loss, Vrec
  summary: 测量恢复损耗时的关断电压 10 V（默认）| 正标量
  group: 积分二极管
- name: Filter time constant for voltage and current values
  summary: 电压和电流值的滤波时间常数 1 / 1000 / 100 s（默认）| 正标量
  group: 积分二极管
- name: Junction capacitance
  summary: 结电容 50e-9 F（默认）
  group: 积分二极管
- name: Peak reverse current, iRM
  summary: 峰值反向电流 -235 A（默认）| 负标量
  group: 积分二极管
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 300 A（默认）| 正标量
  group: 积分二极管
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -50A/μs（默认）| 负标量
  group: 积分二极管
- name: Reverse recovery time parameterization
  summary: 反向恢复时间参数化 Specify reverse recovery time directly（默认）| Specify stretch factor | Specify reverse recovery charge
  group: 积分二极管
- name: Reverse recovery time, trr
  summary: 反向恢复时间 15 μs（默认）| 标量
  group: 积分二极管
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认）| 大于 1 的标量
  group: 积分二极管
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 μAs（默认）
  group: 积分二极管
- name: Diode turn-off voltage when measuring Erec
  summary: 测量 Erec 时的二极管关断电压 -600 V（默认）
  group: 积分二极管
- name: Stray inductance when measuring Erec
  summary: 测量 Erec 时的杂散电感 150 nH（默认）
  group: 积分二极管
- name: Reverse recovery energy, Erec
  summary: 反向恢复能量 0.03 J（默认）
  group: 积分二极管
- name: Thermal network
  summary: 热网络建模选项 External（默认）| Specify junction and case thermal parameters | Cauer model | Cauer model parameterized with
    Foster coefficients
  group: 热端口
- name: Thermal mass parameterization
  summary: 热质量参数化选项 By thermal time constants（默认）| By thermal mass
  group: 热端口
- name: Junction case and case-ambient (or case-heatsink) thermal resistances, [R_JC R_CA]
  summary: 结-壳和壳-环境（或壳-散热器）热阻 [.08, .5] K/W（默认）| 正值向量
  group: 热端口
- name: Junction and case thermal time constants, [t_J t_C]
  summary: 结和壳热时间常数 [.001, .2] s（默认）| 正值向量
  group: 热端口
- name: Junction and case thermal masses, [M_J M_C]
  summary: 结和壳热质量 [.01, .5] J/K（默认）| 正值向量
  group: 热端口
- name: Junction and case initial temperatures, [T_J T_C]
  summary: 结和壳初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal resistances, [R1 R2 … Rn]
  summary: 热阻 [.08,.1,.5] K/W | [.08,.14,.22,.16] K/W | 正值向量
  group: 热端口
- name: Thermal masses, [M1 M2 … Mn]
  summary: 热质量 [.01,.1,.5] J/K | [.001,.005,.05,.5] J/K | 正值向量
  group: 热端口
- name: Thermal masses initial temperatures, [T1 T2 … Tn]
  summary: 热质量初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal time constants, [t1 t2 … tn]
  summary: 热时间常数 [.001,.1,.2] s | [7e-05, .0007, .01, .08] s | 正值向量
  group: 热端口
- name: Initial node temperatures, [T1 T2 ... Tn]
  summary: 初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Junction thermal mass
  summary: 结热质量 0.01 J/K（默认）| 正标量
  group: 热端口
```

### **Modeling option** — 热端口可见性 `No thermal port`（默认）| `Show thermal port`

是否启用热端口。

### 主要

此表显示了 **Main** 参数的可见性如何取决于您如何配置 **Modeling option** 和
**On-state behavior and switching losses** 参数。要了解
如何阅读此表，请参阅参数依赖关系。

**主要参数依赖关系**

| 参数和选项 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Modeling option** | | | | | | | |
| *`No thermal port`* | | | | *`Show thermal port`* | | | |
| Gate-control port | | | | Gate-control port | | | |
| Forward voltage, Vf | | | | Gate trigger voltage, Vgt | | | |
| On-state resistance | | | | Holding current | | | |
| Off-state conductance | | | | **On-state behavior and switching losses** | | | |
| *`Specify constant values`* | *`Tabulate`* | | |
| Gate trigger voltage, Vgt | | | | Forward voltage, Vf | On-state voltage, Vak(Tj,Iak) | | |
| Holding current | | | | On-state resistance | Temperature vector, Tj | | |
| Off-state conductance | Anode-cathode current vector, Iak | | |
| Off-state conductance | | |

### **Gate-control port** — 是否指定物理或电气控制端口 `PS`（默认）| `Electrical`

是否为开关门极指定物理或电气控制端口。

### **On-state behavior and switching losses** — 用于开关损耗数据的通态电流 `Specify constant values`（默认）| `Tabulate`

通态行为和开关损耗的参数化方法，
指定为以下值之一：

- `Specify constant values` — 使用
  标量值来指定输出电流、开通损耗
  和关断损耗数据。
- `Tabulate` — 使用向量来
  指定输出电流和温度数据。使用
  矩阵来指定开通损耗和关断损耗
  数据。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

器件导通时的正向电压。

#### 依赖关系

请参阅主要参数依赖关系
表。

### **On-state resistance** — 通态电阻 `0.001` `Ohm`（默认）

器件导通时的阳极-阴极电阻。

#### 依赖关系

请参阅主要参数依赖关系
表。

### **Off-state conductance** — 断态电导 `1e-5` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须
小于 1/*R*，其中 *R* 是
**On-state resistance** 的值。

#### 依赖关系

请参阅主要参数依赖关系
表。

### **Gate trigger voltage, Vgt** — 门极触发电压 `6` `V`（默认）

门极-阴极电压阈值。当
门极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅主要参数依赖关系
表。

### **Holding current** — 维持电流 `1` `A`（默认）

电流阈值。当电流高于此值时，器件保持导通，
即使门极-阴极电压降至门极触发
电压以下。

#### 依赖关系

请参阅主要参数依赖关系
表。

### **On-state voltage, Vak(Tj,Iak)** — 通态电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V`（默认）| 非负标量矩阵

器件在触发导通状态下的电压降。此
参数是温度和最终通态输出
电流的函数。

#### 依赖关系

请参阅主要参数依赖关系
表。

### **Temperature vector, Tj** — 温度值 `[298.15, 398.15]` `K`（默认）| 向量

您给出通态电压时所对应的
温度值。

#### 依赖关系

请参阅主要参数依赖关系
表。

### **Anode-cathode current vector, Iak** — 阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）

定义通态电压所对应的阳极-阴极电流。第一个
元素必须为零。使用向量
量指定此参数。

#### 依赖关系

请参阅主要参数依赖关系
表。

### 开关损耗

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and
switching losses** 设置为 `Specify constant
values`。

### **Natural commutation rectification loss** — 自然换流整流损耗 `10e-3` `J`（默认）| 正标量

当电流降至 **Holding current** 参数值以下且模块
关断时适用的整流损耗。

### **Off-state voltage for switching loss data** — 用于损耗数据的断态电压 `300` `V`（默认）| 正标量

器件在断态期间的输出电压。此值是
您定义开通损耗和关断
损耗数据时的阻断电压。

### **On-state current for switching loss data** — 输出电流 `600` `A`（默认）| 正标量

您定义开通损耗和关断损耗时所对应的
输出电流。

**注意**

模块在门极电压降至 **Gate trigger voltage,
Vgt** 参数值以下时测量此参数。开通脉冲长于
电流达到其最大值所需的时间。

#### 依赖关系

要启用此参数，请将 **On-state behavior and
switching losses** 设置为 `Specify constant
values`。

### **Switch-on loss, Eon(Tj,Iak)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 非负标量矩阵

单次开通事件期间耗散的能量，作为
温度和最终通态输出电流的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and
switching losses** 设置为
`Tabulate`。

### **Temperature vector for switching losses, Tj** — 开关损耗温度 `[298.15, 398.15]` `K`（默认）| 向量

您给出开通损耗和
关断损耗时所对应的温度值。

#### 依赖关系

要启用此参数，请将 **On-state behavior and
switching losses** 设置为
`Tabulate`。

### **Anode-cathode current vector for switching losses, Iak** — 开关损耗阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 非负标量向量

您给出开通损耗和
关断损耗时所对应的阳极-阴极电流。第一个元素必须为零。

#### 依赖关系

要启用此参数，请将 **On-state behavior and
switching losses** 设置为
`Tabulate`。

### **Wait time before switch-on current measurement** — 测量通态电流之前的时间 `1e-4` `s`（默认）| 非负标量

记录通态电流之前等待的时间。

### 积分二极管

### **Integral protection diode** — 集成保护二极管 `External diode`（默认）| `Protection diode with no dynamics` | `Protection diode with charge dynamics`

晶闸管（分段线性）模块用于集成保护二极管的模型。请选择以下选项之一：

- `External diode` — 晶闸管（分段线性）不建模集成保护二极管。请使用外部二极管模块。
- `Diode with no dynamics` — 晶闸管（分段线性）模块使用与无动态特性二极管模块相同的方程来建模集成保护二极管。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — 晶闸管（分段线性）模块使用与带电荷动态特性二极管模块相同的方程来建模集成保护二极管。选择此选项可优先考虑详细的仿真结果。

### **Diode model** — 二极管模型 `Piecewise Linear`（默认）| `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 使用分段线性模型对二极管进行建模，如分段线性二极管中所述。
- `Tabulated I-V curve` — 使用表格化的正向偏置 I-V 数据加上固定的反向偏置关断电导。

#### 依赖关系

此参数仅在热端口暴露且 **Integral protection diode** 参数设置为 `Protection diode with no dynamics` 或 `Protection diode with charge dynamics` 时可见。

### **Table type** — 表格化函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

是将电流表示为温度和电压的函数，还是将电压表示为温度和电流的函数。

#### 依赖关系

此参数仅在热端口暴露且 **Integral protection diode** 参数设置为 `Protection diode with no dynamics` 或 `Protection diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时可见。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性梯度为 1/*R*on 所需的 `+` 和 `-` 模块端口之间的最小电压，其中 *R*on 是 **On resistance** 参数的值。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）

高于 **Forward voltage** 参数值时电压随电流的变化率。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **Forward currents, If(Tj,Vf)** — 正向电流向量 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）| 非负向量

正向电流。此参数必须是至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Junction temperatures, Tj** — 结温向量 `[25, 125]` `degC`（默认）

结温向量。此参数必须是至少包含两个元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`。

### **Forward voltages, Vf** — 正向电压向量 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

正向电压向量。此参数必须是至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Forward voltages, Vf(Tj,If)** — 正向电压向量 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）| 非负向量

正向电压。此参数必须是至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Forward currents, If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

正向电流向量。此参数必须是至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖关系

此参数仅在 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics` 时可见。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认）| `Tabulated loss`

*自 R2023a 起*

是对固定反向恢复损耗还是表格化反向恢复损耗进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认）| 非负标量

*自 R2023a 起*

每次关断事件中耗散的能量。无论开关事件前后二极管的状态如何，模块都会耗散此能量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 随电流和电压缩放反向恢复损耗的选项 `On`（默认）| `Off`

*自 R2023b 起*

随电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Reverse recovery loss table, Erect(Tj), If** — 反向恢复损耗表 `zeros(2,3)` `J`（默认）| 非负标量向量

*自 R2023a 起*

作为开关事件前正向电流 *If* 以及二极管处于关断状态后的最终关断电压的函数的耗散能量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15 398.15]` `K`（默认）| 向量

*自 R2023a 起*

模块用于表格化反向恢复损耗的温度向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `K`（默认）| 非负标量向量

*自 R2023a 起*

模块用于表格化反向恢复损耗的正向电流向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current when measuring recovery loss, Irec** — 测量恢复损耗时的正向电流 `10` `A`（默认）| 正标量

*自 R2023b 起*

模块用于测量恢复损耗的反向恢复事件前通过二极管的正向电流。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认）| 正标量

*自 R2023a 起*

反向恢复事件后二极管两端的电压，模块使用该电压来测量恢复损耗。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认）| 正标量

*自 R2023a 起*

模块用于计算反向恢复损耗的电压和电流值的滤波时间常数。将此参数设置为小于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Junction capacitance** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认）| `Specify stretch factor` | `Specify reverse recovery charge`

确定在模块中如何指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需要指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认）| 标量

电流初始降至零（二极管关断时）与电流降至小于峰值反向电流 10% 之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery time directly` 时，此参数才可见。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify stretch factor` 时，此参数才可见。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery charge` 时，此参数才可见。

### **Diode turn-off voltage when measuring Erec** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认）

稳态时二极管两端的电压。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Stray inductance when measuring Erec** — 测量 Erec 时的杂散电感 `150` `nH`（默认）

测量电路中的总非预期电感。模块使用此值来计算 **Reverse recovery energy, Erec**。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Reverse recovery energy, Erec** — 反向恢复能量 `0.03` `J`（默认）

由二极管反向恢复引起的总开关损耗。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

有关这些参数的详细信息，请参阅 Diode。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### **Thermal network** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

模块热网络建模的选项。

### **Thermal mass parameterization** — 热质量参数化选项 `By thermal time constants`（默认）| `By thermal mass`

热质量的参数化选项：

- `By thermal time constants` — 以热时间常数来参数化热质量。
- `By thermal mass` — 直接指定热质量值。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[.08, .5]` `K/W`（默认）| 正值向量

由两个导热模块表示的两个热阻值的行向量 [ *R\_JC* *R\_CA* ]。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和壳热时间常数 `[.001, .2]` `s`（默认）| 正值向量

由两个热时间常数值组成的行向量 [ *t\_J* *t\_C* ]。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结和壳热质量 `[.01, .5]` `J/K`（默认）| 正值向量

由两个热质量值组成的行向量 [ *M\_J* *M\_C* ]。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结和壳初始温度 `[25, 25]` `degC`（默认）| 正值向量

由两个温度值组成的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.08,.1,.5]` `K/W` | `[.08,.14,.22,.16]` `K/W` | 正值向量

由 *n* 个热阻值组成的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.08,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.08,.14,.22,.16]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | 正值向量

由 *n* 个热质量值组成的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.01,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.001,.005,.05,.5]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

与模型中每个热容两端温差相对应的温度值行向量。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正值向量

由 *n* 个热时间常数值组成的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方式时，模块将热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.001,.1,.2]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[7e-05, .0007, .01, .08]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Initial node temperatures, [T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

从结开始每个节点的温度值行向量。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Junction thermal mass** — 结热质量 `0.01` `J/K`（默认）| 正标量

结的热质量。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `External`。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2023b：随电流和电压缩放反向恢复损耗

现在可以随电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **Scale reverse recovery loss with current and voltage** 参数。

在 R2023a 或更早版本中创建的模型默认不进行缩放，以保持向后兼容性。

### R2023a：关于集成二极管建模选项的更新

从 R2023a 开始，您可以在 Thyristor (Piecewise Linear) 模块中对反向恢复损耗进行建模。要启用 **Reverse recovery loss model** 参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 设置为 `Diode with no dynamics`。

### R2021a：移除能量耗散时间常数参数

从 R2021a 开始，Thyristor (Piecewise Linear) 模块的 **Energy dissipation time constant** 参数不再使用。结温的阶跃现在反映开关损耗。如果您的模型包含直接连接到此模块热端口的热质量，请将其移除，并在组件内部对热质量进行建模。

### R2020b：开关损耗和热建模选项的更新

从 R2020b 开始，Thyristor (Piecewise
Linear) 模块改进了损耗和热建模选项。

这些更改的结果如下：

- 电气和热导通态损耗现在始终相同。**Thermal loss dependent on** 参数及其选项 `Voltage and current` 和 `Voltage, current, and temperature` 已重命名为 **On-state behavior and switching losses**、`Specify constant values` 和 `Tabulate`：

  - 如果您为 **Thermal loss dependent on** 选择了 `Voltage and current`，则电气导通态损耗不变，其值由导通态电阻确定。但是，热导通态损耗现在也由导通态电阻确定。在 R2020b 之前，热导通态损耗由 **On-state voltage** 和 **Output current, Iout** 参数的乘积定义。
  - 如果您为 **Thermal loss dependent on** 选择了 `Voltage, current, and temperature`，则热导通态损耗不变，并且由 **On-state voltage, Vak(Tj,Iak)** 参数设置其值。但是，电气导通态损耗现在等于热导通态损耗。在 R2020b 之前，电气导通态损耗由导通态电阻的值定义。
- **On-state voltage** 和关断参数不再使用。

## 描述

Thyristor

Thyristor (Piecewise Linear) 模块对晶闸管进行建模。晶闸管的 I-V 特性使得如果栅极-阴极电压超过指定的栅极触发电压，晶闸管就会导通。如果负载电流降至指定的维持电流值以下，器件就会关断。

要定义晶闸管的 I-V 特性，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values` 或 `Tabulate`。仅当您暴露模块的热端口时，`Tabulate` 选项才可用。

在导通状态下，阳极-阴极路径的行为类似于具有正向电压降 *Vf* 和导通电阻 *Ron* 的线性二极管。但是，如果您暴露模块的热端口并使用表格化 I-V 数据对器件进行参数化，则表格化电阻是温度和电流的函数。

在关断状态下，阳极-阴极路径的行为类似于具有低关断态电导 *Goff* 的线性电阻。

该模块的定义 Simscape™ 方程为：

```
    if (v > Vf)&&((G>Vgt)||(i>Ih))
        i == (v - Vf*(1-Ron*Goff))/Ron;
    else
        i == v*Goff;
    end
```

其中：

- *v* 是阳极-阴极电压。
- *Vf* 是正向电压。
- *G* 是栅极电压。
- *Vgt* 是栅极触发电压。
- *i* 是阳极-阴极电流。
- *Ih* 是维持电流。
- *Ron* 是导通态电阻。
- *Goff* 是关断态电导。

使用模块对话框的 Integral Diode 选项卡，您可以包含一个集成阴极-阳极二极管。集成二极管通过为反向电流提供导电路径来保护半导体器件。当半导体器件突然切断向负载的电压供应时，感性负载可能会产生高反向电压尖峰。

下表显示了如何根据您的目标设置 **Integral protection diode** 参数。

| 目标 | 要选择的值 | 模块行为 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | 该模块包含 Diode 模块的集成副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |
| 精确指定反向模式电荷动态。 | `Diode with charge dynamics` | 该模块包含 Diode 模块动态模型的集成副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |

### 对栅极端口和热效应进行建模

您可以选择使用物理端口或电气端口来控制栅极端子，并暴露热端口以对开关事件和传导损耗产生的热量进行建模。要选择栅极控制端口，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。要暴露热端口，请将 **Modeling option** 参数设置为 `No thermal port` 或 `Show thermal port`。

有关使用热端口的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### Thermal Losses

开关损耗是半导体中热损耗的主要来源。在每次通断开关转换期间，晶闸管寄生效应会存储能量，然后耗散能量。

开关损耗取决于断态电压和通态电流。当开关器件导通时，功率损耗取决于器件两端的初始断态电压以及器件处于完全导通状态时的最终通态电流。

此模块通过将结温升高一个等于开关损耗除以结处总热质量的值来施加开关损耗。您必须指定单次开通事件期间耗散的能量。您还必须指定与所引用损耗相对应的断态电压和通态电流值。您可以根据所拥有的数据对开通损耗进行参数化。如果有表格数据，请使用表格数据。

- 要为开通损耗指定标量值，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values`。**Switch-on loss** 参数值设置开通损耗的大小。模块会根据断态电压和通态电流对该损耗进行缩放。
- 要将开通损耗指定为结温和通态电流的函数，请将 **On-state behavior and switching losses** 参数设置为 `Tabulate`。**Switch-on loss, Eon(Tj,Iak)** 参数设置损耗的大小。模块会根据断态电压对该损耗进行缩放。

当电流降至 **Holding current** 参数值以下时，器件关断。**Natural commutation rectification loss** 参数值定义关断损耗。模块不会根据断态电压或通态电流对该损耗进行缩放，因为对于整流损耗，无法知道何时测量起始电流或最终电压。

反向恢复损耗可能是二极管中热损耗的重要来源。二极管每次从导通状态关断到开路状态时都会耗散能量。要对反向恢复损耗建模：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。

如果将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`，则 **Reverse recovery loss table, Erec(Tj, If)** 参数的值指定了作为结温和开关事件前正向电流函数的耗散能量。断态电压会相对于 **Turn-off voltage when measuring recovery loss, Vrec** 参数值对损耗进行线性缩放。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage and current values** 参数设置为低于最快开关周期的值。

如果将 **Reverse recovery loss model** 参数设置为 `Fixed loss`，则 **Reverse recovery loss** 参数的值指定每次关断事件期间耗散的能量。如果选择 **Scale reverse recovery loss with current and voltage** 参数，则模块会根据通态电流和断态电压对该损耗值进行线性缩放。要使用接近瞬时值的缩放值，请将 **Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

作为反向恢复建模的另一种方法，您可以将 **Integral protection diode** 参数设置为 `Diode with charge dynamics`。但是，与使用第一种方法相比，此方法需要更小的仿真时间步长。

**注意**

模块在仿真期间不知道开关事件后的电流，因此当电流大于保持电流的时间超过 **Wait time before switch-on current measurement** 参数指定的值后，模块会记录通态电流。类似地，模块会在器件开通时记录断态电压。因此，记录的仿真数据直到一个开关周期后才会向热网络报告开关损耗。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。

对于所有理想开关器件，记录的仿真数据会将热损耗报告为 `lastTurnOffLoss`、`lastTurnOnLoss` 和 `lastReverseRecoveryLoss`。对于 Thyristor (Piecewise Linear) 模块，`lastTurnOnLoss` 等于 **Natural commutation rectification loss** 参数值。这些变量以脉冲形式包含损耗，其幅度等于能量损耗。如果使用脚本对定义仿真周期内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录数据中提取导通损耗和开关损耗。

您还可以从记录仿真数据中的 `accumulatedSwitchingLosses` 变量访问累计的总开关损耗。此变量汇总到目前为止的所有开关损耗，包括二极管的反向恢复损耗。

记录仿真数据中的 `power_dissipated` 变量不包括开关损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆通态损耗。

如果使用表格数据对开关损耗或反向恢复损耗建模，请检查温度和电流是否在您指定的范围内。如果未定义真实的热模型，例如，如果结质量或从结到壳体的电导过小，则温度可能超出您指定的范围，导致模块将损耗外推到非物理值。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
