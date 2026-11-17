---
type: simulink-block
title: 'PMLSM'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmlsm'
documentation_source_path: 'ref/pmlsm.html'
language: zh-CN
chinese_source: worker-translation
---

# PMLSM

## 端口

### 守恒

### **~** — 三相端口电气

可扩展三相端口。

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

与定子正端连接相关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **~2** — 定子负端连接电气

*自 R2024a 起*

与定子负端连接相关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`，并将 **绕组类型** 设置为 `Open-end`。

### **n** — 中性相电气

与中性相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **绕组类型** 设置为 `Wye-wound`，并将 **零序** 设置为 `Include`。

### **R** — 电机动子机械

与电机动子相关联的机械平移守恒端口。

### **C** — 电机壳体机械

与电机壳体相关联的机械平移守恒端口。

### **HA** — 绕组 A 热端口热

与绕组 A 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热端口热

与绕组 B 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HC** — 绕组 C 热端口热

与绕组 C 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口，并对产生的热量和电机温度的影响进行建模。

### 主要

### **电气连接** — 电气连接 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

使用复合三相端口还是扩展三相端口。

### **绕组类型** — 绕组配置 `Wye-wound`（默认） | `Delta-wound` | `Open-end`

绕组的配置：

- `Wye-wound` — 绕组为星形绕组。
- `Delta-wound` — 绕组为三角形绕组。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组采用开口端配置。模块将绕组的每一端作为电气连接暴露出来。

### **建模保真度** — 建模保真度 `Constant Ld, Lq and PM`（默认） | `Tabulated Ld, Lq and PM`

建模保真度：

- `Constant Ld, Lq and PM` — *Ld*、*Lq* 和 *PM* 值为常数，并由各自的参数定义。
- `Tabulated Ld, Lq and PM` — *Ld*、*Lq* 和 *PM* 值根据 DQ 电流查找表在线计算，如下：h

  Ld=f1(id,iq)

  Ld=f2(id,iq)

  λPM=f2(id,iq)

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`。

### **极距** — 极距 `0.03` `m`（默认） | scalar

极距。

### **永磁体磁链参数化** — 永磁体磁链参数化 `Specify flux linkage`（默认） | `Specify force constant` | `Specify back EMF constant`

永磁体磁链，指定为 `Specify flux linkage`、`Specify force constant` 或 `Specify back EMF constant`。

### **永磁体磁链** — 永磁体磁链 `0.03` `Wb`（默认） | scalar

与任一定子绕组交链的峰值永磁体磁链。

#### 依赖关系

要启用此参数，请将 **永磁体磁链参数化** 设置为 `Specify flux linkage`，并将 **建模保真度** 设置为 `Constant Ld, Lq and PM`。

### **力常数** — 力常数 `0.18` `N/A`（默认） | scalar

任一定子绕组的力常数。

#### 依赖关系

要启用此参数，请将 **永磁体磁链参数化** 设置为 `Specify force constant`，并将 **建模保真度** 设置为 `Constant Ld, Lq and PM`。

### **反电动势常数** — 反电动势常数 `0.18` `s*V/m`（默认） | scalar

任一定子绕组的反电动势常数。

#### 依赖关系

要启用此参数，请将 **永磁体磁链参数化** 设置为 `Specify back EMF constant`，并将 **建模保真度** 设置为 `Constant Ld, Lq and PM`。

### **定子参数化** — 定子参数化 `Specify Ld, Lq, and L0`（默认） | `Specify Ls, Lm, and Ms`

定子参数化，指定为 `Specify Ld, Lq, and L0` 或 `Specify Ls, Lm, and Ms`。

### **定子 d 轴电感，Ld** — 定子 `d` 轴电感 `0.00019` `H`（默认） | scalar

`d` 轴电感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Constant Ld, Lq and PM`。

### **定子 q 轴电感，Lq** — 定子 `q` 轴电感 `0.00025` `H`（默认） | scalar

`q` 轴电感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Constant Ld, Lq and PM`。

### **定子零序电感，L0** — 定子零序电感 `0.00016` `H`（默认） | scalar

零序电感。

#### 依赖关系

要启用此参数，需满足以下任一条件：

- 将 **绕组类型** 设置为 `Wye-wound`，将 **零序** 设置为 `Include`，并将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`。
- 将 **绕组类型** 设置为 `Delta-wound`，并将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`。

### **直轴电流向量，iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认） | vector

直轴电流向量，iD。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld, Lq and PM`。

### **交轴电流向量，iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认） | vector

交轴电流向量，iQ。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld, Lq and PM`。

### **Ld 矩阵，Ld(id,iq)** — Ld 矩阵 `0.00019 * ones(3, 3)` `H`（默认） | matrix

