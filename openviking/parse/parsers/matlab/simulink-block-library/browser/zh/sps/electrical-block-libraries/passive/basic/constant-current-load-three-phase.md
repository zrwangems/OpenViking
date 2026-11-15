---
type: simulink-block
title: 'Constant Current Load (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'constantcurrentloadthreephase'
documentation_source_path: 'ref/constantcurrentloadthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Current Load (Three-Phase)

## 端口

### 守恒

### **~** — 三相电压电气

与三相电压关联的可扩展三相电气端口。

## 参数

### **建模选项** — 对复合还是展开的三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

对复合还是展开的三相端口进行建模。

复合三相端口使用单个模块端口表示三个独立电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

展开三相端口使用三个独立电气守恒端口表示三相系统的各相。

### 主

### **消耗电流（RMS）** — 均方根消耗电流 `1` `A`（默认）| scalar

模块消耗的均方根电流。

### **最小电源电压（相间 RMS）** — 最小电源电压 `10` `V`（默认）| scalar

电源必须提供的最小电压（以相间 RMS 为单位），以使模块作为电流负载工作。

### 故障

### **开路故障** — 用于添加开路故障的选项 `Add fault`（默认）

用于在 Constant Current Load (Three-Phase) 模块中添加开路故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **开路电导** — 开路电导 `1e-4` `S`（默认）| scalar

开路状态期间的电导。

#### 依赖关系

要启用此参数，请在 **开路故障** 参数中单击 **Add fault** 超链接，向 Constant Current Load (Three-Phase) 模块添加故障。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当您打开含故障的模块时，会显示 **打开故障检查器** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **触发故障时间** — 进入故障状态之前的时间 `0` `s`（默认）| nonnegative scalar

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Timed`。

### **最大允许功率** — 触发故障转换的功率阈值 `inf` `W`（默认）

最大允许功率值。如果功率超过此值的时间长于 **超过功率时的故障时间** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **超过功率时的故障时间** — 功率超过阈值的最大持续时间 `1` `s`（默认）

功率可以超过最大允许值而不触发故障的最长时间。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

三相恒流负载

Constant Current Load (Three-Phase) 模块为三相电源实现恒流负载。

只要三相电源的电压等于或大于 **最小电源电压（相间 RMS）** 参数指定的值，此模块消耗的电流就等于 **消耗电流（RMS）** 参数的值。

当三相电源的电压降至 **最小电源电压（相间 RMS）** 的值以下时，负载行为发生变化，模块将对具有恒定电阻的负载进行建模。

### 方程

如果三相电压平衡，则相间 RMS 电压由以下方程定义：

VlineRMS=(va−vdc)2+(vb−vdc)2+(vc−vdc)2,

其中 vdc=va+vb+vc3。

三相中每一相的电流由以下方程定义：

ik(t)=vk(t)Requiv,

其中 *Requiv* 是等效电阻，其取决于 **最小电源电压（相间 RMS）** 参数的值。

如果三相电源的电压大于 **最小电源电压（相间 RMS）** 参数指定的值，则等效电阻由以下方程定义：

Requiv=vpk2IRMSconsumed,

其中 *vpk* 是电压峰值，*IRMSconsumed* 是 **消耗电流（RMS）** 参数的值。

如果三相电源的电压小于 **最小电源电压（相间 RMS）** 参数指定的值，则等效电阻由以下方程定义：

Requiv=vphRMSminIRMSconsumed,

其中 vphRMSmin=vlineRMSmin3 是相对地 RMS 最小电压。

### 故障

要在 Constant Current Load (Three-Phase) 模块中对故障建模，请在 **故障** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

Constant Current Load (Three-Phase) 模块允许您将电气故障建模为开路。该模块可以触发故障事件，方式为：

- 在特定时间
- 当功率限制被超过的时间长于特定时间
  间隔时

### 潮流分析

如果模块所在网络与频率-时间仿真模式兼容，您可以对该网络执行潮流分析。潮流分析提供稳态值，可用于初始化电机。

有关详细信息，请参阅使用 Simscape Electrical 执行潮流分析和频率和时间仿真模式。
