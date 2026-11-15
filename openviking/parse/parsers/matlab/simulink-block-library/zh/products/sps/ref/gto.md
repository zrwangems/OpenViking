---
type: simulink-block
title: 'GTO'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'gto'
documentation_source_path: 'ref/gto.html'
language: zh-CN
chinese_source: worker-translation
---

# GTO

## 端口

### 守恒

### **G** — 栅极端子电气

与栅极端子关联的端口。您可以将该端口设置为物理信号端口或电气端口。

### **A** — 阳极端子电气

与阳极端子关联的电气守恒端口。

### **K** — 阴极端子电气

与阴极端子关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 热端口可见性 `No thermal port` (默认) | `Show thermal port`

是否启用热端口。

### 主要

此表显示 **主要** 参数的可见性如何取决于您如何配置 **Modeling option** 和 **On-state behavior and switching losses** 参数。要了解如何阅读此表，请参阅参数依赖关系。

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

### **Gate-control port** — 是否指定物理或电气控制端口 `PS` (默认) | `Electrical`

是否为开关栅极指定物理或电气控制端口。

### **On-state behavior and switching losses** — 开关损耗数据的通态电流 `Specify constant values` (默认) | `Tabulate`

通态行为和开关损耗的参数化方法，指定为以下值之一：

- `Specify constant values` — 使用标量值指定输出电流、开通损耗和关断损耗数据。
- `Tabulate` — 使用向量指定输出电流和温度数据。使用矩阵指定开通损耗和关断损耗数据。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Gate trigger voltage, Vgt** — 栅极触发电压 `6` `V` (默认)

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 栅极关断电压 `-1` `V` (默认)

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Holding current** — 维持电流 `1` `A` (默认)

电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件也保持导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Forward voltage, Vf** — 正向电压 `0.8` `V` (默认)

为使器件 I-V 特性的斜率为 1/Ron，阳极端口和阴极端口之间所需的最小电压，其中 Ron 是 **On-state resistance** 的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **On-state resistance** — 通态电阻 `0.001` `Ohm` (默认)

高于正向电压时电压相对于电流的变化率。默认值为 `0.001`。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Off-state conductance** — 断态电导 `1e-5` `1/Ohm` (默认)

