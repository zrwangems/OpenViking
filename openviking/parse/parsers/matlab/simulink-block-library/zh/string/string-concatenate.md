---
type: simulink-block
title: 'String Concatenate'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringconcatenate'
language: zh-CN
chinese_source: official
---

# String Concatenate

串联各个输入字符串以形成一个输出字符串。

## 所属库

Simulink / String

## 描述

String Concatenate 模块按输入顺序串联多个输入字符串，以形成一个输出字符串。如果要将多个字符串组合为单个字符串，请使用此模块。

## 端口

### 输入

### **Port\_1** — 第一个输入字符串 标量

第一个输入字符串，指定为标量。

**数据类型:** `string`

### **Port\_2** — 第二个输入字符串 标量

第二个输入字符串，指定为标量。

**数据类型:** `string`
### 输出

### **Port\_1** — 串联的字符串 标量

串联的字符串，指定为标量。

**数据类型:** `string`

## 参数

### **输入数目** — 输入字符串的个数 标量

要串联的输入字符串的数目，指定为标量。您可以指定 2 到 512 个输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型：**字符向量 |
| **值：**从 `2` 到 `512` 的标量 |
| **默认值：**`'2'` |

### **输出数据类型** — 输出数据类型 `string` (默认) | **<数据类型表达式>** | 标量

输出数据类型，指定为不设最大长度限制的字符串数据类型。

要指定具有最大长度的字符串数据类型，请指定 `stringtype(N)`。例如，`stringtype(128)` 创建一个最大长度为 128 个字符的字符串数据类型。

点击**显示数据类型助手**按钮  以显示**数据类型助手**，帮助您设置数据类型属性。有关详细信息，请参阅 。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值**：`'string'` | *`<data type expression>`* |
| **默认值：**`'string'` |

### **模式** — 数据类别 `stringtype(128)` (默认) | `scalar`

使用 `stringtype` 函数，例如 `stringtype(128)`。

#### 依赖关系

点击**显示数据类型助手**按钮将启用此参数。

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史记录

**在 R2018a 中推出**
