---
type: simulink-block
title: 'Entity Batch Splitter'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitybatchsplitter'
documentation_source_path: 'ref/entitybatchsplitter.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Batch Splitter

## 端口
```yaml
ports:
- name: port_1
  summary: 输入批次实体 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: port_1
  summary: 输出实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: port_a
  summary: 已到达实体数量 标量
  direction: output
  data_types: double
- name: port_d
  summary: 已离开模块的实体数量 标量
  direction: output
  data_types: double
- name: port_rem
  summary: 模块中剩余实体数量 标量
  direction: output
  data_types: double
- name: port_pe
  summary: 模块中的待处理实体 off（默认）| on
  direction: output
  data_types: double
```

### 输入

### **port\_1** — 输入批次实体 标量 | 向量 | 矩阵

进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **port\_1** — 输出实体 标量 | 向量 | 矩阵

离开模块的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_a** — 已到达实体数量 标量

已到达模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities arrived, a** 的复选框。

**数据类型：** `double`

### **port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities departed, d** 的复选框。

**数据类型：** `double`

### **port\_rem** — 模块中剩余实体数量 标量

仍在模块中尚未离开的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities remaining to depart, rem** 的复选框。

**数据类型：** `double`

### **port\_pe** — 模块中的待处理实体 `off`（默认）| `on`

选中此复选框时，对于模块中的待处理实体输出值 `1`，否则输出 `0`。

#### 依赖

要启用此端口，请选择 **Statistics** > **Pending entity in block, pe**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Event actions
  summary: 指定事件动作 Entry（默认）| Unbatch | Exit | Blocked
  group: ''
  block_parameter: EntryAction, UnbatchAction, ExitAction, BlockedAction
  type: 字符向量
  values: MATLAB 代码
  default: ''''''
- name: Number of entities arrived, a
  summary: 输出已到达模块的实体数量 off（默认）| on
  group: ''
  block_parameter: NumberOfEntitiesArrived
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities departed, d
  summary: 输出已离开模块的实体数量 off（默认）| on
  group: ''
  block_parameter: NumberOfEntitiesDeparted
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities remaining to depart, rem
  summary: 输出模块中剩余的实体数量 off（默认）| on
  group: ''
  block_parameter: NumberOfEntitiesWaitingToDepart
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Pending entity in block, pe
  summary: 待处理实体 off（默认）| on
  group: ''
  block_parameter: PendingEntity
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Event actions** — 指定事件动作 `Entry`（默认）| `Unbatch` | `Exit` | `Blocked`

指定实体在特定事件下的行为。例如，当实体进入模块时会调用 **Entry** 动作。要自定义实体进入、离开、取消批处理或被阻塞时的动作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Unbatch action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关事件动作的详细信息，请参阅 Events and Event Actions。有关示例，请参阅 Manage Entities Using Event Actions

#### 编程用法

|  |
| --- |
| **模块参数**：`EntryAction, UnbatchAction, ExitAction, BlockedAction` |
| **类型**：字符向量 |
| **值**：MATLAB 代码 |
| **默认值**：`''` |

### **Number of entities arrived, a** — 输出已到达模块的实体数量 `off`（默认）| `on`

已到达模块的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfEntitiesArrived` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认）| `on`

选中此复选框时输出已离开模块的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfEntitiesDeparted` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities remaining to depart, rem** — 输出模块中剩余的实体数量 `off`（默认）| `on`

输出仍在模块中尚未离开的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfEntitiesWaitingToDepart` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Pending entity in block, pe** — 待处理实体 `off`（默认）| `on`

指示模块中是否存在尚未离开的实体。对于待处理实体，该值为 `1`，否则为 `0`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`PendingEntity` |
| **类型**：字符向量 |
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

拆分批量实体

Entity Batch Splitter 模块将批量实体拆分为其各个单独实体，并通过输出端口输出每个实体。批量实体是 Entity Batch Creator 模块的输出。

若要自定义实体进入、退出、被阻塞或取消批量时的操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Blocked action` 或 `Unbatch action` 字段中输入 MATLAB® 代码。
