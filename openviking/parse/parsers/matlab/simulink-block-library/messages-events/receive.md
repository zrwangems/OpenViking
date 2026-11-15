---
type: simulink-block
title: 'Receive'
family: messages-events
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'receive'
---

# Receive

Receive messages

## 中文

接收消息

### 库

Simulink / Messages & Events SimEvents

### 说明

Receive 模块从接收到的消息中提取数据，并将其写入输出信号端口。如果模块执行时没有新消息，则模块使用 **队列为空时的值来源** 的值。
Receive 和 Message Receive 模块是完全相同的模块。

- 选择 `Hold last value` 以保持从最后一条消息读取的数据。
- 选择 `Use initial value` 以写入默认数据。

### 端口

#### 输入

#### **Port\_1** — 输入消息 标量 | 向量 | 矩阵

消息的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
#### 输出

#### **Port\_S** — 显示是否接收到消息 标量

如果模块成功接收到消息，则输出 `1`；否则输出 `0`。

#### 依赖关系

要启用此端口，请选中标有 **显示接收状态** 的复选框。

**数据类型：** `double`

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

信号的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### 参数

#### **使用内部队列** — 选择以使用内部队列 on（SimEvents® 的默认值） | off（Simulink® 的默认值）

如果要使用内部队列接收消息，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `UseInternalQueue` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

#### **队列已满时覆盖最旧元素** — 指定队列覆盖策略 on（Simulink 的默认值） | off（SimEvents 的默认值）

选中此复选框可在两种队列覆盖策略之间进行选择。

- 如果选中此复选框，则当队列已满时，传入消息会覆盖最旧的消息。
- 如果清除此复选框，则当队列已满时，模块不接受新消息。

#### 依赖关系

此参数在选中 **使用内部队列** 复选框时可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `QueueOverwriting` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'`（对于 Simulink）和 `'off'`（对于 SimEvents） |

#### **队列长度** — 指定消息队列的长度 `16`（默认） | `scalar`

指定消息队列容量。队列长度可指定为 `1` 和 *2*26-*1* 之间的正整数（包含两端）。

#### 依赖关系

此参数在选中 **使用内部队列** 复选框时可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `QueueLength` |
| **类型**: character vector |
| **值**: `'16'` | scalar |
| **默认值**: `'16'` |

#### **队列类型** — 指定消息队列排序策略 `FIFO`（默认） | `LIFO` | `Priority`

该模块支持三种消息排序策略：

- 先进先出（`FIFO`）— 存储中最旧的消息最先离开。
- 后进先出（`LIFO`）— 存储中最新的消息最先离开。
- `Priority` — 消息或实体按其优先级排序。

  仅当清除 **队列已满时覆盖最旧元素** 复选框时，才能使用优先级队列。

  **注意**

  优先级队列仅接受非总线标量，并且不支持 `fixed point` 数据类型。

#### 依赖关系

此参数在选中 **使用内部队列** 复选框时可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `QueueType` |
| **类型**: character vector |
| **值**: `'FIFO'` | `'LIFO'` | `'Priority'` |
| **默认值**: `'FIFO'` |

#### **优先级顺序** — 指定消息队列优先级 `Ascending`（默认） | `Descending`

选择按优先级对消息排序的方向。

- `Ascending` — 优先级值较小的消息出现在队列前面。
- `Descending` — 优先级值较大的消息出现在队列前面。

#### 依赖关系

此参数在选中 **使用内部队列** 复选框且 **队列类型** > **Priority** 时可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `PriorityOrder` |
| **类型**: character vector |
| **值**: `'Ascending'` | `'Descending'` |
| **默认值**: `'Ascending'` |

#### **显示接收状态** — 显示是否接收到消息 `off`（默认） | on

选中此复选框可显示是否接收到消息。如果选中此复选框，则当模块成功接收到消息时输出 `1`，否则输出 `0`。

#### 编程用法

|  |
| --- |
| **模块参数**: `ShowQueueStatus` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

#### **初始值** — 设置初始数据值 `[](unspecified)`（默认） | `scalar` | `vector` | `matrix`

在第一条消息到达之前，为队列输入初始数据值。默认值 `[](unspecified)` 将被视为数据类型为 double 的 `0`。

要使用此模块初始化非虚拟总线信号，请将初始值指定为 MATLAB® 结构体。有关使用结构体初始化非虚拟总线信号的详细信息，请参阅指定总线元素的初始条件。

#### 编程用法

|  |
| --- |
| **模块参数**: `InitialValue` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认值**: `'[]'` |

#### **队列为空时的值来源** — 空队列的值来源 `Hold last value`（默认） | `Use initial value`

指定接收消息队列为空时要接收的值。

- `Hold last value`（默认）— 保持从最后一条消息读取的数据。

  最初，如果模块尝试接收消息但失败，则它会输出初始值。
- `Use initial value` — 写入默认数据。

#### 依赖关系

此参数在选中 **使用内部队列** 复选框时可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `ValueSourceWhenQueueIsEmpty` |
| **类型**: character vector |
| **值**: `'Hold last value'` | `'Use initial value'` |
| **默认值**: `'Hold last value'` |

