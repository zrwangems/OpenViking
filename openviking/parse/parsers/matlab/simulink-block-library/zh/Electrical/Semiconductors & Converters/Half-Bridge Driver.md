---
type: simulink-block
title: 'Half-Bridge Driver'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'halfbridgedriver'
documentation_source_path: 'ref/halfbridgedriver.html'
language: zh-CN
chinese_source: worker-translation
---

# Half-Bridge Driver

## 端口

### 输入

### **u** — 控制信号，无量纲物理信号

指定输入控制值的输入物理信号。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`PS input`。
### 守恒

### **PWM** — 脉宽调制信号电气

与脉宽调制信号关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **REF** — 浮地零伏参考电气

与浮地零伏参考关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **HO** — 高侧栅极连接电气

与半桥高侧栅极关联的电气守恒端口。将此端口连接到 MOSFET 或 IGBT
模块的栅极。

### **HS** — 高侧源极或发射极连接电气

与半桥高侧源极或发射极关联的电气守恒端口。将此端口连接到
MOSFET 模块的源极或 IGBT 模块的发射极。

### **LO** — 低侧栅极连接电气

与半桥低侧栅极关联的电气守恒端口。将此端口连接到 MOSFET 或 IGBT
模块的栅极。

### **LS** — 低侧源极或发射极连接电气

与半桥低侧源极或发射极关联的电气守恒端口。将此端口连接到
MOSFET 模块的源极或 IGBT 模块的发射极。

## 参数

### **Modeling option** — 建模为电气输入端口还是物理信号输入端口 `PS input`（默认）| `Electrical input ports`

建模为物理信号输入端口还是电气输入端口。

### 输入逻辑

### **Logic 1 input value** — 逻辑 1 的信号值 0.7（默认）

对应于逻辑 1 电平的输入信号值。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`PS input`。

### **Logic 0 input value** — 逻辑 0 的信号值 0.3（默认）

对应于逻辑 0 电平的输入信号值。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`PS input`。

### **Logic 1 input voltage** — 逻辑 1 的电压值 2.0 V（默认）

对应于逻辑 1 电平的输入电压值。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### **Logic 0 input voltage** — 逻辑 0 的电压值 0.8 V（默认）

对应于逻辑 0 电平的输入电压值。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical input ports`。

### 输出

### **On-state gate-source voltage** — 导通状态所需输出电压 15 V（默认）

驱动器处于导通状态时所需的输出电压。

### **Off-state gate-source voltage** — 关断状态所需输出电压 0 V（默认）

驱动器处于关断状态时所需的输出电压。

### 时序

### **Low-side propagation delay (logic 0->logic 1)** — 时序图中的 *t*pLH 50 ns（默认）

输入逻辑从 0 变为 1 时的低侧传播延迟。

### **High-side dead time (logic 0->logic 1)** — 时序图中的 *t*dLH 100 ns（默认）

输入逻辑从 0 变为 1 时的高侧死区时间。

### **High-side propagation delay (logic 1->logic 0)** — 时序图中的 *t*pHL 50 ns（默认）

输入逻辑从 1 变为 0 时的高侧传播延迟。

### **Low-side dead time (logic 1->logic 0)** — 时序图中的 *t*dHL 100 ns（默认）

输入逻辑从 1 变为 0 时的低侧死区时间。

### 动态特性

### **Parameterization** — 选择驱动器参数化方式 `Output impedance`（默认）| `Rise and fall times`

选择驱动器参数化类型：

- `Output impedance` — 指定
  导通状态和关断状态的栅极驱动电阻。
- `Rise and fall times` —
  指定上升时间、下降时间和负载电容。

### **On-state gate drive resistance** — 导通状态所需输出电压 2 Ω（默认）

驱动器处于导通状态时所需的输出电压。

#### 依赖关系

当 **Parameterization** 参数
设置为 `Output impedance` 时启用。

### **Off-state gate drive resistance** — 关断状态所需输出电压 2 Ω（默认）

驱动器处于关断状态时所需的输出电压。

#### 依赖关系

当 **Parameterization** 参数
设置为 `Output impedance` 时启用。

### **Rise time** — 驱动器上升时间 20 ns（默认）

驱动器从 10% 到 90% 的上升时间。

#### 依赖关系

当 **Parameterization** 参数
设置为 `Rise and fall times` 时启用。

### **Fall time** — 驱动器下降时间 20 ns（默认）

驱动器从 90% 到 10% 的下降时间。

#### 依赖关系

当 **Parameterization** 参数
设置为 `Rise and fall times` 时启用。

### **Load capacitance for rise and fall times** — 驱动器负载电容 10 nF（默认）

驱动器负载电容。

#### 依赖关系

当 **Parameterization** 参数
设置为 `Rise and fall times` 时启用。

### 故障

### **State fault** — 在半桥驱动器中建模故障状态的选项 `Add fault`（默认）

在半桥驱动器模块中建模故障状态的选项。

要添加故障，请单击 **Add fault**
超链接。

### **Failure mode** — 故障后驱动器的状态 `Fail input fixed at logic 0`（默认）| `Fail input fixed at logic 1` | `Fail high side off` | `Fail high side on` | `Fail low side off` | `Fail low side on` | `Fail high and low sides off` | `Fail high and low sides on`

选择故障后驱动器的状态。

#### 依赖关系

要启用此参数，请通过单击
**State fault** 参数中的 **Add fault** 超链接，向半桥驱动器模块添加故障。

创建故障后，您可以在
**Fault Inspector** 窗口中更改属性。当您打开包含故障的模块时，
**Open Fault Inspector** 超链接将替代 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Timed`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

