---
type: simulink-block
title: 'PMSM (DQ0)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmsmdq0'
documentation_source_path: 'ref/pmsmdq0.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM (DQ0)

## 端口

### 守恒

### **d** — *d* 轴分量电气

与 *d* 轴分量关联的电气守恒端口。

### **q** — *q* 轴分量电气

与 *q* 轴分量关联的电气守恒端口。

### **0** — 零序分量电气

与零序分量关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Zero sequence** 设置为
`Include`。

### **R** — 电机转子机械

与电机转子关联的机械旋转守恒端口。

### **C** — 电机机壳机械

与电机机壳关联的机械旋转守恒端口。

### **HR** — 转子热端口热

与转子关联的热守恒端口。

#### 依赖

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HS** — 定子绕组热端口热

与定子绕组关联的热守恒端口。

#### 依赖

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并建模将功率转换为热量的损耗效应。

### 主

### **Modeling fidelity** — 建模保真度 `Constant Ld, Lq and PM`（默认）| `Tabulated Ld, Lq and PM`

选择模块的建模保真度：

- `Constant Ld, Lq and PM` — *Ld*、
  *Lq* 和 *PM* 值为常数。各自的参数定义其值。
- `Tabulated Ld, Lq and PM` — 模块使用以下方程从 DQ 电流查找表在线计算
  *Ld*、*Lq* 和 *PM*：

  Ld=f1(id,iq)

  Ld=f2(id,iq)

  λPM=f2(id,iq)

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ld, Lq, and L0`。

### **Number of pole pairs** — 转子上永磁极对数 `6`（默认）| 正标量

转子上永磁极的对数。

### **Permanent magnet flux linkage parameterization** — 永磁磁链的参数化选项 `Specify flux linkage`（默认）| `Specify torque constant` | `Specify back EMF constant`

永磁磁链的参数化选项。

### **Permanent magnet flux linkage** — 永磁磁链 `0.03` `Wb`（默认）

与任一 stator 绕组交链的峰值永磁磁链。

#### 依赖

要启用此参数，请将 **Permanent magnet flux linkage
parameterization** 设置为 `Specify flux linkage`，并将
**Modeling fidelity** 设置为 `Constant Ld, Lq and
PM`。

### **Torque constant** — 转矩常数 `0.18` `N*m/A`（默认）

与任一 stator 绕组相关的转矩常数。

#### 依赖

要启用此参数，请将 **Permanent magnet flux linkage
parameterization** 设置为 `Specify torque constant`，
并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and
PM`。

### **Back EMF constant** — 反电动势常数 `0.18` `V*s/rad`（默认）

与任一 stator 绕组相关的反电动势常数。

**注意**

反电动势常数是永磁体在各相单位转速下感应的峰值电压。

#### 依赖

要启用此参数，请将 **Permanent magnet flux linkage
parameterization** 设置为 `Specify back EMF
constant`，并将 **Modeling fidelity** 设置为
`Constant Ld, Lq and PM`。

### **Stator parameterization** — 定子的参数化选项 `Specify Ld, Lq, and L0`（默认）| `Specify Ls, Lm, and Ms`

定子的参数化选项。

### **Stator d-axis inductance, Ld** — 定子 *d* 轴电感 `0.00022` `H`（默认）

定子的 *d* 轴电感。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ld, Lq, and L0`，并将 **Modeling
fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Stator q-axis inductance, Lq** — 定子 *q* 轴电感 `0.00022` `H`（默认）

定子的 *q* 轴电感。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ld, Lq, and L0`，并将 **Modeling
fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）| 包含两个或更多值的向量

直轴电流向量。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ld, Lq, and L0`，并将 **Modeling
fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）| 包含两个或更多值的向量

交轴电流向量。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ld, Lq, and L0`，并将 **Modeling
fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Ld matrix, Ld(id,iq)** — Ld 矩阵 `0.0002 * ones(3, 3)` `H`（默认）| 标量矩阵

