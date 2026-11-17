---
type: simulink-block
title: 'Synchronous Machine Model 2.1'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinemodel21'
documentation_source_path: 'ref/synchronousmachinemodel21.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine Model 2.1

## 端口

### 输出

### **pu** — 电机标幺值测量 physical

与电机标幺值测量相关联的物理信号矢量端口。矢量元素为：

- 励磁电压（励磁回路基准值，Efd），
  *pu\_fd\_Efd*
- 励磁电流（励磁回路基准值，Ifd），
  *pu\_fd\_Ifd*
- 电磁转矩，*pu\_torque*
- 转子速度，*pu\_velocity*
- 定子 d 轴电压，*pu\_ed*
- 定子 q 轴电压，*pu\_eq*
- 定子零序电压，*pu\_e0*
  — 提供此端口是为了保持与其他电机模型的兼容
  接口。其值始终为
  零。
- 定子 d 轴电流，*pu\_id*
- 定子 q 轴电流，*pu\_iq*
- 定子零序电流，*pu\_i0*
  — 提供此端口是为了保持与其他电机模型的兼容
  接口。其值始终为
  零。
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

与定子绕组相关联的可扩展三相
端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Composite three-phase
ports`。

### **n** — 中性相 electrical

与星形绕组配置的中性点相关联的电气守恒端口。提供此端口是为了保持
与现有电机模型的兼容接口。此端口上的电压和
电流被忽略。

### **a** — *a* 相 electrical

与 *a* 相相关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **b** — *b* 相 electrical

与 *b* 相相关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **c** — *c* 相 electrical

与 *c* 相相关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **HA** — *a* 相端子热端口 thermal

与定子绕组 *a* 相关联的
热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HB** — *b* 相端子热端口 thermal

与定子绕组 *b* 相关联的
热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HC** — *c* 相端子热端口 thermal

与定子绕组 *c* 相关联的
热守恒端口。

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

启用模块热端口并模拟生成热量和电机温度效应的
选项。

### 主要

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

使用复合三相端口还是扩展三相端口。

### **Rated apparent power** — 额定视在功率 `555e6` `V*A`（默认）

额定视在功率。

### **Rated voltage** — RMS 额定线电压 `24e3` `V`（默认）

RMS 额定线电压。

### **Rated electrical frequency** — 标称电气频率 `60` `Hz`（默认）

额定视在功率所对应的标称电气频率。

### **Number of pole pairs** — 极对数 `1`（默认）

电机极对数。

### **Specify parameterization by** — 模块参数化方法 `Fundamental parameters`（默认）| `Standard parameters`

模块参数化方法。选项包括：

- `Fundamental parameters` —
  基本参数在 **Impedances** 设置中可见，
  **Time Constants** 设置不可见。
- `Standard parameters` —
  标准参数在 **Impedances** 中可见，
  **Time Constants** 设置可见。

此参数影响 **Time
Constant** 设置和 **Impedances** 设置中参数的
可见性。

### **Specify field circuit input required to produce rated terminal voltage at no load by** — 指定空载时产生额定端子电压所需的励磁回路输入 `Field circuit current`（默认）| `Field circuit voltage`

励磁回路参数化方法。选项包括：

- `Field circuit voltage` —
  以电压形式指定励磁回路。
- `Field circuit current` —
  以电流形式指定励磁回路。此方法是默认的励磁回路参数化
  方法。

此参数影响 **Field circuit
voltage** 和 **Field circuit current**
参数的可见性。

### **Field circuit voltage** — 励磁回路电压 `92.95` `V`（默认）

在电机端子处产生额定电压的励磁回路
电压。

#### 依赖关系

仅当 **Specify field
circuit input required to produce rated terminal voltage at no
load by** 参数设置为 `Field
circuit voltage` 时，此参数才可见。

### **Field circuit current** — 励磁回路电流 `1300` `A`（默认）

在电机端子处产生额定电压的励磁回路
电流。

#### 依赖关系

仅当 **Specify field
circuit input required to produce rated terminal voltage at no
load by** 参数设置为 `Field
circuit current` 时，此参数才可见。

### **Rotor angle definition** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。

当您选择默认值时，转子 *d* 轴和定子 *a* 相磁轴在转子角度为零时对齐。

此参数可选的另一个值为 `Angle between the a-phase magnetic axis and the q-axis`。当您选择此值时，转子 *q* 轴和定子 *a* 相磁轴在转子角度为零时对齐。

### 阻抗

### **Stator d-axis mutual inductance (unsaturated), Ladu** — 定子 d 轴互感（未饱和）`1.66`（默认）| 正标量

未饱和定子 *d* 轴互感。此
参数必须大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Stator q-axis mutual inductance (unsaturated), Laqu** — 定子 q 轴互感（未饱和）`1.61`（默认）| 正标量

未饱和定子 *q* 轴互感。此
参数必须大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Stator leakage inductance, Ll** — 定子漏电感 `0.15`（默认）| 正标量

定子漏电感。此参数必须大于
0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Stator resistance, Ra** — 定子电阻 `0.003`（默认）| 正标量

定子电阻。此参数必须大于 0。

### **Rotor field circuit inductance, Lfd** — 转子励磁回路电感 `0.165`（默认）| 正标量

转子励磁回路电感。此参数必须大于
0。

### **Rotor field circuit resistance, Rfd** — 转子励磁回路电阻 `0.0006`（默认）| 正标量

转子励磁回路电阻。此参数必须大于
0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Rotor d-axis damper winding 1 inductance, L1d** — 转子 d 轴阻尼绕组 1 电感 `0.1713`（默认）| 正标量

转子 *d* 轴阻尼绕组 1 电感。此
参数必须大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Rotor d-axis damper winding 1 resistance, R1d** — 转子 d 轴阻尼绕组 1 电阻 `0.0284`（默认）| 正标量

转子 *d* 轴阻尼绕组 1 电阻。此
参数必须大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Rotor q-axis damper winding 1 inductance, L1q** — 转子 q 轴阻尼绕组 1 电感 `0.1066`（默认）| 正标量

转子 *q* 轴阻尼绕组 1 电感。此
参数必须大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Rotor q-axis damper winding 1 resistance, R1q** — 转子 q 轴阻尼绕组 1 电阻 `0.0650`（默认）| 正标量

转子 *q* 轴阻尼绕组 1 电阻。此
参数必须大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Fundamental parameters` 时，此参数才可见。

