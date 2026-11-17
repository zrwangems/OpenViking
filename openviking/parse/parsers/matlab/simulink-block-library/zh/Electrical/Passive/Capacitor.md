---
type: simulink-block
title: 'Capacitor'
family: 'passive'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'capacitor'
documentation_source_path: 'ref/capacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# Capacitor

## 端口

### 守恒

### **+** — 正极端子电气

与电容器正电压关联的电气守恒端口。

### **-** — 负极端子电气

与电容器负电压关联的电气守恒端口。

### **H** — 电容器热质量热

*自 R2024a 起*

与电容器热质量关联的热守恒端口。

## 参数

### 主要

### **Capacitance model** — 电容器类型 `Constant`（默认）| `Lookup table` | `Dielectric relaxation (Debye)`

选择电容器类型：

- `Constant` — 对线性电容器建模，其标称电容由 **Capacitance** 参数值定义。
- `Lookup table` — 对非线性电容器建模，其中标称电容值根据所施加的端子电压值变化。
- `Dielectric relaxation (Debye)` — 对具有电阻损耗和介电损耗的频率相关电容器建模。

### **Capacitance** — 标称电容 `1e-6` `F`（默认）

线性电容器的标称电容值，或 Debye 参数化中的低频电容。

#### 依赖项

仅当您为 **Capacitance model** 参数选择 `Constant` 或 `Dielectric relaxation (Debye)` 时，此参数才可见。

### **Capacitance values** — 电容值向量 `[1e-05, 1e-06]` `F`（默认）| 正向量

用于基于对应电压值进行表查找的电容值向量。向量长度必须与电压向量长度相同。

#### 依赖项

仅当您为 **Capacitance model** 参数选择 `Lookup table` 时，此参数才可见。

### **Corresponding voltage values** — 电压值输入向量 `[0, 10]` `V`（默认）

用于基于表的电容计算的电压值输入向量。向量长度必须大于或等于 2，且值必须严格单调，即递增或递减。

#### 依赖项

仅当您为 **Capacitance model** 参数选择 `Lookup table` 时，此参数才可见。

### **Symmetric C-V table** — 表数据 `Yes - use voltage magnitude when computing C`（默认）| `No - use C-V data as-is`

指定如何使用表数据：

- `Yes - use voltage magnitude when computing C` — 使用此选项可确保电容相对于所施加端子电压的对称性。
- `No - use C-V data as-is` — 使用此选项对极性电容器建模。例如，对于基于表的电容的默认参数值，施加 –10 V 电压会产生 1e-6 F 的标称电容。但是，如果您为 **Symmetric C-V table** 参数选择 `No - use C-V data as-is`，则得到的电容值为 1e-5 F，因为该模块使用最近的输入值进行外推。

#### 依赖项

仅当您为 **Capacitance model** 参数选择 `Lookup table` 时，此参数才可见。

### **Frequencies for specifying dissipation factors [f1 f2]** — 用于计算耗散因数的频率 `[1, 10]` `kHz`（默认）

计算耗散因数 **[DF1 DF2]** 的频率，以 kHz 为单位。

#### 依赖项

仅当您为 **Capacitance model** 参数选择 `Dielectric relaxation (Debye)` 时，此参数才可见。

### **Dissipation factors (%) at f1 and f2 [DF1 DF2]** — f1 和 f2 处的耗散因数 `[.8, 1.2]`（默认）

等效串联电阻与容抗之比，或损耗角正切。耗散因数是电容器的常用指标。

#### 依赖项

仅当您为 **Capacitance model** 参数选择 `Dielectric relaxation (Debye)` 时，此参数才可见。

### **Capacitance tolerance (%)** — 电容器容差 `5`（默认）

制造商数据手册中定义的电容器容差。对于基于表的电容器，此容差一次性应用于整个表。

### **Tolerance application** — 容差应用 `None — use nominal value`（默认）| `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择仿真期间如何应用容差：

- `None — use nominal value` — 该模块不应用容差，使用标称电容值。
- `Random tolerance` — 该模块在容差值限制内对电容值施加随机偏移。您可以使用 **Tolerance distribution** 参数选择 Uniform 或 Gaussian 分布来计算随机数。
- `Apply maximum tolerance value` — 电容按指定的容差百分比值增加。
- `Apply minimum tolerance value` — 电容按指定的容差百分比值减小。

