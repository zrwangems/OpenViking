---
type: simulink-block
title: 'MOSFET (Ideal, Switching)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'mosfetidealswitching'
documentation_source_path: 'ref/mosfetidealswitching.html'
language: zh-CN
chinese_source: worker-translation
---

# MOSFET (Ideal, Switching)

## 端口
```yaml
ports:
- name: G
  summary: 栅极端子电气
  direction: conserving
- name: S
  summary: 源极端子电气
  direction: conserving
- name: D
  summary: 漏极端子电气
  direction: conserving
- name: H
  summary: 热端口热
  direction: conserving
- name: HDiode
  summary: 集成保护二极管的热端口热
  direction: conserving
```

### 守恒端口

### **G** — 栅极端子电气

与栅极端子关联的端口。您可以将该端口设置为物理信号端口或电气端口。

### **S** — 源极端子电气

与源极端子关联的电气守恒端口。

### **D** — 漏极端子电气

与漏极端子关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HDiode** — 集成保护二极管的热端口热

*自 R2024b 起*

与集成保护二极管关联的热守恒端口。

#### 依赖关系

要启用此端口，请选中 **Separate thermal port for integral diode** 参数。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 热端口可见性 No thermal port（默认）| Show thermal port
  group: ''
- name: Gate-control port
  summary: 用于指定物理或电气控制端口的选项 PS（默认）| Electrical
  group: 主要
- name: On-state behavior and switching losses
  summary: 导通行为和开关损耗 Specify constant values（默认）| Tabulate
  group: 主要
- name: Drain-source on resistance, R_DS(on)
  summary: 漏源导通电阻 0.01 Ohm（默认）
  group: 主要
- name: Off-state conductance
  summary: 断态电导 1e-6 1/Ohm（默认）
  group: 主要
- name: Threshold voltage, Vth
  summary: 阈值电压 2 V（默认）
  group: 主要
- name: On-state voltage, Vds(Tj,Ids)
  summary: 导通电压 [0, 1.8, 3.2, 6, 10, 16; 0, 2, 5.5, 9.5, 15, 25] V（默认）| 非负标量矩阵
  group: 主要
- name: Temperature vector, Tj
  summary: 温度值 [298.15, 448.15] K（默认）
  group: 主要
- name: Drain-source current vector, Ids
  summary: 漏源电流向量 [0, 20, 40, 60, 80, 100] A（默认）
  group: 主要
- name: Switch-on loss
  summary: 开通损耗 22.86e-3 J（默认）| 正标量
  group: 开关损耗
- name: Switch-off loss
  summary: 关断损耗 17.14e-3 J（默认）| 正标量
  group: 开关损耗
- name: Off-state Vds voltage for switching loss data
  summary: 开关损耗数据的断态漏源电压 300 V（默认）| 正标量
  group: 开关损耗
- name: On-state current for switching loss data
  summary: 开关损耗数据的导通电流 600 A（默认）| 正标量
  group: 开关损耗
- name: Use last on-state current from previous cycle for turn-on loss
  summary: 使用前一周期最后一个导通电流计算开通损耗的选项 Off（默认）| On
  group: 开关损耗
- name: Use last off-state voltage from previous cycle for turn-off loss
  summary: 使用前一周期最后一个断态电压计算关断损耗的选项 Off（默认）| On
  group: 开关损耗
- name: Switch-on loss, Eon(Tj,Ids)
  summary: 开通损耗 [0, 55.04, 124.57, 235.53, 362.12; 0, 71.25, 161.25, 304.88, 468.75] * 1e-6 J（默认）| 非负标量矩阵
  group: 开关损耗
- name: Switch-off loss, Eoff(Tj,Ids)
  summary: 关断损耗 [0, 18, 30, 56.1, 76.5; 0, 22.5, 37.5, 70.13, 95.63] * 1e-6 J（默认）| 非负标量矩阵
  group: 开关损耗
- name: Temperature vector for switching losses, Tj
  summary: 开关损耗的温度 [298.15, 448.15] K（默认）| 向量
  group: 开关损耗
- name: Drain-source current vector for switching losses, Ids
  summary: 开关损耗的漏源电流向量 [0, 10, 20, 30, 40] A（默认）| 非负标量向量
  group: 开关损耗
- name: Include switching loss tabulation with off-state Vds voltage
  summary: 使用断态漏源电压对开关损耗进行表格化的选项 Off（默认）| On
  group: 开关损耗
- name: Switch-on loss, Eon(Tj,Ids,Vds)
  summary: 开通损耗 [zeros(2, 5, 3)] J（默认）| 非负标量三维数组
  group: 开关损耗
- name: Switch-off loss, Eoff(Tj,Ids,Vds)
  summary: 关断损耗 [zeros(2, 5, 3)] J（默认）| 非负标量三维数组
  group: 开关损耗
- name: Off-state Vds voltage vector for switching loss data
  summary: 开关损耗数据的断态 Vds 电压向量 [0, 150, 300] V（默认）| 向量
  group: 开关损耗
- name: Integral protection diode
  summary: 保护二极管 Diode with no dynamics（默认）| External diode | Diode with charge dynamics
  group: 集成二极管
- name: Diode model
  summary: 二极管模型 Piecewise Linear（默认）| Tabulated I-V curve
  group: 集成二极管
- name: Table type
  summary: 表格化函数 Table in If(Tj,Vf) form（默认）| Table in Vf(Tj,If) form
  group: 集成二极管
- name: Reverse I-V characteristics type
  summary: 反向 I-V 特性类型 Specify off conductance（默认）| Tabulate
  group: 集成二极管
- name: Forward voltage
  summary: 正向电压 0.8 V（默认）
  group: 集成二极管
- name: On resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 集成二极管
- name: Forward currents, If(Tj,Vf)
  summary: 正向电流向量 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12] A（默认）| 非负向量
  group: 集成二极管
