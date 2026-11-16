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

要启用此端口，将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 热端口可见性 `No thermal port`（默认）| `Show thermal port`

是否启用热端口。

### 主参数

此表显示 **Main** 参数的可见性如何取决于您如何配置 **Modeling option** 和 **On-state behavior and switching losses** 参数。要了解如何读取此表，请参阅 Parameter Dependencies。

**主参数依赖关系**

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

### **Gate-control port** — 指定物理控制端口还是电气控制端口 `PS`（默认）| `Electrical`

是否为开关栅极指定物理控制端口或电气控制端口。

### **On-state behavior and switching losses** — 用于开关损耗数据的通态电流 `Specify constant values`（默认）| `Tabulate`

通态行为和开关损耗的参数化方法，指定为以下值之一：

- `Specify constant values` — 使用标量值指定输出电流、开通损耗和关断损耗数据。
- `Tabulate` — 使用向量指定输出电流和温度数据。使用矩阵指定开通损耗和关断损耗数据。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

器件导通时的正向电压。

#### 依赖关系

参见主参数依赖关系表。

### **On-state resistance** — 通态电阻 `0.001` `Ohm`（默认）

器件导通时的阳极-阴极电阻。

#### 依赖关系

参见主参数依赖关系表。

### **Off-state conductance** — 断态电导 `1e-5` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须小于 1/*R*，其中 *R* 是 **On-state resistance** 的值。

#### 依赖关系

参见主参数依赖关系表。

### **Gate trigger voltage, Vgt** — 栅极触发电压 `6` `V`（默认）

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

参见主参数依赖关系表。

### **Holding current** — 维持电流 `1` `A`（默认）

电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

参见主参数依赖关系表。

### **On-state voltage, Vak(Tj,Iak)** — 通态电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V`（默认）| 非负标量矩阵

器件处于触发导通状态时的电压降。此参数是温度和最终通态输出电流的函数。

#### 依赖关系

参见主参数依赖关系表。

### **Temperature vector, Tj** — 温度值 `[298.15, 398.15]` `K`（默认）| 向量

用于给出通态电压的温度值。

#### 依赖关系

参见主参数依赖关系表。

### **Anode-cathode current vector, Iak** — 阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）

定义通态电压所对应的阳极-阴极电流。第一个元素必须为零。使用向量量指定此参数。

#### 依赖关系

参见主参数依赖关系表。

### 开关损耗

要启用这些参数，将 **Modeling option** 设置为 `Show thermal port`。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Natural commutation rectification loss** — 自然换流整流损耗 `10e-3` `J`（默认）| 正标量

当电流降至 **Holding current** 参数值以下且模块关断时适用的整流损耗。

### **Off-state voltage for switching loss data** — 损耗数据的断态电压 `300` `V`（默认）| 正标量

器件在断态期间的输出电压。此值是您定义开通损耗和关断损耗数据时的阻断电压。

### **On-state current for switching loss data** — 输出电流 `600` `A`（默认）| 正标量

您定义开通损耗和关断损耗时的输出电流。

**注意**

模块在栅极电压降至 **Gate trigger voltage, Vgt** 参数值以下时测量此参数。开通脉冲持续时间长于电流达到其最大值所需的时间。

#### 依赖关系

要启用此参数，将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Switch-on loss, Eon(Tj,Iak)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 非负标量矩阵

单次开通事件期间耗散的能量，作为温度和最终通态输出电流的函数。

#### 依赖关系

要启用此参数，将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Temperature vector for switching losses, Tj** — 开关损耗温度 `[298.15, 398.15]` `K`（默认）| 向量

用于给出开通损耗和关断损耗的温度值。

#### 依赖关系

要启用此参数，将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Anode-cathode current vector for switching losses, Iak** — 开关损耗的阳极-阴极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 非负标量向量

用于给出开通损耗和关断损耗的阳极-阴极电流。第一个元素必须为零。

#### 依赖关系

要启用此参数，将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Wait time before switch-on current measurement** — 测量通态电流之前的等待时间 `1e-4` `s`（默认）| 非负标量

记录通态电流之前等待的时间。

### 集成二极管

### **Integral protection diode** — 集成保护二极管 `External diode`（默认）| `Protection diode with no dynamics` | `Protection diode with charge dynamics`

