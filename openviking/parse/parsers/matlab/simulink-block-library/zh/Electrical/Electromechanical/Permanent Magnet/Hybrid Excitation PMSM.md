---
type: simulink-block
title: 'Hybrid Excitation PMSM'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'hybridexcitationpmsm'
documentation_source_path: 'ref/hybridexcitationpmsm.html'
language: zh-CN
chinese_source: worker-translation
---

# Hybrid Excitation PMSM

## 端口

### 守恒

### **R** — 机器转子机械旋转

与机器转子关联的机械旋转守恒端口。

### **C** — 机器机壳机械旋转

与机器机壳关联的机械旋转守恒端口。

### **~** — 三相复合电气

与定子绕组关联的可扩展三相端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **~1** — 定子正端连接电气

*自 R2024a 起*

与定子正端连接相关联的可扩展三相端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **~2** — 定子负端连接电气

*自 R2024a 起*

与定子负端连接相关联的可扩展三相端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 正端连接相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 正端连接相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 正端连接相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 负端连接相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 负端连接相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 负端连接相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **n** — 中性相电气

与中性相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Winding type** 设置为 `Wye-wound`，并将 **Zero sequence** 设置为 `Include`。

### **fd+** — 励磁绕组正端子电气

与励磁绕组正端子相关联的电气守恒端口。

### **fd-** — 励磁绕组负端子电气

与励磁绕组负端子相关联的电气守恒端口。

### **HA** — 绕组 A 热端口热

与绕组 A 相关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热端口热

与绕组 B 相关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — 绕组 C 热端口热

与绕组 C 相关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子相关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并模拟产生的热量和电机温度的影响。

### 主要

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是使用复合三相端口还是扩展三相端口。

### **Winding type** — 绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

*自 R2024a 起*

选择绕组配置：

- `Wye-wound` — 绕组为星形连接。
- `Delta-wound` — 绕组为三角形连接。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组采用开端配置。该模块将绕组的每一端作为电气连接引出。

### **Modeling fidelity** — 建模保真度 `Constant Ld, Lq, Lmf, Lf and PM`（默认）| `Tabulated Ld, Lq, Lmf, Lf and PM`

选择建模保真度：

- `Constant Ld, Lq, Lmf, Lf and PM` — *Ld*、*Lq*、*Lmf*、*Lf* 和 *PM* 值为常量，并由其各自参数定义。
- `Tabulated Ld, Lq, Lmf, Lf and PM` — *Ld*、*Lq*、*Lmf*、*Lf* 和 *PM* 值根据 DQ 和励磁电流查找表在线计算，如下所示：

  Ld=f1(id,iq,if)

  Lq=f2(id,iq,if)

  Lmf=f3(id,iq,if)

  λPM=f4(id,iq,if)

  Lf=f5(if)

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 时可见。

### **Number of pole pairs** — 转子极对数 `6`（默认）| integer

转子上的永磁体极对数。

### **Permanent magnet flux linkage** — 磁链 `0.09` `Wb`（默认）| positive integer

任一定子绕组的峰值永磁体磁链。

#### 依赖项

此参数仅在将 **Modeling fidelity** 参数设置为 `Constant Ld, Lq, Lmf, Lf and PM` 时可见。

### **Stator parameterization** — 参数化模型 `Specify Ld, Lq and L0`（默认）| `Specify Ls, Lm, and Ms`

定子参数化模型。

#### 依赖项

**Stator parameterization** 设置会影响其他参数的可见性。

### **Stator d-axis inductance, Ld** — 电感 `0.0031` `H`（默认）

机器定子的直轴电感。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Constant Ld, Lq, Lmf, Lf and PM` 时可见。

### **Stator q-axis inductance, Lq** — 电感 `0.0045` `H`（默认）

机器定子的交轴电感。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Constant Ld, Lq, Lmf, Lf and PM` 时可见。

### **Direct-axis current vector, iD** — 直轴电流向量，iD `[-200, 0, 200]` `A`（默认）

直轴电流向量，iD。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Quadrature-axis current vector, iQ** — 交轴电流向量，iQ `[-200, 0, 200]` `A`（默认）

交轴电流向量，iQ。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Excitation current vector, iF** — 励磁电流向量，iF `[-20, 0, 20]` `A`（默认）

励磁电流向量，iF。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Ld matrix, Ld(id,iq,if)** — Ld 矩阵 `0.0031 * ones(3, 3, 3)` `H`（默认）

Ld 矩阵。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Lq matrix, Lq(id,iq,if)** — Lq 矩阵 `0.0045 * ones(3, 3, 3)` `H`（默认）

Lq 矩阵。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Mutual field armature inductance, Lmf(id,iq,if)** — 励磁-电枢互感电感 `0.0067 * ones(3, 3, 3)` `H`（默认）

励磁-电枢互感电感。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Permanent magnet flux linkage, PM(id,iq,if)** — 永磁体磁链 `0.1 * ones(3, 3, 3)` `Wb`（默认）

