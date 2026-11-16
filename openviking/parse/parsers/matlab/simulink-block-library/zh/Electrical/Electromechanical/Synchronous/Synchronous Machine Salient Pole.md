---
type: simulink-block
title: 'Synchronous Machine Salient Pole'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinesalientpole'
documentation_source_path: 'ref/synchronousmachinesalientpole.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine Salient Pole

## 端口

### 输出

### **pu** — 电机标幺值测量 物理

与电机标幺值测量关联的物理信号矢量端口。矢量元素为：

- 励磁电压（励磁电路基准值，Efd），*pu\_fd\_Efd*
- 励磁电流（励磁电路基准值，Ifd），*pu\_fd\_Ifd*
- 电磁转矩，*pu\_torque*
- 转子速度，*pu\_velocity*
- 定子 d 轴电压，*pu\_ed*
- 定子 q 轴电压，*pu\_eq*
- 定子零序电压，*pu\_e0*
- 定子 d 轴电流，*pu\_id*
- 定子 q 轴电流，*pu\_iq*
- 定子零序电流，*pu\_i0*
- 转子电角度，*electrical\_angle\_out*

要连接到此端口，请使用 Synchronous Machine Measurement 模块。

### 守恒

### **fd+** — 励磁绕组正极端子 电气

与励磁绕组正极端子关联的电气守恒端口。

### **fd-** — 励磁绕组负极端子 电气

与励磁绕组负极端子关联的电气守恒端口。

### **R** — 电机转子 机械

与电机转子关联的机械旋转守恒端口。

### **C** — 电机外壳 机械

与电机外壳关联的机械旋转守恒端口。

### **~** — 定子绕组 电气

与定子绕组关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **n** — 中性点 电气

与星形绕组配置的中性点关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **零序** 设置为 `Include`。

### **a** — *a* 相 电气

与 *a* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相 电气

与 *b* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相 电气

与 *c* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **HA** — *a* 相端子热端口 热

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口 热

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口 热

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HR** — 转子热端口 热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 启用热端口的选项 `No thermal port`（默认）| `Show thermal port`

启用模块热端口并对生成热量和电机温度效应进行建模的选项。

### 主要

### **电气连接** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

使用复合三相端口还是扩展三相端口。

### **额定视在功率** — 额定视在功率 `300e6` `V*A`（默认）

额定视在功率。

### **额定电压** — RMS 额定线电压 `24e3` `V`（默认）

RMS 额定线电压。

### **额定电气频率** — 标称电气频率 `60` `Hz`（默认）

给出额定视在功率时的标称电气频率。

### **极对数** — 极对数 `10`（默认）

电机极对数。

### **指定参数化方式** — 模块参数化 `Fundamental parameters`（默认）| `Standard parameters`

模块参数化方法。选项包括：

- `Fundamental parameters` — 使用基本参数指定阻抗。
- `Standard parameters` — 使用基本参数指定阻抗，并指定 d 轴和 q 轴时间常数。

#### 依赖关系

如果此参数设置为 `Fundamental parameters`：

- **阻抗** 设置中的基本参数可见。
- **时间常数** 设置可见。

如果此参数设置为 `Standard parameters`：

- **阻抗** 设置中的标准参数可见。
- **时间常数** 设置不可见。

### **通过以下方式指定空载时产生额定端电压所需的励磁电路输入** — 通过以下方式指定空载时产生额定端电压所需的励磁电路输入 `Field circuit current`（默认）| `Field circuit voltage`

励磁电路参数化方法。选项包括：

- `Field circuit voltage` — 以电压形式指定励磁电路。
- `Field circuit current` — 以电流形式指定励磁电路。

此参数影响 **励磁电路电压** 和 **励磁电路电流** 参数的可见性。

#### 依赖关系

如果此参数设置为 `Field circuit voltage`。

- **励磁电路电压** 参数可见。
- **励磁电路电流** 参数不可见。

如果此参数设置为 `Field circuit current`：

- **励磁电路电流** 参数可见。
- **励磁电路电压** 参数不可见。

