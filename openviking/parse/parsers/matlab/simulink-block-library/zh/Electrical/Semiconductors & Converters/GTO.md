---
type: simulink-block
title: 'GTO'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'gto'
documentation_source_path: 'ref/gto.html'
language: zh-CN
chinese_source: worker-translation
---

# GTO

## 端口
```yaml
ports:
- name: G
  summary: 门极端子电气端口
  direction: conserving
- name: A
  summary: 阳极端子电气端口
  direction: conserving
- name: K
  summary: 阴极端子电气端口
  direction: conserving
- name: H
  summary: 热端口热端口
  direction: conserving
```

### 守恒端口

### **G** — 门极端子电气端口

与门极端子关联的端口。您可以将该端口设置为物理信号端口或电气端口。

### **A** — 阳极端子电气端口

与阳极端子关联的电气守恒端口。

### **K** — 阴极端子电气端口

与阴极端子关联的电气守恒端口。

### **H** — 热端口热端口

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 热端口可见性 No thermal port（默认）| Show thermal port
  group: ''
- name: Gate-control port
  summary: 指定物理控制端口还是电气控制端口 PS（默认）| Electrical
  group: 主要参数
- name: On-state behavior and switching losses
  summary: 开关损耗数据的通态电流 Specify constant values（默认）| Tabulate
  group: 主要参数
- name: Gate trigger voltage, Vgt
  summary: 门极触发电压 6 V（默认）
  group: 主要参数
- name: Gate turn-off voltage, Vgt_off
  summary: 门极关断电压 -1 V（默认）
  group: 主要参数
- name: Holding current
  summary: 维持电流 1 A（默认）
  group: 主要参数
- name: Forward voltage, Vf
  summary: 正向电压 0.8 V（默认）
  group: 主要参数
- name: On-state resistance
  summary: 通态电阻 0.001 Ohm（默认）
  group: 主要参数
- name: Off-state conductance
  summary: 断态电导 1e-5 1/Ohm（默认）
  group: 主要参数
- name: On-state voltage, Vak(Tj,Iak)
  summary: 通态电压 [0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8] V（默认）| 非负标量矩阵
  group: 主要参数
- name: Temperature vector, Tj
  summary: 温度值 [298.15, 398.15] K（默认）| 向量
  group: 主要参数
- name: Anode-cathode current vector, Iak
  summary: 阳极-阴极电流向量 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）
  group: 主要参数
- name: Switch-on loss
  summary: 开通损耗 22.86e-3 J（默认）| 正标量
  group: 开关损耗
- name: Forced commutation switch-off loss
  summary: 强制换相关断损耗 17.14e-3 J（默认）| 正标量
  group: 开关损耗
- name: Natural commutation rectification loss
  summary: 自然换相整流损耗 10e-3 J（默认）| 正标量
  group: 开关损耗
- name: Off-state voltage for switching loss data
  summary: 损耗数据的断态电压 300 V（默认）| 正标量
  group: 开关损耗
- name: On-state current for switching loss data
  summary: 输出电流 600 A（默认）| 正标量
  group: 开关损耗
