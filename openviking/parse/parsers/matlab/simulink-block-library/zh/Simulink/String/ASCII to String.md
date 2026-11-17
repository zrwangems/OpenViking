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
chinese_source: worker-translation
---

# ASCII to String

## 端口

### 输入

### **Port\_1** — ASCII 信号向量

ASCII 信号，指定为向量。

在使用动态字符串时，如果输入向量的长度超过配置参数 **Buffer size of dynamically-sized string (bytes)**（默认为 `256`）中指定的字符数，则对于生成的代码，ASCII to String 模块会将字符串输出截断为缓冲区大小减一（例如 `255`）。为避免截断，请增大 **Buffer size of dynamically-sized string (bytes)** 配置参数的值。

**示例：** [088 099]

**数据类型：** `uint8`
### 输出

### **Port\_1** — 转换后的字符串信号标量

从输入 ASCII 信号转换而来的字符串信号，指定为标量。该模块将向量中的每个 ASCII 元素转换为其字母数字等效字符，并将所有元素拼接为一个字符串输出。

**数据类型：** `string`

## 参数

未在 R2025b 中记录。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

Uint8 向量信号转换为字符串信号

ASCII to String 模块将 uint8 向量信号转换为字符串信号。该模块在转换过程中将输入向量中的每个元素视为一个 ASCII 值。例如，该模块将输入向量 `[72 101 108 108 111]` 转换为字符串 `"Hello"`。