Thyristor (Piecewise Linear) 模块用于集成保护二极管的模型。选择以下选项之一：

- `External diode` — Thyristor (Piecewise Linear) 不对集成保护二极管建模。使用外部 Diode 模块。
- `Diode with no dynamics` — Thyristor (Piecewise Linear) 模块使用与 Diode 模块（无动态）相同的方程对集成保护二极管建模。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — Thyristor (Piecewise Linear) 模块使用与 Diode 模块（具有电荷动态）相同的方程对集成保护二极管建模。选择此选项可优先考虑详细仿真结果。

### **Diode model** — 二极管模型 `Piecewise Linear`（默认）| `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 使用二极管的分段线性模型，如 Piecewise Linear Diode 中所述。
- `Tabulated I-V curve` — 使用制表的正向偏置 I-V 数据加上固定的反向偏置断态电导。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Protection diode with no dynamics` 或 `Protection diode with charge dynamics` 时，此参数才可见。

### **Table type** — 制表函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

是将电流制表为温度和电压的函数，还是将电压制表为温度和电流的函数。

#### 依赖关系

仅当热端口暴露且 **Integral protection diode** 参数设置为 `Protection diode with no dynamics` 或 `Protection diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时，此参数才可见。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性的斜率为 1/*R*on 所需的跨 `+` 和 `-` 模块端口的最小电压，其中 *R*on 是 **On resistance** 参数的值。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）

高于 **Forward voltage** 参数值时的电压对电流的变化率。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **Forward currents, If(Tj,Vf)** — 正向电流向量 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）| 非负向量

正向电流。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Junction temperatures, Tj** — 结温向量 `[25, 125]` `degC`（默认）

结温向量。此参数必须为至少包含两个元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`。

### **Forward voltages, Vf** — 正向电压向量 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

正向电压向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Forward voltages, Vf(Tj,If)** — 正向电压向量 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）| 非负向量

正向电压。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Forward currents, If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

正向电流向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Off conductance** — 断态电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖关系

仅当 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认）| `Tabulated loss`

*自 R2023a 起*

是对固定的还是制表的反向恢复损耗建模。

#### 依赖关系

要启用此参数，将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认）| 非负标量

*自 R2023a 起*

每个关断事件中耗散的能量。无论开关事件之前或之后二极管的状态如何，模块都会耗散此能量。

#### 依赖关系

要启用此参数，将 **Reverse recovery loss model** 参数设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 按电流和电压缩放反向恢复损耗的选项 `On`（默认）| `Off`

*自 R2023b 起*

按电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Reverse recovery loss table, Erect(Tj), If** — 反向恢复损耗 `zeros(2,3)` `J`（默认）| 非负标量向量

*自 R2023a 起*

耗散能量，作为紧接开关事件之前的正向电流 *If* 以及二极管处于断态后的最终断态电压的函数。

#### 依赖关系

要启用此参数，将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15 398.15]` `K`（默认）| 向量

*自 R2023a 起*

模块用于制表反向恢复损耗的温度向量。

#### 依赖关系

要启用此参数，将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `K`（默认）| 非负标量向量

*自 R2023a 起*

模块用于制表反向恢复损耗的正向电流向量。

#### 依赖关系

要启用此参数，将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current when measuring recovery loss, Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认）| 正标量

*自 R2023b 起*

模块用于测量恢复损耗的、反向恢复事件之前流过二极管的正向电流。

#### 依赖关系

要启用此参数，将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选择 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认）| 正标量

*自 R2023a 起*

模块用于测量恢复损耗的、反向恢复事件之后二极管两端的电压。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **反向恢复损耗模型** 设置为
  `Fixed loss`，并选择 **随电流和电压缩放反向恢复损耗** 参数。
- 将 **反向恢复损耗模型** 参数设置为
  `Tabulated loss`。

### **电压和电流值的滤波时间常数** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认值）| 正标量

*自 R2023a 起*

用于模块计算反向恢复损耗时使用的电压和电流值的滤波时间常数。将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **反向恢复损耗模型** 设置为
  `Fixed loss`，并选择 **随电流和电压缩放反向恢复损耗** 参数。
- 将 **反向恢复损耗模型** 参数设置为
  `Tabulated loss`。

### **结电容** — 结电容 `50e-9` `F`（默认值）

二极管结电容。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **峰值反向电流，iRM** — 峰值反向电流 `-235` `A`（默认值）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **测量 iRM 时的初始正向电流** — 测量 iRM 时的初始正向电流 `300` `A`（默认值）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **测量 iRM 时的电流变化率** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认值）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **反向恢复时间参数化** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认值）| `Specify stretch factor` | `Specify reverse recovery charge`

确定在模块中指定反向恢复时间的方式。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需要指定一个值，模块使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **反向恢复时间，trr** — 反向恢复时间 `15` `μs`（默认值）| 标量

电流最初降为零（二极管关断时）与电流下降到峰值反向电流的 10% 以下之间的时间间隔。**反向恢复时间，trr** 参数的值必须大于 **峰值反向电流，iRM** 参数的值除以 **测量 iRM 时的电流变化率** 参数的值。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery time directly` 时，此参数才可见。

### **反向恢复时间拉伸因子** — 反向恢复时间拉伸因子 `3`（默认值）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。与指定反向恢复电荷相比，指定拉伸因子是更简便的反向恢复时间参数化方法。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，且 **反向恢复时间参数化** 参数设置为 `Specify stretch factor` 时，此参数才可见。

### **反向恢复电荷，Qrr** — 反向恢复电荷 `1500` `μAs`（默认值）

模块用于计算反向恢复时间的反向恢复电荷。如果二极管器件的数据手册指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **峰值反向电流，iRM** 指定的值。
- *a* 是为 **测量 iRM 时的电流变化率** 指定的值。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery charge` 时，此参数才可见。

### **测量 Erec 时的二极管关断电压** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认值）

稳态时二极管两端的电压。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **测量 Erec 时的杂散电感** — 测量 Erec 时的杂散电感 `150` `nH`（默认值）

测量电路中总的非预期电感。模块使用此值计算 **反向恢复能量，Erec**。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **反向恢复能量，Erec** — 反向恢复能量 `0.03` `J`（默认值）

由二极管反向恢复引起的总开关损耗。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

有关这些参数的详细信息，请参阅 Diode。

### 热端口

要启用这些参数，请将 **建模选项** 设置为 `Show thermal port`。

有关使用热端口和 **热端口** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### **热网络** — 热网络建模选项 `External`（默认值）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

用于对模块热网络进行建模的选项。

### **热质量参数化** — 用于参数化热质量的选项 `By thermal time constants`（默认值）| `By thermal mass`

用于参数化热质量的选项：

- `By thermal time constants` — 根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **结-壳和壳-环境（或壳-散热器）热阻，[R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[.08, .5]` `K/W`（默认值）| 正值向量

行向量 [ *R\_JC* *R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **结和壳热时间常数，[t\_J t\_C]** — 结和壳热时间常数 `[.001, .2]` `s`（默认值）| 正值向量

行向量 [ *t\_J* *t\_C* ]，包含两个热时间常数值。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`，并将 **热质量参数化** 设置为 `By thermal time constants`。

### **结和壳热质量，[M\_J M\_C]** — 结和壳热质量 `[.01, .5]` `J/K`（默认值）| 正值向量

行向量 [ *M\_J* *M\_C* ]，包含两个热质量值。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`，并将 **热质量参数化** 设置为 `By thermal mass`。

### **结和壳初始温度，[T\_J T\_C]** — 结和壳初始温度 `[25, 25]` `degC`（默认值）| 正值向量

行向量 [ *T\_J* *T\_C* ]，包含两个温度值。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **热阻，[R1 R2 … Rn]** — 热阻 `[.08,.1,.5]` `K/W` | `[.08,.14,.22,.16]` `K/W` | 正值向量

*n* 个热阻值的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[.08,.1,.5]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.08,.14,.22,.16]`。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **热质量，[M1 M2 … Mn]** — 热质量 `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | 正值向量

*n* 个热质量值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[.01,.1,.5]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.001,.005,.05,.5]`。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **热质量参数化** 设置为 `By thermal mass`。

### **热质量初始温度，[T1 T2 … Tn]** — 热质量的初始温度 `[25, 25, 25]` `degC`（默认值）| 正值向量

温度值行向量，对应于模型中每个热容两端的温度降。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Cauer model`。

### **热时间常数，[t1 t2 … tn]** — 热时间常数 `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正值向量

*n* 个热时间常数值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **热阻，[R1 R2 … Rn]** 的长度匹配。使用此参数化时，模块按 `Mi = ti/Ri` 计算热质量，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **热网络** 设置为 `Cauer model`）或 Foster 元件（如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[.001,.1,.2]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[7e-05, .0007, .01, .08]`。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **热质量参数化** 设置为 `By thermal time constants`。

### **初始节点温度，[T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认值）| 正值向量

从结开始的每个节点的温度值行向量。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`。

### **结热质量** — 结的热质量 `0.01` `J/K`（默认值）| 正标量

结的热质量。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `External`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2023b：随电流和电压缩放反向恢复损耗

现在可以随电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **随电流和电压缩放反向恢复损耗** 参数。

为保持向后兼容，在 R2023a 或更早版本中创建的模型默认不进行缩放。

### R2023a：集成二极管建模选项更新

从 R2023a 起，可以在 Thyristor (Piecewise Linear) 模块中对反向恢复损耗进行建模。要启用 **反向恢复损耗模型** 参数，请将 **建模选项** 参数设置为 `Show thermal port`，并将 **集成保护二极管** 设置为 `Diode with no dynamics`。

### R2021a：移除能量耗散时间常数参数

从 R2021a 起，不再使用 Thyristor (Piecewise Linear) 模块的 **能量耗散时间常数** 参数。结温中的阶跃现在反映开关损耗。如果模型包含直接连接到该模块热端口的热质量，请将其移除，并在组件自身内部对热质量进行建模。

### R2020b：开关损耗和热建模选项更新

从 R2020b 起，Thyristor (Piecewise Linear) 模块具有改进的损耗和热建模选项。

这些更改的结果如下：

- 电气和热导通状态损耗现在始终相同。**热损耗取决于** 参数及其选项 `Voltage and current` 和 `Voltage, current, and temperature` 已重命名为 **导通状态行为与开关损耗**、`Specify constant values` 和 `Tabulate`：

  - 如果为 **热损耗取决于** 选择了 `Voltage and current`，则电气导通状态损耗保持不变，其值由导通状态电阻确定。但是，热导通状态损耗现在也由导通状态电阻确定。在 R2020b 之前，热导通状态损耗由 **导通状态电压** 和 **输出电流，Iout** 参数的乘积定义。
  - 如果为 **热损耗取决于** 选择了 `Voltage, current, and temperature`，则热导通状态损耗保持不变，并由 **导通状态电压，Vak(Tj,Iak)** 参数设置其值。但是，电气导通状态损耗现在等于热导通状态损耗。在 R2020b 之前，电气导通状态损耗由导通状态电阻的值定义。
- 不再使用 **导通状态电压** 和关断参数。

## 描述

Thyristor

Thyristor (Piecewise Linear) 模块对晶闸管进行建模。晶闸管的 I-V 特性使得：如果门极-阴极电压超过指定的门极触发电压，则晶闸管导通。如果负载电流降至指定的保持电流值以下，则器件关断。

要定义晶闸管的 I-V 特性，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values` 或 `Tabulate`。仅当您暴露模块的热端口时，`Tabulate` 选项才可用。

在导通状态下，阳极-阴极路径的行为类似于具有正向电压降 *Vf* 和导通电阻 *Ron* 的线性二极管。但是，如果您暴露模块的热端口并使用表格化 I-V 数据参数化器件，则表格化电阻是温度和电流的函数。

在关断状态下，阳极-阴极路径的行为类似于具有低关断电导 *Goff* 的线性电阻。

用于定义该模块的 Simscape™ 方程为：

        if (v > Vf)&&((G>Vgt)||(i>Ih))
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
- *Ron* 是导通状态电阻。
- *Goff* 是关断状态电导。

使用模块对话框的 Integral Diode 选项卡，您可以包含一个集成的阴极-阳极二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断向负载的电压供应时，感性负载可能产生高反向电压尖峰。

下表说明了如何根据您的目标设置 **Integral protection diode** 参数。

| 目标 | 要选择的值 | 模块行为 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | 该模块包含 Diode 模块的集成副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |
| 精确指定反向模式电荷动态特性。 | `Diode with charge dynamics` | 该模块包含 Diode 模块动态模型的集成副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |

### 对门极端口和热效应建模

您可以在物理端口或电气端口之间进行选择，以控制门极端子，并暴露热端口来对开关事件和导通损耗产生的热量进行建模。要选择门极控制端口，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。要暴露热端口，请将 **Modeling option** 参数设置为 `No thermal port` 或 `Show thermal port`。

有关使用热端口的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 热损耗

开关损耗是半导体中热损耗的主要来源。在每次开-关开关转换期间，晶闸管的寄生参数会存储能量，然后耗散能量。

开关损耗取决于关断状态电压和导通状态电流。当开关器件导通时，功率损耗取决于器件两端的初始关断状态电压以及器件处于完全导通状态时的最终导通状态电流。

该模块通过将结温阶跃升高一个等于开关损耗除以结处总热质量的值来施加开关损耗。您必须指定单次开通事件期间耗散的能量。您还必须指定与所引用损耗对应的关断状态电压和导通状态电流值。您可以根据所拥有的数据来参数化开通损耗。如果有表格化数据可用，请使用表格化数据。

- 要为开通损耗指定标量值，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values`。**Switch-on loss** 参数值设置开通损耗的大小。该模块按关断状态电压和导通状态电流对损耗进行缩放。
- 要将开通损耗指定为结温和导通状态电流的函数，请将 **On-state behavior and switching losses** 参数设置为 `Tabulate`。**Switch-on loss, Eon(Tj,Iak)** 参数设置损耗的大小。该模块按关断状态电压对损耗进行缩放。

当电流降至 **Holding current** 参数值以下时，器件关断。**Natural commutation rectification loss** 参数值定义关断损耗。该模块不会按关断状态电压或导通状态电流对该损耗进行缩放，因为对于整流损耗，无法知道何时测量起始电流或最终电压。

反向恢复损耗可能是二极管中热损耗的重要来源。二极管每次从导通状态关断到开路状态时都会耗散能量。要对反向恢复损耗进行建模：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。

如果将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`，则 **Reverse recovery loss table, Erec(Tj, If)** 参数的值指定耗散能量，该能量是结温和开关事件前正向电流的函数。关断状态电压会相对于 **Turn-off voltage when measuring recovery loss, Vrec** 参数值对损耗进行线性缩放。该表使用电流和电压的延迟值。若要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage and current values** 参数设置为低于最快开关周期的值。

如果将 **Reverse recovery loss model** 参数设置为 `Fixed loss`，则 **Reverse recovery loss** 参数的值指定每个关断事件期间耗散的能量。如果您选择 **Scale reverse recovery loss with current and voltage** 参数，则该模块会按导通状态电流和关断状态电压对该损耗值进行线性缩放。若要使用接近瞬时值的缩放值，请将 **Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

作为对反向恢复进行建模的替代方法，您可以将 **Integral protection diode** 参数设置为 `Diode with charge dynamics`。但是，与使用第一种方法相比，此方法需要更小的仿真时间步长。

**注意**

该模块在仿真期间不知道开关事件之后的电流，因此一旦电流大于保持电流的持续时间超过 **Wait time before switch-on current measurement** 参数指定的值，该模块就会记录导通状态电流。类似地，该模块在器件开通时记录关断状态电压。因此，记录的仿真数据直到一个开关周期之后才会向热网络报告开关损耗。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。

对于所有理想开关器件，记录的仿真数据会将热损耗报告为 `lastTurnOffLoss`、`lastTurnOnLoss` 和 `lastReverseRecoveryLoss`。对于 Thyristor (Piecewise Linear) 模块，`lastTurnOnLoss` 等于 **Natural commutation rectification loss** 参数值。这些变量将损耗表示为脉冲，其幅度等于能量损耗。如果您使用脚本对定义的仿真时间段内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录的数据中提取导通损耗和开关损耗。

您还可以从记录的仿真数据中的 `accumulatedSwitchingLosses` 变量访问累计的总开关损耗。此变量汇总截至当前的所有开关损耗，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗，因为该模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆导通状态损耗。

如果您使用表格化数据对开关损耗或反向恢复损耗进行建模，请检查温度和电流是否在您指定的范围内。如果您未定义真实的热模型，例如，如果结质量或从结到外壳的电导过小，则温度可能超出您指定的范围，导致该模块将损耗外推到非物理值。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
