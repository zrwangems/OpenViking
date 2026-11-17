---
type: simulink-block
title: 'Diffusion Resistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'diffusionresistor'
documentation_source_path: 'ref/diffusionresistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Diffusion Resistor

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

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Resistance
  summary: 标称零偏置电阻 1 Ohm（默认）
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
- name: Parameterization
  summary: 选择参数化方法 Simplified（默认）| Advanced
  group: 主要
- name: Critical voltage
  summary: 饱和临界电压 4 V（默认）
  group: 主要
- name: Corner voltage
  summary: 电阻开始增加的电压 2 V（默认）
  group: 主要
- name: Quadratic voltage coefficient
  summary: 系数 *p*2 0.25（默认）
  group: 主要
- name: Inverse voltage for quadratic voltage activation
  summary: 系数 *θ*2 0.25 1/V（默认）
  group: 主要
- name: Linear voltage coefficient
  summary: 系数 *p*3 0.25（默认）
  group: 主要
- name: Inverse voltage for linear voltage activation
  summary: 系数 *θ*3 0.25 1/V（默认）
  group: 主要
- name: Enable operating limits
  summary: 选择 Yes 以在超出工作限值时启用报告 No（默认）| Yes
  group: 工作限值
- name: Reporting when operating limits exceeded
  summary: 选择报告方法 Warn（默认）| Error
  group: 工作限值
- name: Maximum working voltage
  summary: 模块正常工作允许的最大电压 100 V（默认）
  group: 工作限值
- name: Power rating
  summary: 模块正常工作允许的最大功率 1 W（默认）
  group: 工作限值
- name: Temperature below which full power rating is available
  summary: 仍适用满功率额定值的最高温度 70 degC（默认）
  group: 工作限值
- name: Temperature above which power rating is reduced to zero
  summary: 功率额定值变为 0 的温度 155 degC（默认）
  group: 工作限值
- name: Operating temperature range, [Tmin Tmax]
  summary: 模块正常工作允许的最低和最高温度值 [-50 150] degC（默认）
  group: 工作限值
- name: Resistance fault
  summary: 添加电阻故障的选项 Add fault（默认）
  group: 故障
- name: Faulted zero-voltage resistance
  summary: 模块处于故障状态时的电阻 inf Ohm（默认）| 正标量
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
- name: Resistance linear temperature coefficient
  summary: 指定电阻值如何随温度变化 0 1/K（默认）
  group: 热
- name: Resistance quadratic temperature coefficient
  summary: 指定电阻值如何随温度变化 0 1/K^2（默认）
  group: 热
- name: Measurement temperature
  summary: 标称电阻对应的温度 25 degC（默认）
  group: 热
- name: Thermal mass
  summary: 与端口 H 关联的热质量 100 J/K（默认）
  group: 热
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并指定电阻值如何随温度变化以及设置热质量。

### 主要

### **Resistance** — 标称零偏置电阻 `1` `Ohm`（默认）

零偏置电阻，用作标称电阻值。电阻值必须大于零。如果将 **Modeling option** 设置为
`Show thermal port`，则这是温度等于热部分中 **Measurement
temperature** 参数时的零偏置电阻。

### **Tolerance (%)** — 电阻容差，以百分比表示 `5`（默认）

制造商数据手册中定义的电阻容差。

### **Tolerance application** — 选择仿真期间如何应用容差 `None — use nominal value`（默认）| `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择仿真期间如何应用容差：

- `None — use nominal value`
  — 模块不应用容差，使用标称电阻值。
- `Random tolerance` — 模块在容差限值内对电阻值应用随机偏移。可以使用
  **Tolerance distribution**
  参数选择均匀分布或高斯分布来计算随机数。
- `Apply maximum tolerance value`
  — 电阻增加指定的容差百分比值。
- `Apply minimum tolerance value`
  — 电阻减少指定的容差百分比值。

### **Tolerance distribution** — 选择分布类型 `Uniform`（默认）| `Gaussian`

