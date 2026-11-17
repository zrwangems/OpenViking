---
type: simulink-block
title: 'Entity Server'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'SimEvents'
documentation_page: 'entityserver'
documentation_source_path: 'ref/entityserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Server

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

输入实体，其携带标量、bus 或向量数据以进入服务器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **Port\_2** — 用于服务时间源的输入信号端口 标量

用于确定服务时间的输入信号端口。

#### 依赖关系

当 **服务时间源** 设置为 `Signal port` 时，此端口可见。

**数据类型：** `double`

### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

用于离开服务器的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **Port\_d** — 已离开该模块的实体数 标量

已离开该模块的实体数。

#### 依赖关系

要启用此端口，请单击 **统计** 选项卡，然后选中标有 **离开的实体数, d** 的复选框。

**数据类型：** `double`

### **Port\_n** — 尚未离开该模块的实体数 标量

尚未离开该模块的实体数。

#### 依赖关系

要启用此端口，请单击 **统计** 选项卡，然后选中标有 **模块中的实体数, n** 的复选框。

**数据类型：** `double`

### **Port\_pe** — 模块中的待处理实体 off（默认） | on

选中此复选框时，如果模块中存在待处理实体，则输出值 `1`，否则输出 `0`。

#### 依赖关系

要启用此端口，请选择 **统计** > **模块中的待处理实体, pe**。

**数据类型：** `double`

### **Port\_np** — 待处理实体数 off（默认） | on

选中此复选框时，输出模块中待处理实体的数量。

#### 依赖关系

要启用此端口，请选择 **统计** > **待处理实体数, np**。

**数据类型：** `double`

### **Port\_w** — 模块中实体的平均等待时间 标量

模块中实体的平均等待时间。

#### 依赖关系

要启用此端口，请单击 **统计** 选项卡，然后选中标有 **平均等待时间, w** 的复选框。

**数据类型：** `double`

### **Port\_util** — 输出服务器被占用的平均时间 标量

服务器被占用的平均时间。

#### 依赖关系

要启用此端口，请单击 **统计** 选项卡，然后选中标有 **利用率, util** 的复选框。

**数据类型：** `double`

### **Port\_p** — 输出被抢占的实体数 标量

被抢占的实体数。

#### 依赖关系

要启用此端口，请先单击 **抢占** 选项卡，然后单击 **统计** 选项卡，并选中标有 **被抢占的实体数, p** 的复选框。

**数据类型：** `double`

### **Port\_ex** — 提取的实体数 标量

从该模块中拉出的实体数。

#### 依赖关系

要启用此端口，请单击 **统计** 选项卡，然后选中标有 **提取的实体数, ex** 的复选框。

**数据类型：** `double`

## 参数

### **容量** — 指定服务器的容量 `1`（默认） | 标量

指定该模块可以同时服务的实体数。

#### 编程用法

|  |
| --- |
| **模块参数**: `Capacity` |
| **类型**: character vector |
| **值**: `'1'` | 标量 |
| **默认值**: `'1'` |

### **服务时间源** — 选择用于指定服务时间的源 `Dialog`（默认） | `Signal port` | `Attribute` | `MATLAB action`

确定用于指定服务时间的源。

可以选择：

- `Dialog`

  在 **服务时间值** 参数中输入常量值。

- `Signal port`

  将时间源连接到生成的信号端口。

- `Attribute`

  输入包含要解释为服务时间的数据的属性名称。

- `MATLAB action`

  在 **服务时间操作** 部分中，输入 MATLAB 代码以更改服务时间。为变量 *dt* 赋值，模型将其用作服务时间。

#### 编程用法

|  |
| --- |
| **模块参数**: `ServiceTimeSource` |
| **类型**: character vector |
| **值**: `'Dialog'` | `'Signal port'` | `'Attribute'` | `'MATLAB action'` |
| **默认值**: `'Dialog'` |

### **服务时间属性名称** — 指定服务时间源属性名称 `ServiceTime`（默认） | character vector

确定用作服务时间值的属性名称。

#### 依赖关系

当 **服务时间源** 设置为 `Attribute` 时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `ServiceTimeAttributeName` |
| **类型**: character vector |
| **值**: `'ServiceTime'` | character vector |
| **默认值**: `'ServiceTime'` |

### **服务时间值** — 指定服务时间的值 `1`（默认） | 标量

**可调：** 是

#### 依赖关系

当 **服务时间源** 设置为 `Dialog` 时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `ServiceTimeValue` |
| **类型**: character vector |
| **值**: `'1.0'` | 标量 |
| **默认值**: `'1.0'` |

### **服务时间操作** — 指定服务时间 `dt = rand(1,1)`（默认） | MATLAB code

使用 MATLAB 代码指定服务时间。`dt` 指定服务时间。您可以手动指定 `dt`，或使用 **插入模式** 按钮从重复序列或分布中指定服务时间。有关示例，请参阅统计服务器同时离开的实体数。

#### 依赖关系

当 **服务时间源** 设置为 `MATLAB action` 时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `ServiceTimeAction` |
| **类型**: character vector |
| **值**: MATLAB code |
| **默认值**: `'dt = rand(1,1);'` |

### **事件操作** — 指定实体在某些事件中的行为 `Entry`（默认） | `Service complete` | `Exit` | `Blocked` | `Preempt`

指定实体在某些事件中的行为。在 **事件操作** 参数中定义行为。**Entry** 和 **Exit** 操作分别在实体进入后和实体离开前调用。**Service complete** 操作在实体服务完成后调用。**Blocked** 操作在实体被阻塞后调用。**Preempt** 在抢占后调用。

**注意**

如果事件操作更改了实体，则相关模块行为（例如重新排列优先级队列以及对任何事件重新调度）将在事件操作完全结束并返回后发生。

