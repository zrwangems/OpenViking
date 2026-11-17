---
type: simulink-block
title: 'Conveyor System'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'conveyorsystem'
documentation_source_path: 'ref/conveyorsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Conveyor System

## 端口
```yaml
ports:
- name: Port_1
  summary: 传入实体 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: S
  summary: 传入匿名实体 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Port_1
  summary: 离开实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_d
  summary: 已离开实体数 关闭（默认）| 开启
  direction: output
  data_types: double
- name: Port_n
  summary: 模块中的实体数 关闭（默认）| 开启
  direction: output
  data_types: double
- name: Port_pe
  summary: 模块中的待处理实体 关闭（默认）| 开启
  direction: output
  data_types: double
- name: Port_s
  summary: 传送带速度 关闭（默认）| 开启
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 传入实体 标量 | 向量 | 矩阵

进入队列的实体的输入实体端口。当传送带速度为 `0` 时，模块不接受实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **S** — 传入匿名实体 标量

进入模块的匿名实体的输入端口。该实体携带的数据指定其到达时的新传送带速度。实体数据必须为 `0` 到 `Inf` 之间的非负值。新速度适用于模块中的所有实体，包括传入实体和已有实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Port\_1** — 离开实体 标量 | 向量 | 矩阵

离开队列的实体的输出实体端口

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开实体数 关闭（默认）| 开启

选中此复选框将输出已离开模块的实体数量。

#### 依赖

要启用此端口，请选中 **Statistics** > **Number of entities departed, d** 复选框。

**数据类型：** `double`

### **Port\_n** — 模块中的实体数 关闭（默认）| 开启

选中此复选框将输出模块中的实体数量。

#### 依赖

要启用此模块，请选中 **Statistics** > **Number of entities in block, n** 复选框。

**数据类型：** `double`

### **Port\_pe** — 模块中的待处理实体 关闭（默认）| 开启

选中此复选框时，对于模块中的待处理实体输出值 `1`，否则输出 `0`。

#### 依赖

要启用此端口，请选中 **Statistics** > **Pending entity in block, pe**。

**数据类型：** `double`

### **Port\_s** — 传送带速度 关闭（默认）| 开启

选中此复选框将输出传送带速度。

#### 依赖

要启用此端口，请选中 **Statistics** > **Conveyor speed, s**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Conveyor length
  summary: 表面长度 100（默认）| 数值
  group: ''
  block_parameter: mConveyorLength
  type: 字符向量
  values: '''100'' | 标量'
  default: '''100'''
- name: Conveyor speed
  summary: 传送带表面速度 1000（默认）| 数值
  group: ''
  block_parameter: mConveyorSpeed
  type: 字符向量
  values: '''1000'' | 标量'
  default: '''1000'''
- name: Minimum distance between entities
  summary: 最小物理间距 0（默认）| 数值
  group: ''
  block_parameter: mMinDisBetEntity
  type: 字符向量
  values: '''0'' | 标量'
  default: '''0'''
- name: Entity length source
  summary: 实体长度来源 Dialog（默认）| Attribute
  group: ''
  block_parameter: mEntityLengthSource
  type: 字符向量
  values: '''Dialog'' | ''Attribute'''
  default: '''Dialog'''
- name: Entity length value
  summary: 实体长度 1（默认）| 数值
  group: ''
  block_parameter: mEntityLength
  type: 字符向量
  values: '''1'' | 标量'
  default: '''1'''
- name: Entity length attribute name
  summary: 实体长度属性名称 Length（默认）| 字符向量
  group: ''
  block_parameter: mEntityLengthAttrName
  type: 字符向量
  values: '''Length'' | 字符向量'
  default: '''Length'''
- name: Blocked output behavior
  summary: 输出阻塞时的行为 Accumulate（默认）| Pause | Error
  group: ''
  block_parameter: mOutputBlockedOpt
  type: 字符向量
  values: '''Accumulate'' | ''Pause'' | ''Error'''
  default: '''Accumulate'''
- name: Error if conveyor full
  summary: 达到最大实体数量时的传送带行为 on（默认）| off
  group: ''
  block_parameter: mErrorUponFullOpt
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Variable conveyor speed
  summary: 恒定或可变传送带速度 off（默认）| on
  group: ''
  block_parameter: mIsVariableSpeed
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Number of entities departed, d
  summary: 已离开的实体数量 off（默认）| on
  group: ''
  block_parameter: mNumEntitiesDepOpt
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities in block, n
  summary: 现有实体数量 off（默认）| on
  group: ''
  block_parameter: mNumEntitiesInBlockOpt
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: 模块中的待处理实体，pe
  summary: 待处理实体 off（默认）| on
  group: ''
  block_parameter: mEntityPendingOpt
  type: 字符向量
  values: '''on'' | ''off'''
- name: 提取的实体数量，ex
  summary: 从此模块提取的实体数量 off（默认）| on
  group: ''
  block_parameter: mNumExtractedFromBlockOpt
  type: 字符向量
  values: '''on'' | ''off'''
- name: 传送带速度，s
  summary: 仿真期间传送带的速度 off（默认）| on
  group: ''
  block_parameter: mConveyorSpeedOpt
  type: 字符向量
  values: '''on'' | ''off'''
```

