---
type: simulink-block
title: 'BLDC'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Permanent Magnet'
documentation_page: 'bldc'
documentation_source_path: 'ref/bldc.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC

## 端口

### 守恒

### **~** — 三相端口电气

可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **a** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **b** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **c** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **~1** — 定子正端连接电气

*自 R2024a 起*

与定子正端连接相关的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **~2** — 定子负端连接电气

*自 R2024a 起*

与定子负端连接相关的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 正端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 正端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 正端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 负端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 负端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 负端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **n** — 中性相电气

与中性相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **绕组类型** 设置为 `Wye-wound`，并将 **零序** 设置为 `Include`。

### **R** — 电机转子机械

与电机转子相关的机械旋转守恒端口。

### **C** — 电机壳体机械

与电机壳体相关的机械旋转守恒端口。

### **HA** — 绕组 A 热端口热

与绕组 A 相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热端口热

与绕组 B 相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HC** — 绕组 C 热端口热

与绕组 C 相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **选定部件** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商提供的组件的选项。单击 **<click to select>** 超链接以打开“模块参数化管理器”窗口。有关模块参数化管理器的详细信息，请参阅加载预定义参数化。

### **建模选项** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### 转子

### **电气连接** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

使用复合三相端口还是扩展三相端口。

### **反电动势曲线** — 反电动势曲线 `Perfect trapezoid - specify maximum flux linkage`（默认）| `Perfect trapezoid - specify maximum rotor-induced back emf` | `Tabulated - specify flux partial derivative with respect to rotor angle` | `Tabulated - specify rotor-induced back emf as a function of rotor angle`

用于定义永磁体磁链分布随转子角度变化的参数化。选择：

- `Perfect trapezoid - specify maximum flux linkage` 用于指定永磁体的最大磁链以及反电动势恒定的转子角度。该模块假设反电动势为完美梯形。
- `Perfect trapezoid - specify maximum rotor-induced back emf` 用于指定最大转子感应反电动势及相应的转子速度。该模块假设反电动势为完美梯形。
- `Tabulated - specify flux partial derivative with respect to rotor angle` 用于指定磁链偏导数的值及相应的转子角度。
- `Tabulated - specify rotor-induced back emf as a function of rotor angle` 用于指定测得的反电动势常数及相应的转子速度和角度。

### **最大永磁体磁链** — 最大永磁体磁链 `0.03` `Wb`（默认）

与任何定子绕组交链的峰值永磁体磁链。

#### 依赖关系

要启用此参数，请将 **反电动势曲线** 设置为 `Perfect trapezoid - specify maximum flux linkage`。

### **反电动势恒定的转子角度** — 反电动势恒定的转子角度 `pi / 12` `rad`（默认）

与定子绕组交链的永磁体磁链保持恒定的转子角度范围。该角度是显示梯形磁链变化率的图中的 θF。

#### 依赖关系

要启用此参数，请将 **反电动势曲线** 设置为 `Perfect trapezoid - specify maximum flux linkage` 或 `Perfect trapezoid - specify maximum rotor-induced back emf`。

### **最大转子感应反电动势** — 最大转子感应反电动势 `9.6` `V`（默认）

进入定子绕组的峰值转子感应反电动势。

#### 依赖关系

要启用此参数，请将 **反电动势曲线** 设置为 `Perfect trapezoid - specify maximum rotor-induced back emf`。

### **转子感应反电动势** — 转子感应反电动势 `[0, -9.6, -9.6, 9.6, 9.6, 0]` `V`（默认）

转子感应反电动势随转子角度变化的值的向量。第一个和最后一个值必须相同，并且通常均为零。有关详细信息，请参阅 **对应的转子角度** 参数。第一个和最后一个值相同，因为磁链以 2π/N 为周期循环，其中 N 是永磁体极对数。

#### 依赖关系

要启用此参数，请将 **反电动势曲线** 设置为 `Tabulated - specify rotor-induced back emf as a function of rotor angle`。

### **磁链对转子角度的偏导数** — 磁链对转子角度的偏导数 `[0, -.1528, -.1528, .1528, .1528, 0]` `Wb/rad`（默认）

