---
type: simulink-block
title: 'Event Send'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Adaptive Software Component Modeling / Component Development'
documentation_page: 'eventsend'
documentation_source_path: 'ref/eventsend.html'
language: zh-CN
chinese_source: official
---

# Event Send

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

Event Send 模块的输入端口用于接收 AUTOSAR Blockset 支持的任何类型的输入。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出事件 标量 | 向量 | 矩阵

Event Send 模块的输出端口用于输出事件。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus`

## 参数

R2025b 官方文档未提供。

## 所属库

AUTOSAR Blockset / Adaptive Platform / Signal Routing

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2019a 中推出**

## 描述

将输入信号转换为事件

在 AUTOSAR Adaptive 模型的顶层，使用 Event Receive 和 Event Send 模块设置基于事件的通信。

- 在每个根输入端口后添加一个 Event Receive 模块，后者将输入事件转换为信号，同时保留信号值和数据类型。
- 在每个根输出端口前添加一个 Event Send 模块，后者将输入信号转换为事件，同时保留信号值和数据类型。

Event Send 模块不支持行优先代码生成。
