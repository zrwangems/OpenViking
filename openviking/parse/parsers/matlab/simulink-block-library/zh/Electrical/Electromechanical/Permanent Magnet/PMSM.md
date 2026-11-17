---
type: simulink-block
title: 'PMSM'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmsm'
documentation_source_path: 'ref/pmsm.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM

## 端口

### 守恒

### **~** — 三相端口电气

可扩展三相端口。有关详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **~1** — 定子正端连接电气

*自 R2024a 起*

与定子正端连接相关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **~2** — 定子负端连接电气

*自 R2024a 起*

与定子负端连接相关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **n** — 中性相电气

与中性相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding Type** 设置为 `Wye-wound`，并将 **Zero sequence** 设置为 `Include`。

### **R** — 电机转子机械

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳机械

与电机机壳相关联的机械旋转守恒端口。

### **HA** — 绕组 A 热端口热

与绕组 A 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热端口热

与绕组 B 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — 绕组 C 热端口热

与绕组 C 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Selected part** — 预定义参数化选项 `<click to select>` (默认)

用于将模块参数化以表示特定供应商组件的选项。点击 **<click to select>** 超链接打开模块参数化管理器窗口。有关模块参数化管理器的详细信息，请参阅加载预定义参数化。

### **Modeling option** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports` (默认) | `Expanded three-phase ports`

是使用复合三相端口还是扩展三相端口。

### **Winding type** — 绕组配置 `Wye-wound` (默认) | `Delta-wound` | `Open-end`

选择绕组配置：

- `Wye-wound` — 绕组为星形绕组。
- `Delta-wound` — 绕组为三角形绕组。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组采用开口端配置。模块将绕组的每一端暴露为电气连接。

### **Modeling fidelity** — 建模保真度 `Constant Ld, Lq and PM` (默认) | `Tabulated Ld, Lq and PM`

选择建模保真度：

- `Constant Ld, Lq and PM` — *Ld*、*Lq* 和 *PM* 值为常量，并由各自参数定义。
- `Tabulated Ld, Lq and PM` — *Ld*、*Lq* 和 *PM* 值根据 DQ 电流查找表在线计算，如下所示：

  Ld=f1(id,iq)

  Ld=f2(id,iq)

  λPM=f2(id,iq)

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。

### **Number of pole pairs** — 极对数 `6` (默认)

转子上的永磁体极对数。

### **Permanent magnet flux linkage parameterization** — 永磁体磁链参数化 `Specify flux linkage` (默认) | `Specify torque constant` | `Specify back EMF constant`

选择 `Specify flux linkage`、`Specify torque constant` 或 `Specify back EMF constant`。

### **Permanent magnet flux linkage** — 永磁体磁链 `0.03` `Wb` (默认)

与任一定子绕组交链的峰值永磁体磁链。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify flux linkage`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Torque constant** — 转矩常数 `0.18` `N*m/A` (默认)

任一定子绕组的转矩常数。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify torque constant`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Back EMF constant** — 反电动势常数 `0.18` `V*s/rad` (默认)

任一定子绕组的反电动势常数。

**注意**

反电动势常数是永磁体在每相每单位转速下感应出的峰值电压。对于星形绕组电机，该电压为线对中性点电压。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify back EMF constant`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Stator parameterization** — 定子参数化 `Specify Ld, Lq, and L0` (默认) | `Specify Ls, Lm, and Ms`

选择 `Specify Ld, Lq, and L0` 或 `Specify Ls, Lm, and Ms`。

### **Stator d-axis inductance, Ld** — 定子 d 轴电感 `0.00022` `H` (默认)

D 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Stator q-axis inductance, Lq** — 定子 q 轴电感 `0.00022` `H` (默认)

Q 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A` (默认)

直轴电流向量，iD。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A` (默认)

交轴电流向量，iQ。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Ld matrix, Ld(id,iq)** — Ld 矩阵 `0.0002 * ones(3, 3)` `H` (默认)

Ld 矩阵。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Lq matrix, Lq(id,iq)** — Lq 矩阵 `0.0002 * ones(3, 3)` `H` (默认)

Lq 矩阵。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Permanent magnet flux linkage, PM(id,iq)** — 永磁体磁链 `0.1 * ones(3, 3)` `Wb` (默认)

永磁体磁链。

#### 依赖关系

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld, Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq and PM`
- **Permanent magnet flux linkage parameterization** 为 `Specify flux linkage`

### **Torque constant matrix, kt(id,iq)** — 力常数矩阵 `0.18 * ones(3, 3)` `N*m/A` (默认)

转矩常数矩阵。

