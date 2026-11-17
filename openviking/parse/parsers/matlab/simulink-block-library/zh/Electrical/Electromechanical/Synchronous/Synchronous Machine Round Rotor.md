---
type: simulink-block
title: 'Synchronous Machine Round Rotor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachineroundrotor'
documentation_source_path: 'ref/synchronousmachineroundrotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine Round Rotor

## 端口

### 输出

### **pu** — 电机标幺值测量 physical

与电机标幺值测量相关联的物理信号向量端口。向量元素为：

- 励磁电压（励磁电路基准值，Efd），
  *pu\_fd\_Efd*
- 励磁电流（励磁电路基准值，Ifd），
  *pu\_fd\_Ifd*
- 电磁转矩，*pu\_torque*
- 转子速度，*pu\_velocity*
- 定子 d 轴电压，*pu\_ed*
- 定子 q 轴电压，*pu\_eq*
- 定子零序电压，
  *pu\_e0*
- 定子 d 轴电流，*pu\_id*
- 定子 q 轴电流，*pu\_iq*
- 定子零序电流，
  *pu\_i0*
- 转子电角度，
  *electrical\_angle\_out*

要连接到此端口，请使用 Synchronous Machine Measurement 模块。
### 守恒

### **fd+** — 励磁绕组正极端子 electrical

与励磁绕组正极端子相关联的电气守恒端口。

### **fd-** — 励磁绕组负极端子 electrical

与励磁绕组负极端子相关联的电气守恒端口。

### **R** — 电机转子 mechanical

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳 mechanical

与电机机壳相关联的机械旋转守恒端口。

### **~** — 定子绕组 electrical

与定子绕组相关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Composite three-phase
ports`。

### **n** — 中性相 electrical

与星形绕组配置的中性点相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Zero sequence** 设置为
`Include`。

### **a** — *a* 相 electrical

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **b** — *b* 相 electrical

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **c** — *c* 相 electrical

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **HA** — *a* 相端子热端口 thermal

与定子绕组 *a* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HB** — *b* 相端子热端口 thermal

与定子绕组 *b* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HC** — *c* 相端子热端口 thermal

与定子绕组 *c* 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HR** — 转子热端口 thermal

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

## 参数

### **Modeling option** — 启用热端口的选项 `No thermal port`（默认）| `Show thermal port`

启用模块热端口并对产生的热量和电机温度效应进行建模的选项。

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是扩展三相端口。

### **Rated apparent power** — 额定视在功率 `555e6` `V*A`（默认）

额定视在功率。

### **Rated voltage** — RMS 额定线电压 `24e3` `V`（默认）

RMS 额定线电压。

### **Rated electrical frequency** — 标称电气频率 `60` `Hz`（默认）

额定视在功率对应的标称电气频率。

### **Number of pole pairs** — 极对数 `1`（默认）

电机极对数。

### **Specify parameterization by** — 模块参数化 `Fundamental parameters`（默认）| `Standard parameters`

模块参数化方法。选项为：

- `Fundamental parameters` —
  使用基本参数指定阻抗。
- `Standard parameters` —
  使用基本参数指定阻抗，并指定 d 轴和 q 轴时间常数。

此参数影响 **Time
Constant** 设置和 **Impedances** 设置中参数的可见性。

### **Specify field circuit input required to produce rated terminal voltage at no load by** — 指定空载时产生额定端子电压所需的励磁电路输入 `Field circuit current`（默认）| `Field circuit voltage`

励磁电路参数化方法。选项为：

- `Field circuit voltage` —
  以电压形式指定励磁电路。
- `Field circuit current` —
  以电流形式指定励磁电路。

此参数影响 **Field circuit
voltage** 和 **Field circuit current** 参数的可见性。

### **Field circuit voltage** — 励磁电路电压 `95.95` `V`（默认）

在电机端子处产生额定电压的励磁电路两端电压。

#### 依赖关系

仅当 **Specify field
circuit input required to produce rated terminal voltage at no
load by** 参数设置为 `Field
circuit voltage` 时，此参数才可见。

### **Field circuit current** — 励磁电路电流 `1300` `A`（默认）

在电机端子处产生额定电压的励磁电路电流。

#### 依赖关系

仅当 **Specify field
circuit input required to produce rated terminal voltage at no
load by** 参数设置为 `Field
circuit current` 时，此参数才可见。

### **Zero sequence** — 零序模型 `Include`（默认）| `Exclude`

零序模型：

- `Include` — 优先考虑模型保真度。
  此模型是默认的零序模型。如果为使用 Partitioning 求解器的仿真包含零序项，则会发生错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

#### 依赖关系

如果此参数设置为：

- `Include` 且 **Specify
  parameterization by** 设置为 **Fundamental
  parameters** — **Impedances** 设置中的 **Stator zero-sequence
  inductance, L0** 参数可见。
- `Include` 且 **Specify
  parameterization by** 设置为 **Standard
  parameters** — **Impedances** 设置中的 **zero-sequence
  reactance, X0** 参数可见。
- `Exclude` — **Impedances** 设置中的零序参数不可见。

### **Rotor angle definition** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。

当您选择默认值时，转子 *d* 轴和定子 *a* 相磁轴在转子角度为零时对齐。

此参数的另一个可选值为 `Angle between the a-phase magnetic axis and the q-axis`。当您选择此值时，转子 *q* 轴和定子 *a* 相磁轴在转子角度为零时对齐。

### 阻抗

### **Stator d-axis mutual inductance (unsaturated), Ladu** — 定子 d 轴互感（未饱和）`1.66`（默认）| 正标量

未饱和定子 *d* 轴互感。如果 **Magnetic saturation representation** 设置为 `None`，则此参数等同于定子 d 轴互感。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Stator q-axis mutual inductance (unsaturated), Laqu** — 定子 q 轴互感（未饱和）`1.61`（默认）| 正标量

未饱和定子 *q* 轴互感。如果 **Magnetic saturation representation** 设置为 `None`，则此参数等同于定子 q 轴互感。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.15`（默认）| 正标量

