---
type: simulink-block
title: 'Switched Reluctance Machine (Multi-Phase)'
family: 'electromechanical'
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

### 守恒

### **R** — Machine rotor mechanical rotational

与机器转子关联的机械旋转守恒端口。

**数据类型：** `double`

### **C** — Machine case mechanical rotational

与机器外壳关联的机械旋转守恒端口。

**数据类型：** `double`

### **a1** — *a*-phase positive supply electrical

相 *a* 的电气正电源。

**数据类型：** `double`

### **b1** — *b*-phase positive supply electrical

相 *b* 的电气正电源。

**数据类型：** `double`

### **c1** — *c*-phase positive supply electrical

相 *c* 的电气正电源。

**数据类型：** `double`

### **d1** — *d*-phase positive supply electrical

相 *d* 的电气正电源。

**数据类型：** `double`

### **e1** — *e*-phase positive supply electrical

相 *e* 的电气正电源。

如果为 **Number of stator phases** 参数选择 `Five-phase`，则此端口可见。

**数据类型：** `double`

### **f1** — *f*-phase positive supply electrical

相 *f* 的电气正电源。

如果为 **Number of stator phases** 参数选择 `Six-phase`，则此端口可见。

**数据类型：** `double`

### **a2** — *a*-phase negative supply electrical

相 *a* 的电气负电源。

**数据类型：** `double`

### **b2** — *b*-phase negative supply electrical

相 *b* 的电气负电源。

**数据类型：** `double`

### **c2** — *c*-phase negative supply electrical

相 *c* 的电气负电源。

**数据类型：** `double`

### **d2** — *d*-phase negative supply electrical

相 *d* 的电气负电源。

**数据类型：** `double`

### **e2** — *e*-phase negative supply electrical

相 *e* 的电气负电源。

如果为 **Number of stator phases** 参数选择 `Five-phase`，则此端口可见。

**数据类型：** `double`

### **f2** — *f*-phase negative supply electrical

相 *f* 的电气负电源。

如果为 **Number of stator phases** 参数选择 `Six-phase`，则此端口可见。

**数据类型：** `double`

### **HA** — *a*-phase terminal thermal port thermal

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b*-phase terminal thermal port thermal

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c*-phase terminal thermal port thermal

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HD** — *d*-phase terminal thermal port thermal

与定子绕组 *d* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HE** — *e*-phase terminal thermal port thermal

与定子绕组 *e* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`，并将 **Number of stator phases** 设置为 `Five-phase`。

### **HF** — *f*-phase terminal thermal port thermal

与定子绕组 *f* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`，并将 **Number of stator phases** 设置为 `Six-phase`。

### **HR** — Rotor thermal port thermal

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 主

### **Number of stator phases** — 四相或五相 SRM `Four-phase`（默认） | `Five-phase` | `Six-phase`

多相 SRM 的类型，依据定子相数。

### **Number of rotor poles** — 转子极 `8`（默认） | positive integer

转子上的极对数。

### **Stator resistance per phase** — 电阻 `3` `Ohm`（默认） | positive scalar

每个定子绕组的每相电阻。

### **Stator parameterization** — 参数化方法 `Specify saturated flux linkage`（默认） | `Specify flux characteristic`

定子参数化方法。

#### 依赖关系

选择 `Specify saturated flux linkage` 将启用以下参数：

- **Saturated flux linkage**
- **Aligned inductance**
- **Unaligned inductance**

选择 `Specify flux characteristic` 将启用以下参数：

- **Current vector, i**
- **Angle vector, theta**
- **Flux linkage matrix, Phi(i,theta)**

### **Saturated flux linkage** — 磁链 `0.43` `Wb`（默认） | positive scalar

每相饱和磁链。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify saturated flux linkage`。

### **Aligned inductance** — 电感 `0.0046` `H`（默认） | positive scalar

当转子极轴线与励磁定子极轴线重合时的电感。此参数的值必须大于 **Unaligned inductance** 参数的值。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify saturated flux linkage`。

### **Unaligned inductance** — 电感 `6.7e-4` `H`（默认） | positive scalar

