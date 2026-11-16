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

### 输入

### **In** — 来自函数调用子系统模块的信号 标量 | 向量 | 矩阵

来自函数调用子系统模块的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Out** — 到函数调用子系统的信号 标量 | 向量 | 矩阵

到函数调用子系统的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

在 R2025b 中未记录。

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

断开函数调用模块之间涉及数据信号的反馈环路

使用 Function-Call Feedback Latch 模块断开一个或多个函数调用模块之间的数据信号反馈环路。具体而言，断开以下列方式之一形成的反馈环路。

- **当函数调用模块连接到同一函数调用信号的分支时**

  将 Function-Call Feedback Latch 模块放置在分支模块之间的反馈信号上。因此，锁存模块会延迟目标函数调用模块输入处的信号，并且目标函数调用模块会在锁存模块的源函数调用模块之前执行。

  要运行此模型，请参阅 Function-Call Blocks Connected to Branches of the Same Function-Call Signal。
- **当环路涉及父函数调用模块和子函数调用模块，且子启动器位于父模块内部时**

  将 Function-Call Feedback Latch 模块放置在子模块和父模块之间的反馈信号上。这种布置可防止父模块读取的信号值 (FCSS1) 在子模块执行期间发生变化。换言之，父模块读取的是子模块上一次执行的值 (FCSS2)。

  要运行此模型，请参阅 Function-Call Feedback Latch on Feedback Signal Between Child and Parent。

使用锁存模块等效于在目标函数调用子系统或模型的 Inport 模块上选中 **为函数调用反馈信号锁存输入** 复选框。然而，与使用对话框参数相比，锁存模块的一个优势是：可以以模块化方式设计目标函数调用子系统或模型，然后既可在环路上下文中使用它，也可在环路上下文之外使用它。

与 Unit Delay 或 Memory 模块相比，Function-Call Feedback Latch 模块更适合用于断开函数调用反馈环路，原因如下：

- 锁存模块将反馈信号恰好延迟源函数调用模块的一次执行。在函数调用子系统模块可能在给定仿真步中执行多次的情况下，此行为与 Unit Delay 或 Memory 模块不同。
- 与 Unit Delay 或 Memory 模块不同，锁存模块可用于断开涉及异步函数调用子系统的环路。
- 对于生成的代码，锁存模块在内存优化方面可以带来更好的性能。
