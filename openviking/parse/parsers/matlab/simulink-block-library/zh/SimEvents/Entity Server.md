---
type: simulink-block
title: 'Entity Server'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityserver'
documentation_source_path: 'ref/entityserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Server

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

携带标量、总线或向量数据进入服务器的输入实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **Port\_2** — 服务时间源的输入信号端口 标量

用于确定服务时间的输入信号端口。

#### 依赖关系

当 **Service time source** 设置为 `Signal port` 时，此端口可见。

**数据类型：** `double`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

离开服务器的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Number of entities departed, d** 的框。

**数据类型：** `double`

### **Port\_n** — 尚未离开模块的实体数量 标量

尚未离开模块的实体数量。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Number of entities in block, n** 的框。

**数据类型：** `double`

### **Port\_pe** — 模块中的待处理实体 off（默认）| on

选中此复选框时，对于模块中的待处理实体输出值 `1`，否则输出 `0`。

#### 依赖关系

要启用此端口，请选择 **Statistics** > **Pending entity in block, pe**。

**数据类型：** `double`

### **Port\_np** — 待处理实体数量 off（默认）| on

选中此复选框时，输出模块中待处理实体的数量。

#### 依赖关系

要启用此端口，请选择 **Statistics** > **Number of pending entities, np**。

**数据类型：** `double`

### **Port\_w** — 模块中实体的平均等待时间 标量

模块中实体的平均等待时间。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Average wait, w** 的框。

**数据类型：** `double`

### **Port\_util** — 输出服务器被占用的平均时间 标量

服务器被占用的平均时间。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Utilization, util** 的框。

**数据类型：** `double`

### **Port\_p** — 输出被抢占的实体数量 标量

被抢占的实体数量。

#### 依赖关系

要启用此端口，请先单击 **Preemption** 选项卡，然后单击 **Statistics** 选项卡，并选中标记为 **Number of entities preempted, p** 的框。

**数据类型：** `double`

### **Port\_ex** — 被提取的实体数量 标量

从此模块中被拉出的实体数量。

#### 依赖关系

要启用此端口，请单击 **Statistics** 选项卡，然后选中标记为 **Number of entities extracted, ex** 的框。

**数据类型：** `double`

## 参数

### **Capacity** — 指定服务器的容量 `1`（默认）| 标量

指定模块可以同时服务的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Capacity` |
| **类型**：字符向量 |
| **值**：`'1'`| 标量 |
| **默认值**：`'1'` |

### **Service time source** — 选择用于指定服务时间的来源 `Dialog`（默认）| `Signal port` | `Attribute` | `MATLAB action`

确定用于指定服务时间的来源。

您可以选择：

- `Dialog`

  在 **Service time value** 参数中输入常量值。
- `Signal port`

  将时间源连接到生成的信号端口。
- `Attribute`

  输入包含要解释为服务时间的数据的属性名称。
- `MATLAB action`

  在 **Service time action** 部分中，输入 MATLAB 代码以更改服务时间。为变量 *dt* 赋值，模型将其用作服务时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`ServiceTimeSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Signal port'` | `'Attribute'`| `'MATLAB action'` |
| **默认值**：`'Dialog'` |

### **Service time attribute name** — 指定服务时间来源属性名称 `ServiceTime`（默认）| character vector

确定用作服务时间值的属性名称。

#### 依赖关系

当 **Service time source** 设置为 `Attribute` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`ServiceTimeAttributeName` |
| **类型**：character vector |
| **值**：`'ServiceTime'` | character vector |
| **默认值**：`'ServiceTime'` |

### **Service time value** — 指定服务时间的值 `1`（默认）| scalar

**Tunable:** Yes

#### 依赖关系

当 **Service time source** 设置为 `Dialog` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`ServiceTimeValue` |
| **类型**：character vector |
| **值**：`'1.0'` | scalar |
| **默认值**：`'1.0'` |

### **Service time action** — 指定服务时间 `dt = rand(1,1)`（默认）| MATLAB code

使用 MATLAB 代码指定服务时间。`dt` 指定服务时间。您可以手动指定 `dt`，或使用 **Insert pattern** 按钮从重复序列或分布中指定服务时间。有关示例，请参阅 Count Simultaneous Departures from a Server。

#### 依赖关系

当 **Service time source** 设置为 `MATLAB action` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`ServiceTimeAction` |
| **类型**：character vector |
| **值**：MATLAB code |
| **默认值**：`'dt = rand(1,1);'` |

### **Event action** — 指定实体在特定事件中的行为 `Entry`（默认）| `Service complete` | `Exit` | `Blocked` | `Preempt`

指定实体在特定事件中的行为。在 **Event action** 参数中定义行为。**Entry** 和 **Exit** 动作分别在实体进入之后和实体退出之前被调用。**Service complete** 动作在实体服务完成后被调用。**Blocked** 动作在实体被阻塞后被调用。**Preempt** 在抢占后被调用。

**Note**

