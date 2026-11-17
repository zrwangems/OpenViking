---
type: simulink-block
title: 'AC Cable (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'accablethreephase'
documentation_source_path: 'ref/accablethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# AC Cable (Three-Phase)

## 端口

### 守恒端口

### **~S1** — 护套电气

与护套 1 关联的可扩展三相电气守恒端口。

### **~N1** — 相电气

与 *a*、*b* 和 *c* 相 1 关联的可扩展三相电气守恒端口。

### **g1** — 接地电气

与接地 1 关联的电气守恒端口。

### **~S2** — 护套电气

与护套 2 关联的可扩展三相电气守恒端口。

### **~N2** — 相电气

与 *a*、*b* 和 *c* 相 2 关联的可扩展三相电气守恒端口。

### **g2** — 接地电气

与接地 2 关联的电气守恒端口。

## 参数

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电力系统单线图的模型。

扩展三相端口用三个独立的电气守恒端口表示三相系统的各个相。

### **Cable length** — 长度 `120` `km`（默认）

电缆的长度。

### **Geometric mean radius of conductor** — 半径 `5` `mm`（默认）

导体的几何平均半径，它是交流电缆导体中单股线数量和类型的函数。

### **Sheath radius** — 半径 `10` `mm`（默认）

护套的平均半径。为确保护套半径大于具有特定 GMR 的单股导体的物理半径，护套半径必须大于 GMR\*e14。

### **Outer cable radius** — 外半径 `20` `mm`（默认）

电缆的外半径，单位为 mm。电缆半径必须大于 **Sheath radius** 参数。这确保护套和导体都封装在绝缘外电缆层内。

### **Line-line spacing (center-to-center)** — 距离 `25` `mm`（默认）

线路中心之间的距离。

### **Line formation** — 线路配置 `Trefoil`（默认）| `Flat`

电缆线路形成方式。

### **Conductor resistance per length** — 电阻 `1` `Ohm/km`（默认）

导体每单位长度的电阻。

### **Sheath resistance per length** — 电阻 `10` `Ohm/km`（默认）

护套每单位长度的电阻。

### **Insulation relative permittivity** — 介电常数 `2.4`（默认）

绝缘的相对介电常数。

### **Relative permittivity between lines and return path** — 相对介电常数 1（默认）

电路的相对介电常数。

### **Return parameterization** — 模型 `Use frequency and Earth resistivity`（默认）| `Use distance and resistance`

参数化方法。

#### 依赖关系

启用任一选项会启用其他参数。

### **Frequency for Earth-return impedance** — 频率 `60` `Hz`（默认）

计算大地回路阻抗的频率。

#### 依赖关系

为 **Return parameterization** 参数选择 `Use frequency and Earth resistivity` 会启用此参数。

### **Earth resistivity** — 电阻 `100` `m*Ohm`（默认）

大地回路电阻率。

#### 依赖关系

为 **Return parameterization** 参数选择 `Use frequency and Earth resistivity` 会启用此参数。

### **Effective distance to return path** — 回路距离 `1` `km`（默认）

相与回路之间的有效距离。

#### 依赖关系

为 **Return parameterization** 参数选择 `Use distance and resistance` 会启用此参数。

### **Return path resistance per length** — 回路单位电阻 `0.1` `Ohm/km`（默认）

回路每单位长度的电阻。

#### 依赖关系

为 **Return parameterization** 参数选择 `Use distance and resistance` 会启用此参数。

## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

三相交流电力电缆

AC Cable (Three-Phase) 模块表示一根三相交流电力电缆，每相周围都有导电护套。该图显示了导电护套内的单相导体。内圆柱表示该相的主导体，外圆柱表示导电护套。

您可以通过将 **Modeling option** 参数设置为以下任一值来对复合或扩展三相端口进行建模：

- `Composite three-phase ports` — 包含用于护套和相的三相连接端口，以及用于每个电气参考节点的单相连接端口。
- `Expanded three-phase ports` — 包含用于每个护套、相和电气参考节点的单相连接端口。

AC Cable (Three-Phase) 模块包含各相、护套和回路之间的电感和互感。因此，您可以将理想电气参考模块连接到两个回路端口 **g1** 和 **g2**，同时在接地回路或中性点回路线路中保持损耗建模。