- name: Junction temperatures, Tj
  summary: 结温向量 [25, 125] degC（默认）
  group: 集成二极管
- name: Forward voltages, Vf
  summary: 正向电压向量 [.5, .7, .9, 1.3, 1.7, 2.1, 2.5] V（默认）
  group: 集成二极管
- name: Forward voltages, Vf(Tj,If)
  summary: 正向电压向量 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7] V（默认）| 非负向量
  group: 集成二极管
- name: Forward currents, If
  summary: 正向电流向量 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认值）
  group: 集成二极管
- name: Reverse currents, Ir(Tj,Vr)
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005] A（默认值）|
    非负向量
  group: 集成二极管
- name: Reverse voltages, Vr
  summary: 反向电压向量 [10, 20, 40, 50, 70, 80, 100] V（默认值）| 非负向量
  group: 集成二极管
- name: Reverse voltages, Vr(Tj,Ir)
  summary: 反向电压向量 [10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320] V（默认值）| 非负向量
  group: 集成二极管
- name: Reverse currents, Ir
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001] A（默认值）| 非负向量
  group: 集成二极管
- name: Off conductance
  summary: 关断电导 1e-5 1/Ohm（默认值）
  group: 集成二极管
- name: Reverse recovery loss model
  summary: 反向恢复损耗模型 Fixed loss（默认值）| Tabulated loss
  group: 集成二极管
- name: Reverse recovery loss
  summary: 反向恢复损耗 0 J（默认值）| 非负标量
  group: 集成二极管
- name: Scale reverse recovery loss with current and voltage
  summary: 使用电流和电压缩放反向恢复损耗的选项 On（默认值）| Off
  group: 集成二极管
- name: Reverse recovery loss table, Erect(Tj), If
  summary: 反向恢复损耗 zeros(2,3) J（默认值）| 非负标量向量
  group: 集成二极管
- name: Temperature vector for recovery loss table, Tj
  summary: 恢复损耗表的温度向量 [298.15 398.15] K（默认值）| 向量
  group: 集成二极管
- name: Forward current vector for recovery loss table, If
  summary: 恢复损耗表的正向电流向量 [.1, 1, 10] K（默认值）| 非负标量向量
  group: 集成二极管
- name: Forward current when measuring recovery loss, Irec
  summary: 测量恢复损耗时的正向电流 10 A（默认值）| 正标量
  group: 集成二极管
- name: Turn-off voltage when measuring recovery loss, Vrec
  summary: 测量恢复损耗时的关断电压 10 V（默认值）| 正标量
  group: 集成二极管
- name: Filter time constant for voltage and current values
  summary: 电压和电流值的滤波时间常数 1 / 1000 / 100 s（默认值）| 正标量
  group: 集成二极管
- name: Junction capacitance
  summary: 结电容 50e-9 F（默认值）
  group: 集成二极管
- name: Peak reverse current, iRM
  summary: 峰值反向电流 -235 A（默认值）| 负标量
  group: 集成二极管
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 300 A（默认值）| 正标量
  group: 集成二极管
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -50A/μs（默认值）| 负标量
  group: 集成二极管
- name: Reverse recovery time parameterization
  summary: 反向恢复时间参数化 Specify reverse recovery time directly（默认值）| Specify stretch factor | Specify reverse recovery charge
  group: 集成二极管
- name: Reverse recovery time, trr
  summary: 反向恢复时间 15 μs（默认值）| 标量
  group: 集成二极管
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认值）| 大于 1 的标量
  group: 集成二极管
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 μAs（默认值）
  group: 集成二极管
- name: Diode turn-off voltage when measuring Erec
  summary: 测量 Erec 时的二极管关断电压 -600 V（默认值）
  group: 集成二极管
- name: Stray inductance when measuring Erec
  summary: 测量 Erec 时的杂散电感 150 nH（默认值）
  group: 集成二极管
- name: Reverse recovery energy, Erec
  summary: 反向恢复能量 0.03 J（默认值）
  group: 集成二极管
- name: Separate thermal port for integral diode
  summary: 为集成二极管分离热端口的选项 off（默认值）| on
  group: 热端口
- name: Thermal network
  summary: 热网络建模选项 External（默认值）| Specify junction and case thermal parameters | Cauer model | Cauer model parameterized with
    Foster coefficients
  group: 热端口
- name: Thermal mass parameterization
  summary: 热质量参数化选项 By thermal time constants（默认值）| By thermal mass
  group: 热端口
- name: Junction case and case-ambient (or case-heatsink) thermal resistances, [R_JC R_CA]
  summary: 结-壳和壳-环境（或壳-散热器）热阻 [.03, .2] K/W（默认值）| 正值向量
  group: 热端口
- name: Junction and case thermal time constants, [t_J t_C]
  summary: 结和壳热时间常数 [.1, 5] s（默认值）| 正值向量
  group: 热端口
- name: Junction and case thermal masses, [M_J M_C]
  summary: 结和壳热质量 [3, 25] J/K（默认值）| 正值向量
  group: 热端口
- name: Junction and case initial temperatures, [T_J T_C]
  summary: 结温和壳温初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R_JC R_CA]
  summary: 集成二极管结-壳和壳-环境（或壳-散热器）热阻 [.03, .2] K/W（默认）| 正值向量
  group: 热端口
- name: Thermal time constants of diode junction and case, [t_J t_C]
  summary: 集成二极管结温和壳温的热时间常数 [.1, 5] s（默认）| 正值向量
  group: 热端口
- name: Thermal masses of diode junction and case, [M_J M_C]
  summary: 二极管结温和壳温的热质量 [3, 25] J/K（默认）| 正值向量
  group: 热端口
