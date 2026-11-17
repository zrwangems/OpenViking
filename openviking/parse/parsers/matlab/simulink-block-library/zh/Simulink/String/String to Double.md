---
type: simulink-block
title: 'String to Double'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringtodouble'
documentation_source_path: 'slref/stringtodouble.html'
language: zh-CN
chinese_source: worker-translation
---

# String to Double

## 端口

### 输入

### **Port\_1** — 输入字符串标量

输入字符串，指定为标量。

**数据类型：** `string`
### 输出

### **d** — 格式与 `%d` 格式匹配的输出数据标量

格式与指定格式匹配的输出数据，定义为标量。最大输出总数为 128。

如果模块无法将输入字符串与 **Format** 中指定的格式运算符匹配，则返回警告，并为每个未匹配的格式运算符输出适当的值（`0` 或 `""`）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **f** — 格式与 %f 格式匹配的输出数据标量

格式与 `%f` 格式匹配的输出数据，指定为标量。最大输出总数为 128。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — 格式与 N 格式匹配的输出数据标量

格式与 *`N`* 格式匹配的输出数据，指定为标量。最大输出总数为 128。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Format** — 输入的格式运算符 `"%lf"`（默认）| 格式字符串 | 字符向量

输入的格式运算符，指定为标量。如果模块无法将输入字符串与指定格式匹配，则返回 `0`。返回 `0` 与 `sscanf` 函数的返回值不同，如果该函数无法将输入与指定格式匹配，则返回空矩阵。

- 对于 String to Double 模块，此参数的默认值为 `%lf`。
- 对于 String to Single 模块，此参数的默认值为 `%f`。

有关可接受的格式运算符的详细信息，请参阅算法部分。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Format` |
| **类型：** 字符向量 |
| **值：** `'<filename>'` |
| **默认值：** 如果模块为 String to Double，则为 `'"%lf"'`；如果模块为 String to Single，则为 `'"%f"'` |

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

将字符串信号转换为双精度信号

Scan String 扫描输入字符串，并根据 **Format** 参数指定的格式将其转换为信号。该模块将值转换为其十进制（基数为 10）表示形式，并将结果输出为数值或字符串信号。例如，如果 **Format** 参数设置为 `"%s is %f."`，则该模块输出两部分：一个字符串信号和一个单精度信号。如果输入为字符串 `"Pi is 3.14"`，则两个输出分别为 `"Pi"` 和 `"3.14"`。

Scan String、String to Double 和 String to Single 模块是相同的模块。当配置为 String to Double 时，该模块将输入字符串信号转换为双精度数值输出。当配置为 String to Single 时，该模块将输入字符串信号转换为单精度数值输出。

对于代码生成，请通过选中 **Configuration Parameters** > **Code Generation** > **Interface** > **Support non-finite numbers** 复选框，为包含此模块的模型配置非有限数支持。