#### 依赖关系

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld, Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq and PM`
- **Permanent magnet flux linkage parameterization** 为 `Specify torque constant`

### **Back EMF constant matrix, ke(id,iq)** — 永磁体磁链 `0.18 * ones(3, 3)` `V/(rad/s)` (默认)

反电动势常数矩阵。

#### 依赖关系

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld, Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq and PM`
- **Permanent magnet flux linkage parameterization** 为 `Specify back EMF constant`

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H` (默认)

零序电感。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Winding Type** 设置为 `Wye-wound`，将 **Zero sequence** 设置为 `Include`，并将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。
- 将 **Winding Type** 设置为 `Delta-wound`，并将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。

### **Stator self-inductance per phase, Ls** — 每相定子自感 `0.0002` `H` (默认)

三个定子绕组中每个绕组的平均自感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator inductance fluctuation, Lm** — 定子电感波动 `-0.0002` `H` (默认)

定子绕组的自感和互感随转子角度波动的量。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator mutual inductance, Ms** — 定子互感 `0.00002` `H` (默认)

定子绕组之间的平均互感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm` (默认)

每个定子绕组的电阻。

### **Zero sequence** — 零序选项 `Include` (默认) | `Exclude`

包含或排除零序项的选项。

- `Include` — 包含零序项。为优先考虑模型保真度，请使用此默认设置。使用此选项：

  - 对于使用 Partitioning 求解器的仿真会导致错误。有关详细信息，请参阅使用 Partitioning 求解器提高仿真速度。
  - 显示 **Stator zero-sequence inductance, L0** 参数。
- `Exclude` — 排除零序项。为优先考虑桌面仿真或实时部署的仿真速度，请选择此选项。

#### 依赖关系

要启用此参数，请将 **Winding Type** 设置为 `Wye-wound`。

### **Rotor angle definition** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis` (默认) | `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。电机结构部分中的图显示了默认值 `Angle between the a-phase magnetic axis and the d-axis`。选择此值时，当转子角度为零时，转子和 *a* 相磁通对齐。

当选择 `Angle between the a-phase magnetic axis and the q-axis` 时，当转子角度为零时，*a* 相电流产生最大转矩。

### 铁耗

### **Model** — 启用铁耗计算 `None` (默认) | `Empirical`

指定铁耗计算模型。

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 开路铁耗 `[0, 0, 0]` `W` (默认)

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses determined** 指定的频率下由磁滞、涡流和附加损耗引起的开路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 短路铁耗 `[0, 0, 0]` `W` (默认)

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses determined** 指定的频率下由磁滞、涡流和附加损耗引起的短路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### **Electrical frequency at which losses determined** — 确定损耗时的电气频率 `60` `Hz` (默认)

模块测量开路和短路铁耗时的电气频率。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### **Short-circuit RMS current for short-circuit iron losses** — 用于短路铁耗的短路 RMS 电流 `95` `A` (默认)

测量短路损耗时产生的短路 RMS 相电流。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2` (默认) | nonnegative scalar

连接到机械平移端口 **R** 的转子惯量。该值可以为零。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)` (默认) | nonnegative scalar

旋转阻尼。

### 温度相关性

### **Measurement temperature** — 模块引用电机参数时的温度 `298.15` `K` (默认)

模块引用电机参数时的温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **电阻温度系数** — 电阻温度系数 `3.93e-3` `1/K`（默认）

将电阻与温度相关联的方程中的系数 α。有关详细信息，请参阅 Thermal Model for Actuator Blocks。默认值适用于铜。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Show thermal port`。

### **永磁体磁通温度系数** — 永磁体磁通密度随温度变化的比例速率 `-0.001` `1/K`（默认） | scalar

永磁体磁通密度随温度变化的比例速率。使用此参数可在温度升高时线性降低转矩和感应反电动势。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Show thermal port`。

### 热端口

### **每个定子绕组的热质量** — 每个定子绕组的热质量 `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Show thermal port`。

### **转子热质量** — 转子热质量 `200` `J/K`（默认）

转子的热质量，即，将转子温度升高一度所需的能量。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Show thermal port`。

### **与转子相关的主磁通路径铁损百分比** — 与转子相关的主磁通路径铁损百分比 `90`（默认）

与通过转子的磁路相关的主磁通路径铁损百分比。它确定有多少铁损发热归属于转子热端口 **HR**，以及有多少归属于三个绕组热端口 **HA**、**HB** 和 **HC**。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Show thermal port`，并在 **铁损** 选项卡中，将 **模型** 设置为 `Empirical`。

### **与转子相关的跨齿磁通路径铁损百分比** — 与转子相关的跨齿磁通路径铁损百分比 `30`（默认）

