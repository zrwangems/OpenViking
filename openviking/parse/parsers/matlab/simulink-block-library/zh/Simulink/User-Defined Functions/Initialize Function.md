---
type: simulink-block
title: 'Initialize Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'initializefunction'
documentation_source_path: 'slref/initializefunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Initialize Function

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

### R2025a: 支持掩码和模型工作区中的变体控制变量

您可以在掩码或模型工作区中定义变体控制变量，以控制 Initialize Function 模块中的活动变体，前提是 **Generate preprocessor conditionals** 参数为 `off`。

## 描述

在模型初始化事件上执行子系统

Initialize Function 模块是一个预配置的 Subsystem 模块，在模型初始化事件上执行。默认情况下，Initialize Function 模块包含：

- 一个 Event Listener 模块，其 **Event type** 设置为 `Initialize`
- 一个 Constant 模块，其 **Constant value** 设置为 `0`
- 一个 State Writer 模块，未设置 **State owner block**

initialize function block contents

当您需要基于事件初始化任务时，请使用此模块。例如，由 Model 模块引用的 Simulink 模型内部的 Initialize Function 模块，会在 Model 模块的 **initialize** 端口接收到函数调用控制信号时被触发。有关使用 Initialize Function 模块的建模模式的详细信息，请参阅 Common Uses of the Initialize Function Block。此模块允许您调度和控制模型中任务的初始化。

通过例如将 Constant 模块替换为为 State Writer 模块生成状态值的源模块，并为 State Writer 模块指定 **State owner block**，可以自定义 Initialize Function 模块的内容。

带有输出端口的条件执行子系统在 Initialize Function 模块中完全受支持。有关不支持的模块和功能的列表，请参阅 Initialize, Reinitialize, Reset, and Terminate Function Limitations。

包含 Initialize Function 和 Terminate Function 模块的组件的输入和输出端口必须分别连接到 Inport 和 Outport 模块。

从此模块生成的代码是 `model_initialize` 函数的一部分，该函数在模型执行开始时被调用一次。

您可以选择 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块或相应的状态所有者模块，以高亮显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请将鼠标悬停在选择后出现的省略号上。然后，从操作栏中选择 **Related Blocks**。当多个模块与所选模块对应时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示相关模块的打开图或新选项卡。