磁链（其中磁链是磁通乘以绕组匝数）对转子角度的偏导数的值的向量。第一个和最后一个值必须相同，并且通常均为零。有关详细信息，请参阅 **对应的转子角度** 参数。第一个和最后一个值相同，因为磁链以 2π/N 为周期循环，其中 *N* 是永磁体极对数。

### **对应的转子角度** — 对应的转子角度 `[0, 7.5, 22.5, 37.5, 52.5, 60]` `deg`（默认）

定义磁链偏导数或转子感应反电动势所在的转子角度向量。转子角度定义为 *a* 相磁轴与 *d* 轴之间的角度。也就是说，当角度为零时，由转子和 *a* 相绕组产生的磁场对齐。无论模块的转子角度定义设置如何，都使用此定义。第一个值为零，最后一个值为 2π/N，其中 *N* 是永磁体极对数。

#### 依赖关系

要启用此参数，请将 **反电动势曲线** 设置为 `Tabulated - specify flux partial derivative with respect to rotor angle` 或 `Tabulated - specify rotor-induced back emf as a function of rotor angle`。

### **用于反电动势测量的转子速度** — 用于反电动势测量的转子速度 `600` `rpm`（默认）

指定对应于最大转子感应反电动势的转子速度。

#### 依赖关系

要启用此参数，请将 **反电动势曲线** 设置为 `Perfect trapezoid - specify maximum rotor-induced back emf` 或 `Tabulated - specify rotor-induced back emf as a function of rotor angle`。

### **极对数** — 极对数 `6`（默认）

转子上的永磁体极对数。

### **转子角度定义** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。默认值为 `Angle between the a-phase magnetic axis and the d-axis`。此定义显示在电机结构图中。选择此值时，当转子角度为零时，转子和 *a* 相磁链对齐。

此参数可选择的另一个值是 `Angle between the a-phase magnetic axis and the q-axis`。选择此值时，当转子角度为零时，*a* 相电流产生最大转矩。

### 定子

### **绕组类型** — 绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择绕组配置：

- `Wye-wound` — 绕组为星形连接。
- `Delta-wound` — 绕组为三角形连接。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组采用开路端配置。模块将绕组的每一端都作为电气连接暴露出来。

### **建模保真度** — 建模保真度 `Constant Ld and Lq`（默认）| `Tabulated Ld and Lq`

选择建模保真度：

- `Constant Ld and Lq` — *Ld* 和 *Lq* 值为常数，并由它们各自的参数定义。
- `Tabulated Ld and Lq` — *Ld* 和 *Lq* 值根据 DQ 电流查找表在线计算，如下所示：

  Ld=f1(id,iq)

  Ld=f2(id,iq)

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`。

### **定子参数化** — 定子参数化 `Specify Ld, Lq, and L0`（默认）| `Specify Ls, Lm, and Ms`

选择 `Specify Ld, Lq, and L0` 或 `Specify Ls, Lm, and Ms`。

### **定子 d 轴电感，Ld** — 定子 d 轴电感 `0.00022` `H`（默认）

d 轴电感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Constant Ld and Lq`。

### **定子 q 轴电感，Lq** — 定子 q 轴电感 `0.00022` `H`（默认）

q 轴电感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Constant Ld and Lq`。

### **直轴电流向量，iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

直轴电流向量，iD。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld and Lq`。

### **交轴电流向量，iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

交轴电流向量，iQ。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld and Lq`。

### **Ld 矩阵，Ld(id,iq)** — Ld 矩阵 `0.00022 * ones(3, 3)` `H`（默认）

Ld 矩阵。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld and Lq`。

### **Lq 矩阵，Lq(id,iq)** — Lq 矩阵 `0.00022 * ones(3, 3)` `H`（默认）

