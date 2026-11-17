---
type: simulink-block
title: 'Switched Reluctance Machine (Multi-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'switchedreluctancemachinemultiphase'
documentation_source_path: 'ref/switchedreluctancemachinemultiphase.html'
language: zh-CN
chinese_source: worker-translation
---

# Switched Reluctance Machine (Multi-Phase)

## 端口
```yaml
ports:
- name: R
  summary: 机器转子机械旋转
  direction: unspecified
  data_types: double
- name: C
  summary: 机器壳体机械旋转
  direction: unspecified
  data_types: double
- name: a1
  summary: '*a* 相正电源电气'
  direction: unspecified
  data_types: double
- name: b1
  summary: '*b* 相正电源电气'
  direction: unspecified
  data_types: double
- name: c1
  summary: '*c* 相正电源电气'
  direction: unspecified
  data_types: double
- name: d1
  summary: '*d* 相正电源电气'
  direction: unspecified
  data_types: double
- name: e1
  summary: '*e* 相正电源电气'
  direction: unspecified
  data_types: double
- name: f1
  summary: '*f* 相正电源电气'
  direction: unspecified
  data_types: double
- name: a2
  summary: '*a* 相负电源电气'
  direction: unspecified
  data_types: double
- name: b2
  summary: '*b* 相负电源电气'
  direction: unspecified
  data_types: double
- name: c2
  summary: '*c* 相负电源电气'
  direction: unspecified
  data_types: double
- name: d2
  summary: '*d* 相负电源电气'
  direction: unspecified
  data_types: double
- name: e2
  summary: '*e* 相负电源电气'
  direction: unspecified
  data_types: double
- name: f2
  summary: '*f* 相负电源电气'
  direction: unspecified
  data_types: double
- name: HA
  summary: '*a* 相端子热端口热'
  direction: unspecified
- name: HB
  summary: '*b* 相端子热端口热'
  direction: unspecified
- name: HC
  summary: '*c* 相端子热端口热'
  direction: unspecified
- name: HD
  summary: '*d* 相端子热端口热'
  direction: unspecified
- name: HE
  summary: '*e* 相端子热端口热'
  direction: unspecified
- name: HF
  summary: '*f* 相端子热端口热'
  direction: unspecified
- name: HR
  summary: 转子热端口热
  direction: unspecified
```

### 守恒

### **R** — 机器转子机械旋转

与机器转子关联的机械旋转守恒端口。

**数据类型：** `double`

### **C** — 机器壳体机械旋转

与机器壳体关联的机械旋转守恒端口。

**数据类型：** `double`

### **a1** — *a* 相正电源电气

*a* 相的正电源。

**数据类型：** `double`

### **b1** — *b* 相正电源电气

*b* 相的正电源。

**数据类型：** `double`

### **c1** — *c* 相正电源电气

*c* 相的正电源。

**数据类型：** `double`

### **d1** — *d* 相正电源电气

*d* 相的正电源。

**数据类型：** `double`

### **e1** — *e* 相正电源电气

*e* 相的正电源。

如果将 **Number of stator phases** 参数设置为 `Five-phase`，则此端口可见。

**数据类型：** `double`

### **f1** — *f* 相正电源电气

*f* 相的正电源。

如果将 **Number of stator phases** 参数设置为 `Six-phase`，则此端口可见。

**数据类型：** `double`

### **a2** — *a* 相负电源电气

*a* 相的负电源。

**数据类型：** `double`

### **b2** — *b* 相负电源电气

*b* 相的负电源。

**数据类型：** `double`

### **c2** — *c* 相负电源电气

*c* 相的负电源。

**数据类型：** `double`

### **d2** — *d* 相负电源电气

*d* 相的负电源。

**数据类型：** `double`

### **e2** — *e* 相负电源电气

*e* 相的负电源。

如果将 **Number of stator phases** 参数设置为 `Five-phase`，则此端口可见。

**数据类型：** `double`

### **f2** — *f* 相负电源电气

*f* 相的负电源。

如果将 **Number of stator phases** 参数设置为 `Six-phase`，则此端口可见。

**数据类型：** `double`

### **HA** — *a* 相端子热端口热

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口热

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口热

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HD** — *d* 相端子热端口热

与定子绕组 *d* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HE** — *e* 相端子热端口热

