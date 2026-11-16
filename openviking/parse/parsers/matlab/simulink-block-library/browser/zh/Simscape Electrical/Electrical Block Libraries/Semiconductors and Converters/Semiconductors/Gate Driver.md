---
type: simulink-block
title: 'Gate Driver'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'gatedriver'
documentation_source_path: 'ref/gatedriver.html'
language: zh-CN
chinese_source: worker-translation
---

# Gate Driver

## 端口

### 输入

### **u** — 控制信号，无量纲物理信号

指定输入控制值的输入物理信号。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为
`PS input`。
### 守恒

### **PWM** — 脉宽调制信号电气

与脉宽调制信号关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **REF** — 浮动零伏参考电气

与浮动零伏参考关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **G** — 栅极连接电气

与栅极关联的电气守恒端口。将此端口连接到 MOSFET 或 IGBT 模块的栅极。

### **S** — 源极或发射极连接电气

与源极或发射极关联的电气守恒端口。
将此端口连接到 MOSFET 模块的源极或 IGBT 模块的发射极。

## 参数

### **Modeling option** — 是否对电气或物理信号输入端口建模 `PS input`（默认）| `Electrical input ports`

是否对物理信号或电气输入端口建模。

### 输入逻辑

### **Logic 1 input value** — 逻辑 1 的信号值 0.7（默认）

对应于逻辑 1 电平的输入信号值。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为
`PS input`。

### **Logic 0 input value** — 逻辑 0 的信号值 0.3（默认）

对应于逻辑 0 电平的输入信号值。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为
`PS input`。

### **Logic 1 input voltage** — 逻辑 1 的电压值 2.0 V（默认）

对应于逻辑 1 电平的输入电压值。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **Logic 0 input voltage** — 逻辑 0 的电压值 0.8 V（默认）

对应于逻辑 0 电平的输入电压值。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### 输出

### **On-state gate-source voltage** — 导通状态所需的输出电压 15 V（默认）

驱动器处于导通状态时所需的输出电压。

### **Off-state gate-source voltage** — 关断状态所需的输出电压 0 V（默认）

驱动器处于关断状态时所需的输出电压。

### 时序

### **Propagation delay (logic 0->logic 1)** — 开通传播延迟 50 ns（默认）

当输入上升到逻辑 1 输入电平以上时，输出状态从关断到导通的转换在等于开通传播延迟的延迟之后开始。

### **Propagation delay (logic 1->logic 0)** — 关断传播延迟 50 ns（默认）

当输入下降到逻辑 0 输入值以下时，输出状态从导通到关断的转换在等于关断传播延迟的延迟之后开始。

### 动态特性

### **Parameterization** — 选择驱动器参数化 `Output impedance`（默认）| `Rise and fall times`

选择驱动器参数化类型：

- `Output impedance` — 指定
  导通状态和关断状态的栅极驱动电阻。
- `Rise and fall times` —
  指定上升时间、下降时间和负载电容。

### **On-state gate drive resistance** — 导通状态的栅极驱动电阻 2 Ω（默认）

导通状态下的栅极驱动电阻。

#### 依赖项

当 **Parameterization** 参数设置为 `Output impedance` 时启用。

### **Off-state gate drive resistance** — 关断状态的栅极驱动电阻 2 Ω（默认）

关断状态下的栅极驱动电阻。

#### 依赖项

当 **Parameterization** 参数设置为 `Output impedance` 时启用。

### **Rise time** — 驱动器上升时间 20 ns（默认）

驱动器上升时间，从 10% 到 90%。

#### 依赖项

当 **Parameterization** 参数设置为 `Rise and fall times` 时启用。

### **Fall time** — 驱动器下降时间 20 ns（默认）

驱动器下降时间，从 90% 到 10%。

#### 依赖项

当 **Parameterization** 参数设置为 `Rise and fall times` 时启用。

### **Load capacitance for rise and fall times** — 驱动器负载电容 10 nF（默认）

驱动器负载电容。

#### 依赖项

当 **Parameterization** 参数设置为 `Rise and fall times` 时启用。

### 故障

### **State fault** — 用于对栅极驱动器中的故障状态建模的选项 `Add fault`（默认）

用于对 Gate Driver 模块中的故障状态建模的选项。

要添加故障，请单击 **Add fault**
超链接。

### **Failure mode** — 故障后驱动器的状态 `Fail off`（默认）| `Fail on`

选择驱动器是通过使所连接的半导体器件永久关断还是永久导通来发生故障。

#### 依赖项

要启用此参数，请通过单击 **State fault** 参数中的 **Add fault** 超链接，向 Gate Driver 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| nonnegative scalar

模块进入故障状态的仿真时间。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

栅极驱动器集成电路的行为模型

Gate Driver 模块提供栅极驱动器集成电路的抽象表示。该模块对输入迟滞、传播延迟以及开通/关断动态特性进行建模。除非显式地对栅极驱动器电路建模，否则应始终使用此模块或 Half-Bridge Driver 模块来设置 MOSFET 模块上的栅源电压或 IGBT 模块上的栅射电压。不要将受控电压源直接连接到半导体栅极，因为这会忽略决定开关动态特性的栅极驱动器输出阻抗。

通过将 **Modeling option** 参数设置为以下任一值，可以对电气或物理信号输入端口建模：

- `PS input` — 驱动器输出状态由物理信号输入 u 控制。如果您的所有控制器（包括 PWM 波形生成）都由 Simulink® 模块确定，请使用此建模选项。此建模选项为默认值。
- `Electrical input ports` — 驱动器输出状态由两个电气输入连接 PWM 和 REF 控制。如果您的模型具有上游模拟组件，例如 Controlled PWM Voltage 源，请使用此选项。

当输入上升到逻辑 1 输入电平以上时，输出状态从关断到导通的转换在等于开通传播延迟的延迟之后开始。**G** 和 **S** 端口上的所需输出电压从关断状态输出电压阶跃到导通状态输出电压，但实际输出电压由与 **On-state gate drive resistance** 值和总负载电容相关的 RC 时间常数决定。类似地，当输入下降到逻辑 0 输入值以下时，输出状态从导通到关断的转换在等于关断传播延迟的延迟之后开始，并且其动态特性现在由 **Off-state gate drive resistance** 值决定。

### 故障

要对 Gate Driver 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参阅故障行为建模和故障触发。

您可以在指定的仿真时间将故障插入到栅极驱动器的输出中，以使所连接的半导体器件永久关断或永久导通。使用此功能可将故障半导体器件表示为在开路条件下失效或在正常导通状态下失效。
