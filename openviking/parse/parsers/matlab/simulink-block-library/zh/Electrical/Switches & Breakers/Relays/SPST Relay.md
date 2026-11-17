---
type: simulink-block
title: 'SPST Relay'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers / Relays'
documentation_page: 'spstrelay'
documentation_source_path: 'ref/spstrelay.html'
language: zh-CN
chinese_source: worker-translation
---

# SPST Relay

## 端口
```yaml
ports:
- name: PS
  summary: 物理信号控制物理信号
  direction: input
- name: x
  summary: 继电器状态物理信号
  direction: output
- name: S
  summary: 常闭触点电气
  direction: output
- name: C
  summary: 公共触点电气
  direction: output
- name: +
  summary: 绕组正极端子电气
  direction: output
- name: '-'
  summary: 绕组负极端子电气
  direction: output
```

### 输入

### **PS** — 物理信号控制物理信号

为使继电器通电和断电的物理信号输入端口。

#### 依赖

要启用此端口，请在**Main**设置中将**Control port**参数设置为
`PS`。
### 输出

### **x** — 继电器状态物理信号

继电器在**C**-**S**连接方面的状态：

- 1 — 闭合连接
- 0 — 断开连接

#### 依赖

要启用此端口，请在**Main**设置中将**State port**参数设置为
`Visible`。
### 守恒

### **S** — 常闭触点电气

与 SPST 继电器常闭触点关联的电气守恒端口。

### **C** — 公共触点电气

与 SPST 继电器公共触点关联的电气守恒端口。

### **+** — 绕组正极端子电气

与 SPST 继电器绕组正电压端子关联的电气守恒端口。通过绕组的电流控制继电器
状态。

#### 依赖

要启用此端口，请在**Main**设置中将**Control port**参数设置为
`Electrical`。

### **-** — 绕组负极端子电气

与 SPST 继电器绕组负电压端子关联的电气守恒端口。通过绕组的电流控制继电器
状态。

#### 依赖

要启用此端口，请在**Main**设置中将**Control port**设置为
`Electrical`。
## 参数
```yaml
parameters:
- name: Control port
  summary: 输入端口选择 PS（默认）| Electrical
  group: 主要参数
- name: Closed resistance
  summary: 连接触点电阻 0.01 Ohm（默认）| 正标量
  group: 主要参数
- name: Open conductance
  summary: 开路电导 1e-8 1/Ohm（默认）| 正标量
  group: 主要参数
- name: Threshold
  summary: 继电器阈值 0（默认）| 非负标量
  group: 主要参数
- name: State port
  summary: 继电器状态输出端口可见性 Hidden（默认）| Visible
  group: 主要参数
- name: Rated voltage
  summary: 额定电压 5 V（默认）| 正标量
  group: Winding
- name: Percent rated voltage to energize
  summary: 使继电器通电的额定电压百分比 75（默认）| 正标量
  group: Winding
- name: Percent rated voltage to de-energize
  summary: 使继电器断电的额定电压百分比 25（默认）| 正标量
  group: Winding
- name: Winding inductance
  summary: 绕组电感 0.08 H（默认）| 正标量
  group: Winding
- name: Winding series resistance
  summary: 绕组串联电阻 12.5 Ohm（默认）| 正标量
  group: Winding
- name: Winding parallel conductance
  summary: 绕组并联电导 1e-9 1/Ohm（默认）| 正标量
  group: Winding
- name: Time-to-break C-S connection
  summary: 断开 C-S 连接的延迟时间 0 s（默认）| 非负标量
  group: Mechanical
- name: Time-to-make C-S connection
  summary: 建立 C-S 连接的延迟时间 0 s（默认）| 非负标量
  group: Mechanical
- name: Switch fault
  summary: 添加开关故障的选项 Add fault
  group: 故障
- name: Switch fault
  summary: 开关故障模型 C-S stuck closed（默认）| C open circuit (no path to S) | Degraded contact resistance
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认）| Timed | Behavioral | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum load permissible current
  summary: 故障转换的负载电流阈值 inf A（默认）| 正标量
  group: 故障
- name: Time to fail when exceeding current
  summary: 超过电流时发生故障的时间 1 s（默认）| 正标量
  group: 故障
- name: Trigger configuration
  summary: 启用附加触发类型的选项 Open fault properties
  group: 故障
- name: Degraded contact resistance
  summary: 退化触点电阻 1e-9 Ohm（默认）| 正标量
  group: 故障
- name: Time constant for degraded contact resistance
  summary: 退化触点电阻的时间常数 1e-3（默认）| 正标量
  group: 故障
- name: Winding fault
  summary: 添加绕组故障的选项 Add fault
  group: 故障
- name: Time constant for winding open circuit transition
  summary: 绕组失效的时间常数 1e-3 s（默认）| 正标量
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认）| Timed | Behavioral | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible winding voltage
  summary: 最大允许绕组电压 inf V（默认）| 正标量
  group: 故障
- name: Number of events to fail when exceeding voltage
  summary: 超过电压时失效的事件数 1（默认）| 正标量整数
  group: 故障
- name: Maximum permissible winding current
  summary: 最大允许绕组电流 inf A（默认）| 正标量
  group: 故障
- name: Time to fail when exceeding winding current
  summary: 超过绕组电流时失效的时间 1 s（默认）| 正标量
  group: 故障
- name: Trigger configuration
  summary: 启用附加触发类型的选项 Open fault properties
  group: 故障
```

