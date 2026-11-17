---
type: simulink-block
title: 'Entity Multicast'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entitymulticast'
documentation_source_path: 'ref/entitymulticast.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Multicast

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入实体 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | string | fixed point
- name: send
  summary: 广播实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | string | fixed point
```

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入端口。

**注意**

字符串实体数据类型不支持事件动作

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
### 输出

### **send** — 广播实体 标量 | 向量 | 矩阵

输出广播的实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
## 参数
```yaml
parameters:
- name: Multicast tag
  summary: 指定用于广播实体的标签 A（默认）| 字符向量
  group: ''
  block_parameter: MulticastTag
  type: 字符向量
  values: '''A'' | 字符向量'
```

### **Multicast tag** — 指定用于广播实体的标签 `A`（默认）| 字符向量

指定用于广播实体的标签。例如，如果使用默认标签 `A`，则每个将 **Entity arrival source** 指定为 `Multicast` 且 **Multicast tag** 设置为 `A` 的 Entity Queue 模块都会收到一份副本。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MulticastTag` |
| **类型**：字符向量 |
| **值**：`'A'` | 字符向量 |
| **默认**：`'A'` |
## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

发送多播实体

Entity Multicast 模块广播实体。到达该模块的实体会被克隆为多份副本，并附带一个 **Multicast tag** 发送出去。每个将 **Entity arrival source** 指定为 `Multicast` 且具有相同 **Multicast tag** 的 Entity Queue 模块都会收到副本。有关详细信息，请参阅 Overview of Queues and Servers in Discrete-Event Simulation。
