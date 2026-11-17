---
type: simulink-block
title: 'Sequence Viewer'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: ''
documentation_page: 'sequenceviewer'
documentation_source_path: 'ref/sequenceviewer.html'
language: zh-CN
chinese_source: worker-translation
---

# Sequence Viewer

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Time Precision for Variable Step
  summary: 时间增量精度的位数 3（默认）| 标量
  group: ''
  block_parameter: VariableStepTimePrecision
  type: string scalar or character vector
  values: '"3" | scalar'
  default: '"3"'
- name: History
  summary: 要显示的先前事件的最大数量 5000（默认）| 标量
  group: ''
  block_parameter: History
  type: string scalar or character vector
  values: '"1000" | scalar'
  default: '"1000"'
```

### **Time Precision for Variable Step** — 时间增量精度的位数 `3`（默认）| 标量

时间增量精度的位数。使用变步长求解器时，更改此参数以调整序列查看器的时间精度。默认情况下，该模块支持 `3` 位精度。

假设该模块显示在时间 `0.1215` 和 `0.1219` 发生的两个事件。精确显示这两个事件需要 `4` 位精度。如果精度为 `3`，则该模块在时间 `0.121` 显示两个事件。

#### 编程使用

|  |
| --- |
| **模块参数**：`VariableStepTimePrecision` |
| **类型**：string scalar or character vector |
| **值**：`"3"` | scalar |
| **默认值**：`"3"` |

### **History** — 要显示的先前事件的最大数量 `5000`（默认）| 标量

最后一个事件之前要显示的事件总数。

例如，如果 **History** 为 `5`，并且仿真中有 `10` 个事件，则该模块显示 `6` 个事件，包括最后一个事件以及最后一个事件之前的五个事件。更早的事件不会显示。时间标尺会变灰，以指示从仿真开始到第一个显示事件的时间之间的时间。

每个发送、接收、丢弃或函数调用事件都计为一个事件，即使它们发生在相同的仿真时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`History` |
| **类型**：string scalar or character vector |
| **值**：`"1000"` | scalar |
| **默认值**：`"1000"` |
## 所属库

Simulink / Messages & Events Simulink Test SimEvents Stateflow

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于在仿真期间可视化消息转换，但不包含在生成的代码中。

## 版本历史

**在 R2015b 中引入**

## 描述

在仿真期间显示模块之间的消息、事件、状态、转换和函数

Sequence Viewer 模块在仿真期间显示某些模块之间的消息、事件、状态、转换和函数。可以显示的模块称为*生命线模块*，包括：

- 子系统
- 引用的模型
- 包含消息的模块，例如 Stateflow® 图
- 调用函数或生成事件的模块，例如 Function Caller、Function-Call Generator 和 MATLAB Function 模块
- 包含函数的模块，例如 Function-Call Subsystem 和 Simulink Function 模块

要查看引用模型中生命线模块的状态、转换和事件，必须在引用模型中具有 Sequence Viewer 模块。如果引用模型中没有 Sequence Viewer 模块，则只能查看引用模型中生命线模块的消息和函数。

**注意**

Sequence Viewer 模块不显示由 MATLAB Function 模块和 S-function 生成的函数调用。
