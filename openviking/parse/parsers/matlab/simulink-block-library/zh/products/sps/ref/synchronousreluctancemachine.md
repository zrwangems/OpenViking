---
type: simulink-block
title: 'Synchronous Reluctance Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Reluctance and Stepper'
documentation_page: 'synchronousreluctancemachine'
documentation_source_path: 'ref/synchronousreluctancemachine.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Reluctance Machine

## 端口

### 守恒

### **R** — 机器转子机械转动

与机器转子关联的机械转动守恒端口。

### **C** — 机器机壳机械转动

与机器机壳关联的机械转动守恒端口。

### **~** — 三相复合电气

与定子绕组关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Wye-wound` 或 `Delta-wound`。

### **~1** — 定子正端连接电气

*自 R2024a 起*

与定子正端连接关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **~2** — 定子负端连接电气

*自 R2024a 起*

与定子负端连接关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **n** — 中性相电气

与中性相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **绕组类型** 设置为 `Wye-wound`，并将 **零序** 设置为 `Include`。

### **HA** — 绕组 A 热端口热

与绕组 A 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热端口热

与绕组 B 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HC** — 绕组 C 热端口热

与绕组 C 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 主要

### **电气连接** — 电气连接 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

使用复合还是展开的三相端口。

### **绕组类型** — 绕组配置 `Wye-wound`（默认） | `Delta-wound` | `Open-end`

*自 R2024a 起*

选择绕组配置：

- `Wye-wound` — 绕组为星形连接。
- `Delta-wound` — 绕组为三角形连接。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组为开口配置。模块将绕组的每一端作为电气连接暴露出来。

### **极对数** — 转子极对数 `6`（默认） | integer

转子上的永磁极对数。

### **定子参数化** — 参数化模型 `Specify Ld, Lq and L0`（默认） | `Specify Ls, Lm, and Ms`

定子参数化模型。

#### 依赖关系

**定子参数化** 设置会影响其他参数的可见性。

### **建模保真度** — 建模保真度 `Constant Ld and Lq`（默认） | `Tabulated Ld and Lq`

选择建模保真度：

- `Constant Ld and Lq` — *Ld* 和 *Lq* 值恒定，并由其各自参数定义。
- `Tabulated Ld and Lq` — *Ld* 和 *Lq* 值根据 DQ 电流查找表在线计算，如下所示：

  Ld=f1(id,iq)

  Ld=f2(id,iq)

#### 依赖关系

仅当您将 **定子参数化** 参数设置为 `Specify Ld, Lq, and L0` 时，此参数才可见。

### **定子 d 轴电感，Ld** — 电感 `0.0031` `H`（默认）

机器定子的直轴电感。

#### 依赖关系

仅当您将 **定子参数化** 参数设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 参数设置为 `Constant Ld and Lq` 时，此参数才可见。

### **定子 q 轴电感，Lq** — 电感 `0.004` `H`（默认）

机器定子的交轴电感。

#### 依赖关系

仅当您将 **定子参数化** 参数设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 参数设置为 `Constant Ld and Lq` 时，此参数才可见。

### **直轴电流向量，iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

直轴电流向量，iD。

#### 依赖关系

仅当您将 **定子参数化** 参数设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **交轴电流向量，iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

交轴电流向量，iQ。

#### 依赖关系

仅当您将 **定子参数化** 参数设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **Ld 矩阵，Ld(id,iq)** — Ld 矩阵 `0.0031 * ones(3, 3)` `H`（默认）

Ld 矩阵。

#### 依赖关系

仅当您将 **定子参数化** 参数设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **Lq 矩阵，Lq(id,iq)** — Lq 矩阵 `0.004 * ones(3, 3)` `H`（默认）

Lq 矩阵。

#### 依赖关系

仅当您将 **定子参数化** 参数设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 参数设置为 `Tabulated Ld and Lq` 时，此参数才可见。

### **定子零序电感，L0** — 电感 `0.0005` `H`（默认）

机器定子的零轴电感。

#### 依赖关系

仅当 **定子参数化** 设置为 `Specify Ld, Lq and L0` 且 **零序** 设置为 `Include` 时，此参数才可见。

### **每相定子自感，Ls** — 电感 `0.0025` `H`（默认）

三个定子绕组的平均自感。

#### 依赖关系

仅当 **定子参数化** 设置为 `Specify Ls, Lm, and Ms` 时，此参数才可见。

### **定子电感波动，Lm** — 电感 `-0.0003` `H`（默认）

自感和互感随转子角度波动的幅值。

#### 依赖关系

仅当 **定子参数化** 设置为 `Specify Ls, Lm, and Ms` 时，此参数才可见。

### **定子互感，Ms** — 电感 `0.0010` `H`（默认）

定子绕组之间的平均互感。

#### 依赖关系

仅当 **定子参数化** 设置为 `Specify Ls, Lm, and Ms` 时，此参数才可见。

### **每相定子电阻，Rs** — 电阻 `0.7` `Ohm`（默认）

每个定子绕组的电阻。

### **零序** — 零序模型 `Include`（默认） | `Exclude`

零序模型：

- `Include` — 优先考虑模型保真度。如果为使用 Partitioning 求解器的仿真包含零序项，则会发生错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

#### 依赖关系

如果此参数设置为：

- `Include` 且 **定子参数化** 设置为 **Specify Ld, Lq, and L0** — **定子零序电感，L0** 参数可见。
- `Exclude` — **定子零序电感，L0** 参数不可见。

### 铁耗

有关计算铁耗的更多信息，请参阅 Calculating Iron Losses。

### **模型** — 铁耗建模选项 `Specify magnetizing resistance`（默认） | `Specify tabulated Steinmetz coefficients` | `Tabulate with current and speed`

是否启用铁耗建模。

#### 依赖关系

要启用此参数，请将 **建模保真度** 设置为 `Tabulate Ld and Lq`。

### **磁化电阻** — 铁耗磁化电阻 `inf` `Ohm`（默认）

磁化电阻。值必须大于零。默认值为 `inf`，表示没有铁耗。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Specify magnetizing resistance`，或将 **建模保真度** 设置为 `Constant Ld and Lq`。

