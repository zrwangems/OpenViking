---
type: simulink-block
title: 'Induction Machine Squirrel Cage'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'inductionmachinesquirrelcage'
documentation_source_path: 'ref/inductionmachinesquirrelcage.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Squirrel Cage

## 端口
```yaml
ports:
- name: pu
  summary: 标幺值测量输出端口 physical
  direction: input
- name: R
  summary: 电机转子机械
  direction: input
- name: C
  summary: 电机机壳机械
  direction: input
- name: ~1
  summary: 定子正端连接 electrical
  direction: input
- name: ~2
  summary: 定子负端连接 electrical
  direction: input
- name: a1
  summary: '*a* 正端连接 electrical'
  direction: input
- name: b1
  summary: '*b* 正端连接 electrical'
  direction: input
- name: c1
  summary: '*c* 正端连接 electrical'
  direction: input
- name: a2
  summary: '*a* 负端连接 electrical'
  direction: input
- name: b2
  summary: '*b* 负端连接 electrical'
  direction: input
- name: c2
  summary: '*c* 负端连接 electrical'
  direction: input
- name: HA
  summary: '*a* 相端子热端口 thermal'
  direction: input
- name: HB
  summary: '*b* 相端子热端口 thermal'
  direction: input
- name: HC
  summary: '*c* 相端子热端口 thermal'
  direction: input
- name: HR
  summary: 转子热端口 thermal
  direction: input
```

### 输入

### **pu** — 标幺值测量输出端口 physical

与电机标幺值测量相关联的物理信号矢量端口。矢量元素为：

- *pu\_torque*
- *pu\_velocity*
- *pu\_vds*
- *pu\_vqs*
- *pu\_v0s*
- *pu\_ids*
- *pu\_iqs*
- *pu\_i0s*
### 守恒

### **R** — 电机转子机械

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳机械

与电机机壳相关联的机械旋转守恒端口。

### **~1** — 定子正端连接 electrical

与定子正端连接相关联的可扩展三相端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Composite three-phase
ports`。

### **~2** — 定子负端连接 electrical

与定子负端连接相关联的可扩展三相端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Composite three-phase
ports`。

### **a1** — *a* 正端连接 electrical

与 *a* 正端连接相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **b1** — *b* 正端连接 electrical

与 *b* 正端连接相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **c1** — *c* 正端连接 electrical

与 *c* 正端连接相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **a2** — *a* 负端连接 electrical

与 *a* 负端连接相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **b2** — *b* 负端连接 electrical

与 *b* 负端连接相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **c2** — *c* 负端连接 electrical

