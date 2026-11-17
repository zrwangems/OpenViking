---
type: simulink-block
title: 'Winding'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'winding'
documentation_source_path: 'ref/winding.html'
language: zh-CN
chinese_source: worker-translation
---

# Winding

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: N
  summary: 北端子磁性
  direction: conserving
- name: S
  summary: 南端子磁性
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与模块正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与模块负极端子关联的电气守恒端口。

### **N** — 北端子磁性

与模块北端子关联的磁性守恒端口。

### **S** — 南端子磁性

与模块南端子关联的磁性守恒端口。
## 参数
```yaml
parameters:
- name: Number of winding turns
  summary: 绕组匝数 10（默认）| 正数
  group: 主
- name: Winding resistance
  summary: 串联电阻 1e-3 Ohm（默认）| 正数
  group: 主
- name: Leakage reluctance
  summary: 并联磁阻 1e5 1/H（默认）| 正数
  group: 主
- name: Parallel conductance
  summary: 并联电导 0 1/Ohm（默认）| 正数
  group: 主
- name: Thermal port
  summary: 是否对热端口建模 Omit（默认）| Model
  group: 热端口
- name: Measurement temperature
  summary: 测量温度 25 K（默认）
  group: 热端口
- name: Resistance temperature coefficient
  summary: 电阻温度系数 3.93e-3 1/K（默认）
  group: 热端口
- name: Winding Thermal mass
  summary: 绕组热质量 100 J/K（默认）
  group: 热端口
- name: Winding fault
  summary: 对绕组中的故障建模的选项 Add fault（默认）
  group: 故障
- name: Location of fault node (% of total turns from - terminal)
  summary: 与故障绕组 – 端口接触的子电感中的匝数百分比 50（默认）| (0,100) 范围内的标量
  group: 故障
- name: Short-circuit turns
  summary: 选择故障是否导致其中一个段短路 No（默认）| To negative terminal | To positive terminal
  group: 故障
- name: Open-circuit at fault node
  summary: 选择是否在两个段之间施加开路故障 No（默认）| Yes
  group: 故障
- name: Ground fault
  summary: 选择故障是否导致其中一个段短路 No（默认）| Negative terminal side of fault node | Positive terminal side of fault node
  group: 故障
- name: Conductance of faulted ground path
  summary: 两个子电感之间的互感耦合 0 1/Ohm（默认）| 非负标量
  group: 故障
- name: Fault transition time constant
  summary: 过渡到故障状态的时间常数 1e-3 s（默认）| 正标量
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认）| Timed | Behavioral | Additional triggers | Conditional | Manual
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
- name: Trigger configuration
  summary: 启用附加触发类型的选项 Open fault properties
  group: 故障
```

### 主

### **Number of winding turns** — 绕组匝数 `10`（默认）| 正数

变压器绕组上的导线匝数。

### **Winding resistance** — 串联电阻 `1e-3` `Ohm`（默认）| 正数

绕组中的功率损耗。

### **Leakage reluctance** — 并联磁阻 `1e5` `1/H`（默认）| 正数

绕组中的磁通损耗。如果您不想在 Winding 模块内部对漏磁进行建模，请将此参数设置为 `inf`。

### **Parallel conductance** — 并联电导 `0` `1/Ohm`（默认）| 正数

并联泄漏路径。某些电路的仿真可能需要存在一个小的并联电导。

### 热端口

### **Thermal port** — 是否对热端口建模 `Omit`（默认）| `Model`

是否对绕组的热端口建模。热端口报告绕组电阻损耗。

### **Measurement temperature** — 测量温度 `25` `K`（默认）

绕组参数的标称温度。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Model`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值为铜的值。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Model`。

### **Winding Thermal mass** — 绕组热质量 `100` `J/K`（默认）