### **转子磁滞损耗系数，k\_hr(id,iq)** — 转子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认）

转子的磁滞损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Specify tabulated Steinmetz coefficients`。

### **转子涡流损耗系数，k\_Jr(id,iq)** — 转子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认）

转子的涡流损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Specify tabulated Steinmetz coefficients`。

### **转子附加损耗系数，k\_er(id,iq)** — 转子附加损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认）

转子的附加损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Specify tabulated Steinmetz coefficients`。

### **定子磁滞损耗系数，k\_hs(id,iq)** — 定子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认）

定子的磁滞损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Specify tabulated Steinmetz coefficients`。

### **定子涡流损耗系数，k\_Js(id,iq)** — 定子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认）

定子的涡流损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Specify tabulated Steinmetz coefficients`。

### **定子附加损耗系数，k\_es(id,iq)** — 定子附加损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认）

定子的附加损耗系数，取决于 *d* 轴和 *q* 轴电流。它用于 Steinmetz 方程。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Specify tabulated Steinmetz coefficients`。

### **转子速度向量，w** — 转子速度 `[1000, 2000]` `rpm`（默认）

用于铁耗表格化的转子速度向量。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Tabulate with current and speed`。

### **转子铁耗表，Pr(id,iq,w)** — 转子铁耗表 `zeros(3, 3, 2)` `W`（默认）

转子的铁耗，基于 *d* 轴和 *q* 轴电流以及转子速度进行表格化。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Tabulate with current and speed`。

### **定子铁耗表，Ps(id,iq,w)** — 定子铁耗表 `zeros(3, 3, 2)` `W`（默认）

定子的铁耗，基于 *d* 轴和 *q* 轴电流以及转子速度进行表格化。

#### 依赖关系

要启用此参数，请将 **模型** 设置为 `Tabulate with current and speed`。

### 机械

### **转子惯量** — 惯量 `0.01` `kg*m^2`（默认）

连接到机械平移端口 **R** 的转子惯量。

### **转子阻尼** — 阻尼 `0` `N*m/(rad/s)`（默认）

旋转阻尼。

### **转子角度定义** — 角度 `Angle between the a-phase magnetic axis and the d-axis`（默认） | `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。如果选择默认值，则在零转子角度时，转子和 *a* 相磁通对齐。否则，在零转子角度时，*a* 相电流生成最大转矩值。