Ld 矩阵。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld, Lq and PM`。

### **Lq 矩阵，Lq(id,iq)** — Lq 矩阵 `0.00025 * ones(3, 3)` `H`（默认） | matrix

Lq 矩阵。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ld, Lq, and L0`，并将 **建模保真度** 设置为 `Tabulated Ld, Lq and PM`。

### **永磁体磁链，PM(id,iq)** — 永磁体磁链 `0.03 * ones(3, 3)` `Wb`（默认）

永磁体磁链。

#### 依赖关系

要启用此参数，请设置：

- **定子参数化** 为 `Specify Ld, Lq, and L0`
- **建模保真度** 为 `Tabulated Ld, Lq and PM`
- **永磁体磁链参数化** 为 `Specify flux linkage`

### **力常数矩阵，kf(iD,iQ)** — 力常数矩阵 `0.18 * ones(3, 3)` `N/A`（默认） | matrix

力常数矩阵。

#### 依赖关系

要启用此参数，请设置：

- **定子参数化** 为 `Specify Ld, Lq, and L0`
- **建模保真度** 为 `Tabulated Ld, Lq and PM`
- **永磁体磁链参数化** 为 `Specify force constant`

### **反电动势常数矩阵，ke(iD,iQ)** — 反电动势常数矩阵 `0.18 * ones(3, 3)` `s*V/m`（默认） | matrix

反电动势常数矩阵。

#### 依赖关系

要启用此参数，请设置：

- **定子参数化** 为 `Specify Ld, Lq, and L0`
- **建模保真度** 为 `Tabulated Ld, Lq and PM`
- **永磁体磁链参数化** 为 `Specify back EMF constant`

### **每相定子自感，Ls** — 每相定子自感 `0.0002` `H`（默认） | scalar

五个定子绕组各自的平均自感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ls, Lm, and Ms`。

### **定子电感波动，Lm** — 定子电感波动 `-0.00002` `H`（默认） | scalar

定子绕组的自感和互感随角度的波动。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ls, Lm, and Ms`。

### **定子互感，Ms** — 定子互感 `0.00002` `H`（默认） | scalar

定子绕组之间的平均互感。

#### 依赖关系

要启用此参数，请将 **定子参数化** 设置为 `Specify Ls, Lm, and Ms`。

### **每相定子电阻，Rs** — 每相定子电阻 `0.013` `Ohm`（默认） | scalar

每个定子绕组的电阻。

### **零序** — 零序选项 `Include`（默认） | `Exclude`

包含或排除零序项的选项。

- `Include` — 包含零序项。为优先保证模型保真度，请使用此默认设置。使用此选项：

  - 对于使用 Partitioning 求解器的仿真会导致错误。有关详细信息，请参阅使用 Partitioning 求解器提高仿真速度。
  - 会暴露一个零序参数。
- `Exclude` — 排除零序项。为优先提高桌面仿真或实时部署的仿真速度，请选择此选项。

#### 依赖关系

要启用此参数，请将 **绕组类型** 设置为 `Wye-wound`。

### **角度定义** — 角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认） | `Angle between the a-phase magnetic axis and the q-axis`

角度测量的参考点。默认值为 `Angle between the a-phase magnetic axis and the d-axis`。此定义在电机结构图中显示。选择此值时，当动子角度为零时，动子和 *a* 相磁通对齐。

此参数可选择的另一个值为 `Angle between the a-phase magnetic axis and the q-axis`。选择此值时，当动子角度为零时，*a* 相电流产生最大力。

### 机械

### **动子质量** — 动子质量 `0.01` `kg`（默认）

电机动子的质量。

### **线性阻尼** — 线性阻尼 `0` `N/(m/s)`（默认）

线性阻尼。

### 热

要启用这些参数，请将 **建模选项** 设置为 `Show thermal port`。

### **测量温度** — 测量温度 `298.15` `K`（默认）

电机参数对应的温度。

### **电阻温度系数** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻与温度关系方程中的系数 α，如执行器模块的热模型所述。默认值适用于铜。

### **永磁体磁通温度系数** — 永磁体磁通温度系数 `-0.001` `1/K`（默认）

永磁体磁通密度随温度变化的分数变化率。使用此参数可在温度升高时线性降低转矩和感应反电动势。

### **每个定子绕组的热质量** — 每个定子绕组的热质量 `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

### **转子热质量** — 转子热质量 `200` `J/K`（默认）

转子的热质量，即使转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：定子绕组的开口端配置

要对电机的定子绕组进行开口端配置建模，请将 **绕组类型** 参数设置为 `Open-end`。随后，PMLSM 模块会通过启用相应的电气守恒端口来暴露绕组的每一端。

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **电气连接** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **电气连接** 参数。

## 描述

Permanent magnet linear synchronous motor with sinusoidal flux distribution

PMLSM 模块对具有三相星形绕组定子的永磁直线同步电机 (PMLSM) 建模。使用此模块对直线同步电机 (LSMs) 和直线伺服电机建模。下图显示定子绕组的等效电路。