为了在将 AC Cable (Three-Phase) 模块连接到源模块时促进仿真收敛，请使用以下方法之一包含源阻抗：

- 将源模块配置为包含阻抗。
- 在源模块和 AC Cable (Three-Phase) 模块之间插入一个对阻抗进行建模的模块。

要对未键合护套进行建模，请将未键合护套连接到 Open Circuit (Three-Phase) 模块。该图显示了当 **Modeling option** 设置为 `Composite three-phase ports` 时的单点键合模型。

为了获得高性能建模（就仿真速度而言），请使用单个 AC Cable (Three-Phase) 模块。为了提高模型保真度（就频率行为而言），请将多个 AC Cable (Three-Phase) 模块串联连接。对于串联连接的模块，护套和主导体充当具有完美相换位的耦合传输线。用于对特定物理长度电缆进行建模的 AC Cable (Three-Phase) 模块数量必须小于您所建模的物理系统中的换位次数。您可以建模的连续多段电缆类型包括：

- 未键合连续电缆
- 单点键合连续电缆
- 双点键合连续电缆

您还可以使用 AC Cable (Three Phase) 模块对交叉键合电缆进行建模。

这个三 pi 段电缆模型使用扩展三相端口和单相连接线实现交叉键合。模型中的护套是双点键合的。

这个具有复合三相端口的模块模型使用 Phase Permute 模块实现交叉键合。模型中的护套是未键合的。

有关允许您选择段数和键合类型的示例，请参阅 AC Cable with Bonded Sheaths。

### 三相交流电缆模型

AC Cable (Three-Phase) 模块使用部分电感的概念来计算电感值。这些值包括各相、护套和回路的部分自感，以及以下各项之间的部分互感：

- 相与各其他相
- 相与该相的护套
- 相与相邻相的护套
- 相与回路
- 护套与各相邻护套
- 护套与回路

对于三个等效相，定义向量 [phase A; sheath A; phase B; sheath B; phase C; sheath C] 的电阻关系的矩阵为

R=[Ra+RgRgRgRgRgRgRgRs+RgRgRgRgRgRgRgRa+RgRgRgRgRgRgRgRs+RgRgRgRgRgRgRgRa+RgRgRgRgRgRgRgRs+Rg]

Ra=Ra'l

Rg=Rreturn'l,

其中 *R'return* 取决于回路参数化方法，使得：

- 对于基于距离和电阻的回路参数化 Rreturn'=Rg'。
- 对于基于频率和大地电阻率的回路参数化 Rreturn'=π210−7f

并且

Rs=Rs'l,

其中：

- *R* 是电阻矩阵。
- *Ra* 是特定相的电阻。
- *Rs* 是特定护套的电阻。
- *Rg* 是接地回路或中性点回路的电阻。
- *R'a* 是相的单位长度电阻。
- *l* 是电缆长度。
- *R's* 是护套的单位长度电阻。
- *R'return* 是回路的单位长度电阻。*R'return* 的值根据回路参数化方法而变化。
- *R'g* 是接地回路或中性点回路的单位长度电阻。
- *f* 是如果您使用频率和大地电阻率方法对模块进行参数化，模块用于计算大地回路参数的频率。

该模块使用标准表达式来计算以下各项之间的电容：

- 同心或相邻圆柱体
- 各相与其自身护套
- 各护套与回路

定义这些电容关系的矩阵为

C=[Casa−Casa0000−CasaCasa+Csag000000Casa−Casa0000−CasaCasa+Csag000000Casa−Casa0000−CasaCasa+Csag]

Casa=2πεrε0lln(rsra)

ra=GMR⋅e14

Csag=2πεenvε0lln(rcablers,outer),

其中：

- *C* 是电容矩阵。
- *Casa* 是各相与该相护套之间的电容。
- *Csag* 是各护套与回路之间的电容。
- *ϵr* 是电介质的介电常数。
- *ϵ0* 是自由空间的介电常数。
- *rs* 是护套的半径。
- *ra* 是导体的有效半径。对于单股导体，*ra* 是股线的半径。
- *rcable* 是电缆半径，且 *rcable* 大于 *rs,outer*。
- *GMR* 是导体的几何平均半径。对于单股导体，GMR=rstrande−14，其中 *rstrand* 是股线的半径。
- *ϵenv* 是护套线路与回路之间材料的介电常数。