选择随机容差的分布类型：

- `Uniform` — 均匀分布
- `Gaussian` — 高斯分布

#### 依赖关系

要启用此参数，请将 **Tolerance application** 设置为
`Random tolerance`。

### **Number of standard deviations for quoted tolerance** — 用于计算高斯随机数 `4`（默认）

用于计算高斯随机数的标准差数量。

#### 依赖关系

要启用此参数，请将 **Tolerance distribution** 设置为
`Gaussian`。

### **Parameterization** — 选择参数化方法 `Simplified`（默认）| `Advanced`

选择仿真期间如何应用容差：

- `Simplified` — 假设二次和线性系数相同，并使用 **Critical voltage** 和
  **Corner voltage** 参数定义模块行为。
- `Advanced` — 显式指定二次和线性电压系数的值，以及二次和线性电压激活的反向电压值。

### **Critical voltage** — 饱和临界电压 `4` `V`（默认）

饱和机制的临界电压。可以通过取 *R*/*R*0
随电压增量的斜率的倒数来确定此参数值。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Simplified`。

### **Corner voltage** — 电阻开始增加的电压 `2` `V`（默认）

拐点电压，电阻开始增加的电压。**Corner voltage** 必须小于
**Critical voltage**。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Simplified`。

### **Quadratic voltage coefficient** — 系数 *p*2 `0.25`（默认）

定义方程中的系数 *p*2。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Advanced`。

### **Inverse voltage for quadratic voltage activation** — 系数 *θ*2 `0.25` `1/V`（默认）

定义方程中的系数 *θ*2。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Advanced`。

### **Linear voltage coefficient** — 系数 *p*3 `0.25`（默认）

定义方程中的系数 *p*3。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Advanced`。

### **Inverse voltage for linear voltage activation** — 系数 *θ*3 `0.25` `1/V`（默认）

定义方程中的系数 *θ*3。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Advanced`。

### 工作限值

### **Enable operating limits** — 选择 `Yes` 以在超出工作限值时启用报告 `No`（默认）| `Yes`

选择 `Yes` 以在超出工作限值时启用报告。**Operating Limits** 部分中的关联参数将变为可见，以便选择报告方法并以功率和最大工作电压的形式指定工作限值。以温度形式指定工作限值的参数仅对具有暴露热端口的模块可见（请参阅 Model Thermal Effects）。默认值为
`No`。

### **Reporting when operating limits exceeded** — 选择报告方法 `Warn`（默认）| `Error`

选择超出工作限值时发生的情况：

- `Warn` — 模块发出警告。
- `Error` — 仿真停止并报错。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为
`Yes`。

### **Maximum working voltage** — 模块正常工作允许的最大电压 `100` `V`（默认）

模块正常工作允许的最大电压幅值。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为
`Yes`。

### **Power rating** — 模块正常工作允许的最大功率 `1` `W`（默认）

模块正常工作允许的最大功率。

如果暴露模块的热端口，此参数将变为温度相关。为 **Power
rating** 参数指定的值适用于 **Temperature below which full power rating is
available** 参数值所指定的温度以下。然后功率额定值随温度线性下降，直到在 **Temperature above which power rating is
reduced to zero** 参数值所指定的温度处变为 0。

#### 依赖关系

要启用此参数，请将 **Enable operating
limits** 设置为 `Yes`。

### **Temperature below which full power rating is available** — 仍适用满功率额定值的最高温度 `70` `degC`（默认）

**Power rating** 参数值所指定的满功率额定值仍适用的最高温度。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Show thermal port`。

### **Temperature above which power rating is reduced to zero** — 功率额定值变为 0 的温度 `155` `degC`（默认）

功率额定值变为 0 的温度。高于此温度时，无论耗散功率如何，仿真始终发出断言。此参数值必须高于 **Temperature below
which full power rating is available**。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Show thermal port`。

### **Operating temperature range, [Tmin Tmax]** — 模块正常工作允许的最低和最高温度值 `[-50 150]` `degC`（默认）

长度为 2 的行向量，指定模块正常工作允许的最低和最高温度值。第一个元素是最低允许工作温度，第二个元素是最高允许工作温度。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Show thermal port`。

### 故障

### **Resistance fault** — 添加电阻故障的选项 `Add fault`（默认）

在 Diffusion Resistor 模块中添加电阻故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Faulted zero-voltage resistance** — 模块处于故障状态时的电阻 `inf` `Ohm`（默认）| 正标量

模块处于故障状态时 + 和 – 端口之间的零电压电阻。

#### 依赖关系

要启用此参数，请通过单击 **Resistance fault** 参数中的 **Add fault** 超链接向 Diffusion Resistor 模块添加故障。

创建故障后，可以在 **Fault Inspector** 窗口中更改属性。打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Timed`。

### **Maximum permissible current** — 故障转换的电流阈值 `1` `A`（默认）| 正标量

故障转换的电流阈值。如果电流超过此值的时间长于 **Time to fail when exceeding maximum
permissible current** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **Time to fail when exceeding maximum permissible current** — 电流超过阈值的最长时间 `1` `s`（默认）| 非负标量

电流可以超过最大允许值而不触发故障的最长时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### 噪声

### **Noise mode** — 选择是否对热噪声电流建模 `Disabled`（默认）| `Enabled`

选择是否对热噪声电流建模：

- `Disabled` — 电阻不产生噪声。
- `Enabled` — 电阻产生热噪声电流，关联参数将在 **Noise** 部分中变为可见。

### **Sample time** — 噪声源的采样速率 `1e-3` `s`（默认）

定义噪声源的采样速率。选择它时应反映模型中所关注的频率。采样时间过小会不必要地减慢仿真速度。

#### 依赖关系

要启用此参数，请将 **Noise mode** 设置为
`Enabled`。

### **Repeatability** — 选择噪声控制选项 `Not repeatable`（默认）| `Repeatable` | `Specify seed`

选择噪声控制选项：

- `Not repeatable` —
  用于噪声生成的随机序列不可重复。
- `Repeatable` — 用于噪声生成的随机序列可重复，使用系统生成的种子。
- `Specify seed` — 用于噪声生成的随机序列可重复，并且可以通过 **Seed** 参数控制种子。

#### 依赖关系

要启用此参数，请将 **Noise mode** 设置为
`Enabled`。

### **Auto-generated seed used for repeatable option** — 自动生成的随机数种子 随机实数

存储在模块内部的随机数种子，用于使随机序列可重复。参数值使用 MATLAB 随机数生成器命令自动生成。可以修改此参数值，但如果将模块复制到模型中的另一个模块，它将被新的随机值覆盖。因此，如果要控制随机序列的种子，请对 **Repeatability** 参数使用 `Specify
seed` 选项，并使用 **Seed** 参数指定所需的种子值。

#### 依赖关系

要启用此参数，请将 **Repeatability** 设置为
`Repeatable`。

### **Seed** — 随机数种子 `0`（默认）

噪声随机数生成器使用的种子。

#### 依赖关系

要启用此参数，请将 **Repeatability** 设置为 `Specify
seed`。

### **Device simulation temperature** — 仿真开始时电阻的温度 `25` `degC`（默认）

仿真开始时电阻的温度。

#### 依赖关系

要启用此参数，请将 **Noise mode** 设置为
`Enabled`。

对于具有暴露热端口的模块，此参数被禁用。请改用 **Variables** 选项卡设置初始温度目标。有关详细信息，请参阅 Variables。

### 热

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Resistance linear temperature coefficient** — 指定电阻值如何随温度变化 `0` `1/K`（默认）

描述电阻随温度变化的方程中的系数 TC1eff。有关详细信息，请参阅 Model Thermal Effects。

### **Resistance quadratic temperature coefficient** — 指定电阻值如何随温度变化 `0` `1/K^2`（默认）

描述电阻随温度变化的方程中的系数 TC2eff。有关详细信息，请参阅 Model Thermal Effects。

### **Measurement temperature** — 标称电阻对应的温度 `25` `degC`（默认）

指定标称电阻 *R* 的温度 *T*0。

### **Thermal mass** — 与端口 H 关联的热质量 `100` `J/K`（默认）

与热端口 H 关联的热质量。它表示将热端口温度升高一度所需的能量。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2023a: 使用单个参数实现故障的时间或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已删除，并替换为 **Fault
trigger** 参数。可以将 **Fault trigger**
参数设置为 `Temporal` 或 `Behavioral`。
只能启用一个触发器。

如果在早期版本中创建了模型并同时启用了时间触发器和行为触发器，则现在仅启用时间触发器。因此，如果行为触发器在模型中导致故障，仿真结果会有所不同。

如果要在特定时间触发故障，请将 **Fault trigger**
参数设置为 `Temporal`。如果要确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为
`Behavioral`。

## 描述

具有速度饱和以及可选容差、工作限值、故障行为和噪声的电阻模型

Diffusion Resistor 模块表示具有速度饱和的电阻，同时允许对以下效应建模：

- 容差
- 工作限值
- 故障
- 热噪声
- 热效应建模

可以相互独立地打开和关闭这些建模选项。

在其最简单的形式中，Diffusion Resistor 模块的电阻为：

R=R0(1−p2−p3+p21+(θ2vpn)2+p31+|θ3vpn|33)

其中：

- *R0* 是零偏置电阻。
- *p2* 和
  *p*3 分别是二次和线性电压系数。
- *θ2* 和
  *θ*3 分别是二次和线性电压激活的反向电压。
- *vpn* 是施加在电阻上的电压。

在低偏置下，

R≈R0(1+p2θ22vpn22)

因此 *p2* 和
*θ2* 决定电阻的低偏置二次行为。

在高偏置下，

R≈R0(1−p2−p3+|vpn|(p2θ2+p3θ3))

因此 *p3* 和
*θ3* 仅影响电阻的高偏置线性行为。

可以使用电阻的电压依赖性来对扩散电阻中的速度饱和建模。对于足够高的电压，

isat=1R0(p2θ2+p3θ3)

其中 *isat* 是饱和电流。

### 简化参数化

简化参数化模型假设二次项和线性项系数相同。这是 Compact Model Coalition 提供的 r2\_cmc 模型推荐假设之一，可作为执行参数提取时的合理初始猜测。在此假设下，可以定义两个新参数，**Critical voltage** 和 **Corner voltage**，它们为模型参数化提供了一种更简单的方法：

p2=p3=vco2vcritθ2=θ3=12vco

其中：

- *vcrit* 是临界电压。
- *vco* 是拐点电压。

在高电压下，

dRdvpn≈R0vcrit

因此，临界电压是 *R*/*R0* 随电压增加的斜率的倒数。