- name: Switch-on loss, Eon(Tj,Iak)
  summary: 开通损耗 [0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3 J（默认）|
    非负标量矩阵
  group: 开关损耗
- name: Switch-off loss, Eoff(Tj,Iak)
  summary: 关断损耗 [0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3 J（默认）|
    非负标量矩阵
  group: 开关损耗
- name: Temperature vector for switching losses, Tj
  summary: 开关损耗温度 [298.15, 398.15] K（默认）| 向量
  group: 开关损耗
- name: Anode-cathode current vector for switching losses, Iak
  summary: 开关损耗的阳极-阴极电流向量 [0, .1, 1, 5, 10, 20, 40, 70, 100] A（默认）| 非负标量向量
  group: 开关损耗
- name: Wait time before switch-on current measurement
  summary: 开通电流测量前的等待时间 0 s（默认）| 非负标量
  group: 开关损耗
- name: Use last on-state current from previous cycle for turn-on loss
  summary: 使用上一周期的最后通态电流计算开通损耗的选项 Off（默认）| On
  group: 开关损耗
- name: Use last off-state current from previous cycle for turn-offloss
  summary: 使用上一周期的最后断态电流计算关断损耗的选项 Off（默认）| On
  group: 开关损耗
- name: Integral protection diode
  summary: 集成保护二极管 External diode（默认）| Diode with no dynamics | Diode with charge dynamics
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
  summary: 正向电流向量 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认）
  group: 集成二极管
- name: Reverse currents, Ir(Tj,Vr)
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005] A（默认）|
    非负向量
  group: 集成二极管
- name: Reverse voltages, Vr
  summary: 反向电压向量 [10, 20, 40, 50, 70, 80, 100] V（默认）| 非负向量
  group: 集成二极管
- name: 反向电压，Vr(Tj,Ir)
  summary: 反向电压向量 [10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320] V（默认）| 非负向量
  group: 集成二极管
- name: 反向电流，Ir
  summary: 反向电流向量 [1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001] A（默认）| 非负向量
  group: 集成二极管
- name: 关断电导
  summary: 关断电导 1e-5 1/Ohm（默认）
  group: 集成二极管
- name: 反向恢复损耗模型
  summary: 反向恢复损耗模型 固定损耗（默认）| 表格化损耗
  group: 集成二极管
- name: 反向恢复损耗
  summary: 反向恢复损耗 0 J（默认）| 非负标量
  group: 集成二极管
- name: 随电流和电压缩放反向恢复损耗
  summary: 随电流和电压缩放反向恢复损耗的选项 开（默认）| 关
  group: 集成二极管
- name: 反向恢复损耗表，Erect(Tj), If
  summary: 反向恢复损耗 zeros(2,3) J（默认）| 非负标量向量
  group: 集成二极管
- name: 恢复损耗表的温度向量，Tj
  summary: 恢复损耗表的温度向量 [298.15 398.15] K（默认）| 向量
  group: 集成二极管
- name: 恢复损耗表的正向电流向量，If
  summary: 恢复损耗表的正向电流向量 [.1, 1, 10] K（默认）| 非负标量向量
  group: 集成二极管
- name: 测量恢复损耗时的正向电流，Irec
  summary: 模块测量恢复损耗时的正向电流 10 A（默认）| 正标量
  group: 集成二极管
- name: 测量恢复损耗时的关断电压，Vrec
  summary: 测量恢复损耗时的关断电压 10 V（默认）| 正标量
  group: 集成二极管
- name: 电压和电流值的滤波时间常数
  summary: 电压和电流值的滤波时间常数 1 / 1000 / 100 s（默认）| 正标量
  group: 集成二极管
- name: 结电容
  summary: 结电容 50e-9 F（默认）
  group: 集成二极管
- name: 峰值反向电流，iRM
  summary: 峰值反向电流 -235 A（默认）| 负标量
  group: 集成二极管
- name: 测量 iRM 时的初始正向电流
  summary: 测量 iRM 时的初始正向电流 300 A（默认）| 正标量
  group: 集成二极管
- name: 测量 iRM 时的电流变化率
  summary: 测量 iRM 时的电流变化率 -50A/μs（默认）| 负标量
  group: 集成二极管
- name: 反向恢复时间参数化
  summary: 反向恢复时间参数化 直接指定反向恢复时间（默认）| 指定拉伸因子 | 指定反向恢复电荷
  group: 集成二极管
- name: 反向恢复时间，trr
  summary: 反向恢复时间 15 μs（默认）| 标量
  group: 集成二极管
- name: 反向恢复时间拉伸因子
  summary: 反向恢复时间拉伸因子 3（默认）| 大于 1 的标量
  group: 集成二极管
- name: 反向恢复电荷，Qrr
  summary: 反向恢复电荷 1500 μAs（默认）
  group: 集成二极管
- name: 测量 Erec 时的二极管关断电压
  summary: 测量 Erec 时的二极管关断电压 -600 V（默认）
  group: 集成二极管
- name: 测量 Erec 时的杂散电感
  summary: 测量 Erec 时的杂散电感 150 nH（默认）
  group: 集成二极管
- name: 反向恢复能量，Erec
  summary: 反向恢复能量 0.03 J（默认）
  group: 集成二极管
- name: 热网络
  summary: 热网络建模选项 外部（默认）| 指定结温和壳温热参数 | Cauer 模型 | 使用 Foster 系数参数化的 Cauer 模型
  group: 热端口
- name: 热质量参数化
  summary: 热质量参数化选项 按热时间常数（默认）| 按热质量
  group: 热端口
- name: 结-壳温和壳温-环境（或壳温-散热器）热阻，[R_JC R_CA]
  summary: 结-壳温和壳温-环境（或壳温-散热器）热阻 [.08, .5] K/W（默认）| 正值向量
  group: 热端口
- name: 结温和壳温的热时间常数，[t_J t_C]
  summary: 结温和壳温的热时间常数 [.001, .2] s（默认）| 正值向量
  group: 热端口
- name: 结温和壳温的热质量，[M_J M_C]
  summary: 结温和壳温的热质量 [.01, .5] J/K（默认）| 正值向量
  group: 热端口
- name: 结温和壳温的初始温度，[T_J T_C]
  summary: 结温和壳温的初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: 热阻，[R1 R2 … Rn]
  summary: 热阻 [.08,.1,.5] K/W | [.08,.14,.22,.16] K/W | 正值向量
  group: 热端口
- name: 热质量，[M1 M2 … Mn]
  summary: 热质量 [.01,.1,.5] J/K | [.001,.005,.05,.5] J/K | 正值向量
  group: 热端口
- name: 热质量初始温度，[T1 T2 … Tn]
  summary: 热质量的初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: 热时间常数，[t1 t2 … tn]
  summary: 热时间常数 [.001,.1,.2] s | [7e-05, .0007, .01, .08] s | 正值向量
  group: 热端口
- name: 初始节点温度，[T1 T2 ... Tn]
  summary: 初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: 结热质量
  summary: 结的热质量 0.01 J/K（默认）| 正标量
  group: 热端口
```

### **Modeling option** — 热端口可见性 `No thermal port`（默认）| `Show thermal port`

是否启用热端口。

### 主要参数

下表显示了 **Main** 参数的可见性如何取决于您如何配置 **Modeling option** 和 **On-state behavior and switching losses** 参数。要了解如何阅读此表，请参阅参数依赖关系。

**主要参数依赖关系**

| 参数和选项 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Modeling option** | | | | | | | |
| *`No thermal port`* | | | | *`Show thermal port`* | | | |
| Gate-control port | | | | Gate-control port | | | |
| Gate trigger voltage, Vgt | | | | Gate trigger voltage, Vgt | | | |
| Gate turn-off voltage, Vgt\_off | | | | Gate turn-off voltage, Vgt\_off | | | |
| Holding current | | | | Holding current | | | |
| Forward voltage, Vf | | | | **On-state behavior and switching losses** | | | |
| *`Specify constant values`* | *`Tabulate`* | | |
| On-state resistance | | | | Forward voltage, Vf | On-state voltage, Vak(Tj,Iak) | | |
| Off-state conductance | | | | On-state resistance | Temperature vector, Tj | | |
| Off-state conductance | Anode-cathode current vector, Iak | | |
| Off-state conductance | | |

### **Gate-control port** — 指定物理控制端口还是电气控制端口 `PS`（默认）| `Electrical`

指定开关门极的控制端口是物理端口还是电气端口。

### **On-state behavior and switching losses** — 开关损耗数据的通态电流 `Specify constant values`（默认）| `Tabulate`

通态行为和开关损耗的参数化方法，指定为以下值之一：

- `Specify constant values` — 使用标量值指定输出电流、开通损耗和关断损耗数据。
- `Tabulate` — 使用向量指定输出电流和温度数据。使用矩阵指定开通损耗和关断损耗数据。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Gate trigger voltage, Vgt** — 门极触发电压 `6` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 门极关断电压 `-1` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Holding current** — 维持电流 `1` `A`（默认）

电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

使器件 I-V 特性斜率为 1/Ron 所需的阳极和阴极模块端口之间的最小电压，其中 Ron 为 **On-state resistance** 的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **On-state resistance** — 通态电阻 `0.001` `Ohm`（默认）

高于正向电压时电压随电流的变化率。默认值为 `0.001`。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Off-state conductance** — 断态电导 `1e-5` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。默认值为 `1e-5`。

#### 依赖关系

请参阅主要参数依赖关系表。

### **On-state voltage, Vak(Tj,Iak)** — 通态电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V`（默认）| 非负标量矩阵

器件在触发导通状态下的电压降。此参数是温度和最终通态输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Temperature vector, Tj** — 温度值 `[298.15, 398.15]` `K`（默认）| 向量

您给出通态电压时所对应的温度值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Anode-cathode current vector, Iak** — 阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）

定义通态电压所对应的阳极-阴极电流。第一个元素必须为零。使用向量量指定此参数。

#### 依赖关系

请参阅主要参数依赖关系表。

### 开关损耗

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Forced commutation switch-off loss** — 强制换相关断损耗 `17.14e-3` `J`（默认）| 正标量

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Natural commutation rectification loss** — 自然换相整流损耗 `10e-3` `J`（默认）| 正标量

当电流降至 **Holding current** 参数值以下且模块关断时适用的整流损耗。

### **Off-state voltage for switching loss data** — 损耗数据的断态电压 `300` `V`（默认）| 正标量

器件在断态期间的输出电压。此值是您定义开通损耗和关断损耗数据时的阻断电压。

### **On-state current for switching loss data** — 输出电流 `600` `A`（默认）| 正标量

您定义开通损耗和关断损耗时所对应的输出电流。

**注意**

模块在门极电压降至 **Gate trigger voltage, Vgt** 参数值以下时测量此参数。开通脉冲持续时间长于电流达到最大值所需的时间。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Switch-on loss, Eon(Tj,Iak)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 非负标量矩阵

单次开通事件期间耗散的能量，作为温度和最终通态输出电流的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Switch-off loss, Eoff(Tj,Iak)** — 关断损耗 `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J`（默认）| 非负标量矩阵

单次关断事件期间耗散的能量，作为温度和最终通态输出电流的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Temperature vector for switching losses, Tj** — 开关损耗温度 `[298.15, 398.15]` `K`（默认）| 向量

您给出开通损耗和关断损耗时所对应的温度值。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Anode-cathode current vector for switching losses, Iak** — 开关损耗的阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 非负标量向量

您给出开通损耗和关断损耗时所对应的阳极-阴极电流。第一个元素必须为零。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Wait time before switch-on current measurement** — 开通电流测量前的等待时间 `0` `s`（默认）| 非负标量

如果您将 GTO 模块用作半控器件，则在记录通态电流之前等待的时间。如果您将 GTO 模块用作全控器件，请将此参数设置为 `0`。

### **Use last on-state current from previous cycle for turn-on loss** — 使用上一周期的最后通态电流计算开通损耗的选项 `Off`（默认）| `On`

*自 R2024a 起*

使用上一周期的最后通态电流计算开通损耗的选项。

### **Use last off-state current from previous cycle for turn-offloss** — 使用上一周期的最后断态电流计算关断损耗的选项 `Off`（默认）| `On`

*自 R2024a 起*

使用上一周期的最后断态电流计算关断损耗的选项。

### 集成二极管

### **Integral protection diode** — 集成保护二极管 `External diode`（默认）| `Diode with no dynamics` | `Diode with charge dynamics`

GTO 模块用于集成保护二极管的模型。选择以下选项之一：

- `External diode` — GTO 不建模集成保护二极管。使用外部 Diode 模块。
- `Diode with no dynamics` — GTO 模块使用与无动态特性 Diode 模块相同的方程来建模集成保护二极管。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — GTO 模块使用与带电荷动态特性 Diode 模块相同的方程来建模集成保护二极管。选择此选项可优先考虑详细的仿真结果。

### **Diode model** — 二极管模型 `Piecewise Linear`（默认）| `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 使用分段线性模型建模二极管，如分段线性二极管所述。这是默认方法。
- `Tabulated I-V curve` — 使用表格化的正向偏置 I-V 数据加上固定的反向偏置断态电导。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics` 时，此参数才可见。

### **Table type** — 表格化函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

是将电流表格化为温度和电压的函数，还是将电压表格化为温度和电流的函数。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时，此参数才可见。

### **Reverse I-V characteristics type** — 反向 I-V 特性类型 `Specify off conductance`（默认）| `Tabulate`

*自 R2024a 起*

是通过使用二极管断态电导来指定反向 I-V 特性，还是通过将电流表格化为温度和电压的函数或将电压表格化为温度和电流的函数来指定。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时，此参数才可见。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性斜率为 1/*R*on 所需的 `+` 和 `-` 模块端口之间的最小电压，其中 *R*on 为 **On resistance** 参数的值。

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

### **Reverse currents, Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流。此参数必须是至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V curve`
- **Table type** 为 `Table in If(Tj,Vf) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Reverse voltages, Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压向量。此参数必须是至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **建模选项**为`显示热端口`
- **集成保护二极管**为`无动态特性二极管`或`具有电荷动态特性二极管`
- **二极管模型**为`表格化 I-V 曲线`
- **表格类型**为`If(Tj,Vf) 形式的表格`
- **反向 I-V 特性**为`制表`

### **反向电压，Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压。此参数必须是至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **建模选项**为`显示热端口`
- **集成保护二极管**为`无动态特性二极管`或`具有电荷动态特性二极管`
- **二极管模型**为`表格化 I-V 曲线`
- **表格类型**为`Vf(Tj,If) 形式的表格`
- **反向 I-V 特性**为`制表`

### **反向电流，Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流向量。此参数必须是至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **建模选项**为`显示热端口`
- **集成保护二极管**为`无动态特性二极管`或`具有电荷动态特性二极管`
- **二极管模型**为`表格化 I-V 曲线`
- **表格类型**为`Vf(Tj,If) 形式的表格`
- **反向 I-V 特性**为`制表`

### **关断电导** — 关断电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖关系

仅当**集成保护二极管**参数设置为`无动态特性二极管`或`具有电荷动态特性二极管`，且**反向 I-V 特性类型**设置为`指定关断电导`时，此参数才可见。

### **反向恢复损耗模型** — 反向恢复损耗模型 `固定损耗`（默认）| `表格化损耗`

*自 R2023a 起*

是否对固定或表格化反向恢复损耗进行建模。

#### 依赖关系

要启用此参数，请将**建模选项**参数设置为`显示热端口`，并将**集成保护二极管**参数设置为`无动态特性二极管`。

### **反向恢复损耗** — 反向恢复损耗 `0` `J`（默认）| 非负标量

*自 R2023a 起*

每次关断事件中耗散的能量。无论开关事件前后二极管的状态如何，该模块都会耗散此能量。

#### 依赖关系

要启用此参数，请将**反向恢复损耗模型**参数设置为`固定损耗`。

### **随电流和电压缩放反向恢复损耗** — 随电流和电压缩放反向恢复损耗的选项 `开`（默认）| `关`

*自 R2023b 起*

随电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数：

- 将**建模选项**设置为`显示热端口`。
- 将**集成保护二极管**设置为`无动态特性二极管`。
- 将**反向恢复损耗模型**设置为`固定损耗`。

### **反向恢复损耗表，Erect(Tj), If** — 反向恢复损耗 `zeros(2,3)` `J`（默认）| 非负标量向量

*自 R2023a 起*

作为开关事件前正向电流 *If* 以及二极管处于关断状态后最终关断电压的函数的耗散能量。

#### 依赖关系

要启用此参数，请将**反向恢复损耗模型**参数设置为`表格化损耗`。

### **恢复损耗表的温度向量，Tj** — 恢复损耗表的温度向量 `[298.15 398.15]` `K`（默认）| 向量

*自 R2023a 起*

该模块用于制表反向恢复损耗的温度向量。

#### 依赖关系

要启用此参数，请将**反向恢复损耗模型**参数设置为`表格化损耗`。

### **恢复损耗表的正向电流向量，If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `K`（默认）| 非负标量向量

*自 R2023a 起*

该模块用于制表反向恢复损耗的正向电流向量。

#### 依赖关系

要启用此参数，请将**反向恢复损耗模型**参数设置为`表格化损耗`。

### **测量恢复损耗时的正向电流，Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认）| 正标量

*自 R2023b 起*

模块用于测量恢复损耗的反向恢复事件之前流过二极管的正向电流。

#### 依赖关系

要启用此参数，请将**反向恢复损耗模型**设置为`固定损耗`，并选中**随电流和电压缩放反向恢复损耗**参数。

### **测量恢复损耗时的关断电压，Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认）| 正标量

*自 R2023a 起*

模块用于测量恢复损耗的反向恢复事件之后二极管两端的电压。

#### 依赖关系

要启用此参数，请从以下选项中选择：

- 将**反向恢复损耗模型**设置为`固定损耗`，并选中**随电流和电压缩放反向恢复损耗**参数。
- 将**反向恢复损耗模型**参数设置为`表格化损耗`。

### **电压和电流值的滤波时间常数** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认）| 正标量

*自 R2023a 起*

模块用于计算反向恢复损耗的电压和电流值的滤波时间常数。将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择：

- 将**反向恢复损耗模型**设置为`固定损耗`，并选中**随电流和电压缩放反向恢复损耗**参数。
- 将**反向恢复损耗模型**参数设置为`表格化损耗`。

### **结电容** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`时，此参数才可见。

### **峰值反向电流，iRM** — 峰值反向电流 `-235` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`时，此参数才可见。

### **测量 iRM 时的初始正向电流** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`时，此参数才可见。

### **测量 iRM 时的电流变化率** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`时，此参数才可见。

### **反向恢复时间参数化** — 反向恢复时间参数化 `直接指定反向恢复时间`（默认）| `指定拉伸因子` | `指定反向恢复电荷`

确定如何在模块中指定反向恢复时间。默认值为 `直接指定反向恢复时间`。

如果选择`指定拉伸因子`或`指定反向恢复电荷`，则需要指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`时，此参数才可见。

### **反向恢复时间，trr** — 反向恢复时间 `15` `μs`（默认）| 标量

电流初始降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。**反向恢复时间，trr**参数的值必须大于**峰值反向电流，iRM**参数的值除以**测量 iRM 时的电流变化率**参数的值。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`，且**反向恢复时间参数化**参数设置为`直接指定反向恢复时间`时，此参数才可见。

### **反向恢复时间拉伸因子** — 反向恢复时间拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`，且**反向恢复时间参数化**参数设置为`指定拉伸因子`时，此参数才可见。

### **反向恢复电荷，Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据手册指定了反向恢复电荷的值而非反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为**峰值反向电流，iRM**指定的值。
- *a* 是为**测量 iRM 时的电流变化率**指定的值。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`，且**反向恢复时间参数化**参数设置为`指定反向恢复电荷`时，此参数才可见。

### **测量 Erec 时的二极管关断电压** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认）

稳态时二极管两端的电压。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`，且**反向恢复时间参数化**参数设置为`指定反向恢复能量`时，此参数才可见。

### **测量 Erec 时的杂散电感** — 测量 Erec 时的杂散电感 `150` `nH`（默认）

测量电路中的总非预期电感。模块使用此值来计算**反向恢复能量，Erec**。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`，且**反向恢复时间参数化**参数设置为`指定反向恢复能量`时，此参数才可见。

### **反向恢复能量，Erec** — 反向恢复能量 `0.03` `J`（默认）

由二极管反向恢复引起的总开关损耗。

#### 依赖关系

仅当**集成保护二极管**参数设置为`具有电荷动态特性二极管`，且**反向恢复时间参数化**参数设置为`指定反向恢复能量`时，此参数才可见。

有关这些参数的详细信息，请参阅二极管。

### 热端口

要启用这些参数，请将**建模选项**设置为`显示热端口`。

有关使用热端口和**热端口**参数的详细信息，请参阅半导体热效应仿真。

### **热网络** — 热网络建模选项 `外部`（默认）| `指定结温和壳温热参数` | `Cauer 模型` | `使用 Foster 系数参数化的 Cauer 模型`

模块热网络建模的选项。

### **热质量参数化** — 热质量参数化选项 `按热时间常数`（默认）| `按热质量`

热质量参数化选项：

- `按热时间常数` — 按热时间常数对热质量进行参数化。
- `按热质量` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将**热网络**设置为`指定结温和壳温热参数`、`Cauer 模型`或`使用 Foster 系数参数化的 Cauer 模型`。

### **结-壳温和壳温-环境（或壳温-散热器）热阻，[R\_JC R\_CA]** — 结-壳温和壳温-环境（或壳温-散热器）热阻 `[.08, .5]` `K/W`（默认）| 正值向量

行向量 [ *R\_JC* *R\_CA* ]，包含两个热阻值，由两个传导传热模块表示。第一个值 *R\_JC* 是结温与壳温之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件外壳之间的热阻。

#### 依赖关系

要启用此参数，请将**热网络**设置为`指定结温和壳温热参数`。

### **结温和壳温的热时间常数，[t\_J t\_C]** — 结温和壳温的热时间常数 `[.001, .2]` `s`（默认）| 正值向量

行向量 [ *t\_J* *t\_C* ]，包含两个热时间常数值。第一个值 *t\_J* 是结温时间常数。第二个值 *t\_C* 是壳温时间常数。

#### 依赖关系

要启用此参数，请将**热网络**设置为`指定结温和壳温热参数`，并将**热质量参数化**设置为`按热时间常数`。

### **结温和壳温的热质量，[M\_J M\_C]** — 结温和壳温的热质量 `[.01, .5]` `J/K`（默认）| 正值向量

行向量 [ *M\_J* *M\_C* ]，包含两个热质量值。第一个值 *M\_J* 是结温热质量。第二个值 *M\_C* 是壳温热质量。

#### 依赖关系

要启用此参数，请将**热网络**设置为`指定结温和壳温热参数`，并将**热质量参数化**设置为`按热质量`。

### **结温和壳温的初始温度，[T\_J T\_C]** — 结温和壳温的初始温度 `[25, 25]` `degC`（默认）| 正值向量

行向量 [ *T\_J* *T\_C* ]，包含两个温度值。第一个值 *T\_J* 是结温初始温度。第二个值 *T\_C* 是壳温初始温度。

#### 依赖关系

要启用此参数，请将**热网络**设置为`指定结温和壳温热参数`。

### **热阻，[R1 R2 … Rn]** — 热阻 `[.08,.1,.5]` `K/W` | `[.08,.14,.22,.16]` `K/W` | 正值向量

包含 *n* 个热阻值的行向量，由热网络中使用的 Cauer 元件表示。

如果将**热网络**设置为`Cauer 模型`，默认值为 `[.08,.1,.5]`。如果将**热网络**设置为`使用 Foster 系数参数化的 Cauer 模型`，默认值为 `[.08,.14,.22,.16]`。

#### 依赖关系

要启用此参数，请将**热网络**设置为`Cauer 模型`或`使用 Foster 系数参数化的 Cauer 模型`。

### **热质量，[M1 M2 … Mn]** — 热质量 `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | 正值向量

包含 *n* 个热质量值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将**热网络**设置为`Cauer 模型`，默认值为 `[.01,.1,.5]`。如果将**热网络**设置为`使用 Foster 系数参数化的 Cauer 模型`，默认值为 `[.001,.005,.05,.5]`。

#### 依赖关系

要启用此参数，请将**热网络**设置为`Cauer 模型`或`使用 Foster 系数参数化的 Cauer 模型`，并将**热质量参数化**设置为`按热质量`。

### **热质量初始温度，[T1 T2 … Tn]** — 热质量的初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

与模型中每个热容上的温度降相对应的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **热时间常数，[t1 t2 … tn]** — 热时间常数 `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正值向量

包含 *n* 个热时间常数值的行向量，其中 *n* 是热网络中的 Cauer 元件数量。此向量的长度必须与 **Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方式时，模块将热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.001,.1,.2]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[7e-05, .0007, .01, .08]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **初始节点温度，[T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

从结开始每个节点的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **结热质量** — 结的热质量 `0.01` `J/K`（默认）| 正标量

结的热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `External`。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024a：对表格化反向 I-V 特性建模

您现在可以通过将电流表示为温度和电压的函数，或将电压表示为温度和电流的函数，来为 GTO 模块的反向 I-V 特性建模。

在 R2024a 之前，您只能通过指定反偏二极管的关断电导来为反向 I-V 特性建模。

### R2024a：确定不连续负载电流的开关损耗

GTO 模块现在支持不连续负载电流。

该模块通过在所有开通和关断事件中测量断态电压和通态电流来计算开关损耗，从而支持不连续负载电流。新模型默认采用此行为。如果您使用定步长求解器，最短的器件开通或关断周期现在为一个步长。在 R2024a 之前，最小周期为三个步长。要报告开关损耗，最小周期仍为三个步长。

在 R2024a 之前，该模块仅在开通前测量断态电压，在关断前测量通态电流。

在 R2024a 中，您仍然可以使用原始方法，即在开通前测量断态电压，在关断前测量通态电流。您在 R2023b 或更早版本中创建的模型默认采用此行为以保持向后兼容性。原始方法专为具有连续电流的感性负载而设计。如果您要对开关器件两端的电容或开关器件引线电感建模，请使用原始方法：

- 要对开关器件两端的电容建模，例如，如果并联二极管具有电容，或者您使用的是 Lauritzen 电荷模型，请选择 **Use last on-state current from previous cycle for turn-on loss** 参数。
- 要对开关器件引线电感建模，请选择 **Use last off-state voltage from previous cycle for turn-off loss** 参数。

### R2023b：随电流和电压缩放反向恢复损耗

您现在可以随电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **Scale reverse recovery loss with current and voltage** 参数。

您在 R2023a 或更早版本中创建的模型默认不缩放，以保持向后兼容性。

### R2023a：关于集成二极管建模选项的更新

从 R2023a 起，您可以在 GTO (Ideal, Switching) 模块中为反向恢复损耗建模。要启用 **Reverse recovery loss model** 参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### R2021a：移除能量耗散时间常数参数

从 R2021a 起，GTO (Ideal, Switching) 模块的 **Energy dissipation time constant** 参数不再使用。结温的阶跃现在反映开关损耗。如果您的模型中包含直接连接到该模块热端口的热质量，请将其移除，并在组件内部对热质量建模。

### R2020b：关于开关损耗和热建模选项的更新

从 R2020b 起，GTO (Ideal, Switching) 模块具有改进的损耗和热建模选项。

这些更改的结果如下：

- 电气和热通态损耗现在始终相同。**Thermal loss dependent on** 参数及其选项 `Voltage and current` 和 `Voltage, current, and temperature` 已重命名为 **On-state behavior and switching losses**、`Specify constant values` 和 `Tabulate`：

  - 如果您为 **Thermal loss dependent on** 选择了 `Voltage and current`，则电气通态损耗保持不变，其值由通态电阻确定。但是，热通态损耗现在也由通态电阻确定。在 R2020b 之前，热通态损耗由 **On-state voltage** 和 **Output current, Iout** 参数的乘积定义。
  - 如果您为 **Thermal loss dependent on** 选择了 `Voltage, current, and temperature`，则热通态损耗保持不变，并由 **On-state voltage, Vak(Tj,Iak)** 参数设置其值。但是，电气通态损耗现在等于热通态损耗。在 R2020b 之前，电气通态损耗由通态电阻的值定义。
- **On-state voltage** 参数不再使用。

## 描述

门极关断晶闸管

GTO 模块对门极关断晶闸管（GTO）建模。GTO 的 I-V 特性使得如果门极-阴极电压超过指定的门极触发电压，则 GTO 开通。如果门极-阴极电压降至指定的门极关断电压值以下，或者如果负载电流降至指定的维持电流值以下，则器件关断。

要定义 GTO 的 I-V 特性，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values` 或 `Tabulate`。仅当您暴露模块的热端口时，`Tabulate` 选项才可用。

在通态下，阳极-阴极路径的行为类似于具有正向电压降 *Vf* 和通态电阻 *Ron* 的线性二极管。但是，如果您暴露模块的热端口并使用表格化 I-V 数据对器件进行参数化，则表格化电阻是温度和电流的函数。

在断态下，阳极-阴极路径的行为类似于具有低断态电导值 *Goff* 的线性电阻。

该模块的定义性 Simscape™ 方程为：

```
    if ((v > Vf)&&((G>Vgt)||(i>Ih)))&&(G>Vgt_off)
        i == (v - Vf*(1-Ron*Goff))/Ron;
    else
        i == v*Goff;
    end
```

其中：

- *v* 是阳极-阴极电压。
- *Vf* 是正向电压。
- *G* 是门极电压。
- *Vgt* 是门极触发电压。
- *i* 是阳极-阴极电流。
- *Ih* 是维持电流。
- *Vgt\_off* 是门极关断电压。
- *Ron* 是通态电阻。
- *Goff* 是断态电导。

使用 **Integral Diode** 参数，您可以包含一个集成阴极-阳极二极管。包含集成阴极-阳极二极管的 GTO 称为非对称 GTO（A-GTO）或逆导 GTO（RCGTO）。集成二极管通过为反向电流提供导电路径来保护半导体器件。当半导体器件突然切断负载的电压供应时，感性负载可能产生高反向电压尖峰。

下表显示了如何根据您的目标设置 **Integral protection diode** 参数。

| 目标 | 要选择的值 | 模块行为 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | 该模块包含 Diode 模块的集成副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |
| 精确指定反向模式电荷动态。 | `Diode with charge dynamics` | 该模块包含 Diode 模块动态模型的集成副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |

### 门极端口和热效应建模

您可以选择使用物理端口或电气端口来控制门极端子，并暴露热端口以对开关事件和传导损耗产生的热量建模。要选择门极控制端口，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。要暴露热端口，请将 **Modeling option** 参数设置为 `No thermal port` 或 `Show thermal port`。

有关使用热端口的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 热损耗

该图显示了半导体器件输出电压 *V*out 和输出电流 *I*out 的理想化表示。该图中的区间包含整个第 *n* 个开关周期，在此期间模块先关断然后导通。

开关损耗是半导体中热损耗的主要来源。在每次开-关开关转换期间，GTO 寄生参数会存储能量，然后耗散能量。

开关损耗取决于断态电压和通态电流。当开关器件导通时，功率损耗取决于器件两端的初始断态电压以及器件处于完全导通状态时的最终通态电流。类似地，当开关器件关断时，功率损耗取决于流过器件的初始通态电流以及器件处于完全关断状态时器件两端的最终断态电压。

您可以选择何时测量模块用于计算开通损耗和关断损耗的电流和电压。对于大多数电路，您可以在开通或关断事件期间进行测量：

- 开通损耗为
  *E*on*(I*TurnOn*(n),V*TurnOn*(n))*
- 关断损耗为
  *E*off*(I*TurnOff*(n),V*TurnOff*(n))*

但是，您不能总是使用这些测量值，例如，在以下情况下：

- 您正在对开关器件两端的电容进行建模。例如，您正在对带电容的保护二极管进行建模，或者您正在使用 Lauritzen 电荷模型。该电容会导致器件开通时电流出现过冲瞬态，这意味着您不能使用测量值
  *I*TurnOn*(n)*
  来计算开通损耗。模块需要瞬态之后的值。不要对开关器件两端的电容进行建模，因为该模型将半导体开关器件的抽象行为与二极管的详细物理特性混合在一起。如果必须对开关器件两端的电容进行建模，可以使用最后一个导通周期结束时的电流测量值，
  *I*TurnOff*(n-1)*。
  要启用此选项，请选择 **Use last on-state current
  from previous cycle for turn-on loss** 参数。
- 您正在对开关器件引线电感进行建模。该电感会导致器件关断时电压出现过冲瞬态，这意味着您不能使用测量值
  *V*TurnOff*(n)*
  来计算关断损耗。模块需要瞬态之后的值。不要对开关器件引线电感进行建模，因为与引线电感相关的时间常数通常远小于脉宽调制 (PWM) 周期。这个较小的时间常数意味着仿真需要更小的仿真时间步长，从而减慢仿真速度。如果必须对开关器件引线电感进行建模，请使用最后一个关断周期结束时的电压测量值，
  *V*TurnOn*(n)*。
  要启用此选项，请选择 **Use last off-state voltage
  from previous cycle for turn-off loss** 参数。

检查仿真结果，以确认损耗行为符合您的预期。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。下表定义了记录的仿真数据中与开关损耗计算相关的变量名称。

**用于计算开关损耗的电压和电流**

| 量 | 记录的仿真数据中的变量名称 |
| --- | --- |
| *V*TurnOn | `zvOn` |
| *I*TurnOn | `ziOn` |
| *V*TurnOff | `zvOff` |
| *I*TurnOff | `ziOff` |

该模块通过将结温升高一个等于开关损耗除以结处总热质量的值来施加开关损耗。您必须指定在单次开通和强制换相关断事件期间耗散的能量。您还必须指定您据以给出损耗的相应断态电压和通态电流值。您可以根据所拥有的数据对开关损耗进行参数化。如果有表格数据，请使用表格数据。

- 要为开通损耗和强制换相关断损耗指定标量值，请将 **On-state behavior and switching
  losses** 参数设置为 `Specify constant
  values`。**Switch-on loss** 和
  **Forced commutation switch-off loss** 参数值设置损耗的大小。模块会按断态电压和通态电流对损耗进行缩放。
- 要将开通损耗和强制换相关断损耗指定为结温和通态电流的函数，请将
  **On-state behavior and switching losses** 参数设置为
  `Tabulate`。**Switch-on loss,
  Eon(Tj,Iak)** 和 **Switch-off loss,
  Eoff(Tj,Iak)** 参数设置损耗的大小。模块会按断态电压对损耗进行缩放。

当电流降至 **Holding current** 参数值以下时，器件关断。**Natural commutation rectification
loss** 参数值定义关断损耗。模块不会按断态电压或通态电流对该损耗进行缩放，因为对于整流损耗，无法知道何时测量起始电流或最终电压。

反向恢复损耗可能是二极管中热损耗的重要来源。二极管每次从导通状态关断到开路状态时都会耗散能量。要对反向恢复损耗进行建模：

- 将 **Modeling option** 设置为 `Show thermal
  port`。
- 将 **Integral protection diode** 设置为 `Diode with
  no dynamics`。

如果将 **Reverse recovery loss model** 参数设置为
`Tabulated loss`，则 **Reverse recovery
loss table, Erec(Tj, If)** 参数的值指定了作为结温和开关事件前正向电流函数的耗散能量。断态电压会相对于 **Turn-off
voltage when measuring recovery loss, Vrec** 参数值对损耗进行线性缩放。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage
and current values** 参数设置为低于最快开关周期的值。

如果将 **Reverse recovery loss model** 参数设置为
`Fixed loss`，则 **Reverse recovery
loss** 参数的值指定每次关断事件期间耗散的能量。如果选择 **Scale reverse recovery loss with current and voltage**
参数，则模块会按通态电流和断态电压对该损耗值进行线性缩放。要使用接近瞬时值的缩放值，请将
**Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

作为对反向恢复进行建模的另一种方法，您可以将 **Integral
protection diode** 参数设置为 `Diode with charge
dynamics`。但是，与使用第一种方法相比，这种方法需要更小的仿真时间步长。

**注意**

如果将 GTO 模块用作部分可控器件，则当电流大于保持电流的时间超过
**Wait time before switch-on current
measurement** 参数的值时，模块会记录通态电流。

对于所有理想开关器件，记录的仿真数据会将热损耗报告为 `lastTurnOffLoss`、
`lastTurnOnLoss` 和
`lastReverseRecoveryLoss`。这些变量以脉冲形式包含损耗，其幅度等于能量损耗。如果使用脚本对指定仿真周期内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和
`ee_getPowerLossTimeSeries`
函数从记录的数据中提取传导损耗和开关损耗。

您还可以从记录的仿真数据中的
`accumulatedSwitchingLosses` 变量访问累计的总开关损耗。该变量汇总截至目前的所有开关损耗，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆通态损耗。

如果您使用的是定步长求解器，则支持捕获开关损耗的最短导通脉冲或关断脉冲长度为三个时间步。如果脉冲短于三个步长，模块不会报告开关损耗。

如果使用表格数据对开关损耗或反向恢复损耗进行建模，请检查温度和电流是否在您指定的范围内。如果您没有定义现实的热模型，例如，如果结质量或从结到壳体的电导过小，则温度可能超出您指定的范围，导致模块将损耗外推到非物理值。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property
Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal
Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
