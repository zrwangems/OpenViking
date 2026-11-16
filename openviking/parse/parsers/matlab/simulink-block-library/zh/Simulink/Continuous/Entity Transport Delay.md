---
type: simulink-block
title: 'Entity Transport Delay'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'entitytransportdelay'
documentation_source_path: 'slref/entitytransportdelay.html'
language: zh-CN
chinese_source: official
---

# Entity Transport Delay

## 端口

### 输入

### **Port\_1** — 输入实体 SimEvents 实体

SimEvents 实体或消息。有关 SimEvents 中实体的更多信息，请参阅 Entities in a SimEvents Model (SimEvents)。

此端口没有直接馈通。

### **ti** — 瞬时延迟 标量 | 向量 | 矩阵

SimEvents 实体传输的瞬时延迟。*ti* 是实体速度的倒数。有关瞬时延迟计算的更多信息，请参阅可变传输延迟。

此端口具有直接馈通。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `bus`
### 输出

### **Port\_1** — 延迟实体 SimEvents 实体

SimEvents 实体，其应用了瞬时延迟 *ti*。

### **n** — 延迟实体的数量 实数标量

模块的次要输出信号，显示在一个时间步内处理的实体数量。

#### 依赖关系

要启用此端口，请启用**模块中的实体数量，n** 参数

**数据类型:** `double`

## 参数

### **容量** — 指定模块的容量 inf (默认) | 标量

指定接受延迟实体的能力。

#### 编程用法

|  |
| --- |
| **模块参数**：`Capacity` |
| **类型**：字符向量 |
| **值**：`'inf'` | 实数标量 |
| **默认值：**`'inf'` |

### **输出模块中实体的数量，n** — 输出模块中存在的延迟实体的数量 `off` (默认) | `on`

模块中被延迟的实体数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`ShowNumberEntitiesInBlock` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Continuous SimEvents

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2019b 中推出**

## 描述

引入 SimEvents 消息传播的延迟

Entity Transport Delay 模块将实体延迟一段时间，称为*传输延迟*。第一个输入是实体，它在一个长度恒定的移动表面上从 A 点传输到 B 点，其速度随时间而变化。第二个输入的值是*瞬时延迟*。表面速度是瞬时延迟的倒数。瞬时延迟与速度的乘积为 1。

该模块通过距离-速度-时间关系计算实现的传输延迟，其中表面长度（距离）等于可变表面速度在传输延迟持续时间（时间）内的积分。有关此计算的更多信息，请参阅Variable Transport Delay。

Entity Transport Delay 模块使用来自 Simulink® 信号的输入将 SimEvents® 连接到 Simulink，并将传输延迟计算为连续过程，并将此延迟应用于离散事件过程中的实体。有关使用 Entity Transport Delay 模块的示例，请参阅信息物理系统建模。