定子零序电感。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 且 **Zero Sequence** 参数设置为 `Include` 时，此参数才可见。

### **Stator leakage inductance, Ll** — 定子漏电感 `0.15`（默认）| 正标量

定子漏电感。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Stator resistance, Ra** — 定子电阻 `0.003`（默认）| 正标量

定子电阻。此参数必须大于 `0`。

### **Rotor field circuit inductance, Lfd** — 转子励磁电路电感 `0.165`（默认）| 正标量

转子励磁电路电感。此参数必须大于 `0`。

### **Rotor field circuit resistance, Rfd** — 转子励磁电路电阻 `0.0006`（默认）| 正标量

转子励磁电路电阻。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Rotor d-axis damper winding 1 inductance, L1d** — 转子 d 轴阻尼绕组 1 电感 `0.1713`（默认）| 正标量

转子 *d* 轴阻尼绕组 1 电感。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Rotor d-axis damper winding 1 resistance, R1d** — 转子 d 轴阻尼绕组 1 电阻 `0.0284`（默认）| 正标量

转子 *d* 轴阻尼绕组 1 电阻。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Rotor q-axis damper winding 1 inductance, L1q** — 转子 q 轴阻尼绕组 1 电感 `0.7252`（默认）| 正标量

转子 *q* 轴阻尼绕组 1 电感。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Rotor q-axis damper winding 1 resistance, R1q** — 转子 q 轴阻尼绕组 1 电阻 `0.00619`（默认）| 正标量

转子 *q* 轴阻尼绕组 1 电阻。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Rotor q-axis damper winding 2 inductance, L2q** — 转子 q 轴阻尼绕组 2 电感 `0.125`（默认）| 正标量

转子 *q* 轴阻尼绕组 2 电感。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Rotor q-axis damper winding 2 resistance, R2q** — 转子 q 轴阻尼绕组 2 电阻 `0.02368`（默认）| 正标量

转子 *q* 轴阻尼绕组 2 电阻。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **Stator leakage reactance, Xl** — 定子漏电抗 `0.15`（默认）| 正标量