### 主要参数

### **Control port** — 输入端口选择 `PS`（默认）| `Electrical`

继电器状态控制方法，指定为：

- `PS` —
  **PS**物理信号输入
  端口
- `Electrical` —
  与继电器绕组端子关联的
  **+**和**-**
  电气守恒端口

下表显示了此参数如何影响**Main**设置中其他
参数的可见性。要了解如何阅读该表，请参阅参数依赖关系

****Control Port** 参数
依赖关系**

| **Control port** | |
| --- | --- |
| `PS` | `Electrical` |
| **Closed resistance** | **Closed resistance** |
| **Open conductance** | **Open conductance** |
| **Threshold** |
| **State port** | **State port** |

### **Closed resistance** — 连接触点电阻 `0.01` `Ohm`（默认）| 正标量

闭合继电器触点两端的电阻。

### **Open conductance** — 开路电导 `1e-8` `1/Ohm`（默认）| 正标量

断开继电器触点两端的电导。

### **Threshold** — 继电器阈值 `0`（默认）| 非负标量

继电器的阈值。如果物理信号输入升至阈值以上，
继电器通电。相反，如果物理信号输入降至
阈值以下，继电器断电。

#### 依赖

要启用此参数，请将**Control port**设置为
`PS`。

### **State port** — 继电器状态输出端口可见性 `Hidden`（默认）| `Visible`

输出继电器状态的物理信号端口的可见性。如果连接闭合，此参数
值为 `1`，否则为
`0`。

要启用 **x** 端口，请将此参数设置为
`Visible`。

### Winding

要启用这些参数，请在**Main**设置中将
**Control port**参数设置为
`Electrical`。

### **Rated voltage** — 额定电压 `5` `V`（默认）| 正标量

在正常工作条件下施加到操作线圈的标准电压。电流
阈值取决于此参数的值。

### **Percent rated voltage to energize** — 使继电器通电的额定电压百分比 `75`（默认）| 正标量

使继电器通电所需的额定电压最小百分比。电流
阈值取决于此参数的值。

### **Percent rated voltage to de-energize** — 使继电器断电的额定电压百分比 `25`（默认）| 正标量

使继电器断电所需的额定电压百分比。电流阈值
取决于此参数的值。

### **Winding inductance** — 绕组电感 `0.08` `H`（默认）| 正标量

绕组电感。

### **Winding series resistance** — 绕组串联电阻 `12.5` `Ohm`（默认）| 正标量

绕组端子之间的电阻。电流阈值取决于此
参数的值。

### **Winding parallel conductance** — 绕组并联电导 `1e-9` `1/Ohm`（默认）| 正标量

绕组电导。

### Mechanical

### **Time-to-break C-S connection** — 断开 C-S 连接的延迟时间 `0` `s`（默认）| 非负标量

当继电器通电时，断开端口
**C**和**S**之间连接的
机械开关时间。

### **Time-to-make C-S connection** — 建立 C-S 连接的延迟时间 `0` `s`（默认）| 非负标量

当继电器断电时，建立端口 **C**
和 **S** 之间连接的机械开关时间。

### 故障

### **Switch fault** — 添加开关故障的选项 `Add fault`

添加开关故障的选项。

