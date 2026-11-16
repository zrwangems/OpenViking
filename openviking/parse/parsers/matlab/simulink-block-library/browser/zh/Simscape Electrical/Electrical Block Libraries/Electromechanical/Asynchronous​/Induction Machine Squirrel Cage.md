---
type: simulink-block
title: 'Induction Machine Squirrel Cage'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Asynchronous\u200b'
documentation_page: 'inductionmachinesquirrelcage'
documentation_source_path: 'ref/inductionmachinesquirrelcage.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Squirrel Cage

## 端口

### 输入

### **pu** — 标幺测量输出端口（物理）

与电机标幺测量关联的物理信号向量端口。向量元素为：

- *pu\_torque*
- *pu\_velocity*
- *pu\_vds*
- *pu\_vqs*
- *pu\_v0s*
- *pu\_ids*
- *pu\_iqs*
- *pu\_i0s*

### 守恒

### **R** — 电机转子（机械）

与电机转子关联的机械旋转守恒端口。

### **C** — 电机机壳（机械）

与电机机壳关联的机械旋转守恒端口。

### **~1** — 定子正端连接（电气）

与定子正端连接关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **~2** — 定子负端连接（电气）

与定子负端连接关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a1** — *a* 正端连接（电气）

与 *a* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b1** — *b* 正端连接（电气）

与 *b* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c1** — *c* 正端连接（电气）

与 *c* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **a2** — *a* 负端连接（电气）

与 *a* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b2** — *b* 负端连接（电气）

与 *b* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c2** — *c* 负端连接（电气）

与 *c* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **HA** — *a* 相端子热端口（热）

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口（热）

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口（热）

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HR** — 转子热端口（热）

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

所有默认参数值均基于电机三角形绕组配置。

### **建模选项** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口，并对产生的热量和电机温度的影响进行建模。

### 主

### **电气连接** — 电气连接 `Composite three-phase ports` (默认) | `Expanded three-phase ports`

使用复合三相端口还是扩展三相端口。

### **额定视在功率** — 额定视在功率 `15e3` `V*A` (默认)

感应电机在电气侧的额定视在功率。

### **额定电压** — RMS 电压 `220` `V` (默认)

线间 RMS 电压。

### **额定电气频率** — 标称电气频率 `60` `Hz` (默认)

与额定视在功率对应的标称电气频率。

### **极对数** — 电机极对数 `1` (默认)

电机极对数。

### **参数化单位** — 模块参数化的单位制 `SI` (默认) | `Per unit`

模块参数化的单位制。可在 `SI`（国际单位制）和 `Per unit`（标幺制）之间选择。

#### 依赖关系

选择：

- `SI` 会在 **阻抗** 和 **饱和** 设置中显示 SI 参数。
- `Per unit` 会在 **阻抗** 和 **饱和** 设置中显示标幺参数。

### **鼠笼** — 鼠笼规格选项 `Single squirrel cage` (默认) | `Double squirrel cage`

用于为电机指定单鼠笼或双鼠笼的选项。

将此参数设置为 `Double squirrel cage` 会显示第二个鼠笼的 **阻抗** 参数。

### **零序** — 零序 `Include` (默认) | `Exclude`

零序模型：

- `Include` — 优先考虑模型保真度。如果为使用 Partitioning 求解器的仿真选择 `Include` 以包含零序项，则会发生错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

#### 依赖关系

如果此参数设置为：

- `Include` 且 **参数化单位** 设置为 `SI` — **阻抗** 设置中的 **定子零序电抗, X0** 参数可见。
- `Include` 且 **参数化单位** 设置为 `Per unit` — **阻抗** 设置中的 **定子零序电感, pu\_L0 (pu)** 参数可见。
- `Exclude` — **阻抗** 设置中的定子零序参数不可见。

### **初始化选项** — 初始化方法 `Set targets for flux variables` (默认) | `Set targets for load flow variables`

初始化方法。您可以使用磁链数据或潮流分析数据来初始化电机以进行稳态仿真。