### **Tolerance distribution** — 容差分布类型 `Uniform`（默认）| `Gaussian`

选择分布类型：

- `Uniform` — 均匀分布。
- `Gaussian` — 高斯分布。

#### 依赖项

仅当您为 **Tolerance application** 参数选择 `Random tolerance` 时，此参数才可见。

### **Number of standard deviations for quoted tolerance** — 引用容差的标准差数 `4`（默认）

用于计算高斯随机数的标准差数。

#### 依赖项

仅当您为 **Tolerance distribution** 参数选择 `Gaussian` 时，此参数才可见。

### **Series resistance** — 串联电阻 `1e-6` `Ohm`（默认）

某些电路的仿真可能需要存在较小的串联电阻。等效串联电阻 (ESR) 有时在制造商数据手册中指定。如果未指定，您可以通过耗散因数 (DF) 为线性电容器定义此电阻，许多数据手册中也给出了 DF。关系为 *`DF`* = 2π· *`f`*· *`C`*· *`ESR`*，其中 *`f`* 是信号频率。对于 Debye 电容器，在计算 𝛼 和 𝜏 之前，会根据此附加串联电阻对 **Dissipation factors (%) at f1 and f2 [DF1 DF2]** 进行校正。

### **Parallel conductance** — 并联泄漏路径 `0` `1/Ohm`（默认）

与电容器关联的并联泄漏路径。对于串联连接的电容器，存在较小的并联电导有助于收敛。

### **Averaging period for power logging** — 功率记录平均周期 `0` `s`（默认）

功率记录的平均周期，以 s 为单位。

**注意**

如果此参数设置为 `0`，则输出为瞬时功率。

#### 依赖项

仅当您为 **Capacitance model** 参数选择 `Dielectric relaxation (Debye)` 时，此参数才可见。

### 工作限制

### **Enable operating limits** — 启用工作限制 `No`（默认）| `Yes`

选择 `Yes` 以在超出工作限制时启用报告。关联参数将在 **工作限制** 选项卡上可见，以便您选择报告方法，并以功率和工作电压形式指定工作限制。

### **Reporting if operating limits exceeded** — 报告行为 `Warn`（默认）| `Error`

选择超出工作限制时发生的情况：

- `Warn` — 该模块发出警告。
- `Error` — 仿真停止并报错。

### **Working voltage range** — 工作电压范围 `[-25, 25]` `V`（默认）

模块正常工作所允许的电压值范围，指定为大小为 2 的向量。

### **Power rating** — 最大瞬时功率耗散 `1` `W`（默认）

与电容器关联的电阻和电导元件中的最大瞬时功率耗散。

### **Temperature** — 最高允许温度 `85` `degC`（默认）

*自 R2024a 起*

最高允许温度。如果电容器温度高于此值，该模块会发出警告或错误。

#### 依赖项

要启用此参数，请在 **热** 部分中选择 **Model thermal port** 参数。

### 热

### **Model thermal port** — 用于对热端口建模的选项 `off`（默认）| `on`

*自 R2024a 起*

用于在 Capacitor 模块中对热端口建模的选项。

### **Thermal mass** — 与热端口关联的热质量 `1` `J/K`（默认）

*自 R2024a 起*

与热端口 **H** 关联的热质量。它表示将热端口的温度升高一度所需的能量。

#### 依赖项

要启用此参数，请选择 **Model thermal port** 参数。

### 故障

### **Capacitor fault** — 用于对电容器中的故障建模的选项 `Add fault`（默认）

用于在 Capacitor 模块中对故障建模的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Faulted capacitance as % of unfaulted** — 故障电容占未故障电容的百分比 `100`（默认）| 正标量

当模块处于故障状态时，相对于未故障状态的电容相对变化。对于基于表的电容，相对变化应用于向量的所有元素。默认值为 `100`，这意味着故障电容等于未故障电容。

#### 依赖项

要启用此参数，请点击 **Capacitor fault** 参数中的 **Add fault** 超链接，向 Capacitor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted series resistance** — 故障串联电阻 `1e-3` `Ohm`（默认）| 有限正标量

