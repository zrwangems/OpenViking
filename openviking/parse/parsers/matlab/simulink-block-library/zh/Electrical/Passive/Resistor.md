---
type: simulink-block
title: 'Resistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'resistor'
documentation_source_path: 'ref/resistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Resistor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: H
  summary: 电阻热质量热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与电阻正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电阻负极端子关联的电气守恒端口。

### **H** — 电阻热质量热

表示电阻热质量的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Resistance
  summary: 标称电阻值 1 Ohm（默认）
  group: 主要
- name: Tolerance (%)
  summary: 电阻容差，以百分比表示 5（默认）
  group: 主要
- name: Tolerance application
  summary: 选择仿真期间如何应用容差 None — use nominal value（默认）| Random tolerance | Apply maximum tolerance value | Apply minimum tolerance
    value
  group: 主要
- name: Tolerance distribution
  summary: 选择分布类型 Uniform（默认）| Gaussian
  group: 主要
- name: Number of standard deviations for quoted tolerance
  summary: 用于计算高斯随机数 4（默认）
  group: 主要
- name: Enable operating limits
  summary: 选择 Yes 以在超出工作限值时启用报告 No（默认）| Yes
  group: 工作限值
- name: Reporting when operating limits exceeded
  summary: 选择报告方法 Warn（默认）| Error
  group: 工作限值
- name: Maximum working voltage
  summary: 模块正常工作所允许的最大电压 100 V（默认）
  group: 工作限值
- name: Power rating
  summary: 模块正常工作所允许的最大功率 1 W（默认）
  group: 工作限值
- name: Temperature below which full power rating is available
  summary: 仍适用满功率额定值的最高温度 70 degC（默认）
  group: 工作限值
- name: Temperature above which power rating is reduced to zero
  summary: 功率额定值变为 0 的温度 155 degC（默认）
  group: 工作限值
- name: Operating temperature range, [Tmin Tmax]
  summary: 模块正常工作所允许的最低和最高温度值 [-50 150] degC（默认）
  group: 工作限值
- name: Noise mode
  summary: 选择是否对热噪声电流建模 Disabled（默认）| Enabled
  group: 噪声
- name: Sample time
  summary: 噪声源的采样速率 1e-3 s（默认）
  group: 噪声
- name: Repeatability
  summary: 选择噪声控制选项 Not repeatable（默认）| Repeatable | Specify seed
  group: 噪声
- name: Auto-generated seed used for repeatable option
  summary: 自动生成的随机数种子 随机实数
  group: 噪声
- name: Seed
  summary: 随机数种子 0（默认）
  group: 噪声
- name: Device simulation temperature
  summary: 仿真开始时电阻的温度 25 degC（默认）
  group: 噪声
- name: Resistance temperature coefficient
  summary: 指定电阻值如何随温度变化 0.00393 1/K（默认）
  group: 热
- name: Measurement temperature
  summary: 对应于标称电阻的温度 25 degC（默认）
  group: 热
- name: Thermal mass
  summary: 与端口 H 关联的热质量 100 J/K（默认）
  group: 热
- name: Resistance fault
  summary: 添加电阻故障的选项 Add fault（默认）
  group: 故障
- name: Faulted resistance
  summary: 模块处于故障状态时的电阻 inf Ohm（默认）| 正标量
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认）| Timed | Behavioral | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible current
  summary: 故障转换的电流阈值 1 A（默认）| 正标量
  group: 故障
- name: Time to fail when exceeding maximum permissible current
  summary: 电流超过阈值的最长时间 1 s（默认）| 非负标量
  group: 故障
- name: Trigger configuration
  summary: 启用附加触发类型的选项 Open fault properties
  group: 故障
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并指定电阻值如何随温度变化以及设置热质量。

### 主要

### **Resistance** — 标称电阻值 `1` `Ohm`（默认）

标称电阻值。电阻值必须大于零。

### **Tolerance (%)** — 电阻容差，以百分比表示 `5`（默认）

制造商数据手册中定义的电阻容差。

### **Tolerance application** — 选择仿真期间如何应用容差 `None — use nominal value`（默认）| `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择仿真期间如何应用容差：

- `None — use nominal value`
  — 模块不应用容差。模块使用标称电阻值。
- `Random tolerance` — 模块在容差
  值限制内对电阻值应用随机偏移。您可以通过
  **Tolerance distribution**
  参数选择均匀分布或高斯分布来计算随机数。
- `Apply maximum tolerance value`
  — 电阻增加指定的容差
  百分比值。
- `Apply minimum tolerance value`
  — 电阻减少指定的容差
  百分比值。

