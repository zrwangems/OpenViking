---
type: simulink-block
title: 'Resource Acquirer'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'resourceacquirer'
documentation_source_path: 'ref/resourceacquirer.html'
language: zh-CN
chinese_source: worker-translation
---

# Resource Acquirer

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

离开模块的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Number of entities departed, d** 的复选框。

**数据类型：** `double`

### **Port\_n** — 尚未离开模块的实体数量 标量

尚未离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Number of entities in block, n** 的复选框。

**数据类型：** `double`

### **Port\_w** — 模块中实体的平均等待时间 标量

模块中实体的平均等待时间。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Average wait, w** 的复选框。

**数据类型：** `double`

### **Port\_ex** — 提取的实体数量 标量

从此模块中拉出的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Number of entities extracted, ex** 的复选框。

**数据类型：** `double`

## 参数

### **Maximum number of waiting entities** — 可以等待资源的实体最大数量 `1`（默认）| `scalar`

输入可以等待资源的实体最大数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberWaitingEntities` |
| **类型**：character vector |
| **值**：`'1'` | scalar |
| **默认值**：`'1'` |

### **Event actions** — 指定实体在特定事件下的行为 `Entry`（默认）| `Exit` | `Blocked`

在 **Event actions** 中定义行为。例如，当实体进入模块时，会调用 **Entry** 动作。

**注意**

如果事件动作更改了实体，相关的模块行为（例如重新排序优先级队列以及重新调度任何事件）将在事件动作完全结束并返回后发生。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntryAction, ExitAction, BlockedAction` |
| **类型**：character vector |
| **值**：MATLAB code |
| **默认值**：`''` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认）| `on`

选中此复选框将输出已离开模块的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities in block, n** — 输出模块中存在的、尚未离开的实体数量 `off`（默认）| `on`

选中此复选框将输出模块中存在的、尚未离开的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesInBlock` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Average wait, w** — 输出平均等待时间 `off`（默认）| `on`

离开模块的实体的等待时间之和除以其总数。*等待时间* 是实体进入和离开 Resource Acquirer 模块之间的持续时间。有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AverageWait` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities extracted, ex** — 从此模块提取的实体数量 `off`（默认）| `on`

输出由 Entity Find 模块从此模块中拉出的已提取实体数量。当实体被提取时，其从 Resource Pool 模块获取的资源将被取消，并且 **Number of entities departed, d**、**Number of entities in block, n** 和 **Average wait, w** 统计量会相应更新。有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models。

#### 程序化使用

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

**在 R2016a 中引入**

## 描述

获取实体资源

Resource Acquirer 模块为输入实体获取资源并将其分配给这些实体。您可以指定模块获取的资源数量和类型。

实体在获取所有请求的资源之前不会离开 Resource Acquirer 模块。例如，如果一个实体请求 `5` 个资源，而 Resource Pool 模块中有 `2` 个资源可用，则该实体会等待直到所有请求的资源都可用后才退出。类似地，如果一个实体从一个类型请求 `2` 个资源，从另一个类型请求 `3` 个资源，则该实体会等待直到两个类型的所有资源都可用。

使用指定数量的可用资源初始化 Resource Pool 模块。然后：

- 使用一个或多个 Resource Acquirer 模块来预留这些资源。

  Resource Acquirer 模块的优先级顺序在仿真开始时确定，无法自定义。较高优先级 Resource Acquirer 模块中的实体总是先获取资源。

  两个实体获取同一资源

  例如，假设 Resource Pool 模块中只有 `1` 个资源可用，且 Resource Acquirer1 的优先级高于 Resource Acquirer2。如果 Entity1 和 Entity2 同时想要获取该资源，Entity1 总是获取该资源。即使该资源再次变为可用，并且有两个实体 Entity1 和 Entity2 分别在 ResourceAcquirer1 和 ResourceAcquirer2 中等待，Entity1 仍会再次获取该资源。
- 使用 Resource Releaser 模块将资源返还给 Resource Pool 模块以供将来使用。