- name: Initial temperatures of diode junction and case, [T_J T_C]
  summary: 二极管结温和壳温的初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal resistances, [R1 R2 … Rn]
  summary: 热阻 [.03, .1, .2] K/W | [.03, .2] K/W | 正值向量
  group: 热端口
- name: Thermal time constants, [t1 t2 … tn]
  summary: 热时间常数 [.1, 1, 5] s | [1, 10] s | 正值向量
  group: 热端口
- name: Thermal masses, [M1 M2 … Mn]
  summary: 热质量 [3, 10, 25] J/K | [33, 50] J/K | 正值向量
  group: 热端口
- name: Thermal masses initial temperatures, [T1 T2 … Tn]
  summary: 热质量初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Diode thermal resistances, [R1 R2 … Rn]
  summary: 集成二极管热阻 [.03, .1, .2] K/W | [.03, .2] K/W | 正值向量
  group: 热端口
- name: Diode thermal time constants, [t1 t2 … tn]
  summary: 集成二极管热时间常数 [.1, 1, 5] s | [1, 10] s | 正值向量
  group: 热端口
- name: Diode thermal masses, [M1 M2 … Mn]
  summary: 集成二极管热质量 [3, 10, 25] J/K（默认）| [33, 50] J/K | 正值向量
  group: 热端口
- name: Initial temperatures of diode thermal masses, [T1 T2 … Tn]
  summary: 二极管热质量初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Initial node temperatures, [T1 T2 ... Tn]
  summary: 初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Diode initial node temperatures, [T1 T2 ... Tn]
  summary: 集成二极管初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Junction thermal mass
  summary: 结热质量 0.1 J/K（默认）| 正标量
  group: 热端口
- name: Diode junction thermal mass
  summary: 二极管结热质量 0.1 J/K（默认）| 正标量
  group: 热端口