如果选择 `Set targets for load flow variables`，为了完整指定初始条件，必须以高优先级目标值的形式包含初始化约束。例如，如果您的感应电机连接到 Inertia 模块，则在 Inertia 模块的 **初始目标** 部分中，将 **旋转速度** 的 **优先级** 设置为 `High` 时，感应电机的初始条件将被完全指定。或者，您可以将 Inertia 模块 **旋转速度** 的 **优先级** 设置为 `None`，而将感应电机模块 **转差率**、**发出的有功功率** 或 **消耗的机械功率** 的 **优先级** 设置为 `High`。

#### 依赖关系

**初始目标** 部分中可见的变量类型取决于您在 **主** 部分中为 **初始化选项** 参数选择的初始化方法。要使用以下方式指定目标值：

- 磁链变量 — 将 **初始化选项** 参数设置为 `Set targets for flux variables`。
- 潮流分析数据 — 将 **初始化选项** 参数设置为 `Set targets for load flow variables`。

### 阻抗

对于 **主** 设置中的 **参数化单位** 参数，选择 `SI` 以显示 SI 参数，或选择 `Per unit` 以显示标幺参数。

### **定子电阻, Rs** — 定子电阻 `0.25` `Ohm` (默认)

定子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI` 时，此参数才可见。

### **定子漏抗, Xls** — 定子漏抗 `0.4` `Ohm` (默认)

定子漏抗。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI` 时，此参数才可见。

### **折算转子电阻, Rr'** — 折算转子电阻 `0.14` `Ohm` (默认)

折算至定子的转子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **折算转子漏抗, Xlr'** — 折算转子漏抗 `0.41` `Ohm` (默认)

折算至定子的转子漏抗。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **鼠笼 1 中的折算转子电阻, Rr1'** — 第一个鼠笼中的折算转子电阻 `0.28` `Ohm` (默认)

鼠笼 1 中的转子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **鼠笼 1 中的折算转子漏抗, Xlr1'** — 第一个鼠笼中的折算转子漏抗 `0.82` `Ohm` (默认)

鼠笼 1 中的转子漏抗。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **鼠笼 2 中的折算转子电阻, Rr2'** — 第二个鼠笼中的折算转子电阻 `0.28` `Ohm` (默认)

鼠笼 2 中的转子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **鼠笼 2 中的折算转子漏抗, Xlr2'** — 第二个鼠笼中的折算转子漏抗 `0.82` `Ohm` (默认)

鼠笼 2 中的转子漏抗。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **励磁电抗, Xm** — 励磁电抗 `17` `Ohm` (默认)

励磁电抗。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI` 时，此参数才可见。

### **定子零序电抗, X0** — 定子零序电抗 `0.4` `Ohm` (默认)

定子零序电抗。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `SI`，且将 **主** 设置中的 **零序** 参数设置为 `Include` 时，此参数才可见。

### **定子电阻, Rs (pu)** — 标幺定子电阻 `0.0258` (默认)

标幺定子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit` 时，此参数才可见。

### **定子漏电感, Lls (pu)** — 标幺定子漏电感 `0.0413` (默认)

标幺定子漏电感。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit` 时，此参数才可见。

### **折算转子电阻, Rr' (pu)** — 标幺折算转子电阻 `0.0145` (默认)

折算至定子的标幺转子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **折算转子漏电感, Llr' (pu)** — 标幺折算转子漏电感 `0.0424` (默认)

折算至定子的标幺转子漏电感。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Single squirrel cage` 时，此参数才可见。

### **鼠笼 1 中的折算转子电阻, Rr1' (pu)** — 鼠笼 1 中的标幺折算转子电阻 `0.0290` (默认)

鼠笼 1 中的标幺转子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **鼠笼 1 中的折算转子漏电感, Llr1' (pu)** — 标幺折算转子漏电感 `0.0848` (默认)

鼠笼 1 中的标幺转子漏电感。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **鼠笼 2 中的折算转子电阻, Rr2' (pu)** — 鼠笼 2 中的标幺折算转子电阻 `0.0290` (默认)

