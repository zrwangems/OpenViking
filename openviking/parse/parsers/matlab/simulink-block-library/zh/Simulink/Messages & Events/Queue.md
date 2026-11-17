---
type: simulink-block
title: 'Queue'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'queue'
documentation_source_path: 'slref/queue.html'
language: zh-CN
chinese_source: worker-translation
---

# Queue

## 端口

### 输入

### **Port\_1** — 输入实体或消息 标量 | 向量 | 矩阵

输入实体或消息，携带标量、总线或向量数据进入队列。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出实体或消息 标量 | 向量 | 矩阵

输出端口，允许队列头部的实体或消息在下游模块准备好接收时离开。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请在**统计**选项卡中，选中**已离开的实体数量，d**复选框。

**数据类型：** `double`

### **Port\_n** — 尚未离开模块的实体数量 标量

尚未离开模块的实体数量。

#### 依赖

要启用此端口，请在**统计**选项卡中，选中**模块中的实体数量，n**复选框。

**数据类型：** `double`

### **Port\_w** — 模块中实体的平均等待时间 标量

模块中实体的平均等待时间。

#### 依赖

要启用此端口，请在**统计**选项卡中，选中**平均等待时间，w**复选框。

**数据类型：** `double`

### **Port\_l** — 实体队列的平均长度 标量

**Port\_l** 输出实体队列的平均长度。

#### 依赖

要启用此端口，请在**统计**选项卡中，选中**平均队列长度，l**复选框。

**数据类型：** `double`

### **Port\_ex** — 被提取的实体数量 标量

从此模块中拉出的实体数量。

#### 依赖

要启用此端口，请在**统计**选项卡中，选中**被提取的实体数量，ex**复选框。

**数据类型：** `double`

## 参数

### **Overwrite the oldest element if queue is full** — 指定队列满时的覆盖策略 on（Simulink® 默认值） | off（SimEvents® 默认值）

选中此复选框可在两种队列覆盖策略之间进行选择。

- 如果选中此复选框，当队列已满时，传入的消息将覆盖最旧的元素。

  此模式表示一个简单的消息缓冲区，可用于在 Simulink 组件与生产代码之间生成异步通信。
- 如果清除此复选框，当队列已满时，模块将不接受新消息。

  在此模式下，您可以使用事件操作来操作实体数据并可视化统计数据。

  要在实体或消息进入、退出或被阻塞时自定义操作，请在**事件操作**选项卡的 `Entry action`、`Exit action` 或 `Blocked action` 字段中输入 MATLAB® 代码。有关详细信息，请参阅 Events and Event Actions (SimEvents)。

  有关示例，请参阅 Manage Entities Using Event Actions (SimEvents)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`QueueOverwriting` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'`（对于 Simulink）和 `'off'`（对于 SimEvents） |

### **Capacity** — 指定队列的容量 25（默认值） | 标量

指定队列的容量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Capacity` |
| **类型**：字符向量 |
| **值**：`'25'` | 标量 |
| **默认值**：`'25'` |

### **Queue type** — 选择队列类型 `FIFO`（默认值） | `LIFO` | `Priority`

选择队列类型。

- `FIFO` — 先进先出
- `LIFO` — 后进先出
- `Priority` — 按优先级顺序存储元素，请参阅 Serve High-Priority Customers by Sorting Entities Based on Priority (SimEvents)。
  当您清除 **Overwrite the oldest element if queue is full** 复选框时，可以选择 `Priority`。

  **注意**

  优先级队列不支持 `fixed point` 数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数**：`QueueType` |
| **类型**：字符向量 |
| **值**：`'FIFO'` | `'LIFO'` | `'Priority'` |
| **默认值**：`'FIFO'` |

### **Multicast tag** — 指定通过多播源广播时接受实体的标签 `A`（默认值） | 字符向量

指定通过多播源广播时接受实体的标签。Entity Multicast 模块需要 SimEvents 许可证。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框，并将 **Entity arrival source** 设置为 `Multicast` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MulticastTag` |
| **类型**：字符向量 |
| **值**：`'A'` | 字符向量 |
| **默认值**：`'A'` |

### **Priority source** — 指定实体的哪个属性决定其优先级 字符向量 | `entitySys.priority`

将优先级源指定为您创建的自定义实体属性，或专门指定为 `entitySys.priority` 属性。

例如，假设您在 Entity Generator 模块的 Entity Type 选项卡中为实体添加了两个新属性，分别命名为 `height` 和 `width`。这些属性将以字符向量的形式作为 **Priority source** 参数的选项出现。参数的值决定实体的优先级。

**注意**

