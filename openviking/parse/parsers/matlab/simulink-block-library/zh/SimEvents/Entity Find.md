---
type: simulink-block
title: 'Entity Find'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityfind'
documentation_source_path: 'ref/entityfind.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Find

## 端口

### 输入

### **Port\_1** — 用于触发查找实体的输入实体 标量 | 向量 | 矩阵

用于触发使用特定资源查找实体的事件的实体输入端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### 输出

### **Port\_1** — 输出找到的实体 标量 | 向量 | 矩阵

该模块找到的实体的输出实体端口。

#### 依赖项

要启用此端口，请选中 **提取找到的实体** 复选框。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_f** — 找到的实体数量 标量

该模块找到的实体数量。

#### 依赖项

要启用此端口，请点击 **统计** 选项卡，并选中标记为 **找到的实体数量, f** 的框。

**数据类型:** `double`

### **Port\_d** — 已离开该模块的实体数量 标量

已离开该模块的实体数量。

#### 依赖项

要启用此端口，请点击 **统计** 选项卡，并选中标记为 **已离开的实体数量, d** 的框。

**数据类型:** `double`

### **Port\_n** — 尚未离开该模块的找到的实体数量 标量

尚未离开该模块的找到的实体数量。

#### 依赖项

要启用此端口，请点击 **统计** 选项卡，并选中标记为 **模块中找到的实体数量, n** 的框。

**数据类型:** `double`

### **Port\_w** — 该模块中找到的实体的平均等待时间 标量

该模块中找到的实体的平均等待时间。

#### 依赖项

要启用此端口，请点击 **统计** 选项卡，并选中标记为 **平均等待时间, w** 的框。

**数据类型:** `double`

### **Port\_l** — 找到的实体队列的平均长度 标量

输出找到的实体队列的平均长度。

#### 依赖项

要启用此端口，请点击 **统计** 选项卡，并选中标记为 **平均队列长度, l** 的框。

**数据类型:** `double`

### **Port\_ex** — 提取的实体数量 标量

从该模块中提取的实体数量。

#### 依赖项

要启用此端口，请点击 **统计** 选项卡，并选中标记为 **提取的实体数量, ex** 的框。

**数据类型:** `double`

## 参数

### 主要

### **资源** — 指定实体使用的参考资源的名称 `Resource1`（默认） | character vector

该模块要查找的实体所使用的参考资源的名称。

#### 编程用法

|  |
| --- |
| **模块参数**: `ResourceName` |
| **类型**: character vector |
| **值**: 资源名称 |
| **默认值**: `'Resource1'` |

### **提取找到的实体** — 提取并重新路由找到的实体 `off`（默认） | `on`

提取并输出搜索中找到的实体。

#### 编程用法

|  |
| --- |
| **模块参数**: `EnableOutput` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **附加筛选条件** — 添加可选的筛选条件 `off`（默认） | `on`

启用为查找实体定义附加匹配条件的选项。如果选中，将出现一个 MATLAB 编辑器，您可以在其中定义附加匹配条件。

#### 编程用法

|  |
| --- |
| **模块参数**: `EntityFilter` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **匹配条件** — 定义匹配条件 `match = true;`（默认）

使用 MATLAB 代码为查找实体定义附加匹配条件。该模块搜索实体，使得布尔变量 `match` 的值变为 `true`。例如，当

```
match = isequal(trigger.Attribute1, entity.Attribute1);
```

时，该模块查找与触发实体具有相同 Attribute1 值的实体，因为只有它们的相等性会将 `match` 设置为 `true`。

在编写附加匹配条件时，可以使用以下变量。

- `trigger` — 用于访问触发实体的属性。
- `entity` — 用于访问正在被查找的实体的属性。
- `match` — 用作匹配条件返回的布尔值。`match` 的值初始化为 `false`。

#### 依赖项

如果在 **主要** 选项卡中选中了 **附加筛选条件** 复选框，则会出现此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `MatchingCondition` |
| **类型**: character vector |
| **值**: MATLAB 代码 |
| **默认值**: `'% match = isequal(trigger.Attribute1, entity.Attribute1);match = true;'` |

### 事件操作

### **事件操作** — 指定事件操作 `OnFound`（默认） | `Entry` | `Exit` | `Blocked`