与定子绕组 *e* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`，并将 **Number of stator phases** 设置为 `Five-phase`。

### **HF** — *f* 相端子热端口热

与定子绕组 *f* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`，并将 **Number of stator phases** 设置为 `Six-phase`。

### **HR** — 转子热端口热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Number of stator phases
  summary: 四相或五相 SRM Four-phase（默认）| Five-phase | Six-phase
  group: 主
- name: Number of rotor poles
  summary: 转子极数 8（默认）| 正整数
  group: 主
- name: Stator resistance per phase
  summary: 电阻 3 Ohm（默认）| 正标量
  group: 主
- name: Stator parameterization
  summary: 参数化方法 Specify saturated flux linkage（默认）| Specify flux characteristic
  group: 主
- name: Saturated flux linkage
  summary: 磁链 0.43 Wb（默认）| 正标量
  group: 主
- name: Aligned inductance
  summary: 电感 0.0046 H（默认）| 正标量
  group: 主
- name: Unaligned inductance
  summary: 电感 6.7e-4 H（默认）| 正标量
  group: 主
- name: Current vector, i
  summary: 电流 [0, 50, 100] A（默认）| 正向量
  group: 主
- name: Angle vector, theta
  summary: 角度 [0, 22.5, 45] deg（默认）| 正向量
  group: 主
- name: Flux linkage matrix, Phi(i,theta)
  summary: 磁链 [0, 0, 0; .37, .06, .37; .43, .1, .43] Wb（默认）| 标量
  group: 主
- name: Model
  summary: 铁损建模选项 None（默认）| Tabulate losses from current and speed | Tabulate losses from current, speed, and angle
  group: 铁损
- name: Magnetizing resistance
  summary: 铁损的励磁电阻 inf Ohm（默认）
  group: 铁损
- name: Rotor speed vector, w
  summary: 转子速度 [500, 1000, 1500] rpm（默认）
  group: 铁损
- name: Iron loss table, Ploss(i,w)
  summary: 基于电流和速度制表的铁损表 zeros(3, 3) W（默认）
  group: 铁损
- name: Iron loss table, Ploss(i,w,theta)
  summary: 基于电流、速度和角度制表的铁损表 zeros(3, 3, 2) W（默认）
  group: 铁损
- name: Rotor inertia
  summary: 惯量 0.01 kg*m^2（默认）| 正标量
  group: 机械
- name: Rotor Damping
  summary: 阻尼 0 N*m/(rad/s)（默认）| 标量
  group: 机械
- name: Measurement temperature
  summary: 额定温度 298.15 k（默认）| 实标量
  group: 热
- name: Resistance temperature coefficient
  summary: 温度系数 3.93e-3 1/K（默认）| 正标量
  group: 热
- name: Thermal mass for each stator winding
  summary: 绕组热质量 100 J/K（默认）| 正标量
  group: 热
- name: Rotor thermal mass
  summary: 转子热质量 200 J/K（默认）| 正标量
  group: 热
- name: Percentage of total iron losses associated with the rotor
  summary: 总铁损百分比 50（默认）
  group: 热
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并建模将功率转换为热量的损耗效应。

### 主

### **Number of stator phases** — 四相或五相 SRM `Four-phase`（默认）| `Five-phase` | `Six-phase`

以定子相数表示的多相 SRM 类型。

### **Number of rotor poles** — 转子极数 `8`（默认）| 正整数

转子上的极对数。

### **Stator resistance per phase** — 电阻 `3` `Ohm`（默认）| 正标量

每个定子绕组的每相电阻。

### **Stator parameterization** — 参数化方法 `Specify saturated flux linkage`（默认）| `Specify flux characteristic`

定子参数化的方法。

#### 依赖关系

选择 `Specify saturated flux linkage` 会启用以下参数：

- **Saturated flux linkage**
- **Aligned inductance**
- **Unaligned inductance**

选择 `Specify flux characteristic` 会启用以下参数：

- **Current vector, i**
- **Angle vector, theta**
- **Flux linkage matrix, Phi(i,theta)**

### **Saturated flux linkage** — 磁链 `0.43` `Wb`（默认）| 正标量

每相饱和磁链。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify saturated flux linkage`。

### **Aligned inductance** — 电感 `0.0046` `H`（默认）| 正标量

当转子极轴线与励磁定子极轴线重合时的电感。此参数的值必须大于 **Unaligned inductance** 参数的值。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify saturated flux linkage`。

