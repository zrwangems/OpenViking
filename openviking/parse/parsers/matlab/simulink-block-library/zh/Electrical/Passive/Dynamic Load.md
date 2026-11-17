---
type: simulink-block
title: 'Dynamic Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'dynamicload'
documentation_source_path: 'ref/dynamicload.html'
language: zh-CN
chinese_source: worker-translation
---

# Dynamic Load

## 端口

### 输入

### **P** — 有功功率，W 物理信号

与有功功率关联的物理信号端口，指定为标量。

### **Q** — 无功功率，V\*A 物理信号

与无功功率关联的物理信号端口，指定为标量。
### 守恒

### **+** — 正极端子 电气

与动态负载正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与动态负载负极端子关联的电气守恒端口。

## 参数

### 主

### **Load type** — 负载类型 `DC`（默认）| `AC`

负载类型。选择 `DC` 以将此负载用于直流电源，或选择 `AC` 以将此负载用于交流电源。

### **Minimum supply voltage** — 最小直流电源电压 `20` `V`（默认）| 标量

直流电源需要提供给模块以使其作为恒功率负载运行的最小电压。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Minimum consumed power** — 最小消耗功率 `1e-3` `W`（默认）| 标量

模块消耗的最小功率量。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Reverse conductance** — 反向电导 `1e-6` `S`（默认）| 标量

当电源电压变为负值时的反向电导值。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Transition voltage width** — 过渡电压宽度 `1e-3` `V`（默认）| 标量

过渡电压宽度。当电源电压降至 **Minimum supply voltage** 以下或变为负值时，此值用于确保模块行为之间的平滑过渡。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Rated frequency** — 额定频率 `60` `Hz`（默认）| 标量

额定频率。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Minimum supply voltage (RMS)** — 最小交流电源电压 `200` `V`（默认）| 标量

交流电源需要提供给模块以使其作为动态负载运行的最小电压（RMS）。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Voltage time constant** — 电压动态时间常数 `0.01` `s`（默认）| 正标量

*自 R2024a 起*

与端子电压测量瞬态相关的时间常数。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Initial supply voltage (RMS)** — 初始端子电压 `300` `V`（默认）| 正标量

*自 R2024a 起*

零时刻的端子电压（RMS）。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Initial supply voltage angle** — 端子电压初始角度 `0` `deg`（默认）| 标量

*自 R2024a 起*

零时刻的端子电压角度。

#### 依赖

要启用此参数，请将 **Load Type** 设置为 `AC`。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

在 Dynamic Load 模块中添加开路故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Open-circuit conductance** — 开路电导 `1e-4` `S`（默认）| 标量

开路状态期间的电导。

#### 依赖

要启用此参数，请通过单击 **Open circuit fault** 参数中的 **Add fault** 超链接向 Dynamic Load 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开包含故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Timed`。

## 所属库

Simscape / Electrical / Passive

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2024a：改进了对感性节点和双向有功功率输入的支持

在 R2024a 之前，要将 Dynamic Load 模块连接到
感性节点，必须提供较大的寄生电阻。从 R2024a 开始，如果将
**Load type** 参数设置为 `AC`，
则可以通过指定 **Voltage
time constant**、**Initial supply voltage (RMS)** 和
**Initial supply voltage angle** 参数，将此模块连接到感性节点。由于
此更改，**Minimum active power** 参数已被
移除。如果您的模型保存在较早版本中并包含此模块，则必须为新参数设置
适当的值。

Dynamic Load 模块现在还会根据输入有功功率
*Pin* 的极性来消耗或
生成有功功率。如果
*Pin* 大于 0，则该模块
消耗有功功率。如果 *Pin* 小于
0，则该模块生成有功功率。

## 描述

用于直流或交流电源的动态负载

Dynamic Load 模块为直流或交流
电源实现动态负载。

如果将 **Load type** 参数设置为
`DC`：

- 只要 **P**
  端口的值大于 **Minimum
  consumed power** 参数的值，并且直流电源的电压
  等于或大于 **Minimum
  supply voltage** 参数指定的值，该模块消耗的功率就等于 **P**
  端口的值。
- 当直流电源的电压降至
  **Minimum supply voltage** 以下时，
  负载行为会发生变化，该模块表现为电阻性
  负载。如果电源电压变为负值，则该模块
  表现为开路电导。

为确保这些行为之间的平滑过渡，该模块使用具有连续导数的
三阶多项式样条。您可以使用 **Transition
voltage width** 参数指定此过渡的宽度。

如果将 **Load type** 参数设置为 `AC`，
下表显示了该模块如何根据电源电压 *V* 计算消耗的有功功率和无功功率。

| *V* 值范围 | 消耗的有功功率和无功功率 |
| --- | --- |
| V>Vmin | Pactual=PinQactual=Qin |
| V<Vmin | 该模块对负载建模，其阻抗等于：R=Vmin2PinPin2+Qin2X=Vmin2QinPin2+Qin2Z=R2+X2 |

在这些方程中：

- *Vmin* 是 Minimum supply voltage (RMS)
  参数的值。
- *Pin* 是
  Dynamic Load 模块的输入有功功率，由
  外部输入端口 **P** 确定。
- *Pactual* 是 Dynamic Load 模块消耗的有功
  功率。
- *Qin* 是 Dynamic Load 模块的输入无功功率，
  由
  外部输入端口 **Q** 确定。
- *Qactual* 是 Dynamic Load 模块消耗的无功
  功率。

Dynamic Load 模块根据输入有功功率
*Pin* 的极性来消耗或生成有功
功率。如果
*Pin* 大于 0，则该模块
消耗有功功率。如果 *Pin* 小于 0，
则该模块生成有功功率。

### 故障

要对 Dynamic Load 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Dynamic Load 模块允许您将
电气故障建模为开路。该模块可以在
特定时间触发故障事件。

### 潮流分析

如果该模块所在的网络与
频率-时间仿真模式兼容，则您可以对该
网络执行潮流分析。潮流分析提供稳态值，您可以使用这些值来
初始化电机。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode。
