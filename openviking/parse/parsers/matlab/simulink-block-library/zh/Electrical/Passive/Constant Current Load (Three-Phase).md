---
type: simulink-block
title: 'Constant Current Load (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'constantcurrentloadthreephase'
documentation_source_path: 'ref/constantcurrentloadthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Current Load (Three-Phase)

## 端口
```yaml
ports:
- name: '~'
  summary: 三相电压电气端口
  direction: conserving
```

### 守恒端口

### **~** — 三相电压电气端口

与三相电压关联的可扩展三相电气端口。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 选择建模为复合三相端口还是扩展三相端口 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Consumed current (RMS)
  summary: 消耗电流的均方根值 1 A（默认）| 标量
  group: 主参数
- name: Minimum supply voltage (phase-to-phase RMS)
  summary: 最小供电电压 10 V（默认）| 标量
  group: 主参数
- name: Open circuit fault
  summary: 添加开路故障的选项 Add fault（默认）
  group: 故障
- name: Open-circuit conductance
  summary: 开路电导 1e-4 S（默认）| 标量
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible power
  summary: 故障转换的功率阈值 inf W（默认）
  group: 故障
- name: Time to fail when exceeding power
  summary: 功率超过阈值的最长时间 1 s（默认）
  group: 故障
```

### **Modeling option** — 选择建模为复合三相端口还是扩展三相端口 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择建模为复合三相端口还是扩展三相端口。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各相。

### 主参数

### **Consumed current (RMS)** — 消耗电流的均方根值 `1` `A`（默认）| 标量

模块消耗的电流均方根值。

### **Minimum supply voltage (phase-to-phase RMS)** — 最小供电电压 `10` `V`（默认）| 标量

电源必须提供的最小相间均方根电压，以使模块作为电流负载工作。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

用于在 Constant Current Load (Three-Phase) 模块中添加开路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Open-circuit conductance** — 开路电导 `1e-4` `S`（默认）| 标量

开路状态下的电导。

#### 依赖关系

要启用此参数，请通过点击 **Open circuit fault** 参数中的 **Add fault** 超链接，向 Constant Current Load (Three-Phase) 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible power** — 故障转换的功率阈值 `inf` `W`（默认）

最大允许功率值。如果功率超过此值的时间长于 **Time to fail when exceeding power** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding power** — 功率超过阈值的最长时间 `1` `s`（默认）

功率可以超过最大允许值而不触发故障的最长时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

三相恒定电流负载

Constant Current Load (Three-Phase) 模块为三相电源实现恒定电流负载。

只要三相电源的电压等于或大于 **Minimum supply voltage (phase-to-phase RMS)** 参数指定的值，此模块就消耗等于 **Consumed current (RMS)** 参数值的电流。

当三相电源的电压降至 **Minimum supply voltage (phase-to-phase RMS)** 的值以下时，负载行为发生变化，模块将建模为恒定电阻负载。

### 方程

如果三相电压平衡，则相间均方根电压由以下方程定义：

VlineRMS=(va−vdc)2+(vb−vdc)2+(vc−vdc)2,

其中 vdc=va+vb+vc3。

三相中每一相的电流由以下方程定义：

ik(t)=vk(t)Requiv,

其中 *Requiv* 是等效电阻，取决于 **Minimum supply voltage (phase-to-phase RMS)** 参数的值。

如果三相电源的电压大于 **Minimum supply voltage (phase-to-phase RMS)** 参数指定的值，则等效电阻定义为：

Requiv=vpk2IRMSconsumed,

其中 *vpk* 是电压峰值幅值，*IRMSconsumed* 是 **Consumed current (RMS)** 参数的值。

如果三相电源的电压小于 **Minimum supply voltage (phase-to-phase RMS)** 参数指定的值，则等效电阻定义为：

Requiv=vphRMSminIRMSconsumed,

其中 vphRMSmin=vlineRMSmin3 是相对地均方根最小电压。

### 故障

要在 Constant Current Load (Three-Phase) 模块中建模故障，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Constant Current Load (Three-Phase) 模块允许您将电气故障建模为开路。该模块可以通过以下方式触发故障事件：

- 在特定时间
- 当功率限制被超过的时间长于特定时间间隔时

### 潮流分析

如果模块所在的网络与频率-时间仿真模式兼容，您可以对网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。