### **励磁电路电压** — 励磁电路电压 `216.54` `V`（默认）

在电机端子处产生额定电压的励磁电路两端电压。

#### 依赖关系

仅当 **通过以下方式指定空载时产生额定端电压所需的励磁电路输入** 参数设置为 `Field circuit voltage` 时，此参数才可见。

### **励磁电路电流** — 励磁电路电流 `1000` `A`（默认）

在电机端子处产生额定电压的励磁电路中的电流。

#### 依赖关系

仅当 **通过以下方式指定空载时产生额定端电压所需的励磁电路输入** 参数设置为 `Field circuit current` 时，此参数才可见。

### **零序** — 零序模型 `Include`（默认）| `Exclude`

零序模型：

- `Include` — 优先考虑模型保真度。此模型是默认零序模型。如果为使用 Partitioning 求解器的仿真包含零序项，则会发生错误。有关详细信息，请参阅使用 Partitioning 求解器提高仿真速度。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

#### 依赖关系

如果此参数设置为：

- `Include` 且 **指定参数化方式** 设置为 **Fundamental parameters** — **阻抗** 设置中的 **定子零序电感，L0** 参数可见。
- `Include` 且 **指定参数化方式** 设置为 **Standard parameters** — **阻抗** 设置中的 **零序电抗，X0** 参数可见。
- `Exclude` — **阻抗** 设置中的零序参数不可见。

### **转子角度定义** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。

当选择默认值时，转子 *d* 轴与定子 *a* 相磁轴在转子角度为零时对齐。

此参数的另一个可选值为 `Angle between the a-phase magnetic axis and the q-axis`。选择此值时，转子 *q* 轴与定子 *a* 相磁轴在转子角度为零时对齐。

### 阻抗

### **定子 d 轴互感（未饱和），Ladu** — 定子 d 轴互感（未饱和） `0.9`（默认）| positive scalar

未饱和定子 *d* 轴互感，以标幺值表示。如果 **磁饱和表示** 设置为 `None`，则这等效于定子 d 轴互感。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子 q 轴互感，Laq** — 定子 q 轴互感 `0.55`（默认）| positive scalar

定子 *q* 轴互感，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子零序电感，L0** — 定子零序电感 `0.15`（默认）| positive scalar

定子零序电感，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 且 **零序** 参数设置为 `Include` 时，此参数才可见。

### **定子漏电感，Ll** — 定子漏电感 `0.15`（默认）| positive scalar

定子漏电感，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子电阻，Ra** — 定子电阻 `0.011`（默认）| positive scalar

定子电阻，以标幺值表示。此参数必须大于 0。

### **转子励磁电路电感，Lfd** — 转子励磁电路电感 `0.2571`（默认）| positive scalar

转子励磁电路电感，以标幺值表示。此参数必须大于 0。

### **转子励磁电路电阻，Rfd** — 转子励磁电路电阻 `0.0006`（默认）| positive scalar

转子励磁电路电阻，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 d 轴阻尼绕组 1 电感，L1d** — 转子 d 轴阻尼绕组 1 电感 `0.2`（默认）| positive scalar

转子 *d* 轴阻尼绕组 1 电感，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 d 轴阻尼绕组 1 电阻，R1d** — 转子 d 轴阻尼绕组 1 电阻 `0.0354`（默认）| positive scalar

转子 *d* 轴阻尼绕组 1 电阻，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 q 轴阻尼绕组 1 电感，L1q** — 转子 q 轴阻尼绕组 1 电感 `0.2567`（默认）| positive scalar

转子 *q* 轴阻尼绕组 1 电感，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 q 轴阻尼绕组 1 电阻，R1q** — 转子 q 轴阻尼绕组 1 电阻 `0.0428`（默认）| positive scalar

转子 *q* 轴阻尼绕组 1 电阻，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子漏电抗，Xl** — 定子漏电抗 `0.15`（默认）| positive scalar