定子漏电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 时，此参数才可见。

### **d-axis synchronous reactance, Xd** — d 轴同步电抗 `1.81`（默认）| 正标量

*d* 轴同步电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 时，此参数才可见。

### **q-axis synchronous reactance, Xq** — q 轴同步电抗 `1.76`（默认）| 正标量

*q* 轴同步电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 时，此参数才可见。

### **zero-sequence reactance, X0** — 零序电抗 `0.15`（默认）| 正标量

零序电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 且 **Zero Sequence** 参数设置为 `Include` 时，此参数才可见。

### **d-axis transient reactance, Xd'** — d 轴瞬态电抗 `0.3`（默认）| 正标量

*d* 轴瞬态电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 时，此参数才可见。

### **q-axis transient reactance, Xq'** — q 轴瞬态电抗 `0`（默认）| 正标量

*q* 轴瞬态电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 时，此参数才可见。

### **d-axis subtransient reactance, Xd''** — d 轴次瞬态电抗 `0.23`（默认）| 正标量

*d* 轴次瞬态电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 时，此参数才可见。

### **q-axis subtransient reactance, Xq''** — q 轴次瞬态电抗 `0.25`（默认）| 正标量

*q* 轴次瞬态电抗。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为 `Standard parameters` 时，此参数才可见。

### 时间常数

### **Specify d-axis time constant** — 指定 d 轴时间常数 `Open circuit`（默认）| `Short circuit`

在 `Open circuit` 和 `Short circuit` 之间选择。

此参数的设置影响 *d* 轴时间常数参数的可见性。

### **d-axis transient open-circuit, Td0'** — d 轴瞬态开路 `8` `s`（默认）| 正标量

*d* 轴瞬态开路时间常数。此参数必须：

- 大于 0。
- 大于 **d-axis subtransient open-circuit,
  Td0''**。

#### 依赖关系

仅当 **Specify d-axis
transient time constant** 参数设置为 `Open circuit` 时，此参数才可见。

### **d-axis transient short-circuit, Td'** — d 轴瞬态短路 `1.3260` `s`（默认）| 正标量

*d* 轴瞬态短路时间常数。此参数必须：

- 大于 0。
- 大于 **d-axis subtransient short-circuit,
  Td''**。

#### 依赖关系

仅当 **Specify d-axis
transient time constant** 参数设置为 `Short circuit` 时，此参数才可见。

### **d-axis subtransient open-circuit, Td0''** — d 轴次瞬态开路 `0.03` `s`（默认）| 正标量

*d* 轴次瞬态开路时间常数。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify d-axis
transient time constant** 参数设置为 `Open circuit` 时，此参数才可见。

### **d-axis subtransient short-circuit, Td''** — d 轴次瞬态短路 `0.0230` `s`（默认）| 正标量

*d* 轴次瞬态短路时间常数。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify d-axis transient time constant** 参数设置为 `Short circuit` 时，此参数才可见。

### **Specify q-axis time constant** — 指定 q 轴时间常数 `Open circuit`（默认）| `Short circuit`

在 `Open circuit` 和 `Short circuit` 之间选择。

此参数的设置会影响 *q* 轴时间常数参数的可见性。

### **q-axis transient open-circuit, Tq0'** — q 轴瞬态开路 `1` `s`（默认）| 正标量

*q* 轴瞬态开路时间常数。此参数必须：

- 大于 0。
- 大于 **q-axis subtransient open-circuit, Tq0''**。

#### 依赖关系

仅当 **Specify q-axis transient time constant** 参数设置为 `Open circuit` 时，此参数才可见。

### **q-axis transient short-circuit, Tq'** — q 轴瞬态短路 `0.3693` `s`（默认）| 正标量

*q* 轴瞬态短路时间常数。此参数必须：

- 大于 0。
- 大于 **q-axis subtransient short-circuit, Tq''**。

#### 依赖关系

仅当 **Specify q-axis transient time constant** 参数设置为 `Short circuit` 时，此参数才可见。