使用此参数化时，饱和电流为

isat=vcritR0

### 容差

您可以对为 **Resistance** 参数提供的标称值应用容差。数据手册通常会给出给定电阻器类型的容差百分比。下表显示了模块如何根据所选的 **Tolerance application** 选项应用容差并计算电阻。

| 选项 | 电阻值 |
| --- | --- |
| `None — use nominal value` | *R*0 |
| `Random tolerance` | 均匀分布：*R0* · (1 – *tol* + 2· *tol*· `rand`)  高斯分布：*R0* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *R0* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *R0* · (1 – *tol* ) |

表中，

- *R*0 是 **Resistance** 参数值，即标称零偏置电阻。
- *tol* 是分数容差，即 **Tolerance (%)** /100。
- *nSigma* 是您为 **Number of standard deviations for quoted tolerance** 参数提供的值。
- `rand` 和 `randn` 是用于生成均匀分布和正态分布随机数的标准 MATLAB® 函数。

**注意**

如果您选择 `Random tolerance` 选项并且处于 “Fast Restart” 模式，那么只要分数容差 *tol* 或 **Number of standard deviations for quoted tolerance** *nSigma* 中至少有一个设置为 Run-time 并使用变量定义（即使您未修改该变量），随机容差值就会在每次仿真时更新。