### **Unaligned inductance** — 电感 `6.7e-4` `H`（默认）| 正标量

当两个转子极之间的轴线与励磁定子极轴线重合时的电感。此参数的值必须小于 **Aligned inductance** 参数的值。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify saturated flux linkage`。

### **Current vector, i** — 电流 `[0, 50, 100]` `A`（默认）| 正向量

用于标识磁链曲线族的电流向量。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify flux characteristic`。

### **Angle vector, theta** — 角度 `[0, 22.5, 45]` `deg`（默认）| 正向量

用于标识磁链曲线族的角度向量。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify flux characteristic`。

### **Flux linkage matrix, Phi(i,theta)** — 磁链 `[0, 0, 0; .37, .06, .37; .43, .1, .43]` `Wb`（默认）| 标量

定义磁链曲线族的磁链矩阵。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify flux characteristic`。

### 铁损

有关计算铁损的详细信息，请参阅 Calculating Iron Losses。

### **Model** — 铁损建模选项 `None`（默认）| `Tabulate losses from current and speed` | `Tabulate losses from current, speed, and angle`

是否启用铁损建模。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify tabulated flux data`。

### **Magnetizing resistance** — 铁损的励磁电阻 `inf` `Ohm`（默认）

励磁电阻。该值必须大于零。默认值为 `inf`，表示没有铁损。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify parametric data`。

### **Rotor speed vector, w** — 转子速度 `[500, 1000, 1500]` `rpm`（默认）

用于制表铁损的转子速度向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed` 或 `Tabulate losses from current, speed, and angle`。

### **Iron loss table, Ploss(i,w)** — 基于电流和速度制表的铁损表 `zeros(3, 3)` `W`（默认）

由于特定相中的铁损而在轴上损失的机械功率，作为瞬时相电流和转子速度的函数制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed`。

### **Iron loss table, Ploss(i,w,theta)** — 基于电流、速度和角度制表的铁损表 `zeros(3, 3, 2)` `W`（默认）

由于特定相中的铁损而在轴上损失的机械功率，作为瞬时相电流、转子速度和转子角度的函数制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current, speed, and angle`。

### 机械

### **Rotor inertia** — 惯量 `0.01` `kg*m^2`（默认）| 正标量

连接到机械平移端口 **R** 的转子的惯量。

### **Rotor Damping** — 阻尼 `0` `N*m/(rad/s)`（默认）| 标量

旋转阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认）| 实标量

引用电机参数时的温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是使温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是使转子温度升高一度所需的能量。

### **Percentage of total iron losses associated with the rotor** — 总铁损百分比 `50`（默认）

与转子关联的总铁损百分比。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed` 或 `Tabulate losses from current, speed, and angle`。
## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

四相、五相或六相开关磁阻电机（SRM）

Switched Reluctance Machine (Multi-Phase) 模块表示四相、五相或六相开关磁阻电机（SRM）。

此图显示了四相电机的电机结构。

此图显示了五相电机的电机结构。

此图显示了六相电机的电机结构。

### 方程

多相电机的转子行程角为

θst=2πNsNr

其中：

- *θst* 是行程角。
- *Ns* 是相数。
- *Nr* 是转子极数。

一个转子极的转矩产生能力 *β* 为

β=2πNr。

开关磁阻电机（SRM）的数学模型由于磁饱和对磁链-角度曲线 *λ*(*θph*) 的影响而高度非线性。SRM 的相电压方程为

vph=Rsiph+dλph(iph,θph)dt

其中：

- *vph* 是每相电压。
- *Rs* 是每相定子电阻。
- *iph* 是每相电流。
- *λph* 是每相磁链。
- *θph* 是每相角度。

将相电压方程用偏导数重写得到以下方程：

vph=Rsiph+∂λph∂iphdiphdt+∂λph∂θphdθphdt。

瞬态电感定义为

Lt(iph,θph)=∂λph(iph,θph)∂iph，

或更简单地表示为

∂λph∂iph。

反电动势定义为

Eph=∂λph∂θphωr。

将这些项代入重写的电压方程得到以下电压方程：

vph=Rsiph+Lt(iph,θph)diphdt+Eph。