Lq 矩阵。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld and Lq`。

### **定子零序电感，L0** — 定子零序电感 `0.00016` `H`（默认）

零序电感。

#### 依赖关系

要启用此参数，需满足以下任一条件：

- 将 **绕组类型** 设置为 `Wye-wound`，将 **零序** 设置为 `Include`，并将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`。
- 将 **绕组类型** 设置为 `Delta-wound`，并将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`。

### **每相定子自感，Ls** — 每相定子自感 `0.0002` `H`（默认）

三个定子绕组中每个绕组的平均自感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ls, Lm, and Ms`。

### **定子电感波动，Lm** — 定子电感波动 `0` `H`（默认）

定子绕组的自感和互感随转子角度的波动。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ls, Lm, and Ms`。

### **定子互感，Ms** — 定子互感 `0.00002` `H`（默认）

定子绕组之间的平均互感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ls, Lm, and Ms`。

### **每相定子电阻，Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### **零序** — 零序选项 `Include`（默认）| `Exclude`

包含或排除零序项的选项。

- `Include` — 包含零序项。若要优先考虑模型保真度，请使用此默认设置。使用此选项：

  - 对于使用 Partitioning 求解器的仿真会导致错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
  - 会显示 **定子零序电感，L0** 参数。
- `Exclude` — 排除零序项。若要优先考虑桌面仿真或实时部署的仿真速度，请选择此选项。

#### 依赖关系

要启用此参数，请将 **绕组类型** 设置为 `Wye-wound`。

### 铁耗

### **模型** — 启用铁耗计算 `None`（默认）| `Empirical`

指定铁耗计算模型。

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Open-circuit iron losses `[0, 0, 0]` `W`（默认）

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses determined** 指定的频率下，由磁滞、Eddy 和 excess 损耗引起的开路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Short-circuit iron losses `[0, 0, 0]` `W`（默认）

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses determined** 指定的频率下，由磁滞、Eddy 和 excess 损耗引起的短路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### **Electrical frequency at which losses determined** — Electrical frequency at which losses determined `60` `Hz`（默认）

测量开路铁耗和短路铁耗时的电气频率。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### **Short-circuit RMS current for short-circuit iron losses** — Short-circuit RMS current for short-circuit iron losses `95` `A`（默认）

测量短路损耗时得到的短路 RMS 相电流。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### 机械

### **Rotor inertia** — Rotor inertia `0.01` `kg*m^2`（默认）

连接至机械平移端口 **R** 的转子的惯量。该值可以为零。

### **Rotor damping** — Rotor damping `0` `N*m/(rad/s)`（默认）

旋转阻尼。

### 温度依赖性

这些参数仅对具有暴露热端口的模块出现。

### **Measurement temperature** — Measurement temperature `298.15` `K`（默认）

电机参数所对应的温度。

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K`（默认）

将电阻与温度关联的方程中的系数 α，如执行器模块的热模型所述。默认值适用于铜。

### **Permanent magnet flux temperature coefficient** — Permanent magnet flux temperature coefficient `-0.001` `1/K`（默认）

永磁体磁通密度随温度的分数变化率。它用于在温度升高时线性降低转矩和感应反电动势。

### 热端口

这些参数仅对具有暴露热端口的模块出现。

### **Thermal mass for each stator winding** — Thermal mass for each stator winding `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K`（默认）

转子的热质量，即将转子温度升高一度所需的能量。

### **Percentage of main flux path iron losses associated with the rotor** — Percentage of main flux path iron losses associated with the rotor `90`（默认）

与通过转子的磁路相关的主磁通路径铁耗百分比。它决定有多少铁耗发热归因于转子热端口 **HR**，以及有多少归因于三个绕组热端口 **HA**、**HB** 和 **HC**。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — Percentage of cross-tooth flux path iron losses associated with the rotor `30`（默认）

与通过转子的磁路相关的交叉齿磁通路径铁耗百分比。它决定有多少铁耗发热归因于转子热端口 **HR**，以及有多少归因于三个绕组热端口 **HA**、**HB** 和 **HC**。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Empirical`。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024a：定子绕组的 Open-end 配置

要将电机的定子绕组建模为 Open-end 配置，请将 **Winding type** 参数设置为 `Open-end`。然后 BLDC 模块通过启用相应的电气守恒端口来暴露绕组的每一端。