### **Tolerance distribution** — 选择分布类型 `Uniform`（默认）| `Gaussian`

选择随机容差的分布类型：

- `Uniform` — 均匀
  分布
- `Gaussian` — 高斯
  分布

#### 依赖关系

要启用此参数，请将 **Tolerance application** 设置为 `Random tolerance`。

### **Number of standard deviations for quoted tolerance** — 用于计算高斯随机数 `4`（默认）

用于计算高斯随机数的标准差数量。

#### 依赖关系

要启用此参数，请将 **Tolerance distribution** 设置为 `Gaussian`。

### 工作限值

### **Enable operating limits** — 选择 `Yes` 以在超出工作限值时启用报告 `No`（默认）| `Yes`

选择 `Yes` 以在超出工作限值时启用报告。**Operating Limits** 部分中的相关参数将变为可见，以便您选择报告方法并以功率和最大工作电压的形式指定工作限值。以温度形式指定工作限值的参数仅对具有暴露热端口的模块可见（参见 Model Thermal Effects）。默认值为 `No`。

### **Reporting when operating limits exceeded** — 选择报告方法 `Warn`（默认）| `Error`

选择超出工作限值时发生的情况：

- `Warn` — 模块
  发出警告。
- `Error` — 仿真
  因错误而停止。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为 `Yes`。

### **Maximum working voltage** — 模块正常工作所允许的最大电压 `100` `V`（默认）

模块正常工作所允许的最大电压幅值。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为 `Yes`。

### **Power rating** — 模块正常工作所允许的最大功率 `1` `W`（默认）

模块正常工作所允许的最大功率。

如果暴露模块的热端口，此参数将变为温度相关。您为 **Power rating** 参数指定的值适用于 **Temperature below which full power rating is available** 参数值所指定的温度以下。然后功率额定值随温度线性下降，直到在 **Temperature above which power rating is reduced to zero** 参数值所指定的温度处变为 0。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为 `Yes`。

### **Temperature below which full power rating is available** — 仍适用满功率额定值的最高温度 `70` `degC`（默认）

**Power rating** 参数值所指定的满功率额定值仍然适用的最高温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Temperature above which power rating is reduced to zero** — 功率额定值变为 0 的温度 `155` `degC`（默认）

功率额定值变为 0 的温度。高于此温度时，无论耗散功率如何，仿真始终发出断言。此参数值必须高于 **Temperature below which full power rating is available**。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Operating temperature range, [Tmin Tmax]** — 模块正常工作所允许的最低和最高温度值 `[-50 150]` `degC`（默认）

