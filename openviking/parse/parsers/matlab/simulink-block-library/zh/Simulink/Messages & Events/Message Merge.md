---
type: simulink-block
title: 'Message Merge'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'messagemerge'
documentation_source_path: 'slref/messagemerge.html'
language: zh-CN
chinese_source: worker-translation
---

# Message Merge

## 端口

### 输入

### **Port\_1** — 要合并的输入消息线 标量 | 向量 | 矩阵

进入模块的消息的输入消息端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — 要合并的输入消息线 标量 | 向量 | 矩阵

进入模块的消息的输入消息端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port** — 输出消息线 标量 | 向量 | 矩阵

离开模块的消息的输出消息端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## 参数

### **Number of input ports** — 指定要合并的消息线数量 `2`（默认）| 标量

确定要合并的消息输入端口数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberInputPorts` |
| **类型**：字符向量 |
| **值**：`'2'` | 标量 |
| **默认值**：`'2'` |

## 所属库

Simulink / Messages & Events

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

合并消息路径

Message Merge 模块以图形方式将多条消息线合并为一条消息线。合并消息线不会更改消息本身。您可以指定要合并的消息线数量。

当您想要合并多条传入消息并输出到单个目标（例如队列或消息存储模块）时，请使用此模块。

**注意**

Message Merge 模块不支持 AUTOSAR 模式下的代码生成。