与 *c* 负端连接相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`。

### **HA** — *a* 相端子热端口 thermal

与定子绕组 *a* 相关联的热守恒端口。

#### 依赖

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HB** — *b* 相端子热端口 thermal

与定子绕组 *b* 相关联的热守恒端口。

#### 依赖

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HC** — *c* 相端子热端口 thermal

与定子绕组 *c* 相关联的热守恒端口。

#### 依赖

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HR** — 转子热端口 thermal

与转子相关联的热守恒端口。

#### 依赖

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主要
- name: Rated apparent power
  summary: 额定视在功率 15e3 V*A（默认）
  group: 主要
- name: Rated voltage
  summary: RMS 电压 220 V（默认）
  group: 主要
- name: Rated electrical frequency
  summary: 额定电气频率 60 Hz（默认）
  group: 主要
- name: Number of pole pairs
  summary: 电机极对数 1（默认）
  group: 主要
- name: Parameterization unit
  summary: 模块参数化单位制 SI（默认）| Per unit
  group: 主要
- name: Squirrel cage
  summary: 鼠笼规格选项 Single squirrel cage（默认）| Double squirrel cage
  group: 主要
- name: Zero sequence
  summary: 零序 Include（默认）| Exclude
  group: 主要
- name: Initialization option
  summary: 初始化方法 Set targets for flux variables（默认）| Set targets for load flow variables
  group: 主要
- name: Stator resistance, Rs
  summary: 定子电阻 0.25 Ohm（默认）
  group: 阻抗
- name: Stator leakage reactance, Xls
  summary: 定子漏电抗 0.4 Ohm（默认）
  group: 阻抗
- name: Referred rotor resistance, Rr'
  summary: 折算转子电阻 0.14 Ohm（默认）
  group: 阻抗
- name: Referred rotor leakage reactance, Xlr'
  summary: 折算转子漏电抗 0.41 Ohm（默认）
  group: 阻抗
- name: Referred rotor resistance in cage 1, Rr1'
  summary: 第一个笼的折算转子电阻 0.28 Ohm（默认）
  group: 阻抗
- name: Referred rotor leakage reactance in cage 1, Xlr1'
  summary: 第一个笼的折算转子漏电抗 0.82 Ohm（默认）
  group: 阻抗
- name: Referred rotor resistance in cage 2, Rr2'
  summary: 第二个笼的折算转子电阻 0.28 Ohm（默认）
  group: 阻抗
- name: Referred rotor leakage reactance in cage 2, Xlr2'
  summary: 第一个笼的折算转子漏电抗 0.82 Ohm（默认）
  group: 阻抗
- name: Magnetizing reactance, Xm
  summary: 励磁电抗 17 Ohm（默认）
  group: 阻抗
- name: Stator zero-sequence reactance, X0
  summary: 定子零序电抗 0.4 Ohm（默认）
  group: 阻抗
- name: Stator resistance, Rs (pu)
  summary: 标幺值定子电阻 0.0258（默认）
  group: 阻抗
- name: Stator leakage inductance, Lls (pu)
  summary: 标幺值定子漏电感 0.0413（默认）
  group: 阻抗
- name: Referred rotor resistance, Rr' (pu)
  summary: 标幺值折算转子电阻 0.0145（默认）
  group: 阻抗
- name: Referred rotor leakage inductance, Llr' (pu)
  summary: 标幺值折算转子漏电感 0.0424（默认）
  group: 阻抗
- name: Referred rotor resistance in cage 1, Rr1' (pu)
  summary: 笼 1 的标幺值折算转子电阻 0.0290（默认）
  group: 阻抗
- name: Referred rotor leakage inductance in cage 1, Llr1' (pu)
  summary: 标幺值折算转子漏电感 0.0848（默认）
  group: 阻抗
- name: Referred rotor resistance in cage 2, Rr2' (pu)
  summary: 笼 2 的标幺值折算转子电阻 0.0290（默认）
  group: 阻抗
- name: Referred rotor leakage inductance in cage 2, Llr2' (pu)
  summary: 标幺值折算转子漏电感 0.0848（默认）
  group: 阻抗
- name: Magnetizing inductance, Lm (pu)
  summary: 标幺值励磁电感 1.7562（默认）
  group: 阻抗
- name: Stator zero-sequence inductance, L0 (pu)
  summary: 标幺值定子零序电感 0.0413（默认）
  group: 阻抗
- name: Magnetic saturation representation
  summary: 磁饱和表示 None（默认）| Open-circuit lookup table (v versus i)
  group: 饱和
- name: No-load line current saturation data, i (rms)
  summary: 空载线电流 RMS 饱和数据 [0, 4, 9, 18, 25, 34, 50, 68, 95, 120] A（默认）
  group: 饱和
- name: Terminal voltage saturation data, v (phase-phase, rms)
  summary: 端子 RMS 电压饱和数据 [0, 88, 154, 198, 220, 242, 264, 286, 308, 327] V（默认）
  group: 饱和
- name: 标幺值空载线电流饱和数据，i
  summary: 标幺值空载线电流饱和数据 [0, .176, .396, .792, 1.1, 1.496, 2.2, 2.992, 4.18, 5.28]（默认）
  group: 饱和
- name: 标幺值端电压饱和数据，v
  summary: 标幺值端电压饱和数据 [0, .4, .7, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.4864]（默认）
  group: 饱和
- name: 测量温度
  summary: 额定温度 298.15 K（默认）| 实标量
  group: 热
- name: 电阻温度系数
  summary: 温度系数 3.93e-3 1/K（默认）| 正标量
  group: 热
- name: 笼型电阻温度系数
  summary: 转子温度系数 4.4e-3（默认）| 1/K | 标量
  group: 热
- name: 每个定子绕组的热质量
  summary: 绕组热质量 100 J/K（默认）| 正标量
  group: 热
- name: 转子热质量
  summary: 转子热质量 200 J/K（默认）| 正标量
  group: 热
```