长度为 2 的行向量，指定模块正常工作所允许的最低和最高温度值。第一个元素是最低允许工作温度，第二个元素是最高允许工作温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`。

### 噪声

### **Noise mode** — 选择是否对热噪声电流建模 `Disabled`（默认）| `Enabled`

选择是否对热噪声电流建模：

- `Disabled` — 电阻不
  产生噪声。
- `Enabled` — 电阻产生
  热噪声电流，相关参数将在 **Noise** 部分中变为可见。

### **Sample time** — 噪声源的采样速率 `1e-3` `s`（默认）

噪声源的采样速率。选择该值以反映模型中所关注的频率。将采样时间设置得太小会不必要地减慢仿真速度。

#### 依赖关系

要启用此参数，请将 **Noise mode** 设置为 `Enabled`。

### **Repeatability** — 选择噪声控制选项 `Not repeatable`（默认）| `Repeatable` | `Specify seed`

选择噪声控制选项：

- `Not repeatable` —
  用于噪声生成的随机序列不可重复。
- `Repeatable` — 用于
  噪声生成的随机序列可重复，使用系统生成的种子。
- `Specify seed` — 用于
  噪声生成的随机序列可重复，您可以通过 **Seed** 参数控制种子。

#### 依赖关系

要启用此参数，请将 **Noise mode** 设置为 `Enabled`。

### **Auto-generated seed used for repeatable option** — 自动生成的随机数种子 随机实数

存储在模块内部的随机数种子，用于使随机序列可重复。该参数值使用 MATLAB 随机数生成器命令自动生成。您可以修改此参数值，但如果您将模块复制到模型中的另一个模块，它将被新的随机值覆盖。因此，如果您想控制随机序列的种子，请对 **Repeatability** 参数使用 `Specify seed` 选项，并使用 **Seed** 参数指定所需的种子值。

#### 依赖关系

要启用此参数，请将 **Repeatability** 设置为 `Repeatable`。

### **Seed** — 随机数种子 `0`（默认）

噪声随机数生成器使用的种子。

#### 依赖关系

要启用此参数，请将 **Repeatability** 设置为 `Specify seed`。

### **Device simulation temperature** — 仿真开始时电阻的温度 `25` `degC`（默认）

仿真开始时电阻的温度。

#### 依赖关系

要启用此参数，请将 **Noise mode** 设置为 `Enabled`。

对于具有暴露热端口的模块，此参数被禁用。请改用 **Variables** 选项卡设置初始温度目标。有关详细信息，请参见 Variables。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 指定电阻值如何随温度变化 `0.00393` `1/K`（默认）

描述电阻随温度变化的方程中的系数 α，*R*T = *R* (1+*α*(*T*–*T*0))。默认值为铜的值。

### **Measurement temperature** — 对应于标称电阻的温度 `25` `degC`（默认）

温度 *T*0，标称电阻 *R* 是在该温度下指定的。

### **Thermal mass** — 与端口 H 关联的热质量 `100` `J/K`（默认）

与热端口 H 关联的热质量。它表示将热端口温度升高一度所需的能量。

### 故障

### **Resistance fault** — 添加电阻故障的选项 `Add fault`（默认）

在 Resistor 模块中添加电阻故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Faulted resistance** — 模块处于故障状态时的电阻 `inf` `Ohm`（默认）| 正标量

模块处于故障状态时 + 和 – 端口之间的电阻。

#### 依赖关系

要启用此参数，请单击 **Resistance fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到您为 **Trigger fault at time** 参数指定的值时注入。
- `Behavioral` — 故障因仿真期间的故障参数值而注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器而注入。选择此选项并单击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障因反映信号相关行为的条件而注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的其余时间保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时模块进入故障状态，当触发条件为 false 时进入非故障状态。要了解更多信息，请参见 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参见 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请单击 **Resistance fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请单击 **Resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible current** — 故障转换的电流阈值 `1` `A`（默认）| 正标量

故障转换的电流阈值。如果电流连续超过此值的时间长于 **Time to fail when exceeding maximum permissible current** 参数的值，模块将进入故障状态。

#### 依赖关系

要启用此参数，请单击 **Resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding maximum permissible current** — 电流超过阈值的最长时间 `1` `s`（默认）| 非负标量

在故障触发之前，电流必须连续超过最大允许电流的时间量。

#### 依赖关系

要启用此参数，请单击 **Resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请单击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请单击 **Resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

### R2025a：对瞬态条件故障建模

您现在可以通过清除 **Trigger stays on once activated** 参数，在 Resistor 模块中对可逆条件故障建模。当触发条件为 true 时模块进入故障状态，当触发条件为 false 时进入非故障状态。

在 R2025a 之前，当触发条件首次变为 true 时，模块进入故障状态，并在仿真的其余时间保持故障状态。

如果您在 R2025a 之前创建了模型并在 Resistor 模块中启用了条件故障，为向后兼容，模块现在默认选择 **Trigger stays on once activated** 参数。

### R2023a：使用单个参数实现故障的时间或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并由 **Fault trigger** 参数替代。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。您只能启用一个触发器。

如果您在较早版本中创建了模型并同时启用了时间触发器和行为触发器，现在仅启用时间触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果将不同。

如果您想在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果您想确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

包含可选容差、工作限值、故障行为和噪声的电阻

Resistor 模块表示一个线性电阻，同时允许您对以下效应建模：

- 容差
- 工作限值
- 故障
- 热噪声
- 热效应建模

您可以独立地打开和关闭这些建模选项。当所有附加选项都关闭时，组件行为与 Simscape™ Foundation 库的 Resistor 模块相同。

在其最简单的形式中，Resistor 模块对线性电阻建模，用以下方程描述：

i=v/R

其中：

- *i* 是电流。
- *v* 是电压。
- *R* 是电阻。

如果您将 **Noise mode** 参数设置为 `Enabled`，则定义方程将增加一个离散变量 *i*N 来表示热噪声，如 Thermal Noise 中所述。

### 容差

您可以为 **Resistance** 参数提供的标称值应用容差。数据手册通常会为给定电阻器类型提供容差百分比。下表显示了模块如何根据所选的 **Tolerance application** 选项应用容差并计算电阻。

| 选项 | 电阻值 |
| --- | --- |
| `None — use nominal value` | *R* |
| `Random tolerance` | 均匀分布：*R* · (1 – *tol* + 2· *tol*· `rand`)  高斯分布：*R* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *R* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *R* · (1 – *tol* ) |

表中，

- *R* 是 **Resistance** 参数值，即标称电阻。
- *tol* 是分数容差，由基于百分比的 **Tolerance (%)** 参数计算得出。
- *nSigma* 是您为 **Number of standard deviations for quoted tolerance** 参数提供的值。
- `rand` 和 `randn` 是标准 MATLAB® 函数，用于生成均匀分布和正态分布随机数。

**注意**

如果您选择 `Random tolerance` 选项并且处于“Fast Restart”模式，那么只要分数容差 *tol* 或 **Number of standard deviations for quoted tolerance** *nSigma* 中至少有一个设置为 Run-time 并使用变量定义（即使您未修改该变量），随机容差值就会在每次仿真时更新。

### 工作限制

您可以按功率和最大工作电压指定工作限制。如果您将 **Modeling option** 参数设置为 `Show thermal port`（请参阅 Model Thermal Effects），则还可以按温度指定工作限制。

当超出工作限制时，模块可以生成警告，也可以停止仿真并报错。有关详细信息，请参阅 Operating Limits parameters 部分。

### 故障

要对 Resistor 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当电阻器发生故障时，其电阻会变为您为 **Faulted resistance** 参数指定的值。

**故障触发**

您可以使用 **Trigger type** 参数指定故障发生的方式和时间。

如果您将 **Trigger type** 设置为 `Behavioral`，则当电流连续超过 **Maximum permissible current** 参数的值，且持续时间长于 **Time to fail when exceeding maximum permissible current** 参数的值时，Resistor 模块会触发故障事件。

如果您将 **Trigger type** 设置为 `Conditional`，则可以选择 Resistor 模块中的故障是否可逆 *(since R2025a)*。要对不可逆故障建模，请单击 **Open fault properties** 以打开 Property Inspector，并选择 **Trigger stays on once activated** 参数。当触发条件第一次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。

有关向模块添加故障以及指定故障触发的详细信息，请参阅 Introduction to Simscape Faults。

### 热噪声

Resistor 模块可以生成热噪声电流。如果您将 **Noise mode** 参数设置为 `Enabled`，则定义方程会通过一个离散变量 *i*N 进行扩展，以表示热噪声：

i=v/R+iN

如果采样时间为 *h*，则热噪声由下式给出：

iN=2kT/RN(0,1)h

其中：

- *k* 是玻尔兹曼常数，1.3806504e-23 J/K。
- *T* 是温度。
- *R* 是电阻。
- *N* 是均值为零、标准差为一的高斯随机数。
- *2kT/R* 是双边热噪声功率分布（单边等效值为 *4kT/R*）。

该模块通过使用 Simscape Foundation 库中的 PS Random Number 源生成高斯噪声。您可以通过设置 **Repeatability** 参数来控制随机数种子：

- `Not repeatable` — 每次对模型进行仿真时，模块都会使用 MATLAB 随机数生成器重置随机种子：

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — 模块会自动生成一个种子值并将其存储在模块内部，以便始终使用相同的随机数开始仿真。当您从模块库向模型添加 Resistor 模块时，会设置这个自动生成的种子值。当您从模型中的现有 Resistor 模块创建新副本时，会生成新的种子值。模块使用上面显示的 MATLAB 随机数生成器命令设置该值。
- `Specify seed` — 如果选择此选项，则附加的 **Seed** 参数允许您直接指定随机数种子值。

### 热效应建模

您可以公开热端口，以指定电阻值如何随温度变化并设置热质量。要公开热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

使用 **Variables** 选项卡设置初始温度目标。

公开热端口后，生成的噪声在确定瞬时噪声值时会使用热端口处的温度。公开热端口还会按如下方式扩展 **Operating Limits** 选项卡上的选项：

- **Power rating** 参数变为与温度相关。您需要定义一个温度，在该温度及以下可获得完整额定功率，并定义另一个更高温度，在该温度下额定功率降为零。假定额定功率在这两个值之间随温度线性下降。
- 附加参数 **Operating temperature range, [Tmin Tmax]** 允许您定义模块运行的有效温度范围。

### 绘图和显示选项

如果您公开热端口，则可以使用模块上下文菜单上的 **Electrical** 菜单执行绘图和显示操作。

右键单击模块，然后从 **Electrical** 菜单中选择 **Basic characteristics**，以使用当前电阻器参数在 MATLAB 图窗中以 SI 单位绘制电阻。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

本节仅对公开热端口的模块显示。**Temperature** 变量允许您为仿真开始时的温度指定高优先级目标。

### 假设和限制

启用噪声进行仿真会减慢仿真速度。请选择采样时间 (*h*)，使噪声仅在感兴趣的频率上生成，而不会在更高频率上生成。
