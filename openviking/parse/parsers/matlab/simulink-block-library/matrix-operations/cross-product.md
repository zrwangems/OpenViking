---
type: simulink-block
title: 'Cross Product'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'crossproduct'
---

# Cross Product

Cross product of two vectors

## 中文

两个向量的叉积

### 所属库

Simulink / Matrix Operations

### 描述

Cross Product 模块返回两个 3×1 向量的叉积或向量积。

### 端口

#### 输入

#### **Port\_1** — 第一个输入向量 三元素向量

第一个输入向量，指定为三元素向量。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

#### **Port\_2** — 第二个输入向量 三元素向量

第二个输入向量，指定为三元素向量。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Port\_1** — 输入向量的叉积 三元素向量

输入向量的叉积，以三元素向量形式返回。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2021b 中推出**

## Libraries

Simulink / Matrix Operations

## Description

The Cross Product block returns the cross product, or vector product, of
two 3-by-1 vectors.

## Ports

### Input

### **Port\_1** — First input vector 3-element vector

First input vector, specified as a 3-element vector.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

### **Port\_2** — Second input vector 3-element vector

Second input vector, specified as a 3-element vector.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Cross product of input vectors 3-element vector

Cross product of input vectors, returned as a 3-element vector.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**