定子漏电抗，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Standard parameters` 时，此参数才可见。

### **d 轴同步电抗，Xd** — d 轴同步电抗 `1.05`（默认）| positive scalar

*d* 轴同步电抗，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Standard parameters` 时，此参数才可见。

### **q 轴同步电抗，Xq** — q 轴同步电抗 `0.7`（默认）| positive scalar

*q* 轴同步电抗，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Standard parameters` 时，此参数才可见。

### **零序电抗，X0** — 零序电抗 `0.15`（默认）| positive scalar

零序电抗，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Standard parameters` 且 **零序** 参数设置为 `Include` 时，此参数才可见。

### **d 轴暂态电抗，Xd'** — d 轴暂态电抗 `0.35`（默认）| positive scalar

*d* 轴暂态电抗，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Standard parameters` 时，此参数才可见。

### **d 轴次暂态电抗，Xd''** — d 轴次暂态电抗 `0.25`（默认）| positive scalar

*d* 轴次暂态电抗，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Standard parameters` 时，此参数才可见。

### **q 轴次暂态电抗，Xq''** — q 轴次暂态电抗 `0.325`（默认）| positive scalar

*q* 轴次暂态电抗，以标幺值表示。此参数必须大于 0。

#### 依赖关系

仅当 **指定参数化方式** 参数设置为 `Standard parameters` 时，此参数才可见。

### 时间常数

### **指定 d 轴时间常数** — 指定 d 轴时间常数 `Open circuit`（默认）| `Short circuit`

在 `Open circuit` 和 `Short circuit` 之间选择。

此参数的设置会影响 *d* 轴时间常数参数的可见性。

### **d 轴暂态开路，Td0'** — d 轴暂态开路 `5.25` `s`（默认）| positive scalar

*d* 轴暂态开路时间常数。此参数必须：

- 大于 0。
- 大于 **d 轴次暂态开路，Td0''**。

#### 依赖关系

仅当 **指定 d 轴暂态时间常数** 参数设置为 `Open circuit` 时，此参数才可见。

### **d 轴暂态短路，Td'** — d 轴暂态短路 `1.75` `s`（默认）| positive scalar

*d* 轴暂态短路时间常数。此参数必须：

- 大于 0。
- 大于 **d 轴次暂态短路，Td''**。

#### 依赖关系

仅当 **指定 d 轴暂态时间常数** 参数设置为 `Short circuit` 时，此参数才可见。

### **d 轴次暂态开路，Td0''** — d 轴次暂态开路 `0.03` `s`（默认）| positive scalar

*d* 轴次暂态开路时间常数。此参数必须大于 0。

#### 依赖关系

仅当 **指定 d 轴暂态时间常数** 参数设置为 `Open circuit` 时，此参数才可见。

### **d 轴次暂态短路，Td''** — d 轴次暂态短路 `0.0214` `s`（默认）| positive scalar

*d* 轴次暂态短路时间常数。此参数必须大于 0。

#### 依赖关系

仅当 **指定 d 轴暂态时间常数** 参数设置为 `Short circuit` 时，此参数才可见。

### **指定 q 轴时间常数** — 指定 q 轴时间常数 `Open circuit`（默认）| `Short circuit`

在 `Open circuit` 和 `Short circuit` 之间选择。

此参数的设置会影响 *q* 轴时间常数参数的可见性。

### **q-axis subtransient open-circuit, Tq0'** — q 轴次暂态开路 `0.05` `s`（默认）| positive scalar

*q* 轴次暂态开路时间常数。
此参数必须大于 0。

#### 依赖关系

此参数仅当 **Specify q-axis
transient time constant** 参数设置为
`Open circuit` 时可见。

### **q-axis subtransient short-circuit, Tq'** — q 轴次暂态短路 `0.0232` `s`（默认）| positive scalar

*q* 轴次暂态短路时间常数。
此参数必须大于 0。

#### 依赖关系

此参数仅当 **Specify q-axis
transient time constant** 参数设置为
`Short circuit` 时可见。

### 饱和

### **Magnetic saturation representation** — 磁饱和表示 `None`（默认）| `Open-circuit lookup table (v versus i)`

