---
type: simulink-block
title: 'MOSFET (Ideal, Switching)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'mosfetidealswitching'
documentation_source_path: 'ref/mosfetidealswitching.html'
language: zh-CN
chinese_source: worker-translation
---

# MOSFET (Ideal, Switching)

## 端口

### 守恒

### **G** — 栅极端口（电气）

与栅极端口关联的端口。您可以将该端口设置为物理信号或电气端口。

### **S** — 源极端口（电气）

与源极端口关联的电气守恒端口。

### **D** — 漏极端口（电气）

与漏极端口关联的电气守恒端口。

### **H** — 热端口（热）

热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设置为 `Show thermal port`。

### **HDiode** — 集成保护二极管的热端口（热）

*自 R2024b 起*

与集成保护二极管关联的热守恒端口。

#### 依赖关系

要启用此端口，请选中 **Separate thermal port for integral diode** 参数。

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
| Drain-source on resistance, R\_DS(on) | | | | Threshold voltage, Vth | | | |
| Off-state conductance | | | | **On-state behavior and switching losses** | | | |
| *`Specify constant values`* | *`Tabulate`* | | |
| Threshold voltage, Vth | | | | Drain-source on resistance, R\_DS(on) | On-state voltage, Vds(Tj,Ids) | | |
| Off-state conductance | Temperature vector, Tj | | |
| Drain-source current vector, Ids | | |
| Off-state conductance | | |

### **Gate-control port** — 用于指定物理或电气控制端口的选项 `PS` (默认) | `Electrical`

用于指定开关栅极的物理或电气控制端口的选项。

**注意**

如果将此参数设置为 `Electrical`，请在此模块中使用内部或外部反向二极管。出于数值考虑，二极管的正向电压必须小于此模块的 **Threshold voltage, Vth** 参数的值。

### **On-state behavior and switching losses** — 导通状态行为和开关损耗 `Specify constant values` (默认) | `Tabulate`

用于导通状态行为和开关损耗的参数化方法，指定为以下值之一：

- `Specify constant values` — 使用标量值指定输出电流、开通损耗和关断损耗数据。该模块假定单次开通或关断事件期间耗散的能量随关断状态电压和导通状态电流线性缩放。该模块还假定损耗与温度无关。
- `Tabulate` — 使用向量指定输出电流和温度数据。使用数组指定开通损耗和关断损耗数据。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Drain-source on resistance, R\_DS(on)** — 漏源导通电阻 `0.01` `Ohm` (默认)

器件导通时的漏源电阻。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Off-state conductance** — 关断状态电导 `1e-6` `1/Ohm` (默认)

