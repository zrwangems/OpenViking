---
type: simulink-block
title: 'Incandescent Lamp'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'incandescentlamp'
documentation_source_path: 'ref/incandescentlamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Incandescent Lamp

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

与灯正电压相关联的电气守恒端口。

### **-** — 负极端子电气

与灯负电压相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 模块参数化 Specify resistance values directly（默认）| Specify currents
  group: 电阻
- name: Initial resistance at turn-on
  summary: 开启时的初始电阻 0.15 Ohm（默认）
  group: 电阻
- name: Steady-state resistance when on
  summary: 导通时的稳态电阻 1 Ohm（默认）
  group: 电阻
- name: Inrush current at turn-on
  summary: 开启时的浪涌电流 70 A（默认）
  group: 电阻
- name: Steady-state current when on
  summary: 导通时的稳态电流 10 A（默认）
  group: 电阻
- name: Rated voltage
  summary: 灯额定电压 12 V（默认）
  group: 电阻
- name: Resistance temperature coefficient
  summary: 电阻温度系数 0.004 1/K（默认）
  group: 电阻
- name: Thermal time constant
  summary: 热时间常数 25 ms（默认）
  group: 动态特性
- name: Initial lamp state
  summary: 初始灯状态 Off（默认）| On
  group: 动态特性
- name: Open circuit fault
  summary: 添加开路故障的选项 Add fault（默认）
  group: 故障
- name: Open-circuit resistance
  summary: 开路电阻 1e6 Ohm（默认）
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态前的时间 0 s（默认）| 非负标量
  group: 故障
```

### 电阻

### **Parameterization** — 模块参数化 `Specify resistance values directly`（默认）| `Specify currents`

选择以下方法之一进行模块参数化：

- `Specify resistance values
  directly` — 提供灯丝在开启时和稳态导通时的电阻值。模块根据这些值确定传热系数的值。这是默认选项。
- `Specify currents` —
  提供灯丝在开启时和稳态导通时的电流值。模块根据这些值确定传热系数的值。

### **Initial resistance at turn-on** — 开启时的初始电阻 `0.15` `Ohm`（默认）

灯初始开启时外部电路所看到的电阻。

#### 依赖关系

此参数仅在 **Parameterization** 参数选择 `Specify resistance values directly` 时可见。

### **Steady-state resistance when on** — 导通时的稳态电阻 `1` `Ohm`（默认）

灯导通并处于稳态时外部电路所看到的电阻。此电阻应大于 **Initial resistance at turn-on**。

#### 依赖关系

此参数仅在 **Parameterization** 参数选择 `Specify resistance values directly` 时可见。

### **Inrush current at turn-on** — 开启时的浪涌电流 `70` `A`（默认）

灯初始开启时通过灯的电流。

#### 依赖关系

此参数仅在 **Parameterization** 参数选择 `Specify currents` 时可见。

### **Steady-state current when on** — 导通时的稳态电流 `10` `A`（默认）

灯导通并处于稳态时通过灯的电流。此电流应小于 **Inrush current at turn-on**。

#### 依赖关系

此参数仅在 **Parameterization** 参数选择 `Specify currents` 时可见。

### **Rated voltage** — 灯额定电压 `12` `V`（默认）

灯的额定电压，以及导通和开启状态下提供电阻或电流值所对应的电压值。

### **Resistance temperature coefficient** — 电阻温度系数 `0.004` `1/K`（默认）

温度每升高一个单位时电阻的分数增量。

### 动态特性

### **Thermal time constant** — 热时间常数 `25` `ms`（默认）

灯开启或关闭时灯丝温度的一阶热时间常数。

### **Initial lamp state** — 初始灯状态 `Off`（默认）| `On`

在 `On` 和 `Off` 之间选择。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

在 Incandescent Lamp 模块中添加开路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Open-circuit resistance** — 开路电阻 `1e6` `Ohm`（默认）

灯发生开路时灯丝电阻的值。

#### 依赖关系

要启用此参数，请通过点击 **Open circuit fault** 参数中的 **Add fault** 超链接向 Incandescent Lamp 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开一个包含故障的模块时，会出现 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

对于大于此参数值的仿真时间，灯丝电阻变为等于 **Open-circuit resistance**。为此参数指定有限值可让您模拟灯泡烧坏时的故障动态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

具有温度相关电阻的白炽灯

Incandescent Lamp 模块对白炽灯进行建模，其主要特性是电阻随灯丝升温而增大。

在灯丝热损失率与环境温差成正比的简化假设下，灯丝温度由下式决定

ktcdTdt=i2R−kT

灯丝电阻由以下方程决定

R=R0(1+αT)

其中：

- *R0* 是开启时的初始电阻（当灯丝处于环境温度时）。
- *T* 是灯丝相对于环境温度的温度。
- α 是电阻温度系数。
- *tc* 是热时间常数。
- *k* 是传热系数。
- *R* 是灯丝电阻。
- *i* 是灯丝电流。

有两种参数化选项：

- 如果选择 `Specify resistance values directly`，模块使用您提供的导通时和开启时的灯丝电阻值来确定传热系数的值。
- 如果选择 `Specify currents`，模块使用您提供的导通时和开启时的灯丝电流值来确定传热系数的值。

### 故障

要对 Incandescent Lamp 模块中的故障进行建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Incandescence Lamp 模块允许您将电气故障建模为开路电阻。该模块可以在特定时间触发故障事件。当处于开路状态时，灯电阻被设置为 **Open-circuit resistance** 参数的值。