与通过转子的磁路相关的跨齿磁通路径铁损百分比。它确定有多少铁损发热归属于转子热端口 **HR**，以及有多少归属于三个绕组热端口 **HA**、**HB** 和 **HC**。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Show thermal port`，并在 **铁损** 选项卡中，将 **模型** 设置为 `Empirical`。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024a：定子绕组的 Open-end 配置

要对 open-end 配置中的电机定子绕组建模，请将 **绕组类型** 参数设置为 `Open-end`。然后，PMSM 模块通过启用相应的电气守恒端口来暴露绕组的每一端。

### R2021b：电气连接端口更新

从 R2021b 开始，要在 composite 和 expanded 端口之间切换，请将 **电气连接** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **电气连接** 参数。

## 描述

正弦磁通分布的永磁同步电机

PMSM 模块对具有三相 wye-wound、delta-wound 或 open-ended 定子的永磁同步电机（PMSM）建模。使用此模块对内置式永磁同步电机（IPMSM）、表面式永磁同步电机（SPMSM）、横向磁通电机、轴向磁通（盘式）电机或 PMSM 伺服电机建模。

PMSM 具有永磁转子和绕线定子。这些电机可用于电动汽车（EV）等牵引应用以及执行系统中。在执行系统中，PMSM 也称为*无刷伺服电机*。与具有梯形反电动势分布的无刷直流（BLDC）电机相比，PMSM 通常具有正弦反电动势分布，以减少不期望的高频机械和电流谐波。

PMSM 模块使用固定的 *d* 轴和 *q* 轴电感 *Ld* 和 *Lq* 对电机建模。您可以使用此模块对两种主要类型的 PMSM 建模：

- SPMSM 或表面式永磁（SPM）电机 — 转子磁体表面安装。*Ld* 和 *Lq* 相等。
- IPMSM 或内置式永磁（IPM）电机 — 转子磁体位于转子内部。*Ld* 和 *Lq* 不相等。

还可以根据主磁通路径对 PMSM 分类。主磁通路径通常是径向的，但也可以是轴向的，对于相同物理尺寸的电机，轴向磁通会产生高得多的转矩。您可以使用 PMSM 模块对径向和轴向磁通 PMSM 建模。

您可以使用 **绕组类型** 参数指定绕组的配置。此图显示了 wye-wound 定子的等效电路。

您还可以通过分别将 **绕组类型** 设置为 `Delta-wound` 或 `Open-end` 来对 delta-wound 或 open-end 定子建模。

您可以为该模块选择不同的内置参数化。有关详细信息，请参阅“预定义参数化”部分。

**注意**

Simscape™ Electrical™ 包含多个可对同一类型电机或执行器建模的模块。请选择具有足够建模细节的模块，以满足您需要回答的工程设计问题。不要使用建模细节超过所需的模块，因为高保真模型会减慢仿真速度，并且参数化更复杂。

像 PMSM 模块这样的模块使用简单等效电路对具有固定或参数相关系数的电机建模。这些模型具有中等保真度。使用此模块可在机器人技术和机电一体化等执行应用中设计控制或系统，并在饱和与谐波对损耗影响较弱时进行效率预测。有关选择正确模块以适当保真度对电机建模的详细信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 电机结构

此图显示了转子上具有单个极对的电机结构。

永磁体生成转子磁场，该磁场根据转子角度产生正弦磁通变化率。

对于轴约定，当您将 **转子角度定义** 参数设置为 `Angle between the a-phase magnetic axis and the d-axis` 时，当转子机械角度 *θr* 为零时，*a* 相磁通与永磁体磁通对齐。当您将 **转子角度定义** 参数设置为 `Angle between the a-phase magnetic axis and the q-axis` 时，转子机械角度是 *a* 相磁轴与转子 *q* 轴之间的角度。

### 方程

定子绕组两端的电压为

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

其中：

- *va*、*vb* 和 *vc* 是定子绕组各相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、*ib* 和 *ic* 是流过定子绕组的电流。
- dψadt,dψbdt, and dψcdt 是每个定子绕组中磁通的变化率。

永磁体和三个绕组对连接每个绕组的总磁通有贡献。总磁通为

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm],

其中：

- *ψa*、*ψb* 和 *ψc* 是连接每个定子绕组的总磁通。
- *Laa*、*Lbb* 和 *Lcc* 是定子绕组的自感。
- *Lab*、*Lac*、*Lba* 等是定子绕组的互感。
- *ψam*、*ψbm* 和 *ψcm* 是连接定子绕组的永磁体磁通。

定子绕组中的电感是转子电角度的函数，定义如下

θe=Nθr+rotor offset

Laa=Ls+Lmcos(2θe)

Lbb=Ls+Lmcos(2(θe−2π/3))

Lcc=Ls+Lmcos(2(θe+2π/3))

Lab=Lba=−Ms−Lmcos(2(θe+π/6))

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3))

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3))

其中：

- *θr* 是转子机械角度。
- *θe* 是转子电角度。
- *rotor offset* 为 `0`（如果您相对于 *d* 轴定义转子电角度），或 `-pi/2`（如果您相对于 *q* 轴定义转子电角度）。
- *Ls* 是每相定子自感。此值是每个定子绕组的平均自感。
- *Lm* 是定子电感波动。此值是自感和互感随转子角度变化而波动的量。
- *Ms* 是定子互感。此值是定子绕组之间的平均互感。

当 *θe* = 0° 时，连接绕组 *a* 的永磁体磁通最大；当 *θe* = 90° 时为零。因此，连接的电机磁通定义为：

[ψamψbmψcm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)]

其中 *ψm* 是永磁体磁链。

### 简化电气方程

将 Park 变换应用于模块电气方程，可得到与转子角度无关的转矩表达式。

Park 变换定义为：

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]

其中 *θe* 是定义为 *Nθr* 的电角度。*N* 是极对数。

对定子绕组电压和电流使用 Park 变换，将其变换到 dq0 坐标系，该坐标系与转子角度无关：

[vdvqv0]=P[vavbvc]

[idiqi0]=P[iaibic]

将 Park 变换应用于前两个电气方程，可得到定义模块行为的以下方程：

vd=Rsid+Lddiddt−NωiqLq

vq=Rsiq+Lqdiqdt+Nω(idLd+ψm)

v0=Rsi0+L0di0dt

T=32N(iq(idLd+ψm)−idiqLq)

其中：

- *Ld* = *Ls* + *Ms* + 3/2 *Lm*。*Ld* 是定子 *d* 轴电感。
- *Lq* = *Ls* + *Ms* − 3/2 *Lm*。*Lq* 是定子 *q* 轴电感。
- *L0* = *Ls* – 2*Ms*。*L0* 是定子零序电感。
- *ω* 是转子机械转速。
- *N* 是转子永磁体极对数。
- *T* 是转子转矩。转矩从电机壳体（模块物理端口 **C**）流向电机转子（模块物理端口 **R**）。

PMSM 模块使用 Park 变换的原始非正交实现。如果尝试应用替代实现，dq0 电压和电流会得到不同结果。

### 替代磁链参数化

您可以使用 **永磁体磁链** 参数，通过电机数据表中更常见的反电动势或转矩常数来对电机进行参数化。

反电动势常数是永磁体在每相单位转速下感应的峰值电压。峰值永磁体磁链与反电动势之间的关系为：

ke=Nψm.

一相的反电动势 *eph* 为：

eph=keω.

转矩常数是每相单位电流感应的峰值转矩。当二者均以 SI 单位表示时，其数值与反电动势常数相同：

kt=Nψm.

当 *Ld*=*Lq* 且所有三相电流平衡时，合成转矩 *T* 为：

T=32ktiq=32ktIpk,

其中 *Ipk* 是三个绕组中任一绕组的峰值电流。

因子 3/2 来自这是所有相转矩的稳态总和。因此，转矩常数 *kt* 也可以为：

kt=23(TIpk),

其中 *T* 是使用峰值线电压 *Ipk* 的平衡三相电流测试时测得的总转矩。RMS 线电流为：

kt=23Tiline,rms.

### 计算铁损

铁损分为两项，一项表示主磁化路径，另一项表示在弱磁运行期间变得活跃的跨齿尖路径。铁损模型基于 [3]。

表示主磁化路径的项取决于感应的 RMS 线对中性点定子电压 Vmrms：

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

这是空载运行期间的主导项。*k* 是将 RMS 伏特每 Hz 关联起来的反电动势常数。其定义为 k=Vmrms/f，其中 *f* 是电频率。右侧第一项是磁滞损耗，第二项是涡流损耗，第三项是附加损耗。分子中出现的三个系数源自您为开路磁滞、涡流和附加损耗提供的值。

表示跨齿尖路径的项在建立去磁磁场时变得重要，可通过有限元分析短路测试确定。它取决于与跨齿尖磁通相关的 RMS EMF，Vdrms\*：

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

三个分子项源自您为短路磁滞、涡流和附加损耗提供的值。

### 预定义参数化

PMSM 模块有多个可用的内置参数化。

此预参数化数据允许您设置模块以表示特定供应商的组件。这些永磁同步电机的参数化与制造商数据表匹配。要加载预定义参数化，请双击 PMSM 模块，点击 **选定部件** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用数据源获取参数值。使用工程判断和简化假设来填补缺失数据。因此，预计仿真行为与实际物理行为之间存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预参数化的更多信息以及可用组件列表，请参阅 List of Pre-Parameterized Components。

### 建模热效应

您可以公开热端口，以对将功率转换为热量的损耗效应建模。要公开热端口，请将 **建模选项** 参数设置为以下任一项：

- `No thermal port` — 模块包含与定子绕组关联的 expanded 电气守恒端口，但不包含热端口。
- `Show thermal port` — 模块包含与定子绕组关联的 expanded 电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
