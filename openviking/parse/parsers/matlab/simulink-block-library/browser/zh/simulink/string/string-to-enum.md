---
type: simulink-block
title: 'String to Enum'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / String'
documentation_page: 'stringtoenum'
documentation_source_path: 'slref/stringtoenum.html'
language: zh-CN
chinese_source: official
---

# String to Enum

## 端口

### 输入

### **Port\_1** — 输入字符串信号 标量

输入字符串信号，指定为标量。

**数据类型:** `string`
### 输出

### **Output 1** — 枚举编号 标量

与输入字符串关联的枚举编号，指定为标量。

**数据类型:** `enumerated`

## 参数

### **输出数据类型** — 输出数据类型 `SlDemoSign` (默认) | `<data type expression>`

使用数据类型对象，例如 `Simulink.IntEnumType`。

点击**显示数据类型助手**按钮  以显示**数据类型助手**，帮助您设置数据类型属性。有关详细信息，请参阅 。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Enum: SlDemoSign'` | *`<data type expression>`* |
| **默认值**：`'Enum: SlDemoSign'` |

### **模式** — 数据类别 `Enumerated` (默认) | `<data type expression>`

使用数据类型对象，例如 `Simulink.IntEnumType`。

- **枚举** - 枚举数据类对象。
- **<数据类型表达式>** - 计算结果为数据类型的表达式。选择 `Expression` 将在右侧启用另一个菜单/文本框，您可以在其中输入表达式。

#### 依赖关系

点击**显示数据类型助手**按钮将启用此参数。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `enumerated` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

### R2024b: String to Enum 模块生成更高效的代码

String to Enum 模块现在通过为每种枚举类型生成一个共享函数来为枚举生成更高效的代码。在 R2025a 之前，此模块为枚举生成内联代码。

## 描述

输入字符串信号转换为枚举信号

String To Enum 模块将输入字符串信号转换为枚举信号。要使用此模块，请在当前文件夹中创建一个枚举类，并在**输出数据类型**参数中使用该类名称。

String to Enum 模块通过为每种枚举类型生成一个共享函数来为枚举生成高效代码。有关枚举的详细信息，请参阅Simulink 枚举。