还可以通过将 **绕组类型** 设置为 `Delta-wound` 来以三角形绕组配置对永磁直线同步电机建模。

### 电机构造

下图显示电机结构。

### 方程

定子绕组两端的电压由下式定义：

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

其中：

- *va*、
  *vb* 和
  *vc* 是各个
  定子绕组两端的相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、
  *ib* 和
  *ic* 是
  流过定子绕组的电流。
- dψadt、dψbdt 和 dψcdt 是每个定子
  绕组中磁通量的变化率。

永磁体和三个绕组对交链每个绕组的总磁通都有贡献。总磁通由下式定义：

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm],

其中：

- *ψa*、
  *ψb* 和
  *ψc* 是交链每个定子绕组的总磁通。
- *Laa*、
  *Lbb* 和
  *Lcc* 是
  定子绕组的自感。
- *Lab*、
  *Lac*、
  *Lba*、
  *Lbc*、
  *Lca* 和
  *Lcb* 是定子绕组的
  互感。
- *ψam*、
  *ψbm* 和
  *ψcm* 是交链定子绕组的永磁体
  磁通。

定子绕组中的电感是电角度的函数，定义如下：

θe=Npx+rotor offset,

Laa=Ls+Lmcos(2θe)

Lbb=Ls+Lmcos(2(θe−2π/3))

Lcc=Ls+Lmcos(2(θe+2π/3))

Lab=Lba=−Ms−Lmcos(2(θe+π/6))

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3))

以及

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3))

其中：

- *θe* 是电角度。
- *rotor offset* 为 `0`（如果相对于 d 轴定义
  转子电角度），或
  为 `-pi/2`（如果相对于 q 轴定义转子电角度）。
- Np=πτ，*τ* 是极距。
- *x* 是距离。
- *Ls* 是每相定子
  自感。该值是每个
  定子绕组的平均自感。
- *Lm* 是定子电感
  波动。该值是随角度变化的自感和
  互感波动。
- *Ms* 是定子互
  感。该值是定子
  绕组之间的平均互感。

交链绕组 *a* 的永磁体磁通在
*θe* = 0° 时最大，在
*θe* = 90° 时为零。因此，
交链的电机磁通由下式定义：

[ψamψbmψcm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)]

其中 *ψm* 是永磁体磁链。

### 简化电气方程

对电气方程应用 Park 变换可得到与角度无关的力表达式。

Park 变换定义为：

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]

其中 *θe* 是电角度，定义为 *Npx*。

对定子绕组电压和电流使用 Park 变换会将其变换到与角度无关的 dq0 坐标系：

[vdvqv0]=P[vavbvc]

以及

[idiqi0]=P[iaibic]

对前两个电气方程应用 Park 变换可得到以下定义模块行为的方程：

vd=Rsid+Lddiddt−NpviqLq,

vq=Rsiq+Lqdiqdt+Npv(idLd+ψm),

v0=Rsi0+L0di0dt

以及

F=32Np(iq(idLd+ψm)−idiqLq),

Mdvdt=F−FL−Bmv,

其中：

- *Ld* =
  *Ls* +
  *Ms* + 3/2
  *Lm*。
  *Ld* 是定子
  *d* 轴电感。
- *Lq* =
  *Ls* +
  *Ms* − 3/2
  *Lm*。
  *Lq* 是定子
  *q* 轴电感。
- *L0* =
  *Ls* –
  2*Ms*。
  *L0* 是定子
  零序电感。
- *Rs* 是每相
  定子电阻。
- *v* 是线速度。
- *Np* 是极距
  因子。
- *M* 是动子
  质量。
- *Bm* 是阻尼。
- *FL* 是负载力。

PMLSM 模块使用 Park 变换的原始非正交实现。如果尝试应用替代实现，dq0 电压和电流会得到不同结果。

力常数
*kf*、反电动势常数
*ke* 与永磁体磁链
之间的关系定义如下：

ke=kf=Npψm.

### 对热效应建模

可以暴露热端口以对生成热量和电机温度的影响建模。要
暴露热端口，请将 **建模选项** 参数设置为以下任一值：

- `No thermal port` — 该模块包含与定子绕组关联的扩展
  电气守恒端口，但不
  包含热端口。
- `Show thermal port` — 该模块包含与定子绕组关联的扩展
  电气守恒端口，以及每个绕组和转子的热
  守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，
请使用模块对话框或属性检查器中的 **初始目标** 区段。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供一种在模型中指定变量预期幅值的方法。
使用基于标称值的系统缩放可提高仿真鲁棒性。可以
使用不同来源指定标称值，包括模块对话框或属性检查器中的 **标称值** 区段。有关
详细信息，请参阅 System Scaling by Nominal Values。
