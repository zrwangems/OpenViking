---
type: simulink-block
title: 'Reinitialize Function'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'reinitializefunction'
---

# Reinitialize Function

Execute subsystem on model or subsystem reinitialize event

## 中文

在模型或子系统重新初始化事件时执行子系统

### 库

Simulink / User-Defined Functions

### 描述

Reinitialize Function 模块是一个预配置的 Subsystem 模块，在模型或子系统重新初始化事件时执行。默认情况下，Reinitialize Function 模块包括：

- 一个 Event Listener 模块，其 **Event type** 设置为 `Reinitialize`，**Event name** 设置为 `reinit`
- 一个 Constant 模块，其 **Constant value** 设置为 `0`
- 一个 State Writer 模块，未设置 **State owner block**

Reinitialize Function 模块图标。Event Listener 模块和 Constant 模块连接到 State Writer 模块。

通过例如将 Constant 模块替换为为 State Writer 模块生成状态值的源模块，并为 State Writer 模块指定 **State owner block**，来自定义 Reinitialize Function 模块。

要生成模型重新初始化事件，请向 Model 模块的重新初始化端口发送函数调用信号，该 Model 模块引用包含 Reinitialize Function 模块的模型。要生成子系统重新初始化事件，请向 Subsystem 模块的重新初始化端口发送函数调用信号，该 Subsystem 模块包含 Reinitialize Function 模块。重新初始化事件具有以下效果：

1. 模型或子系统中每个模块的状态恢复到其初始条件，包括接收重新初始化事件的模型或子系统内部的子系统或引用模型中的模块。
2. 与重新初始化端口对应的 Reinitialize Function 模块的内容被执行。
3. 如果接收重新初始化事件的模型或子系统内部的任何子系统或引用模型包含 Reinitialize Function 模块，并且该模块的 **Event name** 与对应于重新初始化端口的 Reinitialize Function 模块的 **Event name** 匹配，则执行这些 Reinitialize Function 模块的内容。

要在重新初始化事件时执行由 Model 模块引用的模型，必须将 Reinitialize Function 模块放在被引用模型的根级别。根据你的建模需求，你可能需要自定义被引用模型内部的 Reinitialize Function 模块。

如果 Stateflow® 图中的基于 Simulink® 的状态包含 Reinitialize Function 模块，要为该状态生成子系统重新初始化事件，请使用以下语法的转移事件：

```
{StateName.ReinitializeEventName()}
```

带输出端口的条件执行子系统在 Reinitialize Function 模块内完全受支持。

一个模型或子系统可以有多个 Reinitialize Function 模块，每个模块具有不同的 **Event name**。每个此类重新初始化事件在生成的代码中显示为不同的函数。在 Event Listener 模块的模块对话框中设置 **Event name**。**Event Name** 显示在 Reinitialize Function 模块图标上，并作为对应于重新初始化事件的重新初始化端口的端口标签。

你可以选择 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块，或对应的状态所有者模块，以突出显示与其相关的模块。要在打开的图或新标签页中显示相关模块，请将鼠标悬停在选择后出现的省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块对应于所选模块时，会打开相关模块列表。你可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的打开图或新标签页。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或能力支持取决于模块实现。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的代码生成支持取决于模块实现。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

### 版本历史

**在 R2022a 中引入**

#### R2025a：支持掩码和模型工作区中的变体控制变量

你可以在掩码和模型工作区中定义变体控制变量，以控制 Reinitialize Function 模块中的活动变体，前提是 **Generate preprocessor conditionals** 参数为 `off`。

## Libraries

Simulink / User-Defined Functions

## Description

The Reinitialize Function block is a preconfigured Subsystem block that executes on a model or subsystem reinitialize event. By
default, the Reinitialize Function block includes:

- An Event Listener block with the
  **Event type** set to `Reinitialize` and the
  **Event name** set to `reinit`
- A Constant block with the **Constant value** set to
  `0`
- A State Writer block with no **State
  owner block** set

Reinitialize Function block iconEvent listener block and Constant block connected to State Writer block.

Customize the Reinitialize Function block by, for example, replacing the
Constant block with source blocks that generate the state value for the
State Writer block and specifying a **State owner block**
for the State Writer block.

To generate a model reinitialize event, send a function-call signal to a reinitialize port
of a Model block that references a model that contains a Reinitialize
Function block. To generate a subsystem reinitialize event, send a function-call
signal to a reinitialize port of a Subsystem block that contains a
Reinitialize Function block. The reinitialize event has these effects:

1. The state of each block in the model or subsystem reverts back to its initial
   condition, including blocks within subsystems or referenced models inside the model or
   subsystem receiving the reinitialize event.
2. The contents of the Reinitialize Function block corresponding to the
   reinitialize port are executed.
3. If any subsystems or referenced models inside the model or subsystem receiving the
   reinitialize event contain a Reinitialize Function block, and the
   **Event name** of that block matches the **Event
   name** of the Reinitialize Function block corresponding to the
   reinitialize port, then the contents of those Reinitialize Function
   blocks are executed.

To execute a model referenced by a Model block on a reinitialize event, you
must place a Reinitialize Function block at the root level of the referenced
model. Based on your modeling requirements, you might need to customize the
Reinitialize Function block inside the referenced model.

If a Simulink® based state in a Stateflow® chart contains a Reinitialize Function block, to generate a
subsystem reinitialize event for the state, use a transition event with this
syntax:

```
{StateName.ReinitializeEventName()}
```

Conditionally executed subsystems with output ports are fully supported within
Reinitialize Function blocks.

A model or subsystem can have multiple Reinitialize Function blocks with
each block having a different **Event name**. Each of these reinitialize
events appears in the generated code as a different function. Set the **Event
name** in the block dialog box of the Event Listener block. The
**Event Name** appears on the Reinitialize Function block
icon, and as the port label for the reinitialize port corresponding to the reinitialize
event.

You can select an Initialize Function, Reinitialize
Function, Reset Function, or Terminate Function block or
a corresponding state owner block to highlight blocks related to it. To show a related block
in an open diagram or new tab, pause on the ellipsis that appears after selection. Then,
select **Related Blocks**
Related Blocks button from the action bar. When multiple blocks correspond to the
selected block, a list of related blocks opens. You can filter the list of related blocks by
entering a search term in the text box. After you select a related block from the list, window
focus goes to the open diagram or new tab that shows the related block.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2022a**

### R2025a: Variant control variables in mask and model workspaces supported

You can define variant control variables in the mask and model workspaces to control
active variants in Reinitialize
Function block, provided the **Generate preprocessor
conditionals** parameter is `off`.
