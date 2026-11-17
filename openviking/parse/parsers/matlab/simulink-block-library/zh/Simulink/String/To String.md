---
type: simulink-block
title: 'To String'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'tostring'
documentation_source_path: 'slref/tostring.html'
language: zh-CN
chinese_source: worker-translation
---

# To String

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: Port_1
  summary: 输出字符串 标量
  direction: output
  data_types: string
```

### 输入

### **Port\_1** — 输入信号 标量

输入信号，指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 输出字符串 标量

输出字符串，指定为标量。此模块将输出以双引号括起的字符串形式返回。

- 如果输入为布尔值，则输出为逻辑值
  （`1` 或 `0`），模块
  返回其文本等效形式（`true` 或
  `false`）。

- 如果输入为数值数据类型，例如整数、
  single、double 或定点，则模块将该数字以
  字符串形式返回。例如，输入 `1` 转换为
  `"1"`，输入 `0`
  转换为 `"0"`。

  **注意**

  输出字符串可能不包含输入端口数值的
  所有位数。

**数据类型：** `string`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2018a 中引入**

### R2024b：To String 模块生成更高效的代码

To String 模块现在通过为每种枚举类型生成共享函数，为枚举生成更高效的代码。在 R2024b 之前，此模块为枚举生成内联代码。

## 描述

将输入信号转换为字符串信号

To String 模块从输入信号创建字符串信号。例如，考虑使用此信号将逻辑值 `1` 或
`0` 转换为其字符串等效形式 `"false"` 或
`"true"`。

To String 模块通过为每种枚举类型生成共享函数，为枚举生成高效的代码。有关枚举的详细信息，请参阅 Simulink Enumerations。

当 MinGW® 编译器编译由该模块生成的代码时，运行编译后的代码
可能会对浮点输入产生非标准结果。例如，数值输入
`501.987` 返回字符串 `"5.019870e+002"`
而不是预期的字符串 `"5.019870e+02"`。
