---
type: simulink-block
title: 'Multicast Receive Queue'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'multicastreceivequeue'
documentation_source_path: 'ref/multicastreceivequeue.html'
language: zh-CN
chinese_source: worker-translation
---

# Multicast Receive Queue

## 端口

### 输入

### **receive** — 接收广播实体 标量 | 向量 | 矩阵

用于已接收实体的输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

当下游模块准备好接受该实体时，位于队列头部并即将离开的输出实体。

**注意**

string 实体数据类型不支持事件动作

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string` | `fixed point`

## 参数

R2025b 中未记录。

## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

接收多播实体

Multicast Receive Queue 模块与将 **实体到达源** 参数设置为 `Multicast` 的 Entity Queue 模块相同。有关参数说明的信息，请参阅 Entity Queue 模块的文档。

您为接收实体指定 **多播标签**。然后，该模块接收由 Entity Multicast 模块广播的、具有匹配 **多播标签** 的实体。有关使用多播模式广播实体的详细信息，请参阅离散事件仿真中的队列和服务器概述。
