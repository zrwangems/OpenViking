---
type: simulink-block
title: 'Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'inductor'
documentation_source_path: 'ref/inductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Inductor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气端口
  direction: conserving
- name: '-'
  summary: 负极端子电气端口
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气端口

与电感正极端子关联的电气守恒端口。

### **-** — 负极端子电气端口

与电感负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Inductance
  summary: 标称电感值 1e-6 H（默认）
  group: 主要
- name: Tolerance (%)
  summary: 电感容差，以百分比表示 20（默认）
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
- name: Series resistance
  summary: 电感的等效串联电阻 0 Ohm（默认）
  group: 主要
- name: Parallel conductance
  summary: 与电感关联的并联泄漏路径 1e-9 1/Ohm（默认）
  group: 主要
- name: Enable operating limits
  summary: 选择 Yes 以启用超出工作限值时的报告 No（默认）| Yes
  group: 工作限值
- name: Reporting when operating limits exceeded
  summary: 选择报告方法 Warn（默认）| Error
  group: 工作限值
- name: Saturation current
  summary: 电感饱和电流 1 A（默认）
  group: 工作限值
- name: Power rating
  summary: 电感中的最大功率耗散 1 W（默认）
  group: 工作限值
- name: Inductor fault
  summary: 对电感中的故障建模的选项 Add fault（默认）
  group: 故障
- name: Location of fault node (% of total turns from - terminal)
  summary: 与模块 – 端口接触的子电感中的匝数百分比 50（默认）| (0,100) 范围内的标量
  group: 故障
- name: Faulted coupling factor
  summary: 两个子电感之间的互感耦合 0.9999（默认）| [0,1) 范围内的标量
  group: 故障
- name: Short-circuit turns
  summary: 选择故障是否导致其中一个段短路 No（默认）| To negative terminal | To positive terminal
  group: 故障
- name: Open-circuit at fault node
  summary: 选择是否在段之间应用开路故障 No（默认）| Yes
  group: 故障
- name: Ground fault
  summary: 选择故障是否导致其中一个段短路 No（默认）| Negative terminal side of fault node | Positive terminal side of fault node
  group: 故障
- name: Conductance of faulted ground path
  summary: 两个子电感之间的互感耦合 1 1/Ohm（默认）| 非负标量
  group: 故障
- name: Fault transition time constant
  summary: 过渡到故障状态的时间常数 1e-3 s（默认）| 正标量
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible voltage
  summary: 故障过渡的电压阈值 100 V（默认）| 正标量
  group: 故障
- name: Number of events to fail when exceeding voltage
  summary: 电压超过阈值的最大次数 1（默认）| 正标量
  group: 故障
- name: Maximum permissible current
  summary: 故障过渡的电流阈值 1 A（默认）| 正标量
  group: 故障
- name: Time to fail when exceeding current
  summary: 电流超过阈值的最大持续时间 1 s（默认）| 非负标量
  group: 故障
```

### 主要

### **Inductance** — 标称电感值 `1e-6` `H`（默认）

标称电感值。电感值必须大于零。

### **Tolerance (%)** — 电感容差，以百分比表示 `20`（默认）

制造商数据手册中定义的电感容差。

### **Tolerance application** — 选择仿真期间如何应用容差 `None — use nominal value`（默认）| `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择仿真期间如何应用容差：

- `None — use nominal value` — 模块不应用容差，使用标称电感值。
- `Random tolerance` — 模块在容差限值范围内对电感值应用随机偏移。您可以通过 **Tolerance distribution** 参数选择使用均匀分布或高斯分布来计算随机数。
- `Apply maximum tolerance value` — 电感增加指定的容差百分比值。
- `Apply minimum tolerance value` — 电感减少指定的容差百分比值。

### **Tolerance distribution** — 选择分布类型 `Uniform`（默认）| `Gaussian`

选择随机容差的分布类型：

- `Uniform` — 均匀分布
- `Gaussian` — 高斯分布

#### 依赖关系

当 **Tolerance application** 参数设置为 `Random tolerance` 时启用。

### **Number of standard deviations for quoted tolerance** — 用于计算高斯随机数 `4`（默认）

用于计算高斯随机数的标准差数量。

#### 依赖关系

当 **Tolerance distribution** 参数设置为 `Gaussian` 时启用。

### **Series resistance** — 电感的等效串联电阻 `0` `Ohm`（默认）

电感的等效串联电阻（ESR），有时在制造商数据手册中给出。默认值与 Simscape Foundation 库的 Inductor 模块一致。如果您对故障建模，请为此参数指定正值。

### **Parallel conductance** — 与电感关联的并联泄漏路径 `1e-9` `1/Ohm`（默认）

与电感关联的并联泄漏路径。某些电路的仿真可能需要存在较小的并联电导。您也可以使用此参数来对电感磁芯损耗建模。

### 工作限值

### **Enable operating limits** — 选择 `Yes` 以启用超出工作限值时的报告 `No`（默认）| `Yes`

选择 `Yes` 以启用超出工作限值时的报告。**Operating Limits** 部分中的关联参数将变为可见，以便您选择报告方法并以功率和电流的形式指定工作限值。