指定实体在特定事件上的行为。例如，当实体进入模块时，会调用 **Entry** 操作。要自定义实体进入、离开、被找到或被阻止时的操作，请在 **事件操作** 选项卡的 `Entry action`、`Exit action`、`On found action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关事件操作的详细信息，请参阅事件和事件操作。有关示例，请参阅使用事件操作管理实体。

#### 依赖项

`On found action` 仅在未选中 **提取找到的实体** 复选框时出现。

`Entry action`、`Exit action` 和 `Blocked action` 仅在选中 **提取找到的实体** 复选框时出现。

#### 编程用法

|  |
| --- |
| **模块参数**: `EntryAction, ExitAction, BlockedAction` |
| **类型**: character vector |
| **值**: MATLAB 代码 |
| **默认值**: `''` |

### 统计

### **找到的实体数量, f** — 输出找到的实体数量 `off`（默认） | `on`

仿真期间该模块找到的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumberEntitiesDeparted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **已离开的实体数量, d** — 输出已离开该模块的实体数量 `off`（默认） | `on`

已离开该模块的实体数量。

#### 依赖项

如果在 **主要** 选项卡中选中了 **提取找到的实体** 复选框，则会出现此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumberEntitiesDeparted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **模块中找到的实体数量, n** — 输出尚未离开的找到的实体数量 `off`（默认） | `on`

尚未离开的找到的实体数量。

#### 依赖项

如果在 **主要** 选项卡中选中了 **提取找到的实体** 复选框，则会出现此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumberEntitiesInBlock` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **平均等待时间, w** — 输出平均等待时间 `off`（默认） | `on`

离开该模块的实体的等待时间总和除以它们的总数。*等待时间* 是实体进入和离开 Entity Find 模块之间的持续时间。有关详细信息，请参阅使用统计分析解释 SimEvents 模型。

#### 依赖项

如果在 **主要** 选项卡中选中了 **提取找到的实体** 复选框，则会出现此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `AverageWait` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **平均队列长度, l** — 输出实体队列的平均长度 `off`（默认） | `on`

累积的时间加权平均队列大小。该模块通过以下方式计算此值：

1. 将队列大小乘以其持续时间，以计算时间加权
   队列大小
2. 将所有时间加权队列大小相加，并对总时间
   求平均

有关详细信息，请参阅使用统计分析解释 SimEvents 模型。

#### 依赖项

如果在 **主要** 选项卡中选中了 **提取找到的实体** 复选框，则会出现此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `AverageStoreSize` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **提取的实体数量, ex** — 从此模块提取的实体数量 `off`（默认） | `on`

输出提取的实体数量。

#### 依赖项

如果在 **主要** 选项卡中选中了 **提取找到的实体** 复选框，则会出现此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumEntitiesExtracted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

## 所属库

SimEvents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

查找实体

Entity Find 模块查找使用特定资源的实体。该模块从其输入端口接收触发实体。收到触发实体后，它会启动对模型中所有模块的搜索，以查找具有特定资源的实体。您可以通过添加附加筛选条件来进一步筛选要查找的实体。该模块可以通过以下方式操作找到的实体。

- 搜索模型中跨模块满足特定条件的实体，以找到并检查它们。
- 从模型中提取找到的实体，而不修改它们。
- 在不提取的情况下，在模型中其所在位置更改找到的实体的属性。

  在这种情况下，要在找到实体时自定义操作，请在 **事件操作** 选项卡的 `On found action` 字段中输入 MATLAB® 代码。

- 提取并更改实体属性。提取的实体会在该模块中排队，并通过其输出端口重新路由。

  在这种情况下，要自定义实体进入、离开或被阻止时的操作，请在 **事件操作** 选项卡的 `Entry action`、`Exit action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关详细信息，请参阅为旧版模型编写事件操作。

该模块可以从 Entity Server、Entity Queue、Entity Store、Resource Acquirer、Entity Replicator、Conveyor System、Entity Selector、MATLAB Discrete-Event System 和 Discrete-Event Chart 模块中提取实体。

提取实体时，待处理事件和统计信息会相应更新。例如，如果在服务期间由 Entity Find 模块从 Entity Server 模块中提取实体，则剩余服务会被取消，并且统计信息的输出会更新。

**注意**

该模块只能查找您在模型中指定的一种实体类型，并且不能跨模型引用边界查找或提取实体。

有关涉及 Entity Find 模块的常见工作流的详细信息，请参阅在 SimEvents 模型中查找和提取实体。