#### **采样时间（-1 表示继承）** — 指定采样之间的时间间隔 `-1`（默认） | `scalar`

要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: character vector |
| **值**: `'-1'` | scalar |
| **默认值**: `'-1'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

为使用消息队列并启用了多任务的模型生成代码时，如果该模型将部署到多任务环境，请启用并发任务行为。否则，生成的代码可能会发生数据损坏。通过选择“允许任务在目标上并发执行”来启用并发任务行为。

**注意**

Receive 模块不支持行主序代码生成。

### 版本历史

**在 R2016a 中引入**

## Libraries

Simulink / Messages & Events SimEvents

## Description

The Receive block extracts data from received messages and writes them
to the output signal port. If there are no new messages when the block executes, the
block uses the **Value source when queue is empty** value.
Receive and Message Receive blocks are identical
blocks.

- Select `Hold last value` to hold data read from the
  last message.
- Select `Use initial value` to write default
  data.

## Ports

### Input

### **Port\_1** — Input message scalar | vector | matrix

The input port for the message.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_S** — Show whether a message was received scalar

Outputs `1` if the block receives a message
successfully, and `0` otherwise.

#### Dependencies

To enable this port, select the check box labeled **Show
receive status**.

**Data Types:** `double`

### **Port\_1** — Output signal scalar | vector | matrix

Output port for the signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Use internal queue** — Select to use an internal queue on (default for SimEvents®) | off (default for Simulink®)

Select this check box if you use an internal queue to receive
messages.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UseInternalQueue` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Overwrite the oldest element if queue is full** — Specify queue overwriting policy on (default for Simulink) | off (default for SimEvents)

Select this check box to choose between two queue overwriting
policies.

- If you select the check box, an incoming message overwrites the
  oldest if the queue is full.
- If you clear the check box, the block does not accept new messages
  if the queue is full.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueOverwriting` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` (for Simulink) and `'off'` (for SimEvents) |

### **Queue length** — Specify the length of the message queue `16` (default) | `scalar`

Specify message queue capacity. The queue length can be specified as a
positive integer between `1` and *2*26-*1* (both included).

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueLength` |
| **Type**: character vector |
| **Values**: `'16'` | scalar |
| **Default**: `'16'` |

### **Queue type** — Specify message queue sorting policy `FIFO` (default) | `LIFO` | `Priority`

The block supports three message sorting policies:

- First-in-first-out (`FIFO`) — The oldest
  message in the storage departs first.
- Last-in-first-out (`LIFO`) — The newest
  message in the storage departs first.
- `Priority` — Messages or entities are
  sorted based on their priority.

  The priority queue can be used only when the **Overwrite the oldest element if queue is full** check
  box is cleared.

  **Note**

  Priority queue accepts only non-bus scalar and it does not
  support `fixed point` data type.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueType` |
| **Type**: character vector |
| **Values**: `'FIFO'` | `'LIFO'` | `'Priority'` |
| **Default**: `'FIFO'` |

### **Priority order** — Specify message queue priority `Ascending` (default) | `Descending`

Choose the direction of sorting messages based on priority.

- `Ascending` — Messages with smaller
  priority values appear in front of the queue.
- `Descending` — Messages with greater
  priority values appear in front of the queue.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue** and**Queue type** > **Priority**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PriorityOrder` |
| **Type**: character vector |
| **Values**: `'Ascending'` | `'Descending'` |
| **Default**: `'Ascending'` |

### **Show receive status** — Show whether a message was received `off` (default) | on

Select this check box to show whether a message was received. If this
check box is selected the block outputs `1` if it receives
a message successfully, and `0` otherwise.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowQueueStatus` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Initial value** — Set initial data value `[](unspecified)` (default) | `scalar` | `vector` | `matrix`

Enter an initial data value for the queue before the arrival of the first
message. The default value `[](unspecified)` is treated as
`0` with data type double.

To use this block to initialize a nonvirtual bus signal, specify the
initial value as a MATLAB® structure. For more information about initializing nonvirtual
bus signals using structures, see Specify Initial Conditions for Bus Elements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialValue` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Value source when queue is empty** — Value source for empty queue `Hold last value` (default) | `Use initial value`

Specify the value to receive when received message queue is empty.

- `Hold last value` (default) — Holds data
  read from the last message.

  Initially, if the block tries to receive a message and fails, it
  outputs the initial value.
- `Use initial value` — Writes default
  data.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ValueSourceWhenQueueIsEmpty` |
| **Type**: character vector |
| **Values**: `'Hold last value'` | `'Use initial value'` |
| **Default**: `'Hold last value'` |

### **Sample time (-1 for inherited)** — Specify the time interval between samples `-1` (default) | `scalar`

To inherit the sample time, set this parameter to `-1`.
See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: `'-1'` | scalar |
| **Default**: `'-1'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When you generate code for a model that uses a message queue and has multitasking
enabled, enable concurrent tasking behavior if that model will be deployed to a
multitasking environment. Otherwise, the generated code has the potential for data
corruption. You enable concurrent tasking behavior by selecting Allow tasks to execute concurrently on target.

**Note**

Receive blocks do not support row-major code generation.

## Version History

**Introduced in R2016a**