#### 编程用法

|  |
| --- |
| **模块参数**: `EntryAction, ServiceCompleteAction, ExitAction, BlockedAction, PreemptAction` |
| **类型**: character vector |
| **值**: MATLAB code |
| **默认值**: `''` |

### **允许基于属性抢占** — 启用实体抢占 `off`（默认） | `on`

如果要允许实体抢占，请选中此复选框。抢占是指用满足特定条件的实体替换服务器模块中的实体。选中此复选框会启用以下参数：

- **抢占** 选项卡中的 **排序属性名称**
- **抢占** 选项卡中的 **排序方向**
- **抢占** 选项卡中的 **将剩余时间写入属性**
- **统计** 选项卡中的 **被抢占的实体数, p**

有关示例，请参阅多任务处理器中的任务抢占。

#### 编程用法

|  |
| --- |
| **模块参数**: `PermitPreemptionBasedOnAttribute` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **排序属性名称** — 指定用于确定优先级的属性名称 `entity` | `entitySys.priority` | character vector

指定用于确定优先级的属性名称。

#### 依赖关系

当选中 **允许基于属性抢占** 复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `SortingAttributeName` |
| **类型**: character vector |
| **值**: `'entity'` | `'entitySys.priority'` | character vector |
| **默认值**: `'entity'` |

### **排序方向** — 选择实体的排序方向 `Ascending`（默认） | `Descending`

指定实体是按 `ascending` 还是 `descending` 顺序排序。

- `ascending` — 将键值较小的实体排序为具有更高优先级
- `descending` — 将键值较大的实体排序为具有更高优先级

#### 依赖关系

当选中 **允许基于属性抢占** 复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `SortingDirection` |
| **类型**: character vector |
| **值**: `'Ascending'` | `'Descending'` |
| **默认值**: `'Ascending'` |

### **将剩余时间写入属性** — 将抢占实体的剩余服务时间保存到属性 `off`（默认） | `on`

#### 依赖关系

当选中 **允许基于属性抢占** 复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `WriteResidualTimeToAttribute` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **剩余时间属性名称** — 指定用于包含被抢占实体的剩余服务时间的属性名称 `ResidualTime`（默认） | character vector

#### 依赖关系

当选中 **将剩余时间写入属性** 复选框时，此参数可见。

#### 编程用法

|  |
| --- |
| **模块参数**: `ResidualTimeAttributeName` |
| **类型**: character vector |
| **值**: `'ResidualTime'` | character vector |
| **默认值**: `'ResidualTime'` |

### **离开的实体数, d** — 输出已离开该模块的实体数 `off`（默认） | `on`

已离开该模块的实体数。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumberEntitiesDeparted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **模块中的实体数, n** — 输出模块中存在的、尚未离开的实体数 `off`（默认） | `on`

模块中存在的、尚未离开的实体数。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumberEntitiesInBlock` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **模块中的待处理实体, pe** — 待处理实体 `off`（默认） | `on`

指示模块中是否存在尚未离开的实体。对于待处理实体，该值为 `1`，否则为 `0`。

#### 编程用法

|  |
| --- |
| **模块参数**: `PendingEntityPresentInBlock` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **待处理实体数, np** — 待处理实体数 `off`（默认） | `on`

输出该模块已服务但尚未离开的待处理实体数。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumberEntitiesPending` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **平均等待时间, w** — 输出平均等待时间 `off`（默认） | `on`

已离开该模块的实体的等待时间总和除以其总数。*等待时间* 是实体进入和离开 Entity Server 模块之间的持续时间。有关详细信息，请参阅使用统计分析解释 SimEvents 模型。

#### 编程用法

|  |
| --- |
| **模块参数**: `AverageWait` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **利用率, util** — 输出服务器被占用的平均时间 `off`（默认） | `on`

服务器被占用的平均时间。该模块将此时间计算为实体的总等待时间与服务器容量乘以总仿真时间之比。

等待时间是实体进入和离开 Entity Server 模块之间的持续时间。总等待时间是已离开该模块的实体的等待时间之和。

#### 编程用法

|  |
| --- |
| **模块参数**: `Utilization` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **被抢占的实体数, p** — 输出被抢占的实体数 `off`（默认） | `on`

输出被抢占的实体数。抢占是指用满足特定条件的实体替换服务器模块中的实体。

#### 依赖关系

如果选中 **允许基于属性抢占** 复选框，则会出现此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `NumberEntitiesPreempted` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **提取的实体数, ex** — 从该模块提取的实体数 `off`（默认） | `on`

输出由 Entity Find 模块从该模块中拉出的提取实体数。如果在提取期间正在服务某个实体，则服务终止。如果定义服务时间的属性被 Entity Find 模块修改，则服务时间不变。提取实体时，**离开的实体数, d**、**模块中的实体数, n**、**平均等待时间, w** 和 **利用率, util** 统计信息会相应更新。有关查找和提取实体的详细信息，请参阅在 SimEvents 模型中查找和提取实体。

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

**在 R2016a 中引入**

## 描述

为实体提供服务

Entity Server 模块在实体到达时为其提供服务。在离散事件仿真中，服务器将实体存储一段时间，这段时间称为 *服务时间*，然后尝试输出该实体。在服务期间，称该模块正在 *服务* 它存储的实体。该模块可以同时服务多个实体，并通过输出端口输出每个实体，除非该端口被阻塞。当该模块允许抢占时，服务器中的实体可以通过第二个端口提前离开。

要自定义实体进入、完成服务、离开以及被该模块阻塞或抢占时的操作，请在 **事件操作** 选项卡的 `Entry action`、`Service complete action`、`Exit action`、`Blocked action` 或 `Preempt action` 字段中输入 MATLAB® 代码。有关详细信息，请参阅事件和事件操作。
