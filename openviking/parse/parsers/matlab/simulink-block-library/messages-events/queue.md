---
type: simulink-block
title: 'Queue'
family: messages-events
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'queue'
---

# Queue

Enqueue messages and entities

## 中文

将消息和实体入队

### 库
Simulink / Messages & Events SimEvents

### 描述
此模块根据实体或消息的到达顺序或优先级，将它们存储在队列中。当下游模块准备好接收时，队列头部的每个元素会离开。

您可以指定队列的容量，以及队列已满时的策略。该模块支持三种不同的消息或队列排序策略：先进先出 (FIFO)、后进先出 (LIFO) 和优先级。仅当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，才能使用优先级队列。

### 端口

#### 输入

#### **Port\_1** — 输入实体或消息 标量 | 向量 | 矩阵

输入实体或消息，携带 scalar、bus 或 vector 数据进入队列。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

#### 输出

#### **Port\_1** — 输出实体或消息 标量 | 向量 | 矩阵

输出端口，当下游模块准备好接收时，允许队列头部的实体或消息离开。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

#### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖关系

要启用此端口，请在 **统计信息** 选项卡中，选中 **已离开的实体数量, d** 复选框。

**数据类型：** `double`

#### **Port\_n** — 尚未离开模块的实体数量 标量

尚未离开模块的实体数量。

#### 依赖关系

要启用此端口，请在 **统计信息** 选项卡中，选中 **模块中的实体数量, n** 复选框。

**数据类型：** `double`

#### **Port\_w** — 模块中实体的平均等待时间 标量

模块中实体的平均等待时间。

#### 依赖关系

要启用此端口，请在 **统计信息** 选项卡中，选中 **平均等待时间, w** 复选框。

**数据类型：** `double`

#### **Port\_l** — 实体队列的平均长度 标量

**Port\_l** 输出实体队列的平均长度。

#### 依赖关系

要启用此端口，请在 **统计信息** 选项卡中，选中 **平均队列长度, l** 复选框。

**数据类型：** `double`

#### **Port\_ex** — 提取的实体数量 标量

从此模块中拉出的实体数量。

#### 依赖关系

要启用此端口，请在 **统计信息** 选项卡中，选中 **提取的实体数量, ex** 复选框。

**数据类型：** `double`

### 参数

#### **如果队列已满，则覆盖最旧的元素** — 指定队列覆盖策略 on（Simulink® 的默认值） | off（SimEvents® 的默认值）

选中此复选框可在两种队列覆盖策略之间进行选择。

- 如果选中该复选框，则当队列已满时，传入消息会覆盖最旧的元素。

  此模式表示一个简单的消息缓冲区，您可以使用它在 Simulink 组件和生产代码之间生成异步通信。
- 如果清除该复选框，则当队列已满时，模块不会接受新消息。

  在此模式下，您可以使用事件动作操作实体数据，并可视化统计信息。

  若要自定义实体或消息进入、退出或被阻塞时的动作，请在 **事件动作** 选项卡的 `Entry action`、`Exit action` 或 `Blocked action` 字段中输入 MATLAB® 代码。有关详细信息，请参阅 事件和事件动作 (SimEvents)。

  有关示例，请参阅 使用事件动作管理实体 (SimEvents)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `QueueOverwriting` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'`（对于 Simulink）和 `'off'`（对于 SimEvents） |

#### **容量** — 指定队列的容量 25（默认值） | scalar

指定队列的容量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Capacity` |
| **类型**: character vector |
| **值**: `'25'` | scalar |
| **默认值**: `'25'` |

#### **队列类型** — 选择队列类型 `FIFO`（默认值） | `LIFO` | `Priority`

选择队列类型。

- `FIFO` — 先进先出
- `LIFO` — 后进先出
- `Priority` — 按优先级顺序存储元素，请参阅 通过基于优先级排序实体来服务高优先级客户 (SimEvents)。当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，可以选择 `Priority`。

  **注意**

  优先级队列不支持 `fixed point` 数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数**: `QueueType` |
| **类型**: character vector |
| **值**: `'FIFO'` | `'LIFO'` | `'Priority'` |
| **默认值**: `'FIFO'` |

#### **多播标签** — 指定接受通过多播源广播的实体时的标签 `A`（默认值） | character vector

指定接受通过多播源广播的实体时的标签。Entity Multicast 模块需要 SimEvents 许可证。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框，并将 **实体到达源** 设置为 `Multicast` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `MulticastTag` |
| **类型**: character vector |
| **值**: `'A'` | character vector |
| **默认值**: `'A'` |

#### **优先级来源** — 指定实体的哪个属性决定其优先级 character vector | `entitySys.priority`

将优先级来源指定为您创建的自定义实体属性，或专门指定为 `entitySys.priority` 属性。

例如，假设您在 Entity Generator 模块的 Entity Type 选项卡中为实体添加了两个新属性，分别名为 `height` 和 `width`。这些属性以 character vector 形式作为 **优先级来源** 参数的选项出现。这些参数的值决定实体优先级。

**注意**

如果未将默认文本提示 PriorityAttribute 替换为优先级来源，则模型会在编译期间生成错误。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框，并将 **队列类型** 设置为 `Priority` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PrioritySource` |
| **类型**: character vector |
| **值**: `'entity'` | `'entitySys.priority'` | character vector |

