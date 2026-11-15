---
type: simulink-block
title: 'To String'
family: string
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'String'
documentation_page: 'tostring'
---

# To String

Convert input signal to string signal

## 中文

将输入信号转换为字符串信号

### 所属库

Simulink / String

### 描述

To String 模块根据输入信号创建字符串信号。例如，假设使用此信号将逻辑值 `1` 或 `0` 转换为其字符串等效值 `"true"` 或 `"false"`。

To String 模块通过为每种枚举类型生成一个共享函数来为枚举生成高效代码。有关枚举的详细信息，请参阅Simulink 枚举。

如果使用 MinGW® 编译器编译从该模块生成的代码，运行编译后的代码时，针对浮点输入有可能产生非标准结果。例如，数值输入 `501.987` 返回字符串 `"5.019870e+002"`，而不是预期的字符串 `"5.019870e+02"`。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量

输入信号，指定为标量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
#### 输出

#### **Port\_1** — 输出字符串 标量

输出字符串，指定为标量。此模块以字符串形式返回输出，用双引号引起来。

- 如果输入为布尔值，则输出为逻辑值（`1` 或 `0`），该模块返回其文本等效值（`true` 或 `false`）。

- 如果输入是数值数据类型，例如整数、单精度数、双精度数或定点数，则模块会以字符串形式返回数字。例如，输入 `1` 将转换为 `"1"`，输入 `0` 将转换为 `"0"`。

  **注意**

  输出字符串可能不包含来自输入端口的数值的所有位数。

**数据类型:** `string`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2018a 中推出**

#### R2024b: To String 模块生成更高效的代码

To String 模块现在通过为每种枚举类型生成一个共享函数来为枚举生成更高效的代码。在 R2024b 之前，此模块为枚举生成内联代码。

## Libraries

Simulink / String

## Description

The To String block creates a string signal from an input signal. For
example, consider using this signal to convert a logical value `1` or
`0` to its string equivalent `"false"` or
`"true"`.

The To String block generates efficient code for enumerations by generating a shared
function for each enumeration type. For more information on enumerations, see Simulink Enumerations.

When a MinGW® compiler compiles code generated from the block, running the compiled code
may produce nonstandard results for floating-point inputs. For example, a numeric input
of `501.987` returns the string `"5.019870e+002"`
instead of the expected string `"5.019870e+02"`.

## Ports

### Input

### **Port\_1** — Input signal scalar

Input signal, specified as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Output string scalar

Output string, specified as a scalar. This block returns the output as
a string, surrounded by double quotes.

- If the input is a Boolean, the output is a logical value
  (`1` or `0`) and the block
  returns its textual equivalent (`true` or
  `false`).

- If the input is a numeric data type, such as an integer,
  single, double, or fixed point, the block returns the number as
  a string. For example, an input of `1` converts
  to `"1"` and an input of `0`
  converts to `"0"`.

  **Note**

  The output string might not contain all the digits of the
  numeric value from the input port.

**Data Types:** `string`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2018a**

### R2024b: To String block generates more efficient code

The To String block now generates more efficient code for enumerations by
generating a shared function for each enumeration type. Prior to R2024b, this block
generated inlined code for enumerations.
