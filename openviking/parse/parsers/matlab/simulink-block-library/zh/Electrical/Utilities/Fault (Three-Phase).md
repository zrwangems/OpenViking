---
type: simulink-block
title: 'Fault (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'faultthreephase'
documentation_source_path: 'ref/faultthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault (Three-Phase)

## 端口
```yaml
ports:
- name: '~'
  summary: 三相端口 electrical
  direction: input
- name: F
  summary: 外部触发故障控制输入 physical
  direction: input
- name: X
  summary: 故障状态 physical
  direction: output
```

### 守恒

### **~** — 三相端口 electrical

用于将故障连接到系统的可扩展电气守恒三相端口。
### 输入

### **F** — 外部触发故障控制输入 physical

用于启用外部触发故障的物理信号标量控制输入端口。

#### 依赖

要启用此端口，请在 **External Trigger** 设置中，将 **Enable external fault trigger** 参数设置为 `Yes`。
### 输出

### **X** — 故障状态 physical

用于报告故障状态的物理信号标量输出端口：

- 1 — 故障
- 0 — 无故障

#### 依赖

要启用此端口，请在 **Main** 设置中，将 **State port** 参数设置为 `Visible`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是建模为复合三相端口还是扩展三相端口 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Failure mode
  summary: 故障类型 None（默认）| Single-phase to ground (a-g) | Single-phase to ground (b-g) | Single-phase to ground (c-g) | Two-phase
    (a-b) | Two-phase (b-c) | Two-phase (c-a) | Two-phase to ground (a-b-g) | Two-phase to ground (b-c-g) | Two-phase to ground
    (c-a-g) | Three-phase (a-b-c) | Three-phase to ground (a-b-c-g)
  group: 主要参数
- name: Faulted phase-neutral resistance
  summary: 故障相-中性点电阻 1e-3 Ohm（默认）
  group: 主要参数
- name: Faulted neutral-ground resistance
  summary: 故障中性点-地电阻 1e-3 Ohm（默认）
  group: 主要参数
- name: State port
  summary: 状态端口可见性 Hidden（默认）| Visible
  group: 主要参数
- name: Enable external fault trigger
  summary: 外部故障模型 No（默认）| Yes
  group: External Trigger
- name: Fault threshold
  summary: 触发故障的阈值 0.5（默认）
  group: External Trigger
- name: External fault trigger
  summary: 故障条件 Faulted if F >= Fault threshold（默认）| Faulted if F <= Fault threshold
  group: External Trigger
- name: Fault resets when fault trigger reverts
  summary: 故障触发恢复时故障复位 No（默认）| Yes
  group: External Trigger
- name: Enable temporal fault trigger
  summary: 时间故障模型 No（默认）| Yes
  group: Temporal Trigger
- name: Fault start time
  summary: 故障开始时间 1 s（默认）
  group: Temporal Trigger
- name: Fault duration
  summary: 故障持续时间 0.1 s（默认）
  group: Temporal Trigger
- name: Unfaulted phase-neutral conductance
  summary: 无故障相-中性点电导 1e-6 1/Ohm（默认）
  group: Parasitics
```

### **Modeling option** — 是建模为复合三相端口还是扩展三相端口 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是建模为复合三相端口还是扩展三相端口。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电力系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### 主要参数

### **Failure mode** — 故障类型 `None`（默认）| `Single-phase to ground (a-g)` | `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

要建模的故障类型。相关参数的可见性取决于故障模型。选项包括：

- `None` — 指定故障未激活。
- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

### **Faulted phase-neutral resistance** — 故障相-中性点电阻 `1e-3` `Ohm`（默认）

故障激活时，相连接与中性点之间的电阻。

#### 依赖

要启用此参数，请将 **Failure mode** 参数设置为：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

### **Faulted neutral-ground resistance** — 故障中性点-地电阻 `1e-3` `Ohm`（默认）

故障激活时，中性点与电气参考之间的电阻。

#### 依赖