当模块处于故障状态时，电容器的等效串联电阻。

#### 依赖项

要启用此参数，请点击 **Capacitor fault** 参数中的 **Add fault** 超链接，向 Capacitor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted parallel conductance** — 故障并联电导 `0` `1/Ohm`（默认）| 有限非负标量

当模块处于故障状态时，电容器的并联泄漏电导。

#### 依赖项

要启用此参数，请点击 **Capacitor fault** 参数中的 **Add fault** 超链接，向 Capacitor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Fault transition time constant** — 故障过渡时间常数 `1e-3` `s`（默认）| 正标量

与过渡到故障状态关联的时间常数，如故障中所述。

#### 依赖项

要启用此参数，请点击 **Capacitor fault** 参数中的 **Add fault** 超链接，向 Capacitor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible temperature** — 最高允许温度 `85` `degC`（默认）| 非负标量

*自 R2024a 起*

最高允许温度。如果温度值超出此值的时间长于 **Time to fail when exceeding maximum temperature** 参数值，则模块开始进入故障状态。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding maximum temperature** — 超过最高温度时的失效时间 `1` `s`（默认）| 非负标量

*自 R2024a 起*

温度可以超出允许温度范围而不触发故障的最长时间。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Permissible voltage range** — 最小和最大允许电压 `[-100, 100]` `V`（默认）| 长度为 2 的向量

最小和最大允许电压。如果电压值超出此范围的时间长于 **Time to fail when exceeding voltage range** 参数值，则模块开始进入故障状态。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding voltage range** — 超过电压范围时的失效时间 `1` `s`（默认）| 非负标量

电压可以超出允许电压范围而不触发故障的最长时间。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024a：通过暴露热端口对热效应建模

Capacitor 模块现在支持热端口。要对热端口建模，请在 **热** 部分中选择 **Model thermal port** 参数。要指定热质量的值以及电容器的最高允许温度，请分别在 **工作限制** 和 **热** 部分中指定新增的 **Temperature** 和 **Thermal mass** 参数的值。

### R2023a：使用单个参数实现故障的时间触发器或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已删除，并替换为 **Fault trigger** 参数。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。您只能启用一个触发器。

如果您在早期版本中创建了模型并启用了时间触发器和行为触发器，现在仅启用时间触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果会有所不同。

如果要在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果要确定系统是否失效以及何时失效，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

具有可选容差、工作限制和故障行为的线性或非线性电容器

Capacitor 模块允许您对线性、非线性（基于表）和频率相关电容器（包括极性电容器）建模。您还可以选择性地对以下效应建模：

- 容差
- 工作限制
- 故障

您可以彼此独立地打开和关闭这些建模选项。当所有附加选项都关闭时，组件行为与 Simscape™ Foundation library Capacitor 模块相同。

在其最简单的形式中，Capacitor 模块对线性电容器建模，由以下方程描述：

I=CdVdt

其中：

- *I* 是电流。
- *C* 是电容。
- *V* 是电压。
- *t* 是时间。

要对非线性或极性电容器建模，请将 **Capacitance model** 参数设置为 `Lookup table`，并提供电容-电压值的查找表：

- 对于极性电容器，其中该查找表相对于所施加的端子电压不对称，将 **Symmetric C-V table** 参数设置为 `No - use C-V data as-is`。
- 对于其他类型的非线性电容器，通过将 **Symmetric C-V table** 参数设置为 `Yes - use voltage magnitude when computing C`，确保电容相对于所施加的端子电压具有对称性。

要对具有电阻损耗和介电损耗的频率相关电容器建模，请将 **Capacitance model** 参数设置为 `Dielectric relaxation (Debye)`。Debye 弛豫模型考虑频域中一组非相互作用偶极子。结果以复介电常数表示。复介电常数的实部（𝜖′）和虚部（𝜖′′）由以下方程给出：

ε'=ε∞+εs−ε∞1+ω2τ2

ε''=(εs−ε∞)ωτ1+ω2τ2,

其中 𝜔 是角频率，𝜖∞ 是极高频下的实介电常数，𝜖𝑠 是低频下的实介电常数，𝜏 是弛豫时间常数。

在时域中，Debye 模型中电容器的特征方程为

τi=−q+Cs(ατν˙+ν),

