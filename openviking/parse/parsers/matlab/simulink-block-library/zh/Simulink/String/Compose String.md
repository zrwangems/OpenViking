---
type: simulink-block
title: 'Compose String'
family: 'string'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'composestring'
documentation_source_path: 'slref/composestring.html'
language: zh-CN
chinese_source: worker-translation
---

# Compose String

## 端口

### 输入

### **d** — 字符串标量第一部分的数据

字符串第一部分的数据，指定为标量。**Format** 参数决定端口标签和输入数据的格式。例如，如果 **Format** 参数中的第一项为 `%d`，则端口标签为 d。

输入信号的数据类型必须与 **Format** 参数中的格式说明符兼容。有关详细信息，请参阅 **Format** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **f** — 字符串标量第二部分的数据

字符串第二部分的数据，指定为标量。**Format** 参数决定端口标签和输入数据的格式。例如，如果 **Format** 参数中的第一项为 `%f`，则端口标签为 f。

输入信号的数据类型必须与 **Format** 参数中指定的格式说明符兼容。有关详细信息，请参阅 **Format** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — N 部分字符串标量的数据（默认）

*`N`* 部分字符串的数据，指定为标量。**Format** 参数决定端口标签和输入数据的格式。例如，如果 **Format** 参数中的对应项为 `%f`，则端口标签为 f。

输入信号的数据类型必须与 **Format** 参数中的格式说明符兼容。有关详细信息，请参阅 **Format** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 输出

### **str** — 输出字符串标量

由输入组成的输出字符串，指定为标量。

**数据类型：** `string`

## 参数

### **Format** — 格式化输入数据 "%d %f"（默认） | 格式字符串 | character vector

输入数据的格式，指定为格式字符串。

有关可接受的格式说明符的详细信息，请参阅算法。

#### 编程用法

|  |
| --- |
| **模块参数：** `Format` |
| **类型：** character vector |
| **值：** `'<filename>'` |
| **默认值：** `'"%d %f"'` |

### **输出数据类型** — 输出数据类型 `string`（默认） | `<data type expression>`

输出数据类型，使用字符串数据类型指定无最大长度的字符串。

要指定具有最大长度的字符串数据类型，请指定 `stringtype(N)`。例如，`stringtype(31)` 创建一个最大长度为 31 个字符的字符串数据类型。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `'string'` | *`<data type expression>`* |
| **默认值：** `'string'` |

### **Mode** — 数据的类别 `string`（默认） | `scalar`

使用 `stringtype` 函数，例如 `stringtype(255)`。

#### 依赖关系

点击 **显示数据类型助手** 按钮会启用此参数。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

基于指定的格式和输入信号组合输出字符串信号

Compose String 模块基于 **Format** 参数中列出的格式说明符组合输出字符串信号。**Format** 参数决定输入信号的数量。如果有多个输入，该模块按顺序组合这些多个输入，并应用关联的格式说明符，每个输入对应一个格式说明符，从而构造字符串。每个格式说明符以百分号 `%` 开头，后跟转换字符。例如，`%f` 将输入格式化为浮点输出。为了补充字符串输出，您还可以向格式规范中添加字符。使用此模块从多个输入组合并格式化输出字符串信号。

例如，如果 **Format** 参数包含 `"%s is
%f"`，则该模块需要两个输入：一个字符串信号和一个 single 或 double 信号。如果第一个输入是字符串 `"Pi"`，第二个输入是 double 值 `3.14`，则输出为 `"Pi is
3.14"`。

当 MinGW® 编译器编译从该模块生成的代码时，运行编译后的代码可能会对浮点输入产生非标准结果。例如，数值输入 `501.987` 会返回字符串 `"5.019870e+002"`，而不是预期的字符串 `"5.019870e+02"`。
