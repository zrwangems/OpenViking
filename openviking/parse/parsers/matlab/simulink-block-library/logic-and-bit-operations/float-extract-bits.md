---
type: simulink-block
title: 'Float Extract Bits'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'floatextractbits'
---

# Float Extract Bits

Extract bits from floating-point input samples

## 中文

从浮点输入样本中提取位

### 库

Simulink / Logic and Bit Operations

### 说明

Float Extract Bits 模块接受包含浮点数据的信号，并输出包含该数据的二进制表示的信号。有关此二进制表示的详细信息，请参阅 IEEE Standard for Floating Point Arithmetic。

### 端口

#### 输入

#### **Port\_1** — 包含浮点数据的信号 标量 | 向量 | 矩阵

包含浮点数据的信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `half` | `bus`
#### 输出

#### **Port\_1** — 数据的二进制表示 标量 | 向量 | 矩阵

数据的二进制表示，返回为标量、向量或矩阵。
Float Extract Bits 基于 **输出模式** 参数计算定点输出。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **输出模式** — 要输出的数据部分 `All bits`（默认） | `Range of bits` | `Sign` | `Mantissa` | `Exponent`

要作为其二进制表示输出的数据部分，指定为：

- `All bits`
- `Range of bits`
- `Sign`
- `Mantissa`
- `Exponent`

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputMode` |
| **类型**：character vector |
| **值**：`'All bits'` | `'Range of bits'` | `'Sign'` | `'Mantissa'` | `'Exponent'` |
| **默认值**：`'All bits'` |

#### **位范围 ([start end]，相对于 LSB 从 0 开始)** — 要返回的位范围 `[0 15]`（默认） | vector

要返回的信号的位范围，指定为向量。

#### 编程用法

|  |
| --- |
| **模块参数**：`BitRange` |
| **类型**：character vector |
| **值**：`'[0 15]'` | vector |
| **默认值**：`'[0 15]'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 版本历史

**在 R2023a 中引入**

## Libraries

Simulink / Logic and Bit Operations

## Description

The Float Extract Bits block accepts a signal containing floating-point
data and outputs a signal containing the binary representation of the data. For more
information on this binary representation, see the IEEE Standard for Floating Point
Arithmetic.

## Ports

### Input

### **Port\_1** — Signal containing floating-point data scalar | vector | matrix

Signal containing floating-point data, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `half` | `bus`
### Output

### **Port\_1** — Binary representation of data scalar | vector | matrix

Binary representation of data, returned as a scalar, vector, or matrix.
Float Extract Bits calculates the fixed point output based on the **Output
mode** parameter.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Output mode** — Parts of data to output `All bits` (default) | `Range of bits` | `Sign` | `Mantissa` | `Exponent`

Parts of data to output as its binary representation, specified as:

- `All bits`
- `Range of bits`
- `Sign`
- `Mantissa`
- `Exponent`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputMode` |
| **Type**: character vector |
| **Values**: `'All bits'` | `'Range of bits'` | `'Sign'` | `'Mantissa'` | `'Exponent'` |
| **Default**: `'All bits'` |

### **Bit range ([start end], 0-based relative to LSB)** — Range of bits to return `[0 15]` (default) | vector

Range of bits of the signal to return, specified as a vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitRange` |
| **Type**: character vector |
| **Values**: `'[0 15]'` | vector |
| **Default**: `'[0 15]'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `half` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**
