---
type: simulink-block
title: 'Entity Gate'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitygate'
documentation_source_path: 'ref/entitygate.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Gate

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

携带标量、总线或向量数据进入门控的输入实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

### **control** — 传入控制实体 标量

输入控制端口，用于接收决定门控状态的实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 离开实体 标量

离开门控的实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## 参数

### **Operating mode** — 选择操作模式 `Enable gate`（默认）| `Release gate` | `Selection gate`

选择此门控的操作模式。当 **Operating mode** 参数设置为：

- `Enable gate`，此模块表示一个门控，当控制端口接收到值为正的匿名实体时打开，当接收到值为零或负值时关闭。根据定义，打开的门控允许实体到达，只要这些实体能够立即前进到下一个模块，而关闭的门控则禁止实体到达。在控制端口接收到的匿名实体具有 double 类型的数值。由于门控接收到值为正的匿名实体并打开，已启用的门控保持打开状态，直到它接收到值为零或负值的实体并关闭。
- `Release gate`，此模块允许每到达控制端口一个匿名实体或消息，就有一个待处理实体到达。在其他所有时间，模块的实体输入端口不可用。根据定义，门控的打开允许一个待处理实体到达，前提是该实体能够立即前进到下一个模块。
- `Selection gate`，当来自控制端口的匿名实体值与待处理实体的属性匹配时，此模块允许待处理实体到达。否则，它阻止待处理实体的到达。

#### 编程使用

|  |
| --- |
| **模块参数**：`OperatingMode` |
| **类型**：character vector |
| **值**：`'Enable gate'` | `'Release gate'` `'Selection gate'` |
| **默认值**：`'Enable gate'` |

### **Matching attribute** — 指定与控制端口的值进行匹配的属性名称 `Attribute1`（默认）| 字符向量

用于与控制端口的值进行匹配的属性名称。

#### 依赖关系

当您将 **Operating mode** 设置为 `Selection Gate` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`MatchingAttributeName` |
| **类型**：character vector |
| **值**：`'Attribute1'` | character vector |
| **默认值**：`'Attribute1'` |

### **Initial value from the control port** — 指定来自控制端口的初始值以匹配匹配属性 `NaN`（默认）| 标量

指定用于匹配打开门控的匹配属性的初始值。

#### 依赖关系

当您将 **Operating mode** 设置为 `Selection Gate` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialValueOfMatchingAttribute` |
| **类型**：character vector |
| **值**：`'NaN'` | scalar |
| **默认值**：`'NaN'` |

### **Open gate at simulation start** — 在仿真开始时打开门控 `off`（默认）| `on`

选择此选项可在仿真开始时打开门控。

未选中复选框off
:   门控在仿真开始时关闭。

选中复选框on
:   门控在仿真开始时打开。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OpenGateAtSimulationStar` |
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

门控实体

Entity Gate 模块控制待处理实体何时可以在模型中推进。

**Operating mode** 参数指定待处理实体如何通过门。

- `Enable gate` — 每当控制端口接收到值为正的匿名实体时打开并允许实体推进，每当其值为零或负时关闭。有关详细信息，请参阅 Use Queue Event Actions to Model a Storage Tank。
- `Release gate` — 对于到达控制端口的每个匿名实体或消息，允许一个待处理实体推进。在其他所有时间，模块的实体输入端口不可用。
- `Selection gate` — 每当来自控制端口的匿名实体值与待处理实体的属性匹配时，允许实体推进。

使用 Entity Gate 模块控制实体路径上实体的流动。使用 Entity Output Switch 模块在多个实体输出端口中选择一个输出端口用于实体的离开。有关详细信息，请参阅 Route Vehicles Using an Entity Output Switch Block。
