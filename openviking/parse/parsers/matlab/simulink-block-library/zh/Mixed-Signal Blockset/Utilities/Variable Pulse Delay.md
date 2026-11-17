---
type: simulink-block
title: 'Variable Pulse Delay'
family: 'msblks'
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
```yaml
ports:
- name: in
  summary: 输入样本数据 固定步长离散样本 | 可变步长离散样本
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | floating point
- name: delay
  summary: 向输入信号引入延迟 非负标量
  direction: input
  data_types: floating point
- name: out
  summary: 延迟后的输出样本 固定步长离散样本 | 可变步长离散样本
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | floating point
```

### 输入

### **in** — 输入样本数据 固定步长离散样本 | 可变步长离散样本

输入样本数据，其类型和宽度继承自信号源。该输入端口支持数据总线操作，但不支持帧格式输入。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `floating point`

### **delay** — 向输入信号引入延迟 非负标量

向输入信号引入延迟，指定为非负标量。输入信号到达时 **delay** 端口的值决定了所引入的延迟量。

**数据类型：** `floating point`
### 输出

### **out** — 延迟后的输出样本 固定步长离散样本 | 可变步长离散样本

延迟后的输出样本数据，其类型和宽度与输入信号相同。输入信号到达时 **delay** 端口的值决定了 **out** 端口所引入的延迟量。输入和输出信号必须保持相同的顺序。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `floating point`
## 参数
```yaml
parameters:
- name: Initial Input
  summary: 仿真前输出端口的值 0（默认）| 标量
  group: ''
- name: Buffer Size
  summary: 仿真期间可用的输入缓冲样本数 1（默认）| 正标量整数
  group: ''
```

### **Initial Input** — 仿真前输出端口的值 `0`（默认）| 标量

仿真前输出端口的值，指定为标量。

在仿真开始时，**out** 端口的值等于 **Initial Input** 参数设置的值。如果 **in** 端口的值不等于 **Initial Input** 参数的值，则输出将在等于 **delay** 端口值的延迟之后过渡到 **in** 端口的值。

#### 编程使用

- 使用 `get_param(gcb,'InitialOutput')` 查看 **Initial Input** 的当前值。
- 使用 `set_param(gcb,'InitialOutput',value)` 将 **Initial Input** 设置为特定值。

### **Buffer Size** — 仿真期间可用的输入缓冲样本数 `1`（默认）| 正标量整数

仿真期间可用的输入缓冲样本数，指定为正标量整数。

#### 编程使用

- 使用 `get_param(gcb,'BufferSize')` 查看 **Buffer Size** 的当前值。
- 使用 `set_param(gcb,'BufferSize',value)` 将 **Buffer Size** 设置为特定值。
## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

以可控的、连续可变的量延迟样本

Variable Pulse Delay 模块向信号样本引入可控延迟。**in** 端口处的每个样本按照输入样本到达时 **delay** 端口的值进行延迟。**out** 端口处的延迟样本必须保持与 **in** 端口相同的顺序。

在仿真开始时，**out** 端口被设置为 **Initial Input** 参数的值。