```

### **Modeling option** — 热端口可见性 `No thermal port`（默认）| `Show thermal port`

是否启用热端口。

### 主要

此表显示了 **Main** 参数的可见性如何取决于您如何配置 **Modeling option** 和 **On-state behavior and switching losses** 参数。要了解如何阅读此表，请参阅参数依赖关系。

**主要参数依赖关系**

| 参数和选项 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Modeling option** | | | | | | | |
| *`No thermal port`* | | | | *`Show thermal port`* | | | |
| 栅极控制端口 | | | | 栅极控制端口 | | | |
| 漏源导通电阻，R\_DS(on) | | | | 阈值电压，Vth | | | |
| 断态电导 | | | | **On-state behavior and switching losses** | | | |
| *`Specify constant values`* | *`Tabulate`* | | |
| 阈值电压，Vth | | | | 漏源导通电阻，R\_DS(on) | 导通电压，Vds(Tj,Ids) | | |
| 断态电导 | 温度向量，Tj | | |
| 漏源电流向量，Ids | | |
| 断态电导 | | |

### **Gate-control port** — 用于指定物理或电气控制端口的选项 `PS`（默认）| `Electrical`

用于为开关栅极指定物理或电气控制端口的选项。

**注意**

如果将此参数设置为 `Electrical`，请与此模块一起使用内部或外部反向二极管。出于数值考虑，二极管的正向电压必须小于此模块的 **Threshold voltage, Vth** 参数值。

### **On-state behavior and switching losses** — 导通行为和开关损耗 `Specify constant values`（默认）| `Tabulate`

导通行为和开关损耗的参数化方法，指定为以下值之一：

- `Specify constant values` — 使用标量值指定输出电流、开通损耗和关断损耗数据。该模块假设单次开通或关断事件期间耗散的能量与断态电压和导通电流成线性关系。该模块还假设损耗与温度无关。
- `Tabulate` — 使用向量指定输出电流和温度数据。使用数组指定开通损耗和关断损耗数据。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Drain-source on resistance, R\_DS(on)** — 漏源导通电阻 `0.01` `Ohm`（默认）

器件导通时的漏源电阻。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Off-state conductance** — 断态电导 `1e-6` `1/Ohm`（默认）

器件关断时的漏源电导。该值必须小于 1/*R*，其中 *R* 是 **On-state resistance** 的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Threshold voltage, Vth** — 阈值电压 `2` `V`（默认）

栅源电压阈值。当栅源电压高于此值时，器件导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **On-state voltage, Vds(Tj,Ids)** — 导通电压 `[0, 1.8, 3.2, 6, 10, 16; 0, 2, 5.5, 9.5, 15, 25]` `V`（默认）| 非负标量矩阵

器件在触发导通状态下的电压降。此参数是温度和最终导通输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Temperature vector, Tj** — 温度值 `[298.15, 448.15]` `K`（默认）

对应于 **on-state voltage, Vds(Tj,Ids)** 参数的温度值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Drain-source current vector, Ids** — 漏源电流向量 `[0, 20, 40, 60, 80, 100]` `A`（默认）

定义导通电压所对应的漏源电流。第一个元素必须为零。使用向量量指定此参数。

#### 依赖关系

请参阅主要参数依赖关系表。

### 开关损耗

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Switch-off loss** — 关断损耗 `17.14e-3` `J`（默认）| 正标量

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Off-state Vds voltage for switching loss data** — 开关损耗数据的断态漏源电压 `300` `V`（默认）| 正标量

器件在断态期间的输出电压。此电压是您引用开通损耗和关断损耗时的阻断电压。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **On-state behavior and switching losses** 设置为 `Specify constant values`。
- 将 **On-state behavior and switching losses** 设置为 `Tabulate` 并清除 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **On-state current for switching loss data** — 开关损耗数据的导通电流 `600` `A`（默认）| 正标量

您定义开通损耗和关断损耗时所对应的输出电流。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Use last on-state current from previous cycle for turn-on loss** — 使用前一周期最后一个导通电流计算开通损耗的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用前一周期最后一个导通电流计算开通损耗的选项。

### **Use last off-state voltage from previous cycle for turn-off loss** — 使用前一周期最后一个断态电压计算关断损耗的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用前一周期最后一个断态电压计算关断损耗的选项。

### **Switch-on loss, Eon(Tj,Ids)** — 开通损耗 `[0, 55.04, 124.57, 235.53, 362.12; 0, 71.25, 161.25, 304.88, 468.75] * 1e-6` `J`（默认）| 非负标量矩阵

单次开通事件期间耗散的能量，作为温度和导通电流的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并清除 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Switch-off loss, Eoff(Tj,Ids)** — 关断损耗 `[0, 18, 30, 56.1, 76.5; 0, 22.5, 37.5, 70.13, 95.63] * 1e-6` `J`（默认）| 非负标量矩阵

单次关断事件期间耗散的能量，作为温度和导通电流的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并清除 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Temperature vector for switching losses, Tj** — 开关损耗的温度 `[298.15, 448.15]` `K`（默认）| 向量

您引用开通损耗和关断损耗时所对应的温度值。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Drain-source current vector for switching losses, Ids** — 开关损耗的漏源电流向量 `[0, 10, 20, 30, 40]` `A`（默认）| 非负标量向量

您引用开通损耗和关断损耗时所对应的漏源电流。第一个元素必须为 `0`。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Include switching loss tabulation with off-state Vds voltage** — 使用断态漏源电压对开关损耗进行表格化的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用断态漏源电压对开关损耗进行表格化的选项。

要使用导通漏源电流和温度对开通损耗和关断损耗进行表格化，请清除此参数。该模块假设损耗与断态漏源电压成线性关系。

要使用温度、导通漏源电流和断态漏源电压对开通损耗和关断损耗进行表格化，请选中此参数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Switch-on loss, Eon(Tj,Ids,Vds)** — 开通损耗 `[zeros(2, 5, 3)]` `J`（默认）| 非负标量三维数组

*自 R2023b 起*

单次开通事件期间耗散的能量，作为温度、导通漏源电流和断态漏源电压的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并选中 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Switch-off loss, Eoff(Tj,Ids,Vds)** — 关断损耗 `[zeros(2, 5, 3)]` `J`（默认）| 非负标量三维数组

*自 R2023b 起*

单次关断事件期间耗散的能量，作为温度、导通漏源电流和断态漏源电压的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并选中 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Off-state Vds voltage vector for switching loss data** — 开关损耗数据的断态 Vds 电压向量 `[0, 150, 300]` `V`（默认）| 向量

*自 R2023b 起*

您引用开通损耗和关断损耗时所对应的断态漏源电压。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并选中 **Include switching loss tabulation with off-state Vds voltage** 参数。

### 集成二极管

### **Integral protection diode** — 保护二极管 `Diode with no dynamics`（默认）| `External diode` | `Diode with charge dynamics`

MOSFET (Ideal, Switching) 模块用于集成保护二极管的模型。选择以下选项之一：

- `External diode` — MOSFET (Ideal, Switching) 不建模集成保护二极管。请使用外部 Diode 模块。
- `Diode with no dynamics` — MOSFET (Ideal, Switching) 模块使用与无动态特性 Diode 模块相同的方程来建模集成保护二极管。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — MOSFET (Ideal, Switching) 模块使用与具有电荷动态特性 Diode 模块相同的方程来建模集成保护二极管。选择此选项可优先考虑详细的仿真结果。

### **Diode model** — 二极管模型 `Piecewise Linear`（默认）| `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 使用分段线性二极管模型，如分段线性二极管中所述。这是默认方法。
- `Tabulated I-V curve` — 使用表格化的正向偏置 I-V 数据加上固定的反向偏置断态电导。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics` 时，此参数才可见。

### **Table type** — 表格化函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

选择将电流表格化为温度和电压的函数，或将电压表格化为温度和电流的函数。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时，此参数才可见。

### **Reverse I-V characteristics type** — 反向 I-V 特性类型 `Specify off conductance`（默认）| `Tabulate`

*自 R2024a 起*

是通过使用二极管断态电导来指定反向 I-V 特性，还是通过将电流表格化为温度和电压的函数或将电压表格化为温度和电流的函数来指定。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时，此参数才可见。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性梯度为 1/*R*on 所需的 `+` 和 `-` 模块端口两端的最小电压，其中 *R*on 是 **On resistance** 参数的值。

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

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Forward currents, If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认值）

正向电流向量。此参数必须是至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Reverse currents, Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认值）| 非负向量

*自 R2024a 起*

反向电流。此参数必须是至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V curve`
- **Table type** 为 `Table in If(Tj,Vf) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Reverse voltages, Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认值）| 非负向量

*自 R2024a 起*

反向电压向量。此参数必须是至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V curve`
- **Table type** 为 `Table in If(Tj,Vf) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Reverse voltages, Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认值）| 非负向量

*自 R2024a 起*

反向电压。此参数必须是至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V curve`
- **Table type** 为 `Table in Vf(Tj,If) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Reverse currents, Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认值）| 非负向量

*自 R2024a 起*

反向电流向量。此参数必须是至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V curve`
- **Table type** 为 `Table in Vf(Tj,If) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认值）

反向偏置二极管的电导。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，且 **Reverse I-V characteristics type** 设置为 `Specify off conductance` 时，此参数才可见。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认值）| `Tabulated loss`

*自 R2023a 起*

是否对固定或表格化的反向恢复损耗进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认值）| 非负标量

*自 R2023a 起*

每次关断事件中耗散的能量。无论开关事件前后二极管的状态如何，该模块都会耗散此能量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 使用电流和电压缩放反向恢复损耗的选项 `On`（默认值）| `Off`

*自 R2023b 起*

使用电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Reverse recovery loss table, Erect(Tj), If** — 反向恢复损耗 `zeros(2,3)` `J`（默认值）| 非负标量向量

*自 R2023a 起*

作为开关事件前正向电流 *If* 以及二极管处于关断状态后的最终关断电压的函数的耗散能量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15 398.15]` `K`（默认值）| 向量

