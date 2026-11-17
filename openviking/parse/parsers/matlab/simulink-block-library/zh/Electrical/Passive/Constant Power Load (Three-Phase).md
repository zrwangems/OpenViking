---
type: simulink-block
title: 'Constant Power Load (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'constantpowerloadthreephase'
documentation_source_path: 'ref/constantpowerloadthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Power Load (Three-Phase)

## 端口

### 守恒端口

### **~** — 三相电压电气

与三相电压关联的复合三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — A 相电压电气

与 A 相电压关联的扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — B 相电压电气

与 B 相电压关联的扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — C 相电压电气

与 C 相电压关联的扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

## 参数

### 主要

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各个相。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）| 正标量

*自 R2023a 起*

额定电气频率。

### **Active power consumed** — 消耗的有功功率 `1` `kW`（默认）| 标量

模块消耗的有功功率。

### **Reactive power consumed** — 消耗的无功功率 `0` `A*kV`（默认）| 标量

模块消耗的无功功率。

### **Minimum supply voltage (phase-to-phase RMS)** — 最低电源电压 `100` `V`（默认）| 正标量

电源使模块作为恒功率负载运行所需的最低电压，以相间 RMS 表示。

### **Voltage time constant** — 电压动态时间常数 `0.01` `s`（默认）| 正标量

*自 R2023a 起*

与端子电压测量瞬态相关的时间常数。

### **Initial supply voltage (phase-to-phase RMS)** — 初始端子电压 `200` `V`（默认）| 正标量

*自 R2023a 起*

时间为零时的端子电压，以相间 RMS 表示。

### **Initial supply voltage angle** — 时间为零时 A 相的端子电压角度 `0` `deg`（默认）| 标量

*自 R2023a 起*

时间为零时 A 相的端子电压角度。

### **Parasitic conductance to electrical reference** — 到电气参考的寄生电导 `1e-6` `S`（默认）| 非负标量

*自 R2023a 起*

到电气参考的寄生电导。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

在 Constant Power Load (Three-Phase) 模块中添加开路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Open-circuit conductance** — 开路电导 `1e-4` `S`（默认）| 标量

开路状态期间的电导。

#### 依赖关系

要启用此参数，请通过点击 **Open circuit fault** 参数中的 **Add fault** 超链接，向 Constant Power Load (Three-Phase) 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开包含故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

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

**在 R2020b 中引入**

### R2023a：改进了对感性节点的支持

在 R2023a 之前，要将 Constant Power Load (Three-Phase) 模块连接到感性节点，您必须提供较大的寄生电阻。从 R2023a 开始，您可以通过指定 **Rated electrical frequency**、**Voltage time constant**、**Initial supply voltage (phase-to-phase RMS)**、**Initial supply voltage angle** 和 **Parasitic conductance to the electrical reference** 参数，将此模块连接到感性节点。如果您的模型保存在早期版本中并包含此模块，则必须为这些参数设置适当的值。

此外，该模块的 **Modeling option** 参数已重命名为 **Electrical connection**，并移至 **Main** 部分。

## 描述

三相恒功率负载

Constant Power Load (Three-Phase) 模块为三相电源实现恒功率负载。

只要三相电源的电压等于或大于 **Minimum supply voltage (phase-to-phase RMS)** 参数指定的值，该模块就输出标称额定功率。

当三相电源的电压降至 **Minimum supply voltage (phase-to-phase RMS)** 的值以下时，负载行为发生变化，模块对恒阻抗负载进行建模。

### 方程

当三相电源的电压大于 **Minimum supply voltage (phase-to-phase RMS)** 参数指定的值时，模块以恒 PQ 模式运行。

有功功率和无功功率定义为：

P=32VpkIpkcos(φV−φI)Q=32VpkIpksin(φV−φI)

其中：

- *Vpk* 是电压峰值幅度。
- φI=φV−atan(QP) 是电流的相位。
- Ipk=23PVpkcos(φV−φI) 是电流峰值幅度。

在第一个周期内，峰值电流等于 0 A。

当三相电源的电压小于或等于 **Minimum supply voltage (phase-to-phase RMS)** 参数指定的值时，模块以恒 Z 模式运行。

有功功率和无功功率定义为：

P=32Vpk2RR2+X2Q=32Vpk2XR2+X2

其中：

- R=V2line RMSminPP2+Q2 是恒定电阻。
- X=V2line RMSminQP2+Q2 是恒定电抗。
- *Vline RMSmin* 是 **Minimum supply voltage (phase-to-phase RMS)**。

### 潮流分析

如果模块所在的网络与频率-时间仿真模式兼容，您可以对网络执行潮流分析。潮流分析提供稳态值，您可以使用这些值来初始化电机。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。

### 故障

要对 Constant Power Load (Three-Phase) 模块中的故障进行建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Constant Power Load (Three-Phase) 模块允许您将电气故障建模为开路。该模块可以在特定时间触发故障事件。