要启用此参数，请将 **Failure mode** 参数设置为：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase to ground (a-b-c-g)`

### **State port** — 状态端口可见性 `Hidden`（默认）| `Visible`

用于隐藏或显示端口 **x** 的选项，该端口是报告故障状态的物理信号输出端口：

- `Hidden` — 如果选择此选项，端口 **x** 不可见。
- `Visible` — 仅当选择此选项时，端口 **x** 才可见。

### External Trigger

### **Enable external fault trigger** — 外部故障模型 `No`（默认）| `Yes`

外部故障模型。在以下选项之间选择：

- `No` — 不建模外部故障。如果选择此选项，物理信号输入端口 **F** 不可见。
- `Yes` — 建模外部故障。仅当选择此选项时，相关参数和物理信号输入端口 **F** 才可见。

### **Fault threshold** — 触发故障的阈值 `0.5`（默认）

当外部信号按故障条件指定的方向越过该阈值时，触发故障的阈值。仅当 **Enable external fault trigger** 参数设置为 `Yes` 时，此参数才可见。默认值为 `0.5`。

#### 依赖

要启用此参数，请将 **Enable external fault trigger** 参数设置为 `Yes`。

### **External fault trigger** — 故障条件 `Faulted if F >= Fault threshold`（默认）| `Faulted if F <= Fault threshold`

选择故障条件：

- `Faulted if F >= Fault threshold` — 当外部信号值大于或等于 **Fault threshold** 参数值时，发生故障。
- `Faulted if F <= Fault threshold` — 当外部信号值小于或等于 **Fault threshold** 参数值时，发生故障。

#### 依赖

要启用此参数，请将 **Enable external fault trigger** 参数设置为 `Yes`。

### **Fault resets when fault trigger reverts** — 故障触发恢复时故障复位 `No`（默认）| `Yes`

选择 `Yes`，使故障在触发信号恢复时复位。默认值为 `No`。

#### 依赖

要启用此参数，请将 **Enable external fault trigger** 参数设置为 `Yes`。

### Temporal Trigger

### **Enable temporal fault trigger** — 时间故障模型 `No`（默认）| `Yes`

时间故障模型。在以下选项之间选择：

- `No` — 不建模时间故障。
- `Yes` — 建模时间故障。仅当选择此选项时，相关参数才可见。

### **Fault start time** — 故障开始时间 `1` `s`（默认）

模块进入故障状态的仿真时间。

#### 依赖

要启用此参数，请将 **Enable temporal fault trigger** 参数设置为 `Yes`。

### **Fault duration** — 故障持续时间 `0.1` `s`（默认）

故障的仿真持续时间。当持续时间结束后，模块退出故障状态。

#### 依赖

要启用此参数，请将 **Enable temporal fault trigger** 参数设置为 `Yes`。

### Parasitics

### **Unfaulted phase-neutral conductance** — 无故障相-中性点电导 `1e-6` `1/Ohm`（默认）

当某相未参与故障时，相连接与中性点之间的电导。
## 所属库

Simscape / Electrical / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

信号启用或基于时间的、单相、两相或三相、接地或不接地故障

Fault (Three-Phase) 可对单相、两相或三相接地或不接地故障的任意排列进行建模。该模块可以施加基于时间和基于事件的故障。该模块可以连续地、同时地或在重叠时间段内施加一种或两种类型的故障。

对于基于时间或时间故障，请使用模块 **Fault start time** 参数指定故障激活时间。当您指定的故障持续时间结束后，故障变为非激活状态。

对于基于事件的故障，请使用模块 **Threshold** 参数指定故障激活阈值。外部控制信号 *F* 启用故障。当 *F* 大于阈值时，故障激活。当 *F* 小于或等于阈值时，故障非激活。

该模块可以表示以下排列：

- 单相接地故障（*a*-*g*、*b*-*g* 或 *c*-*g*）
- 两相故障（*a*-*b*、*b*-*c* 或 *c*-*a*）
- 两相接地故障（*a*-*b*-*g*、*b*-*c*-*g* 或 *c*-*a*-*g*）
- 三相故障（*a*-*b*-*c*）
- 三相接地故障（*a*-*b*-*c*-*g*）

该图显示了模块的等效电路图。

要确定等效电路中的电阻，请应用表中的相关方程。

| 故障模式 | | *R a* 的值 | *R b* 的值 | *R c* 的值 | *R g* 的值 |
| --- | --- | --- | --- | --- | --- |
| 无 / 非激活 | | 1Gpn | 1Gpn | 1Gpn | 无穷大 / 开路 |
| 单相接地 | *a*-*g* | Rpn | 1Gpn | 1Gpn | Rng |
| *b*-*g* | 1Gpn | Rpn | 1Gpn | Rng |
| *c*-*g* | 1Gpn | 1Gpn | Rpn | Rng |
| 两相 | *a*-*b* | Rpn | Rpn | 1Gpn | 无穷大 / 开路 |
| *b*-*c* | 1Gpn | Rpn | Rpn | 无穷大 / 开路 |
| *c*-*a* | Rpn | 1Gpn | Rpn | 无穷大 / 开路 |
| 两相接地 | *a*-*b*-*g* | Rpn | Rpn | 1Gpn | Rng |
| *b*-*c*-*g* | 1Gpn | Rpn | Rpn | Rng |
| *c*-*a*-*g* | Rpn | 1Gpn | Rpn | Rng |
| 三相 | *a*-*b*-*c* | Rpn | Rpn | Rpn | 无穷大 / 开路 |
| 三相接地 | *a*-*b*-*c*-*g* | Rpn | Rpn | Rpn | Rng |

其中：

- *Ra* 是 *a* 相与星形连接中性点之间的电阻。
- *Rb* 是 *b* 相与星形连接中性点之间的电阻。
- *Rc* 是 *c* 相与星形连接中性点之间的电阻。
- *Rg* 是星形连接中性点与电气参考之间的电阻。
- *Rpn* 是 **Faulted phase-neutral resistance** 参数的值。
- *Rng* 是 **Faulted neutral-ground resistance** 参数的值。
- *Gpn* 是 **Unfaulted phase-neutral conductance** 参数的值。