*自 R2023a 起*

模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `K`（默认值）| 非负标量向量

*自 R2023a 起*

模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current when measuring recovery loss, Irec** — 测量恢复损耗时的正向电流 `10` `A`（默认值）| 正标量

*自 R2023b 起*

反向恢复事件前通过二极管的正向电流，模块使用该电流来测量恢复损耗。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认值）| 正标量

*自 R2023a 起*

反向恢复事件后二极管两端的电压，模块使用该电压来测量恢复损耗。

#### 依赖关系

要启用此参数，请从以下选项中选择：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认值）| 正标量

*自 R2023a 起*

模块用于计算反向恢复损耗的电压和电流值的滤波时间常数。将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选中 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Junction capacitance** — 结电容 `50e-9` `F`（默认值）

二极管结电容。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认值）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认值）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认值）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认值）| `Specify stretch factor` | `Specify reverse recovery charge`

确定如何在模块中指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需要指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认值）| 标量

电流初始降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery time directly` 时，此参数才可见。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认值）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间就越长。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify stretch factor` 时，此参数才可见。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认值）

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery charge` 时，此参数才可见。

### **Diode turn-off voltage when measuring Erec** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认值）

二极管处于稳态时的电压。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Stray inductance when measuring Erec** — 测量 Erec 时的杂散电感 `150` `nH`（默认值）

测量电路中的总非预期电感。模块使用此值来计算 **Reverse recovery energy, Erec**。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Reverse recovery energy, Erec** — 反向恢复能量 `0.03` `J`（默认值）

由二极管反向恢复引起的总开关损耗。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

有关这些参数的详细信息，请参阅 Diode。

### 热端口

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### **Separate thermal port for integral diode** — 为集成二极管分离热端口的选项 `off`（默认值）| `on`

*自 R2024b 起*

是否为器件的集成保护二极管分离热端口。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`，并在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Thermal network** — 热网络建模选项 `External`（默认值）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

模块热网络建模的选项。

### **Thermal mass parameterization** — 热质量参数化选项 `By thermal time constants`（默认值）| `By thermal mass`

热质量的参数化选项：

- `By thermal time constants` — 根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[.03, .2]` `K/W`（默认值）| 正值向量

行向量 [ *R\_JC* *R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和壳热时间常数 `[.1, 5]` `s`（默认值）| 正值向量

行向量 [ *t\_J* *t\_C* ]，包含两个热时间常数值。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结和壳热质量 `[3, 25]` `J/K`（默认值）| 正值向量

行向量 [ *M\_J* *M\_C* ]，包含两个热质量值。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结温和壳温初始温度 `[25, 25]` `degC`（默认）| 正值向量

由两个温度值组成的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结温初始温度。第二个值 *T\_C* 是壳温初始温度。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 集成二极管结-壳和壳-环境（或壳-散热器）热阻 `[.03, .2]` `K/W`（默认）| 正值向量

*自 R2024b 起*

由两个热阻值组成的行向量 [ *R\_JC* *R\_CA* ]，由两个 Conductive Heat Transfer 模块表示，用于集成保护二极管。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **HDiode** 与二极管壳之间的热阻。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal time constants of diode junction and case, [t\_J t\_C]** — 集成二极管结温和壳温的热时间常数 `[.1, 5]` `s`（默认）| 正值向量

*自 R2024b 起*

由两个热时间常数值组成的行向量 [ *t\_J* *t\_C* ]，用于集成保护二极管。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Thermal masses of diode junction and case, [M\_J M\_C]** — 二极管结温和壳温的热质量 `[3, 25]` `J/K`（默认）| 正值向量

*自 R2024b 起*

由两个热质量值组成的行向量 [ *M\_J* *M\_C* ]，用于集成保护二极管。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Initial temperatures of diode junction and case, [T\_J T\_C]** — 二极管结温和壳温的初始温度 `[25, 25]` `degC`（默认）| 正值向量

*自 R2024a 起*

由两个温度值组成的行向量 [ *T\_J* *T\_C* ]，用于集成保护二极管。第一个值 *T\_J* 是结温初始温度。第二个值 *T\_C* 是壳温初始温度。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.03, .1, .2]` `K/W` | `[.03, .2]` `K/W` | 正值向量

由 *n* 个热阻值组成的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.03, .1, .2]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.03, .2]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[.1, 1, 5]` `s` | `[1, 10]` `s` | 正值向量

由 *n* 个热时间常数值组成的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方式，模块将热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.1, 1, 5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[1, 10]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[3, 10, 25]` `J/K` | `[33, 50]` `J/K` | 正值向量

由 *n* 个热质量值组成的行向量，其中 n 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[3, 10, 25]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[33, 50]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

由温度值组成的行向量，对应于模型中每个热容上的温度降。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **Diode thermal resistances, [R1 R2 … Rn]** — 集成二极管热阻 `[.03, .1, .2]` `K/W` | `[.03, .2]` `K/W` | 正值向量

*自 R2024b 起*

由 *n* 个热阻值组成的行向量，用于集成保护二极管，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.03, .1, .2]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.03, .2]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Diode thermal time constants, [t1 t2 … tn]** — 集成二极管热时间常数 `[.1, 1, 5]` `s` | `[1, 10]` `s` | 正值向量

*自 R2024b 起*

由 *n* 个热时间常数值组成的行向量，用于集成保护二极管，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **Diode thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方式，模块将热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.1, 1, 5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[1, 10]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Diode thermal masses, [M1 M2 … Mn]** — 集成二极管热质量 `[3, 10, 25]` `J/K`（默认）| `[33, 50]` `J/K` | 正值向量

