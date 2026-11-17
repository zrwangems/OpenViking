---
type: simulink-block
title: 'Function-Call Feedback Latch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functioncallfeedbacklatch'
documentation_source_path: 'slref/functioncallfeedbacklatch.html'
language: zh-CN
chinese_source: worker-translation
---

# Function-Call Feedback Latch

## 端口
```yaml
ports:
- name: In
  summary: 来自函数调用子系统模块的信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
- name: Out
  summary: 输出至函数调用子系统模块的信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **In** — 来自函数调用子系统模块的信号 标量 | 向量 | 矩阵

来自函数调用子系统模块的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Out** — 输出至函数调用子系统模块的信号 标量 | 向量 | 矩阵

输出至函数调用子系统模块的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / Ports & Subsystems

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2011a 中引入**

## 描述

断开函数调用模块之间数据信号的反馈环路

使用 Function-Call Feedback Latch 模块断开一个或多个函数调用模块之间数据信号的反馈环路。具体而言，断开以下列方式之一形成的反馈环路。

- **当函数调用模块连接到同一函数调用信号的分支时**

  将 Function-Call Feedback Latch 模块放置在分支模块之间的反馈信号上。因此，锁存模块会延迟目标函数调用模块输入端的信号，并且目标函数调用模块在锁存模块的源函数调用模块之前执行。

  要运行此模型，请参阅 Function-Call Blocks Connected to Branches of the Same Function-Call Signal。
- **当环路涉及父函数调用模块和子函数调用模块，且子模块的发起者位于父模块内部时**

  将 Function-Call Feedback Latch 模块放置在子模块与父模块之间的反馈信号上。这种安排可防止父模块（FCSS1）读取的信号值在子模块执行期间发生变化。换言之，父模块读取的是子模块（FCSS2）上一次执行的值。

  要运行此模型，请参阅 Function-Call Feedback Latch on Feedback Signal Between Child and Parent。

使用锁存模块等效于在目标函数调用子系统或模型中的 Inport 模块上选中 **Latch input for function-call feedback signals** 复选框。然而，与使用对话框参数相比，锁存模块的一个优势是可以以模块化方式设计目标函数调用子系统或模型，然后将其用于环路上下文中或环路上下文之外。

在断开函数调用反馈环路方面，Function-Call Feedback Latch 模块比 Unit Delay 或 Memory 模块更合适，原因如下：

- 锁存模块将反馈信号恰好延迟源函数调用模块的一次执行。在函数调用子系统模块可能在给定仿真步中执行多次的情况下，此行为与 Unit Delay 或 Memory 模块不同。
- 与 Unit Delay 或 Memory 模块不同，锁存模块可用于断开涉及异步函数调用子系统的环路。
- 在生成代码的内存优化方面，锁存模块可以带来更好的性能。