### 工作限值

您可以按功率和最大工作电压指定工作限值。如果您将 **Modeling option** 参数设置为 `Show thermal port`（请参阅 Model Thermal Effects），则还可以按温度指定工作限值。

当超过工作限值时，模块可以生成警告，也可以因错误而停止仿真。有关详细信息，请参阅 Operating Limits parameters 部分。

### 故障

要对 Diffusion Resistor 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Diffusion Resistor 模块允许您将电气故障建模为电阻的瞬时变化。该模块可以触发故障事件：

- 在特定时间。
- 当电流超过最大允许值的时间长于特定时间间隔时。

如果您想在特定时间触发故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Timed`。如果您想确定系统是否发生故障，以及如果发生故障，何时发生故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Behavioral`。

当电阻器发生故障时，其电阻会变为您为 **Faulted zero-voltage resistance** 参数指定的值。

### 热噪声

Diffusion Resistor 模块可以生成热噪声电流。如果您将 **Noise mode** 参数设置为 `Enabled`，则该模块包含一个与扩散电阻器并联连接的噪声电流源。

如果采样时间为 *h*，则热噪声由下式给出：

iN=2kT/RN(0,1)h

其中：

- *k* 是玻尔兹曼常数，1.3806504e-23 J/K。
- *T* 是温度。
- *R* 是电阻。
- *N* 是均值为零、标准差为一的高斯随机数。
- *2kT/R* 是双边热噪声功率分布（单边等效值为 *4kT/R*）。

