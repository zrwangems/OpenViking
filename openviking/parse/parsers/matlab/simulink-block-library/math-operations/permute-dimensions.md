---
type: simulink-block
title: 'Permute Dimensions'
family: math-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'permutedimensions'
---

# Permute Dimensions

Rearrange dimensions of multidimensional array dimensions

## 中文

重新排列多维数组的维度

### 库

Simulink / Math Operations

### 说明

Permute Dimensions 模块通过置换输入信号的维度来重新排列输入信号的元素。您使用 **Order** 参数指定要应用于输入信号的置换。

例如，要转置 3×5 输入信号，请为 **Order** 参数指定置换向量 `[2
1]`。这样做时，模块会重新排列输入信号的元素并输出一个 5×3 矩阵。

可以将总线数组用作 Permute Dimensions 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅总线数组中的非虚拟总线分组。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

此端口接受 Simulink® 支持的任何数据类型的标量、向量、矩阵和 N 维信号，包括 fixed-point、enumerated 和 nonvirtual bus 数据类型。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### 输出

#### **Port\_1** — 输入信号的置换 标量 | 向量 | 矩阵 | N 维数组

模块根据 **Order** 参数的值输出输入信号的置换。输出与输入具有相同的数据类型。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **Order** — 置换向量 `[2,1]`（默认） | `N` 元素向量，其中 `N` 是输入信号的维数

指定要应用于输入信号维度的置换顺序。此参数的值必须是一个 `N` 元素向量，其中 `N` 是输入信号的维数。置换向量的元素必须是从 1 到 `N` 的值的重新排列。

例如，将置换向量 `[2 1]` 应用于 5×3 输入信号会得到一个 3×5 输出信号，换句话说，即输入信号的转置。

#### 编程使用

|  |
| --- |
| **模块参数**：`Order` |
| **类型**：character vector |
| **值**：`N` 元素向量 |
| **默认值**：`'[2 1]'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2007a 中引入**

## Libraries

Simulink / Math Operations

## Description

The Permute Dimensions block reorders the elements of the input signal by
permuting its dimensions. You specify the permutation to be applied to the input signal
using the **Order** parameter.

For example, to transpose a 3-by-5 input signal, specify the permutation vector `[2
1]` for the **Order** parameter. When you do, the block
reorders the elements of the input signal and outputs a 5-by-3 matrix.

You can use an array of buses as an input signal to a Permute Dimensions
block. For details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

This port accepts scalar, vector, matrix, and N-dimensional signals of
any data type that Simulink® supports, including fixed-point, enumerated, and
nonvirtual bus data types.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Permutation of input signal scalar | vector | matrix | N-D array

The block outputs the permutation of the input signal, according to
the value of the **Order** parameter. The output has
the same data type as the input.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Order** — Permutation vector `[2,1]` (default) | `N`-element vector, where `N` is the number of dimensions of the input signal

Specify the permutation order to apply to the dimensions of the input
signal. The value of this parameter must be an `N`-element
vector where `N` is the number of dimensions of the input
signal. The elements of the permutation vector must be a rearrangement of
the values from 1 to `N`.

For example, the permutation vector `[2 1]` applied to a 5-by-3 input
signal results in a 3-by-5 output signal, in other words, the transpose of
the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Order` |
| **Type**: character vector |
| **Value**: N-element vector |
| **Default**: `'[2 1]'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2007a**
