---
type: simulink-block
title: 'String to ASCII'
family: string
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringtoascii'
---

# String to ASCII

Convert string signal to uint8 vector

## 中文

将字符串信号转换为 uint8 向量

### 所属库

Simulink / String

### 描述

String To ASCII 模块将字符串信号转换为 uint8 向量。该模块将字符串中的每个字符转换为其对应的 ASCII 值。例如，该模块将输入字符串 `"Hello"` 转换为 `[72 101 108 108 111]`。

### 端口

#### 输入

#### **Port\_1** — 输入字符串信号 标量

输入字符串信号，指定为标量。

**数据类型:** `string`
#### 输出

#### **Port\_1** — 转换后的 uint8 向量信号 向量 | *N* 元素的一维向量

从输入字符串信号转换 ASCII 字符的 `uint8` 向量信号，指定为向量。该模块将字符串中的每个元素转换为其 ASCII 字符等效项，并将 ASCII 等效项作为向量输出。如果字符数少于最大长度，模块在仿真时用零填充剩余空间。在代码生成时，模块用空字符填充剩余空间。

**数据类型:** `uint8`

### 参数

#### **输出向量大小** — 输出向量大小 31 (默认) | 标量

输出字符串向量的大小，指定为标量。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputVectorSize` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'31'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2018a 中推出**

#### R2024b: String to ASCII 模块输出维度变化

String to ASCII 模块输出维度已从 2D 行向量（例如 2×*N* 向量）更改为 1D 向量 *N*。*N* 是元素的数量。

## Libraries

Simulink / String

## Description

The String To ASCII block converts a string signal to a uint8 vector. The
block converts each character in the string to its corresponding ASCII value. For
example, the block converts the input string `"Hello"` to `[72
101 108 108 111]`.

## Ports

### Input

### **Port\_1** — Input string signal scalar

Input string signal, specified as a scalar.

**Data Types:** `string`
### Output

### **Port\_1** — Converted uint8 vector signal vector | 1D vector of *N* elements

Converted `uint8` vector signal of ASCII characters from input string
signal, specified as a vector. The block converts each element in the
string into its ASCII character equivalent and outputs the ASCII
equivalents as a vector. If there are fewer characters than the maximum
length, the block fills the remaining space with zeros at simulation. At
code generation, the block fills the remaining space with null
characters.

**Data Types:** `uint8`

## Parameters

### **Output vector size** — Size of output vector 31 (default) | scalar

Size of output string vector, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputVectorSize` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'31'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: String to ASCII block output dimension change

The String to
ASCII block output dimension has changed from a 2D row vector, such as a
2-by-*N* vector, to a 1D vector, *N*.
*N* is the number of elements.
