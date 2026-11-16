---
type: simulink-block
title: 'Float Extract Bits'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'floatextractbits'
documentation_source_path: 'slref/floatextractbits.html'
language: zh-CN
chinese_source: worker-translation
---

# Float Extract Bits

## 端口

### 输入

### **Port\_1** — 包含浮点数据的信号 标量 | 向量 | 矩阵

包含浮点数据的信号，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `half` | `bus`
### 输出

### **Port\_1** — 数据的二进制表示 标量 | 向量 | 矩阵

数据的二进制表示，以标量、向量或矩阵形式返回。
Float Extract Bits 基于 **输出模式** 参数计算 fixed point 输出。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输出模式** — 要输出的数据部分 `All bits`（默认） | `Range of bits` | `Sign` | `Mantissa` | `Exponent`

要作为其二进制表示形式输出的数据部分，指定为：

- `All bits`
- `Range of bits`
- `Sign`
- `Mantissa`
- `Exponent`

#### 程序化使用

|  |
| --- |
| **模块参数**: `OutputMode` |
| **类型**: character vector |
| **值**: `'All bits'` | `'Range of bits'` | `'Sign'` | `'Mantissa'` | `'Exponent'` |
| **默认值**: `'All bits'` |

### **位范围 ([start end]，相对于 LSB 从 0 开始)** — 要返回的位范围 `[0 15]`（默认） | 向量

要返回的信号的位范围，指定为向量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `BitRange` |
| **类型**: character vector |
| **值**: `'[0 15]'` | 向量 |
| **默认值**: `'[0 15]'` |

## 所属库

Simulink / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

从浮点输入样本中提取位

Float Extract Bits 模块接受包含浮点数据的信号，并输出包含该数据二进制表示形式的信号。有关此二进制表示形式的详细信息，请参阅 IEEE Standard for Floating Point Arithmetic。