*自 R2024b 起*

由 *n* 个热质量值组成的行向量，用于集成保护二极管，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[3, 10, 25]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[33, 50]`。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Initial temperatures of diode thermal masses, [T1 T2 … Tn]** — 二极管热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

由温度值组成的行向量，用于集成保护二极管。此参数对应于模型中每个热容上的温度降。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model`。

### **Initial node temperatures, [T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

从结开始每个节点的温度值组成的行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Diode initial node temperatures, [T1 T2 ... Tn]** — 集成二极管初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

从集成保护二极管结开始每个节点的温度值组成的行向量。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Junction thermal mass** — 结热质量 `0.1` `J/K`（默认）| 正标量

结的热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `External`。

### **Diode junction thermal mass** — 二极管结热质量 `0.1` `J/K`（默认）| 正标量

*自 R2024b 起*

二极管结的热质量。

#### 依赖关系

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选中 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `External`。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b：集成二极管的独立热端口

您现在可以将 MOSFET (Ideal, Switching) 模块的集成保护二极管的热端口与 **H** 端口分开。要分离热端口：

- 将 **Modeling option** 参数设置为 `Show thermal port`
- 在 **Integral Diode** 部分中，将 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal port** 部分中，选中 **Separate thermal port for integral diode** 参数。

### R2024a：对表格化反向 I-V 特性建模

您现在可以通过将电流表示为温度和电压的函数，或将电压表示为温度和电流的函数，来对 MOSFET (Ideal, Switching) 模块的反向 I-V 特性进行建模。

在 R2024a 之前，您只能通过指定反向偏置二极管的关断电导来对反向 I-V 特性进行建模。

### R2023b：随电流和电压缩放反向恢复损耗

您现在可以随电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选中 **Scale reverse recovery loss with current and voltage** 参数。

在 R2023a 或更早版本中创建的模型默认不缩放，以保持向后兼容性。

### R2023b：随温度、电流和电压表格化开关损耗

您现在可以随温度、电流和电压表格化开关损耗。在更早的版本中，您只能随温度和电流表格化开关损耗。

要将损耗指定为结温、导通电流和关断电压的函数，请将 **On-state behavior and switching losses** 参数设置为 `Tabulate`，并选中 **Include switching loss tabulation with off-state Vds voltage** 参数。

### R2023b：确定不连续负载电流的开关损耗

MOSFET (Ideal, Switching) 模块现在支持不连续负载电流。

该模块通过在所有开通和关断事件中测量断态电压和通态电流来计算开关损耗，从而支持不连续负载电流。新建模型默认采用此行为。如果使用定步长求解器，最短的器件开通或关断周期现在为一个步长。在 R2023b 之前，最短周期为三个步长。要报告开关损耗，最短周期仍为三个步长。

在 R2023b 之前，该模块仅在开通前测量断态电压，在关断前测量通态电流。

在 R2023b 中，您仍然可以使用原始方法，即在开通前测量断态电压，在关断前测量通态电流。在 R2023a 或更早版本中创建的模型默认采用此行为以实现向后兼容。原始方法专为具有连续电流的感性负载而设计。如果您要对开关器件两端的电容或开关器件引线电感进行建模，请使用原始方法：

- 要对开关器件两端的电容进行建模，例如，如果并联二极管具有电容，或者您使用的是 Lauritzen 电荷模型，请选择 **Use last on-state current from previous cycle for turn-on loss** 参数。
- 要对开关器件引线电感进行建模，请选择 **Use last off-state voltage from previous cycle for turn-off loss** 参数。

### R2023b：绘制基本 I-V 特性

现在，您可以根据当前模块参数值绘制 MOSFET (Ideal, Switching) 模块的基本 I-V 特性，而无需仿真模型。

要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。

如果您使用集成保护二极管对开关器件进行建模，**Basic characteristics** 选项会同时绘制开关器件和二极管的 I-V 特性。如果您启用该模块的热端口，**Basic characteristics** 选项还会生成开通能量损耗和关断能量损耗作为通态电流和断态电压函数的曲面图。

### R2023a：更新集成二极管建模选项

从 R2023a 起，您可以在 MOSFET (Ideal, Switching) 模块中对反向恢复损耗进行建模。要启用 **Reverse recovery loss model** 参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### R2021a：移除能量耗散时间常数参数

从 R2021a 起，MOSFET (Ideal, Switching) 模块的 **Energy dissipation time constant** 参数不再使用。结温的阶跃变化现在反映开关损耗。如果您的模型包含直接连接到该模块热端口的热质量，请将其移除，并在组件内部对热质量进行建模。

### R2020b：更新开关损耗和热建模选项

从 R2020b 起，MOSFET (Ideal, Switching) 模块具有改进的损耗和热建模选项。

由于这些更改：

- 电气和热通态损耗现在始终相同。**Thermal loss dependent on** 参数及其选项 `Voltage and current` 和 `Voltage, current, and temperature` 已重命名为 **On-state behavior and switching losses**、`Specify constant values` 和 `Tabulate with temperature and current`：

  - 如果您为 **Thermal loss dependent on** 选择了 `Voltage and current`，则电气通态损耗不变，其值由通态电阻确定。但是，热通态损耗现在也由通态电阻确定。在 R2020b 之前，热通态损耗由 **On-state voltage** 和 **Output current, Iout** 参数的乘积定义。
  - 如果您为 **Thermal loss dependent on** 选择了 `Voltage, current, and temperature`，则热通态损耗不变，**On-state voltage, Vds(Tj,Ids)** 参数设置其值。但是，电气通态损耗现在等于热通态损耗。在 R2020b 之前，电气通态损耗由通态电阻的值定义。
