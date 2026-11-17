---
type: simulink-block
title: 'String Contains'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcontains'
documentation_source_path: 'slref/stringcontains.html'
language: zh-CN
chinese_source: worker-translation
---

# String Contains

## 端口
```yaml
ports:
- name: str
  summary: 要搜索的字符串 标量
  direction: input
  data_types: string
- name: sub
  summary: 要搜索的字符串模式 标量
  direction: input
  data_types: string
- name: T/F
  summary: 是否检测到字符串模式 1 | 0
  direction: output
  data_types: Boolean
```

### 输入

### **str** — 要搜索的字符串 标量

要在其中搜索模式的字符串，指定为标量。

**数据类型：** `string`

### **sub** — 要搜索的字符串模式 标量

要在字符串中搜索的字符串模式，指定为标量。

**数据类型：** `string`
### 输出

### **T/F** — 是否检测到字符串模式 `1` | `0`

是否检测到字符串模式，返回为已检测到
(`1`) 或未检测到 (`0`)。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Case sensitive
  summary: 区分大小写 on（默认）| off
  group: ''
  block_parameter: CaseSensitive
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Function
  summary: 模式搜索函数 Contains | Starts with | Ends with
  group: ''
  block_parameter: Function
  type: 字符向量
  values: '''Contains'' | ''Starts with'' | ''Ends with'''
  default: String Contains 模块为 'Contains'，String Starts With 模块为 'Starts with'，String Ends With 模块为 'Ends with'
```

### **Case sensitive** — 区分大小写 on（默认）| off

模式检测的大小写敏感性：

on
:   在搜索模式时考虑字符串大小写。

off
:   在搜索模式时不考虑字符串大小写。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CaseSensitive` |
| **类型**：字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Function** — 模式搜索函数 `Contains` | `Starts with` | `Ends with`

模式搜索函数，指定为：

- `Contains`

  在字符串中的任意位置搜索模式。这是
  String Contains 模块的默认值。
- `Starts with`

  仅在字符串的开头搜索模式。这是
  String Starts With 模块的默认值。
- `Ends with`

  仅在字符串的末尾搜索模式。这是
  String Ends With 模块的默认值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Function` |
| **类型**：字符向量 |
| **值：** `'Contains'` | `'Starts with'` | `'Ends with'` |
| **默认值**：String Contains 模块为 `'Contains'`，String Starts With 模块为 `'Starts with'`，String Ends With 模块为 `'Ends with'` |
## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

确定字符串是否包含、开头为或结尾为某个模式

String Contains、String Starts With 和 String
Ends With 模块确定字符串（**str**）是否包含、开头为
或结尾为某个模式（**sub**）。

String Contains、String Starts With 和 String
Ends With 模块是相同的。当 **Function** 设置为
`Contains` 时，模块确定字符串是否包含指定的
模式。当 **Function** 设置为 `Starts with` 时，
模块确定字符串是否开头为指定的模式。当
**Function** 设置为 `Ends with` 时，模块
确定字符串是否结尾为指定的模式。
