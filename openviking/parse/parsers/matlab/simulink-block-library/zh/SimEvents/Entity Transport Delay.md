---
type: simulink-block
title: 'Entity Transport Delay'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitytransportdelay'
documentation_source_path: 'ref/entitytransportdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Transport Delay

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入实体 SimEvents 实体
  direction: input
- name: ti
  summary: 瞬时延迟 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | bus
- name: Port_1
  summary: 延迟实体 SimEvents 实体
  direction: output
- name: n
  summary: 延迟实体数量 实数标量
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 输入实体 SimEvents 实体

SimEvents 实体或消息。有关 SimEvents 中实体的详细信息，请参阅 SimEvents 模型中的实体。

此端口不具有直接馈通。

### **ti** — 瞬时延迟 标量 | 向量 | 矩阵

SimEvents 实体传输中的瞬时延迟。*ti* 是实体速度的倒数。有关瞬时延迟计算的详细信息，请参阅 Variable Transport Delay。

此端口具有直接馈通。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `bus`
### 输出

### **Port\_1** — 延迟实体 SimEvents 实体

应用了瞬时延迟 *ti* 的 SimEvents 实体。

### **n** — 延迟实体数量 实数标量

模块的辅助输出信号，显示在一个时间步内处理的实体数量。

#### 依赖关系

要启用此端口，请启用 **Output number of entities in block, n** 参数

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Capacity
  summary: 指定模块的容量 inf（默认） | 标量
  group: ''
  block_parameter: Capacity
  type: 字符向量
  values: '''inf'' | 实数标量'
  default: '''inf'''
- name: Output number of entities in block, n
  summary: 输出模块中存在的延迟实体数量 off（默认） | on
  group: ''
  block_parameter: ShowNumberEntitiesInBlock
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Capacity** — 指定模块的容量 inf（默认） | 标量

指定接受待延迟实体的容量。

#### 编程用法

|  |
| --- |
| **模块参数**：`Capacity` |
| **类型**：字符向量 |
| **值**：`'inf'` | 实数标量 |
| **默认值**：`'inf'` |

### **Output number of entities in block, n** — 输出模块中存在的延迟实体数量 `off`（默认） | `on`

模块中正在被延迟的实体数量。

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
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

在 SimEvents 消息的传播中引入延迟

Entity Transport Delay 模块将实体延迟一段时间，称为*传输延迟*。第一个输入是从点 A 传输到点 B 的实体，传输发生在一个长度恒定、速度随时间变化的移动表面上。第二个输入的值是*瞬时延迟*。表面的速度是瞬时延迟的倒数。瞬时延迟与速度的乘积为 1。

该模块通过距离-速度-时间关系计算实现的传输延迟，其中表面长度（距离）等于可变表面速度在传输延迟持续时间（时间）内的积分。有关此计算的详细信息，请参阅 Variable Transport Delay。

Entity Transport Delay 模块通过 Simulink 信号的输入将 SimEvents® 连接到 Simulink®，将传输延迟作为连续过程进行计算，并将此延迟应用于离散事件过程中的实体。有关使用 Entity Transport Delay 模块的示例，请参阅 Modeling Cyber-Physical Systems。
