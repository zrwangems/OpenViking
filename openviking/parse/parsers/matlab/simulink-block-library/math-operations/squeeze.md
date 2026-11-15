---
type: simulink-block
title: 'Squeeze'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'squeeze'
---

# Squeeze

Remove singleton dimensions from multidimensional signal

## 中文

从多维信号中删除单一维度

### 所属库

Simulink / Math Operations

### 描述

Squeeze 模块删除其多维输入信号中的单一维度。单一维度是其大小为 1 的任何维度。Squeeze 模块仅对维数大于 2 的信号进行操作。标量、向量和矩阵信号在通过 Squeeze 模块时保持不变。

### 端口

#### 输入

#### **Port\_1** — 多维输入信号 多维信号

输入信号，其中的任何单一维度将在输出中删除。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Port\_1** — 没有单一维度的输出信号 多维信号

没有单一维度的输出信号。例如，大小为 3×1×2 的多维数组会变为 3×2 信号。如果输入中没有单一维度，则输入信号会一直传递到输出而保持不变。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2007b 中推出**

## Libraries

Simulink / Math Operations

## Description

The Squeeze block removes singleton dimensions from its
multidimensional input signal. A singleton dimension is any dimension whose size is one.
The Squeeze block operates only on signals whose number of dimensions is
greater than two. Scalar, vector, and matrix signals pass through the
Squeeze block unchanged.

## Ports

### Input

### **Port\_1** — Multidimensional input signal multidimensional signal

Input signal that has any singleton dimensions removed in the output.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal with no singleton dimensions multidimensional signal

Output signal with no singleton dimensions. For example, a
multidimensional array of size 3-by-1-by-2 changes into a 3-by-2 signal.
If there are no singleton dimensions in the input, then the input signal
is passed through unchanged to the output.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2007b**