#### **排序方向** — 基于优先级选择排序方向 `Ascending`（默认值） | `Descending`

基于优先级选择排序方向。

- `Ascending` — 具有较小优先级值的元素出现在队列前面。
- `Descending` — 具有较大优先级值的元素出现在队列前面。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框，并将 **队列类型** 设置为 `Priority` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `SortingDirection` |
| **类型**: character vector |
| **值**: `'Ascending'` | `'Descending'` |
| **默认值**: `'Ascending'` |

#### **实体到达源** — 选择实体的到达源 `Input port`（默认值） | `Multicast`

选择实体的到达源。

- `Input port` — Input port 是消息或实体的来源。
- `Multicast` — Entity Multicast 模块是实体的来源。Entity Multicast 模块需要 SimEvents 许可证。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `EntityArrivalSource` |
| **类型**: character vector |
| **值**: `'Input port'` | `'Multicast'` |
| **默认值**: `'Input port'` |

#### **事件动作** — 指定实体在某些事件中的行为 `Entry`（默认值） | `Exit` | `Blocked`

指定实体在某些事件中的行为。在 **事件动作** 参数中定义行为。**Entry** 和 **Exit** 动作分别在实体进入之后和实体退出之前调用。**Blocked** 动作在实体被阻塞之后调用。有关详细信息，请参阅 事件和事件动作 (SimEvents)。

**注意**

如果事件动作更改了实体，则相关模块行为（例如重新排序优先级队列以及重新调度任何事件）将在事件动作完全完成并返回后发生。

**注意**

事件动作不支持 `fixed point` 数据类型。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，事件动作可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `EntryAction, ExitAction, BlockedAction` |
| **类型**: character vector |
| **值**: MATLAB code |
| **默认值**: `''` |

#### **已离开的实体数量, d** — 输出已离开模块的实体数量 `off`（默认值） | `on`

已离开模块的实体数量。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，**已离开的实体数量, d** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumberEntitiesDeparted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

#### **模块中的实体数量, n** — 输出模块中存在但尚未离开的实体数量 `off`（默认值） | `on`

模块中存在但尚未离开的实体数量。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，**模块中的实体数量, n** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumberEntitiesInBlock` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

#### **平均等待时间, w** — 输出平均等待时间 `off`（默认值） | `on`

离开模块的实体的等待时间总和除以其总数。*等待时间* 是实体在 Entity Queue 模块进入和退出之间的持续时间。有关详细信息，请参阅 使用统计分析解释 SimEvents 模型 (SimEvents)。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，**平均等待时间, w** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AverageWait` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

#### **平均队列长度, l** — 输出实体队列的平均长度 `off`（默认值） | `on`

累积的时间加权平均队列大小。该模块通过以下方式计算此值：

1. 将队列大小乘以其持续时间，以计算时间加权队列大小
2. 将所有时间加权队列大小相加，并在总时间上取平均值

