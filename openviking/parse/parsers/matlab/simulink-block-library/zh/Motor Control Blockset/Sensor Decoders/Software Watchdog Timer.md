---
type: simulink-block
title: 'Software Watchdog Timer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'softwarewatchdogtimer'
documentation_source_path: 'ref/softwarewatchdogtimer.html'
language: zh-CN
chinese_source: worker-translation
---

# Software Watchdog Timer

## 端口

### 输入

### **Restart** — 用于重新启动看门狗定时器计数器的脉冲 标量

用于重新启动看门狗定时器计数器的脉冲（true 值）。当脉冲下降（false 值）时，
计数器恢复计数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Status** — 看门狗定时器状态 标量

看门狗定时器状态指示为以下值之一：

- True 表示计数器值小于
  **Maximum count** 参数的值。
- False 表示计数器值等于
  **Maximum count** 参数的值，并且模块已停止
  计数器。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Maximum count** — 看门狗定时器值的最大限值 `10` (默认值) | 标量

看门狗定时器计数器值的最大限值，达到该限值会导致模块停止
计数器并将看门狗定时器状态变为 false。

### **Counter data type** — `Status` 输出的数据类型 `uint8` (默认值) | `uint16` | `uint32`

看门狗定时器状态输出的数据类型。

## 所属库

Motor Control Blockset / Sensor Decoders

## 模块特性

在 R2025b 中未提供文档说明。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

输出保持为 true，直到计数器达到最大计数限制

Software Watchdog Timer 模块会递增计数器值，直到模块接收到 `Restart` 输入脉冲，或计数达到 **Maximum count** 参数的值。

接收到 `Restart` 脉冲后，模块会重新启动计数器，并在 `Restart` 脉冲下降时再次开始递增计数器值。

只要计数器值仍小于 **Maximum count** 参数的值，模块就会将 `Status` 输出保持为 true。当计数器达到 **Maximum count** 时，模块会停止计数器，并将 `Status` 置为 false。