绕组的热质量值。热质量是使温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Model`。

### 故障

### **Winding fault** — 对绕组中的故障建模的选项 `Add fault`（默认）

对 Winding 模块中的故障建模的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Location of fault node (% of total turns from - terminal)** — 与故障绕组 – 端口接触的子电感中的匝数百分比 `50`（默认）| (0,100) 范围内的标量

通过将故障绕组分割为两个串联耦合的子电感来启用故障。电感与相应段中匝数的平方成正比，每个子电感的串联电阻与每段中的匝数成正比。并联电导跨越两段。

此参数表示分配给与故障绕组 **–** 端口接触的子电感的匝数百分比。其余匝数分配给另一个子电感。默认值为 `50`，这意味着故障绕组的总电感被分为两个相等的耦合子电感。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数的 **Add fault** 超链接。

### **Short-circuit turns** — 选择故障是否导致其中一个段短路 `No`（默认）| `To negative terminal` | `To positive terminal`

选择故障是否导致其中一个子电感段短路：

- `No` — 故障不产生短路。
- `To negative terminal` — 故障使与模块 **–** 端口接触的子电感短路。
- `To positive terminal` — 故障使与模块 **+** 端口接触的子电感短路。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接。

### **Open-circuit at fault node** — 选择是否在两个段之间施加开路故障 `No`（默认）| `Yes`

选择是否在两个子电感段之间施加开路故障。即使存在开路故障，子电感的特性仍然相关，因为即使在故障状态下它们仍然磁耦合。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接。

### **Ground fault** — 选择故障是否导致其中一个段短路 `No`（默认）| `Negative terminal side of fault node` | `Positive terminal side of fault node`

选择在故障情况下是否存在电流流向接地节点的路径：

- `No` — 故障不导致接地连接。
- `Negative terminal side of fault node` — 与模块 **–** 端口接触的一侧连接到地。
- `Positive terminal side of fault node` — 与模块 **+** 端口接触的一侧连接到地。

如果 **Open-circuit at fault node** 参数设置为 `Yes`，则必须指定哪一侧（负极或正极）连接到地。如果没有开路，两个选项的行为类似。物理上，这对应于绕组与接地铁芯或机壳之间的绝缘击穿。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接。

### **Conductance of faulted ground path** — 两个子电感之间的互感耦合 `0` `1/Ohm`（默认）| 非负标量

接地电流路径的电导。例如，如果接地路径通过铁芯材料，则根据所使用的铁芯材料指定一个较小的电导值。对于高导电性铁芯材料或机壳短路，请指定较高的电导值。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接，并将 **Ground fault** 设置为 `Negative terminal side of fault node` 或 `Positive terminal side of fault node`。

### **Fault transition time constant** — 过渡到故障状态的时间常数 `1e-3` `s`（默认）| 正标量

与过渡到故障状态相关的时间常数，如 Faults 中所述。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Behavioral` — 故障由于仿真期间的故障参数值而注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障由于模块对话框中不可用的附加触发器而注入。选择此选项并点击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由于反映信号相关行为的条件而注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为真时，模块进入故障状态，并在仿真的其余时间保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为真时模块进入故障状态，当触发条件为假时模块进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible voltage** — 故障过渡的电压阈值 `100` `V`（默认）| 正标量

故障过渡的电压阈值。如果电压值超过此阈值一定次数（由 **Number of events to fail when exceeding voltage** 参数值指定），则模块进入故障状态。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Number of events to fail when exceeding voltage** — 电压超过阈值的最大次数 `1`（默认）| 正标量

电感在故障过渡开始之前可以承受的电压超限次数。此模块不检查处于过压条件的时间，只检查过渡次数。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Maximum permissible current** — 故障过渡的电流阈值 `1` `A`（默认）| 正标量

故障过渡的电流阈值。如果电流连续超过此值的时间超过 **Time to fail when exceeding current** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding current** — 电流超过阈值的最大持续时间 `1` `s`（默认）| 非负标量

在故障触发之前，电流必须连续超过最大允许电流的时间量。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数中的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2025a：对可逆条件故障建模