- **On-state voltage** 参数不再使用。

## 描述

用于开关应用的理想 N 沟道 MOSFET

MOSFET (Ideal, Switching) 模块对 N 沟道金属氧化物半导体场效应晶体管 (MOSFET) 的理想开关行为进行建模。

N 沟道 MOSFET 的开关特性是：如果栅源电压超过指定的阈值电压，则 MOSFET 处于开通状态。否则，器件处于关断状态。下图显示了典型的 *i-v 特性*：

要定义 MOSFET 的 I-V 特性，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values` 或 `Tabulate`。仅当您暴露模块的热端口时，`Tabulate` 选项才可用。

在开通状态下，漏源路径表现为具有电阻 *Rds\_on* 的线性电阻。但是，如果您暴露模块的热端口并使用表格化 I-V 数据对器件进行参数化，则表格化电阻是温度和电流的函数。

在关断状态下，漏源路径表现为具有低断态电导 *Goff* 的线性电阻。

然后，该模块的定义 Simscape™ 方程为：

```
    if G > Vth       v == i*Rds_on;     else       v == i/Goff;     end
```

其中：

- *G* 取决于 **Gate-control port** 参数的值。

  - 如果您将 **Gate-control port** 参数设置为 `PS`，则通过物理信号控制栅极端子。*G* 是输入端口 **G** 处的值。
  - 如果您将 **Gate-control port** 参数设置为 `Electrical`，则通过电气信号控制栅极端子。*G* 等于：

    ```
        if v >= 0        G = G.v - S.v;     else       G = G.v - D.v;     end
    ```

    其中 *G.v* 是栅极电压，*S.v* 是源极电压，*D.v* 是漏极电压。
- *Vth* 是阈值电压。
- *v* 是漏源电压。
- *i* 是漏源电流。
- *Rds\_on* 是通态电阻。
- *Goff* 是断态电导。

使用 **Integral Diode** 设置，您可以包含体二极管或集成保护二极管。集成二极管为反向电流提供导通路径，并允许在模型中提高数值稳定性。例如，为半导体器件突然关断感性负载的电压电源时产生的高反向电压尖峰提供路径。

根据您的目标设置 **Integral protection diode** 参数。

| 目标 | | 要选择的值 | 集成保护二极管 |
| --- | --- | --- | --- |
| 不包含保护。 | | `External diode` | 无 |
| 包含保护。 | 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

### 栅极端口和热效应建模

您可以选择物理端口或电气端口来控制栅极端子，并暴露热端口来对开关事件和传导损耗产生的热量进行建模。要选择栅极控制端口，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。要暴露热端口，请将 **Modeling option** 参数设置为 `No thermal port` 或 `Show thermal port`。

您还可以通过选择 **Separate thermal port for integral diode** 参数来暴露集成保护二极管的热端口 **HDiode**。如果您不暴露二极管热端口，则器件和二极管共享公共热端口 **H**。*(自 R2024b 起)*

有关使用热端口的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### Thermal Losses

该图展示了半导体器件的输出电压 *V*out 和输出电流 *I*out 的理想化表示。图中的区间包含整个第 *n* 个开关周期，在此期间模块先关断然后导通。

开关损耗是半导体热损耗的主要来源。在每次通断开关转换期间，MOSFET 寄生效应先存储能量，然后耗散能量。

开关损耗取决于断态电压和通态电流。当开关器件导通时，功率损耗取决于器件两端的初始断态电压以及器件处于完全导通状态时的最终通态电流。类似地，当开关器件关断时，功率损耗取决于流过器件的初始通态电流以及器件处于完全关断状态时器件两端的最终断态电压。

您可以选择何时测量模块用于计算开通损耗和关断损耗的电流和电压。对于大多数电路，您可以在开通或关断事件期间进行测量：

- 开通损耗为
  *E*on*(I*TurnOn*(n),V*TurnOn*(n))*
- 关断损耗为
  *E*off*(I*TurnOff*(n),V*TurnOff*(n))*

然而，您并非总是可以使用这些测量值，例如在以下情况下：

- 您正在对开关器件两端的电容进行建模。例如，您正在对带电容的保护二极管进行建模，或者您正在使用 Lauritzen 电荷模型。该电容会在器件开通时引起电流的过冲瞬态，这意味着您不能使用测量值
  *I*TurnOn*(n)* 来计算开通损耗。模块需要瞬态之后的值。不要对开关器件两端的电容进行建模，因为此模型将半导体开关器件的抽象行为与二极管的详细物理特性混合在一起。
  如果必须对开关器件两端的电容进行建模，您可以使用最后一个导通周期结束时的电流测量值，
  *I*TurnOff*(n-1)*。要启用此选项，请选中 **Use last on-state current from previous cycle
  for turn-on loss** 参数。
- 您正在对开关器件引线电感进行建模。该电感会在器件关断时引起电压的过冲瞬态，这意味着您不能使用测量值
  *V*TurnOff*(n)* 来计算关断损耗。模块需要瞬态之后的值。
  不要对开关器件引线电感进行建模，因为与引线电感相关的时间常数通常远小于脉宽调制 (PWM) 周期。这个较小的时间常数意味着仿真需要更小的仿真时间步长，从而减慢仿真速度。如果必须对开关器件引线电感进行建模，请使用最后一个关断周期结束时的电压测量值，
  *V*TurnOn*(n)*。要启用此选项，请选中 **Use last off-state voltage from previous cycle for
  turn-off loss** 参数。

检查仿真结果，以确认损耗行为符合您的预期。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。下表定义了记录的仿真数据中与开关损耗计算相关的变量名称。

**用于计算开关损耗的电压和电流**

| 量 | 记录的仿真数据中的变量名称 |
| --- | --- |
| *V*TurnOn | `zvOn` |
| *I*TurnOn | `ziOn` |
| *V*TurnOff | `zvOff` |
| *I*TurnOff | `ziOff` |

此模块通过将结温升高一个等于开关损耗除以结处总热质量的值来施加开关损耗。您必须指定单次开通和关断事件期间耗散的能量。您还必须指定您引用损耗时所对应的断态电压和通态电流值。您可以根据所拥有的数据对开关损耗进行参数化。如果有表格数据，请使用表格数据。

- 要将开关损耗指定为标量值，请将 **On-state
  behavior and switching losses** 参数设置为 `Specify constant
  values`。**Switch-on loss** 和
  **Switch-off loss** 参数值设置开关损耗的大小。模块根据断态电压和通态电流对损耗进行缩放。
- 要将损耗指定为固定断态电压下结温和通态电流的函数，请将 **On-state behavior and
  switching losses** 参数设置为 `Tabulate` 并清除 **Include switching loss tabulation with off-state Vds
  voltage** 参数。**Switch-on loss, Eon(Tj,Ids)**
  和 **Switch-off, Eoff(Tj,Ids)** 参数设置损耗的大小。模块根据断态电压对损耗进行缩放。
- 要将损耗指定为结温、通态电流和断态电压的函数，请将 **On-state behavior and switching
  losses** 参数设置为 `Tabulate` 并选中
  **Include switching loss tabulation with off-state Vds voltage**
  参数。

反向恢复损耗可能是二极管中热损耗的重要来源。二极管每次从导通状态关断到开路状态时都会耗散能量。要对反向恢复损耗进行建模：

- 将 **Modeling option** 设置为 `Show thermal
  port`。
- 将 **Integral protection diode** 设置为 `Diode with
  no dynamics`。

如果您将 **Reverse recovery loss model** 参数设置为
`Tabulated loss`，则 **Reverse recovery
loss table, Erec(Tj, If)** 参数的值指定了作为结温和开关事件前正向电流函数的耗散能量。断态电压相对于 **Turn-off
voltage when measuring recovery loss, Vrec** 参数值线性缩放损耗。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage
and current values** 参数设置为低于最快开关周期的值。

如果您将 **Reverse recovery loss model** 参数设置为
`Fixed loss`，则 **Reverse recovery
loss** 参数的值指定了每次关断事件期间耗散的能量。如果您选中 **Scale reverse recovery loss with current and voltage**
参数，则模块根据通态电流和断态电压线性缩放此损耗值。要使用接近瞬时值的缩放值，请将
**Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

作为对反向恢复进行建模的替代方法，您可以将 **Integral
protection diode** 参数设置为 `Diode with charge
dynamics`。然而，与使用第一种方法相比，此方法需要更小的仿真时间步长。

**注意**

对于所有理想开关器件，记录的仿真数据将热损耗报告为 `lastTurnOffLoss`、`lastTurnOnLoss` 和
`lastReverseRecoveryLoss`。这些变量将损耗记录为幅度等于能量损耗的脉冲。如果您使用脚本对定义仿真周期内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。
或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录数据中提取导通损耗和开关损耗。

您还可以从记录的仿真数据中的
`accumulatedSwitchingLosses` 变量访问总累积开关损耗。
此变量汇总了迄今为止的所有开关损耗，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量
不包括开关损耗或反向恢复损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告
欧姆通态损耗。

如果您使用的是定步长求解器，支持捕获开关损耗的最短导通脉冲或关断脉冲为三个时间步长。如果脉冲短于三个步长，则模块不报告开关损耗。

如果您在反向区域操作 MOSFET（负漏源电流），记录的仿真数据不会报告任何开通或关断损耗，因为并联二极管提供连续的并联导通。在记录的仿真数据中，`ziOn` 报告零电流以实现零损耗，即使电流阶跃到负值也是如此。

如果您使用表格数据对开关损耗或反向恢复损耗进行建模，请检查温度、电流和电压是否在您指定的范围内。如果您没有定义实际的热模型，例如，如果结质量或从结到壳体的 conductance 太小，温度可能超出您指定的范围，导致模块将损耗外推到非物理值。

### Parameterization

MOSFET (Ideal, Switching) 模块支持多种预定义参数化。

使用此参数化数据来表示特定供应商的组件。这些 MOSFET 的参数化与制造商数据手册一致。要加载预定义参数化，请双击 MOSFET (Ideal, Switching)
模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择您要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用的数据源来获取参数值。工程判断和简化假设用于填补缺失数据。因此，预期仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预定义参数化的更多信息以及可用组件列表，请参阅 List of Pre-Parameterized Components。

您还可以使用 `ee_importDeviceParameters` 函数从 XML 文件中提取器件参数并将其导入模块。XML 文件必须位于 MATLAB® 路径上，并且必须使用 Hitachi 支持的参数化格式。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期幅度。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal
Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。

### Plot Basic I-V Characteristics

*Since R2023b*

您可以在不构建完整模型的情况下绘制 MOSFET (Ideal, Switching) 模块的基本 I-V 特性。使用这些图来探索您的参数选择对器件特性的影响。如果您从数据手册对模块进行参数化，您可以将图与数据手册进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整的工作模型但不知道使用哪个制造部件，您可以将图与数据手册进行比较以帮助您做出决定。

要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。

**Basic characteristics** 选项会根据您为 MOSFET (Ideal, Switching) 模块的 **Modeling option**、**On-state behavior and losses** 和 **Integral protection
diode** 参数指定的值生成不同的图。如果您使用集成保护二极管对开关器件进行建模，则 **Basic characteristics** 选项会绘制开关器件和二极管的 I-V 特性。如果您启用模块的热端口，则 **Basic characteristics** 选项还会生成开通能量损耗和关断能量损耗作为通态电流和断态电压函数的曲面图。有关此选项的更多信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
