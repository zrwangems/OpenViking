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

#### 依赖项

要启用此端口，请点击 **实体生成** 选项卡，并为 **生成方法** 选择 `Event-based`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — 用于确定下一次实体生成的生成间隔时间值的信号输入 标量 | 向量 | 矩阵

#### 依赖项

要启用此端口，请点击 **实体生成** 选项卡，为 **生成方法** 选择 `Time-based`，并为 **时间源** 选择 `Signal port`。

**数据类型：** `double`

### 输出

### **Port\_1** — 输出生成的实体 标量 | 向量 | 矩阵

离开生成器的已生成实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖项

要启用此端口，请点击 **统计信息** 选项卡，并选中标记为 **已离开实体数量，d** 的框。

**数据类型：** `double`

### **Port\_pe** — 模块中的待处理实体 off（默认） | on

对于待处理实体输出 `1`，否则输出 `0`。

#### 依赖项

要启用此端口，请选择 **统计信息** > **模块中的待处理实体，pe**。

**数据类型：** `double`

### **Port\_w** — 平均生成间隔时间 off（默认） | on

输出实体生成之间的平均时间。

#### 依赖项

要启用此端口，请选择 **统计信息** > **平均生成间隔时间，w**。

**数据类型：** `double`

## 参数

### **生成方法** — 选择实体生成方法 `Time-based`（默认） | `Event-based`

选择实体生成方法。选择 `Time-based` 可以使用来自输入信号或统计分布的生成间隔时间生成实体。选择 `Event-based` 可以由外部事件确定实体生成间隔时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`GenerationMethod` |
| **类型**：character vector |
| **值**：`'Time-based'` | `'Event-based'` |
| **默认值**：`'Time-based'` |

### **时间源** — 选择生成间隔时间的来源 `Dialog`（默认） | `Signal port` | `MATLAB action`

指定实体生成间隔时间的来源。

- 选择 `Dialog` 以指定实体生成之间的固定周期。
- 选择 `Signal port` 以基于输入信号生成实体。
- 选择 `MATLAB action` 以定义一个 MATLAB 脚本，该脚本定义由 `dt` 表示的生成间隔时间。

有关为实体指定生成间隔时间的详细信息，请参阅“为实体指定生成间隔时间”。

#### 依赖项

当 **生成方法** 设置为 `Time-based` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Signal port'` | `'MATLAB action'` |
| **默认值**：`'Dialog'` |

### **周期** — 定义实体生成之间的周期 `1`（默认） | 标量

指定实体生成间隔时间。例如，如果 **周期** 为 `1`，则该模块在实体生成之间等待 `1` 个仿真时间。有关详细信息，请参阅“为实体指定生成间隔时间”。

**可调：** 是

#### 依赖项

当 **生成方法** 设置为 `Time-based` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`Period` |
| **类型**：character vector |
| **值**：`'1'` | 标量 |
| **默认值**：`'1'` |

### **生成间隔时间动作** — 指定实体生成之间的时间 `dt = rand(1,1)`（默认） | MATLAB 代码

使用 MATLAB 代码指定服务时间。`dt` 指定实体生成之间的时间。您可以手动指定 `dt`，或使用 **插入模式** 按钮以重复序列或从分布生成实体。每次模块准备好生成实体时都会使用此参数。有关示例，请参阅“为实体指定生成间隔时间”。

#### 依赖项

当 **服务时间源** 设置为 `MATLAB action` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntergenerationTimeAction` |
| **类型**：character vector |
| **值**：MATLAB 代码 |
| **默认值**：`'dt = rand(1,1);'` |

### **在仿真开始时生成实体** — 在仿真开始时生成实体 `on`（默认） | `off`

在仿真开始时生成实体。

#### 编程使用

|  |
| --- |
| **模块参数**：`GenerateEntityAtSimulationStart` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **实体类型** — 选择要生成的实体类型 `Structured`（默认） | `Anonymous` | `Bus object`

选择要生成的实体类型。

- `Anonymous` 类型有一个与其关联的数据值。
- `Structured` 类型（默认）包含您可以指定的名称和初始值属性。

  - 您可以通过点击绿色加号符号为实体附加多个属性。
  - 您可以通过点击红色叉号符号删除属性。
  - 您可以通过点击蓝色向上箭头和蓝色向下箭头更改属性的顺序。
  - 您可以通过点击其上方有两个较小符号的文件符号：左上角的绿色向下箭头，以及右下角的三条平行黑线，将 `Structured` 类型实体转换为总线对象。
- `Bus object` 类型允许您生成总线对象作为实体。

  要打开类型编辑器以生成总线对象，请点击 **打开类型编辑器**。总线对象可以是另一个总线对象的元素，这可用于在附加到实体的数据中创建层次结构。

有关详细信息，请参阅“SimEvents 模型中的实体”。

#### 限制

对于 `Structured` 实体类型，您可以从“模块参数”对话框中最多创建 31 个属性。要创建超过 31 个属性，请对 `EntityType` 模块参数使用 `set_param` 函数。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntityType` |
| **类型**：character vector |
| **值**：`'Structured'` | `'Anonymous'` | `'Bus object'` |
| **默认值**：`'Structured'` |