所有默认参数值均基于电机三角形绕组配置。

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并建模生成热量和电机温度的影响。

### 主要

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是展开三相端口。

### **Rated apparent power** — 额定视在功率 `15e3` `V*A`（默认）

感应电机在电气侧的额定视在功率。

### **Rated voltage** — RMS 电压 `220` `V`（默认）

RMS 线电压。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）

对应于额定视在功率的额定电气频率。

### **Number of pole pairs** — 电机极对数 `1`（默认）

电机极对数。

### **Parameterization unit** — 模块参数化单位制 `SI`（默认）| `Per unit`

模块参数化的单位制。在 `SI`（国际单位制）和 `Per unit`（标幺值制）之间选择。

#### 依赖

选择：

- `SI` 会在 **Impedances** 和
  **Saturation** 设置中显示 SI 参数。
- `Per unit` 会在 **Impedances** 和
  **Saturation** 设置中显示标幺值参数。

### **Squirrel cage** — 鼠笼规格选项 `Single squirrel cage`（默认）| `Double squirrel cage`

指定电机为单鼠笼或双鼠笼的选项。

将此参数设置为 `Double squirrel cage` 会显示第二个笼的 **Impedances** 参数。

### **Zero sequence** — 零序 `Include`（默认）| `Exclude`

零序模型：

- `Include` — 优先考虑模型保真度。如果对使用 Partitioning 求解器的仿真包含零序项，则会发生错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

#### 依赖

如果此参数设置为：

- `Include` 且 **Parameterization unit** 设置为
  `SI` — **Impedances** 设置中的 **Stator
  zero-sequence reactance, X0** 参数可见。
- `Include` 且 **Parameterization unit** 设置为
  `Per unit` — **Impedances** 设置中的
  **Stator zero-sequence inductance, pu\_L0
  (pu)** 参数可见。
- `Exclude` — **Impedances** 设置中的定子零序参数不可见。

### **Initialization option** — 初始化方法 `Set targets for flux variables`（默认）| `Set targets for load flow variables`

初始化方法。您可以使用磁链数据或潮流分析数据来初始化电机以进行稳态仿真。

如果选择 `Set targets for load flow variables`，要完全指定初始条件，必须以高优先级目标值的形式包含初始化约束。例如，如果您的感应电机连接到 Inertia 模块，则在 Inertia 模块的 **Initial Targets** 部分中，将 **Rotational velocity** 的 **Priority** 设置为 `High`，即可完全指定感应电机的初始条件。或者，您可以将 Inertia 模块 **Rotational velocity** 的 **Priority** 设置为 `None`，而将感应电机模块 **Slip**、**Real power generated** 或 **Mechanical power consumed** 的 **Priority** 设置为 `High`。

#### 依赖

**Initial Targets** 部分中可见的变量类型取决于您在 **Main** 部分中为 **Initialization option** 参数选择的初始化方法。要使用以下方式指定目标值：

- 磁链变量 — 将 **Initialization option** 参数设置为 `Set targets for flux variables`。
- 潮流分析数据 — 将 **Initialization option** 参数设置为 `Set targets for load flow variables`。

### 阻抗

对于 **Main** 设置中的 **Parameterization unit** 参数，选择 `SI` 以显示 SI 参数，或选择 `Per unit` 以显示标幺值参数。

