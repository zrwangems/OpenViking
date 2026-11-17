---
type: simulink-block
title: 'Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'receive'
documentation_source_path: 'slref/receive.html'
language: zh-CN
chinese_source: worker-translation
---

# Receive

## 端口

### 输入

### **Port\_1** — 输入消息 标量 | 向量 | 矩阵

消息的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_S** — 显示是否接收到消息 标量

如果模块成功接收到消息，则输出 `1`，否则输出 `0`。

#### 依赖关系

要启用此端口，请选中标记为 **Show receive status** 的复选框。

**数据类型：** `double`

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

信号的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## 参数

### **Use internal queue** — 选择使用内部队列 on（SimEvents® 的默认值） | off（Simulink® 的默认值）

如果使用内部队列接收消息，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**：`UseInternalQueue` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Overwrite the oldest element if queue is full** — 指定队列覆盖策略 on（Simulink 的默认值） | off（SimEvents 的默认值）

选中此复选框可在两种队列覆盖策略之间进行选择。

- 如果选中此复选框，当队列已满时，传入消息将覆盖最旧的消息。
- 如果清除此复选框，当队列已满时，模块将不接受新消息。

#### 依赖关系

当选中标记为 **Use internal queue** 的复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**：`QueueOverwriting` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'`（对于 Simulink）和 `'off'`（对于 SimEvents） |

### **Queue length** — 指定消息队列的长度 `16`（默认值） | `scalar`

指定消息队列容量。队列长度可以指定为 `1` 到 *2*26-*1*（含两端）之间的正整数。

#### 依赖关系

当选中标记为 **Use internal queue** 的复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**：`QueueLength` |
| **类型**：字符向量 |
| **值**：`'16'` | scalar |
| **默认值**：`'16'` |

### **Queue type** — 指定消息队列排序策略 `FIFO`（默认值） | `LIFO` | `Priority`

模块支持三种消息排序策略：

- 先进先出（`FIFO`）— 存储中最旧的消息最先离开。
- 后进先出（`LIFO`）— 存储中最新的消息最先离开。
- `Priority` — 消息或实体根据其优先级进行排序。

  仅当清除 **Overwrite the oldest element if queue is full** 复选框时，才能使用优先级队列。

  **注意**

  优先级队列仅接受非总线标量，且不支持 `fixed point` 数据类型。

#### 依赖关系

当选中标记为 **Use internal queue** 的复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**：`QueueType` |
| **类型**：字符向量 |
| **值**：`'FIFO'` | `'LIFO'` | `'Priority'` |
| **默认值**：`'FIFO'` |

### **Priority order** — 指定消息队列优先级 `Ascending`（默认值） | `Descending`

选择基于优先级对消息进行排序的方向。

- `Ascending` — 优先级值较小的消息出现在队列前面。
- `Descending` — 优先级值较大的消息出现在队列前面。

#### 依赖关系

当选中标记为 **Use internal queue** 的复选框且 **Queue type** > **Priority** 时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**：`PriorityOrder` |
| **类型**：字符向量 |
| **值**：`'Ascending'` | `'Descending'` |
| **默认值**：`'Ascending'` |

### **Show receive status** — 显示是否接收到消息 `off`（默认值） | on

选中此复选框可显示是否接收到消息。如果选中此复选框，模块在成功接收到消息时输出 `1`，否则输出 `0`。

#### 编程用法

|  |
| --- |
| **模块参数**：`ShowQueueStatus` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Initial value** — 设置初始数据值 `[](unspecified)`（默认值） | `scalar` | `vector` | `matrix`

在第一条消息到达之前，为队列输入初始数据值。默认值 `[](unspecified)` 被视为数据类型为 double 的 `0`。

要使用此模块初始化非虚拟总线信号，请将初始值指定为 MATLAB® 结构体。有关使用结构体初始化非虚拟总线信号的详细信息，请参阅 Specify Initial Conditions for Bus Elements。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitialValue` |
| **类型**：字符向量 |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Value source when queue is empty** — 空队列时的值来源 `Hold last value`（默认值） | `Use initial value`

指定当接收消息队列为空时要接收的值。

- `Hold last value`（默认值）— 保持从最后一条消息读取的数据。

  最初，如果模块尝试接收消息但失败，则输出初始值。
- `Use initial value` — 写入默认数据。

#### 依赖关系

当选中标记为 **Use internal queue** 的复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**：`ValueSourceWhenQueueIsEmpty` |
| **类型**：字符向量 |
| **值**：`'Hold last value'` | `'Use initial value'` |
| **默认值**：`'Hold last value'` |

### **Sample time (-1 for inherited)** — 指定采样之间的时间间隔 `-1`（默认值） | `scalar`

要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：`'-1'` | scalar |
| **默认值**：`'-1'` |

## 所属库

Simulink / Messages & Events SimEvents

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当为使用消息队列且启用了多任务的模型生成代码时，如果该模型将部署到多任务环境，请启用并发任务行为。否则，生成的代码可能会出现数据损坏。通过选择 Allow tasks to execute concurrently on target 来启用并发任务行为。

**注意**

Receive 模块不支持行主序代码生成。

## 版本历史

**在 R2016a 中引入**

## 描述

接收消息

Receive 模块从接收到的消息中提取数据，并将其写入输出信号端口。如果模块执行时没有新消息，模块将使用 **Value source when queue is empty** 值。Receive 和 Message Receive 模块是相同的模块。

- 选择 `Hold last value` 以保持从最后一条消息读取的数据。
- 选择 `Use initial value` 以写入默认数据。
