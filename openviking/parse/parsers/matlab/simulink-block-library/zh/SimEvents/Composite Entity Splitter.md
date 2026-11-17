---
type: simulink-block
title: 'Composite Entity Splitter'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'compositeentitysplitter'
documentation_source_path: 'ref/compositeentitysplitter.html'
language: zh-CN
chinese_source: worker-translation
---

# Composite Entity Splitter

## 端口
```yaml
ports:
- name: port_1
  summary: 输入复合实体 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: port_1
  summary: 输出实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: port_2
  summary: 输出实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | enumerated | bus | fixed point
```

### 输入

### **port\_1** — 输入复合实体 标量 | 向量 | 矩阵

进入模块的复合实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **port\_1** — 输出实体 标量 | 向量 | 矩阵

离开模块的实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **port\_2** — 输出实体 标量 | 向量 | 矩阵

离开模块的实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `enumerated` | `bus` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of output ports
  summary: 指定输出端口数量 2（默认）| 标量
  group: ''
  block_parameter: NumberOutputPorts
  type: 字符向量
  values: '''2'' | 标量'
  default: '''2'''
```

### **Number of output ports** — 指定输出端口数量 `2`（默认）| 标量

指定用于输出实体的输出端口数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberOutputPorts` |
| **类型**：字符向量 |
| **值**：`'2'` | 标量 |
| **默认值**：`'2'` |
## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

拆分复合实体

Composite Entity Splitter 模块将复合实体拆分为其各个单独实体，并通过每个未阻塞的实体输出端口输出它们。复合实体可以是 Composite Entity Creator 模块的输出，也可以是来自 Entity Generator 或 Message Send 模块的结构化类型或总线类型实体。