永磁体磁链。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0`，将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Lf vector, Lf(if)** — Lf 向量 `0.06 * ones(1, 3)` `H`（默认）

Lf 向量。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0`，将 **Modeling fidelity** 参数设置为 `Tabulated Ld, Lq, Lmf, Lf and PM` 时可见。

### **Stator zero-sequence inductance, L0** — 电感 `0.0006` `H`（默认）

机器定子的零轴电感。

#### 依赖项

此参数仅在 **Stator parameterization** 设置为 `Specify Ld, Lq and L0` 且 **Zero sequence** 设置为 `Include` 时可见。

### **Stator self-inductance per phase, Ls** — 电感 `0.0027` `H`（默认）

三个定子绕组的平均自感。

#### 依赖项

此参数仅在 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms` 时可见。

### **Stator inductance fluctuation, Lm** — 电感 `-0.0005` `H`（默认）

自感和互感随转子角度的波动。

#### 依赖项

此参数仅在 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms` 时可见。

### **Stator mutual inductance, Ms** — 电感 `0.0011` `H`（默认）

定子绕组之间的平均互感。

#### 依赖项

此参数仅在 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms` 时可见。

### **Field winding inductance, Lf** — 电感 `0.06` `H`（默认）

励磁绕组的电感。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Constant Ld, Lq, Lmf, Lf and PM`，或者将 **Stator parameterization** 参数设置为 `Specify Ls, Lm, and Ms` 时可见。

### **Mutual field armature inductance, Lmf** — 电感 `0.0067` `H`（默认）

电枢-励磁互感电感。

#### 依赖项

此参数仅在将 **Stator parameterization** 参数设置为 `Specify Ld, Lq, and L0` 且将 **Modeling fidelity** 参数设置为 `Constant Ld, Lq, Lmf, Lf and PM`，或者将 **Stator parameterization** 参数设置为 `Specify Ls, Lm, and Ms` 时可见。

### **Stator resistance per phase, Rs** — 电阻 `0.7` `Ohm`（默认）

每个定子绕组的电阻。

### **Field winding resistance, Rf** — 电阻 `2.85` `Ohm`（默认）

励磁绕组的电阻。

### **Zero sequence** — 零序模型 `Include`（默认）| `Exclude`

零序模型：

- `Include` — 优先考虑模型保真度。如果对使用 Partitioning 求解器的仿真包含零序项，则会发生错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

#### 依赖项

如果此参数设置为：

- `Include`，且 **Stator parameterization** 设置为 **Specify Ld, Lq, and L0** — **Stator zero-sequence inductance, L0** 参数可见。
- `Exclude` — **Stator zero-sequence inductance, L0** 参数不可见。

### **Rotor angle definition** — 角度 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。如果选择默认值，则对于零转子角度，转子和 *a* 相磁链对齐。否则，对于零转子角度，*a* 相电流产生最大转矩值。

### 机械

### **Rotor inertia** — 惯量 `0.01` `kg*m^2`（默认）

连接到机械平移端口 **R** 的转子惯量。

### **Rotor Damping** — 阻尼 `0` `N*m/(rad/s)`（默认）

旋转阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 测量温度 `298.15` `K`（默认）

电机参数标称所用的温度。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值适用于铜。

### **Permanent magnet flux temperature coefficient** — 永磁体磁通温度系数 `-0.001`（默认）

永磁体磁通密度随温度变化的分数变化率。它用于随温度升高线性降低转矩和感应反电动势。

### **Thermal mass for each stator winding** — 每个定子绕组的热质量 `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）

转子的热质量，即将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2024a: 定子绕组的 open-end 和 delta-wound 配置

除了 wye-wound 配置外，还可以将电机的定子绕组建模为 delta-wound 配置或 open-end 配置。

要将电机的定子绕组建模为 delta-wound 配置，请将 **Winding type** 参数设置为 `Delta-wound`。*a* 相连接在端口 **a** 与 **b** 之间，*b* 相连接在端口 **b** 与 **c** 之间，*c* 相连接在端口 **c** 与 **a** 之间。

要将电机的定子绕组建模为 open-end 配置，请将 **Winding type** 参数设置为 `Open-end`。Hybrid Excitation PMSM 模块随后通过启用相应的电气守恒端口来暴露绕组的每一端。

### R2021b: 电气连接端口更新

从 R2021b 起，要在 composite 和 expanded 端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些变更，在较早版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

具有三相 wye-wound 定子的混合励磁同步电机

Hybrid Excitation PMSM 模块表示具有三相 wye-wound 定子的混合励磁同步电机。永磁体和励磁绕组提供电机励磁。使用此模块对混合励磁永磁同步电机（PMSM）、双激励 PMSM 和同步电机进行建模。此图显示定子和转子绕组的等效电路。

还可以通过将 **Winding type** 分别设置为 `Delta-wound` 或 `Open-end`，将永磁同步电机建模为 delta-wound 或 open-end 配置。

### 电机构造

该图显示转子上具有单个极对的电机构造。对于轴约定，当转子机械角 *θr* 为零时，*a* 相磁通与永磁体磁通对齐。该模块支持第二种转子轴定义，其中转子机械角定义为 *a* 相磁轴与转子 *q* 轴之间的角度。

