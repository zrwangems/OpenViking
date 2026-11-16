---
type: simulink-block
title: 'IGBT (Ideal, Switching)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'igbtidealswitching'
documentation_source_path: 'ref/igbtidealswitching.html'
language: zh-CN
chinese_source: worker-translation
---

# IGBT (Ideal, Switching)

## 端口

### 守恒

### **G** — 栅极端子 electrical

与栅极端子关联的端口。您可以将该端口设置为物理信号或电气端口。

### **C** — 集电极端子 electrical

与集电极端子关联的电气守恒端口。

### **E** — 发射极端子 electrical

与发射极端子关联的电气守恒端口。

### **H** — 热端口 thermal

热守恒端口。

#### 依赖关系

要启用此端口，请将**建模选项**设置为
`Show thermal port`。

### **HDiode** — 集成保护二极管的热端口 thermal

*自 R2024b 起*

与集成保护二极管关联的热守恒端口。

#### 依赖关系

要启用此端口，请选中**为集成二极管单独设置热端口**
参数。

## 参数

### **建模选项** — 热端口可见性 `No thermal port`（默认）| `Show thermal port`

是否启用热端口。

### **选定部件** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商组件的选项。单击
**<click to select>** 超链接以打开模块参数化管理器窗口。有关模块参数化
管理器的详细信息，请参阅加载预定义参数化。

### 主要

此表显示了 **主要** 参数的可见性如何取决于您对**建模选项**和**通态
行为及开关损耗**参数的配置。要了解如何阅读此表，
请参阅参数依赖关系。

**主要参数依赖关系**

| 参数和选项 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **建模选项** | | | | | | | |
| *`No thermal port`* | | | | *`Show thermal port`* | | | |
| 栅极控制端口 | | | | 栅极控制端口 | | | |
| 正向电压, Vf | | | | 阈值电压, Vth | | | |
| 通态电阻 | | | | **通态行为及开关损耗** | | | |
| *`Specify constant values`* | *`Tabulate`* | | |
| 断态电导 | | | | 正向电压, Vf | 通态电压, Vce(Tj,Ice) | | |
| 阈值电压, Vth | | | | 通态电阻 | 温度向量, Tj | | |
| 断态电导 | 集电极-发射极电流向量, Ice | | |
| 断态电导 | | |

### **栅极控制端口** — 用于指定物理或电气控制端口的选项 `PS`（默认）| `Electrical`

用于为开关栅极指定物理或电气控制端口的选项。

### **通态行为及开关损耗** — 通态行为和开关损耗数据 `Specify constant values`（默认）| `Tabulate`

通态行为和开关损耗的参数化方法，指定为以下值之一：

- `Specify constant values` — 使用标量
  值指定输出电流、开通损耗和关断
  损耗数据。该模块假定单次开通或关断事件期间耗散的能量
  随断态电压和通态电流线性缩放。该模块还假定
  损耗与温度无关。
- `Tabulate` — 使用向量指定
  输出电流和温度数据。使用数组指定
  开通损耗和关断损耗数据。

#### 依赖关系

请参阅主要参数依赖关系表。