要添加故障，请单击 **Add fault**
超链接。

### **Switch fault** — 开关故障模型 `C-S stuck closed`（默认）| `C open circuit (no path to S)` | `Degraded contact resistance`

开关故障模型。

#### 依赖

要启用此参数，请单击 **Switch fault**
参数的 **Add fault**
超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时
  注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time**
  参数指定的值时，故障注入。
- `Behavioral` — 故障因仿真期间的故障
  参数值而注入。将 **Trigger type** 设置为
  `Behavioral` 会启用定义
  故障条件的模块参数。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器
  而注入。选择此选项
  并单击 **Open fault properties** 超链接，以在属性检查器中将
  **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障因反映与信号关联行为的条件
    而注入。
    条件在每个时间步评估
    **Condition** 参数中的布尔表达式。当触发条件首次变为 true 时，
    模块进入故障状态，并在仿真的其余时间保持故障状态。
    要了解更多信息，请参阅创建和管理条件。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，
    故障注入或清除。
    要了解更多信息，请参阅在模型中手动触发故障。

#### 依赖

要启用此参数，请单击 **Switch fault**
参数的 **Add fault**
超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖

要启用此参数，请单击 **Switch fault** 参数的 **Add fault**
超链接，并将 **Trigger type** 设置为
`Timed`。

### **Maximum load permissible current** — 故障转换的负载电流阈值 `inf` `A`（默认）| 正标量

故障转换的电流阈值。如果电流连续超过此值的时间长于 **Time to
fail when exceeding current** 参数的值，则模块进入故障状态。

#### 依赖

要启用此参数，请单击 **Switch fault** 参数的 **Add fault**
超链接，并将 **Trigger type** 设置为
`Behavioral`。

### **Time to fail when exceeding current** — 超过电流时发生故障的时间 `1` `s`（默认）| 正标量

在故障触发之前，电流必须连续超过最大允许电流的
时间量。

#### 依赖关系

要启用此参数，请点击 **Switch fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请点击 **Switch fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。

### **Degraded contact resistance** — 退化触点电阻 `1e-9` `Ohm`（默认）| 正标量

故障 **S** 触点的退化电阻。

#### 依赖关系

要启用此参数，请点击 **Switch fault** 参数的 **Add fault** 超链接，并将 **Switch fault** 设置为 `Degraded contact resistance`。

### **Time constant for degraded contact resistance** — 退化触点电阻的时间常数 `1e-3`（默认）| 正标量

触点电阻降至退化状态的时间常数。

#### 依赖关系

要启用此参数，请点击 **Switch fault** 参数的 **Add fault** 超链接，并将 **Switch fault** 设置为 `Degraded contact resistance`。

### **Winding fault** — 添加绕组故障的选项 `Add fault`

添加绕组故障的选项。

要添加故障，请点击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请将 **Control port** 设置为 `Electrical`。

### **Time constant for winding open circuit transition** — 绕组失效的时间常数 `1e-3` `s`（默认）| 正标量

绕组失效的时间常数。该常数是描述从正常状态过渡到开路状态的特征时间。您可以将其计算为故障发生时响应达到其稳态值 63% 所需的时间。

#### 依赖关系

要启用此参数，请将 **Control port** 设置为 `Electrical`，并点击 **Winding fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到 **Trigger fault at time** 参数指定的值时注入。
- `Behavioral` — 故障因仿真期间的故障参数值而注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器而注入。选择此选项并点击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障因反映信号相关行为的条件而注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请点击 **Winding fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数：

- 将 **Control port** 设置为 `Electrical`。
- 点击 **Winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible winding voltage** — 最大允许绕组电压 `inf` `V`（默认）| 正标量

继电器绕组的最大电压。如果电压超过此值达到第 *k* 次，模块进入故障状态，其中 *k* 是 **Number of events to fail when exceeding voltage** 参数的值。

#### 依赖关系

要启用此参数：

- 将 **Control port** 设置为 `Electrical`。
- 点击 **Winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Number of events to fail when exceeding voltage** — 超过电压时失效的事件数 `1`（默认）| 正标量整数

在开路绕组故障触发之前，继电器必须超过绕组电压阈值的次数。

#### 依赖关系

要启用此参数：

- 将 **Control port** 设置为 `Electrical`。
- 点击 **Winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Maximum permissible winding current** — 最大允许绕组电流 `inf` `A`（默认）| 正标量

