---
type: simulink-block
title: 'Battery Single Particle'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Electrochemical Cell Modeling'
documentation_page: 'batterysingleparticle'
documentation_source_path: 'ref/batterysingleparticle.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Single Particle

## 端口

### 守恒

### **+** — 正极端子电气

与电池正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电池负极端子关联的电气守恒端口。

### **H** — 电池热质量热

与电池热质量关联的热守恒端口。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。从 Simulink® 工具条，在 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **所有表格的外推方法** — 表格的外推方法 `Nearest`（默认） | `Linear` | `Error`

表格参数的外推方法：

- `Linear` — 通过在已知数据的末端创建切线并将其延伸到该范围之外，估计超出数据的值。
- `Nearest` — 在查询点处外推，取最近样本网格点处的值。
- `Error` — 如果值超出已知数据，则返回错误。如果选择此选项，模块不使用外推。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ExtrapolationMethod` |
| **值：** | `"nearest"`（默认） | `"linear"` | `"error"` |

### 几何

### **负极厚度** — 负极的厚度 `3.4E-5` `m`（默认） | 正标量

负极的厚度。

### **负极的电解质层数** — 负极的电解质层数 `10`（默认） | 大于 3 的标量

负极的电解质层数。

### **隔膜厚度** — 隔膜的厚度 `2.5E-5``m`（默认） | 正标量

隔膜的厚度。

### **隔膜的电解质层数** — 隔膜的电解质层数 `5`（默认） | 大于 3 的标量

隔膜的电解质层数。

### **正极厚度** — 正极的厚度 `8E-5``m`（默认） | 正标量

正极的厚度。

### **正极的电解质层数** — 正极的电解质层数 `10`（默认） | 大于 3 的标量

正极的电解质层数。

### **电极板面积** — 电极板的面积 `1.8E-1``m^2`（默认） | 正标量

电极板的面积。

### **负极颗粒半径** — 负极的颗粒半径 `5E-6``m`（默认） | 正标量

负极的颗粒半径。

### **负极壳层数** — 负极的壳层数 `10`（默认） | 大于 3 的正标量

负极的壳层数。

### **正极颗粒半径** — 正极的颗粒半径 `5E-8``m`（默认） | 正标量

正极的颗粒半径。

### **正极壳层数** — 正极的壳层数 `10`（默认） | 大于 3 的正标量

正极的壳层数。

### 电极属性

### **负极活性材料的体积分数** — 负极中活性材料的体积分数 `0.58`（默认） | 范围 (0,1) 内的标量

负极中活性材料的体积分数。

### **正极活性材料的体积分数** — 正极中活性材料的体积分数 `0.374`（默认） | 范围 (0,1) 内的标量

正极中活性材料的体积分数。

### **化学计量断点规格** — 用于指定化学计量断点的选项 `Normalized`（默认） | `Absolute`

*自 R2025a 起*

用于指定化学计量断点的选项。将此参数设置为 `Normalized`，以指定归一化到相对化学计量的开路电位。将此参数设置为 `Absolute`，以指定归一化到绝对化学计量的开路电位。

### **归一化化学计量断点** — 电极开路电位的归一化化学计量断点 `linspace(0.025, 0.975, 39)`（默认） | 范围 [0,1] 内的元素向量

用于电极开路电位的归一化化学计量断点。此参数的大小必须等于 **相对于归一化化学计量的负极开路电位** 和 **相对于归一化化学计量的正极开路电位** 参数的大小。

**注意**

`0` 的值表示颗粒的化学计量等于电极的最小化学计量，如您在 **负极最小化学计量** 和 **正极最小化学计量** 参数中所指定的。`1` 的值表示颗粒的化学计量等于电极的最大化学计量，如您在 **负极最大化学计量** 和 **正极最大化学计量** 参数中所指定的。

总体而言，模块使用以下方程计算归一化化学计量的值：

NormalizedSurfaceStoichiometry = ElectrodeStoichiometry(end) - MinimumStoichiometryMaximumStoichiometry - MinimumStoichiometry.

#### 依赖关系

要启用此参数，请将 **化学计量断点规格** 设置为 `Normalized`。

### **相对于归一化化学计量的负极开路电位** — 负极相对于归一化化学计量的开路电位 `[.435; .325; .259; .221; .204; .194; .179; .166; .155; .145; .137; .131; .128; .127; .126; .125; .124; .123; .122; .121; .118; .117; .112; .109; .105; .1; .098; .095; .094; .093; .091; .09; .089; .088; .087; .086; .085; .084; .083]` `V`（默认） | 正元素向量

*自 R2025a 起*

负极相对于归一化化学计量的开路电位。此参数的大小必须等于 **归一化化学计量断点** 参数的大小。

#### 依赖关系

要启用此参数，请将 **化学计量断点规格** 设置为 `Normalized`。

### **相对于归一化化学计量的正极开路电位** — 正极相对于归一化化学计量的开路电位 `[3.598; 3.53; 3.494; 3.474; 3.46; 3.455; 3.454; 3.453; 3.4528; 3.4526; 3.4524; 3.452; 3.4518; 3.4516; 3.4514; 3.4512; 3.451; 3.4508; 3.4506; 3.4503; 3.45; 3.4498; 3.4495; 3.4493; 3.449; 3.4488; 3.4486; 3.4484; 3.4482; 3.4479; 3.4477; 3.4475; 3.4473; 3.447; 3.4468; 3.4466; 3.4464; 3.4462; 3.4458]` `V`（默认） | 正元素向量

*自 R2025a 起*

正极相对于归一化化学计量的开路电位。此参数的大小必须等于 **归一化化学计量断点** 参数的大小。

#### 依赖关系

要启用此参数，请将 **化学计量断点规格** 设置为 `Normalized`。

### **绝对负极化学计量断点** — 负极开路电位的绝对化学计量断点 `linspace(0.025, 0.975, 39)`（默认） | 范围 [0,1] 内的元素向量

*自 R2025a 起*

负极开路电位的绝对化学计量断点。此参数的大小必须等于 **相对于绝对化学计量的负极开路电位** 参数的大小。

#### 依赖关系

要启用此参数，请将 **化学计量断点规格** 设置为 `Absolute`。

### **相对于绝对化学计量的负极开路电位** — 负极相对于绝对化学计量的开路电位 `[.484; .335; .253; .209; .2; .181; .165; .151; .139; .131; .128; .125; .124; .124; .123; .122; .119; .117; .111; .108; .101; .098; .095; .093; .092; .088; .088; .088; .088; .087; .087; .087; .085; .082; .079; .071; .064; .049; .026]` `V`（默认） | 正元素向量

*自 R2025a 起*

负极相对于绝对化学计量的开路电位。此参数的大小必须等于 **绝对负极化学计量断点** 参数的大小。

#### 依赖关系

要启用此参数，请将 **化学计量断点规格** 设置为 `Absolute`。

### **绝对正极化学计量断点** — 正极开路电位的绝对化学计量断点 `linspace(0.025, 0.975, 39)`（默认） | 范围 [0,1] 内的元素向量

*自 R2025a 起*

正极开路电位的绝对化学计量断点。此参数的大小必须等于 **相对于绝对化学计量的正极开路电位** 参数的大小。

#### 依赖关系

要启用此参数，请将 **化学计量断点规格** 设置为 `Absolute`。

### **相对于绝对化学计量的正极开路电位** — 正极相对于绝对化学计量的开路电位 `[3.81; 3.608; 3.512; 3.478; 3.459; 3.453; 3.45257; 3.45214; 3.45171; 3.45128; 3.45085; 3.45042; 3.44999; 3.44956; 3.44913; 3.4487; 3.44827; 3.44784; 3.44741; 3.44698; 3.44655; 3.44612; 3.44569; 3.44526; 3.44483; 3.4444; 3.44397; 3.44354; 3.44311; 3.44268; 3.44225; 3.44182; 3.44139; 3.44096; 3.44053; 3.44; 3.412; 3.304; 2.968]` `V`（默认） | 正元素向量

*自 R2025a 起*

正极相对于绝对化学计量的开路电位。此参数的大小必须等于 **绝对正极化学计量断点** 参数的大小。

#### 依赖关系

要启用此参数，请将 **化学计量断点规格** 设置为 `Absolute`。

### **负极最大离子浓度** — 负极中的最大离子浓度 `30555` `mol/m^3`（默认） | 正标量

负极中的最大离子浓度。

### **负极最大化学计量** — 负极中的最大化学计量 `0.811`（默认） | 正标量

负极中的最大化学计量。此参数的值必须大于 **负极最小化学计量** 参数的值。

### **负极最小化学计量** — 负极中的最小化学计量 `0.0132`（默认） | 正标量

负极中的最小化学计量。此参数的值必须小于 **负极最大化学计量** 参数的值。

### **正极最大离子浓度** — 正极中的最大离子浓度 `22806` `mol/m^3`（默认） | 正标量

正极中的最大离子浓度。

### **正极最大化学计量** — 正极中的最大化学计量 `0.74`（默认） | 正标量

正极中的最大化学计量。此参数的值必须大于 **正极最小化学计量** 参数的值。

### **正极最小化学计量** — 正极中的最小化学计量 `0.035`（默认） | 正标量

正极中的最小化学计量。此参数的值必须小于 **正极最大化学计量** 参数的值。

### **负极活性材料的扩散系数** — 负极中活性材料的扩散系数 `3E-15` `m^2/s`（默认） | 正标量

负极中活性材料的扩散系数。

### **正极活性材料的扩散系数** — 正极中活性材料的扩散系数 `5.9E-20` `m^2/s`（默认） | 正标量

正极中活性材料的扩散系数。

### **负极电导率** — 负极的电导率 `100` `S/m`（默认） | 正标量

负极的电导率。

### **正极电导率** — 正极的电导率 `0.5` `S/m`（默认） | 正标量

正极的电导率。

### **集流体电阻** — 集流体的电阻 `0` `Ohm`（默认） | 非负标量

集流体的电阻。

### 电解质属性

### **负极中电解质的体积分数** — 负极中电解质的体积分数 `0.3874`（默认） | 范围 (0,1) 内的标量

负极中电解质的体积分数。

### **隔膜中电解质的体积分数** — 隔膜中电解质的体积分数 `0.45`（默认） | 范围 (0,1) 内的标量

隔膜中电解质的体积分数。

### **正极中电解质的体积分数** — 正极中电解质的体积分数 `0.5725`（默认） | 范围 (0,1) 内的标量

正极中电解质的体积分数。

### **电解质电导率** — 电解质的电导率 `0.29` `S/m`（默认） | 正标量

电解质的电导率。

### **负极 Bruggeman 指数** — 负极的 Bruggeman 指数 `1.5`（默认） | 大于或等于 1 的标量

负极的 Bruggeman 指数。

### **隔膜 Bruggeman 指数** — 隔膜的 Bruggeman 指数 `1.5`（默认） | 大于或等于 1 的标量

隔膜的 Bruggeman 指数。

### **正极 Bruggeman 指数** — 正极的 Bruggeman 指数 `1.5`（默认） | 大于或等于 1 的标量

正极的 Bruggeman 指数。

### **迁移数** — 离子在电解质中携带的总电流分数 `0.363`（默认） | 范围 [0,1] 内的标量

离子在电解质中携带的总电流分数。

### **电解质扩散系数** — 电解质的扩散系数 `2E-10` `m^2/s`（默认） | 正标量

模块在菲克定律方程中使用的电解质扩散系数。

### 反应动力学

### **负极的电荷转移速率常数** — 负极的电荷转移速率常数 `8.8E-11` `m^(5/2)/(mol^(1/2)*s)`（默认） | 正标量

负极的电荷转移速率常数。模块在 Butler-Volmer 方程中使用此值来模拟电极-电解质界面处的电化学动力学。

### **正极的电荷转移速率常数** — 正极的电荷转移速率常数 `2.8E-13` `m^(5/2)/(mol^(1/2)*s)`（默认） | 正标量

正极的电荷转移速率常数。模块在 Butler-Volmer 方程中使用此值来模拟电极-电解质界面处的电化学动力学。

### 热

### **电池热质量** — 与热端口关联的电池热质量 `77` `J/K`（默认） | 正标量

热端口 **H** 处的热质量。此参数表示将热端口温度升高 1 kelvin 所需的能量。

### **Arrhenius 参考温度** — Arrhenius 参考温度 `298.15` `K`（默认） | 正标量

Arrhenius 参考温度。

### **负极活性材料中扩散的活化能** — 负极活性材料内部扩散的活化能 `39000` `J/mol`（默认） | 正标量

负极活性材料内部扩散的活化能。

### **正极活性材料中扩散的活化能** — 正极活性材料内部扩散的活化能 `35000` `J/mol`（默认） | 正标量

正极活性材料内部扩散的活化能。

### **电解质中扩散的活化能** — 电解质内部扩散的活化能 `26600` `J/mol`（默认） | 正标量

电解质内部扩散的活化能。

### **负极中传导的活化能** — 负极内部传导的活化能 `3000` `J/mol`（默认） | 正标量

负极内部传导的活化能。

### **正极中传导的活化能** — 正极内部传导的活化能 `3000` `J/mol`（默认） | 正标量

正极内部传导的活化能。

### **电解质中传导的活化能** — 电解质内部传导的活化能 `11000` `J/mol`（默认） | 正标量

电解质内部传导的活化能。

### **负极中电荷转移的活化能** — 负极内部电荷转移的活化能 `13000` `J/mol`（默认） | 正标量

负极内部电荷转移的活化能。

### **Activation energy for charge transfer in Cathode** — 阴极内部电荷转移的活化能 `20000` `J/mol`（默认）| 正标量

阴极内部电荷转移的活化能。

### 故障

### **Additional resistance fault** — 用于对串联电阻设置故障的选项 `Add fault`

*自 R2025a 起*

用于对串联电阻设置故障的选项。如果附加电阻大于 1000 ohm，或存在异常内阻，可使用此故障对开路电池建模。

要添加故障，请点击 **Add fault** 超链接。

### **Additional resistance when faulted** — 模块发生故障时的附加电阻 `1e5` `Ohm`（默认）| 正标量

*自 R2025a 起*

当模块处于故障状态时附加电阻的值。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 故障触发类型 `Always On`（默认）| `Timed` | `Additional triggers` | `Conditional` | `Manual`

*自 R2025a 起*

故障触发类型。选择以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Additional triggers` — 故障由于模块对话框中不可用的附加触发器而注入。选择此选项，然后点击 **Open fault properties** 超链接，以在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由于反映与信号相关行为的条件而注入。条件在每个时间步计算 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件第一次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。要了解更多信息，请参阅创建和管理条件。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅在模型中手动触发故障。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

