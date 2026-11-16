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
chinese_source: official
---

# Software Watchdog Timer

## 端口

### 输入

### **Restart** — 用于重启 watchdog 计时器计数器的脉冲 标量

重启 watchdog 计时器计数器的脉冲（值为 true）。当脉冲下降时，计数器恢复计数（值为 false）。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Status** — watchdog 计时器状态 标量

watchdog 计时器状态显示为以下状态之一：

- true 表示计数器值小于**最大计数**参数的值。
- false 表示计数器值等于**最大计数**参数的值，并且该模块已停止计数器。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **最大计数** — watchdog 计时器值的最大限值 `10` (默认) | 标量

watchdog 计时器计数器值的最大限值，它会导致模块停止计数并将 watchdog 计时器状态变为 false。

### **计数器数据类型** — `Status` 输出的数据类型 **uint8** (默认) | **uint16** | **uint32**

watchdog 计时器状态输出的数据类型。

## 所属库

Motor Control Blockset / Sensor Decoders

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

输出 true，直到计数器达到最大计数限值

Software Watchdog Timer 模块会递增计数器值，直到该模块接收到 `Restart` 输入脉冲，或计数达到**最大计数**参数的值。

接收到 `Restart` 脉冲后，该模块会重新启动计数器，并在 `Restart` 脉冲下降时再次开始递增计数器值。

该模块将 `Status` 输出保持为 true，直到计数器值持续小于**最大计数**参数的值。当计数器达到**最大计数**时，模块会停止计数器并将 `Status` 设置为 false。
