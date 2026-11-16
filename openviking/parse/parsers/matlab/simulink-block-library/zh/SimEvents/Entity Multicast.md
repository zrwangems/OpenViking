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

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

进入该模块的实体的输入实体端口。

**注意**

使用 string 实体数据类型时不支持事件动作

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
### 输出

### **send** — 广播实体 标量 | 向量 | 矩阵

输出广播后的实体。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## 参数

### **多播标签** — 指定用于广播实体的标签 `A`（默认）| character vector

指定用于广播实体的标签。例如，如果使用默认标签 `A`，则每个 **实体到达来源** 指定为 `Multicast` 且 **多播标签** 设置为 `A` 的 Entity Queue 模块都会收到一个副本。

#### 编程用法

|  |
| --- |
| **模块参数**: `MulticastTag` |
| **类型**: character vector |
| **值**: `'A'` | character vector |
| **默认值**: `'A'` |

## 所属库

SimEvents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016a 中引入**

## 描述

发送多播实体

Entity Multicast 模块广播实体。到达该模块的实体会被克隆为多个副本，并使用**多播标签**发送。每个 **实体到达来源** 指定为 `Multicast` 且具有相同**多播标签**的 Entity Queue 模块都会收到副本。有关详细信息，请参阅离散事件仿真中的队列和服务器概述。
