---
type: simulink-block
title: 'Sequence Viewer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Messages & Events'
documentation_page: 'sequenceviewer'
documentation_source_path: 'slref/sequenceviewer.html'
language: zh-CN
chinese_source: worker-translation
---

# Sequence Viewer

## 端口

R2025b 中未记录。

## 参数

### **可变步长的时间精度** — 时间增量精度的位数 `3`（默认）| scalar

时间增量精度的位数。使用可变步长求解器时，更改此参数以调整 Sequence Viewer 的时间精度。默认情况下，该模块支持 `3` 位精度。

假设该模块显示两个事件，发生时间分别为 `0.1215` 和 `0.1219`。精确显示这两个事件需要 `4` 位精度。如果精度为 `3`，则该模块在时间 `0.121` 显示两个事件。

#### 程序化使用

|  |
| --- |
| **模块参数**: `VariableStepTimePrecision` |
| **类型**: string scalar or character vector |
| **值**: `"3"` | scalar |
| **默认值**: `"3"` |

### **History** — 要显示的先前事件最大数量 `5000`（默认）| scalar

要显示的最后一个事件之前的事件总数。

例如，如果 **History** 为 `5`，并且仿真中有 `10` 个事件，则该模块显示 `6` 个事件，包括最后一个事件以及最后一个事件之前的五个事件。更早的事件不显示。时间标尺变灰，以指示从仿真开始到第一个显示事件的时间之间的时间。

每个发送、接收、丢弃或函数调用事件都计为一个事件，即使它们发生在同一仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数**: `History` |
| **类型**: string scalar or character vector |
| **值**: `"1000"` | scalar |
| **默认值**: `"1000"` |

## 所属库

Simulink / Messages & Events Simulink Test SimEvents Stateflow

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于在仿真期间可视化消息转移，但不包含在生成的代码中。

## 版本历史

**在 R2015b 中引入**

## 描述

在仿真期间显示模块之间的消息、事件、状态、转移和函数

Sequence Viewer 模块在仿真期间显示某些模块之间的消息、事件、状态、转移和函数。可以显示的模块称为 *生命线模块*，包括：

- 子系统
- 引用模型
- 包含消息的模块，例如 Stateflow® 图
- 调用函数或生成事件的模块，例如 Function Caller、Function-Call Generator 和 MATLAB Function 模块
- 包含函数的模块，例如 Function-Call Subsystem 和 Simulink Function 模块

要查看引用模型中生命线模块的状态、转移和事件，引用模型中必须有一个 Sequence Viewer 模块。如果引用模型中没有 Sequence Viewer 模块，则只能查看引用模型中生命线模块的消息和函数。

**注意**

Sequence Viewer 模块不显示由 MATLAB Function 模块和 S-functions 生成的函数调用。
