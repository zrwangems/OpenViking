---
type: simulink-block
title: 'Entity Generator'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitygenerator'
documentation_source_path: 'ref/entitygenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Generator

## 端口

### 输入

### **Port\_1** — 在事件到达时触发实体生成的输入 标量 | 向量 | 矩阵

#### 依赖

要启用此端口，请点击 **Entity generation** 选项卡，并为 **Generation method** 选择 `Event-based`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — 用于确定下一次实体生成的代际时间值的信号输入 标量 | 向量 | 矩阵

#### 依赖

要启用此端口，请点击 **Entity generation** 选项卡，为 **Generation method** 选择 `Time-based`，并为 **Time source** 选择 `Signal port`。

**数据类型：** `double`
### 输出

### **Port\_1** — 输出的已生成实体 标量 | 向量 | 矩阵

离开生成器的已生成实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，并选中标记为 **Number of entities departed, d** 的复选框。

**数据类型：** `double`

### **Port\_pe** — 模块中的待处理实体 关（默认） | 开

对于待处理实体输出 `1`，否则输出 `0`。

#### 依赖

要启用此端口，请选择 **Statistics** > **Pending entity in block, pe**。

**数据类型：** `double`

### **Port\_w** — 平均代际时间 关（默认） | 开

输出实体生成之间的平均时间。

#### 依赖

要启用此端口，请选择 **Statistics** > **Average intergeneration time, w**。

**数据类型：** `double`

## 参数

### **Generation method** — 选择实体生成的方法 `Time-based`（默认） | `Event-based`

选择实体生成方法。选择 `Time-based` 以使用来自输入信号或统计分布的代际时间来生成实体。选择 `Event-based` 以由外部事件确定实体代际时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`GenerationMethod` |
| **类型**：字符向量 |
| **值**：`'Time-based'` | `'Event-based'` |
| **默认值**：`'Time-based'` |

### **Time source** — 选择代际时间的来源 `Dialog`（默认） | `Signal port` | `MATLAB action`

指定实体代际时间的来源。

- 选择 `Dialog` 以指定实体生成之间的固定周期。
- 选择 `Signal port` 以基于输入信号生成实体。
- 选择 `MATLAB action` 以定义由 `dt` 表示的代际时间的 MATLAB 脚本。

有关为实体指定代际时间的详细信息，请参阅 Specify Intergeneration Times for Entities。

#### 依赖

当 **Generation method** 设置为 `Time-based` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：字符向量 |
| **值**：`'Dialog'` | `'Signal port'` | `'MATLAB action'` |
| **默认值**：`'Dialog'` |

### **Period** — 定义实体生成之间的周期 `1`（默认） | 标量

指定实体代际之间的时间。例如，如果 **Period** 为 `1`，则模块在实体生成之间等待 `1` 个仿真时间。有关详细信息，请参阅 Specify Intergeneration Times for Entities。

**可调：** 是

#### 依赖

当 **Generation method** 设置为 `Time-based` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`Period` |
| **类型**：字符向量 |
| **值**：`'1'` | 标量 |
| **默认值**：`'1'` |

### **Intergeneration time action** — 指定实体生成之间的时间 `dt = rand(1,1)`（默认）| MATLAB 代码

使用 MATLAB 代码指定服务时间。`dt` 指定实体生成之间的时间。您可以手动指定 `dt`，或使用 **Insert pattern** 按钮以重复序列或从分布生成实体。该模块每次准备好生成实体时都会使用此参数。有关示例，请参阅 Specify Intergeneration Times for Entities。

#### 依赖关系

当 **Service time source** 设置为 `MATLAB action` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntergenerationTimeAction` |
| **类型**：字符向量 |
| **值**：MATLAB 代码 |
| **默认值**：`'dt = rand(1,1);'` |

### **Generate entity at simulation start** — 在仿真开始时生成实体 `on`（默认）| `off`

在仿真开始时生成实体。

#### 编程使用

|  |
| --- |
| **模块参数**：`GenerateEntityAtSimulationStart` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Entity type** — 选择要生成的实体类型 `Structured`（默认）| `Anonymous` | `Bus object`

选择要生成的实体类型。

- `Anonymous` 类型有一个与之关联的数据值。
- `Structured` 类型（默认）包含您可以指定的名称和初始值属性。

  - 您可以通过点击绿色加号符号将多个属性附加到一个实体。
  - 您可以通过点击红色叉号符号删除属性。
  - 您可以通过点击蓝色向上箭头和蓝色向下箭头更改属性的顺序。
  - 您可以通过点击 File symbol with two smaller symbols atop: a green down arrow on the top left, and a group of three parallel black lines on the bottom right，将 `Structured` 类型实体转换为总线对象。
- `Bus object` 类型允许您生成总线对象作为实体。

  要打开 Type Editor 以生成总线对象，请点击 **Open Type Editor**。总线对象可以是另一个总线对象的元素，这可用于在附加到实体的数据中创建层次结构。

有关详细信息，请参阅 Entities in a SimEvents Model。

#### 限制

对于 `Structured` 实体类型，您可以从 Block Parameters 对话框中最多创建 31 个属性。要创建超过 31 个属性，请对 `EntityType` 模块参数使用 `set_param` 函数。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntityType` |
| **类型**：字符向量 |
| **值**：`'Structured'` | `'Anonymous'` | `'Bus object'` |
| **默认值**：`'Structured'` |

