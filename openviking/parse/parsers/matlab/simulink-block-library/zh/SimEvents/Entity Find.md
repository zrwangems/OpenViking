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

用于触发使用特定资源查找实体事件的实体输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出的已找到实体 标量 | 向量 | 矩阵

该模块找到的实体的输出实体端口。

#### 依赖

要启用此端口，请选中 **Extract found entities** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_f** — 已找到的实体数量 标量

该模块找到的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities found, f** 的框。

**数据类型：** `double`

### **Port\_d** — 已离开该模块的实体数量 标量

已离开该模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities departed, d** 的框。

**数据类型：** `double`

### **Port\_n** — 尚未离开该模块的已找到实体数量 标量

尚未离开该模块的已找到实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of found entities in block, n** 的框。

**数据类型：** `double`

### **Port\_w** — 该模块中已找到实体的平均等待时间 标量

该模块中已找到实体的平均等待时间。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Average wait, w** 的框。

**数据类型：** `double`

### **Port\_l** — 已找到实体队列的平均长度 标量

输出已找到实体队列的平均长度。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Average queue length, l** 的框。

**数据类型：** `double`

### **Port\_ex** — 已提取的实体数量 标量

从该模块中提取的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities extracted, ex** 的框。

**数据类型：** `double`

## 参数

### 主要

### **Resource** — 指定实体使用的引用资源名称 `Resource1`（默认）| 字符向量

该模块要查找的实体所使用的引用资源名称。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ResourceName` |
| **类型**：字符向量 |
| **值**：资源名称 |
| **默认值**：`'Resource1'` |

### **Extract found entities** — 提取并重新路由已找到的实体 `off`（默认）| `on`

提取并输出在搜索中找到的实体。

#### 程序化使用

|  |
| --- |
| **模块参数**：`EnableOutput` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Additional filtering condition** — 添加可选的过滤条件 `off`（默认）| `on`

启用为查找实体定义额外匹配条件的选项。如果选中，将出现一个 MATLAB 编辑器，您可以在其中定义额外的匹配条件。

#### 程序化使用

|  |
| --- |
| **模块参数**：`EntityFilter` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Matching condition** — 定义匹配条件 `match = true;`（默认）

使用 MATLAB 代码定义用于查找实体的附加匹配条件。该模块搜索实体，使得布尔变量 `match` 的值变为 `true`。例如，当

```
match = isequal(trigger.Attribute1, entity.Attribute1);
```

时，该模块查找与触发实体具有相同 Attribute1 值的实体，因为只有它们的相等性会将 `match` 设置为 `true`。

在编写附加匹配条件时，您可以使用以下变量。

- `trigger` — 用于访问触发实体的属性。
- `entity` — 用于访问正在被查找的实体的属性。
- `match` — 用作匹配条件返回的布尔值。`match` 的值初始化为 `false`。

#### 依赖关系

如果 **Main** 选项卡中的 **Additional filtering condition** 复选框被选中，则此复选框出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`MatchingCondition` |
| **类型**：character vector |
| **值**：MATLAB code |
| **默认值**：`'% match = isequal(trigger.Attribute1, entity.Attribute1);match = true;'` |

### Event Actions

### **Event actions** — 指定事件动作 `OnFound`（默认）| `Entry` | `Exit` | `Blocked`

指定实体在特定事件下的行为。例如，当实体进入模块时会调用 **Entry** 动作。要自定义实体进入、退出、被找到或被阻塞时的动作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action`、`On found action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关事件动作的详细信息，请参阅 Events and Event Actions。有关示例，请参阅 Manage Entities Using Event Actions

#### 依赖关系

`On found action` 仅在 **Extract found entities** 复选框未被选中时出现。

`Entry action`、`Exit action` 和 `Blocked action` 仅在 **Extract found entities** 复选框被选中时出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntryAction, ExitAction, BlockedAction` |
| **类型**：character vector |
| **值**：MATLAB code |
| **默认值**：`''` |

### Statistics

### **Number of entities found, f** — 输出被找到的实体数量 `off`（默认）| `on`

仿真期间被该模块找到的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities departed, d** — 输出已离开该模块的实体数量 `off`（默认）| `on`

已离开该模块的实体数量。

#### 依赖关系

如果 **Main** 选项卡中的 **Extract found entities** 复选框被选中，则此复选框出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of found entities in block, n** — 输出模块中尚未离开的被找到实体数量 `off`（默认）| `on`

尚未离开的被找到实体数量。

#### 依赖关系

如果 **Main** 选项卡中的 **Extract found entities** 复选框被选中，则此复选框出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesInBlock` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Average wait, w** — 输出平均等待时间 `off`（默认）| `on`

离开该模块的实体的等待时间之和除以其总数。*等待时间* 是实体从 Entity Find 模块进入到退出的持续时间。有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 依赖关系

如果 **Main** 选项卡中的 **Extract found entities** 复选框被选中，则此复选框出现。

#### 编程用法

|  |
| --- |
| **模块参数**：`AverageWait` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **平均队列长度，l** — 输出实体队列的平均长度 `off`（默认）| `on`

累积的时间加权平均队列大小。该模块通过以下方式计算此值：

1. 将队列的大小乘以其持续时间，以计算时间加权队列大小
2. 将所有时间加权队列大小求和，并在总时间上取平均值

有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 依赖关系

如果 **Main** 选项卡中的 **Extract found entities** 复选框被选中，则此复选框会出现。

#### 编程用法

|  |
| --- |
| **模块参数**：`AverageStoreSize` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **提取的实体数量，ex** — 从此模块提取的实体数量 `off`（默认）| `on`

输出提取的实体数量。

#### 依赖关系

如果 **Main** 选项卡中的 **Extract found entities** 复选框被选中，则此复选框会出现。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumEntitiesExtracted` |
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

**在 R2018b 中引入**

## 描述

查找实体

Entity Find 模块查找使用特定资源的实体。该模块从其输入端口接收触发实体。在接收到触发实体后，它会启动对模型中所有模块的搜索，以查找具有特定资源的实体。您可以通过添加额外的过滤条件来进一步筛选要查找的实体。该模块可以通过以下方式操作找到的实体。

- 在模型中的各模块间搜索满足特定条件的实体，以查找并检查它们。
- 从模型中提取找到的实体而不修改它们。
- 在模型中实体所在位置更改找到的实体的属性而不进行提取。

  在这种情况下，要在找到实体时自定义操作，请在 **Event actions** 选项卡的 `On found action` 字段中输入 MATLAB® 代码。
- 提取并更改实体属性。提取的实体在模块中排队，并通过其输出端口重新路由。

  在这种情况下，要在实体进入、退出或被阻塞时自定义操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action` 或 `Blocked action` 字段中输入 MATLAB 代码。有关详细信息，请参阅 Write Event Actions for Legacy Models。

该模块可以从 Entity Server、Entity Queue、Entity Store、Resource Acquirer、Entity Replicator、Conveyor System、Entity Selector、MATLAB Discrete-Event System 和 Discrete-Event Chart 模块中提取实体。

当实体被提取时，待处理事件和统计信息会相应更新。例如，如果某个实体在服务期间被 Entity Find 模块从 Entity Server 模块中提取，则剩余的服务会被取消，并且统计信息的输出会更新。

**注意**

该模块只能查找您在模型中指定的一种实体类型，并且不能跨模型引用边界查找或提取实体。

有关涉及 Entity Find 模块的常见工作流的详细信息，请参阅 Find and Extract Entities in SimEvents Models。