### **q-axis subtransient open-circuit, Tq0''** — q 轴次瞬态开路 `0.07` `s`（默认）| 正标量

*q* 轴次瞬态开路时间常数。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify q-axis transient time constant** 参数设置为 `Open circuit` 时，此参数才可见。

### **q-axis subtransient short-circuit, Tq''** — q 轴次瞬态短路 `0.0269` `s`（默认）| 正标量

*q* 轴次瞬态短路时间常数。此参数必须大于 `0`。

#### 依赖关系

仅当 **Specify q-axis transient time constant** 参数设置为 `Short circuit` 时，此参数才可见。

### 饱和

### **Magnetic saturation representation** — 磁饱和表示 `None`（默认）| `Open-circuit lookup table (v versus i)`

模块磁饱和模型：

- `None`
- `Open-circuit lookup table (v versus i)`

#### 依赖关系

如果将此参数设置为 `Open-circuit lookup table (v versus i)`，则相关参数可见。

### **Per-unit field current saturation data, ifd** — 标幺励磁电流饱和数据 `[0, .48, .76, 1.38, 1.79]`（默认）

填充气隙电压 *Vag* 对励磁电流 *ifd* 查找表的励磁电流 *ifd* 数据。此参数必须包含至少五个元素的向量。

#### 依赖关系

仅当 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table (v versus i)` 时，此参数才可见。

### **Per-unit air-gap voltage saturation data, Vag** — 标幺气隙电压饱和数据 `[0, .8, 1.08, 1.31, 1.4]`（默认）

填充气隙电压 *Vag* 对励磁电流 *ifd* 查找表的气隙电压 *Vag* 数据。此参数必须包含至少五个元素的向量。

#### 依赖关系

仅当 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table (v versus i)` 时，此参数才可见。

### 初始条件

### **Initialization option** — 用于指定仿真开始时的值的选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认）| `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

用于在仿真开始时为某些参数和变量指定值的选项。将此参数设置为：

- `Set real power, reactive power, terminal voltage and terminal phase` — 设置运行点，无论所连接的网络如何。
- `Set targets for rotor angle and Park's transform variables` — 在仿真前使用 **Variables** 设置指定模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。
- `Set targets for load flow variables` — 在 **Initial Conditions** 设置中选择母线类型并指定潮流分析的相关参数。

### **Source type** — 电压源模型 `Swing bus`（默认）| `PV bus` | `PQ bus`

模块建模的电压源类型。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`。

### **Terminal voltage magnitude** — 端电压幅值 `24e3` `V`（默认）| 正标量

端电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `Swing bus` 或 `PV bus`。

### **Terminal voltage angle** — 端电压角度 `0` `deg`（默认）| 标量

端电压角度。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `Swing bus`。

### **Active power generated** — 生成的有功功率 `500e6` `V*A`（默认）| 标量

电机生成的有功功率。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PV bus` 或 `PQ bus`。

### **Reactive power generated** — 生成的无功功率 `0` `V*A`（默认）| 标量

电机生成的无功功率。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PQ bus`。

### **Minimum terminal voltage magnitude (pu)** — 最小端电压幅值 `0.95`（默认）| 正标量

标幺最小稳态电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PQ bus`。

### **Phase search range at terminals** — 端子处的相位搜索范围 `[-inf, inf]` `deg`（默认）| 两个元素的向量