资源的可见性由模型中 Resource Pool 模块的 **Resource visibility** 参数决定。

要在实体进入、退出或被阻塞时自定义操作，请在 **Event actions** 选项卡的 `Entry action`、`Exit action` 或 `Blocked action` 字段中输入 MATLAB® 代码。

### 可用资源

使用**可用资源**控件可以：

- 从模型中所有资源池模块定义的资源中选择资源。
- 将资源添加到**已选资源**表中，在此可以配置资源获取详细信息。

该列表显示模型中的所有可用资源。（如果没有资源，则**可用属性**列表为空。）

如果资源列表很长，可以在文本框中键入资源名称以筛选列表。

使用**可用资源**区域中的按钮可帮助构建资源表。这些按钮执行以下操作。

| 按钮 | 操作 |
| --- | --- |
| 带有绿色圆形箭头符号的按钮 | 刷新**可用资源**列表。当模块对话框打开时，该列表会随您所做的任何上游模型更改而更新。 |
| 带有指向右侧的蓝色箭头的按钮 | 将所选资源添加到**已选资源**表。 |
| 带有指向左侧的蓝色箭头的按钮 | 将所选资源从**已选资源**表移动到**可用资源**列表。**注意** 如果所选资源是您手动添加的资源，则此按钮显示为灰显。 |

可用资源列表下方的消息区域会显示有关资源的其他适用消息。

| 消息 | 含义 |
| --- | --- |
| `> Resource already selected` | 您已将资源添加到**已选资源**表。无法再次将该资源添加到表中。 |

### Selected Resources

使用 **Selected Resources** 下的控件来构建和管理要附加到实体的资源列表。每个资源在表中显示为一行。

使用这些控件，您可以：

- 手动添加资源。
- 修改您从 **Available Resources** 列表添加到表中以附加到实体的资源。

**Selected Resources** 下的按钮执行以下操作：

| 按钮 | 操作 | 说明 |
| --- | --- | --- |
| 带绿色加号符号的按钮 | 向表中添加模板资源。 | 重命名资源并指定其属性。 |
| 带两个重叠的相同纸张符号的按钮 | 向表中添加所选资源的副本，用作新资源的基础。 | 重命名副本。两个资源不能具有相同的名称。 |
| 带红色叉号符号的按钮 | 从 **Selected Resources** 表中移除所选资源。 | 以这种方式删除资源时，不会出现确认提示，并且无法撤销该操作。 |
| 带指向上方的蓝色箭头的按钮 | 在 **Selected Resources** 表中按顺序上移所选资源。 | 不适用 |
| 带指向下方的蓝色箭头的按钮。 | 在 **Selected Resources** 表中按顺序下移所选资源。 | 不适用 |

**注意**

如果删除一行并应用更改，该删除可能会影响与其他属性对应的信号输出端口。例如，如果模块具有信号输出端口 **A2**，而您删除了带有标记为 **A1** 的端口的属性，则该模块会将 **A2** 重新标记为 **A1**。请验证连接到重新标记端口的任何信号是否仍按预期连接。

| 属性 | 指定 | 使用 |
| --- | --- | --- |
| **Name** | 资源的名称。每个资源必须具有唯一的名称。 | 双击现有名称，然后键入新名称。 |
| **Amount Source** | 实体请求的资源量是来自对话框还是来自属性。 | 选择 `Dialog` 或 `Attribute`。如果选择 `Attribute`，则资源量的来源来自实体的属性。此选项允许每个实体获取不同数量的资源。有关详细信息，请参阅 Set Resource Amount with Attributes。 |
| **Amount** | 要分配给资源的值（当资源来自对话框时）。 | 双击该值，然后键入要分配的值。此值是每个实体获取的资源数量。例如，如果 **Amount** 为 `3`，则到达 Resource Acquire 模块的每个实体必须等待获取 3 个资源，然后才能离开该模块。要获取的资源的粒度与 Resource Pool 模块中资源的粒度一致。 |
