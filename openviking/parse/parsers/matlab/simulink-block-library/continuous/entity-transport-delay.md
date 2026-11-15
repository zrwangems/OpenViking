---
type: simulink-block
title: 'Entity Transport Delay'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'entitytransportdelay'
---

# Entity Transport Delay

Introduce a delay in propagation of a SimEvents message

## 中文

引入 SimEvents 消息传播的延迟

### 所属库

Simulink / Continuous SimEvents

### 描述

Entity Transport Delay 模块将实体延迟一段时间，称为*传输延迟*。第一个输入是实体，它在一个长度恒定的移动表面上从 A 点传输到 B 点，其速度随时间而变化。第二个输入的值是*瞬时延迟*。表面速度是瞬时延迟的倒数。瞬时延迟与速度的乘积为 1。

该模块通过距离-速度-时间关系计算实现的传输延迟，其中表面长度（距离）等于可变表面速度在传输延迟持续时间（时间）内的积分。有关此计算的更多信息，请参阅Variable Transport Delay。

Entity Transport Delay 模块使用来自 Simulink® 信号的输入将 SimEvents® 连接到 Simulink，并将传输延迟计算为连续过程，并将此延迟应用于离散事件过程中的实体。有关使用 Entity Transport Delay 模块的示例，请参阅信息物理系统建模。

### 端口

#### 输入

#### **Port\_1** — 输入实体 SimEvents 实体

SimEvents 实体或消息。有关 SimEvents 中实体的更多信息，请参阅 Entities in a SimEvents Model (SimEvents)。

此端口没有直接馈通。

#### **ti** — 瞬时延迟 标量 | 向量 | 矩阵

SimEvents 实体传输的瞬时延迟。*ti* 是实体速度的倒数。有关瞬时延迟计算的更多信息，请参阅可变传输延迟。

此端口具有直接馈通。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `bus`
#### 输出

#### **Port\_1** — 延迟实体 SimEvents 实体

SimEvents 实体，其应用了瞬时延迟 *ti*。

#### **n** — 延迟实体的数量 实数标量

模块的次要输出信号，显示在一个时间步内处理的实体数量。

##### 依赖关系

要启用此端口，请启用**模块中的实体数量，n** 参数

**数据类型:** `double`

### 参数

#### **容量** — 指定模块的容量 inf (默认) | 标量

指定接受延迟实体的能力。

##### 编程用法

|  |
| --- |
| **模块参数**：`Capacity` |
| **类型**：字符向量 |
| **值**：`'inf'` | 实数标量 |
| **默认值：**`'inf'` |

#### **输出模块中实体的数量，n** — 输出模块中存在的延迟实体的数量 `off` (默认) | `on`

模块中被延迟的实体数量。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowNumberEntitiesInBlock` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2019b 中推出**

## Libraries

Simulink / Continuous SimEvents

## Description

The Entity Transport Delay block delays an entity for a period of time, named *transport delay*. The first input is the entity that is
transported from point A to point B on a constant-length moving surface whose speed
changes over time. The value from the second input is the *instantaneous delay*. The speed of the surface is the reciprocal of
instantaneous delay. The product of instantaneous delay and the speed is 1.

The block calculates the implemented transport delay by the distance-speed-time
relationship, where the surface length (distance) is equal to the integral of the
variable surface speed over the duration of the transport delay (time). For more
information about this calculation, see Variable Transport Delay.

The Entity Transport Delay block connects SimEvents® to Simulink® using the input from a Simulink signal and computing the transport delay as a continuous process, and
applying this delay to an entity in a discrete-event process. For an example that uses
the Entity Transport Delay block, see Modeling Cyber-Physical Systems.

## Ports

### Input

### **Port\_1** — Input entity SimEvents entity

SimEvents entity or message. For more information on entities in
SimEvents, see Entities in a SimEvents Model (SimEvents).

This port does not have direct feedthrough.

### **ti** — Instantaneous delay scalar | vector | matrix

Instantaneous delay in the transport of the SimEvents entity. *ti* is
the reciprocal of the speed of the entity. For more information on the
calculation of instantaneous delay, see Variable Transport Delay.

This port has direct feedthrough.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `bus`
### Output

### **Port\_1** — Delayed entity SimEvents entity

SimEvents entity with the instantaneous delay
*ti* applied to
it.

### **n** — Number of delayed entities real scalar

Secondary output signal of the block, which displays the number of
entities processed in a time step.

#### Dependencies

To enable this port, enable the **Output number of entities in block,
n** parameter

**Data Types:** `double`

## Parameters

### **Capacity** — Specify the capacity of the block inf (default) | scalar

Specify capacity to accept entities to be delayed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Capacity` |
| **Type**: character vector |
| **Values**: `'inf'` | real scalar |
| **Default**: `'inf'` |

### **Output number of entities in block, n** — Outputs the number of delayed entities present in the block `off` (default) | `on`

Number of entities present in the block that are being delayed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowNumberEntitiesInBlock` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**
