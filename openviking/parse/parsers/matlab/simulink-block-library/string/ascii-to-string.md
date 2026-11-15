---
type: simulink-block
title: 'ASCII to String'
family: string
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'String'
documentation_page: 'asciitostring'
---

# ASCII to String

Uint8 vector signal to string signal

## 中文

Uint8 向量信号转换为字符串信号

### 所属库

Simulink / String

### 描述

ASCII to String 模块将 uint8 向量信号转换为字符串信号。在转换过程中，该模块将输入向量中的每个元素视为一个 ASCII 值。例如，该模块将输入向量 `[72 101 108 108 111]` 转换为字符串 `"Hello"`。

### 端口

#### 输入

#### **Port\_1** — ASCII 信号 向量

ASCII 信号，指定为向量。

使用动态字符串时，如果输入向量的长度超出配置参数**动态大小字符串的缓冲区大小(以字节为单位)** 中指定的字符数（默认值为 `256`），则对于生成的代码，ASCII to String 模块会将字符串输出截断到缓冲区大小-1（例如 `255`）。要避免截断，请增大**动态大小字符串的缓冲区大小(以字节为单位)** 配置参数的值。

**示例:**  [088 099]

**数据类型:** `uint8`
#### 输出

#### **Port\_1** — 转换后的字符串信号 标量

从输入 ASCII 信号转换的字符串信号，指定为标量。该模块将向量中的每个 ASCII 元素转换为其字母数字等效项，并将所有元素串联成一个字符串进行输出。

**数据类型:** `string`

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

## Libraries

Simulink / String

## Description

The ASCII to String block converts uint8 vector signals to string
signals. The block treats each element in the input vector as an ASCII value during the
conversion. For example, the block converts an input vector of `[72 101 108 108
111]` to the string `"Hello"`.

## Ports

### Input

### **Port\_1** — ASCII signal vector

ASCII signal, specified as a vector.

While using dynamic strings, if the length of the input vector exceeds
the number of characters specified in the configuration parameter
**Buffer size of dynamically-sized string (bytes)**
(`256` by default), the ASCII to
String block truncates the string output to the buffer
size-1 (for example, `255`), for generated code. To
avoid truncation, increase the value of the **Buffer size of
dynamically-sized string (bytes)** configuration
parameter.

**Example:**  [088 099]

**Data Types:** `uint8`
### Output

### **Port\_1** — Converted string signal scalar

Converted string signal from input ASCII signal, specified as a
scalar. The block converts each ASCII element in the vector into its
alphanumeric equivalent and outputs all elements concatenated into one
string.

**Data Types:** `string`

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