### R2021b：电气连接端口更新

从 R2021b 起，要在 composite 和 expanded 端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

## 描述

三绕组梯形磁通分布无刷直流电机

BLDC 模块对具有三相 wye-wound、delta-wound 或 open-end 定子的无刷直流 (BLDC) 电机建模。使用此模块对 BLDC 电机和 BLDC 伺服电机建模。

BLDC 电机具有永磁体转子和绕线定子。磁通分布为梯形，向驱动电子设备呈现恒定反电动势，从而简化电机控制。您可以在洗衣机、小型四轴飞行器、泵和风扇等消费品中，以及工业自动化和机器人等应用中使用这些电机。

您可以使用 **Back EMF profile** 参数选择如何参数化永磁体磁通分布。两个选项通过假设反电动势为完美梯形来实现简单参数化。您指定磁链或转子感应反电动势。另外两个选项使用您指定的表格数据给出更准确的结果。您指定磁链偏导数或给定转子速度下测得的反电动势常数。

您可以使用 **Winding type** 参数指定绕组的配置。此图显示 wye-wound 定子的等效电路。

您还可以通过将 **Winding type** 分别设置为 `Delta-wound` 或 `Open-end` 来对 delta-wound 或 open-end 定子建模。

**注意**

Simscape™ Electrical™ 包含若干可对同一类型电机或执行器建模的模块。请选择具有足够建模细节的模块，以回答您需要解决的工程设计问题。不要使用比您所需更多建模细节的模块，因为更高保真度的模型会减慢仿真速度，并且参数化更复杂。

像 BLDC 模块这样的模块使用简单等效电路对具有固定系数或参数相关系数的电机建模。这些模型具有中等保真度。使用此模块设计执行应用（如机器人学和机电一体化）中的控制或系统，并在饱和和谐波仅微弱影响损耗时进行效率预测。有关选择合适模块以合适保真度对电机建模的更多信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 电机结构

此图显示转子上具有单个极对的电机结构。

对于前图中的轴约定，当转子角 *θr* 为零时，*a* 相磁通和永磁体磁通对齐。该模块支持第二种转子轴定义。对于第二种定义，转子角是 *a* 相磁轴与转子 *q* 轴之间的角度。

### 梯形磁通变化率

由永磁体产生的转子磁场产生随转子角变化的梯形磁通变化率。此图显示该磁通变化率。

反电动势是磁通变化率，定义为

dΦdt=∂Φ∂θdθdt=∂Φ∂θω,

其中：

- *Φ* 是永磁体磁链。
- *θ* 是转子角。
- *ω* 是机械转速。

梯形磁通变化率曲线的高度 `h` 由永磁体峰值磁通导出。

对 ∂Φ∂θ 在 0 到 π/2 范围内积分，

Φmax=h2(θF+θW),

其中：

- *Φmax* 是永磁体磁链。
- *h* 是磁通变化率曲线高度。
- *θF* 是转子角范围，在该范围内，永磁体磁通在定子中感应的反电动势恒定。
- *θW* 是转子角范围，在该范围内，当转子以恒定速度运动时，反电动势线性增加或减小。

重新整理上述方程，

h=2Φmax/(θF+θW).

### 电气定义方程

定子绕组两端的电压定义为

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

其中：

- *va*、*vb* 和 *vc* 是施加到三个电机电气连接点的外部电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、*ib* 和 *ic* 是流经定子绕组的电流。
- dψadt、dψbdt 和 dψcdt 是每个定子绕组中磁通的变化率。

永磁体和三个绕组共同贡献链接每个绕组的总磁通。总磁通定义为

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm],

其中：

- *ψa*、*ψb* 和 *ψc* 是链接每个定子绕组的总磁通。
- *Laa*、*Lbb* 和 *Lcc* 是定子绕组的自感。
- *Lab*、*Lac*、*Lba* 等是定子绕组的互感。
- *ψam*、*ψbm* 和 *ψcm* 是链接定子绕组的永磁体磁通。

定子绕组中的电感是转子角的函数，定义为

