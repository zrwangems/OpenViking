---
type: simulink-block
title: 'String Compare'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcompare'
documentation_source_path: 'slref/stringcompare.html'
language: zh-CN
chinese_source: worker-translation
---

# String Compare

## 端口

### 输入

### **Port\_1** — 要比较的第一个字符串 标量

要比较的第一个字符串，指定为标量。

**数据类型：** `string`

### **Port\_2** — 要比较的第二个字符串 标量

要比较的第二个字符串，指定为标量。

**数据类型：** `string`
### 输出

### **Port\_1** — 真或假结果 标量

真或假结果，指定为标量：

- `1` — 匹配。
- `0` — 不匹配。

**数据类型：** `Boolean`

## 参数

### **Case sensitive** — 字符串比较的区分大小写 on（默认）| off

字符串比较的区分大小写：

on
:   比较字符串时考虑字符串大小写。

off
:   比较字符串时不考虑字符串大小写。

#### 编程使用

|  |
| --- |
| **模块参数**：`CaseSensitive` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Compare Option** — 要比较的字符数量 `Entire string`（默认）| `First N characters`

要比较的字符串数量：

- `Entire string` — 比较两个完整字符串。
- `First N characters` — 比较两个字符串的前 *`N`* 个字符。

#### 依赖关系

将此参数设置为 `First N
characters` 会启用 **Number of
characters** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`CompareOption` |
| **类型**：character vector |
| **值**：`'Entire string'` | `'First N characters'` |
| **默认值**：`'Entire string'` |

### **Number of characters** — 要比较的字符数量 `1`（默认）| 标量

要比较的字符数量

#### 依赖关系

当 **Compare Option** 参数设置为 `First N
characters` 时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`CompareOption` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'1'` |

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

比较两个输入字符串

String Compare 比较两个字符串。使用此模块可以查看两个字符串是否相同。您可以指定匹配是否区分大小写以及要比较字符串的多少部分。