### **Conveyor length** — 表面长度 100（默认）| 数值

实体在其上移动的表面长度。有关详细信息，请参阅描述。

#### 编程用法

|  |
| --- |
| **模块参数**：`mConveyorLength` |
| **类型**：字符向量 |
| **值**：`'100'` | 标量 |
| **默认值**：`'100'` |

### **Conveyor speed** — 传送带表面速度 1000（默认）| 数值

实体在其上移动的表面速度。速度可以取大于 `0` 的值，仅当选中 **Variable conveyor speed** 复选框时其值才可以为零。有关详细信息，请参阅描述。

#### 编程用法

|  |
| --- |
| **模块参数**：`mConveyorSpeed` |
| **类型**：字符向量 |
| **值**：`'1000'` | 标量 |
| **默认值**：`'1000'` |

### **Minimum distance between entities** — 最小物理间距 0（默认）| 数值

实体在传送带系统上移动时保持的最小物理间距。有关详细信息，请参阅描述。

#### 编程用法

|  |
| --- |
| **模块参数**：`mMinDisBetEntity` |
| **类型**：字符向量 |
| **值**：`'0'` | 标量 |
| **默认值**：`'0'` |

### **Entity length source** — 实体长度来源 `Dialog`（默认）| `Attribute`

提供实体长度，从下拉列表中选择。

#### 依赖

- `Dialog` — 选择此选项将启用 **Entity length value** 参数。
- `Attribute` — 选择此选项将启用 **Entity length attribute name** 参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`mEntityLengthSource` |
| **类型**：字符向量 |
| **值**：`'Dialog'` | `'Attribute'` |
| **默认值**：`'Dialog'` |

### **Entity length value** — 实体长度 1（默认）| 数值

实体长度，指定为数值。有关详细信息，请参阅描述。

#### 依赖关系

要启用此参数，请为 **实体长度来源** 选择 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数**：`mEntityLength` |
| **类型**：字符向量 |
| **值**：`'1'` | 标量 |
| **默认值**：`'1'` |

### **Entity length attribute name** — 实体长度属性名称 `Length`（默认）| 字符向量

实体长度属性名称，指定为字符向量。

#### 依赖关系

要启用此参数，请为 **实体长度来源** 选择 `Attribute`。

#### 编程用法

|  |
| --- |
| **模块参数**：`mEntityLengthAttrName` |
| **类型**：字符向量 |
| **值**：`'Length'` | 字符向量 |
| **默认值**：`'Length'` |

### **Blocked output behavior** — 输出阻塞时的行为 `Accumulate`（默认）| `Pause` | `Error`

输出阻塞时的行为，从下拉列表中选择：

- `Accumulate` — 累积实体。在 `Accumulate` 模式下，实体继续在传送带表面上移动，直到其运动被前方另一个实体阻挡。

  例如，如果一个或多个实体被 Entity Find 模块从传送带表面提取出来，被提取实体后面的实体会继续向前移动，直到它们占据因提取而空出的空间。
- `Pause` — 暂停传送带系统。在 `Pause` 模式下，传送带表面上的所有实体停止并一起移动。当出口处的实体无法离开时，传送带表面停止移动。暂停期间，传送带系统不接受新实体。
- `Error` — 返回错误。在 `Error` 模式下，当实体被阻止进入传送带表面时，将显示错误。

#### 编程用法

|  |
| --- |
| **模块参数**：`mOutputBlockedOpt` |
| **类型**：字符向量 |
| **值**：`'Accumulate'` | `'Pause'` | `'Error'` |
| **默认值**：`'Accumulate'` |

### **Error if conveyor full** — 达到最大实体数量时的传送带行为 `on`（默认）| `off`

传送带表面已满时的传送带行为。

选中复选框on
:   如果传送带系统已满，则返回错误。

未选中复选框off
:   如果传送带系统已满，则不返回错误。

