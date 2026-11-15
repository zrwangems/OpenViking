---
type: simulink-block
title: 'Terminate Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'terminatefunction'
language: zh-CN
chinese_source: official
---

# Terminate Function

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

您可以在封装工作区和模型工作区中定义变体控制项变量以控制 Terminate Function 模块中的活动变体，前提是**生成预处理器条件句**参数为 `off`。

## 描述

在发生模型终止事件时执行子系统

Terminate Function 模块是预配置的 Subsystem 模块，它在发生模型终止事件时执行。默认情况下，Terminate Function 模块包括：

- **事件类型**设置为**终止**的 Event Listener 模块
- Terminator 模块
- 未设置**状态所有者模块**的 State Reader 模块

Terminate Function block contents

自定义 Terminate Function 模块的内容，例如，通过为 State Reader 模块指定**状态所有者模块**并用模块替换 Terminator 模块以保存来自 State Reader 模块的状态值。

Terminate Function 模块中完全支持带输出端口的条件执行子系统。

有关不受支持的模块和功能的列表，请参阅 Initialize, Reinitialize, Reset, and Terminate Function Limitations。

对于包含 Initialize Function 和 Terminate Function 模块的组件，其输入和输出端口必须连接到输入和输出端口模块。

从该模块生成的代码是 `model_terminate` 函数的一部分，该函数在模型执行结束时被调用一次。

您可以选择 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块或对应的状态所有者模块来突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请在选择后出现的省略号上暂停。然后，从操作栏中选择**相关模块** 。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。
