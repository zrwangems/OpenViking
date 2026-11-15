---
type: simulink-block
title: 'Persistent Variable Write'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Execution Parameters'
documentation_page: 'persistentvariablewrite'
documentation_source_path: 'io_ref/persistentvariablewrite.html'
language: zh-CN
chinese_source: official
---

# Persistent Variable Write

## 端口

### 输入

### **Data** — 持久变量输入数据 变量数据

Persistent Variable Write 模块输入端口的数据类型继承自其输入信号。信号可以是任意维度。

该模块可处理复数。Persistent Variable Write 模块输入端口的复杂性源自其输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

### **Variable name** — 持久变量名称 `Variable1` (默认) | 字符向量 | 字符串

**Variable name** 参数提供持久变量的名称。使用此名称访问通过 `getPersistentVariables` 函数从目标计算机检索到的变量值结构体中的变量。

#### 编程用法

|  |
| --- |
| **模块参数：**`varName` |

## 所属库

Simulink Real-Time / Target Management

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2022a 中推出**

## 描述

将持久变量的值写入目标计算机

Persistent Variable Write 模块在实时应用程序启动和停止时，向选定的持久变量写入值。当 Speedgoat® 目标计算机关闭时，该变量值仍会保留。

使用 `getPersistentVariables` 函数和 `setPersistentVariables` 函数访问目标计算机上的持久变量值。
