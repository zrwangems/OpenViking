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

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

用于进入模块的实体的输入实体端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出批次实体 标量 | 向量 | 矩阵

用于离开模块的批次实体的输出实体端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_a** — 到达的实体数量 标量

已到达模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Number of entities arrived, a** 的框。

**数据类型:** `double`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Number of entities departed, d** 的框。

**数据类型:** `double`

### **Port\_rem** — 下一批剩余的实体数量 标量

为下一批剩余的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Number of entities remaining for the next batch, rem** 的框。

**数据类型:** `double`

### **Port\_pe** — 模块中的待处理实体 off（默认） | on

选中此复选框时，对于模块中的待处理实体输出 `1`，否则输出 `0`。

#### 依赖

要启用此端口，请选择 **Statistics** > **Pending entity in block, pe**。

**数据类型:** `double`

## 参数

### **Number of entities in batch** — 一个批次中的实体数量 `4`（默认） | scalar

指定一个批次中的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumberOfEntitiesInBatch` |
| **类型**: character vector |
| **值**: `'4'` | scalar |
| **默认**: `'4'` |

### **Entity type name** — 合并传入实体后创建的批实体名称 `Batch`（默认） | character vector

指定合并传入实体后创建的批实体名称。

#### 程序化使用

|  |
| --- |
| **模块参数**: `EntityTypeName` |
| **类型**: character vector |
| **值**: `'Batch'` | character vector |
| **默认**: `'Batch'` |

### **Bus object** — 指定是否将批实体输出为 bus object off（默认） | on

指定是否将批实体输出为 bus object。

#### 程序化使用

|  |
| --- |
| **模块参数**: `BusObject` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **Input entity name** — 指定要附加到输入实体的名称 `batch`（默认） | character vector

指定要附加到输入实体的名称，这些名称可用于在批实体中引用这些实体。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InputEntityName` |
| **类型**: character vector |
| **值**: `'batch'` | character vector |
| **默认**: `'batch'` |

### **Event actions** — 指定事件操作 `Entry`（默认） | `Batch generate` | `Exit` | `Blocked`

指定实体在特定事件发生时的行为。例如，当实体进入模块时调用 **Entry** 操作。要在实体进入、退出、批处理或阻塞时自定义操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Batch generate action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关事件操作的详细信息，请参阅 Events and Event Actions。有关示例，请参阅 Manage Entities Using Event Actions

#### 程序化使用

|  |
| --- |
| **模块参数**: `EntryAction, BatchGenerateAction, ExitAction, BlockedAction` |
| **类型**: character vector |
| **值**: MATLAB code |
| **默认**: `''` |

### **Number of entities arrived, a** — 输出已到达模块的实体数量 `off`（默认） | `on`

已到达模块的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumberOfEntitiesArrived` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认） | `on`

已离开模块的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumberOfEntitiesDeparted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **Number of entities remaining for next batch, rem** — 输出下一批剩余的实体数量 `off`（默认） | `on`

输出模块中仍为下一批实体保留的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumberOfEntitiesRequiredForNextBatch` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **Pending entity in block, pe** — 待处理实体 `off`（默认） | `on`

指示模块中是否存在尚未离开的实体。对于待处理实体，该值为 `1`，否则为 `0`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PendingEntity` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2016b 中引入**

## 描述

创建实体批次

Entity Batch Creator 接收预期数量的实体，并创建一个包含所有这些实体的批实体。批实体是实体的数组。在批处理输入实体之前，必须使用 Resource Releaser 模块释放任何已获取的资源。

要在实体进入、退出、批处理或阻塞时自定义操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`Batch generate action` 或 `Blocked action` 字段中输入 MATLAB® 代码。有关事件操作的详细信息，请参阅 Events and Event Actions。

您可以编写 MATLAB 代码来操作批实体的属性。例如，要在生成实体批次后访问属性，请选择 `Batch generate action` 并使用以下代码。

```
entity.batch
```

如果批次中的实体数量为 `4`，则 `entity.batch` 是一个 `4`×`1` 结构体数组。要操作批次中第三个实体的 `Attribute1`，请输入以下代码。

```
entity.batch(3).Attribute1
```

您可以在事件操作中引用批实体属性。但不能在以下情况中引用它们：

- 优先队列 — 不要将 **Priority source** 参数设置为 `PriorityAttribute`。
- Entity Server 模块 — 不要将 **Service time source** 参数设置为 `Attribute`。
- Output Switch 模块 — 不要将 **Switching criterion** 参数设置为 `From attribute`。

要将批次输出为 bus object，请选择 **Bus object** 参数。在以下情况中，考虑为批实体创建 bus object：

- 向 MATLAB Discrete-Event System 模块发送批实体或从该模块接收批实体时。
- 向 Discrete-Event Chart 模块发送批实体或从该模块接收批实体时。
- 将完整实体数据传递给 Simulink Function 模块时。
- 使用 Message Receive 模块将批实体转换为信号时。