鼠笼 2 中的标幺转子电阻。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **鼠笼 2 中的折算转子漏电感, Llr2' (pu)** — 标幺折算转子漏电感 `0.0848` (默认)

鼠笼 2 中的标幺转子漏电感。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit`，且将 **主** 设置中的 **鼠笼** 参数设置为 `Double squirrel cage` 时，此参数才可见。

### **励磁电感, Lm (pu)** — 标幺励磁电感 `1.7562` (默认)

标幺励磁电感，即定子-转子互感的峰值。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit` 时，此参数才可见。

### **定子零序电感, L0 (pu)** — 标幺定子零序电感 `0.0413` (默认)

标幺定子零序电感。

#### 依赖关系

仅当将 **主** 设置中的 **参数化单位** 参数设置为 `Per unit`，且将 **主** 设置中的 **零序** 参数设置为 `Include` 时，此参数才可见。

### 饱和

对于 **主** 设置中的 **参数化单位** 参数，选择 `SI` 以显示 SI 参数，或选择 `Per unit` 以显示标幺参数。

饱和特性基于电机连接为三角形绕组配置。

### **磁饱和表示** — 磁饱和表示 `None` (默认) | `Open-circuit lookup table (v versus i)`

模块磁饱和表示。

#### 依赖关系

如果此参数设置为 `Open-circuit lookup table (v versus i)`，则相关参数可见。

### **空载线电流饱和数据, i (rms)** — 空载线 RMS 电流饱和数据 `[0, 4, 9, 18, 25, 34, 50, 68, 95, 120]` `A` (默认)

电流 *i* 数据填充电压 *v* 对励磁电流 *i* 的查找表。此参数必须包含至少 10 个元素的向量。

#### 依赖关系

仅当 **磁饱和表示** 参数设置为 `Open-circuit lookup table (v versus i)`，且在 **主** 设置中将 **参数化单位** 参数设置为 `SI` 时，此参数才可见。

### **端子电压饱和数据, v (phase-phase, rms)** — 端子 RMS 电压饱和数据 `[0, 88, 154, 198, 220, 242, 264, 286, 308, 327]` `V` (默认)

端子电压 *v* 数据填充电压 *v* 对电流 *i* 的查找表。此参数必须包含至少 10 个元素的向量。元素数量必须与 **空载线电流饱和数据, i (rms)** 参数的向量元素数量匹配。

#### 依赖项

仅当 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table (v versus i)`，并且在 **Main** 设置中 **Parameterization unit** 参数设置为 `SI` 时，此参数才可见。

### **Per-unit no-load line current saturation data, i** — 标幺值空载线电流饱和数据 `[0, .176, .396, .792, 1.1, 1.496, 2.2, 2.992, 4.18, 5.28]`（默认）

电流 *i* 数据填充电压 *v* 对励磁电流 *i* 查找表。此参数必须包含至少 10 个元素的向量。

#### 依赖项

仅当 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table (v versus i)`，并且在 **Main** 设置中 **Parameterization unit** 参数设置为 `Per unit` 时，此参数才可见。

### **Per-unit terminal voltage saturation data, v** — 标幺值端电压饱和数据 `[0, .4, .7, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.4864]`（默认）

端电压 *v* 数据填充电压 *v* 对电流 *i* 查找表。此参数必须包含至少 10 个元素的向量。元素数量必须与 **Per-unit no-load line current saturation data, i** 参数向量的元素数量匹配。

#### 依赖项

