---
type: simulink-block
title: 'To String'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / String'
documentation_page: 'tostring'
documentation_source_path: 'slref/tostring.html'
language: zh-CN
chinese_source: official
---

# To String

## 端口

### 输入

### **Port\_1** — 输入信号 标量

输入信号，指定为标量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 输出字符串 标量

输出字符串，指定为标量。此模块以字符串形式返回输出，用双引号引起来。

- 如果输入为布尔值，则输出为逻辑值（`1` 或 `0`），该模块返回其文本等效值（`true` 或 `false`）。

- 如果输入是数值数据类型，例如整数、单精度数、双精度数或定点数，则模块会以字符串形式返回数字。例如，输入 `1` 将转换为 `"1"`，输入 `0` 将转换为 `"0"`。

  **注意**

  输出字符串可能不包含来自输入端口的数值的所有位数。

**数据类型:** `string`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2018a 中推出**

### R2024b: To String 模块生成更高效的代码

To String 模块现在通过为每种枚举类型生成一个共享函数来为枚举生成更高效的代码。在 R2024b 之前，此模块为枚举生成内联代码。

## 描述

将输入信号转换为字符串信号

To String 模块根据输入信号创建字符串信号。例如，假设使用此信号将逻辑值 `1` 或 `0` 转换为其字符串等效值 `"true"` 或 `"false"`。

To String 模块通过为每种枚举类型生成一个共享函数来为枚举生成高效代码。有关枚举的详细信息，请参阅Simulink 枚举。

如果使用 MinGW® 编译器编译从该模块生成的代码，运行编译后的代码时，针对浮点输入有可能产生非标准结果。例如，数值输入 `501.987` 返回字符串 `"5.019870e+002"`，而不是预期的字符串 `"5.019870e+02"`。