将共能公式应用于转矩方程，

Tph=∂W(θph)∂θr，

和能量方程，

W(iph,θph)=∫0iphλph(iph,θph)diph

得到一个定义每相瞬时转矩的积分方程，即

Tph (iph,θph)=∫0iph∂λph(iph,θph)∂θphdiph。

对各相积分得到以下方程，它定义总瞬时转矩为

T=∑j=1NsTph(j)。

运动方程为

Jdωdt=T−TL−Bmω

其中：

- *J* 是转子惯量。
- *ω* 是机械旋转速度。
- *T* 是转子转矩。对于 Switched Reluctance Machine 模块，转矩从机器壳体（模块守恒端口 **C**）流向机器转子（模块守恒端口 **R**）。
- *TL* 是负载转矩。
- *J* 是转子惯量。
- *Bm* 是转子阻尼。

对于高保真建模和控制开发，使用经验数据和有限元计算来确定以电流和角度表示的磁链曲线，即

λph(iph,θph)。

对于低保真建模，您也可以使用分析技术来近似该曲线。其中一种技术 [2] 使用以下指数函数：

λph(iph,θph)=λsat(1−e−iphf(θph))，

其中：

- *λsat* 是饱和磁链。
- *f*(*θr*) 通过傅里叶展开获得。

对于傅里叶展开，使用以下方程的前两个偶次项：

f(θph)=a+bcos(Nrθph)

其中 *a* > *b*，

a= Lmin+Lmax2λsat，

以及

b= Lmax−Lmin2λsat。

### 计算铁损

Switched Reluctance Machine (Multi-Phase) 模块将铁损实现为电磁转矩的减少。

如果将 **Stator parameterization** 参数设置为 `Specify parametric data`，请指定 **Magnetizing resistance** 参数来建模铁损。

如果将 **Stator parameterization** 参数设置为 `Specify tabulated flux data`，模块将损耗制表为每个定子相中损失的功率。每个定子的损耗仅取决于该相中的定子电流、转子角度（几何上偏移到该相）和转子速度。转子的铁损功率按总铁损功率的百分比计算，如 **Percentage of total iron losses associated with the rotor** 参数中所指定。

如果按电流、速度和角度制表损耗，铁损转矩会减少通用“A”相的电磁转矩：

τelecA=τ(iA,θA)−τloss(iA,w,θA)

其中 τloss(iA,w,θA)=sign(w)Ploss(abs(iA),abs(w),θA)abs(w)+wmin 是转矩损耗，计算为机械功率损耗除以转子速度。*wmin* 是最小转子速度，等于 `1` `rad/s`。此值可防止转子速度等于 `0` 时出现除零。

如果仅按电流和速度的函数制表损耗，铁损转矩会减少通用“A”相的电磁转矩：

τloss(iA,w)=sign(w)Ploss(abs(iA),abs(w))abs(w)+wmin。

铁损作为转矩的减少施加到机械侧。如果从 FEM 结果创建铁损表 *Ploss*，FEM 工具可能将损失的功率表示为电功率而非机械功率。

总电磁转矩等于各相电磁转矩之和：

τelec=τelecA+τelecB+τelecC。

总耗散功率等于铁损和铜损之和：

Pdissipated=(τlossA+τlossB+τlossC)w+Raia2+Rbib2+Rcic2。

**带热端口的铁损**

如果暴露模块的热端口，每相中耗散的功率在电机和转子中充当热源：

PdissA=Raia2+PironAPdissB=Rbib2+PironBPdissC=Rcic2+PironCPdissR=PironR

转子中的铁损等于总铁损的百分比。此损耗保持恒定，不依赖于其他状态：

PironR=percentrotor100(τlossA+τlossB+τlossC)w。

然后剩余的铁损在不同定子相之间分配：

PironA=(1−percentrotor100)τlossA wPironB=(1−percentrotor100)τlossB wPironC=(1−percentrotor100)τlossC w

### 建模热效应

您可以公开热端口，以对将功率转换为热量的损耗效应进行建模。要公开热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参见 Simulating Thermal Effects in Rotational and Translational Actuators。

### 假设

零转子角度对应于与 *a* 相完全对齐的转子磁极，即峰值磁通。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参见 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参见 System Scaling by Nominal Values。