模块磁饱和模型：

- `None`
- `Open-circuit lookup table (v versus
  i)`

#### 依赖关系

如果将此参数设置为 `Open-circuit lookup
table (v versus i)`，则相关参数可见。

### **Per-unit field current saturation data, ifd** — 标幺磁场电流饱和数据 `[0, .48, .76, 1.38, 1.79]`（默认）

磁场电流 *ifd* 数据，
用于填充气隙电压 *Vag* 对磁场电流 *ifd* 的查找表。
此参数必须包含元素数量在 `5` 到 `10` 之间的向量。

#### 依赖关系

此参数仅当 **Magnetic
saturation representation** 参数设置为
`Open-circuit lookup table (v versus
i)` 时可见。

### **Per-unit air-gap voltage saturation data, Vag** — 标幺气隙电压饱和数据 `[0, .8, 1.08, 1.31, 1.4]`（默认）

气隙电压 *Vag* 数据，
用于填充气隙电压 *Vag* 对磁场电流 *ifd* 的查找表。
此参数必须包含元素数量在 `5` 到 `10` 之间的向量。

#### 依赖关系

此参数仅当 **Magnetic
saturation representation** 参数设置为
`Open-circuit lookup table (v versus
i)` 时可见。

### 初始条件

### **Initialization option** — 用于指定仿真开始时的值的选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认）| `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

用于指定仿真开始时某些参数和变量的值的选项。将此参数设置为：

- `Set real power, reactive power, terminal
  voltage and terminal phase` — 设置运行点，无论连接的网络如何。
- `Set targets for rotor angle and Park's
  transform variables` — 使用 **Variables**
  设置，在仿真前指定模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。
- `Set targets for load flow
  variables` — 选择母线类型，并在
  **Initial Conditions** 设置中指定潮流分析的相关参数。

### **Source type** — 电压源模型 `Swing bus`（默认）| `PV bus` | `PQ bus`

模块建模的电压源类型。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set targets for load flow
variables`。

### **Terminal voltage magnitude** — 端子电压幅值 `24e3` `V`（默认）| positive scalar

端子电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set real power, reactive
power, terminal voltage, and terminal phase`。
或者，将 **Initialization option** 设置为
`Set targets for load flow variables`，
并将 **Source type** 设置为 `Swing
bus` 或 `PV bus`。

### **Terminal voltage angle** — 端子电压角度 `0` `deg`（默认）| scalar

端子电压角度。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set real power, reactive
power, terminal voltage, and terminal phase`。
或者，将 **Initialization option** 设置为
`Set targets for load flow variables`，
并将 **Source type** 设置为 `Swing
bus`。

### **Active power generated** — 生成的有功功率 `500e6` `V*A`（默认）| scalar

电机生成的有功功率。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set real power, reactive
power, terminal voltage, and terminal phase`。
或者，将 **Initialization option** 设置为
`Set targets for load flow variables`，
并将 **Source type** 设置为 `PV
bus` 或 `PQ bus`。

### **Reactive power generated** — 生成的无功功率 `0` `V*A`（默认）| scalar

电机生成的无功功率。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set real power, reactive
power, terminal voltage, and terminal phase`。
或者，将 **Initialization option** 设置为
`Set targets for load flow variables`，
并将 **Source type** 设置为 `PQ
bus`。

### **Minimum terminal voltage magnitude (pu)** — 最小端子电压幅值 `0.95`（默认）| positive scalar

标幺最小稳态电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set targets for load flow
variables`，并将 **Source type** 设置为
`PQ bus`。

### **Phase search range at terminals** — 端子处相位搜索范围 `[-inf, inf]` `deg`（默认）| vector of two elements

