---
type: simulink-block
title: 'Constant Power Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'constantpowerload'
documentation_source_path: 'ref/constantpowerload.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Power Load

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与恒功率负载正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与恒功率负载负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Load type
  summary: 负载类型 DC（默认）| AC
  group: 主
- name: Power consumed
  summary: 消耗功率 100 W（默认）| 标量
  group: 主
- name: Minimum supply voltage
  summary: 最小直流电源电压 20 V（默认）| 标量
  group: 主
- name: Reverse conductance
  summary: 反向电导 1e-6 S（默认）| 标量
  group: 主
- name: Transition voltage width
  summary: 过渡电压宽度 1e-3 V（默认）| 标量
  group: 主
- name: Active power consumed
  summary: 消耗有功功率 500 W（默认）| 标量
  group: 主
- name: Reactive power consumed
  summary: 消耗无功功率 0 V*A（默认）| 标量
  group: 主
- name: Rated frequency
  summary: 额定频率 60 Hz（默认）| 标量
  group: 主
- name: Minimum supply voltage (RMS)
  summary: 最小交流电源电压 200 V（默认）| 标量
  group: 主
- name: Voltage time constant
  summary: 电压动态时间常数 0.01 s（默认）| 正标量
  group: 主
- name: Initial supply voltage (RMS)
  summary: 初始端子电压 300 V（默认）| 正标量
  group: 主
- name: Initial supply voltage angle
  summary: 初始端子电压角度 0 deg（默认）| 标量
  group: 主
- name: Open circuit fault
  summary: 添加开路故障的选项 Add fault（默认）
  group: 故障
- name: Open-circuit conductance
  summary: 开路电导 1e-4 S（默认）| 标量
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态前的时间 0 s（默认）| 非负标量
  group: 故障
```

### 主

### **Load type** — 负载类型 `DC`（默认）| `AC`

负载类型。选择 `DC` 以将此负载用于直流电源，或选择 `AC` 以将此负载用于交流电源。

### **Power consumed** — 消耗功率 `100` `W`（默认）| 标量

模块消耗的标称功率。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Minimum supply voltage** — 最小直流电源电压 `20` `V`（默认）| 标量

直流电源需要提供给模块以使模块作为恒功率负载运行的最小电压。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Reverse conductance** — 反向电导 `1e-6` `S`（默认）| 标量

电源电压变为负值时的反向电导值。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Transition voltage width** — 过渡电压宽度 `1e-3` `V`（默认）| 标量

用于确保当电源电压降至 **Minimum supply voltage** 以下或变为负值时，模块行为之间平滑过渡的过渡电压宽度。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `DC`。

### **Active power consumed** — 消耗有功功率 `500` `W`（默认）| 标量

模块消耗的有功功率。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Reactive power consumed** — 消耗无功功率 `0` `V*A`（默认）| 标量

模块消耗的无功功率。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Rated frequency** — 额定频率 `60` `Hz`（默认）| 标量

额定频率。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Minimum supply voltage (RMS)** — 最小交流电源电压 `200` `V`（默认）| 标量

交流电源需要提供给模块以使模块作为恒功率负载运行的最小电压（RMS）。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Voltage time constant** — 电压动态时间常数 `0.01` `s`（默认）| 正标量

*自 R2024a 起*

与端子电压测量瞬态相关的时间常数。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Initial supply voltage (RMS)** — 初始端子电压 `300` `V`（默认）| 正标量

*自 R2024a 起*

时间为零时的端子电压（RMS）。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `AC`。

### **Initial supply voltage angle** — 初始端子电压角度 `0` `deg`（默认）| 标量

*自 R2024a 起*

时间为零时的端子电压角度。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `AC`。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

在 Constant Power Load 模块中添加开路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Open-circuit conductance** — 开路电导 `1e-4` `S`（默认）| 标量

开路状态期间的电导。

#### 依赖关系

要启用此参数，请通过点击 **Open circuit fault** 参数中的 **Add fault** 超链接向 Constant Power Load 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：改进了对感性节点的支持

在 R2024a 之前，要将 Constant Power Load 模块连接到感性节点，必须提供较大的寄生电阻。从 R2024a 开始，如果将 **Load type** 参数设置为 `AC`，则可以通过指定 **Voltage time constant**、**Initial supply voltage (RMS)** 和 **Initial supply voltage angle** 参数将此模块连接到感性节点。

## 描述

用于直流或交流电源的恒功率负载

Constant Power Load 模块为直流或交流电源实现恒功率负载。

如果将 **Load type** 参数设置为 `DC`：

- 只要来自直流电源的电压大于或等于 **Minimum supply voltage** 参数值，模块就输出标称额定功率。
- 当来自直流电源的电压降至 **Minimum supply voltage** 参数值以下时，负载行为发生变化，模块作为恒定电阻运行。如果电源电压变为负值，模块作为恒定反向电导运行。

为确保这些行为之间的平滑过渡，模块使用具有连续导数的三阶多项式样条。您可以使用 **Transition voltage width** 参数指定此过渡的宽度。

如果将 **Load type** 参数设置为 `AC`：

- 只要来自交流电源的电压大于或等于 **Minimum supply voltage (RMS)** 参数值，模块就在稳态下输出标称额定功率。模块在谐波近似中计算 RMS 功率，以便模块可以计算具有时变幅值的交流电压信号的功率。如果幅值变化的时间尺度与交流电的周期相当，则瞬时功率在过渡期间会短暂变化。
- 当来自交流电源的电压降至 **Minimum supply voltage (RMS)** 参数值以下时，负载行为发生变化，模块对具有恒定阻抗的负载进行建模。

有关三相系统中 `AC` 负载类型的方程的详细信息，请参阅 Constant Power Load (Three-Phase) 模块的 Equations 部分。

### 故障

要对 Constant Power Load 模块中的故障进行建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Constant Power Load 模块允许您将电气故障建模为开路。模块可以在特定时间触发故障事件。

### 潮流分析

如果模块所在的网络与频率-时间仿真模式兼容，则可以对网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。