定义端子处相位角搜索范围的向量。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PV bus` 或 `PQ bus`。

### **Parasitic conductance to electrical reference** — 到电气参考的寄生电导 `1e-6` `S`（默认）| 正标量

到电气参考的寄生电导。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认）| 实标量

电机参数的标称温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

如 Thermal Model for Actuator Blocks 中所述，所有三个绕组的电阻与温度关系方程中的系数 α。默认值 `3.93e-3` 1/K 适用于铜。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是使温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是使转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。此外，`Composite three-phase ports` 和 `Expanded three-phase ports` 的 simlog 格式相同。

由于这些更改，在早期版本保存的模型中，请检查此模块的 **Electrical connection** 参数。

## 描述

具有基本或标准参数化的圆转子同步电机

Synchronous Machine Round Rotor 模块使用基本或标准参数对圆转子同步电机进行建模。

### 使用潮流目标值进行同步电机初始化

如果模块所在的网络与频率-时间仿真模式兼容，则可以对网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。有关展示如何使用潮流分析数据初始化同步电机的示例，请参阅 Synchronous Machine Initialization with Loadflow。

### 方程

同步电机方程相对于旋转参考坐标系表示，定义为

θe(t)=Nθr(t),

其中：

- *θe* 是电角度。
- *N* 是极对数。
- *θr* 是转子角度。

Park 变换将同步电机方程映射到相对于电角度的旋转参考坐标系。Park 变换定义为

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212].

Park 变换用于定义标幺同步电机方程。定子电压方程定义为

ed=1ωbasedψddt−Ψqωr−Raid,

eq=1ωbasedψqdt+Ψdωr−Raiq,

以及

e0=1ωbasedΨ0dt−Rai0,

其中：

- *ed*、*eq* 和 *e0* 是 *d* 轴、*q* 轴和零序定子电压，定义为

  [edeqe0]=Ps[vavbvc].

  *va*、*vb* 和 *vc* 是从端口 **~** 到中性端口 **n** 测量的定子电压。
- *ωbase* 是标幺基准电速度。
- *ψd*、*ψq* 和 *ψ0* 是 *d* 轴、*q* 轴和零序定子磁链。
- *ωr* 是标幺转子转速。
- *Ra* 是定子电阻。
- *id*、*iq* 和 *i0* 是 *d* 轴、*q* 轴和零序定子电流，定义为

  [idiqi0]=Ps[iaibic].

  *ia*、*ib* 和 *ic* 是从端口 **~** 流向端口 **n** 的定子电流。

转子电压方程定义为

efd=1ωbasedΨfddt+Rfdifd,

e1d=1ωbasedΨ1ddt+R1di1d=0,

e1q=1ωbasedΨ1qdt+R1qi1q=0,

以及

e2q=1ωbasedΨ2qdt+R2qi2q=0,

其中：

- *efd* 是励磁电压。
- *e1d*、*e1q* 和 *e2q* 是 *d* 轴阻尼绕组 1、*q* 轴阻尼绕组 1 和 *q* 轴阻尼绕组 2 两端的电压。它们都等于 0。
- *ψfd*、*ψ1d*、*ψ1q* 和 *ψ2q* 是链接励磁电路、*d* 轴阻尼绕组 1、*q* 轴阻尼绕组 1 和 *q* 轴阻尼绕组 2 的磁通量。
- *Rfd*、*R1d*、*R1q* 和 *R2q* 是转子励磁电路、*d* 轴阻尼绕组 1、*q* 轴阻尼绕组 1 和 *q* 轴阻尼绕组 2 的电阻。
- *ifd*、*i1d*、*i1q* 和 *i2q* 是在励磁电路、*d* 轴阻尼绕组 1、*q* 轴阻尼绕组 1 和 *q* 轴阻尼绕组 2 中流动的电流。

饱和方程定义为

ψad=ψd+Llid,

ψaq=ψq+Lliq,

ψat=ψad2+ψaq2,

Ks=1（如果饱和被禁用），

Ks=f(ψat)（如果饱和被启用），

Lad=Ks\*Ladu,

以及

Laq=Ks\*Laqu,

其中：

- *ψad* 是 *d* 轴气隙或互感磁链。
- *ψaq* 是 *q* 轴气隙或互感磁链。
- *ψat* 是气隙磁链。
- *Ks* 是饱和因子。
- *Ladu* 是定子 *d* 轴的未饱和互感。
- *Lad* 是定子 *d* 轴的互感。
- *Laqu* 是定子 *q* 轴的未饱和互感。
- *Laq* 是定子 *q* 轴的互感。

饱和因子函数 *f* 由标幺开路查找表计算为：

Lad=dψatdifd,

Vag=g(ifd),

以及

Lad=dg(ifd)difd=dVagdifd,

其中 *Vag* 是标幺气隙电压。

在标幺中，

Ks=LadLadu,

以及

ψat=Vag

可以重新排列为

Ks=f(ψat).

定子磁链方程定义为

Ψd=−(Lad+Ll)id​+Ladifd+Ladi1d,

Ψq=−(Laq+Ll)iq​+Laqi1q+Laqi2q,

以及

Ψ0=−L0i0,

其中：

- *Ll* 是定子漏电感。
- *Lad* 和 *Laq* 是定子 *d* 轴和 *q* 轴的互感。

转子磁链方程定义为

ψfd=Lffdifd+Lf1di1d−Ladid,

ψ1d=Lf1difd+L11di1d−Ladid,

ψ1q=L11qi1q+Laqi2q−Laqiq,

以及

ψ2q=Laqi1q+L22qi2q−Laqiq,

其中：

- *Lffd* 是转子励磁电路的自感。
- *Lffd* 是转子励磁电路的自感。
- *L11d* 是 *d* 轴阻尼绕组 1 的自感。
- *L11q* 是 *q* 轴阻尼绕组 1 的自感。
- *L22q* 是 *q* 轴阻尼绕组 2 的自感。
- *Lf1d* 是转子励磁电路和 *d* 轴阻尼绕组 1 的互感。

电感由以下方程定义：

Lffd=Lad+Lfd

Lf1d=Lffd−Lfd

L11d=Lf1d+L1d

L11q=Laq+L1q

L22q=Laq+L2q

电感方程假设标幺互感 *L12q* = *Laq*，即 *q* 轴中的定子和转子电流都链接由 *Laq* 表示的单一互感磁通。

转子转矩定义为

Te=Ψdiq−Ψqid.

### 绘图和显示选项

您可以使用模块上下文菜单中的 **Electrical** 菜单执行绘图和显示操作。

右键单击模块，然后从 **Electrical** 菜单中选择一个选项：

- **Display Base Values** — 在 MATLAB® 命令窗口中显示电机标幺基准值。
- **Display Associated Base Values** — 在 MATLAB 命令窗口中显示关联的标幺基准值。
- **Display Associated Initial Conditions** — 在 MATLAB 命令窗口中显示关联的初始条件。
- **Plot Open-Circuit Saturation (pu)** — 在 MATLAB 图窗中绘制气隙电压 *Vag* 与励磁电流 *ifd* 的关系，两者均以标幺值测量。该图包含三条曲线：

  - Unsaturated — 您指定的 **Stator d-axis mutual inductance (unsaturated), Ladu**
  - Saturated — 您指定的 **Per-unit open-circuit lookup table (Vag versus ifd)**
  - Derived — 根据您指定的 **Per-unit open-circuit lookup table (Vag versus ifd)** 推导出的开路查找表（标幺值）。此数据用于计算饱和系数 *Ks* 与磁链 *ψat* 的关系特性。
- **Plot Saturation Factor (pu)** — 使用电机参数在 MATLAB 图窗中绘制饱和系数 *Ks* 与磁链 *ψat* 的关系，两者均以标幺值测量。此参数由您指定的其他参数推导得出：

  - **Stator d-axis mutual inductance (unsaturated), Ladu**
  - **Per-unit field current saturation data, ifd**
  - **Per-unit air-gap voltage saturation data, Vag**
- **Plot Power Capability Curves** — 在 MATLAB 图窗中绘制有功功率 P 与无功功率 Q 的关系，两者均以标幺值测量。该图可能包含多条曲线。每条曲线对应一个以标幺值测量的最大励磁电路电压（非互易标幺系统）。该图显示了发电机在滞后功率因数下运行时的最大无功功率，以及发电机在超前功率因数下运行时的最小无功功率。*（自 R2023b 起）*

### 建模热效应

您可以暴露热端口来建模产生的热量和电机温度的影响。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

对于此模块，仅当您在 **Initial Conditions** 部分中将 **Initialization option** 参数设置为 `Set targets for rotor angle and Park's transform variables` 时，**Initial Targets** 设置才可见。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