### 热

要启用这些参数，请将 **建模选项** 设置为 `Show thermal port`。

### **测量温度** — 测量温度 `298.15` `K`（默认）

电机参数对应的温度。

### **电阻温度系数** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 所述。默认值适用于铜。

### **每个定子绕组的热质量** — 每个定子绕组的热质量 `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

### **转子热质量** — 转子热质量 `200` `J/K`（默认）

转子的热质量，即将转子温度升高一度所需的能量。

### **与转子相关的总铁耗百分比** — 总铁耗百分比 `50`（默认）

与转子相关的总铁耗百分比。

#### 依赖关系

要启用此参数，请将 **建模保真度** 设置为 `Costant Ld and Lq`，或将 **定子参数化** 设置为 `Specify Ls, Lm, and Ms`。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2024a: 定子绕组的 Open-end 和 delta-wound 配置

除了 wye-wound 配置外，您还可以将电机的定子绕组建模为 delta-wound 配置或 open-end 配置。

要将电机的定子绕组建模为 delta-wound 配置，请将 **Winding type** 参数设置为 `Delta-wound`。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。

要将电机的定子绕组建模为 open-end 配置，请将 **Winding type** 参数设置为 `Open-end`。然后 Synchronous Reluctance Machine 模块通过启用相应的电守恒端口来暴露绕组的每一端。

### R2021b: Electrical connection 端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

具有正弦磁通分布的同步磁阻电机

Synchronous Reluctance Machine 模块表示具有正弦磁通分布的同步磁阻电机 (SynRM)。该图显示了定子绕组的等效电路。

您还可以通过将 **Winding type** 分别设置为 `Delta-wound` 或 `Open-end`，以 delta-wound 或 open-end 配置对定子绕组建模。

### 电机结构

该图显示了转子上具有单极对的电机结构。对于所示的轴约定，当转子机械角度 *θr* 为零时，*a* 相和永磁磁通对齐。该模块支持第二种转子轴定义，其中转子机械角度定义为 *a* 相磁轴与转子 *q* 轴之间的角度。

### 方程

定子绕组上的合成电压为

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

其中：

- *va*、
  *vb* 和
  *vc* 是定子绕组各相的相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、
  *ib* 和
  *ic* 是流过定子绕组的电流。
- *ψa*、
  *ψb* 和
  *ψc* 是链接每个定子绕组的磁通。

永磁体、励磁绕组和三个定子绕组共同贡献链接每个绕组的磁通。总磁通定义为

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]

其中：

- *Laa*、
  *Lbb* 和
  *Lcc* 是定子绕组的自感。
- *Lab*、
  *Lac*、
  *Lba*、
  *Lbc*、
  *Lca* 和
  *Lcb* 是定子绕组的互感。

θe=Nθr+rotor offset

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
- *rotor offset* 为 `0`（如果您相对于 d 轴定义转子电角度），或 `-pi/2`（如果您相对于 q 轴定义转子电角度）。
- *Ls* 是每相定子自感。该值是每个定子绕组的平均自感。
- *Lm* 是定子电感波动。该值是自感和互感随转子角度变化的波动幅值。
- *Ms* 是定子互感。该值是定子绕组之间的平均互感。

### 简化方程

将 Park 变换应用于模块的电气定义方程，可得到与转子角度无关的转矩表达式。

Park 变换 *P* 定义为

P=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212],

其中 *θe* 是电角度。电角度取决于转子机械角度和极对数，使得

θe=Nθr+rotor offset

其中：

- *N* 是极对数。
- *θr* 是转子机械角度。

将 Park 变换应用于前两个电气定义方程，可得到定义该模块行为的方程：

vd=Rsid+Lddiddt−NωiqLq,

vq=Rsiq+Lqdiqdt+NωidLd,

v0=Rsi0+L0di0dt,

T=32N(iqidLd−idiqLq)

Jdωdt=T−TL−Bmω,

其中：

- *id*、
  *iq* 和
  *i0* 是由以下定义的 *d* 轴、*q* 轴和零序电流：

  [idiqi0]=P[iaibic],

  其中 *ia*、
  *ib* 和
  *ic* 是定子电流。
