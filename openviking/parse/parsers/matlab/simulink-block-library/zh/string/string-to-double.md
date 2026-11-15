---
type: simulink-block
title: 'String to Double'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringtodouble'
language: zh-CN
chinese_source: official
---

# String to Double

## 端口

### 输入

### **Port\_1** — 输入字符串 标量

输入字符串，指定为标量。

**数据类型:** `string`
### 输出

### **d** — 格式与 `%d` 格式匹配的输出数据 标量

格式与指定格式匹配的输出数据，定义为标量。输出总数最大为 128。

如果模块不能将输入字符串与**格式**中指定的格式化操作符匹配，则会返回警告，并为每个不匹配的格式化操作符输出适当的值（`0` 或 `""`）。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **f** — 格式与 %f 格式匹配的输出数据 标量

格式与 `%f` 格式匹配的输出数据，指定为标量。输出总数最大为 128。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — 格式与 N 格式匹配的输出数据 标量

格式与 *`N`* 格式匹配的输出数据，指定为标量。输出总数最大为 128。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **格式** — 输入的格式化操作符 `"%lf"` (默认) | 格式字符串 | 字符向量

输入的格式化操作符，指定为标量。如果模块不能使输入字符串与指定格式匹配，则返回 `0`。该返回值 `0` 与 `sscanf` 函数的返回值不同，对于后者，如果函数不能使输入与指定格式匹配，它返回的是空矩阵。

- 对于 String to Double 模块，此参数的默认值为 `%lf`。
- 对于 String to Single 模块，此参数的默认值为 `%f`。

有关可接受的格式化操作符的详细信息，请参阅“算法”部分。

#### 编程用法

|  |
| --- |
| **模块参数**：`Format` |
| **类型：**字符向量 |
| **值：**`'<filename>'` |
| **默认值：**如果模块是 String to Double，则为 `'"%lf"'`；如果模块是 String to Single，则为 `'"%f"'` |

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

将字符串信号转换为双精度信号。

Scan String 扫描输入字符串并将其转换为符合**格式**参数指定格式的信号。该模块将值转换为其十进制（以 10 为基数）表示，并将结果作为数值或字符串信号输出。例如，如果**格式**参数设置为 `"%s is %f."`，则模块输出两个部分，即一个字符串信号和一个单精度信号。如果输入为字符串 `"Pi is 3.14"`，则两个输出为 `"Pi"` 和 `"3.14"`。

Scan String、String to Double 和 String to Single 模块是相同的模块。为 String to Double 配置时，模块将输入字符串信号转换为双精度数值输出。为 String to Single 配置时，模块将输入字符串信号转换为单精度数值输出。

对于代码生成，通过选中**配置参数** > **代码生成** > **接口** > **支持非有限数**复选框来配置包含此模块的模型，以支持非有限数。