### **Stator leakage reactance, Xl** — 定子漏电抗 `0.15`（默认）| 正标量

定子漏电抗。此参数必须大于
0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Standard parameters` 时，此参数才可见。

### **d-axis synchronous reactance, Xd** — d 轴同步电抗 `1.81`（默认）| 正标量

*d* 轴同步电抗。此参数必须
大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Standard parameters` 时，此参数才可见。

### **q-axis synchronous reactance, Xq** — q 轴同步电抗 `1.76`（默认）| 正标量

*q* 轴同步电抗。此参数必须
大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Standard parameters` 时，此参数才可见。

### **d-axis transient reactance, Xd'** — d 轴瞬态电抗 `0.3`（默认）| 正标量

*d* 轴瞬态电抗。此参数必须
大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Standard parameters` 时，此参数才可见。

### **d-axis subtransient reactance, Xd''** — d 轴次瞬态电抗 `0.23`（默认）| 正标量

*d* 轴次瞬态电抗。此参数必须
大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Standard parameters` 时，此参数才可见。

### **q-axis subtransient reactance, Xq''** — q 轴次瞬态电抗 `0.25`（默认）| 正标量

*q* 轴次瞬态电抗。此参数必须
大于 0。

#### 依赖关系

仅当 **Specify
parameterization by** 参数设置为
`Standard parameters` 时，此参数才可见。

### 时间常数

### **Specify d-axis time constant** — 指定 d 轴时间常数 `Open circuit`（默认）| `Short circuit`

在 `Open circuit` 和
`Short circuit` 之间选择。

此参数的设置影响
*d* 轴时间常数参数的可见性。

### **d-axis transient open-circuit, Td0'** — d 轴瞬态开路 `8` `s`（默认）| 正标量

*d* 轴瞬态开路时间常数。此
参数必须：

- 大于 0。
- 大于 **d-axis subtransient open-circuit,
  Td0''**。

#### 依赖关系

仅当 **Specify d-axis
transient time constant** 参数设置为
`Open circuit` 时，此参数才可见。

### **d-axis transient short-circuit, Td'** — d 轴瞬态短路 `1.3260` `s`（默认）| 正标量

*d* 轴瞬态短路时间常数。此
参数必须：

- 大于 0。
- 大于 **d-axis subtransient short-circuit,
  Td''**。

#### 依赖关系

仅当 **Specify d-axis
transient time constant** 参数设置为
`Short circuit` 时，此参数才可见。

### **d-axis subtransient open-circuit, Td0''** — d 轴次瞬态开路 `0.03` `s`（默认）| 正标量

*d* 轴次瞬态开路时间常数。
此参数必须大于 0。

#### 依赖关系

仅当 **Specify d-axis
transient time constant** 参数设置为
`Open circuit` 时，此参数才可见。

### **d-axis subtransient short-circuit, Td''** — d 轴次瞬态短路 `0.0230` `s`（默认）| 正标量

*d* 轴次瞬态短路时间常数。
此参数必须大于 0。

#### 依赖关系

仅当 **Specify d-axis
transient time constant** 参数设置为
`Short circuit` 时，此参数才可见。

### **Specify q-axis time constant** — 指定 q 轴时间常数 `Open circuit`（默认）| `Short circuit`

在 `Open circuit` 和
`Short circuit` 之间选择。

此参数的设置影响
*q* 轴时间常数参数的可见性。

### **q-axis subtransient open-circuit, Tq0''** — q 轴次瞬态开路 `0.07` `s`（默认）| 正标量

*q* 轴次瞬态开路时间常数。
此参数必须大于 0。

#### 依赖关系

仅当 **Specify q-axis
transient time constant** 参数设置为
`Open circuit` 时，此参数才可见。

### **q-axis subtransient short-circuit, Tq''** — q 轴次瞬态短路 `0.0269` `s`（默认）| 正标量

*q* 轴次瞬态短路时间常数。
此参数必须大于 0。

#### 依赖关系

仅当 **Specify q-axis
transient time constant** 参数设置为
`Short circuit` 时，此参数才可见。

### 初始条件

### **Initialization option** — 初始化选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认）| `设置转子角和 Park 的目标 transform variables` | `Set targets for load flow variables`

用于在仿真开始时指定某些参数和变量值的
模型。要：

设置与所连接网络无关的工作点，
选择 `Set real power, reactive power, terminal
voltage and terminal phase`。

- 在仿真前使用
  **Variables** 设置指定模块变量的优先级和初始目标值，
  选择
  `设置转子角和 Park 的目标
  transform variables`。有关更多信息，
  请参阅 Set Priority and Initial Target for Block Variables。
- 选择母线类型并在 **Initial
  Conditions** 设置中指定潮流分析的相关参数，
  选择 `Set
  targets for load flow variables`。

#### 依赖关系

如果将此参数设置为：

- `设置转子角和 Park 的目标
  transform variables` — **Variables** 设置变为
  可见。
- `Set real power, reactive power, terminal
  voltage, and terminal phase` — 相关
  参数变为可见。
- `Set targets for load flow
  variables` — 相关参数变为
  可见。

### **Source type** — 电压源模型 `Swing bus`（默认）| `Voltage source with series impedance` | `PV bus` | `PQ bus`

模块所建模的电压源类型。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set targets for load flow variables` 且 **Source type** 参数设置为 `Swing bus` 或 `PV bus` 时，此参数才可见。