### **Entity priority** — 指定所生成实体的优先级 `300`（默认）| 标量

确定所生成实体的优先级。值越低优先级越高。有关详细信息，请参阅 Working with Entity Attributes and Entity Priorities。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntityPriority` |
| **类型**：字符向量 |
| **值**：`'300'` | 标量 |
| **默认值**：`'300'` |

### **Entity type name** — 指定所生成实体的名称 `Entity`（默认）| 字符向量

确定所生成实体的名称。

#### 依赖关系

当 **Entity type** 设置为 `Bus object` 或 `Structured` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntityTypeName` |
| **类型**：字符向量 |
| **值**：`'Entity'` | 字符向量 |
| **默认值**：`'Entity'` |

### **Data initial value** — 指定匿名实体数据的初始值 `0`（默认）| 标量 | 向量 | 矩阵

设置匿名实体数据初始值。此值不能为 int64 或定点类型。

#### 依赖关系

当您将 **Entity type** 设置为 `Anonymous` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`DataInitialValue` |
| **类型**：字符向量 |
| **值**：`'0'` | 标量 | 向量 | 矩阵 |
| **默认值**：`'0'` |

### **Attribute Name** — 定义所生成实体属性的名称 `Attribute1`（默认）| 字符向量

定义实体属性名称。

**注意**

完成后，可以将结构化实体类型导出为总线对象，名称为 **Entity type name**，导出到基础工作区。在使用 MATLAB Discrete-Event System 和 Discrete Event Chart 模块时导出该总线对象。

#### 依赖项

当 **Entity type** 设置为 `Structured` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AttributeName` |
| **类型**：字符向量 |
| **值**：`'Attribute1'` | 字符向量 |
| **默认值**：`'Attribute1'` |

### **Attribute Initial Value** — 定义所生成实体属性的初始值 `1`（默认）| 标量

指定实体属性初始值。当 **Entity type** 设置为 `Structured` 时，此参数可见。此值不能为定点类型。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AttributeInitialValue` |
| **类型**：字符向量 |
| **值**：`1` | 标量 |
| **默认值**：`'1'` |

### **Event actions** — 指定实体在特定事件下的行为 `Generate`（默认）| `Exit`

在 **Event action** 参数中定义行为。`Generate` 动作在生成实体时调用，`Exit` 动作在实体即将离开模块之前调用。

#### 程序化使用

|  |
| --- |
| **模块参数**：`GenerateAction, ExitAction` |
| **类型**：字符向量 |
| **值**：MATLAB 代码 |
| **默认值**：`''` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认）| `on`

已离开模块的实体数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Pending entity present in block, pe** — 待处理实体 `off`（默认）| `on`

指示模块中是否存在尚未离开的实体。对于待处理实体，该值为 `1`，否则为 `0`。此模块最多只能有一个待处理实体，因为其存储容量为一。如果存在待处理实体，则模块不会生成另一个实体，直到该待处理实体离开模块。

#### 程序化使用

|  |
| --- |
| **模块参数**：`PendingEntityInBlock` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Average intergeneration time, w** — 实体生成之间的平均时间 `off`（默认）| `on`

输出实体生成之间的平均时间。**Average intergeneration time, w** 是总生成时间与已生成实体总数之比。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AverageIntergenerationTime` |
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

生成实体

Entity Generator 模块生成实体。实体是离散事件仿真中可以定义的离散关注项。一个实体可以携带标量、总线或向量数据。实体的含义取决于模型。实体可以表示排队系统中的顾客、从远程控制器到执行器的数据包，或你定义的任何离散项。

默认情况下，该模块的实体生成方法为 `Time-based`。在此方法中，模块使用由 **Period** 指定的代际时间生成实体，该时间来自输入信号或统计分布。有关创建基于时间和随机化实体的更多信息，请参阅 Entities in a SimEvents Model。

该模块还会创建基于事件的实体。选择 `Event-based` 作为 **Generation Method**，以便由外部事件指定实体代际时间。有关示例，请参阅 Generate Entities When Events Occur。

若要自定义实体生成时或实体退出模块时的动作，请在 **Event actions** 选项卡的 `Generate action` 或 `Exit action` 字段中输入 MATLAB® 代码。有关更多信息，请参阅 Events and Event Actions。
