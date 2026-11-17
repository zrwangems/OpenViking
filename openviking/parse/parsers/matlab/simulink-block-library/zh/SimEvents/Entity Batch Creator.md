---
type: simulink-block
title: 'Entity Batch Creator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitybatchcreator'
documentation_source_path: 'ref/entitybatchcreator.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Batch Creator

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入实体 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_1
  summary: 输出批次实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_a
  summary: 已到达实体数 标量
  direction: output
  data_types: double
- name: Port_d
  summary: 已离开模块的实体数 标量
  direction: output
  data_types: double
- name: Port_rem
  summary: 下一批次剩余实体数 标量
  direction: output
  data_types: double
- name: Port_pe
  summary: 模块中的待处理实体 off（默认）| on
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出批次实体 标量 | 向量 | 矩阵

离开模块的批次实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_a** — 已到达实体数 标量

已到达模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities arrived, a** 的复选框。

**数据类型：** `double`

### **Port\_d** — 已离开模块的实体数 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities departed, d** 的复选框。

**数据类型：** `double`

### **Port\_rem** — 下一批次剩余实体数 标量

下一批次剩余的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities remaining for the next batch, rem** 的复选框。

**数据类型：** `double`

### **Port\_pe** — 模块中的待处理实体 off（默认）| on

选中此复选框时，对于模块中的待处理实体输出 `1`，否则输出 `0`。

#### 依赖

要启用此端口，请选择 **Statistics** > **Pending entity in block, pe**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Number of entities in batch
  summary: 一个批次中的实体数量 4（默认）| 标量
  group: ''
  block_parameter: NumberOfEntitiesInBatch
  type: 字符向量
  values: '''4'' | 标量'
  default: '''4'''
- name: Entity type name
  summary: 合并传入实体后创建的批次实体的名称 Batch（默认）| 字符向量
  group: ''
  block_parameter: EntityTypeName
  type: 字符向量
  values: '''Batch'' | 字符向量'
  default: '''Batch'''
- name: Bus object
  summary: 指定是否将批次实体输出为总线对象 off（默认）| on
  group: ''
  block_parameter: BusObject
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Input entity name
  summary: 指定要附加到输入实体的名称 batch（默认）| 字符向量
  group: ''
  block_parameter: InputEntityName
  type: 字符向量
  values: '''batch'' | 字符向量'
  default: '''batch'''
- name: Event actions
  summary: 指定事件动作 Entry（默认）| Batch generate | Exit | Blocked
  group: ''
  block_parameter: EntryAction, BatchGenerateAction, ExitAction, BlockedAction
  type: character vector
  values: MATLAB code
  default: ''''''
- name: 已到达实体数，a
  summary: 输出已到达该模块的实体数 off（默认）| on
  group: ''
  block_parameter: NumberOfEntitiesArrived
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 已离开实体数，d
  summary: 输出已离开该模块的实体数 off（默认）| on
  group: ''
  block_parameter: NumberOfEntitiesDeparted
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 下一批次剩余实体数，rem
  summary: 输出下一批次剩余实体数 off（默认）| on
  group: ''
  block_parameter: NumberOfEntitiesRequiredForNextBatch
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: 模块中待处理实体，pe
  summary: 待处理实体 off（默认）| on
  group: ''
  block_parameter: PendingEntity
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Number of entities in batch** — 一个批次中的实体数量 `4`（默认）| 标量

指定一个批次中的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberOfEntitiesInBatch` |
| **类型**：字符向量 |
| **值**：`'4'` | 标量 |
| **默认值**：`'4'` |

### **Entity type name** — 合并传入实体后创建的批次实体的名称 `Batch`（默认）| 字符向量

指定合并传入实体后创建的批次实体的名称。

#### 程序化使用

|  |
| --- |
| **模块参数**：`EntityTypeName` |
| **类型**：字符向量 |
| **值**：`'Batch'` | 字符向量 |
| **默认值**：`'Batch'` |

### **Bus object** — 指定是否将批次实体输出为总线对象 off（默认）| on

指定是否将批次实体输出为总线对象。

#### 程序化使用

|  |
| --- |
| **模块参数**：`BusObject` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Input entity name** — 指定要附加到输入实体的名称 `batch`（默认）| 字符向量

指定要附加到输入实体的名称，可用于在批次实体中引用这些实体。

#### 程序化使用

|  |
| --- |
| **模块参数**：`InputEntityName` |
| **类型**：字符向量 |
| **值**：`'batch'` | 字符向量 |
| **默认值**：`'batch'` |

### **Event actions** — 指定事件动作 `Entry`（默认）| `Batch generate` | `Exit` | `Blocked`

指定实体在特定事件下的行为。例如，当实体进入模块时会调用 **Entry** 动作。要自定义实体进入、退出、被批处理或被阻塞时的动作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Batch generate action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关事件动作的详细信息，请参阅 Events and Event Actions。有关示例，请参阅 Manage Entities Using Event Actions

#### 编程使用

|  |
| --- |
| **模块参数**：`EntryAction, BatchGenerateAction, ExitAction, BlockedAction` |
| **类型**：character vector |
| **值**：MATLAB code |
| **默认值**：`''` |

### **已到达实体数，a** — 输出已到达该模块的实体数 `off`（默认）| `on`

已到达该模块的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfEntitiesArrived` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **已离开实体数，d** — 输出已离开该模块的实体数 `off`（默认）| `on`

已离开该模块的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **下一批次剩余实体数，rem** — 输出下一批次剩余实体数 `off`（默认）| `on`

输出仍在该模块中等待下一批实体的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfEntitiesRequiredForNextBatch` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **模块中待处理实体，pe** — 待处理实体 `off`（默认）| `on`

指示该模块中是否存在尚未离开的实体。对于待处理实体，该值为 `1`，否则为 `0`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PendingEntity` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |
## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

创建实体批次

Entity Batch Creator 接收预期数量的实体，并创建一个包含所有这些实体的批次实体。批处理实体是实体的数组。在对输入实体进行批处理之前，任何已获取的资源都必须使用 Resource Releaser 模块释放。

要在实体进入、退出、被批处理或被阻塞时自定义操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Batch generate action` 或 `Blocked action` 字段中输入 MATLAB® 代码。有关事件操作的详细信息，请参阅 Events and Event Actions。

您可以编写 MATLAB 代码来操作批处理实体的属性。例如，要在生成实体批次后访问属性，请选择 `Batch generate action` 并使用以下代码。

```
entity.batch
```

如果批次中的实体数量为 `4`，则 `entity.batch` 是一个 `4` 行 `1` 列的结构体数组。要操作批次中第三个实体的 `Attribute1`，请输入以下代码。

```
entity.batch(3).Attribute1
```

您可以在事件操作中引用批处理实体的属性。但不能在以下情况下引用它们：

- 优先级队列 — 不要将 **Priority source** 参数设置为 `PriorityAttribute`。
- Entity Server 模块 — 不要将 **Service time source** 参数设置为 `Attribute`。
- Output Switch 模块 — 不要将 **Switching criterion** 参数设置为 `From attribute`。

要将批次输出为总线对象，请选择 **Bus object** 参数。在以下情况下，考虑为批处理实体创建总线对象：

- 向 MATLAB Discrete-Event System 模块发送批处理实体或从中接收批处理实体。
- 向 Discrete-Event Chart 模块发送批处理实体或从中接收批处理实体。
- 将完整实体数据传递给 Simulink Function 模块时。
- 使用 Message Receive 模块将批处理实体转换为信号时。