仅当 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table (v versus i)`，并且在 **Main** 设置中 **Parameterization unit** 参数设置为 `Per unit` 时，此参数才可见。

### 热

这些参数仅对具有暴露热端口的模块出现。

### **Measurement temperature** — 额定温度 `298.15` `K`（默认）| 实标量

电机参数所对应的温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Cage resistance temperature coefficient** — 转子温度系数 `4.4e-3`（默认）| `1/K` | 标量

转子笼型电阻与温度相关的系数。默认值 `4.4e-3` 1/K 适用于铝。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

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

从 R2021b 开始，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。此外，`Composite three-phase ports` 和 `Expanded three-phase ports` 的 simlog 格式相同。

由于这些更改，在早期版本保存的模型中，请检查此模块的 **Electrical connection** 参数。

### R2020a：饱和特性更新

从 R2020a 开始，对于饱和特性，Induction Machine Squirrel Cage 模块会考虑由漏电感引起的磁通。

以下参数的默认值已更改：

- **Stator leakage reactance, Xls**
- **Stator zero-sequence reactance, X0**
- **Stator leakage inductance, Lls (pu)**
- **Stator zero-sequence inductance, L0 (pu)**
- **Terminal voltage saturation data, v (phase-phase, rms)**
- **Per-unit terminal voltage saturation data, v**

由于这些更改，在早期版本保存的模型中，如果使用启用了饱和的 Induction Machine Squirrel Cage 模块，请检查饱和数据。

## 描述

具有标幺值或 SI 参数化的鼠笼式转子感应电机

Induction Machine Squirrel Cage 模块对具有以标幺值或国际单位制 (SI) 表示的基本参数的鼠笼式转子感应电机进行建模。鼠笼式转子感应电机是一种感应电机。所有定子连接均可在模块上访问。因此，您可以使用星形和三角形配置之间的切换来对软启动工况进行建模。如果需要访问转子绕组，请改用 Induction Machine Wound Rotor 模块。

将端口 **~1** 连接到三相电路。要将定子连接为三角形配置，请在端口 **~1** 和 **~2** 之间连接一个 Phase Permute 模块。要将定子连接为星形配置，请将端口 **~2** 连接到 Grounded Neutral (Three-Phase) 或 Floating Neutral (Three-Phase) 模块。

### 使用潮流目标值进行感应电机初始化

如果该模块位于与频率-时间仿真模式兼容的网络中，则可以在网络上执行潮流分析。潮流分析提供稳态值，您可以使用这些值来初始化电机。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。有关展示如何使用潮流分析数据初始化感应电机的示例，请参阅 Induction Motor Initialization with Loadflow。

### 方程

对于 SI 实现，模块将您输入的 SI 值转换为标幺值以进行仿真。转换后的值基于电机以三角形绕组配置连接。

对于标幺值实现，必须在阻抗选项卡中基于电机以三角形绕组配置连接来指定电阻和电感。

有关 SI 和标幺值电机参数之间关系的信息，请参阅 Per-Unit Conversion for Machine Parameters。有关标幺值参数化的信息，请参阅 Per-Unit System of Units。

感应电机方程相对于同步参考坐标系表示，其定义为

θe(t)=∫0t2πfrateddt,

其中 *frated* 是 **Rated electrical frequency** 参数的值。

Park 变换将定子方程映射到相对于额定电频率静止的参考坐标系。Park 变换定义为

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212],

其中 *θe* 是电角度。

Park 变换用于定义标幺值感应电机方程。定子电压方程定义为

vds=1ωbasedψdsdt−ωψqs+Rsids,

vqs=1ωbasedψqsdt+ωψds+Rsiqs,

以及

v0s=1ωbasedψ0sdt+Rsi0s,

其中：

- *vds*、*vqs* 和 *v0s* 是由下式定义的 *d* 轴、*q* 轴和零序定子电压：

  [vdsvqsv0s]=Ps[vavbvc].

  *va*、*vb* 和 *vc* 是端口 **~1** 和 **~2** 两端的定子电压。
- *ωbase* 是标幺值基准电速度。
- *ψds*、*ψqs* 和 *ψ0s* 是 *d* 轴、*q* 轴和零序定子磁链。
- *Rs* 是定子电阻。
- *ids*、*iqs* 和 *i0s* 是由下式定义的 *d* 轴、*q* 轴和零序定子电流：

  [idsiqsi0s]=Ps[iaibic].

  *ia*、*ib* 和 *ic* 是从端口 **~1** 流向端口 **~2** 的定子电流。

转子电压方程定义为

vdr=1ωbasedψdrdt−(ω−ωr)ψqr+Rrdidr=0

以及

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

以及

ψ0s=Lssi0s,

其中 *Lss* 是定子自感，*Lm* 是励磁电感。

转子磁链方程定义为

ψdr=Lrrdidr+Lmids

以及

ψqr=Lrrdiqr+Lmiqs,

其中 *Lrrd* 是折算到定子的转子自感。

转子转矩定义为

T=ψdsiqs−ψqsids.

定子自感 *Lss*、定子漏电感 *Lls* 和励磁电感 *Lm* 的关系为

Lss=Lls+Lm.

转子自感 *Lrrd*、转子漏电感 *Llrd* 和励磁电感 *Lm* 的关系为

Lrrd=Llrd+Lm.

当提供饱和曲线时，用于确定饱和励磁电感作为励磁磁通函数的方程为：

Lm\_sat=f(ψm)

ψm=ψdm2+ψqm2

对于无饱和，方程简化为

Lm\_sat=Lm

### 绘图和显示选项

您可以使用模块上下文菜单上的 **Electrical** 菜单执行绘图和显示操作。

右键单击该模块，然后从 **Electrical** 菜单中选择一个选项：

- **Display Base Values** — 在 MATLAB® Command Window 中显示电机的标幺值基准值。
- **Plot Torque Speed (SI)** — 使用当前电机参数，在 MATLAB 图形窗口中绘制转矩与转速的关系，二者均以 SI 单位测量。
- **Plot Torque Speed (pu)** — 使用当前电机参数，在 MATLAB 图形窗口中绘制转矩与转速的关系，二者均以标幺值测量。
- **Plot Open-Circuit Saturation** — 在 MATLAB 图形窗口中绘制端电压与空载线电流的关系，二者均以标幺值表示。该图包含三条迹线：

  - 未饱和 — 定子励磁电感（未饱和）。
  - 饱和 — 您指定的开路查找表（*v* 对 *i*）。
  - 派生 — 从您指定的标幺值开路查找表（*v* 对 *i*）派生的开路查找表。此数据用于计算饱和励磁电感 *Lm\_sat* 和饱和因子 *Ks* 与磁链 *ψm* 的特性关系。
- **Plot Saturation Factor** — 使用电机参数，在 MATLAB 图形窗口中绘制饱和因子 *Ks* 与磁链 *ψm* 的关系。此参数由您指定的其他参数派生：

  - 空载线电流饱和数据 *i*
  - 端电压饱和数据 *v*
  - 漏电感 *Lls*
- **Plot Saturated Inductance** — 使用电机参数，在 MATLAB 图形窗口中绘制励磁电感 *Lm\_sat* 与磁链 *ψm* 的关系。此参数由您指定的其他参数派生：

  - 空载线电流饱和数据 *i*
  - 端电压饱和数据 *v*
  - 漏电感 *Lls*

对于 SI 实现，*v* 以 V（相间 RMS）为单位，*i* 以 A（rms）为单位。

### 对热效应建模

您可以暴露热端口，以模拟生成的热量和电机温度的影响。要暴露热端口和 **Thermal** 参数，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块包含与定子绕组关联的电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子绕组关联的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在致动器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

在 **Initial Targets** 部分中可见的变量类型取决于您在 **Main** 部分中为 **Initialization option** 参数选择的初始化方法。要使用以下方式指定目标值：

- 磁通变量 — 将 **Initialization option** 参数设置为 `Set targets for flux variables`。
- 来自潮流分析的数据 — 将 **Initialization option** 参数设置为 `Set targets for load flow variables`。

如果选择 `Set targets for load flow variables`，为完全指定初始条件，必须以高优先级目标值的形式包含初始化约束。例如，如果您的感应电机连接到 Inertia 模块，则在 Inertia 模块的 **Initial Targets** 部分中，将 **Rotational velocity** 的 **Priority** 设置为 `High` 时，感应电机的初始条件即完全指定。或者，您可以将 Inertia 模块 **Rotational velocity** 的 **Priority** 设置为 `None`，而将感应电机模块 **Slip**、**Real power generated** 或 **Mechanical power consumed** 的 **Priority** 设置为 `High`。