### **Stator resistance, Rs** — 定子电阻 `0.25` `Ohm`（默认）

定子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI` 时，此参数才可见。

### **Stator leakage reactance, Xls** — 定子漏电抗 `0.4` `Ohm`（默认）

定子漏电抗。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI` 时，此参数才可见。

### **Referred rotor resistance, Rr'** — 折算转子电阻 `0.14` `Ohm`（默认）

折算到定子的转子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **Referred rotor leakage reactance, Xlr'** — 折算转子漏电抗 `0.41` `Ohm`（默认）

折算到定子的转子漏电抗。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **Referred rotor resistance in cage 1, Rr1'** — 第一个笼的折算转子电阻 `0.28` `Ohm`（默认）

笼 1 中的转子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Referred rotor leakage reactance in cage 1, Xlr1'** — 第一个笼的折算转子漏电抗 `0.82` `Ohm`（默认）

笼 1 中的转子漏电抗。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Referred rotor resistance in cage 2, Rr2'** — 第二个笼的折算转子电阻 `0.28` `Ohm`（默认）

笼 2 中的转子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Referred rotor leakage reactance in cage 2, Xlr2'** — 第一个笼的折算转子漏电抗 `0.82` `Ohm`（默认）

笼 2 中的转子漏电抗。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Magnetizing reactance, Xm** — 励磁电抗 `17` `Ohm`（默认）

励磁电抗。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI` 时，此参数才可见。

### **Stator zero-sequence reactance, X0** — 定子零序电抗 `0.4` `Ohm`（默认）

定子零序电抗。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `SI`，且 **Main** 设置中的 **Zero sequence** 参数设置为 `Include` 时，此参数才可见。

### **Stator resistance, Rs (pu)** — 标幺值定子电阻 `0.0258`（默认）

标幺值定子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit` 时，此参数才可见。

### **Stator leakage inductance, Lls (pu)** — 标幺值定子漏电感 `0.0413`（默认）

标幺值定子漏电感。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit` 时，此参数才可见。

### **Referred rotor resistance, Rr' (pu)** — 标幺值折算转子电阻 `0.0145`（默认）

折算到定子的标幺值转子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **Referred rotor leakage inductance, Llr' (pu)** — 标幺值折算转子漏电感 `0.0424`（默认）

折算到定子的标幺值转子漏电感。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **Referred rotor resistance in cage 1, Rr1' (pu)** — 笼 1 的标幺值折算转子电阻 `0.0290`（默认）

笼 1 中的标幺值转子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Referred rotor leakage inductance in cage 1, Llr1' (pu)** — 标幺值折算转子漏电感 `0.0848`（默认）

笼 1 中的标幺值转子漏电感。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Referred rotor resistance in cage 2, Rr2' (pu)** — 笼 2 的标幺值折算转子电阻 `0.0290`（默认）

笼 2 中的标幺值转子电阻。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Referred rotor leakage inductance in cage 2, Llr2' (pu)** — 标幺值折算转子漏电感 `0.0848`（默认）

笼 2 中的标幺值转子漏电感。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit`，且 **Main** 设置中的 **Squirrel cage** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **Magnetizing inductance, Lm (pu)** — 标幺值励磁电感 `1.7562`（默认）

标幺值励磁电感，即定子-转子互感峰值。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit` 时，此参数才可见。

### **Stator zero-sequence inductance, L0 (pu)** — 标幺值定子零序电感 `0.0413`（默认）

标幺值定子零序电感。

#### 依赖

仅当您将 **Main** 设置中的 **Parameterization unit** 参数设置为 `Per unit`，且 **Main** 设置中的 **Zero sequence** 参数设置为 `Include` 时，此参数才可见。

### 饱和

对于 **Main** 设置中的 **Parameterization unit** 参数，选择 `SI` 以显示 SI 参数，或选择 `Per unit` 以显示标幺值参数。

饱和特性基于电机连接为三角形绕组配置。

### **Magnetic saturation representation** — 磁饱和表示 `None`（默认）| `Open-circuit lookup table (v versus i)`

模块磁饱和表示。

#### 依赖

如果此参数设置为 `Open-circuit lookup table (v versus i)`，则相关参数可见。

### **No-load line current saturation data, i (rms)** — 空载线电流 RMS 饱和数据 `[0, 4, 9, 18, 25, 34, 50, 68, 95, 120]` `A`（默认）

电流 *i* 数据填充电压 *v* 对励磁电流 *i* 的查找表。此参数必须包含至少 10 个元素的矢量。

#### 依赖

仅当 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table (v versus i)`，且在 **Main** 设置中 **Parameterization unit** 参数设置为 `SI` 时，此参数才可见。

