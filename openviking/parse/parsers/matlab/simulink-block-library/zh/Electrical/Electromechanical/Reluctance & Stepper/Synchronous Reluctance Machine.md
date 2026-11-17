---
type: simulink-block
title: 'Synchronous Reluctance Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'synchronousreluctancemachine'
documentation_source_path: 'ref/synchronousreluctancemachine.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Reluctance Machine

## 端口

### 守恒端口

### **R** — 电机转子机械旋转

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳机械旋转

与电机机壳相关联的机械旋转守恒端口。

### **~** — 三相复合电气

与定子绕组相关联的可扩展三相端口。

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

要启用此端口，请将 **Winding type** 设置为 `Wye-wound`，并将 **Zero sequence** 设置为 `Include`。

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

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

使用复合三相端口还是扩展三相端口。

### **Winding type** — 绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

*自 R2024a 起*

选择绕组配置：

- `Wye-wound` — 绕组为星形连接。
- `Delta-wound` — 绕组为三角形连接。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组为开口端配置。模块将绕组的每一端作为电气连接暴露出来。

### **Number of pole pairs** — 转子极对数 `6`（默认）| 整数

转子上的永磁体极对数。

### **Stator parameterization** — 参数化模型 `Specify Ld, Lq and L0`（默认）| `Specify Ls, Lm, and Ms`

定子参数化模型。

#### 依赖关系

**Stator parameterization** 设置会影响其他参数的可见性。

### **Modeling fidelity** — 建模保真度 `Constant Ld and Lq`（默认）| `Tabulated Ld and Lq`

选择建模保真度：

- `Constant Ld and Lq` — *Ld* 和 *Lq* 值为常数，由各自的参数定义。
- `Tabulated Ld and Lq` — *Ld* 和 *Lq* 值根据 DQ 电流查找表在线计算，如下所示：

  Ld=f1(id,iq)

  Ld=f2(id,iq)

#### 依赖关系

仅当将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 时，此参数才可见。

### **Stator d-axis inductance, Ld** — 电感 `0.0031` `H`（默认）

电机定子的直轴电感。

#### 依赖关系

仅当将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Constant Ld and Lq` 时，此参数才可见。

### **Stator q-axis inductance, Lq** — 电感 `0.004` `H`（默认）

电机定子的交轴电感。

#### 依赖关系

仅当将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Constant Ld and Lq` 时，此参数才可见。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

直轴电流向量，iD。

#### 依赖关系

仅当将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

交轴电流向量，iQ。

#### 依赖关系

仅当将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **Ld matrix, Ld(id,iq)** — Ld 矩阵 `0.0031 * ones(3, 3)` `H`（默认）

Ld 矩阵。

#### 依赖关系

仅当将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **Lq matrix, Lq(id,iq)** — Lq 矩阵 `0.004 * ones(3, 3)` `H`（默认）

Lq 矩阵。

#### 依赖关系

仅当将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **Stator zero-sequence inductance, L0** — 电感 `0.0005` `H`（默认）

电机定子的零轴电感。

#### 依赖关系

仅当 **Stator parameterization** 设置为 `Specify Ld, Lq and L0` 且 **Zero sequence** 设置为 `Include` 时，此参数才可见。

### **Stator self-inductance per phase, Ls** — 电感 `0.0025` `H`（默认）

三个定子绕组的平均自感。

#### 依赖关系

仅当 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms` 时，此参数才可见。

### **Stator inductance fluctuation, Lm** — 电感 `-0.0003` `H`（默认）

自感和互感随转子角度波动的幅值。

#### 依赖关系

仅当 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms` 时，此参数才可见。

### **Stator mutual inductance, Ms** — 电感 `0.0010` `H`（默认）

定子绕组之间的平均互感。

#### 依赖关系

仅当 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms` 时，此参数才可见。

### **Stator resistance per phase, Rs** — 电阻 `0.7` `Ohm`（默认）

每个定子绕组的电阻。

### **Zero sequence** — 零序模型 `Include`（默认）| `Exclude`

零序模型：

- `Include` — 优先考虑模型保真度。如果为使用 Partitioning 求解器的仿真包含零序项，则会发生错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

#### 依赖关系

如果此参数设置为：

- `Include` 且 **Stator parameterization** 设置为 **Specify Ld, Lq, and L0** — **Stator zero-sequence inductance, L0** 参数可见。
- `Exclude` — **Stator zero-sequence inductance, L0** 参数不可见。

### 铁损

有关计算铁损的详细信息，请参阅 Calculating Iron Losses。

### **Model** — 铁损建模选项 `Specify magnetizing resistance`（默认）| `Specify tabulated Steinmetz coefficients` | `Tabulate with current and speed`

是否启用铁损建模。

#### 依赖关系

要启用此参数，请将 **Modeling fidelity** 设置为 `Tabulate Ld and Lq`。

### **Magnetizing resistance** — 铁损的励磁电阻 `inf` `Ohm`（默认）

励磁电阻。该值必须大于零。默认值为 `inf`，表示没有铁损。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify magnetizing resistance`，或将 **Modeling fidelity** 设置为 `Constant Ld and Lq`。

