---
type: simulink-block
title: 'Reset Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'resetfunction'
language: zh-CN
chinese_source: official
---

# Reset Function

## 端口

R2025b 官方文档未提供。

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / User-Defined Functions

## 模块特性

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

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

### R2025a: 支持封装工作区和模型工作区中的变体控制项变量

您可以在封装工作区和模型工作区中定义变体控制项变量以控制 Reset Function 模块中的活动变体，前提是**生成预处理器条件句**参数为 `off`。

## 描述

在发生模型重置事件时执行子系统

Reset Function 模块是预配置的 Subsystem 模块，它在发生模型重置事件时执行。默认情况下，Reset Function 模块包括：

- **事件类型**设置为**重置**且**事件名称**设置为 `reset` 的 Event Listener 模块
- **常量值**设置为 `0` 的 Constant 模块
- 未设置**状态所有者模块**的 State Writer 模块

Reset Function block contents

自定义 Reset Function 模块的内容，例如，用为 State Writer 模块生成状态值的源模块替换 Constant 模块，并为 State Writer 模块指定**状态所有者模块**。

Reset Function 模块中完全支持带输出端口的条件执行子系统。

有关不受支持的模块和功能的列表，请参阅 Initialize, Reinitialize, Reset, and Terminate Function Limitations。

模型可能有多个 Reset Function 模块，每个模块有不同**事件名称**。其中每个重置事件都作为不同函数出现在生成的代码中。

您可以选择 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块或对应的状态所有者模块来突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请在选择后出现的省略号上暂停。然后，从操作栏中选择**相关模块** 。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。