### **Terminal voltage saturation data, v (phase-phase, rms)** — 端子 RMS 电压饱和数据 `[0, 88, 154, 198, 220, 242, 264, 286, 308, 327]` `V`（默认）

端子电压 *v* 数据填充电压 *v* 对电流 *i* 的查找表。此参数必须包含至少 10 个元素的矢量。元素数量必须与 **No-load line current saturation data, i (rms)** 参数的矢量元素数量匹配。

#### 依赖关系

仅当**磁饱和表示**参数设置为 `Open-circuit lookup table (v versus i)`，并且在**主**设置中，**参数化单位**参数设置为 `SI` 时，此参数才可见。

### **标幺值空载线电流饱和数据，i** — 标幺值空载线电流饱和数据 `[0, .176, .396, .792, 1.1, 1.496, 2.2, 2.992, 4.18, 5.28]`（默认）

电流 *i* 数据填充电压 *v* 对励磁电流 *i* 查找表。此参数必须包含至少 10 个元素的向量。

#### 依赖关系

仅当**磁饱和表示**参数设置为 `Open-circuit lookup table (v versus i)`，并且在**主**设置中，**参数化单位**参数设置为 `Per unit` 时，此参数才可见。

### **标幺值端电压饱和数据，v** — 标幺值端电压饱和数据 `[0, .4, .7, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.4864]`（默认）

端电压 *v* 数据填充电压 *v* 对电流 *i* 查找表。此参数必须包含至少 10 个元素的向量。元素数量必须与**标幺值空载线电流饱和数据，i**参数的向量元素数量匹配。

#### 依赖关系

仅当**磁饱和表示**参数设置为 `Open-circuit lookup table (v versus i)`，并且在**主**设置中，**参数化单位**参数设置为 `Per unit` 时，此参数才可见。

### 热

这些参数仅对具有暴露热端口的模块显示。

### **测量温度** — 额定温度 `298.15` `K`（默认）| 实标量

电机参数的标称温度。

### **电阻温度系数** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如执行器模块热模型所述。默认值 `3.93e-3` 1/K 适用于铜。

### **笼型电阻温度系数** — 转子温度系数 `4.4e-3`（默认）| `1/K` | 标量

转子笼型电阻与温度关系的系数。默认值 `4.4e-3` 1/K 适用于铝。

### **每个定子绕组的热质量** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **转子热质量** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。
## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将**电气连接**参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。此外，`Composite three-phase ports` 和 `Expanded three-phase ports` 的 simlog 格式相同。

由于这些更改，在早期版本保存的模型中，请检查此模块的**电气连接**参数。

### R2020a：饱和特性更新

从 R2020a 起，对于饱和特性，Induction Machine Squirrel Cage 模块考虑了由漏电感引起的磁通。

以下参数的默认值已更改：

- **定子漏电抗，Xls**
- **定子零序电抗，X0**
- **定子漏电感，Lls (pu)**
- **定子零序电感，L0 (pu)**
- **端电压饱和数据，v（相-相，RMS）**
- **标幺值端电压饱和数据，v**

由于这些更改，在早期版本保存的模型中，如果您使用了启用饱和的 Induction Machine Squirrel Cage 模块，请检查饱和数据。

## 描述

