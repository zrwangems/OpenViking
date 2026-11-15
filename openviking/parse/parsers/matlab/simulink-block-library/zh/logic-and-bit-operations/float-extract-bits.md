---
type: simulink-block
title: 'Float Extract Bits'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'floatextractbits'
language: zh-CN
chinese_source: worker-translation
---

# Float Extract Bits



从浮点输入样本中提取位

## 库

Simulink / Logic and Bit Operations

## 说明

Float Extract Bits 模块接受包含浮点数据的信号，并输出包含该数据的二进制表示的信号。有关此二进制表示的详细信息，请参阅 IEEE Standard for Floating Point Arithmetic。

## 端口

### 输入

### **Port\_1** — 包含浮点数据的信号 标量 | 向量 | 矩阵

包含浮点数据的信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `half` | `bus`
### 输出

### **Port\_1** — 数据的二进制表示 标量 | 向量 | 矩阵

数据的二进制表示，返回为标量、向量或矩阵。
Float Extract Bits 基于 **输出模式** 参数计算定点输出。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输出模式** — 要输出的数据部分 `All bits`（默认） | `Range of bits` | `Sign` | `Mantissa` | `Exponent`

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

### **位范围 ([start end]，相对于 LSB 从 0 开始)** — 要返回的位范围 `[0 15]`（默认） | vector

要返回的信号的位范围，指定为向量。

#### 编程用法

|  |
| --- |
| **模块参数**：`BitRange` |
| **类型**：character vector |
| **值**：`'[0 15]'` | vector |
| **默认值**：`'[0 15]'` |

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