### **Reporting when operating limits exceeded** — 选择报告方法 `Warn`（默认）| `Error`

选择超出工作限值时发生的情况：

- `Warn` — 模块发出警告。
- `Error` — 仿真停止并报错。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为 `Yes`。

### **Saturation current** — 电感饱和电流 `1` `A`（默认）

制造商数据手册中定义的电感饱和电流。如果电流超过此值，磁芯材料进入饱和。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为 `Yes`。

### **Power rating** — 电感中的最大功率耗散 `1` `W`（默认）

与电感关联的电阻和电导元件中的最大瞬时功率耗散。

#### 依赖关系

要启用此参数，请将 **Enable operating limits** 设置为 `Yes`。

### 故障

### **Inductor fault** — 对电感中的故障建模的选项 `Add fault`（默认）

对 Inductor 模块中的故障建模的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Location of fault node (% of total turns from - terminal)** — 与模块 – 端口接触的子电感中的匝数百分比 `50`（默认）| (0,100) 范围内的标量

在实践中，故障是通过将电感分割为两个串联连接的耦合子电感来实现的。电感与相应段中匝数的平方成正比，每个子电感的串联电阻与每段中的匝数成正比。并联电导跨越两段。

此参数表示分配给与模块 **–** 端口接触的子电感的匝数百分比。其余匝数分配给另一个子电感。默认值为 `50`，这意味着总电感被分为两个相等的耦合子电感。

#### 依赖关系

要启用此参数，请通过点击 **Inductor fault** 参数中的 **Add fault** 超链接向 Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，**Open Fault Inspector** 超链接将代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Faulted coupling factor** — 两个子电感之间的互感耦合 `0.9999`（默认）| [0,1) 范围内的标量

两个子电感之间互感耦合的故障值。支配这种构造的微分方程在完美耦合的极限下会失效，因此耦合应小于 1。值为 `0` 对应于子电感之间完全没有耦合。从物理上讲，这对应于影响电感磁芯内磁通的故障。这可能是磁芯材料的裂纹，或绕组脱离磁芯。

此参数的默认值也是模块在计算未故障状态下的可故障电感时使用的内部值。对于不可故障的电感，只求解一个方程，这对应于完美互感耦合的理想情况。

#### 依赖关系

要启用此参数，请通过点击 **Inductor fault** 参数中的 **Add fault** 超链接向 Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，**Open Fault Inspector** 超链接将代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Short-circuit turns** — 选择故障是否导致其中一个段短路 `No`（默认）| `To negative terminal` | `To positive terminal`

选择故障是否导致其中一个子电感段短路：

- `No` — 故障不产生短路。
- `To negative terminal` — 故障使与模块 **–** 端口接触的子电感短路。
- `To positive terminal` — 故障使与模块 **+** 端口接触的子电感短路。

#### 依赖关系

要启用此参数，请通过点击 **Inductor fault** 参数中的 **Add fault** 超链接向 Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，**Open Fault Inspector** 超链接将代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Open-circuit at fault node** — 选择是否在段之间应用开路故障 `No`（默认）| `Yes`

选择是否在两个子电感段之间应用开路故障。即使存在开路故障，子电感的特性仍可能相关，具体取决于 **Faulted coupling factor** 参数的值：

- 如果耦合因子不为零，则子电感彼此电隔离，但仍磁耦合。从物理上讲，这对应于绕组断裂。
- 耦合因子为零时，子电感在电气和磁方面均隔离。

#### 依赖关系

要启用此参数，请通过点击 **Inductor fault** 参数中的 **Add fault** 超链接向 Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，**Open Fault Inspector** 超链接将代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Ground fault** — 选择故障是否导致其中一个段短路 `No`（默认）| `Negative terminal side of fault node` | `Positive terminal side of fault node`

选择在故障情况下是否存在电流流向接地节点的路径：

- `No` — 故障不导致与地连接。
- `Negative terminal side of fault node` — 与模块 **–** 端口接触的一侧连接到地。
- `Positive terminal side of fault node` — 与模块 **+** 端口接触的一侧连接到地。

如果 **Open-circuit at fault node** 参数设置为 `Yes`，您需要指定哪一侧（负极或正极）连接到地。如果没有开路，两个选项的行为类似。从物理上讲，这对应于绕组与接地磁芯或机壳之间的绝缘击穿。

#### 依赖关系

要启用此参数，请通过点击 **Inductor fault** 参数中的 **Add fault** 超链接向 Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，**Open Fault Inspector** 超链接将代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Conductance of faulted ground path** — 两个子电感之间的互感耦合 `1` `1/Ohm`（默认）| 非负标量

如果存在接地故障，此参数表示到地的电流路径的电导。例如，如果到地的路径是通过磁芯材料，则根据所使用的磁芯材料指定较小的电导值。对于高导电性磁芯材料或机壳短路，请指定较高的电导值。

#### 依赖关系