具有标幺值或 SI 参数化的鼠笼式转子感应电机

Induction Machine Squirrel Cage 模块对鼠笼式转子感应电机进行建模，其基本参数以标幺值或国际单位制（SI）表示。鼠笼式转子感应电机是一种感应电机。所有定子连接均可在模块上访问。因此，您可以使用星形和三角形配置之间的切换来对软启动过程进行建模。如果您需要访问转子绕组，请改用 Induction Machine Wound Rotor 模块。

将端口 **~1** 连接到三相电路。要将定子连接为三角形配置，请在端口 **~1** 和 **~2** 之间连接一个 Phase Permute 模块。要将定子连接为星形配置，请将端口 **~2** 连接到 Grounded Neutral (Three-Phase) 或 Floating Neutral (Three-Phase) 模块。

### 使用潮流目标值进行感应电机初始化

如果模块所在的网络与频率-时间仿真模式兼容，您可以对网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关更多信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。有关使用潮流分析数据初始化感应电机的示例，请参阅 Induction Motor Initialization with Loadflow。

### 方程

对于 SI 实现，模块将您输入的 SI 值转换为标幺值进行仿真。转换后的值基于电机连接为三角形绕组配置。

对于标幺值实现，您必须在阻抗选项卡中基于电机连接为三角形绕组配置来指定电阻和电感。

有关 SI 和标幺值电机参数之间关系的信息，请参阅 Per-Unit Conversion for Machine Parameters。有关标幺值参数化的信息，请参阅 Per-Unit System of Units。

感应电机方程相对于同步参考坐标系表示，定义为

θe(t)=∫0t2πfrateddt,

其中 *frated* 是**额定电气频率**参数的值。

Park 变换将定子方程映射到相对于额定电气频率静止的参考坐标系。Park 变换定义为

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212],

其中 *θe* 是电角度。

Park 变换用于定义标幺值感应电机方程。定子电压方程定义为

vds=1ωbasedψdsdt−ωψqs+Rsids,

vqs=1ωbasedψqsdt+ωψds+Rsiqs,

和

v0s=1ωbasedψ0sdt+Rsi0s,

其中：

- *vds*、*vqs* 和 *v0s* 是 *d* 轴、*q* 轴和零序定子电压，定义为

  [vdsvqsv0s]=Ps[vavbvc].

  *va*、*vb* 和 *vc* 是端口 **~1** 和 **~2** 之间的定子电压。
- *ωbase* 是标幺值基准电气速度。
- *ψds*、*ψqs* 和 *ψ0s* 是 *d* 轴、*q* 轴和零序定子磁链。
- *Rs* 是定子电阻。
- *ids*、*iqs* 和 *i0s* 是 *d* 轴、*q* 轴和零序定子电流，定义为

  [idsiqsi0s]=Ps[iaibic].

  *ia*、*ib* 和 *ic* 是从端口 **~1** 流向端口 **~2** 的定子电流。

转子电压方程定义为

vdr=1ωbasedψdrdt−(ω−ωr)ψqr+Rrdidr=0

和

vqr=1ωbasedψqrdt+(ω−ωr)ψdr+Rrdiqr=0,

其中：

- *vdr* 和 *vqr* 是 *d* 轴和 *q* 轴转子电压。
- *ψdr* 和 *ψqr* 是 *d* 轴和 *q* 轴转子磁链。
- *ω* 是标幺值同步速度。对于同步参考坐标系，该值为 1。
- *ωr* 是标幺值机械转速。
- *Rrd* 是折算到定子的转子电阻。
- *idr* 和 *iqr* 是 *d* 轴和 *q* 轴转子电流。

定子磁链方程定义为

ψds=Lssids+Lmidr,

ψqs=Lssiqs+Lmiqr,

和

ψ0s=Lssi0s,

其中 *Lss* 是定子自感，*Lm* 是励磁电感。

转子磁链方程定义为

ψdr=Lrrdidr+Lmids

和

ψqr=Lrrdiqr+Lmiqs,