半桥驱动器集成电路的行为模型

Half-Bridge Driver 模块提供了用于驱动 MOSFET 和 IGBT 半桥的集成电路的抽象表示。该模块对输入迟滞、传播延迟以及开通/关断动态特性进行建模。除非显式建模栅极驱动器电路，否则请始终使用此模块或 Gate Driver 模块来设置 MOSFET 模块上的栅极-源极电压或 IGBT 模块上的栅极-发射极电压。不要将受控电压源直接连接到半导体栅极，因为这会忽略决定开关动态特性的栅极驱动器输出阻抗。

您可以通过将 **Modeling option** 参数设置为以下任一值来建模电气输入端口或物理信号输入端口：

- `PS input` — 驱动器输出状态由物理信号输入 u 控制。如果您的所有控制器（包括 PWM 波形生成）均由 Simulink® 模块确定，请使用此建模选项。此建模选项为默认值。
- `Electrical input ports` — 驱动器输出状态由两个电气输入连接 PWM 和 REF 控制。如果您的模型具有上游模拟组件（例如 Controlled PWM Voltage 源），请使用此选项。

第一对输出电气端口 HO 和 HS 的行为与 Gate
Driver 模块的 G
和 S 端口相同。将这些端口连接到半桥的高侧 MOSFET 或 IGBT。第二对端口 LO 和 LS 连接到半桥的低侧 MOSFET 或
IGBT。它们的行为类似，只是其逻辑相对于高侧是反相的。

该图显示了半桥驱动器的时序属性，其中：

- *t*pLH 是输入逻辑从 0 变为 1 时的低侧传播延迟。
- *t*dLH 是输入逻辑从 0 变为 1 时的高侧死区时间。
- *t*pHL 是输入逻辑从 1 变为 0 时的高侧传播延迟。
- *t*dHL 是输入逻辑从 1 变为 0 时的低侧死区时间。

### 故障

要在 Half-Bridge Driver 模块中建模故障，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

您可以在指定的仿真时间向一个或两个输出中插入故障。故障选项包括：

- Fail input fixed at logic 0
- Fail input fixed at logic 1
- Fail high side off
- Fail high side on
- Fail low side off
- Fail low side on
- Fail high and low sides off
- Fail high and low sides on
