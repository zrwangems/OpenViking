---
type: simulink-block
title: 'Reset Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'resetfunction'
documentation_source_path: 'slref/resetfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Reset Function

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
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

### R2025a: 支持掩码和工作区中的变体控制变量

您可以在掩码和模型工作区中定义变体控制变量，以控制 Reset Function 模块中的活动变体，前提是 **Generate preprocessor conditionals** 参数为 `off`。

## 描述

在模型重置事件上执行子系统

Reset Function 模块是一个预配置的 Subsystem 模块，在模型重置事件上执行。默认情况下，Reset Function 模块包括：

- 一个 Event Listener 模块，其 **Event type** 设置为 `Reset`，**Event name** 设置为 `reset`
- 一个 Constant 模块，其 **Constant value** 设置为 `0`
- 一个 State Writer 模块，未设置 **State owner block**

Reset Function 模块内容

自定义 Reset Function 模块的内容，例如，将 Constant 模块替换为为 State Writer 模块生成状态值的源模块，并为 State Writer 模块指定 **State owner block**。

带有输出端口的条件执行子系统在 Reset Function 模块中得到完全支持。

有关不支持的模块和功能的列表，请参阅 Initialize, Reinitialize, Reset, and Terminate Function Limitations。

一个模型可能具有多个 Reset Function 模块，每个模块具有不同的 **Event name**。每个重置事件在生成的代码中显示为不同的函数。

您可以选择 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块或相应的状态所有者模块，以高亮显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请暂停在选中后出现的省略号上。然后，从操作栏中选择 **Related Blocks**。当多个模块对应于所选模块时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示相关模块的打开图或新选项卡。