器件关断时的漏源电导。该值必须小于 1/*R*，其中 *R* 是 **On-state resistance** 的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Threshold voltage, Vth** — 阈值电压 `2` `V` (默认)

栅源电压阈值。当栅源电压高于此值时，器件导通。

#### 依赖关系

请参阅主要参数依赖关系表。

### **On-state voltage, Vds(Tj,Ids)** — 导通状态电压 `[0, 1.8, 3.2, 6, 10, 16; 0, 2, 5.5, 9.5, 15, 25]` `V` (默认) | 非负标量矩阵

器件在触发导通状态下的电压降。此参数是温度和最终导通状态输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Temperature vector, Tj** — 温度值 `[298.15, 448.15]` `K` (默认)

与 **on-state voltage, Vds(Tj,Ids)** 参数对应的温度值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **Drain-source current vector, Ids** — 漏源电流向量 `[0, 20, 40, 60, 80, 100]` `A` (默认)

定义导通状态电压所对应的漏源电流。第一个元素必须为零。使用向量指定此参数。

#### 依赖关系

请参阅主要参数依赖关系表。

### 开关损耗

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J` (默认) | 正标量

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Switch-off loss** — 关断损耗 `17.14e-3` `J` (默认) | 正标量

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Off-state Vds voltage for switching loss data** — 用于开关损耗数据的关断状态漏源电压 `300` `V` (默认) | 正标量

器件在关断状态期间的输出电压。此电压是您用于给出开通损耗和关断损耗的阻断电压。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **On-state behavior and switching losses** 设置为 `Specify constant values`。
- 将 **On-state behavior and switching losses** 设置为 `Tabulate` 并清除 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **On-state current for switching loss data** — 用于开关损耗数据的导通状态电流 `600` `A` (默认) | 正标量

您用于定义开通损耗和关断损耗的输出电流。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Specify constant values`。

### **Use last on-state current from previous cycle for turn-on loss** — 使用上一周期的最后导通状态电流计算开通损耗的选项 `Off` (默认) | `On`

*自 R2023b 起*

使用上一周期的最后导通状态电流计算开通损耗的选项。

### **Use last off-state voltage from previous cycle for turn-off loss** — 使用上一周期的最后关断状态电压计算关断损耗的选项 `Off` (默认) | `On`

*自 R2023b 起*

使用上一周期的最后关断状态电压计算关断损耗的选项。

### **Switch-on loss, Eon(Tj,Ids)** — 开通损耗 `[0, 55.04, 124.57, 235.53, 362.12; 0, 71.25, 161.25, 304.88, 468.75] * 1e-6` `J` (默认) | 非负标量矩阵

作为温度和导通状态电流的函数，单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并清除 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Switch-off loss, Eoff(Tj,Ids)** — 关断损耗 `[0, 18, 30, 56.1, 76.5; 0, 22.5, 37.5, 70.13, 95.63] * 1e-6` `J` (默认) | 非负标量矩阵

作为温度和导通状态电流的函数，单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并清除 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Temperature vector for switching losses, Tj** — 开关损耗的温度 `[298.15, 448.15]` `K` (默认) | 向量

您据以给出开通损耗和关断损耗的温度值。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Drain-source current vector for switching losses, Ids** — 开关损耗的漏源电流向量 `[0, 10, 20, 30, 40]` `A` (默认) | 非负标量向量

您据以给出开通损耗和关断损耗的漏源电流。第一个元素必须为 `0`。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Include switching loss tabulation with off-state Vds voltage** — 使用关断状态漏源电压对开关损耗进行制表的选项 `Off` (默认) | `On`

*自 R2023b 起*

使用关断状态漏源电压对开关损耗进行制表的选项。

要使用导通状态漏源电流和温度对开通损耗和关断损耗进行制表，请清除此参数。该模块假定损耗随关断状态漏源电压线性缩放。

要使用温度、导通状态漏源电流和关断状态漏源电压对开通损耗和关断损耗进行制表，请选中此参数。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate`。

### **Switch-on loss, Eon(Tj,Ids,Vds)** — 开通损耗 `[zeros(2, 5, 3)]` `J` (默认) | 非负标量三维数组

*自 R2023b 起*

作为温度、导通状态漏源电流和关断状态漏源电压的函数，单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并选中 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Switch-off loss, Eoff(Tj,Ids,Vds)** — 关断损耗 `[zeros(2, 5, 3)]` `J` (默认) | 非负标量三维数组

*自 R2023b 起*

作为温度、导通状态漏源电流和关断状态漏源电压的函数，单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并选中 **Include switching loss tabulation with off-state Vds voltage** 参数。

### **Off-state Vds voltage vector for switching loss data** — 用于开关损耗数据的关断状态 Vds 电压向量 `[0, 150, 300]` `V` (默认) | 向量

*自 R2023b 起*

您据以给出开通损耗和关断损耗的关断状态漏源电压。

#### 依赖关系

要启用此参数，请将 **On-state behavior and switching losses** 设置为 `Tabulate` 并选中 **Include switching loss tabulation with off-state Vds voltage** 参数。

### 集成二极管

### **Integral protection diode** — 保护二极管 `Diode with no dynamics` (默认) | `External diode` | `Diode with charge dynamics`

MOSFET (Ideal, Switching) 模块用于集成保护二极管的模型。选择以下选项之一：

- `External diode` — MOSFET (Ideal, Switching) 不建模集成保护二极管。请使用外部 Diode 模块。
- `Diode with no dynamics` — MOSFET (Ideal, Switching) 模块使用与无动态特性的 Diode 模块相同的方程对集成保护二极管建模。选择此选项可优先提高仿真速度。
- `Diode with charge dynamics` — MOSFET (Ideal, Switching) 模块使用与具有电荷动态特性的 Diode 模块相同的方程对集成保护二极管建模。选择此选项可优先获得详细仿真结果。

### **Diode model** — 二极管模型 `Piecewise Linear` (默认) | `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 使用二极管的分段线性模型，如 Piecewise Linear Diode 中所述。这是默认方法。
- `Tabulated I-V curve` — 使用制表正向偏置 I-V 数据加上固定反向偏置关断电导。

#### 依赖关系

此参数仅在热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics` 时可见。

### **Table type** — 制表函数 `Table in If(Tj,Vf) form` (默认) | `Table in Vf(Tj,If) form`

用于将电流制表为温度和电压的函数，或将电压制表为温度和电流的函数的选项。

#### 依赖关系

此参数仅在热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时可见。

### **Reverse I-V characteristics type** — 反向 I-V 特性类型 `Specify off conductance` (默认) | `Tabulate`

*自 R2024a 起*

是通过使用二极管关断电导来指定反向 I-V 特性，还是通过将电流制表为温度和电压的函数或将电压制表为温度和电流的函数来指定反向 I-V 特性。

#### 依赖关系

此参数仅在热端口暴露且 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **Diode model** 设置为 `Tabulated I-V curve` 时可见。

### **Forward voltage** — 正向电压 `0.8` `V` (默认)

为使二极管 I-V 特性的梯度为 1/*R*on，`+` 和 `-` 模块端口两端所需的最小电压，其中 *R*on 是 **On resistance** 参数的值。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **On resistance** — 导通电阻 `0.001` `Ohm` (默认)

高于 **Forward voltage** 参数值的电压随电流的变化率。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 如果热端口暴露，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并将 **Diode model** 设置为 `Piecewise linear`。

### **Forward currents, If(Tj,Vf)** — 正向电流向量 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (默认) | 非负向量

正向电流。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`，并将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Junction temperatures, Tj** — 结温向量 `[25, 125]` `degC` (默认)

结温向量。此参数必须为至少包含两个元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`。

### **Forward voltages, Vf** — 正向电压向量 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (默认)

正向电压向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口并将 **Diode model** 设置为 `Tabulated I-V curve`，并将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Forward voltages, Vf(Tj,If)** — 正向电压向量 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (默认) | 非负向量

正向电压。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **二极管模型** 设置为 `Tabulated I-V curve`，将 **表类型** 设置为 `Table in Vf(Tj,If) form`。

### **正向电流, If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

正向电流向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将 **二极管模型** 设置为 `Tabulated I-V curve`，将 **表类型** 设置为 `Table in Vf(Tj,If) form`。

### **反向电流, Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认） | 非负向量

*自 R2024a 起*

反向电流。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **建模选项** 为 `Show thermal port`
- **集成保护二极管** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **二极管模型** 为 `Tabulated I-V curve`
- **表类型** 为 `Table in If(Tj,Vf) form`
- **反向 I-V 特性** 为 `Tabulate`

### **反向电压, Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认） | 非负向量

*自 R2024a 起*

反向电压向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **建模选项** 为 `Show thermal port`
- **集成保护二极管** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **二极管模型** 为 `Tabulated I-V curve`
- **表类型** 为 `Table in If(Tj,Vf) form`
- **反向 I-V 特性** 为 `Tabulate`

### **反向电压, Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认） | 非负向量

*自 R2024a 起*

反向电压。此参数必须为至少包含三个非负元素的向量。

#### 依赖关系

要启用此参数，请设置：

- **建模选项** 为 `Show thermal port`
- **集成保护二极管** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **二极管模型** 为 `Tabulated I-V curve`
- **表类型** 为 `Table in Vf(Tj,If) form`
- **反向 I-V 特性** 为 `Tabulate`

### **反向电流, Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认） | 非负向量

*自 R2024a 起*

反向电流向量。此参数必须为至少包含三个非负值的向量。

#### 依赖关系

要启用此参数，请设置：

- **建模选项** 为 `Show thermal port`
- **集成保护二极管** 为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- **二极管模型** 为 `Tabulated I-V curve`
- **表类型** 为 `Table in Vf(Tj,If) form`
- **反向 I-V 特性** 为 `Tabulate`

### **断态电导** — 断态电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **反向 I-V 特性类型** 设置为 `Specify off conductance` 时，此参数才可见。

### **反向恢复损耗模型** — 反向恢复损耗的模型 `Fixed loss`（默认） | `Tabulated loss`

*自 R2023a 起*

是对固定反向恢复损耗建模，还是对表格化反向恢复损耗建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 参数设置为 `Show thermal port`，并将 **集成保护二极管** 参数设置为 `Diode with no dynamics`。

### **反向恢复损耗** — 反向恢复损耗 `0` `J`（默认） | 非负标量

*自 R2023a 起*

每次关断事件中耗散的能量。无论开关事件之前或之后二极管的状态如何，该模块都会耗散此能量。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 参数设置为 `Fixed loss`。

### **使反向恢复损耗随电流和电压缩放** — 使反向恢复损耗缩放的选项 `On`（默认） | `Off`

*自 R2023b 起*

使反向恢复损耗随电流和电压缩放的选项。

#### 依赖关系

要启用此参数：

- 将 **建模选项** 设置为 `Show thermal port`。
- 将 **集成保护二极管** 设置为 `Diode with no dynamics`。
- 将 **反向恢复损耗模型** 设置为 `Fixed loss`。

### **反向恢复损耗表, Erect(Tj), If** — 反向恢复损耗 `zeros(2,3)` `J`（默认） | 非负标量向量

*自 R2023a 起*

耗散能量，作为紧邻开关事件之前的正向电流 *If* 以及二极管进入断态后的最终断态电压的函数。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`。

### **恢复损耗表的温度向量, Tj** — 恢复损耗表的温度向量 `[298.15 398.15]` `K`（默认） | 向量

*自 R2023a 起*

该模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`。

### **恢复损耗表的正向电流向量, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `K`（默认） | 非负标量向量

*自 R2023a 起*

该模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`。

### **测量恢复损耗时的正向电流, Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认） | 正标量

*自 R2023b 起*

在反向恢复事件之前流过二极管的正向电流，该模块用它来测量恢复损耗。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 设置为 `Fixed loss`，并选择 **使反向恢复损耗随电流和电压缩放** 参数。

### **测量恢复损耗时的关断电压, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认） | 正标量

*自 R2023a 起*

在反向恢复事件之后二极管两端的电压，该模块用它来测量恢复损耗。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **反向恢复损耗模型** 设置为 `Fixed loss`，并选择 **使反向恢复损耗随电流和电压缩放** 参数。
- 将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`。

### **电压和电流值的滤波器时间常数** — 电压和电流值的滤波器时间常数 `1 / 1000 / 100` `s`（默认） | 正标量

*自 R2023a 起*

该模块用于计算反向恢复损耗的电压和电流值的滤波器时间常数。请将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **反向恢复损耗模型** 设置为 `Fixed loss`，并选择 **使反向恢复损耗随电流和电压缩放** 参数。
- 将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`。

### **结电容** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **峰值反向电流, iRM** — 峰值反向电流 `-235` `A`（默认） | 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **测量 iRM 时的初始正向电流** — 测量 iRM 时的初始正向电流 `300` `A`（默认） | 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **测量 iRM 时的电流变化率** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认） | 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **反向恢复时间参数化** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认） | `Specify stretch factor` | `Specify reverse recovery charge`

确定在模块中如何指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果您选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则指定一个值，该模块用它来推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **反向恢复时间, trr** — 反向恢复时间 `15` `μs`（默认） | 标量

从电流最初变为零（二极管关断时）到电流降至小于峰值反向电流的 10% 的时间间隔。**反向恢复时间, trr** 参数的值必须大于 **峰值反向电流, iRM** 参数的值除以 **测量 iRM 时的电流变化率** 参数的值。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，并且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery time directly` 时，此参数才可见。

### **反向恢复时间拉伸因子** — 反向恢复时间拉伸因子 `3`（默认） | 大于 `1` 的标量

该模块用于计算反向恢复时间的拉伸因子。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简便方法。拉伸因子的值越大，反向恢复电流消散所需的时间就越长。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，并且 **反向恢复时间参数化** 参数设置为 `Specify stretch factor` 时，此参数才可见。

### **反向恢复电荷, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

该模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据表中指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **峰值反向电流, iRM** 指定的值。
- *a* 是为 **测量 iRM 时的电流变化率** 指定的值。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，并且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery charge` 时，此参数才可见。

### **测量 Erec 时的二极管关断电压** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认）

稳态时二极管两端的电压。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，并且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **测量 Erec 时的杂散电感** — 测量 Erec 时的杂散电感 `150` `nH`（默认）

测量电路中的总非预期电感。该模块使用此值计算 **反向恢复能量, Erec**。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，并且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **反向恢复能量, Erec** — 反向恢复能量 `0.03` `J`（默认）

由二极管反向恢复引起的总开关损耗。

#### 依赖关系

仅当 **集成保护二极管** 参数设置为 `Diode with charge dynamics`，并且 **反向恢复时间参数化** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

有关这些参数的详细信息，请参阅 Diode。

### 热端口

有关使用热端口和 **热端口** 参数的详细信息，请参阅半导体中的热效应仿真。

### **为集成二极管分离热端口** — 为集成二极管分离热端口的选项 `off`（默认） | `on`

*自 R2024b 起*

是否将器件的集成保护二极管的热端口分离。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Show thermal port`，并在 **集成二极管** 部分中，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **热网络** — 热网络建模选项 `External`（默认） | `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

用于对模块热网络建模的选项。

### **热质量参数化** — 热质量参数化选项 `By thermal time constants`（默认） | `By thermal mass`

热质量参数化选项：

- `By thermal time constants` — 根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **结-壳和壳-环境（或壳-散热器）热阻, [R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[.03, .2]` `K/W`（默认） | 正值向量

行向量 [ *R\_JC* *R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **结和壳的热时间常数, [t\_J t\_C]** — 结和壳的热时间常数 `[.1, 5]` `s`（默认） | 正值向量

行向量 [ *t\_J* *t\_C* ]，包含两个热时间常数值。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`，并将 **热质量参数化** 设置为 `By thermal time constants`。

### **结和壳的热质量, [M\_J M\_C]** — 结和壳的热质量 `[3, 25]` `J/K`（默认） | 正值向量

行向量 [ *M\_J* *M\_C* ]，包含两个热质量值。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`，并将 **热质量参数化** 设置为 `By thermal mass`。

### **结温和壳温初始温度，[T\_J T\_C]** — 结温和壳温初始温度 `[25, 25]` `degC` （默认） | 正值向量

由两个温度值组成的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **二极管结-壳和壳-环境（或壳-散热器）热阻，[R\_JC R\_CA]** — 用于集成二极管的结-壳和壳-环境（或壳-散热器）热阻 `[.03, .2]` `K/W` （默认） | 正值向量

*自 R2024b 起*

由两个热阻值组成的行向量 [ *R\_JC* *R\_CA* ]，由两个 Conductive Heat Transfer 模块表示，用于集成保护二极管。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **HDiode** 与二极管壳之间的热阻。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **二极管结温和壳温的热时间常数，[t\_J t\_C]** — 用于集成二极管的结温和壳温的热时间常数 `[.1, 5]` `s` （默认） | 正值向量

*自 R2024b 起*

由两个热时间常数值组成的行向量 [ *t\_J* *t\_C* ]，用于集成保护二极管。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Specify junction and case thermal parameters`。
  - 将 **热质量参数化** 设置为 `By thermal time constants`。

### **二极管结温和壳温的热质量，[M\_J M\_C]** — 二极管结温和壳温的热质量 `[3, 25]` `J/K` （默认） | 正值向量

*自 R2024b 起*

由两个热质量值组成的行向量 [ *M\_J* *M\_C* ]，用于集成保护二极管。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Specify junction and case thermal parameters`。
  - 将 **热质量参数化** 设置为 `By thermal mass`。

### **二极管结温和壳温的初始温度，[T\_J T\_C]** — 二极管结温和壳温的初始温度 `[25, 25]` `degC` （默认） | 正值向量

*自 R2024a 起*

由两个温度值组成的行向量 [ *T\_J* *T\_C* ]，用于集成保护二极管。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **热阻，[R1 R2 … Rn]** — 热阻 `[.03, .1, .2]` `K/W` | `[.03, .2]` `K/W` | 正值向量

由 *n* 个热阻值组成的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[.03, .1, .2]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.03, .2]`。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **热时间常数，[t1 t2 … tn]** — 热时间常数 `[.1, 1, 5]` `s` | `[1, 10]` `s` | 正值向量

由 *n* 个热时间常数值组成的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **热阻，[R1 R2 … Rn]** 的长度匹配。使用此参数化时，模块将热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 是第 i 个 Cauer 元件（如果将 **热网络** 设置为 `Cauer model`）或 Foster 元件（如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[.1, 1, 5]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[1, 10]`。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **热质量参数化** 设置为 `By thermal time constants`。

### **热质量，[M1 M2 … Mn]** — 热质量 `[3, 10, 25]` `J/K` | `[33, 50]` `J/K` | 正值向量

由 *n* 个热质量值组成的行向量，其中 n 是热网络中 Cauer 元件的数量。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[3, 10, 25]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[33, 50]`。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **热质量参数化** 设置为 `By thermal mass`。

### **热质量初始温度，[T1 T2 … Tn]** — 热质量的初始温度 `[25, 25, 25]` `degC` （默认） | 正值向量

由温度值组成的行向量，这些温度值对应于模型中每个热容上的温度降。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model`。

### **二极管热阻，[R1 R2 … Rn]** — 用于集成二极管的热阻 `[.03, .1, .2]` `K/W` | `[.03, .2]` `K/W` | 正值向量

*自 R2024b 起*

由 *n* 个热阻值组成的行向量，用于集成保护二极管，由热网络中使用的 Cauer 元件表示。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[.03, .1, .2]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.03, .2]`。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **二极管热时间常数，[t1 t2 … tn]** — 用于集成二极管的热时间常数 `[.1, 1, 5]` `s` | `[1, 10]` `s` | 正值向量

*自 R2024b 起*

由 *n* 个热时间常数值组成的行向量，用于集成保护二极管，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **二极管热阻，[R1 R2 … Rn]** 的长度匹配。使用此参数化时，模块将热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 是第 i 个 Cauer 元件（如果将 **热网络** 设置为 `Cauer model`）或 Foster 元件（如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[.1, 1, 5]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[1, 10]`。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **热质量参数化** 设置为 `By thermal time constants`。

### **二极管热质量，[M1 M2 … Mn]** — 用于集成二极管的热质量 `[3, 10, 25]` `J/K` （默认） | `[33, 50]` `J/K` | 正值向量

*自 R2024b 起*

由 *n* 个热质量值组成的行向量，用于集成保护二极管，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **热网络** 设置为 `Cauer model`，则默认值为 `[3, 10, 25]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[33, 50]`。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **热质量参数化** 设置为 `By thermal mass`。

### **二极管热质量的初始温度，[T1 T2 … Tn]** — 二极管热质量的初始温度 `[25, 25, 25]` `degC` （默认） | 正值向量

*自 R2024b 起*

用于集成保护二极管的温度值行向量。此参数对应于模型中每个热容上的温度降。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Cauer model`。

### **初始节点温度，[T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC` （默认） | 正值向量

从结开始每个节点的温度值行向量。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`。

### **二极管初始节点温度，[T1 T2 ... Tn]** — 用于集成二极管的初始节点温度 `[25, 25, 25, 25]` `degC` （默认） | 正值向量

*自 R2024b 起*

从集成保护二极管结开始每个节点的温度值行向量。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`。

### **结热质量** — 结的热质量 `0.1` `J/K` （默认） | 正标量

结的热质量。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `External`。

### **二极管结热质量** — 二极管结的热质量 `0.1` `J/K` （默认） | 正标量

*自 R2024b 起*

二极管结的热质量。

#### 依赖项

要启用此参数：

- 在 **集成二极管** 部分，将 **集成保护二极管** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分：

  - 选择 **为集成二极管使用单独的热端口** 参数。
  - 将 **热网络** 设置为 `External`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b: 为集成二极管使用单独的热端口

现在，您可以将 MOSFET (Ideal, Switching) 模块的集成保护二极管的热端口与 **H** 端口分开。要分离热端口：

- 将 **建模选项** 参数设置为 `Show thermal port`
- 在 **集成二极管** 部分，将 **集成保护二极管** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **热端口** 部分，选择 **为集成二极管使用单独的热端口** 参数。

### R2024a: 对表格化反向 I-V 特性建模

现在，您可以通过将电流表示为温度和电压的函数，或将电压表示为温度和电流的函数，来对 MOSFET (Ideal, Switching) 模块的反向 I-V 特性建模。

在 R2024a 之前，只能通过指定反向偏置二极管的关断态电导来对反向 I-V 特性建模。

### R2023b: 根据电流和电压缩放反向恢复损耗

现在，您可以根据电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **根据电流和电压缩放反向恢复损耗** 参数。

在 R2023a 或更早版本中创建的模型默认不缩放，以保持向后兼容性。

### R2023b: 使用温度、电流和电压表格化开关损耗

现在，您可以使用温度、电流和电压表格化开关损耗。在更早的版本中，只能使用温度和电流表格化开关损耗。

要将损耗指定为结温、导通状态电流和关断状态电压的函数，请将 **导通状态行为和开关损耗** 参数设置为 `Tabulate`，并选择 **包含使用关态 Vds 电压的开关损耗表格** 参数。

### R2023b：确定不连续负载电流的开关损耗

MOSFET (Ideal, Switching) 模块现在支持不连续负载电流。

该模块通过在所有开通和关断事件处测量关断状态电压和导通状态电流来计算开关损耗，从而支持不连续负载电流。新模型默认采用这种方式。如果使用定步长求解器，器件最短导通或关断周期现在为一个步长。在 R2023b 之前，最短周期为三个步长。要报告开关损耗，最短周期仍为三个步长。

在 R2023b 之前，该模块仅在开通前测量关断状态电压，并在关断前测量导通状态电流。

在 R2023b 中，你仍可使用在开通前测量关断状态电压并在关断前测量导通状态电流的原始方法。在 R2023a 或更早版本中创建的模型默认采用此行为，以实现向后兼容。原始方法设计用于具有连续电流的感性负载。如果要对开关器件两端的电容或开关器件引线电感建模，请使用原始方法：

- 要对开关器件两端的电容建模，例如，如果并联二极管具有电容或你使用 Lauritzen 电荷模型，请选择 **Use last on-state current from previous cycle for turn-on loss** 参数。
- 要对开关器件引线电感建模，请选择 **Use last off-state voltage from previous cycle for turn-off loss** 参数。

### R2023b：绘制基本 I-V 特性

现在，你可以基于当前模块参数值，在不仿真模型的情况下，为 MOSFET (Ideal, Switching) 模块绘制基本 I-V 特性。

要绘制基本特性，请右键点击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。

如果使用集成保护二极管对开关器件建模，**Basic characteristics** 选项会为开关器件和二极管绘制 I-V 特性。如果启用该模块的热端口，**Basic characteristics** 选项还会生成开通能量损耗和关断能量损耗作为导通状态电流和关断状态电压函数的曲面图。

### R2023a：更新集成二极管建模选项

从 R2023a 起，你可以在 MOSFET (Ideal, Switching) 模块中对反向恢复损耗建模。要启用 **Reverse recovery loss model** 参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### R2021a：移除能量耗散时间常数参数

从 R2021a 起，MOSFET (Ideal, Switching) 模块的 **Energy dissipation time constant** 参数不再使用。结温中的阶跃现在反映开关损耗。如果你的模型包含直接连接到该模块热端口的热质量，请将其删除，并在组件自身内部对热质量建模。

### R2020b：更新开关损耗和热建模选项

从 R2020b 起，MOSFET (Ideal, Switching) 模块具有改进的损耗和热建模选项。

由于这些更改：

- 电气和热导通状态损耗现在始终相同。**Thermal loss dependent on** 参数及其选项 `Voltage and current` 和 `Voltage, current, and temperature` 已重命名为 **On-state behavior and switching losses**、`Specify constant values` 和 `Tabulate with temperature and current`：

  - 如果你为 **Thermal loss dependent on** 选择了 `Voltage and current`，则电气导通状态损耗不变，其值使用导通电阻确定。但是，热导通状态损耗现在也由导通电阻确定。在 R2020b 之前，热导通状态损耗由 **On-state voltage** 和 **Output current, Iout** 参数的乘积定义。
  - 如果你为 **Thermal loss dependent on** 选择了 `Voltage, current, and temperature`，则热导通状态损耗不变，**On-state voltage, Vds(Tj,Ids)** 参数设置其值。但是，电气导通状态损耗现在等于热导通状态损耗。在 R2020b 之前，电气导通状态损耗由导通电阻的值定义。
- **On-state voltage** 参数不再使用。

## 描述

用于开关应用的理想 N 沟道 MOSFET

MOSFET (Ideal, Switching) 模块对 n 沟道金属氧化物半导体场效应晶体管 (MOSFET) 的理想开关行为建模。

n 沟道 MOSFET 的开关特性为：如果栅源电压超过指定阈值电压，则 MOSFET 处于导通状态。否则，器件处于关断状态。下图显示了典型的 *i-v 特性*：

要定义 MOSFET 的 I-V 特性，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values` 或 `Tabulate`。仅当暴露该模块的热端口时，`Tabulate` 选项才可用。

在导通状态下，漏源路径表现为具有电阻 *Rds\_on* 的线性电阻器。但是，如果暴露该模块的热端口，并使用表格化 I-V 数据对器件进行参数化，则表格化电阻是温度和电流的函数。

在关断状态下，漏源路径表现为具有低关断状态电导 *Goff* 的线性电阻器。

然后，该模块的定义 Simscape™ 方程为：

```
    if G > Vth       v == i*Rds_on;     else       v == i/Goff;     end
```

其中：

- *G* 取决于 **Gate-control port** 参数的值。

  - 如果将 **Gate-control port** 参数设置为 `PS`，则通过物理信号控制栅极端子。*G* 是输入端口 **G** 处的值。
  - 如果将 **Gate-control port** 参数设置为 `Electrical`，则通过电气信号控制栅极端子。*G* 等于：

    ```
        if v >= 0        G = G.v - S.v;     else       G = G.v - D.v;     end
    ```

    其中 *G.v* 是栅极电压，*S.v* 是源极电压，*D.v* 是漏极电压。
- *Vth* 是阈值电压。
- *v* 是漏源电压。
- *i* 是漏源电流。
- *Rds\_on* 是导通电阻。
- *Goff* 是关断状态电导。

使用 **Integral Diode** 设置，你可以包括体二极管或集成保护二极管。集成保护二极管为反向电流提供传导路径，并允许提高模型中的数值稳定性。例如，为半导体器件突然关断感性负载的电压供应时产生的高反向电压尖峰提供路径。

根据你的目标设置 **Integral protection diode** 参数。

| 目标 | | 要选择的值 | 集成保护二极管 |
| --- | --- | --- | --- |
| 不包括保护。 | | `External diode` | None |
| 包括保护。 | 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

### 对栅极端口和热效应建模

你可以选择物理端口或电气端口来控制栅极端子，并暴露热端口，以对开关事件和传导损耗生成的热量建模。要选择栅极控制端口，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。要暴露热端口，请将 **Modeling option** 参数设置为 `No thermal port` 或 `Show thermal port`。

你还可以通过选择 **Separate thermal port for integral diode** 参数来暴露集成保护二极管的 **HDiode** 热端口。如果不暴露二极管热端口，则器件和二极管共享公共热端口 **H**。*（自 R2024b 起）*

有关使用热端口的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 热损耗

图中显示了半导体器件的输出电压 *V*out 和输出电流 *I*out 的理想化表示。该图中的区间包含整个第 *n* 个开关周期，在此期间，该模块先关断，然后导通。

开关损耗是半导体中热损耗的主要来源。在每次通断开关转换期间，MOSFET 寄生参数会存储能量，然后耗散能量。

开关损耗取决于关断状态电压和导通状态电流。当开关器件导通时，功率损耗取决于器件两端的初始关断状态电压以及器件完全导通时的最终导通状态电流。类似地，当开关器件关断时，功率损耗取决于流过器件的初始导通状态电流以及器件完全关断时器件两端的最终关断状态电压。

您可以选择何时测量该模块用于计算开通和关断损耗的电流和电压。对于大多数电路，您可以在开通或关断事件期间进行测量：

- 开通损耗为
  *E*on*(I*TurnOn*(n),V*TurnOn*(n))*
- 关断损耗为
  *E*off*(I*TurnOff*(n),V*TurnOff*(n))*

但是，您不能始终使用这些测量值，例如在以下情况下：

- 您正在对开关器件两端的电容建模。例如，您正在对带电容的保护二极管建模，或者您正在使用 Lauritzen 电荷模型。该电容会在器件开通时导致电流过冲瞬态，这意味着您不能使用测量值 *I*TurnOn*(n)* 来计算开通损耗。该模块需要瞬态之后的值。不要对开关器件两端的电容建模，因为此模型将半导体开关器件的抽象行为与二极管的详细物理特性混合在一起。如果必须对开关器件两端的电容建模，您可以使用最后一个导通周期结束时的电流测量值 *I*TurnOff*(n-1)*。要启用此选项，请选择 **Use last on-state current from previous cycle for turn-on loss** 参数。
- 您正在对开关器件引线电感建模。该电感会在器件关断时导致电压过冲瞬态，这意味着您不能使用测量值 *V*TurnOff*(n)* 来计算关断损耗。该模块需要瞬态之后的值。不要对开关器件引线电感建模，因为与引线电感相关的时间常数通常远小于脉宽调制（PWM）周期。这一较小的时间常数意味着仿真需要更小的仿真时间步长，从而减慢仿真速度。如果必须对开关器件引线电感建模，请使用最后一个关断周期结束时的电压测量值 *V*TurnOn*(n)*。要启用此选项，请选择 **Use last off-state voltage from previous cycle for turn-off loss** 参数。

检查仿真结果，以确认损耗行为符合您的预期。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。下表定义了记录的仿真数据中与开关损耗计算相关的变量名称。

**用于计算开关损耗的电压和电流**

| 量 | 记录的仿真数据中的变量名称 |
| --- | --- |
| *V*TurnOn | `zvOn` |
| *I*TurnOn | `ziOn` |
| *V*TurnOff | `zvOff` |
| *I*TurnOff | `ziOff` |

该模块通过对结温施加一个阶跃来应用开关损耗，该阶跃值等于开关损耗除以结处的总热质量。您必须指定单次开通和关断事件期间耗散的能量。您还必须指定您据以给出损耗的相应关断状态电压和导通状态电流值。您可以根据所拥有的数据对开关损耗进行参数化。如果有表格数据，请使用表格数据。

- 要为开关损耗指定标量值，请将 **On-state behavior and switching losses** 参数设置为 `Specify constant values`。**Switch-on loss** 和 **Switch-off loss** 参数值设置开关损耗的大小。该模块会根据关断状态电压和导通状态电流对损耗进行缩放。
- 要将损耗指定为固定关断状态电压下结温和导通状态电流的函数，请将 **On-state behavior and switching losses** 参数设置为 `Tabulate`，并清除 **Include switching loss tabulation with off-state Vds voltage** 参数。**Switch-on loss, Eon(Tj,Ids)** 和 **Switch-off, Eoff(Tj,Ids)** 参数设置损耗的大小。该模块会根据关断状态电压对损耗进行缩放。
- 要将损耗指定为结温、导通状态电流和关断状态电压的函数，请将 **On-state behavior and switching losses** 参数设置为 `Tabulate`，并选择 **Include switching loss tabulation with off-state Vds voltage** 参数。

反向恢复损耗可能是二极管中热损耗的重要来源。二极管每次从导通状态关断到开路状态时都会耗散能量。要对反向恢复损耗建模：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。

如果您将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`，则 **Reverse recovery loss table, Erec(Tj, If)** 参数的值指定了作为结温和紧接开关事件之前正向电流的函数的耗散能量。关断状态电压会相对于 **Turn-off voltage when measuring recovery loss, Vrec** 参数值线性缩放损耗。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage and current values** 参数设置为低于最快开关周期的值。

如果您将 **Reverse recovery loss model** 参数设置为 `Fixed loss`，则 **Reverse recovery loss** 参数的值指定了每次关断事件期间耗散的能量。如果您选择 **Scale reverse recovery loss with current and voltage** 参数，则该模块会按导通状态电流和关断状态电压线性缩放此损耗值。要使用接近瞬时值的缩放值，请将 **Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

作为对反向恢复建模的另一种方法，您可以将 **Integral protection diode** 参数设置为 `Diode with charge dynamics`。但是，与使用第一种方法相比，此方法需要更小的仿真时间步长。

**注意**

对于所有理想开关器件，记录的仿真数据将热损耗报告为 `lastTurnOffLoss`、`lastTurnOnLoss` 和 `lastReverseRecoveryLoss`。这些变量将损耗记录为幅值等于能量损耗的脉冲。如果您使用脚本对定义仿真时间段内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录的数据中提取导通损耗和开关损耗。

您还可以从记录的仿真数据中的 `accumulatedSwitchingLosses` 变量访问累计的总开关损耗。此变量汇总截至当前的所有开关损耗，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗或反向恢复损耗，因为该模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆导通状态损耗。

如果您使用固定步长求解器，支持捕获开关损耗的最短导通脉冲或关断脉冲为三个时间步长。如果脉冲短于三个步长，则该模块不报告开关损耗。

如果您在反向区域（负漏源电流）中操作 MOSFET，则记录的仿真数据不会报告任何开通或关断损耗，因为并联二极管提供持续并联导通。在记录的仿真数据中，`ziOn` 报告零电流以实现零损耗，即使电流阶跃到负值也是如此。

如果您使用表格数据对开关损耗或反向恢复损耗建模，请检查温度、电流和电压是否在您指定的范围内。如果您未定义真实的热模型，例如，如果结质量或从结到外壳的传导过小，则温度可能超出您指定的范围，导致该模块将损耗外推到非物理值。

### 参数化

MOSFET (Ideal, Switching) 模块支持多个预定义参数化。

使用此参数化数据表示特定供应商的元件。这些 MOSFET 的参数化与制造商数据表匹配。要加载预定义参数化，请双击 MOSFET (Ideal, Switching) 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用元件列表中选择要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用的数据源来获取参数值。工程判断和简化假设用于填补缺失数据。因此，预期仿真行为与实际物理行为之间存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预定义参数化和可用组件列表的详细信息，请参阅 List of Pre-Parameterized Components。

您还可以使用 `ee_importDeviceParameters` 函数从 XML 文件提取器件参数，并将其导入到该模块。该 XML 文件必须位于 MATLAB® 路径上，并且必须使用 Hitachi 支持的参数化格式。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

*自 R2023b 起*

您无需构建完整模型即可绘制 MOSFET (Ideal, Switching) 模块的基本 I-V 特性。使用这些图可探究您的参数选择对器件特性的影响。如果您根据数据表对模块进行参数化，则可以将图与数据表进行比较，以检查您是否正确参数化了模块。如果您有一个完整的工作模型，但不知道使用哪个制造部件，则可以将图与数据表进行比较，以帮助您做出决定。

要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。

**Basic characteristics** 选项会根据您为 MOSFET (Ideal, Switching) 模块的 **Modeling option**、**On-state behavior and losses** 和 **Integral protection diode** 参数指定的值生成不同的图。如果您使用集成保护二极管对开关器件建模，则 **Basic characteristics** 选项会绘制开关器件和二极管的 I-V 特性。如果您启用该模块的热端口，则 **Basic characteristics** 选项还会生成开通能量损耗和关断能量损耗作为导通状态电流和关断状态电压函数的曲面图。有关此选项的详细信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