如果事件动作更改了实体，相关模块行为（例如重新排序优先级队列以及重新调度任何事件）将在事件动作完全结束并返回后发生。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntryAction, ServiceCompleteAction, ExitAction, BlockedAction, PreemptAction` |
| **类型**：character vector |
| **值**：MATLAB code |
| **默认值**：`''` |

### **Permit preemption based on attribute** — 启用实体抢占 `off`（默认）| `on`

如果您希望允许实体抢占，请选中此复选框。
抢占是指服务器模块中的实体被满足特定条件的实体替换。
选中此复选框将启用以下参数：

- **Preemption** 选项卡中的 **Sorting attribute name**
- **Preemption** 选项卡中的 **Sorting direction**
- **Preemption** 选项卡中的 **Write residual time to attribute**
- **Statistics** 选项卡中的 **Number of entities preempted, p**

有关示例，请参阅 Task Preemption in a Multitasking Processor。

#### 编程使用

|  |
| --- |
| **模块参数**：`PermitPreemptionBasedOnAttribute` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Sorting attribute name** — 指定用于确定优先级的属性名称 `entity` | `entitySys.priority` | character vector

指定用于确定优先级的属性名称。

#### 依赖关系

当选中 **Permit preemption based on attribute** 复选框时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`SortingAttributeName` |
| **类型**：character vector |
| **值**：`'entity'` | `'entitySys.priority'` | character vector |
| **默认值**：`'entity'` |

### **Sorting direction** — 选择实体排序的方向 `Ascending`（默认）| `Descending`

指定实体按 `ascending` 还是 `descending` 顺序排序。

- `ascending` — 对具有较小键值的实体进行排序，使其具有较高优先级
- `descending` — 对具有较大键值的实体进行排序，使其具有较高优先级

#### 依赖关系

当选中 **Permit preemption based on attribute** 复选框时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`SortingDirection` |
| **类型**：character vector |
| **值**：`'Ascending'` | `'Descending'` |
| **默认值**：`'Ascending'` |

### **Write residual time to attribute** — 将被抢占实体的剩余服务时间保存到属性 `off`（默认）| `on`

#### 依赖关系

当选中 **Permit preemption based on attribute** 复选框时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`WriteResidualTimeToAttribute` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Residual time attribute name** — 指定用于包含被抢占实体剩余服务时间的属性名称 `ResidualTime`（默认）| character vector

#### 依赖关系

当选中 **Write residual time to attribute** 复选框时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`ResidualTimeAttributeName` |
| **类型**：character vector |
| **值**：`'ResidualTime'` | character vector |
| **默认值**：`'ResidualTime'` |

### **Number of entities departed, d** — 输出已离开该模块的实体数量 `off`（默认）| `on`

已离开该模块的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities in block, n** — 输出该模块中当前存在但尚未离开的实体数量 `off`（默认）| `on`

该模块中当前存在但尚未离开的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesInBlock` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Pending entity in block, pe** — 待处理实体 `off`（默认）| `on`

指示该模块中是否存在尚未离开的实体。
对于待处理实体，该值为 `1`，否则为 `0`。

#### 编程用法

|  |
| --- |
| **模块参数**：`PendingEntityPresentInBlock` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **待处理实体数，np** — 待处理实体数 `off`（默认）| `on`

输出该模块已服务但尚未离开的待处理实体数。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberEntitiesPending` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **平均等待时间，w** — 输出平均等待时间 `off`（默认）| `on`

离开该模块的实体的等待时间之和除以其总数。*等待时间*是实体进入和离开 Entity Server 模块之间的持续时间。有关详细信息，请参阅 Interpret SimEvents Models Using Statistical Analysis。

#### 编程用法

|  |
| --- |
| **模块参数**：`AverageWait` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **利用率，util** — 输出服务器被占用的平均时间 `off`（默认）| `on`

服务器被占用的平均时间。该模块将此时间计算为实体的总等待时间与服务器容量之比乘以总仿真时间。

等待时间是实体进入和离开 Entity Server 模块之间的持续时间。总等待时间是离开该模块的实体的等待时间之和。

#### 编程用法

|  |
| --- |
| **模块参数**：`Utilization` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **被抢占实体数，p** — 输出被抢占的实体数 `off`（默认）| `on`

输出被抢占的实体数。抢占是指服务器模块中的实体被满足特定条件的实体替换。

#### 依赖项

如果选中 **Permit preemption based on attribute** 复选框，则显示此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumberEntitiesPreempted` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **被提取实体数，ex** — 从该模块提取的实体数 `off`（默认）| `on`

输出由 Entity Find 模块从该模块中拉出的被提取实体数。如果在提取期间某个实体正在被服务，则该服务被终止。如果某个属性定义了服务时间且该属性被 Entity Find 模块修改，则服务时间不变。当实体被提取时，**Number of entities departed, d**、**Number of entities in block, n**、**Average wait, w** 和 **Utilization, util** 统计量会相应更新。有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models。

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

**在 R2016a 中引入**

## 描述

为实体提供服务

Entity Server 模块在实体到达时为其提供服务。在离散事件仿真中，服务器将实体存储一段时间，称为*服务时间*，然后尝试输出该实体。在服务期间，该模块被称为正在*服务*其存储的实体。该模块可以同时服务多个实体，并通过输出端口输出每个实体，除非该端口被阻塞。当模块允许抢占时，服务器中的实体可以通过第二个端口提前离开。

要自定义实体进入、完成服务、退出以及被模块阻塞或抢占时的操作，请在**事件操作**选项卡的 `Entry action`、`Service complete action`、`Exit action`、`Blocked action` 或 `Preempt action` 字段中输入 MATLAB® 代码。有关详细信息，请参阅事件和事件操作。