如果您未将默认文本提示 PriorityAttribute 替换为优先级源，则模型在编译期间将生成错误。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框，并将 **Queue type** 设置为 `Priority` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`PrioritySource` |
| **类型**：字符向量 |
| **值**：`'entity'` | `'entitySys.priority'` | 字符向量 |

### **Sorting direction** — 选择基于优先级的排序方向 `Ascending`（默认值） | `Descending`

选择基于优先级的排序方向。

- `Ascending` — 优先级值较小的元素出现在队列前面。
- `Descending` — 优先级值较大的元素出现在队列前面。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框，并将 **Queue type** 设置为 `Priority` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SortingDirection` |
| **类型**：字符向量 |
| **值**：`'Ascending'` | `'Descending'` |
| **默认值**：`'Ascending'` |

### **Entity arrival source** — 选择实体的到达源 `Input port`（默认值） | `Multicast`

选择实体的到达源。

- `Input port` — 输入端口是消息或实体的来源。
- `Multicast` — Entity Multicast 模块是实体的来源。Entity Multicast 模块需要 SimEvents 许可证。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`EntityArrivalSource` |
| **类型**：字符向量 |
| **值**：`'Input port'` | `'Multicast'` |
| **默认值**：`'Input port'` |

### **Event action** — 指定实体在特定事件中的行为 `Entry`（默认值） | `Exit` | `Blocked`

指定实体在特定事件中的行为。在 **Event action** 参数中定义行为。**Entry** 和 **Exit** 操作分别在实体进入之后和实体退出之前调用。**Blocked** 操作在实体被阻塞之后调用。有关详细信息，请参阅 Events and Event Actions (SimEvents)。

**注意**

如果事件操作更改了实体，则相关模块行为（例如重新排序优先级队列以及重新调度任何事件）将在事件操作完全完成并返回之后发生。

**注意**

事件操作不支持 `fixed point` 数据类型。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框时，事件操作可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`EntryAction, ExitAction, BlockedAction` |
| **类型**：字符向量 |
| **值**：MATLAB 代码 |
| **默认值**：`''` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认值） | `on`

已离开模块的实体数量。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框时，**Number of entities departed, d** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities in block, n** — 输出模块中存在的、尚未离开的实体数量 `off`（默认值） | `on`

模块中存在的、但尚未离开的实体数量。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框时，**Number of entities in block, n** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberEntitiesInBlock` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Average wait, w** — 输出平均等待时间 `off`（默认值） | `on`

离开模块的实体的等待时间之和除以其总数。*等待时间* 是实体从进入 Entity Queue 模块到退出的持续时间。有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis (SimEvents)。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框时，**Average wait, w** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AverageWait` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Average queue length, l** — 输出实体队列的平均长度 `off`（默认值） | `on`

累积的时间加权平均队列大小。模块通过以下方式计算此值：

1. 将队列大小乘以其持续时间以计算时间加权队列大小
2. 将所有时间加权队列大小求和并在总时间上取平均值

有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis (SimEvents)。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框时，**Average queue length, l** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AverageQueueLength` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities extracted, ex** — 从此模块中提取的实体数量 `off`（默认值） | `on`

输出由 Entity Find 模块从此模块中拉出的被提取实体数量。Entity Find 模块需要 SimEvents 许可证。如果被提取的实体是队列中的第一个实体，则下一个实体被设置为离开模块的待处理实体。如果实体属性在优先级队列中定义了优先级，并且被 Entity Find 模块修改，则队列将重新排序。当实体被提取时，**Number of entities departed, d**、**Number of entities in block, n**、**Average wait, w** 和 **Average queue length, l** 统计数据将相应更新。有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models (SimEvents)。

#### 依赖

当您清除 **Overwrite the oldest element if queue is full** 复选框时，**Number of entities extracted, ex** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumEntitiesExtracted` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

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

事件操作和统计不支持代码生成。

当您为包含消息队列且启用了多任务的模型生成代码时，如果该模型将部署到多任务环境，请启用并发任务行为。否则，生成的代码可能存在数据损坏的风险。您可以通过选中 Allow tasks to execute concurrently on target 来启用并发任务行为。

## 版本历史

**在 R2016a 中引入**

## 描述

将消息和实体入队

此模块根据实体或消息的到达顺序或优先级将其存储在队列中。当下游模块准备好接收时，队列头部的每个元素将离开。

您可以指定队列的容量以及队列满时的策略。该模块支持三种不同的消息或队列排序策略：先进先出（FIFO）、后进先出（LIFO）和优先级。仅当清除 **Overwrite the oldest element if queue is full** 复选框时，才能使用优先级队列。