有关详细信息，请参阅 使用统计分析解释 SimEvents 模型 (SimEvents)。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，**平均队列长度, l** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AverageQueueLength` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

#### **提取的实体数量, ex** — 从此模块提取的实体数量 `off`（默认值） | `on`

输出由 Entity Find 模块从此模块中拉出的提取实体数量。Entity Find 模块需要 SimEvents 许可证。如果提取的实体是队列中的第一个实体，则下一个实体将设置为要离开模块的待处理实体。如果某个实体属性在优先级队列中定义优先级，并且该属性被 Entity Find 模块修改，则队列会重新排序。提取实体时，**已离开的实体数量, d**、**模块中的实体数量, n**、**平均等待时间, w** 和 **平均队列长度, l** 统计信息会相应更新。有关查找和提取实体的详细信息，请参阅 在 SimEvents 模型中查找和提取实体 (SimEvents)。

#### 依赖关系

当清除 **如果队列已满，则覆盖最旧的元素** 复选框时，**提取的实体数量, ex** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumEntitiesExtracted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

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

事件动作和统计信息不支持代码生成。

当为包含消息队列并启用了多任务的模型生成代码时，如果该模型将部署到多任务环境，请启用并发任务行为。否则，生成的代码可能发生数据损坏。通过选择 Allow tasks to execute concurrently on target 来启用并发任务行为。

### 版本历史

**在 R2016a 中引入**

## Libraries

Simulink / Messages & Events SimEvents

## Description

This block stores entities or messages in a queue, based on their order of arrival or
priority. Each element at the head of the queue departs when the downstream block is
ready to accept it.

You can specify the capacity of the queue, and the policy when the queue is full. The
block supports three different message or queue sorting policies, first-in-first out
(FIFO), last-in-first out (LIFO), and priority. The priority queue can be used only when
the **Overwrite the oldest element if queue is full** check box is
cleared.

## Ports

### Input

### **Port\_1** — Input entity or message scalar | vector | matrix

Input entity or message that carries scalar, bus, or vector data to
enter the queue.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output entity or message scalar | vector | matrix

Output port that allows entities or messages at the head of the queue
to depart when a downstream block is ready to accept them.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — Number of entities that have departed the block scalar

Number of entities that have departed the block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Number of entities departed, d** check
box.

**Data Types:** `double`

### **Port\_n** — Number of entities that have not yet departed the block scalar

Number of entities that have not yet departed the block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Number of entities in block, n** check
box.

**Data Types:** `double`

### **Port\_w** — Average wait time for entities in the block scalar

Average wait time for entities in the block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Average wait, w** check box.

**Data Types:** `double`

### **Port\_l** — Average length of the entity queue scalar

**Port\_l** outputs the average length of the entity
queue.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Average queue length, l** check
box.

**Data Types:** `double`

### **Port\_ex** — Number of entities extracted scalar

Number of entities that are pulled out of this block.

#### Dependencies

To enable this port, in the **Statistics** tab,
select the **Number of entities extracted, ex**
check box.

**Data Types:** `double`

## Parameters

### **Overwrite the oldest element if queue is full** — Specify queue overwriting policy on (default for Simulink®) | off (default for SimEvents®)

Select this check box to choose between two queue overwriting
policies.

- If you select the check box, an incoming message overwrites the
  oldest if the queue is full.

  This mode represents a simple message buffer that you can use to
  generate asynchronous communication between Simulink components and production code.
- If you clear the check box, the block does not accept new messages
  if the queue is full.

  In this mode, you can manipulate entity data using event actions
  and visualize statistics.

  To customize actions when entities or messages enter, exit, or are
  blocked, enter MATLAB® code in the `Entry action`,
  `Exit action`, or `Blocked
  action` field of the **Event actions**
  tab. For more information, see Events and Event Actions (SimEvents).

  For an example, see Manage Entities Using Event Actions (SimEvents).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueOverwriting` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` (for Simulink) and `'off'` (for SimEvents) |

### **Capacity** — Specify the capacity of the queue 25 (default) | scalar

Specify the capacity of the queue.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Capacity` |
| **Type**: character vector |
| **Values**: `'25'` | scalar |
| **Default**: `'25'` |

### **Queue type** — Choose the queue type `FIFO` (default) | `LIFO` | `Priority`

Choose the queue type.

- `FIFO` — first-in-first-out
- `LIFO` — last-in-first-out
- `Priority` — store elements in order of
  priority, see Serve High-Priority Customers by Sorting Entities Based on Priority (SimEvents).
  `Priority` can be selected when you
  clear the **Overwrite the oldest element if queue is
  full** check box.

  **Note**

  Priority queue does not support `fixed
  point` data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueType` |
| **Type**: character vector |
| **Values**: `'FIFO'` | `'LIFO'` | `'Priority'` |
| **Default**: `'FIFO'` |

### **Multicast tag** — Specify the tag when accepting entities broadcast via multicast sources `A` (default) | character vector

Specify the tag when accepting entities broadcast via multicast sources.
The Entity Multicast block requires SimEvents license.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box, and set
**Entity arrival source** to
`Multicast`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MulticastTag` |
| **Type**: character vector |
| **Values**: `'A'` | character vector |
| **Default**: `'A'` |

### **Priority source** — Specify which attribute of the entity determines its priority character vector | `entitySys.priority`

Specify the priority source either as a custom entity attribute that you
created, or the `entitySys.priority` attribute,
specifically.

For example, assume that you added two new attributes named
`height` and `width` for an entity in
the Entity Type tab of a Entity Generator block. These
attributes appear as options, in the form of character vectors, for the
**Priority source** parameter. The value of the
parameters determine the entity priority.

**Note**