该模块使用部分电感的概念来计算电感值。这些值包括各相、护套和回路的部分自感，以及以下各项之间的部分互感：

- 相与各其他相
- 相与该相的护套
- 相与相邻相的护套
- 相与回路
- 护套与各相邻护套
- 护套与回路

定义这些电感关系的方程为：

L=[DaδAαAαδDsαSαSAαDaδAααSδDsαSAαAαDaδαSαSδDs]

Da=La−Mag

La=2×10−7l[ln(2lra)−34]

Mag=Msg=2×10−7l[ln(2lDreturn)−1]

其中 *Dreturn* 取决于回路参数化方法，使得：

- 对于基于距离和电阻的回路参数化 Dreturn=De。
- 对于基于频率和大地电阻率的回路参数化 Dreturn=1650ρ2πf。

Ds=Ls−Msg

Ls=Masa=2×10−7l[ln(2lrs)−34]

δ=Masa−Mag

α=Masb−Mag

Masb=Msasb=Mab=2×10−7l[ln(2ldab)−1],

其中 *dab* 取决于线路形成参数化方法，使得：

- 对于三叶形线路形成参数化 dab=Dab。
- 对于扁平线路形成参数化 dab=Dab23。

A=Mab−Mag

S=Msasb−Msg,

其中：

- *L* 是电感矩阵。
- *Da* 是单相通过其整个路径和回路的自感。
- *La* 是各相的部分自感。
- *Mag* 是各相与接地回路或中性点回路之间的部分互感。
- *Msg* 是各护套与接地回路或中性点回路之间的部分互感。
- 因子 2×10−7 等于 μ0/2π，因为自由空间的磁导率 *μ0* 等于 1.257×10−6 或 4π×10−7 H/m。
- *Ds* 是单个护套通过其整个路径和回路的自感。
- *Ls* 是各护套的部分自感。
- *Masa* 是各相与该相护套之间的部分互感。
- *δ* 是相与该相护套之间的有效互感。
- *α* 是相与相邻护套之间的有效互感。
- *Masb* 是各相与各相邻相护套之间的部分互感。
- *Msasb* 是不同相护套之间的部分互感。
- *Mab* 是各相与各其他相之间的部分互感。
- *Dreturn* 是到回路的有效距离。如果您使用距离/回路参数化方法，*Dreturn* 的值会变化。
- *De* 是到接地回路或中性点回路的有效距离。
- *ρ* 是接地回路的有效大地电阻率。
- *f* 是用于确定回路路径属性的频率。
- *dab* 是相邻相之间的有效距离。*dab* 的值根据线路参数化方法而变化。
- *Dab* 是相邻相之间的中心到中心距离。
- *A* 是相之间的有效互感。
- *S* 是护套之间的有效互感。

与 Clarke 变换相关的模态变换可简化等效电路。六乘六变换 *T* 为

T=13[10200001020010−120320010−1203210−120−320010−120−32].

由于 T†=T−1，应用 *T* 变换可得到模态电阻矩阵 *Rm*、模态电容矩阵 *Cm* 和模态电感矩阵 *Lm*。

变换后的矩阵为：

Rm=T†RT=[Ra+3Rg3Rg00003RgRs+3Rg000000Ra000000Rs000000Ra000000Rs]

Cm=T†CT=[Casa−Casa0000−CasaCasa+Csag000000Casa−Casa0000−CasaCasa+Csag000000Casa−Casa0000−CasaCasa+Csag]=C

Lm=T†LT=[Da+2Aδ+2α0000δ+2αDs+2A000000Da−Aδ−α0000δ−αDs−S000000Da−Aδ−α0000δ−αDs−S].

该变换将每个六乘六矩阵变为三个非耦合的二乘二矩阵。电容矩阵在该变换下不变。由于 *T* 是酉矩阵，功率在变换域和未变换域中保持不变。

### 假设和限制

- 对于电阻计算，各相是等效的。
- 相对于相到护套电容和护套到回路电容，由于导电护套提供的屏蔽，所有其他电容均可忽略。