该模块通过使用 Simscape™ Foundation 库中的 PS Random Number 源生成高斯噪声。您可以通过设置 **Repeatability** 参数来控制随机数种子：

- `Not repeatable` — 每次仿真模型时，模块都会使用 MATLAB 随机数生成器重置随机种子：

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — 模块会自动生成一个种子值并将其存储在模块内部，以便始终使用相同的随机数开始仿真。当您从模块库向模型添加 Diffusion Resistor 模块时，会设置此自动生成的种子值。当您从模型中的现有 Diffusion Resistor 模块创建新副本时，会生成新的种子值。模块使用上面显示的 MATLAB 随机数生成器命令设置该值。
- `Specify seed` — 如果您选择此选项，则附加的 **Seed** 参数允许您直接指定随机数种子值。

### 热效应建模

您可以公开热端口，以指定电阻值如何随温度变化并设置热质量。要公开热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

使用 **Variables** 设置来设置初始温度目标。

如果您将 **Modeling option** 参数设置为 `Show thermal port`，则电阻的定义方程会增加额外的温度缩放：

R=R0(1+TC1effΔT+TC2eff(ΔT)2)(1−p2−p3+p21+(θ2vpn)2+p31+|θ3vpn|33)

其中 TC1eff 和 TC2eff 分别是线性温度缩放系数和二次温度缩放系数。

ΔT=Tsim−Tmeas

其中：

- *T*sim 是仿真温度。
- *T*meas 是测量温度。

公开热端口后，生成的噪声在确定瞬时噪声值时会使用热端口处的温度。公开热端口还会扩展 **Operating Limits** 选项卡上的选项，如下所示：

- **Power rating** 参数变为与温度相关。您需要定义一个温度，在该温度及以下可获得完整功率额定值，再定义一个更高温度，在该温度下功率额定值降为零。假设功率额定值在这两个值之间随温度线性下降。
- 附加参数 **Operating temperature range, [Tmin Tmax]** 允许您定义模块运行的有效温度范围。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

本节仅对公开热端口的模块显示。**Temperature** 变量允许您为仿真开始时的温度指定高优先级目标。

### 基本假设和限制

启用噪声进行仿真会减慢仿真速度。请选择采样时间（*h*），使噪声仅在感兴趣的频率处生成，而不会在更高频率处生成。
