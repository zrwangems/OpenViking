---
type: simulink-block
title: 'Initialize Function'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'initializefunction'
---

# Initialize Function

Execute subsystem on model initialize event

## 中文

在发生模型初始化事件时执行子系统

### 所属库

Simulink / User-Defined Functions

### 描述

Initialize Function 模块是预配置的 Subsystem 模块，它在发生模型初始化事件时执行。默认情况下，Initialize Function 模块包括：

- **事件类型**设置为**初始化**的 Event Listener 模块
- **常量值**设置为 `0` 的 Constant 模块
- 未设置**状态所有者模块**的 State Writer 模块

initialize function block contents

当您需要基于事件初始化任务时，请使用此模块。例如，当 Model 模块在其 **initialize** 端口上接收到函数调用控制信号时，就会触发 Initialize Function 模块所引用的 Simulink 模型中的 Model  模块。有关使用 Initialize Function 模块的建模模式的详细信息，请参阅 Common Uses of the Initialize Function Block。此模块允许您调度和控制模型中任务的初始化。

自定义 Initialize Function 模块的内容，例如，用为 State Writer 模块生成状态值的源模块替换 Constant 模块，并为 State Writer 模块指定**状态所有者模块**。

Initialize Function 模块中完全支持带输出端口的条件执行子系统。有关不受支持的模块和功能的列表，请参阅 Initialize, Reinitialize, Reset, and Terminate Function Limitations。

对于包含 Initialize Function 和 Terminate Function 模块的组件，其输入和输出端口必须分别连接到 Inport 和 Outport 模块。

从该模块生成的代码是 `model_initialize` 函数的一部分，该函数在模型执行开始时被调用一次。

您可以选择 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块或对应的状态所有者模块来突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请在选择后出现的省略号上暂停。然后，从操作栏中选择**相关模块** 。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `否` |
| **多维信号** | `是a` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

### 版本历史记录

#### R2025a: 支持封装工作区和模型工作区中的变体控制项变量

您可以在封装工作区或模型工作区中定义变体控制项变量以控制 Initialize Function 模块中的活动变体，前提是**生成预处理器条件句**参数为 `off`。

## Libraries

Simulink / User-Defined Functions

## Description

The Initialize Function block is a preconfigured Subsystem block that executes on a model initialize event. By default, the
Initialize Function block includes:

- An Event Listener block with
  the **Event type** set to
  `Initialize`
- A Constant block with the **Constant
  value** set to `0`
- A State Writer block with no
  **State owner block** set

initialize function block contents

Use this block when you need to initialize a task based on an event. For example,
Initialize Function block inside a Simulink model referenced by a
Model  block is triggered when the Model block
receives a function-call control signal at its **initialize** port. For more
information about the modeling patterns using Initialize Function block,
see Common Uses of the Initialize Function Block. This block
allows you to schedule and control the initialization of a task in a model.

Customize the contents of the Initialize Function block by, for
example, replacing the Constant block with source blocks that generate
the state value for the State Writer block and specifying a
**State owner block** for the State Writer
block.

Conditionally executed subsystems with output ports are fully supported within
Initialize Function blocks. For a list of unsupported blocks and
features, see Initialize, Reinitialize, Reset, and Terminate Function Limitations.

The input and output ports of a component containing Initialize
Function and Terminate Function blocks must connect to
Inport and Outport blocks, respectively.

The code generated from this block is part of the `model_initialize`
function that is called once at the beginning of model execution.

You can select an Initialize Function, Reinitialize
Function, Reset Function, or Terminate
Function block or a corresponding state owner block to highlight blocks
related to it. To show a related block in an open diagram or new tab, pause on the
ellipsis that appears after selection. Then, select **Related
Blocks**
 from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.

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

### R2025a: Variant control variables in mask and model workspaces supported

You can define variant control variables in the mask or model workspaces to
control active variants in the Initialize Function block, provided
the **Generate preprocessor conditionals** parameter is
`off`.