Laa=Ls+Lmcos(2θr),

Lbb=Ls+Lmcos(2(θr−2π/3)),

Lcc=Ls+Lmcos(2(θr+2π/3)),

Lab=Lba=−Ms−Lmcos(2(θr+π/6)),

Lbc=Lcb=−Ms−Lmcos(2(θr+π/6−2π/3)),

以及

Lca=Lac=−Ms−Lmcos(2(θr+π/6+2π/3)),

其中：

- *Ls* 是每相定子自感 — 每个定子绕组的平均自感。
- *Lm* 是定子电感波动 — 自感和互感随转子角变化的波动。
- *Ms* 是定子互感 — 定子绕组之间的平均互感。

链接每个定子绕组的永磁体磁通遵循图中所示的梯形曲线。该模块使用查找表计算永磁体磁通值，从而实现该梯形曲线。

### 简化方程

该模块的定义电压和转矩方程为

[vdvqv0]=P([vavbvc]−Nω[∂ψam∂θr∂ψbm∂θr∂ψcm∂θr]),

vd=Rsid+Lddiddt−NωiqLq

vq=Rsiq+Lqdiqdt+NωidLd,

v0=Rsi0+L0di0dt

以及

T=32N(iqidLd−idiqLq)+[iaibic][∂ψam∂θr∂ψbm∂θr∂ψcm∂θr],

其中：

- *vd*、*vq* 和 *v0* 是 *d* 轴、*q* 轴和零序电压。
- *P* 是 Park 变换，定义为

  P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]
- *N* 是转子永磁体极对数。
- *ω* 是转子机械转速。
- ∂ψam∂θr、∂ψbm∂θr 和 ∂ψcm∂θr

  是链接每相绕组的瞬时永磁体磁通的偏导数。
- *id*、*iq* 和 *i0* 是 *d* 轴、*q* 轴和零序电流，定义为

  [idiqi0]=P[iaibic]
- *Ld* = *Ls* + *Ms* + 3/2 *Lm*。*Ld* 是定子 *d* 轴电感。
- *Lq* = *Ls* + *Ms* − 3/2 *Lm*。*Lq* 是定子 *q* 轴电感。
- *L0* = *Ls* – 2*Ms*。*L0* 是定子零序电感。
- *T* 是转子转矩。转矩从电机壳体（模块物理端口 **C**）流向电机转子（模块物理端口 **R**）。

### 计算铁耗

铁耗分为两项，一项表示主磁化路径，另一项表示在弱磁运行期间变为有源状态的交叉齿尖路径。铁耗模型基于 Mellor [3] 的工作。

表示主磁化路径的项取决于感应的定子 RMS 电压 Vmrms：

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

这是空载运行期间的主导项。*k* 是将 RMS 伏特每 Hz 关联起来的反电动势常数。它定义为 k=Vmrms/f，其中 *f* 是电气频率。右侧第一项是磁滞损耗，第二项是涡流损耗，第三项是 excess 损耗。分子中出现三个系数由您为开路磁滞、Eddy 和 excess 损耗提供的值导出。

表示交叉齿尖路径的项在建立去磁场时变得重要，并且可以通过有限元分析短路测试确定。它取决于与交叉齿尖磁通相关的 RMS EMF，Vdrms\*：

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

三个分子项由您为短路磁滞、Eddy 和 excess 损耗提供的值导出。

### 预定义参数化

BLDC 模块有多个可用的内置参数化。

此预参数化数据允许您设置模块以表示特定供应商的组件。这些无刷直流电机的参数化与制造商数据表匹配。要加载预定义参数化，请双击 BLDC 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用的数据源来确定参数值。使用工程判断和简化假设来填补缺失数据。因此，预期仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并按需细化组件模型。

有关预参数化的更多信息以及可用组件列表，请参阅 List of Pre-Parameterized Components。

### 对热效应建模

您可以暴露热端口，以对将功率转换为热的损耗效应建模。要暴露热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 该模块包含与定子绕组相关的 expanded 电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子绕组相关的 expanded 电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。
