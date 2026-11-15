---
type: simulink-block
title: 'String Count'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcount'
language: zh-CN
chinese_source: worker-translation
---

# String Count

## 端口

### 输入

### **str** — 要搜索的字符串 标量

要在其中搜索模式的字符串，指定为标量。

**数据类型：** `string`

### **sub** — 要搜索的字符串模式 标量

要在字符串中搜索的字符串模式，指定为标量。

**数据类型：** `string`

### 输出

### **n** — 在字符串中找到模式的次数 标量

在字符串 `str` 中找到字符串模式的次数，以标量形式返回。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

### **区分大小写** — 大小写敏感度 on（默认）| off

字符串计数的区分大小写设置：

on
:   在统计找到的字符串时考虑字符串大小写。

off
:   在统计找到的字符串时不考虑字符串大小写。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CaseSensitive` |
| **类型**：character vector |
| **值：** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **输出数据类型** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `<data type expression>`

输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择继承选项时，模块会表现出以下行为：

- `Inherit: Inherit via internal rule` — Simulink® 选择一种数据类型，以在数值精度、性能和生成代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。

单击显示数据类型助手按钮  以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | *`<data type expression>`* |
| **默认值：** `'Inherit: Inherit via internal rule'` |

### **模式** — 数据类型类别 `Inherit`（默认）| `Built in` | `Expression`

数据类型类别，指定为 `Inherit`、`Built in` 或 `Expression`。有关使用此参数的详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

单击 **显示数据类型助手** 按钮会启用此参数。

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

**在 R2020a 中引入**

## 描述

统计字符串中模式的出现次数

String Count 模块统计模式（**sub**）在字符串（**str**）中的出现次数。如果 **sub** 处的输入与 **str** 处输入的一部分或全部匹配，模块将该出现次数计为 1。
