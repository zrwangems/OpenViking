---
type: simulink-block
title: 'ASCII Decode'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'asciidecode'
documentation_source_path: 'io_ref/asciidecode.html'
language: zh-CN
chinese_source: worker-translation
---

# ASCII Decode

## 端口
```yaml
ports:
- name: D
  summary: 要解析的输入向量 character vector
  direction: input
  data_types: int8 | uint8 | int16 | uint16
- name: '1'
  summary: 发送 Simulink® 数值的编号端口 numeric
  direction: output
  data_types: double | int8 | uint8 | int16 | uint16 | int32 | uint32
```

### 输入

### **D** — 要解析的输入向量 `character vector`

输入向量可以是 8 位或 16 位，也可以是有符号或无符号的。
如果数据格式为 16 位，该模块会忽略每个条目的高 8 位。

**数据类型：** `int8` | `uint8` | `int16` | `uint16`
### 输出

### **1** — 发送 Simulink® 数值的编号端口 numeric

与 **Format string** 中的项对应的输出端口。

#### 依赖关系

**Number of variables** 决定输出端口的数量。

**数据类型：** `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
## 参数
```yaml
parameters:
- name: Format string
  summary: 用于解析输入向量的格式说明符 %d\r （默认） | %c | %i | %o | %u | %x | %e | %f | %g
  group: ''
  block_parameter: format
- name: Number of variables
  summary: 此模块的输出端口数量 1 （默认） | 整数
  group: ''
  block_parameter: nvars
- name: Variable types
  summary: 输出端口允许的 Simulink 数据类型 {'double'} （默认） | {'int8'} | {'uint8'} | {'int16} | {'uint16'} | {'int32'} | {'uint32'}
  group: ''
  block_parameter: varids
```

### **Format string** — 用于解析输入向量的格式说明符 `%d\r` （默认） | `%c` | `%i` | `%o` | `%u` | `%x` | `%e` | `%f` | `%g`

输入一个类似 `scanf` 的格式字符串。每个格式说明符（例如 `%d`）必须与输入向量的对应部分匹配。格式中的字面字符串必须匹配第一个字符加上字符数。格式说明符遵循 `scanf` 的常规描述。

一个示例格式字符串是：

```
'alpha %d bravo %f\n'
```

#### 编程用法

|  |
| --- |
| **模块参数：** `format` |

### **Number of variables** — 此模块的输出端口数量 `1` （默认） | 整数

输入此模块的输出端口数量。例如：

如果 **Format string** 的值为 `%xmore
text%x`，并且该模块的输入向量为
`cdmabcdefgh90`，则必须将
**Number of variables** 参数的值指定为 2。

第一个变量被赋值为 `0xcd`。接下来，
字符向量 `mabcdefgh` 被认为与
`more text` 匹配，因为：

- 两个字符向量的第一个字符都是
  `m`。
- 两个字符向量具有相同数量的字符。

然后第二个变量被赋值为 `0x90`。
字符向量 `mabcdefgh` 不必与 **Format string** 的值完全匹配。此行为
与 `scanf` 的行为不同，后者要求完全匹配。

#### 编程用法

|  |
| --- |
| **模块参数：** `nvars` |

### **Variable types** — 输出端口允许的 Simulink 数据类型 `{'double'}` （默认） | `{'int8'}` | `{'uint8'}` | `{'int16}` | `{'uint16'}` | `{'int32'}` | `{'uint32'}`

一个元胞向量，其元素数量与
**Number of variables** 中指定的数量相同，可以为每个输出端口指定不同的数据类型。单个元素会被复制。例如：

```
nvars=3
```

`{ }` — 三个输出均为 double。

`{'uint8'}` — 三个输出均为
`uint8`。

`{'uint16', 'double', 'uint8'}` — 第一个输出
为 `uint16`，第二个输出为
`double`，第三个输出为
`uint8`。

#### 编程用法

|  |
| --- |
| **模块参数：** `varids` |
## 所属库

Simulink Real-Time / RS232

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

将 ASCII 字符向量解析为 Simulink 值

ASCII Decode 模块根据类似于 `scanf` 的格式说明符解析输入字符向量，并使转换后的值可用于实时
应用程序。

有关详细信息，请参阅 RS-232 Serial Communication 和
RS-232 Legacy Drivers。