#### 编程用法

|  |
| --- |
| **模块参数**：`mErrorUponFullOpt` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Variable conveyor speed** — 恒定或可变传送带速度 `off`（默认）| `on`

指定传送带系统具有恒定速度还是可变速度。

未选中复选框off
:   恒定速度传送带系统。您可以使用 **传送带速度** 参数指定速度。

选中复选框on
:   可变速度传送带系统。将出现一个输入端口，用于接受携带数据的匿名实体以指定新的传送带速度。

#### 编程用法

|  |
| --- |
| **模块参数**：`mIsVariableSpeed` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Number of entities departed, d** — 已离开的实体数量 `off`（默认）| `on`

已离开该模块的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`mNumEntitiesDepOpt` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities in block, n** — 现有实体数量 `off`（默认）| `on`

输出该模块中存在的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`mNumEntitiesInBlockOpt` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **模块中的待处理实体，pe** — 待处理实体 `off`（默认）| `on`

指示模块中是否存在尚未离开的实体。
对于待处理实体，该值为 `1`，否则为
`0`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`mEntityPendingOpt` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **提取的实体数量，ex** — 从此模块提取的实体数量 `off`（默认）| `on`

输出由 Entity Find 模块从此模块中拉出的已提取实体数量。当提取一个实体时，
**已离开的实体数量，d** 和 **模块中的实体数量，n** 统计量会相应更新。
有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models。

#### 程序化使用

|  |
| --- |
| **模块参数**：`mNumExtractedFromBlockOpt` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### **传送带速度，s** — 仿真期间传送带的速度 `off`（默认）| `on`

输出仿真过程中传送带的速度。

#### 程序化使用

|  |
| --- |
| **模块参数**：`mConveyorSpeedOpt` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |
## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

运输实体

Conveyor System 模块在传送带表面上运输实体。实体通过滑入传送带表面进入该模块，并通过滑出传送带表面离开该模块。您可以指定传送带的速度。如果传送带速度是可变的，则该模块上会出现第二个输入端口，用于接收携带数据的匿名实体，这些数据用于指定新的传送带速度。使用此模块可对涉及生产系统或物流系统的运输应用进行建模。

在 Conveyor System 模块中：

- 您可以指定传送带的速度和表面长度。您可以指定长度以及被运输实体之间的最小距离。

  显示传送带长度、实体长度、实体间最小距离和传送带速度的简单示意图。
- 实体滑入传送带表面，当实体的前侧与表面入口重合时，该实体被视为位于传送带表面内部。

  显示实体前端与传送带表面入口对齐的简单示意图。
- 实体滑出传送带表面，当实体的后侧与表面入口重合时，该实体被视为位于传送带表面外部。

  显示实体后端与表面入口对齐的简单示意图。
- 传送带速度决定实体从进入表面到离开表面之间的总时间。

  实体可以进入和离开传送带表面，前提是：

  - 当 **Blocked output behavior** 设置为 `Accumulate` 时，没有其他实体阻挡该实体。
  - 当 **Blocked output behavior** 设置为 `Pause` 时，传送带表面未暂停。有关更多信息，请参阅 Blocked output behavior。

  显示实体进入、移动经过并离开传送带的简单示意图。

  例如，假设传送带长度为 `10`，实体长度为 `1`，传送带速度为 `5`。那么，实体离开表面需要 `2.2` 个仿真时间。`10/5 = 2` 用于穿过表面，`1/5 = 0.2` 用于离开表面，因为其长度为 `1`。
- 在实体进入传送带表面后，下一个实体会在第一个实体行进到指定的实体间最小距离后进入。

  显示仅当前方实体达到指定的实体间最小距离后，实体才进入传送带的简单示意图。
- 传送带系统的容量是表面上允许的最大实体数量。容量由总表面长度、实体长度以及实体间最小距离决定。

  例如，假设实体长度为 `1` 米，传送带系统表面长度为 `100` 米，实体间距离为 `15` 米。传送带系统的容量变为 `6` 个实体。

  简单示意图，说明六个长度为 1 米的实体如何能够容纳在表面长度为 100 米、实体间距离为 15 米的传送带系统上。
- 使用 **Conveyor length**、**Conveyor speed**、**Minimum distance between entities** 和 **Entity length value** 参数时，确保这些值彼此一致。

  例如，指定实体长度为 10 cm，传送带系统长度为 100 m，以实现一致性：

  - 将 **Conveyor length** 参数设置为 `100`。
  - 将 **Entity length** 参数设置为 0.1。
