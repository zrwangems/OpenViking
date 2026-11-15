---
type: simulink-block
title: 'Sequence Viewer'
family: messages-events
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'sequenceviewer'
---

# Sequence Viewer

Display messages, events, states, transitions, and functions between blocks during simulation

## 中文

在仿真期间显示模块之间的消息、事件、状态、转移和函数。

### 库

Simulink / Messages & Events Simulink Test SimEvents Stateflow

### 说明

Sequence Viewer 模块在仿真期间显示某些模块之间的消息、事件、状态、转移和函数。可以显示的模块称为 *生命线模块*，包括：

- 子系统
- 引用模型
- 包含消息的模块，例如 Stateflow® 图
- 调用函数或生成事件的模块，例如 Function Caller、Function-Call Generator 和 MATLAB Function 模块
- 包含函数的模块，例如 Function-Call Subsystem 和 Simulink Function 模块

要查看引用模型中生命线模块的状态、转移和事件，引用模型中必须有一个 Sequence Viewer 模块。如果引用模型中没有 Sequence Viewer 模块，则只能查看引用模型中生命线模块的消息和函数。

**注意**

Sequence Viewer 模块不显示由 MATLAB Function 模块和 S-functions 生成的函数调用。

### 参数

#### **Time Precision for Variable Step** — 时间增量精度的位数 `3`（默认）| scalar

时间增量精度的位数。使用可变步长求解器时，更改此参数可调整序列查看器的时间精度。默认情况下，该模块支持 `3` 位精度。

假设该模块显示发生在时间 `0.1215` 和 `0.1219` 的两个事件。精确显示这两个事件需要 `4` 位精度。如果精度为 `3`，则该模块在时间 `0.121` 显示两个事件。

#### 编程用法

|  |
| --- |
| **模块参数**: `VariableStepTimePrecision` |
| **类型**: string scalar or character vector |
| **值**: `"3"` | scalar |
| **默认**: `"3"` |

#### **History** — 要显示的先前事件最大数量 `5000`（默认）| scalar

要显示的最后一个事件之前的事件总数。

例如，如果 **History** 为 `5`，并且仿真中有 `10` 个事件，则该模块显示 `6` 个事件，包括最后一个事件和最后一个事件之前的五个事件。较早的事件不会显示。时间标尺将变灰，以指示从仿真开始到第一个显示事件的时间之间的时间。

每个发送、接收、丢弃或函数调用事件都计为一个事件，即使它们发生在同一仿真时间。

#### 编程用法

|  |
| --- |
| **模块参数**: `History` |
| **类型**: string scalar or character vector |
| **值**: `"1000"` | scalar |
| **默认**: `"1000"` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于在仿真期间可视化消息转移，但不会包含在生成的代码中。

### 版本历史

**在 R2015b 中引入**

## Libraries

Simulink / Messages & Events Simulink Test SimEvents Stateflow

## Description

The Sequence Viewer block displays messages, events, states,
transitions, and functions between certain blocks during simulation. The blocks that you
can display are called *lifeline blocks* and include:

- Subsystems
- Referenced models
- Blocks that contain messages, such as Stateflow® charts
- Blocks that call functions or generate events, such as Function
  Caller, Function-Call Generator, and MATLAB
  Function blocks
- Blocks that contain functions, such as Function-Call Subsystem
  and Simulink Function blocks

To see states, transitions, and events for lifeline blocks in a referenced model, you
must have a Sequence Viewer block in the referenced model. Without a
Sequence Viewer block in the referenced model, you can see only
messages and functions for lifeline blocks in the referenced model.

**Note**

The Sequence Viewer block does not display function calls generated
by MATLAB Function blocks and S-functions.

## Parameters

### **Time Precision for Variable Step** — Digits for time increment precision `3` (default) | scalar

Number of digits for time increment precision. When using a variable step
solver, change this parameter to adjust the time precision for the sequence
viewer. By default the block supports `3` digits of
precision.

Suppose the block displays two events that occur at times
`0.1215` and `0.1219`. Displaying
these two events precisely requires `4` digits of
precision. If the precision is `3`, then the block displays
two events at time `0.121`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VariableStepTimePrecision` |
| **Type**: string scalar or character vector |
| **Values**: `"3"` | scalar |
| **Default**: `"3"` |

### **History** — Maximum number of previous events to display `5000` (default) | scalar

Total number of events before the last event to display.

For example, if **History** is `5` and
there are `10` events in your simulation, then the block
displays `6` events, including the last event and the five
events prior the last event. Earlier events are not displayed. The time
ruler is greyed to indicate the time between the beginning of the simulation
and the time of the first displayed event.

Each send, receive, drop, or function call event is counted as one event,
even if they occur at the same simulation time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `History` |
| **Type**: string scalar or character vector |
| **Values**: `"1000"` | scalar |
| **Default**: `"1000"` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for visualizing message transitions during simulation, but
is not included in the generated code.

## Version History

**Introduced in R2015b**
