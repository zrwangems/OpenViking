---
type: simulink-block
title: 'String Contains'
family: string
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcontains'
---

# String Contains

Determine if string contains, starts with, or ends with pattern

## 中文

确定字符串是否包含模式、以模式开头或以模式结尾

### 库

Simulink / String

### 描述

String Contains、String Starts With 和 String Ends With 模块确定字符串（**str**）是否包含模式（**sub**）、以模式（**sub**）开头或以模式（**sub**）结尾。

String Contains、String Starts With 和 String Ends With 模块完全相同。当 **Function** 设置为 `Contains` 时，模块确定字符串是否包含指定模式。当 **Function** 设置为 `Starts with` 时，模块确定字符串是否以指定模式开头。当 **Function** 设置为 `Ends with` 时，模块确定字符串是否以指定模式结尾。

### 端口

#### 输入

#### **str** — 要搜索的字符串 标量

要在其中搜索模式的字符串，指定为标量。

**数据类型：** `string`

#### **sub** — 要搜索的字符串模式 标量

要在字符串中搜索的字符串模式，指定为标量。

**数据类型：** `string`
#### 输出

#### **T/F** — 检测到字符串模式 `1` | `0`

是否检测到字符串模式，返回为检测到（`1`）或未检测到（`0`）。

**数据类型：** `Boolean`

### 参数

#### **Case sensitive** — 区分大小写 on（默认）| off

模式检测的大小写敏感性：

on
:   搜索模式时考虑字符串大小写。

off
:   搜索模式时不考虑字符串大小写。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CaseSensitive` |
| **类型**：character vector |
| **值：** `'on'` | `'off'` |
| **默认值**：`'on'` |

#### **Function** — 模式搜索函数 `Contains` | `Starts with` | `Ends with`

模式搜索函数，指定为：

- `Contains`

  搜索字符串中任意位置处的模式。这是 String Contains 模块的默认值。
- `Starts with`

  仅在字符串开头搜索模式。这是 String Starts With 模块的默认值。
- `Ends with`

  仅在字符串结尾搜索模式。这是 String Ends With 模块的默认值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Function` |
| **类型**：character vector |
| **值：** `'Contains'` | `'Starts with'` | `'Ends with'` |
| **默认值**：`'Contains'` 适用于 String Contains 模块，`'Starts with'` 适用于 String Starts With 模块，`'Ends with'` 适用于 String Ends With 模块 |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 版本历史

**在 R2020a 中引入**

## Libraries

Simulink / String

## Description

The String Contains, String Starts With, and String
Ends With blocks determine if a string (**str**) contains, starts
with, or ends with a pattern (**sub**).

The String Contains, String Starts With, and String
Ends With blocks are identical. When **Function** is set to
`Contains`, the block determines if the string contains a specified
pattern. When **Function** is set to `Starts with`,
the block determines if the string starts with a specified pattern. When
**Function** is set to `Ends with`, the block
determines if the string ends with a specified pattern.

## Ports

### Input

### **str** — String to search scalar

String to search for the pattern in, specified as a scalar.

**Data Types:** `string`

### **sub** — String pattern to search for scalar

String pattern to search for in string, specified as a scalar.

**Data Types:** `string`
### Output

### **T/F** — String pattern detected `1` | `0`

Whether the string pattern was detected, returned as detected
(`1`) or not detected (`0`).

**Data Types:** `Boolean`

## Parameters

### **Case sensitive** — Case sensitivity on (default) | off

Case sensitivity for the pattern detection:

on
:   Consider string case when searching for the pattern.

off
:   Do not consider string case when searching for the pattern.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CaseSensitive` |
| **Type**: character vector |
| **Values:** `'on'` | `'off'` |
| **Default**: `'on'` |

### **Function** — Pattern search function `Contains` | `Starts with` | `Ends with`

Pattern search function, specified as:

- `Contains`

  Search for the pattern anywhere in the string. This is the default for the
  String Contains block.
- `Starts with`

  Search for the pattern only at the beginning of the string. This is the default
  for the String Starts With block.
- `Ends with`

  Search for the pattern only at the end of the string. This is the default for
  the String Ends With block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Function` |
| **Type**: character vector |
| **Values:** `'Contains'` | `'Starts with'` | `'Ends with'` |
| **Default**: `'Contains'` for String Contains block, `'Starts with'` for String Starts With block, `'Ends with'` for String Ends With block |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**
