---
type: simulink-block
title: 'Data Type Scaling Strip'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypescalingstrip'
---

# Data Type Scaling Strip

Remove scaling and map to built in integer

## 中文

移除定标并映射到内置整数

### 库

Simulink / Signal Attributes

### 描述

Data Type Scaling Strip 模块去除定点信号的定标。它将输入数据类型映射为具有足够数据位以容纳输入的最小内置数据类型。输入的存储整数值就是输出的值。输出始终具有标称定标（slope = 1.0 和 bias = 0.0），因此输出不区分实际值和存储整数值。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。该模块去除定点输入信号的定标，并使用尽可能小的内置数据类型输出存储整数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 映射到内置数据类型的输入信号 标量 | 向量 | 矩阵

输入信号的存储整数值，采用尽可能小的内置数据类型，并与输入具有相同的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

## Libraries

Simulink / Signal Attributes

## Description

The Data Type Scaling Strip block strips the scaling off a fixed-point
signal. It maps the input data type to the smallest built-in data type that has enough
data bits to hold the input. The stored integer value of the input is the value of the
output. The output always has nominal scaling (slope = 1.0 and bias = 0.0), so the
output does not distinguish between real world value and stored integer value.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix. The block
strips the scaling off a fixed-point input signal, and outputs the
stored integer value with the smallest possible built-in data
type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Input signal mapped to built-in data type scalar | vector | matrix

Stored integer value of the input signal with the smallest possible
built-in data type, and the same dimensions as the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