器件关断时的阳极-阴极电导。该值必须小于 1/*R*，其中 *R* 是 **On-state resistance** 的值。默认值为 `1e-5`。

#### 依赖关系

请参阅主要参数依赖关系表。

### **On-state voltage, Vak(Tj,Iak)** — 通态电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V` (默认) | matrix of nonnegative scalars

器件在触发导通状态下的电压降。此参数是温度和最终通态输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Temperature vector, Tj** — 温度值 `[298.15, 398.15]` `K` (默认) | vector

您据以给出通态电压的温度值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Anode-cathode current vector, Iak** — 阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (默认)

定义通态电压所用的阳极-阴极电流。第一个元素必须为零。使用向量量指定此参数。

#### 依赖关系

请参阅主要参数依赖关系表。

### 开关损耗

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J` (默认) | positive scalar

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Forced commutation switch-off loss** — 强制换相关断损耗 `17.14e-3` `J` (默认) | positive scalar

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Natural commutation rectification loss** — 自然换相整流损耗 `10e-3` `J` (默认) | positive scalar

当电流降至 **Holding current** 参数值以下且模块关断时适用的整流损耗。

### **Off-state voltage for switching loss data** — 损耗数据的断态电压 `300` `V` (默认) | positive scalar

器件在断态期间的输出电压。此值是您据以定义开通损耗和关断损耗数据的阻断电压。

### **On-state current for switching loss data** — 输出电流 `600` `A` (默认) | positive scalar

您据以定义开通损耗和关断损耗的输出电流。

**注意**

模块在栅极电压降至 **Gate trigger voltage, Vgt** 参数值以下时测量此参数。开通脉冲长于电流达到其最大值所需的时间。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Switch-on loss, Eon(Tj,Iak)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J` (默认) | matrix of nonnegative scalars

单次开通事件期间耗散的能量，是温度和最终通态输出电流的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Switch-off loss, Eoff(Tj,Iak)** — 关断损耗 `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J` (默认) | matrix of nonnegative scalars

单次关断事件期间耗散的能量，是温度和最终通态输出电流的函数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Temperature vector for switching losses, Tj** — 开关损耗的温度 `[298.15, 398.15]` `K` (默认) | vector

您据以给出开通损耗和关断损耗的温度值。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Anode-cathode current vector for switching losses, Iak** — 开关损耗的阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (默认) | vector of nonnegative scalars

您据以给出开通损耗和关断损耗的阳极-阴极电流。第一个元素必须为零。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Wait time before switch-on current measurement** — 开通电流测量前的等待时间 `0` `s` (默认) | nonnegative scalar

如果将 GTO 模块用作半控器件，则记录通态电流之前要等待的时间。如果将 GTO 模块用作全控器件，请将此参数设置为 `0`。

### **Use last on-state current from previous cycle for turn-on loss** — 使用上一周期最后一个通态电流计算开通损耗的选项 `Off` (默认) | `On`

*自 R2024a 起*

使用上一周期最后一个通态电流计算开通损耗的选项。

### **Use last off-state current from previous cycle for turn-offloss** — 使用上一周期最后一个断态电流计算关断损耗的选项 `Off` (默认) | `On`

*自 R2024a 起*

使用上一周期最后一个断态电流计算关断损耗的选项。

### 集成二极管

### **Integral protection diode** — 集成保护二极管 `External diode` (默认) | `Diode with no dynamics` | `Diode with charge dynamics`

GTO 模块用于集成保护二极管的模型。请选择以下选项之一：

- `External diode` — GTO 不对集成保护二极管建模。请使用外部 Diode 模块。
- `Diode with no dynamics` — GTO 模块使用与无动态 Diode 模块相同的方程对集成保护二极管建模。选择此选项可优先提高仿真速度。
- `Diode with charge dynamics` — GTO 模块使用与带电荷动态 Diode 模块相同的方程对集成保护二极管建模。选择此选项可优先获得详细仿真结果。

### **Diode model** — 二极管模型 `Piecewise Linear` (默认) | `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 为二极管使用分段线性模型，如 Piecewise Linear Diode 中所述。这是默认方法。
- `Tabulated I-V curve` — 使用表格化的正向偏置 I-V 数据加上固定的反向偏置断态电导。

#### 依赖关系

仅当暴露热端口且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics` 时，此参数才可见。

### **Table type** — 表格化函数 `Table in If(Tj,Vf) form` (默认) | `Table in Vf(Tj,If) form`

是将电流表格化为温度和电压的函数，还是将电压表格化为温度和电流的函数。

#### 依赖关系

仅当暴露热端口，且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时，此参数才可见。

### **Reverse I-V characteristics type** — 反向 I-V 特性类型 `Specify off conductance` (默认) | `Tabulate`

*自 R2024a 起*

是使用二极管断态电导指定反向 I-V 特性，还是通过将电流表格化为温度和电压的函数或将电压表格化为温度和电流的函数来指定。

#### 依赖关系

仅当暴露热端口，且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时，此参数才可见。

### **Forward voltage** — 正向电压 `0.8` `V` (默认)

为使二极管 I-V 特性的斜率为 1/*R*on，`+` 和 `-` 模块端口之间所需的最小电压，其中 *R*on 是 **On resistance** 参数的值。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **On resistance** — 导通电阻 `0.001` `Ohm` (默认)

高于 **Forward voltage** 参数值时电压相对于电流的变化率。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，请将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **Forward currents, If(Tj,Vf)** — 正向电流向量 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (默认) | nonnegative vector

正向电流。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Junction temperatures, Tj** — 结温向量 `[25, 125]` `degC` (默认)

结温向量。此参数必须为至少包含两个元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`。

### **Forward voltages, Vf** — 正向电压向量 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (默认)

正向电压向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Forward voltages, Vf(Tj,If)** — 正向电压向量 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (默认) | nonnegative vector

正向电压。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Forward currents, If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (默认)

正向电流向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Reverse currents, Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A` (默认) | nonnegative vector

*自 R2024a 起*

反向电流。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V curve`
- **Table type** 为 `Table in If(Tj,Vf) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Reverse voltages, Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V` (默认) | nonnegative vector

*自 R2024a 起*

反向电压向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V
  curve`
- **Table type** 为 `Table in If(Tj,Vf) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Reverse voltages, Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认）| 非负向量

*自 R2024a 起*

反向电压。此参数必须为包含至少三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V
  curve`
- **Table type** 为 `Table in Vf(Tj,If) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Reverse currents, Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）| 非负向量

*自 R2024a 起*

反向电流向量。此参数必须为包含至少三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **Modeling option** 为 `Show thermal port`
- **Integral protection diode** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **Diode model** 为 `Tabulated I-V
  curve`
- **Table type** 为 `Table in Vf(Tj,If) form`
- **Reverse I-V characteristics** 为 `Tabulate`

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，且 **Reverse I-V characteristics type** 设置为 `Specify off conductance` 时，此参数才可见。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认）| `Tabulated loss`

*自 R2023a 起*

是建模固定反向恢复损耗还是表格化反向恢复损耗。

#### 依赖关系

要启用此参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认）| 非负标量

*自 R2023a 起*

每次关断事件中耗散的能量。无论二极管在开关事件之前或之后的状态如何，模块都会耗散此能量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 根据电流和电压缩放反向恢复损耗的选项 `On`（默认）| `Off`

*自 R2023b 起*

根据电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Reverse recovery loss table, Erect(Tj), If** — 反向恢复损耗 `zeros(2,3)` `J`（默认）| 非负标量向量

*自 R2023a 起*

耗散能量，表示为开关事件前正向电流 *If* 以及二极管进入关断状态后的最终关断状态电压的函数。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15 398.15]` `K`（默认）| 向量

*自 R2023a 起*

模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `K`（默认）| 非负标量向量

*自 R2023a 起*

模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current when measuring recovery loss, Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认）| 正标量

*自 R2023b 起*

反向恢复事件前通过二极管的正向电流，模块用它来测量恢复损耗。

#### 依赖关系

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选择 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认）| 正标量

*自 R2023a 起*

反向恢复事件后二极管两端的电压，模块用它来测量恢复损耗。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选择 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认）| 正标量

*自 R2023a 起*

电压和电流值的滤波时间常数，模块用它来计算反向恢复损耗。将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选择 **Scale reverse recovery loss with current and voltage** 参数。
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

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则指定一个值，模块用它来推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认）| 标量

电流最初变为零（二极管关断时）的时间与电流降至峰值反向电流的 10% 以下的时间之间的间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery time directly` 时，此参数才可见。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的更简单方法。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify stretch factor` 时，此参数才可见。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算反向恢复时间的反向恢复电荷。如果二极管器件的数据手册指定的是反向恢复电荷值而不是反向恢复时间值，则使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery charge` 时，此参数才可见。

### **Diode turn-off voltage when measuring Erec** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认）

稳态时二极管两端的电压。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Stray inductance when measuring Erec** — 测量 Erec 时的杂散电感 `150` `nH`（默认）

测量电路中的总非预期电感。模块使用此值计算 **Reverse recovery energy, Erec**。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Reverse recovery energy, Erec** — 反向恢复能量 `0.03` `J`（默认）

由二极管反向恢复引起的总开关损耗。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

有关这些参数的详细信息，请参阅 Diode。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅在半导体中模拟热效应。

### **Thermal network** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

模块热网络建模的选项。

### **Thermal mass parameterization** — 参数化热质量的选项 `By thermal time constants`（默认）| `By thermal mass`

参数化热质量的选项：

- `By thermal time constants` — 根据热时间常数参数化热质量。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[.08, .5]` `K/W`（默认）| 正值向量

行向量 [ *R\_JC* *R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和壳热时间常数 `[.001, .2]` `s`（默认）| 正值向量

行向量 [ *t\_J* *t\_C* ]，包含两个热时间常数值。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结和壳热质量 `[.01, .5]` `J/K`（默认）| 正值向量

行向量 [ *M\_J* *M\_C* ]，包含两个热质量值。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结和壳初始温度 `[25, 25]` `degC`（默认）| 正值向量

行向量 [ *T\_J* *T\_C* ]，包含两个温度值。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.08,.1,.5]` `K/W` | `[.08,.14,.22,.16]` `K/W` | 正值向量

*n* 个热阻值的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.08,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[.08,.14,.22,.16]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | 正值向量

*n* 个热质量值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.01,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[.001,.005,.05,.5]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **热质量初始温度，[T1 T2 … Tn]** — 热质量的初始温度 `[25, 25, 25]` `degC`（默认）| 正数值向量

行向量，包含与模型中每个热容两端温降对应的温度值。

#### 依赖项

要启用此参数，请将 **热网络** 设为 `Cauer model`。

### **热时间常数，[t1 t2 … tn]** — 热时间常数 `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正数值向量

*n* 个热时间常数值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **热阻，[R1 R2 … Rn]** 的长度匹配。使用此参数化时，模块按 `Mi = ti/Ri` 计算热质量，其中 `Mi`、`ti` 和 `Ri` 分别是第 *i* 个 Cauer 元件（如果将 **热网络** 设为 `Cauer model`）或 Foster 元件（如果将 **热网络** 设为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **热网络** 设为 `Cauer model`，则默认值为 `[.001,.1,.2]`。如果将 **热网络** 设为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[7e-05, .0007, .01, .08]`。

#### 依赖项

要启用此参数，请将 **热网络** 设为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **热质量参数化** 设为 `By thermal time constants`。

### **初始节点温度，[T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正数值向量

从结开始，每个节点的温度值的行向量。

#### 依赖项

要启用此参数，请将 **热网络** 设为 `Cauer model parameterized with Foster coefficients`。

### **结热质量** — 结的热质量 `0.01` `J/K`（默认）| 正标量

结的热质量。

#### 依赖项

要启用此参数，请将 **热网络** 设为 `External`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024a：对表格化反向 I-V 特性建模

现在，您可以通过将电流表示为温度和电压的函数，或将电压表示为温度和电流的函数，来为 GTO 模块的反向 I-V 特性建模。

在 R2024a 之前，只能通过指定反向偏置二极管的关断电导来为反向 I-V 特性建模。

### R2024a：确定不连续负载电流的开关损耗

GTO 模块现在支持不连续负载电流。

该模块通过在所有开通和关断事件处测量断态电压和通态电流来计算开关损耗，从而支持不连续负载电流。新模型默认采用此行为。如果使用固定步长求解器，器件最短的导通或关断周期现在为一个步长。在 R2024a 之前，最小周期为三个步长。要报告开关损耗，最小周期仍为三个步长。

在 R2024a 之前，该模块仅在开通前测量断态电压，并在关断前测量通态电流。

在 R2024a 中，您仍可使用原始方法，即在开通前测量断态电压，并在关断前测量通态电流。在 R2023b 或更早版本中创建的模型默认采用此行为，以实现向后兼容。原始方法专为具有连续电流的感性负载设计。如果您要对开关器件两端的电容或开关器件引线电感建模，请使用原始方法：

- 要对开关器件两端的电容建模，例如，如果并联二极管具有电容，或者您使用 Lauritzen 电荷模型，请选择 **使用上一周期的最后通态电流计算开通损耗** 参数。
- 要对开关器件引线电感建模，请选择 **使用上一周期的最后断态电压计算关断损耗** 参数。

### R2023b：根据电流和电压缩放反向恢复损耗

现在，您可以根据电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **根据电流和电压缩放反向恢复损耗** 参数。

在 R2023a 或更早版本中创建的模型默认不缩放，以实现向后兼容。

### R2023a：更新集成二极管建模选项

从 R2023a 开始，您可以在 GTO (Ideal, Switching) 模块中对反向恢复损耗建模。要启用 **反向恢复损耗模型** 参数，请将 **建模选项** 参数设为 `Show thermal port`，并将 **集成保护二极管** 参数设为 `Diode with no dynamics`。

### R2021a：移除能量耗散时间常数参数

从 R2021a 开始，GTO (Ideal, Switching) 模块的 **能量耗散时间常数** 参数不再使用。结温中的阶跃现在反映开关损耗。如果您的模型包含直接连接到该模块热端口的热质量，请将其移除，并在组件内部对热质量建模。

### R2020b：更新开关损耗和热建模选项

从 R2020b 开始，GTO (Ideal, Switching) 模块具有改进的损耗和热建模选项。

这些更改带来以下结果：

- 电气和热通态损耗现在始终相同。**热损耗取决于** 参数及其选项 `Voltage and current` 和 `Voltage, current, and temperature` 已重命名为 **导通状态行为和开关损耗**、`Specify constant values` 和 `Tabulate`：

  - 如果您为 **热损耗取决于** 选择了 `Voltage and current`，则电气通态损耗不变，其值由通态电阻确定。但是，热通态损耗现在也由通态电阻确定。在 R2020b 之前，热通态损耗由 **导通状态电压** 和 **输出电流，Iout** 参数的乘积定义。
  - 如果您为 **热损耗取决于** 选择了 `Voltage, current, and temperature`，则热通态损耗不变，其值由 **导通状态电压，Vak(Tj,Iak)** 参数设置。但是，电气通态损耗现在等于热通态损耗。在 R2020b 之前，电气通态损耗由通态电阻的值定义。
- **导通状态电压** 参数不再使用。

## 描述

门极关断晶闸管

GTO 模块对门极关断晶闸管（GTO）建模。GTO 的 I-V 特性使得：如果门极-阴极电压超过指定的门极触发电压，则 GTO 开通。如果门极-阴极电压降至指定的门极关断电压值以下，或者负载电流降至指定的保持电流值以下，则器件关断。

要定义 GTO 的 I-V 特性，请将 **导通状态行为和开关损耗** 参数设为 `Specify constant values` 或 `Tabulate`。仅当您暴露模块的热端口时，`Tabulate` 选项才可用。

在通态下，阳极-阴极路径的行为类似于具有正向电压降 *Vf* 和通态电阻 *Ron* 的线性二极管。但是，如果您暴露模块的热端口并使用表格化 I-V 数据参数化器件，则表格化电阻是温度和电流的函数。

在断态下，阳极-阴极路径的行为类似于具有低断态电导值 *Goff* 的线性电阻器。

该模块的定义 Simscape™ 方程为：

    if ((v > Vf)&&((G>Vgt)||(i>Ih)))&&(G>Vgt_off)
        i == (v - Vf*(1-Ron*Goff))/Ron;
    else
        i == v*Goff;
    end

其中：

- *v* 是阳极-阴极电压。
- *Vf* 是正向电压。
- *G* 是门极电压。
- *Vgt* 是门极触发电压。
- *i* 是阳极-阴极电流。
- *Ih* 是保持电流。
- *Vgt\_off* 是门极关断电压。
- *Ron* 是通态电阻。
- *Goff* 是断态电导。

使用 **集成二极管** 参数，您可以包含一个集成阴极-阳极二极管。包含集成阴极-阳极二极管的 GTO 称为非对称 GTO（A-GTO）或逆导 GTO（RCGTO）。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断向负载的电压供应时，感性负载可能产生高反向电压尖峰。

下表显示了如何根据您的目标设置 **集成保护二极管** 参数。

| 目标 | 要选择的值 | 模块行为 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | 该模块包含 Diode 模块的集成副本。要参数化内部 Diode 模块，请使用 **保护** 参数。 |
| 精确指定反向模式电荷动态。 | `Diode with charge dynamics` | 该模块包含 Diode 模块动态模型的集成副本。要参数化内部 Diode 模块，请使用 **保护** 参数。 |

### 对栅极端口和热效应建模

您可以选择物理端口或电气端口来控制栅极端子，并暴露热端口以对开关事件和导通损耗产生的热量建模。要选择栅极控制端口，请将 **栅极控制端口** 参数设为 `PS` 或 `Electrical`。要暴露热端口，请将 **建模选项** 参数设为 `No thermal port` 或 `Show thermal port`。

有关使用热端口的更多信息，请参阅“模拟半导体中的热效应”。

### 热损耗

该图显示了半导体器件的输出电压 *V*out 和输出电流 *I*out 的理想化表示。图中的区间包括整个第 *n* 个开关周期，在该周期内，模块先关断，然后开通。

开关损耗是半导体中热损耗的主要来源。在每次开-关开关转换期间，GTO 寄生参数存储能量，然后耗散能量。

开关损耗取决于断态电压和通态电流。当开关器件开通时，功率损耗取决于器件两端的初始断态电压以及器件完全处于通态时的最终通态电流。类似地，当开关器件关断时，功率损耗取决于流过器件的初始通态电流以及器件完全处于断态时器件两端的最终断态电压。

您可以选择何时测量模块用于计算开通损耗和关断损耗的电流和电压。对于大多数电路，您可以在开通或关断事件期间进行测量：

- 开通损耗为
  *E*on*(I*TurnOn*(n),V*TurnOn*(n))*
- 关断损耗为
  *E*off*(I*TurnOff*(n),V*TurnOff*(n))*

但是，您不能总是使用这些测量值，例如在以下情况下：

- 您正在对开关器件两端的电容建模。例如，您正在对带电容的保护二极管建模，或者您正在使用 Lauritzen 电荷模型。该电容会在器件开通时引起电流的过冲瞬态，这意味着您不能使用测量值 *I*TurnOn*(n)* 来计算开通损耗。模块需要瞬态之后的值。不要对开关器件两端的电容建模，因为此模型将半导体开关器件的抽象行为与二极管的详细物理特性混合在一起。如果必须对开关器件两端的电容建模，您可以使用最后一个通态周期结束时的电流测量值 *I*TurnOff*(n-1)*。要启用此选项，请选择 **Use last on-state current from previous cycle for turn-on loss** 参数。
- 您正在对开关器件引线电感建模。该电感会在器件关断时引起电压的过冲瞬态，这意味着您不能使用测量值 *V*TurnOff*(n)* 来计算关断损耗。模块需要瞬态之后的值。不要对开关器件引线电感建模，因为与引线电感相关的时间常数通常远小于脉宽调制 (PWM) 周期。该较小的时间常数意味着仿真需要更小的仿真时间步，从而减慢仿真速度。如果必须对开关器件引线电感建模，请使用最后一个断态周期结束时的电压测量值 *V*TurnOn*(n)*。要启用此选项，请选择 **Use last off-state voltage from previous cycle for turn-off loss** 参数。

检查仿真结果，以确认损耗行为符合您的预期。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。下表定义了记录的仿真数据中与开关损耗计算相关的变量名称。

**用于计算开关损耗的电压和电流**

| 量 | 记录的仿真数据中的变量名 |
| --- | --- |
| *V*TurnOn | `zvOn` |
| *I*TurnOn | `ziOn` |
| *V*TurnOff | `zvOff` |
| *I*TurnOff | `ziOff` |

此模块通过将结温升高一个值来施加开关损耗，该值等于开关损耗除以结处的总热质量。您必须指定在单次开通和强制换相关断事件期间耗散的能量。您还必须指定引用损耗时对应的断态电压和通态电流值。您可以根据拥有的数据对开关损耗进行参数化。如果有表格数据，请使用表格数据。

- 要为开通损耗和强制换相关断损耗指定标量值，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values`。**Switch-on loss** 和 **Forced commutation switch-off loss** 参数值设置损耗的大小。模块按断态电压和通态电流缩放损耗。
- 要将开通损耗和强制换相关断损耗指定为结温和通态电流的函数，请将 **On-state behavior and switching losses** 参数设置为 `Tabulate`。**Switch-on loss, Eon(Tj,Iak)** 和 **Switch-off loss, Eoff(Tj,Iak)** 参数设置损耗的大小。模块按断态电压缩放损耗。

当电流降到 **Holding current** 参数值以下时，器件关断。**Natural commutation rectification loss** 参数值定义关断损耗。模块不按断态电压或通态电流缩放此损耗，因为无法知道何时测量整流损耗的起始电流或最终电压。

反向恢复损耗可能是二极管中热损耗的重要来源。二极管每次从导通状态关断到开路状态时都会耗散能量。要对反向恢复损耗建模：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。

如果将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`，则 **Reverse recovery loss table, Erec(Tj, If)** 参数的值将耗散能量指定为结温和开关事件前正向电流的函数。断态电压相对于 **Turn-off voltage when measuring recovery loss, Vrec** 参数值线性缩放损耗。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage and current values** 参数设置为低于最快开关周期的值。

如果将 **Reverse recovery loss model** 参数设置为 `Fixed loss`，则 **Reverse recovery loss** 参数的值指定每个关断事件期间耗散的能量。如果选择 **Scale reverse recovery loss with current and voltage** 参数，则模块按通态电流和断态电压线性缩放此损耗值。要使用接近瞬时值的缩放值，请将 **Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

作为对反向恢复建模的替代方法，您可以将 **Integral protection diode** 参数设置为 `Diode with charge dynamics`。但是，与使用第一种方法相比，此方法需要更小的仿真时间步。

**注意**

如果使用 GTO 模块作为半控器件，则一旦电流大于维持电流的时间超过 **Wait time before switch-on current measurement** 参数值，模块就会记录通态电流。

对于所有理想开关器件，记录的仿真数据将热损耗报告为 `lastTurnOffLoss`、`lastTurnOnLoss` 和 `lastReverseRecoveryLoss`。这些变量将损耗包含为脉冲，其幅度等于能量损耗。如果使用脚本对定义仿真周期内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录数据中提取导通损耗和开关损耗。

您还可以从记录的仿真数据中的 `accumulatedSwitchingLosses` 变量访问累计的总开关损耗。该变量对截至当前的所有开关损耗求和，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆通态损耗。

如果您使用固定步长求解器，支持捕获开关损耗的最短脉冲开或脉冲关为三个时间步长。如果脉冲短于三个步长，则模块不报告开关损耗。

如果您使用表格数据对开关损耗或反向恢复损耗建模，请检查温度和电流是否在您指定的范围内。如果您未定义真实的热模型，例如，如果结质量或从结到外壳的电导过小，则温度可能超出您指定的范围，导致模块将损耗外推到非物理值。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