Ld 矩阵。此矩阵的行数必须等于 **Direct-axis current vector, iD**
参数的值。此矩阵的列数必须等于 **Quadrature-axis current
vector, iQ** 参数的值。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ld, Lq, and L0`，并将 **Modeling
fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Lq matrix, Lq(id,iq)** — Lq 矩阵 `0.0002 * ones(3, 3)` `H`（默认）| 标量矩阵

Lq 矩阵。此矩阵的行数必须等于 **Direct-axis current vector, iD**
参数的值。此矩阵的列数必须等于 **Quadrature-axis current
vector, iQ** 参数的值。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ld, Lq, and L0`，并将 **Modeling
fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Permanent magnet flux linkage, PM(id,iq)** — 永磁体磁链 `0.1 * ones(3, 3)` `Wb`（默认）| 标量矩阵

永磁体的磁链。此矩阵的行数必须等于 **Direct-axis current vector,
iD** 参数的值。此矩阵的列数必须等于 **Quadrature-axis current
vector, iQ** 参数的值。

#### 依赖

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld,
  Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq
  and PM`
- **Permanent magnet flux linkage parameterization** 为
  `Specify flux linkage`

### **Torque constant matrix, kt(id,iq)** — 转矩常数矩阵 `0.18 * ones(3, 3)` `N*m/A`（默认）| 标量矩阵

转矩常数矩阵。此矩阵的行数必须等于 **Direct-axis current vector,
iD** 参数的值。此矩阵的列数必须等于 **Quadrature-axis
current vector, iQ** 参数的值。

#### 依赖

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld,
  Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq
  and PM`
- **Permanent magnet flux linkage parameterization** 为
  `Specify torque constant`

### **Back EMF constant matrix, ke(id,iq)** — 永磁体磁链 `0.18 * ones(3, 3)` `V/(rad/s)`（默认）| 标量矩阵

反电动势常数矩阵。此矩阵的行数必须等于 **Direct-axis current vector,
iD** 参数的值。此矩阵的列数必须等于 **Quadrature-axis
current vector, iQ** 参数的值。

#### 依赖

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld,
  Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq
  and PM`
- **Permanent magnet flux linkage parameterization** 为
  `Specify back EMF constant`

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认）| 正标量

定子的零序电感。

#### 依赖

要启用此参数，请将 **Zero sequence** 设置为
`Include`。

### **Stator self-inductance per phase, Ls** — 每相定子自感 `0.0002` `H`（默认）| 正标量

三个 stator 绕组各自的自感平均值。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ls, Lm, and Ms`。

### **Stator inductance fluctuation, Lm** — 定子电感波动 `-0.0002` `H`（默认）| 标量

stator 绕组的自感和互感随转子角度波动的量。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ls, Lm, and Ms`。

### **Stator mutual inductance, Ms** — stator 绕组之间的平均互感 `0.00002` `H`（默认）| 标量

stator 绕组之间的平均互感。

#### 依赖

要启用此参数，请将 **Stator parameterization** 设置为
`Specify Ls, Lm, and Ms`。

### **Stator resistance per phase, Rs** — 每个 stator 绕组的电阻 `0.013` `Ohm`（默认）| 正标量

每个 stator 绕组的电阻。

### **Zero sequence** — 包含或排除零序项的选项 `Include`（默认）| `Exclude`

包含或排除零序项的选项。

- `Include` — 包含零序项。要优先考虑模型保真度，请使用此默认设置。使用此选项：

  - 对于使用 Partitioning 求解器的仿真会导致错误。
    有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
  - 启用 **Stator zero-sequence inductance, L0**
    参数。
- `Exclude` — 排除零序项。要优先考虑桌面仿真或实时部署的仿真速度，
  请选择此选项。

### 铁损

### **Model** — 启用铁损计算的选项 `None`（默认）| `Empirical`

启用铁损计算模型的选项。

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 由磁滞、涡流和附加损耗引起的开路铁损 `[0, 0, 0]` `W`（默认）| 包含三个非负元素的行向量

在 **Electrical frequency at
which losses determined** 参数中指定的频率下，分别由磁滞、涡流和附加损耗引起的开路铁损。

#### 依赖

要启用此参数，请将 **Model** 设置为
`Empirical`。

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 短路铁损 `[0, 0, 0]` `W`（默认）| 包含三个非负元素的行向量

在 **Electrical frequency at
which losses determined** 参数中指定的频率下，分别由磁滞、涡流和附加损耗引起的短路铁损。

#### 依赖

要启用此参数，请将 **Model** 设置为
`Empirical`。

### **Electrical frequency at which losses determined** — 确定损耗时的电气频率 `60` `Hz`（默认）| 正标量

模块测量开路和短路铁损时的电气频率。

#### 依赖

要启用此参数，请将 **Model** 设置为
`Empirical`。

### **Short-circuit RMS current for short-circuit iron losses** — 短路铁损对应的短路 RMS 电流 `95` `A`（默认）| 正标量

测量短路损耗时得到的短路 RMS 相电流。

#### 依赖

要启用此参数，请将 **Model** 设置为
`Empirical`。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2`（默认）| 非负标量

