---
type: simulink-block
title: 'String to Enum'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringtoenum'
documentation_source_path: 'slref/stringtoenum.html'
language: zh-CN
chinese_source: worker-translation
---

# String to Enum

## 端口

### 输入

### **Port\_1** — 输入字符串信号 标量

输入字符串信号，指定为标量。

**数据类型：** `string`
### 输出

### **Output 1** — 枚举数字 标量

与输入字符串关联的枚举数字，指定为标量。

**数据类型：** `enumerated`

## 参数

### **Output data type** — 输出数据类型 `SlDemoSign`（默认）| `<data type expression>`

使用数据类型对象，例如 `Simulink.IntEnumType`。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Enum: SlDemoSign'` | *`<data type expression>`* |
| **默认值**：`'Enum: SlDemoSign'` |

### **Mode** — 数据类别 `Enumerated`（默认）| `<data type expression>`

使用数据类型对象，例如 `Simulink.IntEnumType`。

- `Enumerated` — 枚举数据类对象。
- `<data type expression>` — 求值为数据类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，您可以在其中输入表达式。

#### 依赖关系

点击 **Show data type assistant** 按钮可启用此参数。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `enumerated` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：String to Enum 模块生成更高效的代码

String to Enum 模块现在通过为每种枚举类型生成一个共享函数，为枚举生成更高效的代码。在 R2025a 之前，此模块为枚举生成内联代码。

## 描述

将输入字符串信号转换为枚举信号

String To Enum 模块将输入字符串信号转换为枚举信号。要使用此模块，请在当前文件夹中创建一个枚举类，并在 **Output data type** 参数中使用该类的名称。

String to Enum 模块通过为每种枚举类型生成一个共享函数，为枚举生成高效的代码。有关枚举的更多信息，请参阅 Simulink Enumerations。