*自 R2025a 起*

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Trigger Configuration** — 为放热反应故障启用附加触发类型的选项 `Open fault properties`

*自 R2025a 起*

用于启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional Triggers`。

## 所属库

Simscape / Battery / Cells

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：注入附加电阻故障并配置故障行为

Battery Single Particle 模块现在支持用于对故障建模的新接口。此接口将系统模型文件与存储故障信息的文件分开。当附加串联电阻很高（大于 1000 ohm）或存在异常内阻时，您可以系统地将其建模为开路电池的故障。您还可以安全地将标称模型行为与故障模型行为分开，以避免安全任务干扰设计任务。有关详细信息，请参阅 Simscape 故障简介。

### R2025a：指定归一化到绝对化学计量比的开路电位

新的 **Stoichiometry breakpoints specification** 参数允许您指定归一化到相对或绝对化学计量比的电极开路电位。要指定归一化到绝对化学计量比的开路电位，请将 **Stoichiometry breakpoints specification** 设置为 `Absolute`。随后模块会公开以下四个参数：

- **Absolute anode stoichiometry breakpoints**
- **Anode open-circuit potential relative to absolute stoichiometry**
- **Absolute cathode stoichiometry breakpoints**
- **Cathode open-circuit potential relative to absolute stoichiometry**

## 描述

采用单粒子方法的电池模型

Battery Single Particle 模块使用单粒子模型表示电池。此实现考虑液体电解质和固体电极相中的欧姆过电位和传质过电位。此外，它还考虑反应动力学和集流体电阻。

电池包括两个电极，即负极和正极，以及电极之间的多孔隔膜。在此模块中，*anode* 指放电时的负电极，*cathode* 指放电时的正电极。模块在一维框架中对电极和电解质的欧姆过电位，以及从负极集流体到正极集流体的电池横截面上的浓度进行建模。

下图展示了放电期间电解质中的代表性浓度。模型包括负极（*x*=[0 …
*L*-]）、隔膜
（*x*=[*L*- …
*L*-+*L*sep]）
和正极
（*x*=[*L*-+*L*sep…
*L*-+*L*sep+*L*+]）。

放电期间电解质中的代表性浓度。模型包括负极、隔膜和正极。

模块计算代表性球形颗粒中沿径向尺寸 *r* 的电极浓度。下图展示了电池连续放电期间代表性颗粒中的浓度梯度：

电池连续放电期间代表性颗粒中的浓度梯度。

### 固相中的物质守恒

当模块处于固相时，单粒子方法将正极和负电极建模为单个代表性球形颗粒。

**注意**

这些方程中的上标指代相应电极。*+* 上标指正极。*-* 上标指负极。*sep* 上标指隔膜。*±* 上标表示该方程同时适用于负极和正极。例如，*c+s* 是正极的固相浓度，*c-s* 是负极的固相浓度。

此方程使用 Fick 定律描述负电极或正电极中阳离子的浓度 *c*。模块仅使用径向坐标计算电极中的浓度。球形颗粒中的扩散驱动传质，

∂cs±∂t(r,t)=∂∂r[Ds±∂cs±∂r(r,t)],

其中：

- *cs* 是固相浓度。
- *Ds* 是固相扩散系数。
- *r* 是半径。
- *t* 是时间。

在颗粒中心，浓度梯度等于 0：

Ds±∂cs±∂r(0,t)=0.

此方程计算颗粒表面的离子浓度梯度：

Ds±∂cs±∂r(Rs±,t)=∓Js±as± F.

在此方程中，*F* 是 Faraday 常数，*J* 是摩尔通量，

J±(t)=I(t)A L±,

其中：

- *I* 是施加到电池的电流。
- *A* 是集流体的总面积。
- *L* 是相应电极的长度。

此外，*a* 是每电极单位体积的活性表面积，

a±=3ε±R±,

其中：

- *ε* 是电极的活性材料分数。
- *R* 是活性颗粒的总半径。

为求解微分方程，Battery Single Particle 模块将半径为 *R* 的颗粒离散为 *n* 个壳层。每个壳层与相邻球体的径向距离等于 δr=Rn。

对于第 *i* 个球体，此方程计算浓度变化率 *δc/δt*：

c˙si=Dsδr2{(i−1i)csi−1−2csi+(i+1i)csi+1}.

对于颗粒中最内层的壳层，模块实现此边界条件：

c˙1=2Dsδr2{cs2−cs1}.

为实现颗粒表面的边界条件，模块在表面周围添加一个附加节点。模块不计算此节点的浓度，因为它在物理上不存在。模块使用此节点，通过 Neumann 边界条件计算颗粒中最外层壳层与其周围不存在的壳层之间的边界条件。此方程描述了颗粒表面的离散化结果：

c˙send=2Dsδr2{csend−1−csend}−2n+1nJF A δr.

### 固相中的传质过电位

当模块处于固相时，开路电位取决于浓度。为计算电极处的传质过电位，Battery Single Particle 模块从表面平均相对浓度的开路电位中减去颗粒内平均相对浓度的开路电位，

η±diffusion,s=ocp±(cs,surface,relative±)−ocp±(c¯s,relative±),

其中：

- *η*diffusion,*s* 是固相传质过电位。
- *ocp(cs*,surface,relative*)* 是颗粒表面浓度的开路电位。
- *ocp(cs*relative*)* 是颗粒平均浓度的开路电位。

模块使用同一方程计算负极和正极的传质过电位。

### 固相中的欧姆过电位

为计算模块处于固相时的欧姆过电位，Battery Single Particle 模块将电极上的电流和集流体处的电流线性近似为等于施加到电池的电流的值。隔膜与电极之间的界面处电流为零。此方程定义固相中的欧姆过电位，

η±ohmic,s=Ibatt2A∗L±κ±,

其中：

- *ηohmic,s* 是固相欧姆过电位。
- *Ibatt/A* 是电池横截面。
- *L* 是相应电极的长度，取决于负极或正极的厚度。
- *κ* 是电导率。电导率取决于电池温度。当模块计算负极的欧姆过电位时，*κ* 等于 **Anode conductivity** 参数；当模块计算正极的欧姆过电位时，*κ* 等于 **Cathode conductivity** 参数。

模块使用同一方程计算负极和正极在固相中的欧姆过电位。

### 液相中的物质守恒

当模块处于液相时，该方程描述两个电极处以及隔膜处电解液中的浓度。为了计算穿过隔膜的浓度，模块考虑由浓度梯度引起的扩散流，

∂cε±∂t(x,t)=∂∂x[Dε∂cε±∂x(x,t)],

其中：

- *cε* 是电解液中的浓度。
- *Dε* 是液相中的扩散系数。
- *x* 是电池厚度方向上的位置，从负极集流体到正极集流体。
- *t* 是时间。

在正负电极处，模块同时考虑扩散流和从固体电极进入电解液的阳离子通量，

∈ε±∂cε±∂t(x,t)=∂∂x[Dεeff∂cε±∂x(x,t)±(1−t+0)JF],

其中：

- *∈* 是电解液的体积分数。
- *Deffε* 是考虑材料孔隙率的液相扩散系数。液体电解质的扩散率取决于周围固体电极材料的性质。电极包含多种组分，例如活性材料和填料，这些组分形成特征性多孔材料。
- *J* 是摩尔通量。
- *t+* 是阳离子的迁移数。
- *F* 是法拉第常数。

因为电解液是连续流体，负极和正极与隔膜交界处的阳离子浓度必须相等。对于负极-隔膜和正极-隔膜界面处电解液中的浓度，模块必须定义电池三个部分之间的边界条件。模块将两个电极和隔膜都表示为长方体。

该模块将电解液视为贯穿电极和隔膜的连续介质。由于界面两侧的浓度必须相等，因此电极与隔膜之间的界面存在连续性边界条件。

该方程描述负极与隔膜之间界面处浓度的连续性边界条件，

cε−(L−,t)=cεsep(L−,t),

其中：

- cε−(L−,t) 是负极与隔膜交界处负极中的浓度。
- cεsep(L−,t) 是负极与隔膜交界处隔膜中的浓度。

该方程描述隔膜与正极之间界面处浓度的连续性边界条件，

cεsep(L−+Lsep,t)=cε+(L−+Lsep,t),

其中：

- cεsep(L−+Lsep,t) 是隔膜与正极交界处隔膜中的浓度。
- cε+(L−+Lsep,t) 是隔膜与正极交界处正极中的浓度。

模块还对电极与隔膜之间的界面施加通量边界条件。界面两侧的通量必须相等，

Deff−∂cε−∂x(L−,t)=Deffsep∂cεsep∂x(L−,t)Deff+∂cε+∂x(L−+Lsep,t)=Deffsep∂cεsep∂x(L−+Lsep,t)

其中：

- Deff− 是负极的扩散系数。
- Deff+ 是正极的扩散系数。
- Deffsep 是隔膜的扩散系数。
- ∂cε−∂x(L−,t) 是负极与隔膜交界处负极的浓度梯度。
- ∂cεsep∂x(L−,t) 是负极与隔膜交界处隔膜的浓度梯度。
- ∂cε+∂x(L−+Lsep,t) 是正极与隔膜交界处正极的浓度梯度。
- ∂cεsep∂x(L−+Lsep,t) 是正极与隔膜交界处隔膜的浓度梯度。

该方程指定电极与集流体之间边界处的浓度。通量与集流体处的通量成比例；由于模块不在那里存储任何离子，该通量等于零。因此，界面处产生的通量为零，

∂cε−∂x(0,t)=∂cε+∂x(L−+Lsep+L+,t)=0,

其中：

- ∂cε−∂x(0,t) 是负极与最左侧集流体交界处负极中的浓度梯度。
- ∂cε+∂x(L−+Lsep+L+,t) 是正极与最右侧集流体交界处正极中的浓度梯度。

与固相类似，模块通过将电解液划分为 *n* 个大小相等的区段来求解微分方程。该方程表示第 *i* 个区段中的浓度，区段之间的距离为 *δx*，并且对区间 [1,Ms-1] 中的所有区段有效：

∂cε∂t(x,t)=Dε,eff±ci+1+ci−1−2ci∂x2+(1−t+0)JF.

模块使用以下方程对隔膜进行离散化：

∂cε∂t(x,t)=Dε,effsepci+1+ci−1−2ciδx2.

为计算电极与隔膜之间界面处的浓度，模块应用所有边界条件。例如，对于负极与隔膜之间的界面，模块应用以下方程：

cε,i=1sep=εε−εεsepcε,i=0−cε,i=−1sep∂x∂x−cε,i=0.

### 液相中的传质过电位

当模块处于液相时，它使用集流体与负极之间的界面处以及正极与集流体之间的界面处的浓度，通过以下方程计算电解液中的传质过电位，

ηdiffusion,ε=2RTF(1−tε0)lncε(L−+Lsep+L+,t)cε(0,t),

其中：

- *R* 是通用气体常数。
- *T* 是温度。
- *F* 是法拉第常数。

### 液相中的欧姆过电位

当模块处于液相时，它通过线性近似电池每个区段中的离子电流来计算欧姆过电位。对于电极，与集流体交界处的离子电流为零。在与隔膜的界面处，离子电流等于电池的电流 *Ibatt*。在隔膜两侧，模块将离子电流近似为常数，并等于施加到电池的电流。模块使用以下方程计算欧姆过电位

ηohmic,ε=−Ibatt2A∗(L+κeff++2Lsepκeffsep+L−κeff−),

其中 *κeff* 是有效电导率，模块通过使用 Bruggeman 系数来计算。有关有效参数的更多信息，请参阅有效电解液特性部分。

### 电荷转移过电位

为对电荷转移过电位建模，该模块使用 Butler-Volmer 方程。Butler-Volmer 方程描述电流密度 *j* 与过电位 *η* 之间的关系，*η* 是实际电极电位与热力学平衡电位之差。Butler-Volmer 方程为

J±(t)=j0,k(t)[exp(αnεFRTη±(t))−exp(−(1−α)nεFRTη±(t))],

其中：

- *α* 是氧化和还原的电荷转移系数。
- *j0* 是交换电流密度。

求解该方程以得到电极过电位，可得到以下方程：

ηkinetic,s=RTαFln(ξ±+(ξ±)2+1)ξ±=j±2a±i0±

*i±0* 是负极和正极中的交换电流密度，等于

i0±=k±[c¯ε±(cs,max±−cs,surf±)cs,surf±]α,

其中：

- *k* 是电荷转移速率常数，对于负极等于 **Charge transfer rate constant for Anode** 参数的值，对于正极等于 **Charge transfer rate constant for Cathode** 参数的值。
- c¯ε± 是平均电解液浓度。
- *cs,max* 是最大电极浓度。
- *cs,surf* 是电极表面浓度。

为计算完整电池的动力学过电位，模块从正极的动力学过电位中减去负极的动力学过电位：

ηkinetic,s=η+kinetic,s−η−kinetic,s.

### 集流体电阻

该模块将集流体电阻建模为单个电阻。您可以通过指定 **Current collector resistance** 参数来设置集流体电阻。

### 电池电压

为对电池电压建模，该模块使用以下方程考虑每个电极表面处的电位、各过电位以及由集流体电阻引起的电压损耗

V(t)=ocp+(csurface,relative+)−ocp−(csurface,relative−)+ηdiffusion,ε+ηohmic,ε+ηkinetic,s+ηohmic−+ηohmic++IbattRCurrentCollector,

其中：

- *ocp+(c+surface,relative)* 是正极颗粒表面处浓度对应的开路电位。
- *ocp-(c-surface,relative)* 是负极颗粒表面处浓度对应的开路电位。
- *η*diffusion,ε 是电解液中的传质过电位。
- *η*ohmic,ε 是电解液中的欧姆过电位。
- *η*kinetic,s 是电极中的电荷转移过电位。
- *η*-ohmic 是负极中的欧姆过电位。
- *η*+ohmic 是正极中的欧姆过电位。
- *I*batt 是电池电流。
- *R*CurrentCollector 是集流体的电阻。

您可以通过使用归一化或绝对化学计量断点，将开路电位参数化为表格数据：

- 如果将 **Stoichiometry breakpoints specification** 参数设置为 `Normalized`，则通过设置 **Anode open-circuit potential**、**Cathode open-circuit potential** 和 **Normalized stoichiometry breakpoints** 参数来指定归一化到相对化学计量的开路电位。负极和正极的化学计量断点相同。
- 如果将 **Stoichiometry breakpoints specification** 参数设置为 `Absolute`，则指定归一化到绝对化学计量的开路电位。使用此选项，您可以通过设置 **Absolute anode stoichiometry breakpoints** 和 **Absolute cathode stoichiometry breakpoints** 参数，分别指定负极和正极的化学计量断点。 *(自 R2025a 起)*

为计算相对浓度，模块考虑每个电极的最大浓度以及最大和最小化学计量。**Anode maximum ion concentration** 和 **Cathode maximum ion concentration** 参数表示每个电极理论上的最大可能浓度。为获得可达到的最大和最小浓度，模块分别将这些参数的值与 **Anode maximum stoichiometry**、**Anode minimum stoichiometry**、**Cathode maximum stoichiometry** 和 **Cathode minimum stoichiometry** 参数的值相乘。然后，模块使用以下方程计算相对浓度

cs,relative=cscs,max−ΝminΝmax−Νmin,

其中：

- *cs*,max 是最大浓度。
- *N*max 是最大化学计量。
- *N*min 是最小化学计量。

### 有效电解液特性

根据您要建模的多孔电极的微观结构设置这些参数的值：

- **Diffusion coefficient of electrolyte** — 将此参数设置为影响电解液中质量传输的电解液扩散系数值。
- **Electrolyte conductivity** — 将此参数设置为电解液的电导率值。

为对该依赖性建模，该模块使用 Bruggeman 关联式，

Parametereffective=Parameterblock∗φεα,

其中：

- *φε* 是电解液的体积分数。该值相应地等于 **Volume fraction of electrolyte in anode**、**Volume fraction of electrolyte in separator** 和 **Volume fraction of electrolyte in cathode** 参数的值。
- *α* 是 Bruggeman 指数。该值相应地等于 **Anode Bruggeman exponent**、**Separator Bruggeman exponent** 和 **Cathode Bruggeman exponent** 参数的值。

### 热

模块认为整个电池的温度恒定。这些模块参数取决于电池的温度：

- **Diffusion coefficient of anode active material** 和 **Diffusion coefficient of cathode active material** — 这些参数是影响电极中质量传输的电极扩散系数。
- **Diffusion coefficient of electrolyte** — 此参数是影响电解液中质量传输的电解液扩散系数。
- **Electrolyte conductivity** — 此参数是电解液的电导率。
- **Anode conductivity** 和 **Cathode conductivity** — 这些参数是电极的电导率。
- **Charge transfer rate constant for Anode** 和 **Charge transfer rate constant for Cathode** — 这些参数是电极的电荷转移速率常数。

为计算这些参数的温度调整值，模块使用 Arrhenius 方程，

ParameterT-adjusted=Parameterblock∗eEaR(1Tref−1T),

其中：

- *Parameterblock* 是温度相关参数的值。
- *Ea* 是活化能，等于 **Thermal** 设置中活化能参数的值。
- *Tref* 是 **Arrhenius reference temperature** 参数的值。
- *T* 是电池温度。

### 电池的热生成

该模块将电池建模为集总热质量。单粒子模型使用以下方程计算由过电位在电池中引起的不可逆发热：

Q=Ibatt(ηdiffusion,ε+ηohmic,ε+ηohmic,s−+ηohmic,s++IbattRCurrentCollector+ηkinetic,s+η+diffusion+η−diffusion).

### 故障建模

*自 R2025a 起*

要对 Battery Single Particle 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

当附加的串联电阻很高（大于 1000 ohm）或存在异常内阻时，Battery Single Particle 模块将该故障建模为开路电池。

**故障触发器**

您通过使用 **Trigger Type** 参数来指定故障如何以及何时发生。

如果将 **Trigger Type** 参数设置为 `Timed`，则当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，Battery Single Particle 模块触发故障事件。

如果将 **Trigger Type** 设置为 `Conditional`，您可以选择 Battery Single Particle 模块中的故障是否可逆 *(自 R2025a 起)*。要对不可逆故障建模，请单击 **Open fault properties** 以打开 Property Inspector，并选择 **Trigger stays on once activated** 参数。当触发条件第一次变为 true 时，模块进入故障状态，并在仿真的其余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入非故障状态。

有关向模块添加故障和指定故障触发器的更多信息，请参阅 Introduction to Simscape Faults。

### 公共变量

您可以使用 Probe 模块在 Battery Single Particle 模块中访问这些变量。单位均为默认值。

- `anodeModel.averageStoichiometry` — 阳极中的平均化学计量比。
- `anodeModel.massTransportOverpotential` — 传质过电位，单位为 volts。
- `anodeModel.normalizedAverageStoichiometry` — 按最小值和最大值归一化的平均化学计量比。
- `anodeModel.normalizedSurfaceStoichiometry` — 按最小值和最大值归一化的表面化学计量比。
- `anodeModel.ohmicOverpotential` — 阳极的欧姆过电位，单位为 volts。
- `anodeModel.shellConcentration` — 建模壳层的浓度，单位为 mol/m^3。壳层数量等于 **Anode Shell Count** 参数的值。
- `anodeModel.shellStoichiometry` — 建模壳层的化学计量比。壳层数量等于 **Anode Shell Count** 参数。
- `anodeModel.surfaceConcentration` — 颗粒表面的浓度，单位为 mol/m^3。
- `anodeModel.surfacePotential` — 颗粒表面的电位，单位为 volts。
- `anodeModel.temperatureAdjustedConductivity` — 已根据电池温度调整的电导率，单位为 S/m。
- `anodeModel.temperatureAdjustedDiffusionCoefficient` — 已根据电池温度调整的扩散系数，单位为 m^2/s。
- `averageElectrolyteConcentration` — 颗粒中的平均浓度，单位为 mol/m^3。
- `batteryCurrent` — 通过电池端子测得的总电流，单位为 amperes。
- `batteryTemperature` — 模块用于电阻和开路电压查表的电池平均温度。如果将 **Thermal model** 参数设置为 `Constant temperature`，则 `batteryTemperature` 变量等于指定的温度值。如果将 **Thermal model** 参数设置为 `Lumped thermal mass`，则 `batteryTemperature` 变量是一个在仿真期间变化的微分状态。
- `batteryVoltage` — 电池端子电压，或正极端子与负极端子之间的电压差，单位为 volts。
- `cathodeModel.averageStoichiometry` — 阴极中的平均化学计量比。
- `cathodeModel.massTransportOverpotential` — 传质过电位，单位为 volts。
- `cathodeModel.normalizedAverageStoichiometry` — 按最小值和最大值归一化的平均化学计量比。
- `cathodeModel.normalizedSurfaceStoichiometry` — 按最小值和最大值归一化的表面化学计量比。
- `cathodeModel.ohmicOverpotential` — 阴极的欧姆过电位，单位为 volts。
- `cathodeModel.shellConcentration` — 建模壳层的浓度，单位为 mol/m^3。壳层数量等于 **Anode Shell Count** 参数的值。
- `cathodeModel.shellStoichiometry` — 建模壳层的化学计量比。壳层数量等于 **Anode Shell Count** 参数。
- `cathodeModel.surfaceConcentration` — 颗粒表面的浓度，单位为 mol/m^3。
- `cathodeModel.surfacePotential` — 颗粒表面的电位，单位为 volts。
- `cathodeModel.temperatureAdjustedConductivity` — 已根据电池温度调整的电导率，单位为 S/m。
- `cathodeModel.temperatureAdjustedDiffusionCoefficient` — 已根据电池温度调整的扩散系数，单位为 m^2/s。
- `electrolyteModel.averageConcentration` — 整个电芯内电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.averageConcentrationAnode` — 阳极内部电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.averageConcentrationCathode` — 阴极内部电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.averageConcentrationSeparator` — 隔膜内部电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.concentrationAnode` — 阳极中建模的电解质层浓度，单位为 mol/m^3。元素数量等于 **Electrolyte layer count of anode** 参数。
- `electrolyteModel.concentrationCathode` — 阴极中建模的电解质层浓度，单位为 mol/m^3。元素数量等于 **Electrolyte layer count of cathode** 参数。
- `electrolyteModel.concentrationSeparator` — 隔膜中建模的电解质层浓度，单位为 mol/m^3。元素数量等于 **Electrolyte layer count of electrolyte** 参数。
- `electrolyteModel.currentDensityAnode` — 阳极中的电流密度，单位为 A/m^3。
- `electrolyteModel.currentDensityCathode` — 阴极中的电流密度，单位为 A/m^3。
- `electrolyteModel.diffusionCoefficientAnode` — 阳极中电解质的温度调整后有效扩散系数，单位为 m^s/s。
- `electrolyteModel.diffusionCoefficientCathode` — 阴极中电解质的温度调整后有效扩散系数，单位为 m^s/s。
- `electrolyteModel.diffusionCoefficientSeparator` — 隔膜中电解质的温度调整后有效扩散系数，单位为 m^s/s。
- `electrolyteModel.conductivityAnode` — 阳极中电解质的温度调整后有效电导率，单位为 S/m。
- `electrolyteModel.conductivityCathode` — 阴极中电解质的温度调整后有效电导率，单位为 S/m。
- `electrolyteModel.effectiveConductivitySeparator` — 隔膜中电解质的温度调整后有效电导率，单位为 S/m。
- `electrolyteModel.massTransportOverpotential` — 电解质的传质过电位，单位为 volts。
- `electrolyteModel.ohmicOverpotential` — 电解质的欧姆过电位，单位为 volts。
- `electrolyteModel.temperatureAdjustedConductivity` — 电解质的温度调整后电导率，单位为 S/m。
- `electrolyteModel.temperatureAdjustedDiffusionCoefficient` — 电解质的温度调整后扩散系数，单位为 m^s/s。
- `heatGenerationRate` — 电池总产热速率，单位为 watts。模块通过将电阻损耗和可逆热贡献相加来计算产热速率。
- `power_dissipated` — 电阻产热速率或耗散功率，单位为 watts。
- `reactionKineticsModel.chargeTransferOverpotential` — 电池的电荷转移过电位，单位为 volts。
- `reactionKineticsModel.exchangeCurrentDensityAnode` — 阳极中的交换电流密度，单位为 C/(m^2\*s)。
- `reactionKineticsModel.exchangeCurrentDensityCathode` — 阴极中的交换电流密度，单位为 C/(m^2\*s)。
- `reactionKineticsModel.temperatureAdjustedChargeTransferRateAnode` — 阳极的温度调整后电荷转移速率常数，单位为 m^(5/2)/(mol^(1/2) \* s)。
- `reactionKineticsModel.temperatureAdjustedChargeTransferRateCathode` — 阴极的温度调整后电荷转移速率常数，单位为 m^(5/2)/(mol^(1/2) \* s)。
- `stateOfCharge` — 通过库仑计数获得的电池荷电状态。
- `thermalModel.batteryTemperature` — 电池的温度，单位为 K。
- `thermalModel.cellTemperature` — 电芯输出的温度。
- `thermalModel.heatDissipationRate` — 电池的散热速率，单位为 watts。
- `thermalModel.heatGeneration` — 电池产生的热量，单位为 watts。
- `thermalModel.thermalMass` — 电池的热质量，单位为 J/K。
