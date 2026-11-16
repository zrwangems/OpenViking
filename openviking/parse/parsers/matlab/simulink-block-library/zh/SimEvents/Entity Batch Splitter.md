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

### 输入

### **port\_1** — 输入批次实体 标量 | 向量 | 矩阵

输入实体端口，用于进入模块的实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### 输出

### **port\_1** — 输出实体 标量 | 向量 | 矩阵

输出实体端口，用于离开模块的实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_a** — 已到达的实体数（标量）

已到达该模块的实体数。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Number of entities arrived, a** 的框。

**数据类型：** `double`

### **port\_d** — 已离开该模块的实体数（标量）

已离开该模块的实体数。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Number of entities departed, d** 的框。

**数据类型：** `double`

### **port\_rem** — 模块中剩余的实体数（标量）

仍在模块中且尚未离开的实体数。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Number of entities remaining to depart, rem** 的框。

**数据类型：** `double`

### **port\_pe** — 模块中的待处理实体 off（默认）| on

选中此复选框时，对于模块中的待处理实体，输出值为 `1`；否则输出 `0`。

#### 依赖关系

要启用此端口，请选择 **Statistics** > **Pending entity in block, pe**。

**数据类型：** `double`

## 参数

### **Event actions** — 指定事件操作 `Entry`（默认）| `Unbatch` | `Exit` | `Blocked`

指定实体在特定事件发生时的行为。例如，当实体进入模块时，会调用 **Entry** 操作。要自定义实体进入、离开、解批或阻塞时的操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Unbatch action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关事件操作的详细信息，请参阅事件和事件操作。有关示例，请参阅使用事件操作管理实体。

#### 编程用法

|  |
| --- |
| **模块参数**：`EntryAction, UnbatchAction, ExitAction, BlockedAction` |
| **类型**：character vector |
| **值**：MATLAB 代码 |
| **默认值**：`''` |

### **Number of entities arrived, a** — 输出已到达模块的实体数 `off`（默认）| `on`

已到达该模块的实体数。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfEntitiesArrived` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities departed, d** — 输出已离开模块的实体数 `off`（默认）| `on`

选中此复选框会输出已离开该模块的实体数。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities remaining to depart, rem** — 输出模块中剩余待离开的实体数 `off`（默认）| `on`

输出仍在模块中且尚未离开的实体数。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfEntitiesWaitingToDepart` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Pending entity in block, pe** — 待处理实体 `off`（默认）| `on`

指示模块中是否存在尚未离开的实体。对于待处理实体，值为 `1`；否则为 `0`。

#### 编程用法

|  |
| --- |
| **模块参数**：`PendingEntity` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

SimEvents

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**R2016b 中引入**

## 描述

拆分批次实体

Entity Batch Splitter 模块将批次实体拆分为其各个实体，并通过输出端口输出每个实体。批次实体是 Entity Batch Creator 模块的输出。

要自定义实体进入、离开以及被阻塞或解批时的操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Blocked action` 或 `Unbatch action` 字段中输入 MATLAB® 代码。