If you do not replace the default text prompt, PriorityAttribute, with
a priority source, then the model generates an error during
compilation.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box, and set
**Queue type** to
`Priority`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PrioritySource` |
| **Type**: character vector |
| **Values**: `'entity'` | `'entitySys.priority'` | character vector |

### **Sorting direction** — Choose the direction of sorting based on priority `Ascending` (default) | `Descending`

Choose the direction of sorting based on priority.

- `Ascending` — Elements with smaller
  priority values appear in front of the queue.
- `Descending` — Elements with greater
  priority values appear in front of the queue.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box, and set
**Queue type** to
`Priority`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SortingDirection` |
| **Type**: character vector |
| **Values**: `'Ascending'` | `'Descending'` |
| **Default**: `'Ascending'` |

### **Entity arrival source** — Choose the source of arrival for the entities `Input port` (default) | `Multicast`

Choose the source of arrival for the entities.

- `Input port` — Input port is source of
  messages or entities.
- `Multicast` — Entity
  Multicast block is source of entities. The Entity
  Multicast block requires SimEvents license.

#### Dependencies

This parameter is visible when you clear the **Overwrite the
oldest element if queue is full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntityArrivalSource` |
| **Type**: character vector |
| **Values**: `'Input port'` | `'Multicast'` |
| **Default**: `'Input port'` |

### **Event action** — Specify the behavior of the entity in certain events `Entry` (default) | `Exit` | `Blocked`

Specify the behavior of the entity in certain events. Define the behavior
in the **Event action** parameter. The
**Entry** and the **Exit** actions are
called just after the entity entry and just before entity exit. The
**Blocked** action is called after an entity is
blocked. For more information, see Events and Event Actions (SimEvents).

**Note**

If an event action changes an entity, related block behavior such
as resorting a priority queue, and rescheduling of any events, will
occur after the event action has fully finished and returned.

**Note**

Event actions do not support `fixed point` data
type.

#### Dependencies

Event actions are visible when you clear the **Overwrite the
oldest element if queue is full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EntryAction, ExitAction, BlockedAction` |
| **Type**: character vector |
| **Values**: MATLAB code |
| **Default**: `''` |

### **Number of entities departed, d** — Outputs the number of entities that have departed the block `off` (default) | `on`

Number of entities that have departed the block.

#### Dependencies

**Number of entities departed, d** is visible when
you clear the **Overwrite the oldest element if queue is
full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesDeparted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities in block, n** — Outputs the number of entities present in the block, that are yet to depart `off` (default) | `on`

Number of entities present in the block, but which are yet to
depart.

#### Dependencies

**Number of entities in block, n** is visible when
you clear the **Overwrite the oldest element if queue is
full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberEntitiesInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average wait, w** — Outputs the average wait time `off` (default) | `on`

Sum of the wait times for entities departing the block divided by their
total number. *Wait time* is the duration between the
Entity Queue block entry and exit of an entity. For more
information, see Interpret SimEvents Models Using Statistical Analysis (SimEvents).

#### Dependencies

**Average wait, w** is visible when you clear the
**Overwrite the oldest element if queue is full**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageWait` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Average queue length, l** — Outputs the average length of the entity queue `off` (default) | `on`

Accumulated time-weighted average queue size. The block computes this
value by:

1. Multiplying the size of the queue by its duration to calculate
   time-weighted queue size
2. Summing up all time-weighted queue sizes and averaging them
   over total time

For more information, see Interpret SimEvents Models Using Statistical Analysis (SimEvents).

#### Dependencies

**Average queue length, l** is visible when you clear
the **Overwrite the oldest element if queue is full**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AverageQueueLength` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Number of entities extracted, ex** — Number of entities extracted from this block `off` (default) | `on`

Outputs the number of extracted entities which are pulled out from this
block by the Entity Find block. The Entity
Find block requires a SimEvents license. If the extracted entity is the first entity in the
queue, the next entity is set as the pending entity to leave the block. If
an entity attribute defines the priority in a priority queue and it is
modified by the Entity Find block, the queue is sorted again.
When an entity is extracted, **Number of entities departed,
d**, **Number of entities in block, n**,
**Average wait, w**, and **Average queue
length, l** statistics are updated accordingly. For more
information about finding and extracting entities, see Find and Extract Entities in SimEvents Models (SimEvents).

#### Dependencies

**Number of entities extracted, ex** is visible when
you clear the **Overwrite the oldest element if queue is
full** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumEntitiesExtracted` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

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

Code generation is not supported for event actions and statistics.

When you generate code for a model that contains a message queue and has
multitasking enabled, enable concurrent tasking behavior if that model will be
deployed to a multitasking environment. Otherwise, the generated code has the
potential for data corruption. You enable concurrent tasking behavior by selecting
Allow tasks to execute concurrently on target.

## Version History

**Introduced in R2016a**
