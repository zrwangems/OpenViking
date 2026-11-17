---
type: simulink-block
title: 'Entity Gate'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'SimEvents'
documentation_page: 'entitygate'
documentation_source_path: 'ref/entitygate.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Gate

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

携带标量、总线或向量数据以进入该门控的输入实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **control** — 传入控制实体 标量

输入控制端口，用于接收决定门控状态的实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1** — 离开的实体 标量

输出实体端口，用于离开该门控的实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## 参数

### **操作模式** — 选择操作模式 `Enable gate`（默认） | `Release gate` | `Selection gate`

选择该门控的操作模式。将 **操作模式** 参数设置为：

- `Enable gate`，此模块表示一个门控：每当控制端口接收到值为正的匿名实体时打开，并在其值为零或负值时关闭。根据定义，打开的门控允许实体到达，只要这些实体能够立即前进到下一个模块；而关闭的门控禁止实体到达。在控制端口接收到的匿名实体具有 double 类型的数值。由于门控接收到值为正的匿名实体并打开，启用的门控会保持打开，直到接收到值为零或负值的实体并关闭。
- `Release gate`，此模块对于到达控制端口的每个匿名实体或消息，允许一个待处理实体到达。在其他所有时间，该模块的实体输入端口不可用。根据定义，如果实体能够立即前进到下一个模块，则打开门控允许一个待处理实体到达。
- `Selection gate`，此模块在来自控制端口的匿名实体值与待处理实体的属性匹配时，允许待处理实体到达。否则，它阻止待处理实体到达。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OperatingMode` |
| **类型**: character vector |
| **值**: `'Enable gate'` | `'Release gate'` `'Selection gate'` |
| **默认值**: `'Enable gate'` |

### **匹配属性** — 指定与控制端口的值匹配的属性名称 `Attribute1`（默认） | character vector

用于与控制端口的值匹配的属性名称。

#### 依赖关系

当您将 **操作模式** 设置为 `Selection Gate` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `MatchingAttributeName` |
| **类型**: character vector |
| **值**: `'Attribute1'` | character vector |
| **默认值**: `'Attribute1'` |

### **来自控制端口的初始值** — 指定来自控制端口的初始值，以与匹配属性匹配 `NaN`（默认） | scalar

指定用于与匹配属性匹配并打开门控的初始值。

#### 依赖关系

当您将 **操作模式** 设置为 `Selection Gate` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InitialValueOfMatchingAttribute` |
| **类型**: character vector |
| **值**: `'NaN'` | scalar |
| **默认值**: `'NaN'` |

### **仿真开始时打开门控** — 在开始时打开门控 `off`（默认） | `on`

选择此选项可在仿真开始时打开门控。

未选中复选框 off
:   门控在仿真开始时关闭。

选中复选框 on
:   门控在仿真开始时打开。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OpenGateAtSimulationStar` |
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

门控实体

Entity Gate 模块控制待处理实体何时可以在模型中前进。

**操作模式** 参数指定待处理实体如何通过该门控前进。

- `Enable gate` — 每当控制端口接收到值为正的匿名实体时打开并允许实体前进，当该值为零或负值时关闭。有关详细信息，请参阅使用队列事件操作对储罐建模。
- `Release gate` — 对于到达控制端口的每个匿名实体或消息，允许一个待处理实体前进。在其他所有时间，该模块的实体输入端口不可用。
- `Selection gate` — 每当来自控制端口的匿名实体值与待处理实体的属性匹配时，允许实体前进。

使用 Entity Gate 模块控制实体路径上的实体流。使用 Entity Output Switch 模块在多个实体输出端口中选择一个输出端口供实体离开。有关详细信息，请参阅使用 Entity Output Switch 模块规划车辆路线。
