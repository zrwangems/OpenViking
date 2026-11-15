---
type: simulink-block
title: 'Message Merge'
family: messages-events
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'messagemerge'
---

# Message Merge

Combine message paths

## 中文

合并消息路径

### 库

Simulink / Messages & Events

### 描述

Message Merge 模块以图形方式将多条消息线合并为单条消息线。合并消息线不会改变消息本身。您可以指定要合并的消息线数量。

当您想要合并多个传入消息并输出到单个目标（例如队列或消息存储模块）时，请使用此模块。

**注意**

Message Merge 模块在 AUTOSAR 模式下不支持代码生成。

### 端口

#### 输入

#### **Port\_1** — 要合并的输入消息线 标量 | 向量 | 矩阵

进入模块的消息的输入消息端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

#### **Port\_2** — 要合并的输入消息线 标量 | 向量 | 矩阵

进入模块的消息的输入消息端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
#### 输出

#### **Port** — 输出消息线 标量 | 向量 | 矩阵

离开模块的消息的输出消息端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### 参数

#### **输入端口数** — 指定要合并的消息线数量 `2` (默认) | scalar

确定要合并的消息输入端口数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NumberInputPorts` |
| **类型**: character vector |
| **值**: `'2'` | scalar |
| **默认值**: `'2'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 版本历史

**在 R2021a 中引入**

## Libraries

Simulink / Messages & Events

## Description

The Message Merge block graphically combines multiple message lines into a
single message line. Merging message lines does not change the messages themselves. You can
specify the number of message lines to merge.

Use this block when you want to merge multiple incoming messages and output to a single
destination such as a queue or a message storage block.

**Note**

Message Merge block is not supported for code generation in AUTOSAR
mode.

## Ports

### Input

### **Port\_1** — Input message line to merge scalar | vector | matrix

Input message port for messages entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — Input message line to merge scalar | vector | matrix

Input message port for messages entering the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port** — Output message line scalar | vector | matrix

Output message port for messages exiting the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Number of input ports** — Specify the number message lines to combine `2` (default) | scalar

Determines the number of message input ports to be combined.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberInputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | scalar |
| **Default**: `'2'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**
