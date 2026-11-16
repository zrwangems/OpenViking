---
type: simulink-block
title: 'ASCII Decode'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'asciidecode'
documentation_source_path: 'io_ref/asciidecode.html'
language: zh-CN
chinese_source: official
---

# ASCII Decode

## 端口

### 输入

### **D** — 待解析的输入向量 `character vector`

输入向量可以是 8 位或 16 位，且可以是有符号或无符号的。如果数据格式为 16 位，则该模块会忽略每个条目的高 8 位。

**数据类型:** `int8` | `uint8` | `int16` | `uint16`
### 输出

### **1** — 发送 Simulink® 值的编号端口 数值

与 **Format string** 中的项目相对应的输出端口。

#### 依赖关系

**Number of variables** 决定输出端口数量。

**数据类型:** `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

### **Format string** — 用于解析输入向量的格式指定符 `%d\r` (默认) | `%c` | `%i` | `%o` | `%u` | `%x` | `%e` | `%f` | `%g`

输入类似 `scanf` 的格式字符串。每个格式指定符（如 `%d`）都必须与输入向量的对应部分匹配。该格式的字符串必须匹配第一个字符加上指定的字符数。格式指定符遵循 `scanf` 的常规描述。

格式字符串示例如下：

```
'alpha %d bravo %f\n'
```

#### 编程用法

|  |
| --- |
| **模块参数：**`format` |

### **Number of variables** — 此模块的输出端口数量 `1` (默认) | 整数

输入此模块的输出端口数量。例如：

如果 **Format string** 的值为 `%xmore text%x`，且该模块的输入向量包含 `cdmabcdefgh90`，则必须将 **Number of variables** 参数的值设为 2。

第一个变量被赋值为 `0xcd`。接下来，字符向量 `mabcdefgh` 被视为与 `more text` 匹配，因为：

- 两个字符向量的第一个字符均为 `m`。
- 两个字符向量都具有相同数量的字符。

第二个变量随后被赋值为 `0x90`。字符向量 `mabcdefgh` 无需与 **Format string** 的值完全匹配。这种行为与 `scanf` 的行为不同，后者要求精确匹配。

#### 编程用法

|  |
| --- |
| **模块参数：**`nvars` |

### **Variable types** — Simulink 输出端口允许的数据类型 `{'double'}` (默认) | `{'int8'}` | `{'uint8'}` | `{'int16}` | `{'uint16'}` | `{'int32'}` | `{'uint32'}`

具有与 **Number of variables** 中指定元素数相同的单元向量，可为每个输出端口指定不同的数据类型。单个元素被复制。例如：

```
nvars=3
```

`{ }` - 这三个输出都是双精度数值。

`{'uint8'}` - 这三个输出是 `uint8`。

`{'uint16', 'double', 'uint8'}` - 第一个输出是 `uint16`，第二个输出是 `double`，第三个输出是 `uint8`。

#### 编程用法

|  |
| --- |
| **模块参数：**`varids` |

## 所属库

Simulink Real-Time / RS232

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

将 ASCII 字符向量解析为 Simulink 值

ASCII Decode 模块根据类似于 `scanf` 的格式指定符解析输入字符向量，并将转换后的值提供给实时应用程序。

有关详细信息，请参阅RS-232 串行通信和RS-232 Legacy Drivers。
