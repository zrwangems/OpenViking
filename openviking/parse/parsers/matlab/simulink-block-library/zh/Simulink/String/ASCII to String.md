---
type: simulink-block
title: 'ASCII to String'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'asciitostring'
documentation_source_path: 'slref/asciitostring.html'
language: zh-CN
chinese_source: official
---

# ASCII to String

## 端口

### 输入

### **Port\_1** — ASCII 信号 向量

ASCII 信号，指定为向量。

使用动态字符串时，如果输入向量的长度超出配置参数**动态大小字符串的缓冲区大小(以字节为单位)** 中指定的字符数（默认值为 `256`），则对于生成的代码，ASCII to String 模块会将字符串输出截断到缓冲区大小-1（例如 `255`）。要避免截断，请增大**动态大小字符串的缓冲区大小(以字节为单位)** 配置参数的值。

**示例:**  [088 099]

**数据类型:** `uint8`
### 输出

### **Port\_1** — 转换后的字符串信号 标量

从输入 ASCII 信号转换的字符串信号，指定为标量。该模块将向量中的每个 ASCII 元素转换为其字母数字等效项，并将所有元素串联成一个字符串进行输出。

**数据类型:** `string`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

Uint8 向量信号转换为字符串信号

ASCII to String 模块将 uint8 向量信号转换为字符串信号。在转换过程中，该模块将输入向量中的每个元素视为一个 ASCII 值。例如，该模块将输入向量 `[72 101 108 108 111]` 转换为字符串 `"Hello"`。