当两个转子极之间的轴线与励磁定子极轴线重合时的电感。此参数的值必须小于 **Aligned inductance** 参数的值。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify saturated flux linkage`。

### **Current vector, i** — 电流 `[0, 50, 100]` `A`（默认） | positive vector

用于标识磁链曲线族的电流向量。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify flux characteristic`。

### **Angle vector, theta** — 角度 `[0, 22.5, 45]` `deg`（默认） | positive vector

用于标识磁链曲线族的角度向量。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify flux characteristic`。

### **Flux linkage matrix, Phi(i,theta)** — 磁链 `[0, 0, 0; .37, .06, .37; .43, .1, .43]` `Wb`（默认） | scalar

定义磁链曲线族的磁链矩阵。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify flux characteristic`。

### 铁耗

有关计算铁耗的详细信息，请参见 Calculating Iron Losses。

### **Model** — 铁耗建模选项 `None`（默认） | `Tabulate losses from current and speed` | `Tabulate losses from current, speed, and angle`

是否启用铁耗建模。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify tabulated flux data`。

### **Magnetizing resistance** — 用于铁耗的磁化电阻 `inf` `Ohm`（默认）

磁化电阻。该值必须大于零。默认值为 `inf`，这表示没有铁耗。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify parametric data`。

### **Rotor speed vector, w** — 转子速度 `[500, 1000, 1500]` `rpm`（默认）

编制铁耗表时所采用的转子速度向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed` 或 `Tabulate losses from current, speed, and angle`。

### **Iron loss table, Ploss(i,w)** — 基于电流和速度编制的铁耗表 `zeros(3, 3)` `W`（默认）

特定相中铁耗在轴上损失的机械功率，表示为瞬时相电流和转子速度的函数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed`。

### **Iron loss table, Ploss(i,w,theta)** — 基于电流、速度和角度编制的铁耗表 `zeros(3, 3, 2)` `W`（默认）

特定相中铁耗在轴上损失的机械功率，表示为瞬时相电流、转子速度和转子角度的函数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current, speed, and angle`。

### 机械

### **Rotor inertia** — 惯量 `0.01` `kg*m^2`（默认） | positive scalar

连接到机械平移端口 **R** 的转子惯量。

### **Rotor Damping** — 阻尼 `0` `N*m/(rad/s)`（默认） | scalar

旋转阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认） | real scalar

电机参数所对应的温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认） | positive scalar

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认） | positive scalar

每个定子绕组的热质量值。热质量是使温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认） | positive scalar

转子的热质量。热质量是使转子温度升高一度所需的能量。

### **Percentage of total iron losses associated with the rotor** — 总铁耗百分比 `50`（默认）

与转子相关的总铁耗百分比。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate losses from current and speed` 或 `Tabulate losses from current, speed, and angle`。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

四相、五相或六相开关磁阻电机（SRM）

Switched Reluctance Machine (Multi-Phase) 模块表示四相、五相或六相开关磁阻电机（SRM）。

此图显示四相电机的电机结构。

此图显示五相电机的电机结构。

此图显示六相电机的电机结构。

### 方程

多相电机的转子步进角为

θst=2πNsNr

其中：

- *θst* 是步进角。
- *Ns* 是相数。
- *Nr* 是转子极数。

一个转子极的转矩产生能力 *β* 为

β=2πNr.

开关磁阻电机（SRM）的数学模型高度非线性，因为磁饱和会影响磁链-角度曲线 *λ*(*θph*)。SRM 的相电压方程为

vph=Rsiph+dλph(iph,θph)dt

其中：

- *vph* 是每相电压。
- *Rs* 是每相定子电阻。
- *iph* 是每相电流。
- *λph* 是每相磁链。
- *θph* 是每相角度。

用偏导数改写相电压方程，得到以下方程：

vph=Rsiph+∂λph∂iphdiphdt+∂λph∂θphdθphdt.

瞬态电感定义为

Lt(iph,θph)=∂λph(iph,θph)∂iph,

或更简单地表示为

∂λph∂iph.

反电动势定义为

Eph=∂λph∂θphωr.

将这些项代入改写后的电压方程，得到以下电压方程：

vph=Rsiph+Lt(iph,θph)diphdt+Eph.

将共能公式应用于转矩方程，

Tph=∂W(θph)∂θr,

和能量，