### **Rotor hysteresis loss coefficient, k\_hr(id,iq)** — 转子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认）

转子的磁滞损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`。

### **Rotor eddy current loss coefficient, k\_Jr(id,iq)** — 转子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认）

转子的涡流损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`。

### **Rotor excess current loss coefficient, k\_er(id,iq)** — 转子附加电流损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认）

转子的附加电流损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`。

### **Stator hysteresis loss coefficient, k\_hs(id,iq)** — 定子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认）

定子的磁滞损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`。

### **Stator eddy current loss coefficient, k\_Js(id,iq)** — 定子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认）

定子的涡流损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`。

### **Stator excess current loss coefficient, k\_es(id,iq)** — 定子附加电流损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认）

定子的附加电流损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`。

### **Rotor speed vector, w** — 转子速度 `[1000, 2000]` `rpm`（默认）

铁损制表所依据的转子速度向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`。

### **Rotor iron loss table, Pr(id,iq,w)** — 转子铁损表 `zeros(3, 3, 2)` `W`（默认）

转子铁损，基于 *d* 轴和 *q* 轴电流以及转子速度制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`。

### **Stator iron loss table, Ps(id,iq,w)** — 定子铁损表 `zeros(3, 3, 2)` `W`（默认）

定子铁损，基于 *d* 轴和 *q* 轴电流以及转子速度制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`。

### 机械

### **Rotor inertia** — 惯量 `0.01` `kg*m^2`（默认）

连接到机械平移端口 **R** 的转子的惯量。

### **Rotor Damping** — 阻尼 `0` `N*m/(rad/s)`（默认）

旋转阻尼。

### **Rotor angle definition** — 角度 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。如果选择默认值，则对于零转子角度，转子和 *a* 相磁通对齐。否则，对于零转子角度，*a* 相电流产生最大转矩值。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 测量温度 `298.15` `K`（默认）

电机参数的标称温度。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值为铜的值。

### **Thermal mass for each stator winding** — 每个定子绕组的热质量 `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）

转子的热质量，即将转子温度升高一度所需的能量。

### **Percentage of total iron losses associated with the rotor** — 总铁损百分比 `50`（默认）

与转子相关联的总铁损百分比。

#### 依赖关系

要启用此参数，请将 **Modeling fidelity** 设置为 `Costant Ld and Lq`，或将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2024a：定子绕组的开放式和三角形绕组配置

除了星形绕组配置外，您还可以将电机的定子绕组建模为三角形绕组配置或开放式配置。

要将电机的定子绕组建模为三角形绕组配置，请将 **Winding type** 参数设置为 `Delta-wound`。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。

要将电机的定子绕组建模为开放式配置，请将 **Winding type** 参数设置为 `Open-end`。然后，Synchronous Reluctance Machine 模块通过启用相应的电气守恒端口来暴露绕组的每一端。

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

具有正弦磁通分布的同步磁阻电机

Synchronous Reluctance Machine 模块表示具有正弦磁通分布的同步磁阻电机（SynRM）。该图显示了定子绕组的等效电路。

您还可以通过将 **Winding type** 分别设置为 `Delta-wound` 或 `Open-end`，将定子绕组建模为三角形绕组或开放式配置。

### 电机结构

该图显示了转子上具有单对极的电机结构。对于所示的轴约定，当转子机械角度 *θr* 为零时，*a* 相和永磁磁通对齐。该模块支持第二种转子轴定义，其中转子机械角度定义为 *a* 相磁轴与转子 *q* 轴之间的角度。

### 方程

定子绕组上的组合电压为

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

其中：

- *va*、*vb* 和 *vc* 是定子绕组上的各相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、*ib* 和 *ic* 是在定子绕组中流动的电流。
- *ψa*、*ψb* 和 *ψc* 是链接每个定子绕组的磁通。

永磁体、励磁绕组和三个定子绕组对链接每个绕组的磁通都有贡献。总磁通定义为

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]

其中：

- *Laa*、*Lbb* 和 *Lcc* 是定子绕组的自感。
- *Lab*、*Lac*、*Lba*、*Lbc*、*Lca* 和 *Lcb* 是定子绕组的互感。

θe=Nθr+rotor offset

Laa=Ls+Lmcos(2θe)

Lbb=Ls+Lmcos(2(θe−2π/3))

Lcc=Ls+Lmcos(2(θe+2π/3))

Lab=Lba=−Ms−Lmcos(2(θe+π/6))

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3))

以及

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3))

其中：

- *θr* 是转子机械角度。
- *θe* 是转子电角度。
- *rotor offset* 如果您相对于 d 轴定义转子电角度，则为 `0`；如果您相对于 q 轴定义转子电角度，则为 `-pi/2`。
- *Ls* 是每相定子自感。此值是每个定子绕组的平均自感。
- *Lm* 是定子电感波动。此值是自感和互感随转子角度变化的波动幅度。
- *Ms* 是定子互感。此值是定子绕组之间的平均互感。

### 简化方程

将 Park 变换应用于模块的电气定义方程，可得到与转子角度无关的转矩表达式。

