---
type: simulink-block
title: 'Sequence Viewer'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: ''
documentation_page: 'sequenceviewer'
documentation_source_path: 'ref/sequenceviewer.html'
language: zh-CN
chinese_source: official
---

# Sequence Viewer

## 端口

R2025b 官方文档未提供。

## 参数

### **变步长的时间精确度** — 时间增量精度的数字 `3` (默认) | 标量

时间增量精度的位数。当使用可变步长求解器时，更改此参数可调整序列查看器的时间精度。默认情况下，该模块支持 `3` 位精度。

假设该模块显示在时间 `0.1215` 和 `0.1219` 发生的两个事件。精确显示这两个事件需要 `4` 位精度。如果精度是 `3`，那么该模块在时间 `0.121` 处显示两个事件。

#### 编程用法

|  |
| --- |
| **区模块参数**：`VariableStepTimePrecision` |
| **类型**：字符串标量或字符向量 |
| **值**：`"3"` | 标量 |
| **默认值**：`"3"` |

### **历史记录** — 可显示的先前事件的最大数量 `5000` (默认) | 标量

要显示的最后一个事件之前的事件总数。

例如，如果**历史记录**是 `5` 并且仿真中有 `10` 个事件，那么该模块将显示 `6` 个事件，包括最后一个事件和最后一个事件之前的五个事件。不显示早期事件。时间标尺呈灰色，表示仿真开始和第一个显示事件的时间之间的时间。

每个发送、接收、丢弃或函数调用事件都算作一个事件，即使它们发生在同一仿真时间。

#### 编程用法

|  |
| --- |
| **区模块参数**：`History` |
| **类型**：字符串标量或字符向量 |
| **值**：`"1000"` | 标量 |
| **默认值**：`"1000"` |

## 所属库

Simulink / Messages & Events Simulink Test SimEvents Stateflow

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

该模块可用于在仿真中可视化消息转移，但不包含在生成的代码中。

## 版本历史

**在 R2015b 中推出**

## 描述

在仿真期间显示模块之间的消息、事件、状态、转移和函数

Sequence Viewer 模块在仿真中显示某些模块之间的消息、事件、状态、转移和函数。您可以显示的模块称为*生命线模块*，其中包括：

- 子系统
- 引用模型
- 包含消息的模块，例如 Stateflow® 图
- 调用函数或生成事件的模块，例如 Function Caller、Function-Call Generator 和 MATLAB Function 模块
- 包含函数的模块，例如 Function-Call Subsystem 和 Simulink Function 模块

要查看引用模型中生命线模块的状态、转移和事件，您必须在引用模型中有一个 Sequence Viewer 模块。如果引用模型中没有 Sequence Viewer 模块，则您只能看到引用模型中生命线模块的消息和函数。

**注意**

Sequence Viewer 模块不显示由 MATLAB Function 模块和 S-function 生成的函数调用。