故障转换的电流阈值。如果电流连续超过此值的时间超过 **Time to fail when exceeding winding current** 参数的值，模块进入故障状态。

#### 依赖关系

要启用此参数：

- 将 **Control port** 设置为 `Electrical`。
- 点击 **Winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding winding current** — 超过绕组电流时失效的时间 `1` `s`（默认）| 正标量

在故障触发之前，电流必须连续超过最大允许电流的时间量。

#### 依赖关系

要启用此参数：

- 将 **Control port** 设置为 `Electrical`。
- 点击 **Winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数：

- 将 **Control port** 设置为 `Electrical`。
- 点击 **Winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Additional triggers`。
## 所属库

Simscape / Electrical / Switches & Breakers / Relays

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a：使用 Simscape faults 接口实现故障

SPST Relay 模块现在支持 Simscape faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

由于此更改，**Faults** 设置中的参数名称和依赖关系已更改。

### R2023a：使用单个参数实现故障的时间触发器或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并由 **Fault trigger** 参数替代。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。您只能启用一个触发器。

如果您在较早版本中创建了模型并同时启用了时间触发器和行为触发器，现在仅启用时间触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果会有所不同。

如果您希望在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果您希望确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

带延迟和故障的单极单掷继电器

SPST Relay 模块对单极单掷继电器进行建模。该模块具有三种可能的状态：

- 失电 — 公共触点 **C** 从与常开触点 **S** 连接变为断开。
- 得电 — 公共触点 **C** 从与常开触点 **S** 断开变为连接。
- 开路 — 继电器断开。公共触点 **C** 未连接到常开触点 **S**。

您可以：

- 使用物理信号输入端口或电气守恒端口控制继电器状态。
- 输出继电器状态。
- 延迟连接的断开和闭合。
- 引入行为故障或时间故障，导致连接卡住、开路或触点电阻退化。

### 继电器状态控制

该模块有两种控制变体：

- 物理信号（PS）控制 — 继电器状态取决于输入物理信号的值与继电器阈值的比较结果。继电器阈值 *th* 是您为 **Threshold** 参数指定的值。
- 电气控制 — 继电器状态取决于流过正负电气守恒端口（代表继电器绕组）的电流与继电器上限和下限阈值的比较结果。上限和下限阈值取决于您为 **Winding** 设置中的参数指定的值。

对于 PS 控制变体，在仿真开始时：

- 如果输入信号 *PS* 小于或等于 *th*，则继电器失电，公共触点 **C** 与常开触点 **S** 断开。
- 如果输入信号 *PS* 大于 *th*，则继电器得电，**C** 连接到常开触点 **S**。

仿真开始后，如果 *PS* 上升到 *th* 以上，模块从失电状态变为得电状态，**C**–**S** 连接在 **Time-to-make C-S connection** 中指定的延迟后闭合。

如果模块从得电状态变为失电状态，即 *PS* 下降到 *th* 或以下，**C**–**S** 连接在 **Time-to-break C-S connection** 中指定的延迟后断开。

对于电气控制变体，上限和下限阈值取决于为 **Rated voltage**、**Percent rated voltage to energize**、**Percent rated voltage to de-energize** 和 **Winding series resistance** 参数指定的值。额定电流为：

irated=Vratedrcoil.

上限电流阈值 *ienergized* 的方程为：

ienergized\_current=Rated Voltage\*Percent rated voltage to energizeWinding series resistance .

下限电流阈值 *ide-energized* 的方程为：

ide−energized\_current=Rated Voltage\*Percent rated voltage to de−energizeWinding series resistance .

在仿真开始时，如果控制电流大于 *ienergized*，则继电器得电，**C** 连接到常开触点 **S**。

仿真开始后，如果电流上升到 *ienergized* 以上，模块从失电状态变为得电状态。**C**–**S** 连接在 **Time-to-make C-S connection** 中指定的延迟后闭合。

如果电流下降到 *ide-energized* 以下，模块从得电状态变为失电状态。**C**–**S** 连接在 **Time-to-break C-S connection** 中指定的延迟后断开。

### 输出继电器状态

要查看继电器状态，请暴露端口 **x**，这是一个输出每个连接状态的物理信号端口。要暴露 **x** 端口，请在 **Main** 设置中将 **State port** 设置为 `Visible`。

下表显示了继电器状态与连接状态的关系。闭合连接的状​​态为 1。断开连接的状态为 0。

**继电器和连接状态**

| **C**–**S** 连接状态 | 继电器状态 |
| --- | --- |
| 0 | 失电或开路 |
| 1 | 得电 |

### 连接延迟

您可以在 **Mechanical** 设置中指定闭合和断开连接的延迟。下表显示了闭合和断开时间延迟如何影响触点 **S1** 和 **S2** 与公共触点 **C** 之间的连接。

| **Mechanical** 设置 | 继电器状态 | **C**–**S** 连接状态 | 结果，**C**–**S** 为蓝色，**PS** 为黄色 |
| --- | --- | --- | --- |
| | 参数 | 值 | | --- | --- | | **Time-to-break C-S connection** | `0` | | **Time-to-make C-S connection** | `0` | | 失电 | 0 |  |
| 得电 | 1 |
| | 参数 | 值 | | --- | --- | | **Time-to-break C-S connection** | > `0` | | **Time-to-make C-S connection** | `0` | | 失电 | 1, 0 |  |
| 得电 | 1 |
| | 参数 | 值 | | --- | --- | | **Time-to-break C-S connection** | `0` | | **Time-to-make C-S connection** | > `0` | | 失电 | 0 |  |
| 得电 | 0, 1 |

### 故障

要在 SPST Relay 模块中对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

您可以向绕组添加开关故障或开路故障。如果添加开关故障，可以将 **Switch fault** 参数设置为：

- `C-S stuck closed`
- `C open circuit (no path to S)`
- `Degraded contact resistance`

您可以使用 **Trigger type** 参数指定故障发生的方式和时间。

有关向模块添加故障以及指定故障触发的详细信息，请参阅 Introduction to Simscape Faults。

****C**–**S** 常闭故障**

如果公共触点 **C** 在机械、电气或化学上粘滞到常闭触点 **S**，则会发生 **C**–**S** 常闭故障。此类故障的原因包括：

- 触点熔焊，可能是由于浪涌电流或分断电流超过额定值或负载短路。
- 机械损坏。
- 绝缘劣化。
- 感性电压。

**C**–**S** 常闭故障的连接状态等于 `1`。

**C**–**S** 常闭行为故障只有在负载电流超过电流阈值的时间超过行为触发时间阈值时才会发生。也就是说，行为故障只有在以下情况下才会发生：

iload>ith，

并且

ti>i\_th>tth\_b，

其中：

- *iload* 是负载电流。
- *ith* 是 **Maximum permissible load current** 参数的指定值。
- *ti>i\_th* 是超过电流阈值的时间。
- *tth\_b* 是 **Time to fail when exceeding current** 参数的指定值。

当故障触发时，如果 **C**–**S** 为：

- 闭合 — **C**–**S** 在仿真的剩余时间内保持闭合。
- 断开 — 除非继电器通电并且 **C**–**S** 连接闭合，否则故障不会生效。一旦闭合，**C**–**S** 连接将在仿真的剩余时间内保持闭合。

****C** 开路（无通向 **S** 的路径）故障**

如果公共触点 **C** 在机械上卡在断开位置，则会发生 **C** 开路（无通向 **S** 的路径）故障。此类故障可能发生在以下情况：

- 存在触点损坏或劣化。
- 开关连接器在继电器中部发生机械卡滞。

**C** 开路（无通向 **S** 的路径）故障的故障状态等于 `0`。

**C** 开路行为故障只有在负载电流超过电流阈值的时间超过行为触发时间阈值时才会发生。也就是说，行为故障只有在以下情况下才会发生：

iload>ith，

然后

ti>i\_th>tth\_b，

其中：

- *iload* 是负载电流。
- *ith* 是 **Maximum permissible load current** 参数的指定值。
- *ti>i\_th* 是超过电流阈值的时间。
- *tth\_b* 是 **Time to fail when exceeding current** 参数的指定值。

当超过时间故障阈值时，如果：

- 继电器处于开路状态，也就是说，连接已断开且尚未接通，则继电器在仿真的剩余时间内保持断开。
- **C**–**S** 连接已闭合，则除非继电器断电并且已闭合的连接断开，否则故障不会生效。如果连接断开，继电器将变为开路，并在仿真的剩余时间内保持断开。

当超过行为故障阈值时，如果：

- 继电器处于开路状态，也就是说，连接已断开且尚未接通，则继电器在仿真的剩余时间内保持断开。
- **C**–**S** 连接已闭合，则继电器状态立即变为开路，并在仿真的剩余时间内保持开路。

**退化触点电阻故障**

退化触点电阻故障的原因包括：

- 过度使用引起的过载条件。高浪涌电流和电压会导致过载条件，继电器的过度切换也会导致过载条件。过载条件最终会触发电弧，从而产生热量并使触点材料退化。
- 干扰继电器触点操作的化学污染。污染物可能包括氧化膜或外来颗粒，往往会产生高且不稳定的接触电阻读数。
- 继电器寿命终止。

**C**–**S** 连接的退化触点电阻故障的故障状态等于 0 或 1。

当时间故障首次发生时，**S** 的接触电阻为：

rcontact\_s(t)=rcontact\_fault\_s−(rcontact\_fault\_s−rcontact)sech(t−tth\_tτ)，

其中：

- *rcontact\_fault\_s* 是故障 **S** 接触电阻的最终值。
- *rcontact* 是未故障 **S** 接触电阻。
- *tth\_t* 是 **Trigger fault at time** 参数的值。

退化触点电阻行为故障只有在负载电流超过电流阈值的时间超过行为触发时间阈值时才会发生。也就是说，行为故障只有在以下情况下才会发生：

iload>ith，

然后

ti>i\_th>tth\_b，

其中：

- *iload* 是负载电流。
- *ith* 是 **Maximum permissible load current** 参数的指定值。
- *ti>i\_th* 是超过电流阈值的时间。
- *tth\_b* 是 **Time to fail when exceeding current** 参数的指定值。

对于行为故障，如果 iS−C>ith 在时间区间 *tth\_b* 内连续成立，

rcontact\_s(t)=rcontact\_fault\_s−(rcontact\_fault\_s−rcontact)sech(ti>i\_th−tth\_bτ)，

其中：

- *iS-C* 是公共触点至常闭触点 **C**–**S** 的电流。
- *ith* 是 **Maximum permissible load current** 参数的指定值。
- *tth\_b* 是 **Time to fail when exceeding current** 参数的指定值。
- *rcontact\_fault\_s* 是故障 **S** 接触电阻的最终值。
- *rcontact* 是未故障 **S** 接触电阻。
- *τ* 是 **Time constant for degraded contact resistance** 参数的值。

当 **C**–**S** 连接超过时间故障阈值时，接触电阻立即退化，并在仿真的剩余时间内保持退化。

当 **C**–**S** 超过行为故障阈值时，就 *iS-C* 而言，**C**–**S** 连接的电阻立即退化，并在仿真的剩余时间内保持退化。

**绕组开路故障**

开路绕组故障仅适用于电气控制变体。绕组线圈中的开路可能导致此类故障。

对于定时故障，模块将绕组电流近似为：

Ldidt+Ri=vwinding\*sech(t−tth\_tτ)，

其中：

- *L* 是绕组电感。
- *R* 是绕组电阻。
- *i* 是绕组电流。
- *vwinding* 是绕组两端电压。
- *tth\_t* 是 **Trigger fault at time** 参数的值。
- *τ* 是 **Time constant for winding open circuit transition** 参数的值。

绕组中的行为故障只有在满足以下条件之一时才会发生：

- 绕组电流超过电流阈值的时间超过行为触发时间阈值。
- 绕组电压超过电压阈值的次数超过电压过载次数阈值。

也就是说，行为故障只有在以下情况下才会发生：

iwinding>ith

然后

ti>i\_th>tth\_b，

其中：

- *iwinding* 是绕组电流。
- *ith* 是 **Maximum permissible winding current** 参数的指定值。
- *ti>i\_th* 是超过电流阈值的时间。
- *tth\_b* 是 **Time to fail when exceeding current** 参数的指定值。

或者如果：

vwinding>vth，

并且随后

Nv>v\_th>Nth，

其中：

- *vwinding* 是绕组电压。
- *vth* 是 **Maximum permissible winding voltage** 参数的指定值。
- *Nv>v\_th* 是超过电压阈值的次数。
- *Nth* 是 **Number of events to fail when exceeding voltage** 参数的指定值。

一旦故障触发，**C**–**S** 在仿真的剩余时间内保持闭合。
