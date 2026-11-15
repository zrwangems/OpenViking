---
type: simulink-block
title: 'String Compare'
family: string
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcompare'
---

# String Compare

Compare two input strings

## 中文

比较两个输入字符串

### 所属库

Simulink / String

### 描述

String Compare 比较两个字符串。要查看两个字符串是否相同，请使用此模块。您可以指定匹配是否区分大小写以及要比较其中多少字符。

### 端口

#### 输入

#### **Port\_1** — 要比较的第一个字符串 标量

要比较的第一个字符串，指定为标量。

**数据类型:** `string`

#### **Port\_2** — 要比较的第二个字符串 标量

要比较的第二个字符串，指定为标量。

**数据类型:** `string`
#### 输出

#### **Port\_1** — true 或 false 结果 标量

true 或 false 结果，指定为标量：

- `1` - 匹配。
- `0` - 不匹配。

**数据类型:** `Boolean`

### 参数

#### **区分大小写** — 在字符串比较时区分大小写 on (默认) | off

字符串比较区分大小写：

on
:   比较字符串时考虑字符串的大小写。

off
:   比较字符串时不考虑字符串的大小写。

##### 编程用法

|  |
| --- |
| **模块参数**：`CaseSensitive` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **比较选项** — 要比较的字符量 **整个字符串** (默认) | **前 N 个字符**

要比较的字符量：

- **整个字符串** - 比较整个字符串。
- **前 N 个字符** - 比较两个字符串的前 *`N`* 个字符。

##### 依赖关系

将此参数设置为**前 N 个字符**会启用**字符数**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`CompareOption` |
| **类型：**字符向量 |
| **值**：`'Entire string'` | `'First N characters'` |
| **默认值：**`'Entire string'` |

#### **字符数** — 要比较的字符数 `1` (默认) | 标量

要比较的字符数

##### 依赖关系

当**比较选项**参数设置为**前 N 个字符**时，此参数将启用。

##### 编程用法

|  |
| --- |
| **模块参数**：`CompareOption` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'1'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `string` |
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

String Compare compares two strings. To see if two strings are
identical, use this block. You can specify if the match is case sensitive and how much
of the string to compare.

## Ports

### Input

### **Port\_1** — First string to compare scalar

First string to compare, specified as a scalar.

**Data Types:** `string`

### **Port\_2** — Second string to compare scalar

Second string to compare, specified as a scalar.

**Data Types:** `string`
### Output

### **Port\_1** — True or false result scalar

True or false result, specified as a scalar:

- `1` — Match.
- `0` — No match.

**Data Types:** `Boolean`

## Parameters

### **Case sensitive** — Case sensitivity for string comparison on (default) | off

Case sensitivity for string comparison:

on
:   Consider string case when comparing strings.

off
:   Do not consider string case when comparing strings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CaseSensitive` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Compare Option** — Amount of characters to compare `Entire string` (default) | `First N characters`

Amount of string to compare:

- `Entire string` — Compare both entire
  strings.
- `First N characters` — Compare the first
  *`N`* characters of both strings.

#### Dependencies

Setting this parameter to `First N
characters` enables the **Number of
characters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CompareOption` |
| **Type:** character vector |
| **Values:** `'Entire string'` | `'First N characters'` |
| **Default:** `'Entire string'` |

### **Number of characters** — Number of characters to compare `1` (default) | scalar

Number of characters to compare

#### Dependencies

This parameter is enabled when the **Compare Option**
parameter is set to `First N
characters`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CompareOption` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

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

**Introduced in R2018a**