### **正向电压, Vf** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性的梯度为
1/*Ron* 所需的集电极和发射极模块端口两端的最小电压，其中
*Ron* 是
**通态电阻**的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **通态电阻** — 通态集电极-发射极电阻 `0.001` `Ohm`（默认）

器件导通时的集电极-发射极电阻。

#### 依赖关系

请参阅主要参数依赖关系表。

### **断态电导** — 断态集电极-发射极电导 `1e-5` `1/Ohm`（默认）

器件关断时的集电极-发射极电导。该值必须小于
1/*R*，其中 *R* 是
**通态电阻**的值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **阈值电压, Vth** — 阈值电压 `6` `V`（默认）

器件导通时的栅极-发射极电压。

#### 依赖关系

请参阅主要参数依赖关系表。

### **通态电压, Vce(Tj,Ice)** — 通态电压 `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V`（默认）| 非负标量矩阵

器件在触发导通状态下的电压降。此
参数是温度和最终通态输出电流的函数。

#### 依赖关系

请参阅主要参数依赖关系表。

### **温度向量, Tj** — 温度值 `[298.15, 398.15]` `K`（默认）

对应于 **通态电压,
Vce(Tj,Ice)** 参数的温度值。

#### 依赖关系

请参阅主要参数依赖关系表。

### **集电极-发射极电流向量, Ice** — 集电极-发射极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）

定义通态电压所对应的集电极-发射极电流。第一个元素必须为零。使用向量
指定此参数。

#### 依赖关系

请参阅主要参数依赖关系表。

### 开关损耗

要启用这些参数，请将**建模选项**设置为
`Show thermal port`。

### **开通损耗** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Specify constant
values`。

### **关断损耗** — 关断损耗 `17.14e-3` `J`（默认）| 正标量

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Specify constant
values`。

### **开关损耗数据的断态电压** — 开关损耗数据的断态电压 `300` `V`（默认）| 正标量

器件在断态期间的输出电压。此值是您定义开通损耗和关断损耗
数据的阻断电压。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将**通态行为及开关损耗**
  设置为 `Specify constant values`。
- 将**通态行为及开关损耗**
  设置为 `Tabulate` 并清除
  **包含断态电压的开关损耗制表**
  参数。

### **开关损耗数据的通态电流** — 开关损耗数据的通态电流 `600` `A`（默认）| 正标量

定义开通损耗和关断
损耗时的输出电流。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Specify constant
values`。

### **使用上一周期的最后通态电流计算开通损耗** — 使用上一周期的最后通态电流计算开通损耗的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用上一周期的最后通态电流计算
开通损耗的选项。

### **使用上一周期的最后断态电压计算关断损耗** — 使用上一周期的最后断态电压计算关断损耗的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用上一周期的最后断态电压计算
关断损耗的选项。

### **开通损耗, Eon(Tj,Ice)** — 开通损耗 `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J`（默认）| 非负标量矩阵

单次开通事件期间耗散的能量，表示为
温度和通态电流的函数。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate` 并清除
**包含断态电压的开关损耗制表**
参数。

### **关断损耗, Eoff(Tj,Ice)** — 关断损耗 `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J`（默认）| 非负标量矩阵

单次关断事件期间耗散的能量，表示为
温度和通态电流的函数。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate` 并清除
**包含断态电压的开关损耗制表**
参数。

### **开关损耗的温度向量, Tj** — 开关损耗的温度 `[298.15, 398.15]` `K`（默认）| 向量

您给出开通损耗和关断
损耗时所对应的温度值。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate`。

### **开关损耗的集电极-发射极电流向量, Ice** — 开关损耗的集电极-发射极电流向量 `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A`（默认）| 非负标量向量

您给出开通损耗和
关断损耗时所对应的集电极-发射极电流。第一个元素必须为 `0`。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate`。

### **包含断态电压的开关损耗制表** — 使用断态电压对开关损耗制表的选项 `Off`（默认）| `On`

*自 R2023b 起*

使用断态电压对开关损耗制表的选项。

要使用通态电流
和温度对开通损耗和关断损耗制表，请清除此参数。该模块假定损耗随
断态电压线性缩放。

要使用温度、
通态电流和断态电压对开通损耗和关断损耗制表，请选中此参数。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate`。

### **开通损耗, Eon(Tj,Ids,Vce)** — 开通损耗 `[zeros(2, 9, 3)]` `J`（默认）| 非负标量的三维数组

*自 R2023b 起*

单次开通事件期间耗散的能量，表示为
温度、通态电流和断态电压的函数。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate` 并选中
**包含断态电压的开关损耗制表**
参数。

### **关断损耗, Eoff(Tj,Ids,Vce)** — 关断损耗 `[zeros(2, 9, 3)]` `J`（默认）| 非负标量的三维数组

*自 R2023b 起*

单次关断事件期间耗散的能量，表示为
温度、电流和断态电压的函数。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate` 并选中
**包含断态电压的开关损耗制表**
参数。

### **开关损耗数据的断态电压向量, Vce** — 开关损耗数据的断态电压向量 `[0, 150, 300]` `V`（默认）| 向量

*自 R2023b 起*

您给出开通损耗
和关断损耗时所对应的断态集电极-发射极电压。

#### 依赖关系

要启用此参数，请将**通态行为及开关
损耗**设置为 `Tabulate` 并选中
**包含断态电压的开关损耗制表**
参数。

### 集成二极管

### **集成保护二极管** — 集成保护二极管 `External diode`（默认）| `Protection diode with no dynamics` | `Protection diode with charge dynamics`

IGBT (Ideal, Switching) 模块用于集成保护二极管的模型。
选择以下选项之一：

- `External diode` — IGBT (Ideal, Switching) 不
  对集成保护二极管建模。请使用外部 Diode 模块。
- `Diode with no dynamics` — IGBT (Ideal, Switching)
  模块使用与无动态 Diode 模块相同的方程
  对集成保护二极管建模。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — IGBT (Ideal, Switching)
  模块使用与电荷动态 Diode 模块相同的方程
  对集成保护二极管建模。选择此选项可优先考虑详细的仿真
  结果。

### **二极管模型** — 二极管模型 `Piecewise Linear`（默认）| `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 使用
  二极管的分段线性模型，如分段线性二极管中所述。这是
  默认方法。
- `Tabulated I-V curve` — 使用
  表格化的正向偏置 I-V 数据以及固定的反向偏置断态
  电导。

#### 依赖关系

仅当热端口暴露且
**集成保护二极管**参数设置为
`Protection diode with no dynamics` 或
`Protection diode with charge dynamics` 时，此参数才可见。

### **表格类型** — 表格化函数 `Table in If(Tj,Vf) form`（默认）| `Table in Vf(Tj,If) form`

是将电流表格化为温度和电压的函数，还是
将电压表格化为温度和电流的函数。

#### 依赖关系

仅当热端口暴露且
**集成保护二极管**参数设置为
`Protection diode with no dynamics` 或
`Protection diode with charge dynamics`，并且
**二极管模型**设置为 `Tabulated I-V
curve` 时，此参数才可见。

### **反向 I-V 特性类型** — 反向 I-V 特性的类型 `Specify off conductance`（默认）| `Tabulate`

*自 R2024a 起*

是使用二极管断态电导指定反向 I-V 特性，还是通过将电流表格化为温度和电压的函数或电压表格化为温度和电流的函数来指定反向 I-V 特性。

#### 依赖关系

仅当热端口暴露且 **集成保护二极管**参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，并且 **二极管模型**设置为 `Tabulated I-V curve` 时，此参数才可见。

### **正向电压** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性的梯度为
1/*R*on 所需的 `+` 和 `-` 模块端口两端的最小电压，其中
*R*on 是 **导通电阻** 参数的值。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，请将**集成保护
  二极管**设置为 `Diode with no
  dynamics` 或 `Diode with charge
  dynamics`。
- 如果热端口暴露，请将**集成保护
  二极管**设置为 `Diode with no
  dynamics` 或 `Diode with charge
  dynamics`，并将**二极管模型**设置为
  `Piecewise linear`。

### **导通电阻** — 导通电阻 `0.001` `Ohm`（默认）

高于 **正向电压**
参数值时电压相对电流的变化率。

#### 依赖关系

要启用此参数：

- 如果热端口隐藏，请将**集成保护
  二极管**设置为 `Diode with no
  dynamics` 或 `Diode with charge
  dynamics`。
- 如果热端口暴露，请将**集成保护
  二极管**设置为 `Diode with no
  dynamics` 或 `Diode with charge
  dynamics`，并将**二极管模型**设置为
  `Piecewise linear`。

### **正向电流, If(Tj,Vf)** — 正向电流向量 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）| 非负向量

正向电流。此参数必须为至少包含三个
非负元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将**二极管
模型**设置为 `Tabulated I-V curve`，将
**表格类型**设置为 `Table in If(Tj,Vf)
form`。

### **结温, Tj** — 结温向量 `[25, 125]` `degC`（默认）

结温向量。此参数必须为至少包含两个
元素的向量。

#### 依赖关系

要启用此参数，请暴露热端口，并将**二极管
模型**设置为 `Tabulated I-V
curve`。

### **正向电压, Vf** — 正向电压向量 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

正向电压向量。此参数必须为至少包含三个
非负值的向量。

#### 依赖项

要启用此参数，请显示热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in If(Tj,Vf) form`。

### **Forward voltages, Vf(Tj,If)** — 正向电压向量 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认） | 非负向量

正向电压。此参数必须为至少包含三个非负元素的向量。

#### 依赖项

要启用此参数，请显示热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Forward currents, If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

正向电流向量。此参数必须为至少包含三个非负值的向量。

#### 依赖项

要启用此参数，请显示热端口，并将 **Diode model** 设置为 `Tabulated I-V curve`，将 **Table type** 设置为 `Table in Vf(Tj,If) form`。

### **Reverse currents, Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认） | 非负向量

*自 R2024a 起*

反向电流。此参数必须为至少包含三个非负元素的向量。

#### 依赖项

要启用此参数，请设置：

- 将 **Modeling option** 设置为 `Show thermal port`
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- 将 **Diode model** 设置为 `Tabulated I-V curve`
- 将 **Table type** 设置为 `Table in If(Tj,Vf) form`
- 将 **Reverse I-V characteristics** 设置为 `Tabulate`

### **Reverse voltages, Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认） | 非负向量

*自 R2024a 起*

反向电压向量。此参数必须为至少包含三个非负值的向量。

#### 依赖项

要启用此参数，请设置：

- 将 **Modeling option** 设置为 `Show thermal port`
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- 将 **Diode model** 设置为 `Tabulated I-V curve`
- 将 **Table type** 设置为 `Table in If(Tj,Vf) form`
- 将 **Reverse I-V characteristics** 设置为 `Tabulate`

### **Reverse voltages, Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认） | 非负向量

*自 R2024a 起*

反向电压。此参数必须为至少包含三个非负元素的向量。

#### 依赖项

要启用此参数，请设置：

- 将 **Modeling option** 设置为 `Show thermal port`
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- 将 **Diode model** 设置为 `Tabulated I-V curve`
- 将 **Table type** 设置为 `Table in Vf(Tj,If) form`
- 将 **Reverse I-V characteristics** 设置为 `Tabulate`

### **Reverse currents, Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认） | 非负向量

*自 R2024a 起*

反向电流向量。此参数必须为至少包含三个非负值的向量。

#### 依赖项

要启用此参数，请设置：

- 将 **Modeling option** 设置为 `Show thermal port`
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`
- 将 **Diode model** 设置为 `Tabulated I-V curve`
- 将 **Table type** 设置为 `Table in Vf(Tj,If) form`
- 将 **Reverse I-V characteristics** 设置为 `Tabulate`

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`，且 **Reverse I-V characteristics type** 设置为 `Specify off conductance` 时，此参数才可见。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认） | `Tabulated loss`

*自 R2023a 起*

是否对固定或表格化反向恢复损耗进行建模。

#### 依赖项

要启用此参数，请将 **Modeling option** 参数设置为 `Show thermal port`，并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认） | 非负标量

*自 R2023a 起*

每次关断事件中耗散的能量。无论开关事件之前或之后二极管的状态如何，该模块都会耗散此能量。

#### 依赖项

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 使用电流和电压缩放反向恢复损耗的选项 `On`（默认） | `Off`

*自 R2023b 起*

使用电流和电压缩放反向恢复损耗的选项。

#### 依赖项

要启用此参数：

- 将 **Modeling option** 设置为 `Show thermal port`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Reverse recovery loss table, Erect(Tj), If** — 反向恢复损耗 `zeros(2,3)` `J`（默认） | 非负标量向量

*自 R2023a 起*

耗散能量，是开关事件刚发生前的正向电流 *If* 以及二极管处于关断状态后的最终关态电压的函数。

#### 依赖项

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15 398.15]` `K`（默认） | 向量

*自 R2023a 起*

模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖项

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `K`（默认） | 非负标量向量

*自 R2023a 起*

模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖项

要启用此参数，请将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current when measuring recovery loss, Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认） | 正标量

*自 R2023b 起*

模块用于测量恢复损耗的反向恢复事件之前流过二极管的正向电流。

#### 依赖项

要启用此参数，请将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选择 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认） | 正标量

*自 R2023a 起*

模块用于测量恢复损耗的反向恢复事件之后二极管两端的电压。

#### 依赖项

要启用此参数，请从以下选项中选择一项：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选择 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波器时间常数 `1 / 1000 / 100` `s`（默认） | 正标量

*自 R2023a 起*

模块用于计算反向恢复损耗的电压和电流值的滤波器时间常数。将此参数设置为低于最快开关周期的值。

#### 依赖项

要启用此参数，请从以下选项中选择一项：

- 将 **Reverse recovery loss model** 设置为 `Fixed loss`，并选择 **Scale reverse recovery loss with current and voltage** 参数。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Junction capacitance** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认） | 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认） | 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认） | 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认） | `Specify stretch factor` | `Specify reverse recovery charge`

确定如何在模块中指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需要指定一个值，模块使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数才可见。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认） | 标量

电流初始降为零（二极管关断时）的时间与电流降至峰值反向电流的 10% 以下的时间之间的间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery time directly` 时，此参数才可见。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认） | 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简单方法。拉伸因子的值越大，反向恢复电流耗散所需的时间越长。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify stretch factor` 时，此参数才可见。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据表指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery charge` 时，此参数才可见。

### **Diode turn-off voltage when measuring Erec** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认）

稳态时二极管两端的电压。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Stray inductance when measuring Erec** — 测量 Erec 时的杂散电感 `150` `nH`（默认）

测量电路中的总非预期电感。模块使用此值计算 **Reverse recovery energy, Erec**。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### **Reverse recovery energy, Erec** — 反向恢复能量 `0.03` `J`（默认）

由于二极管反向恢复引起的总开关损耗。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics`，且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery energy` 时，此参数才可见。

### 热端口

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### **Separate thermal port for integral diode** — 为集成二极管分离热端口的选项 `off`（默认） | `on`

*自 R2024b 起*

是否分离器件的集成保护二极管的热端口。

#### 依赖项

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`，并在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Thermal network** — 热网络建模选项 `External`（默认） | `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

模块热网络建模的选项。

### **Thermal mass parameterization** — 参数化热质量的选项 `By thermal time constants`（默认） | `By thermal mass`

参数化热质量的选项：

- `By thermal time constants` — 根据热时间常数参数化热质量。
- `By thermal mass` — 直接指定热质量值。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结到壳以及壳到环境（或壳到散热器）的热阻 `[.08, .5]` `K/W`（默认） | 正值向量

行向量 [ *R\_JC* *R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和壳的热时间常数 `[.001, .2]` `s`（默认） | 正值向量

行向量 [ *t\_J* *t\_C* ]，包含两个热时间常数值。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结温和壳温热质量 `[.01, .5]` `J/K`（默认） | 正值向量

行向量，[ *M\_J*
*M\_C* ]，包含两个热质量值。第一个值 *M\_J* 是结温热质量。第二个值 *M\_C* 是壳温热质量。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结温和壳温初始温度 `[25, 25]` `degC`（默认） | 正值向量

行向量，[ *T\_J* *T\_C* ]，包含两个温度值。第一个值 *T\_J* 是结温初始温度。第二个值 *T\_C* 是壳温初始温度。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 用于集成保护二极管的结-壳温和壳-环境（或壳-散热器）热阻 `[.03, .2]` `K/W`（默认） | 正值向量

*自 R2024b 起*

行向量，[ *R\_JC*
*R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示，用于集成保护二极管。第一个值 *R\_JC* 是结温与壳温之间的热阻。第二个值 *R\_CA* 是端口 **HDiode** 与二极管壳温之间的热阻。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal time constants of diode junction and case, [t\_J t\_C]** — 用于集成二极管的结温和壳温热时间常数 `[.1, 5]` `s`（默认） | 正值向量

*自 R2024b 起*

行向量，[ *t\_J*
*t\_C* ]，包含集成保护二极管的两个热时间常数值。第一个值 *t\_J* 是结温时间常数。第二个值 *t\_C* 是壳温时间常数。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Thermal masses of diode junction and case, [M\_J M\_C]** — 二极管结温和壳温热质量 `[3, 25]` `J/K`（默认） | 正值向量

*自 R2024b 起*

行向量，[ *M\_J*
*M\_C* ]，包含集成保护二极管的两个热质量值。第一个值 *M\_J* 是结温热质量。第二个值 *M\_C* 是壳温热质量。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Initial temperatures of diode junction and case, [T\_J T\_C]** — 二极管结温和壳温初始温度 `[25, 25]` `degC`（默认） | 正值向量

*自 R2024a 起*

行向量，[ *T\_J* *T\_C* ]，包含集成保护二极管的两个温度值。第一个值 *T\_J* 是结温初始温度。第二个值 *T\_C* 是壳温初始温度。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.08, .1, .5]` `K/W` | `[.08, .14, .22, .16]` `K/W` | 正值向量

由热网络中使用的 Cauer 元件表示的 *n* 个热阻值组成的行向量。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.08, .1, .5]`。
如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[.08, .14, .22, .16]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[.001, .1, .2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正值向量

由 *n* 个热时间常数值组成的行向量，其中 *n* 是热网络中使用的 Cauer 元件数。此向量的长度必须与 **Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化时，热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.001, .1, .2]`。
如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[7e-05, .0007, .01, .08]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[.01, .1, .5]` `J/K` | `[.001, .005, .05, .5]` `J/K` | 正值向量

由 *n* 个热质量值组成的行向量，其中 *n* 是热网络中的 Cauer 元件数。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.01, .1, .5]`。
如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[.001, .005, .05, .5]`。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认） | 正值向量

温度值行向量，对应于模型中每个热容两端的温度降。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **Diode thermal resistances, [R1 R2 … Rn]** — 用于集成二极管的热阻 `[.03, .1, .2]` `K/W` | `[.03, .2]` `K/W` | 正值向量

*自 R2024b 起*

由 *n* 个热阻值组成的行向量，用于集成保护二极管，由热网络中使用的 Cauer 元件表示。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.03, .1, .2]`。
如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[.03, .2]`。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Diode thermal time constants, [t1 t2 … tn]** — 用于集成二极管的热时间常数 `[.1, 1, 5]` `s` | `[1, 10]` `s` | 正值向量

*自 R2024b 起*

由 *n* 个热时间常数值组成的行向量，用于集成保护二极管，其中 *n* 是热网络中使用的 Cauer 元件数。此向量的长度必须与 **Diode thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化时，热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.1, 1, 5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[1, 10]`。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Diode thermal masses, [M1 M2 … Mn]** — 用于集成二极管的热质量 `[3, 10, 25]` `J/K` | `[33, 50]` `J/K` | 正值向量

*自 R2024b 起*

由 *n* 个热质量值组成的行向量，用于集成保护二极管，其中 n 是热网络中的 Cauer 元件数。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[3, 10, 25]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[33, 50]`。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。
  - 将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Initial temperatures of diode thermal masses, [T1 T2 … Tn]** — 二极管热质量初始温度 `[25, 25, 25]` `degC`（默认） | 正值向量

*自 R2024b 起*

用于集成保护二极管的温度值行向量。此参数对应于模型中每个热容两端的温度降。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model`。

### **Initial node temperatures, [T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认） | 正值向量

从结温开始的每个节点的温度值行向量。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Diode initial node temperatures, [T1 T2 ... Tn]** — 用于集成二极管的初始节点温度 `[25, 25, 25, 25]` `degC`（默认） | 正值向量

*自 R2024b 起*

从集成保护二极管结温开始的每个节点的温度值行向量。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Junction thermal mass** — 结温热质量 `0.01` `J/K`（默认） | 正标量

结温热质量。

#### 依赖项

要启用此参数，请将 **Thermal network** 设置为 `External`。

### **Diode junction thermal mass** — 二极管结温热质量 `0.1` `J/K`（默认） | 正标量

*自 R2024b 起*

二极管结温热质量。

#### 依赖项

要启用此参数：

- 在 **Integral Diode** 部分中，将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal Port** 部分中：

  - 选择 **Separate thermal port for integral diode** 参数。
  - 将 **Thermal network** 设置为 `External`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b：为集成二极管提供单独的热端口

现在，您可以将 IGBT (Ideal, Switching) 模块的集成保护二极管的热端口与 **H** 端口分开。要分开热端口：

- 将 **Modeling option** 参数设置为 `Show thermal port`
- 在 **Integral Diode** 部分中，将 **Integral protection diode** 参数设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。
- 在 **Thermal port** 部分中，选择 **Separate thermal port for integral diode** 参数。

### R2024a：对表格化反向 I-V 特性建模

现在，您可以通过将电流表示为温度和电压的函数，或将电压表示为温度和电流的函数，来为 IGBT (Ideal, Switching) 模块的反向 I-V 特性建模。

在 R2024a 之前，您只能通过指定反向偏置二极管的关断电导来对反向 I-V 特性建模。

### R2023b：使用内置参数化对特定 IGBT 建模

现在，您可以使用表示特定供应商组件的内置参数化来参数化 IGBT (Ideal, Switching) 模块。这些理想绝缘栅双极晶体管 (IGBT) 的参数化与制造商数据表匹配。要加载预定义参数化，请双击 IGBT (Ideal, Switching) 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

### R2023b：随电流和电压缩放反向恢复损耗

现在，您可以随电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **Scale reverse recovery loss with current and voltage** 参数。

在 R2023a 或更早版本中创建的模型默认不进行缩放，以保持向后兼容性。

### R2023b：用温度、电流和电压表格化开关损耗

现在，您可以用温度、电流和电压表格化开关损耗。在早期版本中，您只能使用温度和电流表格化开关损耗。

要将损耗指定为结温、导通状态电流和关断状态电压的函数，请将 **On-state behavior and switching losses** 参数设置为 `Tabulate`，并选择 **Include switching loss tabulation with off-state voltage** 参数。

### R2023b: 确定不连续负载电流的开关损耗

IGBT (Ideal, Switching) 模块现在支持不连续负载电流。

该模块通过在所有开通和关断事件中测量关断状态电压和导通状态电流来计算开关损耗，从而支持不连续负载电流。新模型默认采用此行为。如果您使用固定步长求解器，器件最短导通或关断周期现在为一个步长。在 R2023b 之前，最小周期为三个步长。要报告开关损耗，最小周期仍为三个步长。

在 R2023b 之前，该模块仅测量开通前的关断状态电压和关断前的导通状态电流。

在 R2023b 中，您仍然可以使用原始方法，即测量开通前的关断状态电压和关断前的导通状态电流。为向后兼容，您在 R2023a 或更早版本中创建的模型默认采用此行为。原始方法专为具有连续电流的感性负载而设计。如果您要对开关器件两端的电容或开关器件引线电感建模，请使用原始方法：

- 要对开关器件两端的电容建模，例如，如果并联二极管具有电容，或者您使用的是 Lauritzen 电荷模型，请选择 **使用上一周期的最后导通状态电流计算开通损耗** 参数。
- 要对开关器件引线电感建模，请选择 **使用上一周期的最后关断状态电压计算关断损耗** 参数。

### R2023b: 绘制基本 I-V 特性

现在，您可以基于当前模块参数值，在无需对模型进行仿真的情况下，绘制 IGBT (Ideal, Switching) 模块的基本 I-V 特性。

要绘制基本特性，请右键点击该模块，然后从上下文菜单中选择 **电气** > **基本特性**。

如果您使用集成保护二极管对开关器件建模，则 **基本特性** 选项会绘制开关器件和二极管的 I-V 特性。如果您启用模块的热端口，则 **基本特性** 选项还会生成开通能量损耗和关断能量损耗随导通状态电流和关断状态电压变化的曲面图。

### R2023a: 集成二极管建模选项更新

从 R2023a 开始，您可以在 IGBT (Ideal, Switching) 模块中对反向恢复损耗建模。要启用 **反向恢复损耗模型** 参数，请将 **建模选项** 参数设置为 `Show thermal port`，并将 **集成保护二极管** 参数设置为 `Diode with no dynamics`。

### R2021a: 移除能量耗散时间常数参数

从 R2021a 开始，不再使用 IGBT (Ideal, Switching) 模块的 **能量耗散时间常数** 参数。结温的阶跃现在反映开关损耗。如果您的模型包含直接连接到该模块热端口的热质量，请将其移除，并在组件自身内部对热质量建模。

### R2020b: 开关损耗和热建模选项更新

从 R2020b 开始，IGBT (Ideal, Switching) 模块具有改进的损耗和热建模选项。

这些更改带来以下结果：

- 电气导通状态损耗和热导通状态损耗现在始终相同。**热损耗取决于** 参数及其选项 `Voltage and current` 和 `Voltage, current, and temperature` 已重命名为 **导通状态行为和开关损耗**、`Specify constant values` 和 `Tabulate with temperature and current`：

  - 如果您为 **热损耗取决于** 选择了 `Voltage and current`，则电气导通状态损耗不变，其值使用导通状态电阻确定。但是，热导通状态损耗现在也由导通状态电阻确定。在 R2020b 之前，热导通状态损耗由 **导通状态电压** 和 **输出电流, Iout** 参数的乘积定义。
  - 如果您为 **热损耗取决于** 选择了 `Voltage, current, and temperature`，则热导通状态损耗不变，其值由 **导通状态电压, Vds(Tj,Ice)** 参数设置。但是，电气导通状态损耗现在等于热导通状态损耗。在 R2020b 之前，电气导通状态损耗由导通状态电阻的值定义。
- 不再使用 **导通状态电压** 参数。

## 描述

用于开关应用的理想绝缘栅双极晶体管

IGBT (Ideal, Switching) 模块用于对开关应用中的理想绝缘栅双极晶体管 (IGBT) 建模。IGBT 的开关特性为：如果栅极-发射极电压超过指定的阈值电压 *Vth*，则 IGBT 处于导通状态。否则，器件处于关断状态。下图显示了典型的 *i-v 特性*：

要定义 IGBT 的 I-V 特性，请将 **导通状态行为和开关损耗** 参数设置为 `Specify constant values` 或 `Tabulate`。仅当您显示模块的热端口时，`Tabulate` 选项才可用。

在导通状态下，集电极-发射极路径的行为类似于具有正向电压降 *Vf* 和导通电阻 *Ron* 的线性二极管。但是，如果您显示模块的热端口，并使用表格化 I-V 数据对器件进行参数化，则表格化电阻是温度和电流的函数。

在关断状态下，集电极-发射极路径的行为类似于具有低关断状态电导值 *Goff* 的线性电阻。

用于该模块的定义性 Simscape™ 方程为：

         if (v>Vf)&&(G>Vth)
            i == (v - Vf*(1-Ron*Goff))/Ron;
         else
            i == v*Goff;
         end

其中：

- *v* 是集电极-发射极电压。
- *Vf* 是正向电压。
- *G* 是栅极-发射极电压。
- *Vth* 是阈值电压。
- *i* 是集电极-发射极电流。
- *Ron* 是导通状态电阻。
- *Goff* 是关断状态电导。

### 集成保护二极管选项

使用 **集成二极管** 参数，您可以包含一个集成的发射极-集电极二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断对负载的电压供应时，感性负载可能产生高反向电压尖峰。

根据您的目标设置 **集成保护二极管** 参数。

| 目标 | 要选择的值 | 模块行为 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | 模块包含 Diode 模块的集成副本。要对内部 Diode 模块进行参数化，请使用 **保护** 参数。 |
| 精确指定反向模式电荷动态。 | `Diode with charge dynamics` | 模块包含 Diode 模块动态模型的集成副本。要对内部 Diode 模块进行参数化，请使用 **保护** 参数。 |

### 对栅极端口和热效应建模

您可以选择物理端口或电气端口来控制栅极端子，并显示热端口以对开关事件和导通损耗产生的热量建模。要选择栅极控制端口，请将 **栅极控制端口** 参数设置为 `PS` 或 `Electrical`。要显示热端口，请将 **建模选项** 参数设置为 `No thermal port` 或 `Show thermal port`。

您还可以通过选择 **为集成二极管单独设置热端口** 参数来显示集成保护二极管的热端口 **HDiode**。如果不显示二极管热端口，则器件和二极管共享公共热端口 **H**。*（自 R2024b 起）*

有关使用热端口的详细信息，请参阅对半导体中的热效应进行仿真。

### 热损耗

该图显示了半导体器件的输出电压 *V*out 和输出电流 *I*out 的理想化表示。该图中的区间包括整个第 *n* 个开关周期，在此期间模块先关断然后开通。

开关损耗是半导体热损耗的主要来源。在每次开-关切换过程中，IGBT 寄生参数会存储能量，然后耗散能量。

开关损耗取决于断态电压和通态电流。当开关器件开通时，功率损耗取决于器件两端的初始断态电压以及器件完全导通时的最终通态电流。类似地，当开关器件关断时，功率损耗取决于器件中的初始通态电流以及器件完全关断时的最终断态电压。

您可以选择何时测量模块用于计算开通损耗和关断损耗的电流和电压。对于大多数电路，您可以在开通或关断事件期间进行测量：

- 开通损耗为
  *E*on*(I*TurnOn*(n),V*TurnOn*(n))*
- 关断损耗为
  *E*off*(I*TurnOff*(n),V*TurnOff*(n))*

但是，您不能始终使用这些测量值，例如在以下情况下：

- 您正在对开关器件两端的电容建模。例如，您正在对带电容的保护二极管建模，或者您正在使用 Lauritzen 电荷模型。该电容会在器件开通时导致电流过冲瞬态，这意味着您不能使用测量值 *I*TurnOn*(n)* 来计算开通损耗。模块需要瞬态之后的值。不要对开关器件两端的电容建模，因为此模型将半导体开关器件的抽象行为与二极管的详细物理特性混合在一起。如果必须对开关器件两端的电容建模，可以使用最后一个导通周期结束时的电流测量值，*I*TurnOff*(n-1)*。要启用此选项，请选中 **使用上一周期的最后通态电流计算开通损耗** 参数。
- 您正在对开关器件引线电感建模。该电感会在器件关断时导致电压过冲瞬态，这意味着您不能使用测量值 *V*TurnOff*(n)* 来计算关断损耗。模块需要瞬态之后的值。不要对开关器件引线电感建模，因为与引线电感相关的时间常数通常远小于脉冲宽度调制 (PWM) 周期。这个较小的时间常数意味着仿真需要更小的仿真时间步长，从而减慢仿真速度。如果必须对开关器件引线电感建模，请使用最后一个关断周期结束时的电压测量值，*V*TurnOn*(n)*。要启用此选项，请选中 **使用上一周期的最后断态电压计算关断损耗** 参数。

检查仿真结果，确认损耗行为符合预期。要了解如何记录和绘制仿真数据，请参阅记录和绘制仿真数据示例。此表定义了记录仿真数据中与开关损耗计算相关的变量名称。

**用于计算开关损耗的电压和电流**

| 物理量 | 记录的仿真数据中的变量名 |
| --- | --- |
| *V*TurnOn | `zvOn` |
| *I*TurnOn | `ziOn` |
| *V*TurnOff | `zvOff` |
| *I*TurnOff | `ziOff` |

此模块通过将结温升高（升高值等于开关损耗除以结处总热质量）来施加开关损耗。您必须指定单次开通和关断事件期间耗散的能量。您还必须指定您给出损耗时所对应的断态电压和通态电流值。您可以根据拥有的数据对开关损耗进行参数化。如果有表格数据，请使用表格数据。

- 要将开关损耗指定为标量值，请将 **通态行为和开关损耗** 参数设置为 `Specify constant values`。**开通损耗** 和 **关断损耗** 参数值设置开关损耗的大小。模块按断态电压和通态电流对损耗进行缩放。
- 要在固定断态电压下将损耗指定为结温和通态电流的函数，请将 **通态行为和开关损耗** 参数设置为 `Tabulate`，并清除 **包含断态电压的开关损耗表格** 参数。**开通损耗, Eon(Tj,Ice)** 和 **关断损耗, Eoff(Tj,Ice)** 参数设置损耗的大小。模块按断态电压对损耗进行缩放。
- 要将损耗指定为结温、通态电流和断态电压的函数，请将 **通态行为和开关损耗** 参数设置为 `Tabulate`，并选中 **包含断态电压的开关损耗表格** 参数。

反向恢复损耗可能是二极管热损耗的重要来源。二极管每次从导通状态切换到开路状态时都会耗散能量。要对反向恢复损耗建模：

- 将 **建模选项** 设置为 `Show thermal port`。
- 将 **集成保护二极管** 设置为 `Diode with no dynamics`。

如果将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`，则 **反向恢复损耗表, Erec(Tj, If)** 参数的值指定耗散能量，该能量是结温和紧邻开关事件之前的正向电流的函数。断态电压相对于 **测量恢复损耗时的关断电压, Vrec** 参数值对损耗进行线性缩放。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **电压和电流值的滤波时间常数** 参数设置为小于最快开关周期的值。

如果将 **反向恢复损耗模型** 参数设置为 `Fixed loss`，则 **反向恢复损耗** 参数的值指定每个关断事件期间耗散的能量。如果选中 **用电流和电压缩放反向恢复损耗** 参数，则模块按通态电流和断态电压对该损耗值进行线性缩放。要使用接近瞬时值的缩放值，请将 **电压和电流值的滤波时间常数** 设置为小于最快开关周期的值。

作为对反向恢复建模的替代方法，您可以将 **集成保护二极管** 参数设置为 `Diode with charge dynamics`。但是，与使用第一种方法相比，此方法需要更小的仿真时间步长。

**注意**

对于所有理想开关器件，记录的仿真数据将热损耗报告为 `lastTurnOffLoss`、`lastTurnOnLoss` 和 `lastReverseRecoveryLoss`。这些变量将损耗记录为脉冲，其幅值等于能量损耗。如果使用脚本对指定仿真周期内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，您可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录数据中提取导通损耗和开关损耗。

您还可以从记录的仿真数据中的 `accumulatedSwitchingLosses` 变量访问累计的总开关损耗。此变量汇总截至当前的所有开关损耗，包括二极管的反向恢复损耗。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗或反向恢复损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆通态损耗。

如果使用固定步长求解器，支持捕获开关损耗的最短脉冲导通或脉冲关断长度为三个时间步长。如果脉冲短于三个步长，则模块不报告开关损耗。

如果使用表格数据对开关损耗或反向恢复损耗建模，请检查温度、电流和电压是否在您指定的范围内。如果未定义真实的热模型，例如，如果结质量或从结到外壳的电导过小，温度可能会超出您指定的范围，导致模块将损耗外推到非物理值。

### 参数化

*自 R2023b 起*

IGBT (Ideal, Switching) 模块支持多个预定义参数化。

使用此参数化数据表示特定供应商的组件。这些 IGBT 的参数化与制造商数据手册一致。要加载预定义参数化，请双击 IGBT( Ideal, Switching) 模块，单击 **所选部件** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择您要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用数据源获取参数值。工程判断和简化假设用于填补缺失数据。因此，仿真行为与实际物理行为之间可能会出现偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预定义参数化的更多信息以及可用组件列表，请参阅预参数化组件列表。

您还可以使用 `ee_importDeviceParameters` 函数从 XML 文件中提取器件参数并将其导入模块。XML 文件必须位于 MATLAB® 路径上，并且必须使用 Hitachi 或 Infineon® 支持的参数化格式。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

使用标称值指定模型中变量的预期量级。基于标称值使用系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅按标称值进行系统缩放。

### 绘制基本 I-V 特性

*自 R2023b 起*

您无需构建完整模型即可绘制 IGBT (Ideal, Switching) 模块的基本 I-V 特性。使用绘图可探究参数选择对器件特性的影响。如果根据数据手册对模块进行参数化，则可以将绘图与数据手册进行比较，以检查模块参数化是否正确。如果已有完整的工作模型但不知道使用哪个制造部件，则可以将绘图与数据手册进行比较以帮助您做出决定。

要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **电气** > **基本特性**。

**基本特性** 选项会根据您为 IGBT (Ideal, Switching) 模块的 **建模选项**、**通态行为和损耗** 和 **集成保护二极管** 参数指定的值生成不同的绘图。如果对带有集成保护二极管的开关器件建模，则 **基本特性** 选项会绘制开关器件和二极管的 I-V 特性。如果启用模块的热端口，则 **基本特性** 选项还会生成开通能量损耗和关断能量损耗作为通态电流和断态电压函数的曲面图。有关此选项的更多信息，请参阅绘制半导体模块的基本 I-V 特性。
