---
type: simulink-block
title: 'MinMax Running Resettable'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'minmaxrunningresettable'
documentation_source_path: 'slref/minmaxrunningresettable.html'
language: zh-CN
chinese_source: official
---

# MinMax Running Resettable

## 端口

### 输入

### **u** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。根据您为**函数**参数指定的内容，模块输出所有过去的输入 `u` 的最小值或最大值。

如果您为**初始条件**参数指定标量值，模块将扩展该参数，使其与非标量输入 `u` 具有相同的维度。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **R** — 重置信号 标量 | 向量 | 矩阵

输入端口接受标量、向量或矩阵形式的重置信号。当重置信号为非标量时，其维度必须与输入信号 `u` 相同。只要重置信号具有零值，模块就会输出输入信号 `u` 的动态最小值或最大值。只要重置信号具有非零值 (`true`)，模块就会将输出重置为**初始条件**参数的值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### 输出

### **y** — 动态最小值或最大值 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵，其中每个输出元素等于对应输入元素的动态最小值或最大值。输出信号 `y` 与输入信号 `u` 具有相同的数据类型和维度。

当模块接收到非零 (`true`) 重置信号时，模块将输出重置为**初始条件**参数的值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **函数** — 指定最小值或最大值 `min` (默认) | `max`

指定模块是否输出对应输入元素的动态最小值或最大值。

#### 编程用法

|  |
| --- |
| **模块参数**：`Function` |
| **类型：**字符向量 |
| **值：**`'min' | 'max'` |
| **默认值：**`'min'` |

### **初始条件** — 将输出重置后的值 `0.0` (默认) | 标量或向量

指定初始条件值。当重置输入信号 `R` 为 `true` 时，模块将输出重置为您指定的值。

#### 编程用法

|  |
| --- |
| **模块参数**：`vinit` |
| **类型：**字符向量 |
| **值：**标量或向量 |
| **默认值：**`'0.0'` |

## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

确定信号随时间而改变的最小值或最大值

MinMax Running Resettable 模块可输出过去所有输入信号 `u` 的最小值或最大值。您可以使用**函数**参数指定此模块是输出动态最小值还是最大值。

模块可以根据外部重置信号 `R` 重置其状态。当重置信号 `R` 为非零 (`true`) 时，模块将输出重置为**初始条件**参数的值。

输入可以是标量、向量或矩阵信号。模块将输出与输入具有相同维度的信号。每个输出元素等于对应输入元素的动态最小值或最大值。