### 方程

定子绕组两端的电压定义为

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

其中：

- *va*、*vb* 和 *vc* 分别是定子绕组两端的各相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、*ib* 和 *ic* 是在定子绕组中流动的电流。
- dψadt、dψbdt 和 dψcdt 是每个定子绕组中磁通的变化率。

励磁绕组两端的电压表示为

vf=Rfif+dψfdt,

其中：

- *vf* 是励磁绕组两端的单独相电压。
- *Rf* 是励磁绕组的等效电阻。
- *if* 是在励磁绕组中流动的电流。
- dψfdt 是励磁绕组中磁通的变化率。

永磁体、励磁绕组和三个星形连接的定子绕组对链接每个绕组的磁通均有贡献。总磁通定义为

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm]+[LamfLbmfLcmf]if,

其中：

- *ψa*、*ψb* 和 *ψc* 是链接每个定子绕组的总磁通。
- *Laa*、*Lbb* 和 *Lcc* 是定子绕组的自感。
- *Lab*、*Lac*、*Lba*、*Lbc*、*Lca* 和 *Lcb* 是定子绕组的互感。
- *ψam*、*ψbm* 和 *ψcm* 是链接定子绕组的磁化磁通。
- *Lamf*、*Lbmf* 和 *Lcmf* 是励磁绕组的互感。

定子绕组中的电感是转子电角度的函数，定义为

θe=Nθr+rotor offset

Laa=Ls+Lmcos(2θe),

Lbb=Ls+Lmcos(2(θe−2π/3)),

Lcc=Ls+Lmcos(2(θe+2π/3)),

Lab=Lba=−Ms−Lmcos(2(θe+π/6)),

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3)),

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3)),

其中：

- *N* 是转子极对数。

- *θr* 是转子机械角。

- *θe* 是转子电角度。
- *rotor offset* 是 `0`，如果你相对于 d 轴定义转子电角度；或者为 `-pi/2`，如果你相对于 q 轴定义转子电角度。
- *Ls* 是每相定子自感。该值是每个定子绕组的平均自感。
- *Lm* 是定子电感波动。该值是自感和互感随转子角度变化的波动。
- *Ms* 是定子互感。该值是定子绕组之间的平均互感。

链接绕组 *a-a’* 的磁化磁通在 *θe* = 0° 时最大，在 *θe* = 90° 时为零。因此：

ψm=[ψamψbmψcm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)],

Lmf=[LamfLbmfLcmf]=[LmfcosθeLmfcos(θe−2π/3)Lmfcos(θe+2π/3)],

以及

Ψf=Lfif+LmfT[iaibic],

其中：

- *ψm* 是链接的电机磁通。
- *Lmf* 是励磁-电枢互感。
- *ψf* 是链接励磁绕组的磁通。
- *Lf* 是励磁绕组电感。
- [Lmf]T 是 *Lmf* 向量的转置，即，

  [Lmf]T=[LamfLbmfLcmf]T=[LamfLbmfLcmf].

### 简化方程

将 Park 变换应用于模块的电气定义方程，可得到与转子角度无关的转矩表达式。

Park 变换定义为

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]

将 Park 变换应用于前两个电气定义方程，可得到定义模块行为的方程：

vd=Rsid+Lddiddt+Lmfdifdt−NωiqLq,

vq=Rsiq+Lqdiqdt+Nω(idLd+ψm+ifLmf),

v0=Rsi0+L0di0dt

vf=Rfif+Lfdifdt+32Lmfdiddt,

T=32N(iq(idLd+ψm+ifLmf)−idiqLq),

以及

Jdωdt=T=TL−Bmω.

其中：

- *vd*、*vq* 和 *v0* 是 *d* 轴、*q* 轴和零序电压。这些电压定义为

  [vdvqv0]=P[vavbvc].
- *id*、*iq* 和 *i0* 是 *d* 轴、*q* 轴和零序电流，定义为

  [idiqi0]=P[iaibic].
- *Ld* 是定子 *d* 轴电感。*Ld* = *Ls* + *Ms* + 3/2 *Lm*。
- *ω* 是机械转速。
- *Lq* 是定子 *q* 轴电感。*Lq* = *Ls* + *Ms* − 3/2 *Lm*。
- *L0* 是定子零序电感。*L0* = *Ls* – 2*Ms*。
- *T* 是转子转矩。对于 Hybrid Excitation PMSM 模块，转矩从电机外壳（模块守恒端口 **C**）流向电机转子（模块守恒端口 **R**）。
- *J* 是转子惯量。
- *TL* 是负载转矩。
- *Bm* 是转子阻尼。

### 热效应建模

可以暴露热端口，以对产生的热量和电机温度的影响进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块包含与定子绕组相关的扩展电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子绕组相关的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在致动器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

Nominal values 提供了一种指定模型中变量预期幅值的方法。使用基于 nominal values 的系统缩放可提高仿真鲁棒性。可以使用不同来源指定 nominal values，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