定义端子处相角搜索范围的向量。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set targets for load flow
variables`，并将 **Source type** 设置为
`PV bus` 或 `PQ
bus`。

### **Parasitic conductance to electrical reference** — 到电气参考的寄生电导 `1e-6` `S`（默认）| positive scalar

到电气参考的寄生电导。

#### 依赖关系

要启用此参数，请将 **Initialization
option** 设置为 `Set targets for load flow
variables`。

### 热

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认）| real scalar

用于引用电机参数的温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| positive scalar

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值，
`3.93e-3` 1/K，适用于铜。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| positive scalar

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| positive scalar

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2021b：电气连接端口更新

从 R2021b 开始，要在复合端口和扩展端口之间切换，请将
**Electrical connection** 参数设置为
`Composite three-phase ports` 或 `Expanded
three-phase ports`。此外，simlog 格式对于
`Composite three-phase ports` 和 `Expanded
three-phase ports` 是相同的。

由于这些更改，在早期版本中保存的模型内，请检查
此模块的 **Electrical connection** 参数。

## 描述

具有基本或标准参数化的凸极同步电机

Synchronous Machine Salient Pole 模块使用基本参数或标准参数对凸极同步电机进行建模。

### 使用潮流目标值初始化 Synchronous Machine

如果模块位于与频率-时间仿真模式兼容的网络中，您可以对网络执行潮流分析。潮流分析提供稳态值，您可以使用这些值初始化电机。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。有关展示如何使用潮流分析数据初始化同步电机的示例，请参阅 Synchronous Machine Initialization with Loadflow。

### 方程

同步电机方程相对于旋转参考坐标系表示，该坐标系定义为

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

- *ed*、
  *eq* 和
  *e0* 是由以下定义的
  *d* 轴、*q* 轴和零序定子电压：

  [edeqe0]=Ps[vavbvc].

  *va*、
  *vb* 和
  *vc* 是从端口 **~** 到中性端口
  **n** 测得的定子电压。
- *ωbase* 是标幺基准电角速度。
- *ψd*、
  *ψq* 和
  *ψ0* 是
  *d* 轴、*q* 轴和零序定子磁链。
- *ωr* 是标幺转子旋转速度。
- *Ra* 是定子电阻。
- *id*、
  *iq* 和
  *i0* 是由以下定义的
  *d* 轴、*q* 轴和零序定子电流：

  [idiqi0]=Ps[iaibic].

  *ia*、
  *ib* 和
  *ic* 是从端口 ~ 流到端口 n 的定子电流。

转子电压方程定义为

efd=1ωbasedΨfddt+Rfdifd,

e1d=1ωbasedΨ1ddt+R1di1d=0,

以及

e1q=1ωbasedΨ1qdt+R1qi1q=0,

其中：

- *efd* 是励磁电压。
- *e1d* 和
  *e1q* 是
  *d* 轴阻尼绕组 1 和
  *q* 轴阻尼绕组 1 两端的电压。它们等于
  0。
- *ψfd*、
  *ψ1d* 和
  *ψ1q* 是连接励磁电路、
  *d* 轴阻尼绕组 1 和 *q* 轴阻尼绕组 1 的磁通。
- *Rfd*、
  *R1d* 和 *R1q* 是
  转子励磁电路、*d* 轴阻尼
  绕组 1 和 *q* 轴阻尼绕组 1 的电阻。
- *ifd*、
  *i1d* 和 *i1q* 是
  在励磁电路、*d* 轴阻尼绕组
  1 和 *q* 轴阻尼绕组 1 中流动的电流。

饱和方程定义为

ψad=ψd+Llid,

ψaq=ψq+Lliq,

ψat=ψad2+ψaq2,

Ks=1（如果饱和被禁用），

Ks=f(ψat)（如果饱和被启用），

以及

Lad=Ks\*Ladu,

其中：

- *ψad* 是
  *d* 轴气隙磁链或互感磁链。
- *ψaq* 是
  *q* 轴气隙磁链或互感磁链。
- *ψat* 是气隙磁链。
- *Ks* 是饱和因子。
- *Ladu* 是定子 *d* 轴未饱和互感。
- *Lad* 是定子 *d* 轴互感。

饱和因子函数 *f* 根据标幺开路查找表计算如下：

Lad=dψatdifd,

Vag=g(ifd),

以及

Lad=dg(ifd)difd=dVagdifd,

其中：

- *Vag* 是标幺气隙电压。

在标幺制中，

Ks=LadLadu,

以及

ψat=Vag

可重排为

Ks=f(ψat).

定子磁链方程定义为

Ψd=−(Lad+Ll)id​+Ladifd+Ladi1d,

Ψq=−(Laq+Ll)iq​+Laqi1q,

以及

Ψ0=−L0i0,

其中：

- *Ll* 是定子漏电感。
- *Lad* 和
  *Laq* 是定子 *d* 轴和
  *q* 轴互感。

转子磁链方程定义为

ψfd=Lffdifd+Lf1di1d−Ladid,

ψ1d=Lf1difd+L11di1d−Ladid,

以及

ψ1q=L11qi1q−Laqiq,

其中：

- *Lffd* 是转子励磁电路的自感。
- *L11d* 是 *d* 轴阻尼绕组 1 的自感。
- *L11q* 是 *q* 轴阻尼绕组 1 的自感。
- *Lf1d* 是转子励磁
  电路和 *d* 轴阻尼绕组 1 互感。

电感由以下方程定义：

Lffd=Lad+Lfd

Lf1d=Lffd−Lfd

L11d=Lf1d+L1d

L11q=Laq+L1q

这些电感方程假设标幺互感
*L12q* =
*Laq*，即 *q* 轴中的定子和转子
电流都链接由 *Laq* 表示的单个互感磁通。

转子转矩定义为

Te=Ψdiq−Ψqid.

### 绘图和显示选项

您可以使用模块上下文菜单上的
**Electrical** 菜单执行绘图和显示操作。

右键单击模块，然后从 **Electrical** 菜单中选择以下选项之一：

- **Display Base Values** — 在 MATLAB® Command Window 中显示电机的标幺基准值。
- **Display Associated Base Values** — 在 MATLAB Command Window 中显示关联的标幺基准值。
- **Display Associated Initial Conditions** —
  在 MATLAB Command Window 中显示关联的初始条件。
- **Plot Open-Circuit Saturation (pu)** — 在 MATLAB 图窗中绘制气隙电压 *Vag* 对励磁电流 *ifd* 的关系，二者均以标幺值计量。该图包含三条迹线：

  - 未饱和 — 您指定的 **Stator d-axis mutual inductance
    (unsaturated), Ladu**
  - 饱和 — 您指定的 **Per-unit open-circuit lookup table (Vag
    versus ifd)**
  - 派生 — 由您指定的 **Per-unit open-circuit lookup table (Vag versus
    ifd)** 得出的开路查找表（标幺）。此数据用于计算
    饱和因子 *Ks* 对磁链
    *ψat* 的特性。
- **Plot Saturation Factor (pu)** — 使用当前电机参数，在 MATLAB 图窗中绘制饱和
  因子 *Ks* 对磁链 *ψat* 的关系，二者均以标幺值计量。此
  参数由您指定的其他参数得出：

  - **Stator d-axis mutual inductance (unsaturated),
    Ladu**
  - **Per-unit field current saturation data,
    ifd**
  - **Per-unit air-gap voltage saturation data,
    Vag**
- **Plot Power Capability
  Curves** — 在 MATLAB 图窗中绘制有功功率 P 对无功功率 Q 的关系，二者均以标幺值计量。该图可能包含多条迹线。每条
  迹线对应以标幺值（非互易标幺系统）计量的最大励磁电路电压。该图显示发电机在滞后功率因数下运行时产生的最大无功功率，以及发电机在超前功率因数下运行时吸收的最小无功功率。*(since R2023b)*

### 建模热效应

您可以暴露热端口来建模生成的热量和电机温度的影响。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行机构模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，
请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

对于此模块，仅当在 **Initial Conditions** 部分中，将 **Initialization
option** 参数设置为 `Set targets for rotor angle and Park's
transform variables` 时，**Initial Targets** 设置才可见。

标称值提供了一种在模型中指定变量预期幅值的方法。
使用基于标称值的系统缩放可提高仿真鲁棒性。标称
值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal
Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
