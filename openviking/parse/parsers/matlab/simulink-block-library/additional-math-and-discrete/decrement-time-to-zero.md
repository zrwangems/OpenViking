---
type: simulink-block
title: 'Decrement Time To Zero'
family: additional-math-and-discrete
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Additional Math and Discrete'
documentation_page: 'decrementtimetozero'
---

# Decrement Time To Zero

Decrease real-world value of signal by sample time, but only to zero

## 中文

将信号的实际值按采样时间递减，但仅递减到零

### 库

Simulink / Additional Math & Discrete / Additional Math: Increment - Decrement

### 描述

Decrement Time To Zero 模块将信号的实际值减去采样时间 `Ts`。输出永远不会低于零。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出是输入信号的实际值减去采样时间 `Ts` 后的结果。输出永远不会低于零。输出与输入具有相同的数据类型和维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

## Libraries

Simulink / Additional Math & Discrete / Additional Math: Increment - Decrement

## Description

The Decrement Time To Zero block decreases the real-world value of the
signal by the sample time, `Ts`. The output never goes below
zero.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output is the real-world value of the input signal decreased by the
sample time, `Ts`. The output never goes below zero.
The output has the same data type and dimensions as the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
