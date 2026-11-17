---
type: simulink-block
title: 'Reinitialize Function'
family: 'user-defined-functions'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'reinitializefunction'
documentation_source_path: 'slref/reinitializefunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Reinitialize Function

## 端口

R2025b 中未记录。

## 参数

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
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2022a 中引入**

### R2025a：支持 mask 和模型工作区中的变体控制变量

你可以在 mask 和模型工作区中定义变体控制变量，以控制 Reinitialize Function 模块中的活动变体，前提是 **Generate preprocessor conditionals** 参数为 `off`。

## 描述

在模型或子系统重新初始化事件时执行子系统

Reinitialize Function 模块是一个预配置的 Subsystem 模块，在模型或子系统重新初始化事件时执行。默认情况下，Reinitialize Function 模块包括：

- 一个 Event Listener 模块，其 **Event type** 设置为 `Reinitialize`，**Event name** 设置为 `reinit`
- 一个 Constant 模块，其 **Constant value** 设置为 `0`
- 一个 State Writer 模块，未设置 **State owner block**

Reinitialize Function 模块图标Event listener 模块和 Constant 模块连接到 State Writer 模块。

例如，通过将 Constant 模块替换为为 State Writer 模块生成状态值的源模块，并为 State Writer 模块指定 **State owner block**，来自定义 Reinitialize Function 模块。

要生成模型重新初始化事件，请将函数调用信号发送到 Model 模块的重新初始化端口，该模块引用包含 Reinitialize Function 模块的模型。要生成子系统重新初始化事件，请将函数调用信号发送到 Subsystem 模块的重新初始化端口，该模块包含 Reinitialize Function 模块。重新初始化事件具有以下效果：

1. 模型或子系统中每个模块的状态恢复到其初始条件，包括接收重新初始化事件的模型或子系统内部的子系统或引用模型中的模块。
2. 与重新初始化端口对应的 Reinitialize Function 模块的内容被执行。
3. 如果接收重新初始化事件的模型或子系统内部的任何子系统或引用模型包含 Reinitialize Function 模块，并且该模块的 **Event name** 与对应于重新初始化端口的 Reinitialize Function 模块的 **Event name** 匹配，则执行那些 Reinitialize Function 模块的内容。

要在重新初始化事件时执行由 Model 模块引用的模型，必须在引用模型的根级别放置一个 Reinitialize Function 模块。根据你的建模需求，你可能需要自定义引用模型内部的 Reinitialize Function 模块。

如果 Stateflow® 图中基于 Simulink® 的状态包含 Reinitialize Function 模块，要为该状态生成子系统重新初始化事件，请使用以下语法的转移事件：

```
{StateName.ReinitializeEventName()}
```

带有输出端口的条件执行子系统在 Reinitialize Function 模块内完全受支持。

一个模型或子系统可以有多个 Reinitialize Function 模块，每个模块具有不同的 **Event name**。这些重新初始化事件中的每一个在生成的代码中都表现为不同的函数。在 Event Listener 模块的模块对话框中设置 **Event name**。**Event Name** 显示在 Reinitialize Function 模块图标上，并作为对应于重新初始化事件的重新初始化端口的端口标签。

你可以选择一个 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块，或对应的 state owner 模块，以突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请在选中后出现的省略号上暂停。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块与所选模块对应时，将打开相关模块列表。你可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的打开的图或新选项卡。