### **实体优先级** — 指定生成的实体的优先级 `300`（默认） | 标量

确定生成的实体的优先级。值越低，优先级越高。有关详细信息，请参阅“使用实体属性和实体优先级”。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntityPriority` |
| **类型**：character vector |
| **值**：`'300'` | 标量 |
| **默认值**：`'300'` |

### **实体类型名称** — 指定生成的实体的名称 `Entity`（默认） | character vector

确定生成的实体的名称。

#### 依赖项

当 **实体类型** 设置为 `Bus object` 或 `Structured` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntityTypeName` |
| **类型**：character vector |
| **值**：`'Entity'` | character vector |
| **默认值**：`'Entity'` |

### **数据初始值** — 指定匿名实体数据的初始值 `0`（默认） | 标量 | 向量 | 矩阵

设置匿名实体数据初始值。此值不能为 int64 或 fixed-point 类型。

#### 依赖项

当您将 **实体类型** 设置为 `Anonymous` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataInitialValue` |
| **类型**：character vector |
| **值**：`'0'` | 标量 | 向量 | 矩阵 |
| **默认值**：`'0'` |

### **属性名称** — 定义生成的实体属性的名称 `Attribute1`（默认） | character vector

定义实体属性名称。

**注意**

完成后，您可以将结构化实体类型作为总线对象导出到基础工作区，名称为 **实体类型名称**。在使用 MATLAB Discrete-Event System 和 Discrete Event Chart 模块时，请导出该总线对象。

#### 依赖项

当 **实体类型** 设置为 `Structured` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`AttributeName` |
| **类型**：character vector |
| **值**：`'Attribute1'` | character vector |
| **默认值**：`'Attribute1'` |

### **属性初始值** — 定义生成的实体属性初始值 `1`（默认） | 标量

指定实体属性初始值。当 **实体类型** 设置为 `Structured` 时，此参数可见。此值不能为 fixed-point 类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`AttributeInitialValue` |
| **类型**：character vector |
| **值**：`1` | 标量 |
| **默认值**：`'1'` |

### **事件动作** — 指定实体在特定事件上的行为 `Generate`（默认） | `Exit`

在 **事件动作** 参数中定义行为。当生成实体时调用 `Generate` 动作，在实体离开模块之前调用 `Exit` 动作。

#### 编程使用

|  |
| --- |
| **模块参数**：`GenerateAction, ExitAction` |
| **类型**：character vector |
| **值**：MATLAB 代码 |
| **默认值**：`''` |

### **已离开实体数量，d** — 输出已离开模块的实体数量 `off`（默认） | `on`

已离开模块的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **模块中存在待处理实体，pe** — 待处理实体 `off`（默认） | `on`

指示模块中是否存在尚未离开的实体。对于待处理实体，该值为 `1`，否则为 `0`。此模块最多只能有一个待处理实体，因为其存储容量为 1。如果存在待处理实体，则该模块不会生成另一个实体，直到该待处理实体离开模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PendingEntityInBlock` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **平均生成间隔时间，w** — 实体生成之间的平均时间 `off`（默认） | `on`

输出实体生成之间的平均时间。**平均生成间隔时间，w** 是总生成时间与已生成实体总数之比。

#### 编程使用

|  |
| --- |
| **模块参数**：`AverageIntergenerationTime` |
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

**在 R2016a 中引入**

## 描述

生成实体

Entity Generator 模块生成实体。实体是您可以在离散事件仿真中定义的离散关注项。实体可以携带标量、bus 或向量数据。实体的含义取决于模型。实体可以表示排队系统中的客户、从远程控制器到执行器的数据包，或您定义的任何离散项。

默认情况下，模块实体生成方法为 `Time-based`。在此方法中，模块使用由 **周期** 指定、来自输入信号或统计分布的生成间隔时间来生成实体。有关创建基于时间和随机化实体的详细信息，请参阅“SimEvents 模型中的实体”。

该模块还可以创建基于事件的实体。选择 `Event-based` 作为 **生成方法**，以便由外部事件指定实体生成间隔时间。有关示例，请参阅“事件发生时生成实体”。

要自定义生成实体或实体离开模块时的动作，请在 **事件动作** 选项卡中，在 `Generate action` 或 `Exit action` 字段中输入 MATLAB® 代码。有关详细信息，请参阅“事件和事件动作”。