您现在可以通过清除 **Trigger stays on once activated** 参数，在 Winding 模块中对可逆条件故障建模。当触发条件为真时模块进入故障状态，当触发条件为假时模块进入非故障状态。

在 R2025a 之前，当触发条件首次变为真时模块进入故障状态，并在仿真的其余时间保持故障状态。

如果您在 R2025a 之前创建了模型并在 Winding 模块中启用了条件故障，则模块现在默认选择 **Trigger stays on once activated** 参数以保持向后兼容性。

### R2023a：使用单个参数实现故障的时间或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并由 **Fault trigger** 参数替代。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。您只能启用一个触发器。

如果您在早期版本中创建了模型并同时启用了时间触发器和行为触发器，则现在只启用时间触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果会有所不同。

如果您想在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果您想确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

具有欧姆损耗和磁通损耗的电磁转换器

Winding 模块表示具有绕组电阻和漏磁阻的电磁转换器。您可以将此模块用作构建自定义变压器的基本组件。对于理想电磁转换器，请参阅 Electromagnetic Converter。

当您在模块的电气端口上施加正电流时，会在磁性端子之间感应出正磁动势（MMF）。

F=Ni

其中：

- *ℱ* 是模块磁性端子之间的 MMF
- *N* 是绕组匝数
- *i* 是通过绕组的电流

当您在模块的磁性端子上施加正时变磁通时，会在模块的电气端子上感应出负电压。

v=−Ndϕdt+N2Rldidt+Rwi

其中：

- *φ* 是通过模块磁性端子的磁通
- *i* 是通过模块电气端子的电流
- *ℛl* 是漏磁阻
- *Rw* 是绕组电阻
- *ℱ* 是模块磁性端子之间的磁动势
- *v* 是模块电气端子上的电压降

下图显示了模块的等效电路。

在图中，*φ*mp 对应主路径磁通，*φ* 对应总磁通。您可以在模块的 **Variables** 选项卡中设置总磁通的初始条件。

### 故障

要在 Winding 模块中建模故障，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

绕组参数的瞬时变化是非物理的。因此，当 Winding 模块进入故障状态时，短路和开路电压会根据以下公式在一段时间内过渡到其故障值：

*`CurrentValue`* =
*`FaultedValue`* –
(*`FaultedValue`* –
*`UnfaultedValue`*) · `sech`(∆t
/ τ)

其中：

- ∆t 是自故障条件发生以来的时间。
- τ 是与故障过渡相关的用户定义时间常数。

对于短路故障，短路路径的电导也会根据 `sech`(∆t / τ) 函数从小值（表示开路路径）变化到大值。

可发生故障的绕组通常要求您使用定步长局部求解器，尤其是当您的模型过渡到包含短路的故障状态时。有关详细信息，请参阅 Making Optimal Solver Choices for Physical Simulation。

**故障触发器**

您通过使用 **Trigger type** 参数来指定故障发生的方式和时间。

如果将 **Trigger type** 设置为 `Behavioral`，则 Winding 模块会在以下情况下触发故障事件：

- 电流连续超过 **Maximum permissible current** 参数的值，且持续时间长于 **Time to fail when exceeding current** 参数的值。
- 电压超过 **Maximum permissible voltage** 的次数达到 **Number of events to fail when exceeding voltage** 参数值所指定的次数。

如果将 **Trigger type** 设置为 `Conditional`，您可以选择 Winding 模块中的故障是否可逆 *(自 R2025a 起)*。要建模不可逆故障，请单击 **Open fault properties** 以打开 Property Inspector，并选择 **Trigger stays on once activated** 参数。当触发条件第一次变为 true 时，模块进入故障状态，并在仿真的其余时间内保持故障状态。要建模可逆故障，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。

有关向模块添加故障以及指定故障触发器的详细信息，请参阅 Introduction to Simscape Faults。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