W(iph,θph)=∫0iphλph(iph,θph)diph

得到一个定义每相瞬时转矩的积分方程，即，

Tph (iph,θph)=∫0iph∂λph(iph,θph)∂θphdiph.

对各相积分得到以下方程，其将总瞬时转矩定义为

T=∑j=1NsTph(j).

运动方程为

Jdωdt=T−TL−Bmω

其中：

- *J* 是转子惯量。
- *ω* 是机械旋转速度。
- *T* 是转子转矩。对于 Switched Reluctance Machine 模块，转矩从机器外壳（模块守恒端口 **C**）流向机器转子（模块守恒端口 **R**）。
- *TL* 是负载转矩。
- *J* 是转子惯量。
- *Bm* 是转子阻尼。

对于高保真建模和控制开发，使用经验数据和有限元计算来确定以电流和角度表示的磁链曲线，即，

λph(iph,θph).

对于低保真建模，还可以使用分析技术来近似该曲线。其中一种技术 [2] 使用以下指数函数：

λph(iph,θph)=λsat(1−e−iphf(θph)),

其中：

- *λsat* 是饱和磁链。
- *f*(*θr*) 通过傅里叶展开获得。

对于傅里叶展开，使用以下方程的前两个偶次项：

f(θph)=a+bcos(Nrθph)

其中 *a* > *b*，

a= Lmin+Lmax2λsat,

以及

b= Lmax−Lmin2λsat.

### 计算铁耗

Switched Reluctance Machine (Multi-Phase) 模块将铁耗实现为电气转矩的减少。

如果将 **Stator parameterization** 参数设置为 `Specify parametric data`，请指定 **Magnetizing resistance** 参数以对铁耗建模。

如果将 **Stator parameterization** 参数设置为 `Specify tabulated flux data`，模块将损耗制表为每个定子相中损失的功率。每个定子的损耗仅取决于该相中的定子电流、转子角度（几何上移位到该相）和转子速度。转子的铁耗功率按总铁耗功率的百分比计算，该百分比由 **Percentage of total iron losses associated with the rotor** 参数指定。

如果按电流、速度和角度编制损耗表，则铁耗转矩会降低通用“A”相的电气转矩：

τelecA=τ(iA,θA)−τloss(iA,w,θA)

其中 τloss(iA,w,θA)=sign(w)Ploss(abs(iA),abs(w),θA)abs(w)+wmin 是转矩损耗，按机械功率损耗除以转子速度计算。*wmin* 是最小转子速度，等于 `1` `rad/s`。当转子速度等于 `0` 时，此值可防止除以零。

如果仅根据电流和速度编制损耗表，则铁耗转矩会降低通用“A”相的电气转矩：

τloss(iA,w)=sign(w)Ploss(abs(iA),abs(w))abs(w)+wmin.

铁耗作为转矩减少施加到机械侧。如果根据 FEM 结果创建铁耗表 *Ploss*，FEM 工具可能将损失功率表示为电功率而不是机械功率。

总电气转矩等于各相电气转矩之和：

τelec=τelecA+τelecB+τelecC.

总耗散功率等于铁耗与铜耗之和：

Pdissipated=(τlossA+τlossB+τlossC)w+Raia2+Rbib2+Rcic2.

**带热端口的铁耗**

如果公开模块的热端口，则每相中耗散的功率在电机和转子中充当热源：

PdissA=Raia2+PironAPdissB=Rbib2+PironBPdissC=Rcic2+PironCPdissR=PironR

转子中的铁耗等于总铁耗的某个百分比。该损耗保持恒定，不依赖于其他状态：

PironR=percentrotor100(τlossA+τlossB+τlossC)w.

然后，剩余铁耗分配到不同定子相中：

PironA=(1−percentrotor100)τlossA wPironB=(1−percentrotor100)τlossB wPironC=(1−percentrotor100)τlossC w

### 热效应建模

您可以公开热端口，以便对将功率转换为热量的损耗效应进行建模。要公开热端口，请将 **建模选项** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅旋转和平移执行器中的热效应仿真。

### 假设

零转子角度对应于与 *a* 相完全对齐的转子磁极，即峰值磁通。

### 变量

若要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅按标称值进行系统缩放。