其中 𝐶𝑠 是低频电容，𝛼 = 𝜖∞/𝜖𝑠，𝑞 是电荷，𝑖 是电流，𝑣 是电容器两端的电压。

大多数数据手册不提供复介电常数或弛豫时间的显式值；但是，通常会在两个频率下提供耗散因数。参数 𝛼 和 𝜏 可根据这些值按以下方程推导：

τ=DF1DF2(ω22−ω12)+DF12DF22(ω22−ω12)2+4ω1ω2(DF2ω2−DF1ω1)(DF1ω2−DF2ω1)2ω1ω2(DF2ω2−DF1ω1)

α=ω1τ−DF1ω1τ(1+DF1ω1τ),

其中 𝜔1 和 𝜔2 是两个不同的频率，*DF1* 和 *DF2* 分别是所述频率下计算得到的耗散因数。

对于 Debye 模型中的有效参数化，平方根的自变量必须为正。

### 容差

您可以对为 **Capacitance** 参数提供的标称值应用容差。数据手册通常会为给定电容器类型提供容差百分比。该表显示了模块如何根据所选的 **Tolerance application** 选项应用容差并计算电容。

| 选项 | 电容值 |
| --- | --- |
| `None — use nominal value` | *C* |
| `Random tolerance` | 均匀分布：*C* · (1 – *tol* + 2· *tol*· `rand`)  高斯分布：*C* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *C* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *C* · (1 – *tol* ) |

表中，

- *C* 是 **Capacitance** 参数值，即标称电容。
- *tol* 是分数容差，即 **Capacitance tolerance (%)** /100。
- *nSigma* 是您为 **Number of standard deviations for quoted tolerance** 参数提供的值。
- `rand` 和 `randn` 是用于生成均匀分布和正态分布随机数的标准 MATLAB® 函数。

**注意**

如果您选择 `Random tolerance` 选项，并且处于 "Fast Restart" 模式，那么只要分数容差 *tol* 或 **Number of standard deviations for quoted tolerance** 参数 *nSigma* 中至少有一个设置为 Run-time 并使用变量定义（即使您不修改该变量），随机容差值就会在每次仿真时更新。

### 工作限制

您可以按最大工作电压以及电容器串联电阻和并联电导中的最大（瞬时）功率耗散来指定工作限制。

对于极性电容器，您可以定义工作电压范围，使得当所施加电压的极性变得不正确时，模块会提供警告或错误。

当超过工作限制时，模块可以生成警告，也可以因错误而停止仿真。有关更多信息，请参见工作限制。

### 热效应建模

*自 R2024a 起*

您可以暴露热端口，以观察电容器的功率损耗和温度变化，并设置热质量。要暴露热端口，请在 **Thermal** 部分中，选择 **Model thermal port** 参数。

暴露热端口还会启用 **Operating Limits** 部分中的 **Temperature** 参数，该参数定义模块运行的最大有效温度。

使用 **Variables** 选项卡设置初始温度目标。

### 故障

要对 Capacitor 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参见故障行为建模和故障触发。

电容器参数的瞬时变化是非物理的。因此，当 Capacitor 模块进入故障状态时，电容、电阻和电导会根据以下公式在一段时间内过渡到其故障值：

*`CurrentValue`* =
*`FaultedValue`* –
(*`FaultedValue`* –
*`UnfaultedValue`*) · `sech`(∆t
/ τ)

其中：

- ∆t 是自故障条件开始以来的时间。
- τ 是与故障过渡相关联的用户定义时间常数。

模块可以触发故障过渡的开始：

- 在特定时间。
- 当端子电压超出允许电压范围的时间超过特定时间间隔时。

如果要在特定时间触发故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Timed`。如果要确定系统是否失效以及何时失效，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Behavioral`。

### 变量

使用模块界面的 **Variables** 部分，在仿真前设置模块变量的优先级和初始目标值。有关更多信息，请参见为模块变量设置优先级和初始目标。

**Capacitor voltage** 变量允许您指定仿真开始时初始电容器电压的高优先级目标。

**Temperature** 变量允许您指定仿真开始时温度的高优先级目标。要启用此变量，请在 **Thermal** 部分中，选择 **Model thermal port** 参数。*（自 R2024a 起）*