- *vd*、
  *vq* 和
  *v0* 是由以下定义的 *d* 轴、*q* 轴和零序电压：

  [vdvqv0]=P[vavbvc],

  其中 *va*、
  *vb* 和
  *vc* 是定子电压。
- *dq0* 电感分别定义为

  - Ld=Ls+Ms+32Lm
  - Lq=Ls+Ms−32Lm
  - L0=Ls−2Ms.
- *Rs* 是每相定子电阻。
- *N* 是转子极对数。
- *T* 是转子转矩。对于 Synchronous Reluctance Machine 模块，转矩从电机外壳（模块守恒端口 **C**）流向电机转子（模块守恒端口 **R**）。
- *TL* 是负载转矩。
- *Bm* 是转子阻尼。
- *ω* 是转子机械转速。
- *J* 是转子惯量。

### 计算铁耗

要计算 Synchronous Reluctance Machine 模块中的铁耗，请选择是通过指定磁化电阻来对其建模、基于 Steinmetz 方程对其进行参数化，还是将损耗制表为电流和转子转速的函数。

如果将 **Stator parameterization** 参数设置为 `Specify Ls, Lm, and Ms` 或 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Constant Ld and Lq`，则指定 **Magnetizing resistance** 参数以对铁耗建模。

在 **Iron Losses** 设置中，如果将 **Model** 参数设置为 `Specify tabulated Steinmetz coefficients` 或 `Tabulate with current and speed`，则铁耗作为电气转矩的减小量施加到机械侧：

τloss=sign(w)Ploss,stator+Ploss,rotorabs(w)+wmin,

其中 *wmin* 是开始考虑铁耗的最小转子转速，它等于 `1` `rad/s`。

总耗散功率等于铁耗与铜耗之和：

Pdissipated=τlossw+Raia2+Rbib2+Rcic2.

**Steinmetz 参数化方法**

要基于 Steinmetz 方程对铁耗建模，请将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq`。Steinmetz 方法会针对不同电机转速或电频率进行缩放，因此铁耗数据仅需作为电机电流的函数。

如果在 **Iron losses** 设置中将 **Model** 参数设置为 `Specify tabulated Steinmetz coefficients`，则铁耗由下式给出：

Ploss,rotor(f)=khr(id,iq)f+kJr(id,iq)f2+ker(id,iq)f1.5Ploss,stator(f)=khs(id,iq)f+kJs(id,iq)f2+kes(id,iq)f1.5

其中：

- *khr(id,iq)* 是 **Rotor hysteresis loss coefficient, k\_hr(id,iq)**。
- *kJr(id,iq)* 是 **Rotor eddy current loss coefficient, k\_Jr(id,iq)**。
- *ker(id,idq)* 是 **Rotor excess current loss coefficient, k\_er(id,iq)**。
- *khs(id,iq)* 是 **Stator hysteresis loss coefficient, k\_hs(id,iq)**。
- *kJs(id,iq)* 是 **Stator eddy current loss coefficient, k\_Js(id,iq)**。
- *kes(id,iq)* 是 **Stator excess current loss coefficient, k\_es(id,iq)**。
- f=wnPolePairs2π 是电频率，单位为 Hz。

**Tabulate with current and speed**

要通过分别对转子和定子的铁耗进行制表来对铁耗建模，请将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 参数设置为 `Tabulated Ld and Lq`。

然后，如果在 **Iron losses** 设置中将 **Model** 参数设置为 `Tabulate with current and speed`，则铁耗由下式给出：

Ploss(id,iq,w)=tablelookup(Ptable,id,iq,w).

其中 *w* 是 **Rotor speed vector, w** 参数。

**带热端口的铁耗**

如果暴露模块的热端口，则每相耗散的功率在定子和转子中充当热源：

PdissA=Raia2+Ploss,stator3PdissB=Rbib2+Ploss,stator3PdissC=Rcic2+Ploss,stator3PdissR=Ploss,rotor

如果指定磁化电阻，则转子中的铁耗等于总铁耗的某个百分比。该百分比保持恒定，且不依赖于其他状态：

Ploss,rotor=percentrotor100Piron loss,total.

然后，剩余铁耗分配到不同的定子相中：

Ploss,stator=(1−percentrotor100)Piron loss,total.

### 对热效应建模

您可以暴露热端口，以对将功率转换为热量的损耗效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口。
- `Show thermal port` — 该模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
