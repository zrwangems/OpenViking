---
type: simulink-block
title: 'Function-Call Feedback Latch'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'functioncallfeedbacklatch'
---

# Function-Call Feedback Latch

Break feedback loop involving data signals between function-call blocks

## 中文

断开涉及 function-call 模块之间数据信号的反馈环

### 库

Simulink / Ports & Subsystems

### 描述

使用 Function-Call Feedback Latch 模块断开一个或多个 function-call 模块之间数据信号的反馈环。具体而言，断开按以下方式之一形成的反馈环。

- **当 function-call 模块连接到同一 function-call 信号的分支时**

  将 Function-Call Feedback Latch 模块放置在分支模块之间的反馈信号上。因此，latch 模块会延迟目标 function-call 模块输入处的信号，并且目标 function-call 模块先于 latch 模块的源 function-call 模块执行。

  要运行此模型，请参阅 Function-Call Blocks Connected to Branches of the Same Function-Call Signal。
- **当环涉及父级和子级 function-call 模块，且子级发起方位于父级内部时**

  将 Function-Call Feedback Latch 模块放置在子级与父级之间的反馈信号上。此布置可防止父级读取的信号值（FCSS1）在子级执行期间发生变化。换言之，父级读取的是子级上一次执行（FCSS2）的值。

  要运行此模型，请参阅 Function-Call Feedback Latch on Feedback Signal Between Child and Parent。

使用 latch 模块等效于在目标 function-call 子系统或模型的 Inport 模块上选中 **Latch input for function-call feedback signals** 复选框。然而，与使用对话框参数相比，latch 模块的一个优势是可以以模块化方式设计目标 function-call 子系统或模型，然后将其用于环的上下文中或环的上下文之外。

在断开 function-call 反馈环方面，Function-Call Feedback Latch 模块比 Unit Delay 或 Memory 模块更合适，原因如下：

- latch 模块将反馈信号恰好延迟源 function-call 模块的一次执行。对于 function-call 子系统模块可能在给定仿真步中执行多次的情况，此行为与 Unit Delay 或 Memory 模块不同。
- 与 Unit Delay 或 Memory 模块不同，latch 模块可用于断开涉及异步 function-call 子系统的环。
- 在生成代码的内存优化方面，latch 模块可以带来更好的性能。

### 端口

#### 输入

#### **In** — 来自 function-call 子系统模块的信号 标量 | 向量 | 矩阵

来自 function-call 子系统模块的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### 输出

#### **Out** — 到 function-call 子系统的信号 标量 | 向量 | 矩阵

到 function-call 子系统的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2011a 中引入**

## Libraries

Simulink / Ports & Subsystems

## Description

Use the Function-Call Feedback Latch block to break a feedback loop of
data signals between one or more function-call blocks. Specifically, break a feedback
loop formed in one of the following ways.

- **When function-call blocks connect to branches of the
  same function-call signal**

  Place the Function-Call Feedback Latch block on the feedback
  signal between the branched blocks. As a result, the latch block delays the
  signal at the input of the destination function-call block, and the destination
  function-call block executes prior to the source function-call block of the
  latch block.

  To run this model, see Function-Call Blocks Connected to Branches of the Same Function-Call Signal.
- **When the loop involves parent and child function-call
  blocks, where the child initiator is inside the parent**

  Place the Function-Call Feedback Latch block on the feedback
  signal between the child and the parent. This arrangement prevents the signal
  value, read by the parent (FCSS1), from changing during execution of the child.
  In other words, the parent reads the value from the previous execution of the
  child (FCSS2).

  To run this model, see Function-Call Feedback Latch on Feedback Signal Between Child and Parent.

Using the latch block is equivalent to selecting the **Latch input for
function-call feedback signals** check box on the Inport
block in the destination function-call subsystem or model. However, an advantage of the
latch block over using the dialog parameter is that one can design the destination
function-call subsystem or model in a modular fashion and then use it either in or out
of the context of loops.

The Function-Call Feedback Latch block is better suited than
Unit Delay or Memory blocks in breaking function-call
feedback loops for the following reasons:

- The latch block delays the feedback signal for exactly one execution of the
  source function-call block. This behavior is different from the Unit
  Delay or Memory blocks for cases where the
  function-call subsystem blocks may execute multiple times in a given simulation
  step.
- Unlike the Unit Delay or Memory blocks, the
  latch block may be used to break loops involving asynchronous function-call
  subsystems.
- The latch block can result in better performance, in terms of memory
  optimization, for generated code.

## Ports

### Input

### **In** — Signal from function-call subsystem block scalar | vector | matrix

Signal from function-call subsystem block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Out** — Signal to function-call subsystem scalar | vector | matrix

Signal to function-call subsystem.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2011a**
