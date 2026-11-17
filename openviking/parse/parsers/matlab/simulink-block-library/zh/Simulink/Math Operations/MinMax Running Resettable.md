---
type: simulink-block
title: 'MinMax Running Resettable'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'minmaxrunningresettable'
documentation_source_path: 'slref/minmaxrunningresettable.html'
language: zh-CN
chinese_source: worker-translation
---

# MinMax Running Resettable

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    bus
- name: R
  summary: 复位信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    bus
- name: y
  summary: 运行最小值或最大值 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **u** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。根据您为 **Function** 参数指定的内容，该模块输出所有过去输入 `u` 的最小值或最大值。

如果您为 **Initial condition** 参数指定标量值，则该模块会将该参数扩展为与非标量输入 `u` 具有相同的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **R** — 复位信号 标量 | 向量 | 矩阵

接受复位信号的输入端口，指定为标量、向量或矩阵。当复位信号为非标量时，它必须与输入信号 `u` 具有相同的维度。只要复位信号的值为零，该模块就输出输入 `u` 的运行最小值或最大值。每当复位信号具有非零值（`true`）时，该模块会将输出复位为 **Initial condition** 参数的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### 输出

### **y** — 运行最小值或最大值 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵，其中每个输出元素等于对应输入元素的运行最小值或最大值。输出信号 `y` 与输入信号 `u` 具有相同的数据类型和维度。

当该模块接收到非零（`true`）复位信号时，该模块会将输出复位为 **Initial condition** 参数的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Function
  summary: 指定最小值或最大值 min（默认）| max
  group: ''
  block_parameter: Function
  type: 字符向量
  values: '''min'' | ''max'''
- name: Initial condition
  summary: 将输出复位为的值 0.0（默认）| 标量或向量
  group: ''
  block_parameter: vinit
  type: 字符向量
  values: 标量或向量
```

### **Function** — 指定最小值或最大值 `min`（默认）| `max`

指定该模块是输出对应输入元素的运行最小值还是最大值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Function` |
| **类型：** 字符向量 |
| **值：** `'min' | 'max'` |
| **默认：** `'min'` |

### **Initial condition** — 将输出复位为的值 `0.0`（默认）| 标量或向量

指定初始条件值。当复位输入信号 `R` 为 `true` 时，该模块会将输出复位为您指定的值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** 字符向量 |
| **值：** 标量或向量 |
| **默认：** `'0.0'` |
## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

确定信号随时间的最大值或最小值

MinMax Running Resettable 模块输出所有过去输入 `u` 的最小值或最大值。您可以通过 **Function** 参数指定该模块输出运行最小值还是最大值。

该模块可以基于外部复位信号 `R` 复位其状态。当复位信号 `R` 为非零（`true`）时，该模块会将输出复位为 **Initial condition** 参数的值。

输入可以是标量、向量或矩阵信号。该模块输出与输入具有相同维度的信号。每个输出元素等于对应输入元素的运行最小值或最大值。