**Terminal voltage magnitude**、**Terminal voltage angle**、**Active power generated**、**Reactive power generated**、**Minimum terminal voltage magnitude (pu**、**Phase search range at terminals** 和 **Phase search range at terminals** 的可见性取决于为此参数选择的值。

### **Terminal voltage magnitude** — 端子电压幅值 `24e3` `V`（默认）

端子电压幅值。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **Initialization option** 参数设置为 `Set targets for load flow variables` 且 **Source type** 参数设置为 `Swing bus` 或 `PV bus` 时，此参数才可见。

### **Terminal voltage angle** — 端子电压相角 `0` `deg`（默认）

端子电压相角。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **Initialization option** 参数设置为 `Set targets for load flow variables` 且 **Source type** 参数设置为 `Swing bus` 时，此参数才可见。

### **Active power generated** — 生成的有功功率 `500e6` `V*A`（默认）

生成的有功功率。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **Initialization option** 参数设置为 `Set targets for load flow variables` 且 **Source type** 参数设置为 `PV bus` 或 `PQ bus` 时，此参数才可见。

### **Reactive power generated** — 生成的无功功率 `0` `V*A`（默认）

生成的无功功率。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **Initialization option** 参数设置为 `Set targets for load flow variables` 且 **Source type** 参数设置为 `PQ bus` 时，此参数才可见。

### **Minimum terminal voltage magnitude (pu)** — 最小端子电压幅值 `0.95`（默认）

标幺值最小稳态电压幅值。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set targets for load flow variables` 且 **Source type** 参数设置为 `PQ bus` 时，此参数才可见。

### **Phase search range at terminals** — 端子处的相角搜索范围 `[-inf, inf]` `deg`（默认）

定义相角搜索范围的向量。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set targets for load flow variables` 且 **Source type** 参数设置为 `PV bus` 或 `PQ bus` 时，此参数才可见。

### **Parasitic conductance to electrical reference** — 到电气参考的寄生电导 `1e-6` `S`（默认）

到电气参考的寄生电导。

#### 依赖关系

仅当 **Initialization option** 参数设置为 `Set targets for load flow variables` 时，此参数才可见。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认）| 实数标量

电机参数的标称温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和展开端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。此外，`Composite three-phase ports` 和 `Expanded three-phase ports` 的 simlog 格式相同。

由于这些更改，在早期版本保存的模型中，请检查此模块的 **Electrical connection** 参数。

## 描述

具有简化变换、简化表示以及基本或标准参数化的同步电机

Synchronous Machine Model 2.1 模块对同步电机进行建模，其在 *d* 轴上有一个励磁绕组和一个阻尼器，在 *q* 轴上有一个阻尼器。您可以使用基本参数或标准参数来定义电机的特性。此模块包含 *d**q* Park 变换，因此仅用于平衡运行。

### 使用潮流目标值的同步电机初始化

如果模块所在的网络与频率-时间仿真模式兼容，您可以对网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。有关展示如何使用潮流分析数据初始化同步电机的示例，请参阅 Synchronous Machine Initialization with Loadflow。

### 方程

同步电机方程是相对于旋转参考坐标系表示的，定义为

θe(t)=Nθr(t),

其中：

- *θe* 是电角度。
- *N* 是极对数。
- *θr* 是转子角度。

Park 变换将同步电机方程映射到相对于电角度的旋转参考坐标系。Park 变换定义为

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)].