连接到机械平移端口 **R** 的转子惯量。

### **Rotor damping** — 旋转阻尼 `0` `N*m/(rad/s)`（默认）| 非负标量

旋转阻尼。

### 温度依赖性

### **Measurement temperature** — 模块引用电机参数时的温度 `298.15` `K`（默认）| 正标量

模块引用电机参数时的温度。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）| 非负标量

电阻与温度关系方程中的系数 α。有关详细信息，请参阅 Thermal Model for Actuator Blocks。默认值适用于铜。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Permanent magnet flux temperature coefficient** — 永磁磁通密度随温度变化的分数变化率 `-0.001` `1/K`（默认）| 非正标量

永磁磁通密度随温度变化的分数变化率。使用此参数可在温度升高时线性降低转矩和感应反电动势。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`。

### 热端口

### **Thermal mass for each stator winding** — 每个 stator 绕组的热质量 `100` `J/K`（默认）| 正标量

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Rotor thermal mass** — 转子的热质量 `200` `J/K`（默认）| 正标量

转子的热质量。此值是将转子温度升高一度所需的能量。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Percentage of main flux path iron losses associated with the rotor** — 主磁通路径上与转子相关的铁损百分比 `90`（默认）| 正标量

主磁通路径上与通过转子的磁路相关的铁损百分比。此参数决定模块将多少铁损加热归因于转子热端口 **HR** 和定子热端口 **HS**。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`，并在 **Iron
Losses** 选项卡中将 **Model** 设置为
`Empirical`。

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — 跨齿磁通路径上与转子相关的铁损百分比 `30`（默认）| 正标量

