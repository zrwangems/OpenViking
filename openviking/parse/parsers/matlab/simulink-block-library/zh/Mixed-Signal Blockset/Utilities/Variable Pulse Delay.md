---
type: simulink-block
title: 'Variable Pulse Delay'
family: 'utilities'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'variablepulsedelay'
documentation_source_path: 'ref/variablepulsedelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Pulse Delay

## 端口

### 输入

### **in** — 输入样本数据，固定步长离散样本 | 变步长离散样本

输入样本数据，其类型和宽度继承自信号源。该输入端口支持数据总线操作，但不支持帧输入。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `floating point`

### **delay** — 向输入信号引入延迟，非负标量

向输入信号引入延迟，指定为非负标量。输入信号到达时 **delay** 端口的值决定引入的延迟量。

**数据类型：** `floating point`

### 输出

### **out** — 延迟后的输出样本，固定步长离散样本 | 变步长离散样本

延迟后的输出样本数据，其类型和宽度与输入信号相同。输入信号到达时 **delay** 端口的值决定在 **out** 端口引入的延迟量。输入和输出信号必须保持相同顺序。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `floating point`

## 参数

### **初始输入** — 仿真前输出端口的值 `0` (默认) | 标量

仿真前输出端口的值，指定为标量。

仿真开始时，**out** 端口的值等于 **初始输入** 参数设置的值。如果 **in** 端口的值不等于 **初始输入** 参数的值，则经过等于 **delay** 端口值的延迟后，输出将过渡到 **in** 端口的值。

#### 编程用法

- 使用 `get_param(gcb,'InitialOutput')` 查看 **初始输入** 的当前值。
- 使用 `set_param(gcb,'InitialOutput',value)` 将 **初始输入** 设置为特定值。

### **缓冲区大小** — 仿真期间可用的输入缓冲样本数 `1` (默认) | 正整数标量

仿真期间可用的输入缓冲样本数，指定为正整数标量。

#### 编程用法

- 使用 `get_param(gcb,'BufferSize')` 查看 **缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'BufferSize',value)` 将 **缓冲区大小** 设置为特定值。

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

按受控、连续可变的延迟量延迟样本

Variable Pulse Delay 模块在信号样本中引入可控延迟。每个 **in** 端口样本按输入样本到达时 **delay** 端口的值进行延迟。**out** 端口的延迟样本必须与 **in** 端口保持相同顺序。

仿真开始时，**out** 端口设置为 **初始输入** 参数的值。