Park 变换 *P* 定义为

P=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212],

其中 *θe* 是电角度。电角度取决于转子机械角度和极对数，使得

θe=Nθr+rotor offset

其中：

- *N* 是极对数。
- *θr* 是转子机械角度。

将 Park 变换应用于前两个电气定义方程，可得到定义模块行为的方程：

vd=Rsid+Lddiddt−NωiqLq,

vq=Rsiq+Lqdiqdt+NωidLd,

v0=Rsi0+L0di0dt,

T=32N(iqidLd−idiqLq)

Jdωdt=T−TL−Bmω,

其中：

- *id*、*iq* 和 *i0* 是由下式定义的 *d* 轴、*q* 轴和零序电流

  [idiqi0]=P[iaibic],

  其中 *ia*、*ib* 和 *ic* 是定子电流。
- *vd*、*vq* 和 *v0* 是由下式定义的 *d* 轴、*q* 轴和零序电流

  [vdvqv0]=P[vavbvc],

  其中 *va*、*vb* 和 *vc* 是定子电流。
- *dq0* 电感分别定义为

  - Ld=Ls+Ms+32Lm
  - Lq=Ls+Ms−32Lm
  - L0=Ls−2Ms.
- *Rs* 是每相定子电阻。
- *N* 是转子极对数。
- *T* 是转子转矩。对于 Synchronous Reluctance Machine 模块，转矩从电机壳体（模块守恒端口 **C**）流向电机转子（模块守恒端口 **R**）。
- *TL* 是负载转矩。
- *Bm* 是转子阻尼。
- *ω* 是转子机械转速。
- *J* 是转子惯量。

### 计算铁损

要计算 Synchronous Reluctance Machine 模块中的铁损，请选择您希望通过指定磁化电阻来建模铁损、基于 Steinmetz 方程对其进行参数化，还是希望将损耗制表为电流和转子速度的函数。

如果您将 **Stator parameterization** 参数设置为 `Specify Ls, Lm, and Ms` 或 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Constant Ld and Lq`，则指定 **Magnetizing resistance** 参数来建模铁损。

在 **Iron Losses** 设置中，如果您将 **Model** 参数设置为 `Specify tabulated Steinmetz coefficients` 或 `Tabulate with current and speed`，则铁损作为电转矩的减少量施加到机械侧：

τloss=sign(w)Ploss,stator+Ploss,rotorabs(w)+wmin,

其中 *wmin* 是开始考虑铁损的最小转子速度，它等于 `1` `rad/s`。

耗散的总功率等于铁损和铜损之和：

Pdissipated=τlossw+Raia2+Rbib2+Rcic2.

**Steinmetz 参数化方法**

要基于 Steinmetz 方程建模铁损，请将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq`。Steinmetz 方法针对不同的电机速度或电频率进行缩放，因此铁损数据仅需要作为电机电流的函数。

如果在 **Iron losses** 设置中，您将 **Model** 参数设置为 `Specify tabulated Steinmetz coefficients`，则铁损由下式给出：

Ploss,rotor(f)=khr(id,iq)f+kJr(id,iq)f2+ker(id,iq)f1.5Ploss,stator(f)=khs(id,iq)f+kJs(id,iq)f2+kes(id,iq)f1.5

其中：

- *khr(id,iq)* 是 **Rotor hysteresis loss coefficient, k\_hr(id,iq)**。
- *kJr(id,iq)* 是 **Rotor eddy current loss coefficient, k\_Jr(id,iq)**。
- *ker(id,idq)* 是 **Rotor excess current loss coefficient, k\_er(id,iq)**。
- *khs(id,iq)* 是 **Stator hysteresis loss coefficient, k\_hs(id,iq)**。
- *kJs(id,iq)* 是 **Stator eddy current loss coefficient, k\_Js(id,iq)**。
- *kes(id,iq)* 是 **Stator excess current loss coefficient, k\_es(id,iq)**。
- f=wnPolePairs2π 是电频率，单位为 Hz。

**按电流和速度制表**

要通过分别对转子和定子制表来建模铁损，请将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq`。

然后，如果在 **Iron losses** 设置中，您将 **Model** 参数设置为 `Tabulate with current and speed`，则铁损由下式给出：

Ploss(id,iq,w)=tablelookup(Ptable,id,iq,w).

其中 *w* 是 **Rotor speed vector, w** 参数。

**带热端口的铁损**

如果您暴露模块的热端口，则每相中耗散的功率充当定子和转子中的热源：

PdissA=Raia2+Ploss,stator3PdissB=Rbib2+Ploss,stator3PdissC=Rcic2+Ploss,stator3PdissR=Ploss,rotor

如果您指定磁化电阻，则转子中的铁损等于总铁损的某个百分比。此百分比保持恒定，不依赖于其他状态：

Ploss,rotor=percentrotor100Piron loss,total.

然后，剩余的铁损分配到不同的定子相中：

Ploss,stator=(1−percentrotor100)Piron loss,total.

### 建模热效应

您可以暴露热端口来建模将功率转换为热量的损耗效应。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