跨齿磁通路径上与通过转子的磁路相关的铁损百分比。此参数决定模块将多少铁损加热归因于转子热端口 **HR** 和定子热端口 **HS**。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`，并在 **Iron
Losses** 选项卡中将 **Model** 设置为
`Empirical`。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

永磁同步电机的直-交-零表示

PMSM (DQ0) 模块对具有三相定子的永磁同步电机 (PMSM) 的直-交-零 (dq0) 坐标系表示进行建模。使用此模块可对内置式永磁同步电机 (IPMSM)、表贴式永磁同步电机 (SPMSM)、横向磁通电机、轴向磁通（盘式）电机或 PMSM 伺服电机进行建模。

PMSM 具有永磁转子和绕线定子。您可以在牵引应用（如电动汽车 (EV)）和执行系统中使用这些电机。在执行系统中，PMSM 也称为*无刷伺服电机*。您通常将 PMSM 设计为正弦反电动势 (EMF) 波形。与具有梯形反电动势波形的无刷直流 (BLDC) 电机等电机相比，这种设计可减少不期望的高频机械和电流谐波。

使用此模块可对两种主要类型的 PMSM 进行建模：

- SPSM 或表贴式永磁 (SPM) 电机 — “S”表示转子磁体为表贴式。*Ld* 和 *Lq* 相等。
- IPSM 或内置式永磁 (IPM) 电机 — “I”表示转子磁体位于转子内部。*Ld* 和 *Lq* 不相等。

您还可以根据主磁通路径对 PMSM 进行分类。主磁通路径通常为径向，但也可以是轴向的，这会在相同物理尺寸的电机中产生更高的转矩。您可以使用 PMSM (DQ0) 模块对这两类 PMSM 进行建模。

**注意**

Simscape™ Electrical™ 包含多个可对同一类型电机或执行器进行建模的模块。请选择具有足够建模细节的模块，以回答您需要解决的工程设计问题。不要使用建模细节超出您需要的模块，因为高保真模型会减慢仿真速度，并且参数化更加复杂。

PMSM (DQ0) 等模块使用简单等效电路对具有固定系数或参数相关系数的电机进行建模。这些模型具有中等保真度。使用此模块可为执行系统（如机器人和机电一体化）中的控制或系统进行设计，以及在饱和与谐波对损耗影响较弱时进行效率预测。有关选择合适模块以适当保真度对电机进行建模的更多信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 方程

对模块电气方程应用 Park 变换可得到与转子角度无关的转矩表达式。

此方程定义了 Park 变换：

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5],

其中 *θe* 是电角度，等于 *Nθr*。*N* 是极对数。

该模块对定子绕组电压和电流使用 Park 变换，将其变换到 dq0 坐标系，该坐标系与转子角度无关：

[vdvqv0]=P[vavbvc]

[idiqi0]=P[iaibic]

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
- *T* 是转子转矩。转矩从端口 **C**（表示电机壳体）流向端口 **R**（表示电机转子）。

PMSM (DQ0) 模块使用 Park 变换的原始非正交实现。如果您尝试应用替代实现，dq0 电压和电流将得到不同的结果。

### 替代磁链参数化

您可以使用**永磁体磁链**参数通过反电动势常数或转矩常数来参数化电机。

反电动势常数是永磁体在各相单位转速下感应的峰值电压。峰值永磁体磁链与反电动势之间的关系为：

ke=Nψm.

一相的反电动势 *eph* 为：

eph=keω.

转矩常数是各相单位电流感应的峰值转矩。当两者均以 SI 单位表示时，转矩常数在数值上与反电动势常数相同：

kt=Nψm.

当 *Ld*=*Lq* 且所有三相电流平衡时，合成转矩 *T* 为：

T=32ktiq=32ktIpk,

其中 *Ipk* 是三相绕组中任一相的峰值电流。

因子 3/2 源于这是所有相转矩的稳态总和。因此，转矩常数 *kt* 也等于：

kt=23(TIpk),

其中 *T* 是在峰值线电流 *Ipk* 的平衡三相电流下测试时测得的总转矩。RMS 线电流为：

kt=23Tiline,rms.

### 计算铁耗

铁耗由两项组成，一项代表主磁化路径，另一项代表在弱磁运行期间变得活跃的跨齿尖路径。铁耗模型基于 [3]。

代表主磁化路径的项取决于感应的 RMS 定子线对中性点电压 Vmrms：

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

该项在空载运行期间占主导。*k* 是每赫兹 RMS 电压对应的反电动势常数。该项等于 k=Vmrms/f，其中 *f* 是电频率。右侧第一项是磁滞损耗，第二项是涡流损耗，第三项是附加损耗。该模块从您为开路磁滞、涡流和附加损耗指定的值推导出分子上的三个系数。

代表跨齿尖路径的项在建立去磁场时相关，可通过有限元分析短路测试确定。该项取决于与跨齿尖磁通相关的 RMS EMF，Vdrms\*：

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

该模块从您为短路磁滞、涡流和附加损耗指定的值推导出三个分子项。

### 建模热效应

您可以暴露热端口来对将功率转换为热量的损耗效应进行建模。要暴露热端口，请将**建模选项**参数设置为以下值之一：

- `No thermal port` — 该模块包含与定子 dq0 量相关的电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子 dq0 量相关的电气守恒端口以及定子和转子的热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或属性检查器中的**标称值**部分。有关更多信息，请参阅 System Scaling by Nominal Values。