要启用此参数，请通过点击 **Inductor fault** 参数中的 **Add fault** 超链接向 Inductor 模块添加故障，并将 **Ground fault** 设置为 `Negative terminal side of fault node` 或 `Positive terminal side of fault node`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，**Open Fault Inspector** 超链接将代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Fault transition time constant** — 过渡到故障状态的时间常数 `1e-3` `s`（默认）| 正标量

与过渡到故障状态关联的时间常数，如故障中所述。

#### 依赖关系

要启用此参数，请通过点击 **Inductor fault** 参数中的 **Add fault** 超链接向 Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，**Open Fault Inspector** 超链接将代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible voltage** — 故障过渡的电压阈值 `100` `V`（默认）| 正标量

故障过渡的电压阈值。如果电压值超过此阈值一定次数（由 **Number of events to fail when exceeding voltage** 参数值指定），则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Number of events to fail when exceeding voltage** — 电压超过阈值的最大次数 1（默认）| 正标量

由于基于电压的失效的物理机制取决于发生一次或多次局部放电事件，此参数允许您设置电感在故障过渡开始之前可以承受的电压超调次数。请注意，模块不检查处于过压条件的时间，只检查过渡次数。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible current** — 故障过渡的电流阈值 `1` `A`（默认）| 正标量

故障过渡的电流阈值。如果电流超过此值的时间长于 **Time to fail when exceeding current** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding current** — 电流超过阈值的最大持续时间 `1` `s`（默认）| 非负标量

电流可以超过最大允许值而不触发故障的最大持续时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023a: 使用单个参数实现故障的时间或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并由 **Fault trigger** 参数替代。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。您只能启用一个触发器。

如果您在早期版本中创建了模型并同时启用了时间触发器和行为触发器，现在仅启用时间触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果会有所不同。

如果您想在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果您想确定系统是否失效以及何时失效，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

电感，包括可选容差、工作限值和故障行为

Inductor 模块允许您对线性电感进行建模，包括以下效应：

- 容差
- 工作限值
- 故障

您可以相互独立地打开和关闭这些建模选项。当所有附加选项均关闭时，组件行为与 Simscape™ Foundation 库中的 Inductor 模块相同。

在其最简单的形式中，Inductor 模块对线性电感进行建模，用以下方程描述：

V=LdIdt

其中：

- *V* 是电压。
- *L* 是电感。
- *I* 是电流。
- *t* 是时间。

要对非线性电感进行建模，请使用 Nonlinear Inductor 模块。

### 容差

您可以对为 **Inductance** 参数提供的标称值应用容差。数据手册通常会给出给定电感类型的容差百分比。下表显示了模块如何根据所选的 **Tolerance application** 选项应用容差并计算电感。

| 选项 | 电感值 |
| --- | --- |
| `None — use nominal value` | *L* |
| `Random tolerance` | 均匀分布：*L* · (1 – *tol* + 2· *tol*· `rand`)  高斯分布：*L* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *L* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *L* · (1 – *tol* ) |

表中，

- *L* 是 **Inductance** 参数值，即标称电感。
- *tol* 是分数容差，即 **Inductance tolerance (%)** /100。
- *nSigma* 是您为 **Number of standard deviations for quoted tolerance** 参数提供的值。
- `rand` 和 `randn` 是用于生成均匀分布和正态分布随机数的标准 MATLAB® 函数。

**注意**

如果您选择 `Random tolerance` 选项并且处于“Fast Restart”模式，则只要分数容差 *tol* 或 **Number of standard deviations for quoted tolerance** *nSigma* 中至少有一个设置为 Run-time 并且用变量定义（即使您未修改该变量），随机容差值就会在每次仿真时更新。

### 工作限值

电感通常以特定的饱和电流进行额定，并且可能还有最大允许功耗。您可以依据这些值指定工作限值，以便在电感被驱动超出其规格时生成警告或错误。

当超过工作限值时，模块可以生成警告或以错误停止仿真。有关详细信息，请参阅工作限值参数部分。

### 故障

要对 Inductor 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

电感参数的瞬时变化是不符合物理实际的。因此，当 Inductor 模块进入故障状态时，短路和开路电压会在一段时间内过渡到其故障值，基于以下公式：

*`CurrentValue`* = *`FaultedValue`* – (*`FaultedValue`* – *`UnfaultedValue`*) · `sech`(∆t / τ)

其中：

- ∆t 是自故障条件发生以来的时间。
- τ 是与故障过渡相关的用户定义时间常数。

对于短路故障，短路路径的电导也根据 `sech`(∆t / τ) 函数从小值（表示开路路径）变化到大值。

模块可以触发故障过渡的开始：

- 在特定时间。
- 在电压超过最大允许值一定次数之后。
- 当电流超过最大允许值的时间长于特定时间间隔时。

如果您想在特定时间触发故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Timed`。如果您想确定系统是否发生故障以及何时发生故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Behavioral`。

如果您选择行为触发，则一旦其中一个触发条件为真，组件就会发生故障。

可发生故障的电感通常要求您使用定步长局部求解器，尤其是当您的模型过渡到包含短路的故障状态时。有关详细信息，请参阅 Making Optimal Solver Choices for Physical Simulation。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

**Inductor current** 变量允许您为仿真开始时的初始电感电流指定高优先级目标。