其中 *Lrrd* 是折算到定子的转子自感。

转子转矩定义为

T=ψdsiqs−ψqsids.

定子自感 *Lss*、定子漏电感 *Lls* 和励磁电感 *Lm* 的关系为

Lss=Lls+Lm.

转子自感 *Lrrd*、转子漏电感 *Llrd* 和励磁电感 *Lm* 的关系为

Lrrd=Llrd+Lm.

当提供饱和曲线时，确定饱和励磁电感作为励磁磁通函数的方程为：

Lm\_sat=f(ψm)

ψm=ψdm2+ψqm2

对于无饱和情况，方程简化为

Lm\_sat=Lm

### 绘图和显示选项

您可以使用模块上下文菜单中的**电气**菜单执行绘图和显示操作。

右键单击模块，从**电气**菜单中选择一个选项：

- **Display Base Values** — 在 MATLAB® 命令窗口中显示电机标幺值基准值。
- **Plot Torque Speed (SI)** — 使用当前电机参数，在 MATLAB 图形窗口中绘制转矩对速度的关系，两者均以 SI 单位测量。
- **Plot Torque Speed (pu)** — 使用当前电机参数，在 MATLAB 图形窗口中绘制转矩对速度的关系，两者均以标幺值测量。
- **Plot Open-Circuit Saturation** — 在 MATLAB 图形窗口中绘制端电压对空载线电流的关系，两者均以标幺值表示。该图包含三条曲线：

  - Unsaturated — 定子励磁电感（未饱和）。
  - Saturated — 您指定的开路查找表（*v* 对 *i*）。
  - Derived — 从您指定的标幺值开路查找表（*v* 对 *i*）导出的开路查找表。此数据用于计算饱和励磁电感 *Lm\_sat* 和饱和因子 *Ks* 对磁链 *ψm* 的特性。
- **Plot Saturation Factor** — 使用电机参数，在 MATLAB 图形窗口中绘制饱和因子 *Ks* 对磁链 *ψm* 的关系。此参数从您指定的其他参数导出：

  - 空载线电流饱和数据，*i*
  - 端电压饱和数据，*v*
  - 漏电感，*Lls*
- **Plot Saturated Inductance** — 使用电机参数，在 MATLAB 图形窗口中绘制励磁电感 *Lm\_sat* 对磁链 *ψm* 的关系。此参数从您指定的其他参数导出：

  - 空载线电流饱和数据，*i*
  - 端电压饱和数据，*v*
  - 漏电感，*Lls*

对于 SI 实现，*v* 的单位为 V（相-相 RMS），*i* 的单位为 A（RMS）。

### 热效应建模

您可以暴露热端口来模拟产生的热量和电机温度的影响。要暴露热端口和**热**参数，请将**建模选项**参数设置为以下之一：

- `No thermal port` — 模块包含与定子绕组相关的电气守恒端口，但不包含热端口。
- `Show thermal port` — 模块包含与定子绕组相关的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的**标称值**部分。有关更多信息，请参阅 System Scaling by Nominal Values。

**初始目标**部分中可见的变量类型取决于您在**主**部分中为**初始化选项**参数选择的初始化方法。要使用以下方式指定目标值：

- 磁通变量 — 将**初始化选项**参数设置为 `Set targets for flux variables`。
- 潮流分析数据 — 将**初始化选项**参数设置为 `Set targets for load flow variables`。

如果您选择 `Set targets for load flow variables`，要完全指定初始条件，您必须以高优先级目标值的形式包含初始化约束。例如，如果您的感应电机连接到 Inertia 模块，则在 Inertia 模块的**初始目标**部分中，将**旋转速度**的**优先级**设置为 `High`，即可完全指定感应电机的初始条件。或者，您可以将 Inertia 模块**旋转速度**的**优先级**设置为 `None`，转而将感应电机模块**滑差**、**产生的有功功率**或**消耗的机械功率**的**优先级**设置为 `High`。