Park 变换用于定义标幺值同步电机方程。定子电压方程定义为

ed=ed"−Raid+xq"iq

和

eq=eq"−xd"id−Raiq,

其中：

- *e”d* 和 *e”q* 是次暂态电抗后的 *d* 轴和 *q* 轴电压。
- *Ra* 是定子电阻。
- *id* 和 *iq* 是 *d* 轴和 *q* 轴定子电流，定义为

  [idiq]=Ps[iaibic].

  *ia*、*ib* 和 *ic* 是从端口 ~ 流向端口 n 的定子电流。
- *x”d* 和 *x”q* 是 *d* 轴和 *q* 轴次暂态电抗。

- *ed* 和 *eq* 是 *d* 轴和 *q* 轴定子电压，定义为

  [edeq]=Ps[vavbvc].

  *va*、*vb* 和 *vc* 是从端口 ~ 到中性端口 n 测量的定子电压。

转子电压方程定义为

efd=Rfd⋅ifd,

其中：

- *Rfd* 是转子励磁电路电阻。
- *ifd* 是使用同步电机模型互易标幺值系统的标幺值励磁电流。
- *efd* 是使用同步电机模型互易标幺值系统的标幺值励磁电压。

暂态电抗后电压方程定义为

ded"dt=(xq−xq")iq−ed"Tq0",

deq'dt=Efd−(xd−xd')id−eq'Td0',

和

deq"dt=eq'−(xd'−xd")id−eq"Td0,

其中：

- *xd* 和 *xq* 是 *d* 轴和 *q* 轴同步电抗。
- *T”d0* 和 *T”q0* 是 *d* 轴和 *q* 轴次暂态开路时间常数。
- *Efd* 是使用励磁机模型非互易标幺值系统的标幺值励磁电压。
- *x’d* 是 *d* 轴暂态电抗。
- *e’q* 是暂态电抗后的 *q* 轴电压。
- *T’d0* 是 *d* 轴暂态开路时间常数。

转子转矩定义为

Te=ed"id+eq"iq−(xd"−xq")idiq.

这些定义方程并未描述您可以在对话框中设置的参数。要了解它们与方程系数的关系，请参阅 P. Kundur 关于理解、建模、分析和缓解电力系统稳定与控制问题的著作 [1]。

### 显示选项

您可以使用模块上下文菜单上的 **Electrical** 菜单执行显示操作。

右键单击模块，然后从 **Electrical** 菜单中选择一个选项：

- **Display Base Values** 在 MATLAB® 命令窗口中显示电机标幺值基准值。
- **Display Associated Base Values** 在 MATLAB 命令窗口中显示关联的标幺值基准值。
- **Display Associated Initial Conditions** 在 MATLAB 命令窗口中显示关联的初始条件。

### 建模热效应

您可以暴露热端口来建模生成的热量和电机温度的影响。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

对于此模块，仅当在 **Initial Conditions** 部分中将 **Initialization option** 参数设置为 `设置转子角和 Park 的目标 transform variables` 时，**Initial Targets** 设置才可见。

额定值提供了一种指定模型中变量预期幅值的方法。使用基于额定值的系统缩放可提高仿真鲁棒性。额定值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
