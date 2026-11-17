---
type: simulink-block
title: 'Persistent Variable Write'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Target Management'
documentation_page: 'persistentvariablewrite'
documentation_source_path: 'io_ref/persistentvariablewrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Persistent Variable Write

## 端口
```yaml
ports:
- name: Data
  summary: 持久变量输入数据 variable data
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### 输入

### **Data** — 持久变量输入数据 variable data

Persistent Variable Write 模块输入端口的
数据类型继承自其输入信号。该信号可以是任意维度。

该模块可以接受复数。Persistent
Variable Write 模块输入端口的复杂性继承自其输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
## 参数
```yaml
parameters:
- name: Variable name
  summary: 持久变量的名称 Variable1（默认）| 字符向量 | 字符串
  group: ''
  block_parameter: varName
```

### **Variable name** — 持久变量的名称 `Variable1`（默认）| 字符向量 | 字符串

**Variable name** 参数提供持久变量的名称。使用此名称可通过 `getPersistentVariables` 函数从目标计算机检索的变量值结构中访问该变量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `varName` |
## 所属库

Simulink Real-Time / Target Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

将持久变量值写入目标计算机

Persistent Variable Write 模块在实时应用程序启动和停止时向选定的
持久变量写入值。当 Speedgoat® 目标计算机关闭时，该变量值
仍然保留。

使用 `getPersistentVariables` 函数和 `setPersistentVariables` 函数访问
目标计算机上的持久变量值。
