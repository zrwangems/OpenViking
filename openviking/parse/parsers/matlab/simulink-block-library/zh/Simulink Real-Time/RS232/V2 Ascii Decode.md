---
type: simulink-block
title: 'ASCII Decode V2'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'asciidecodev2'
documentation_source_path: 'io_ref/asciidecodev2.html'
language: zh-CN
chinese_source: worker-translation
---

# ASCII Decode V2

## 端口
```yaml
ports:
- name: Data
  summary: 要解析的输入向量 character vector
  direction: input
  data_types: int8 | uint8 | int16 | uint16
- name: cnt
  summary: 输入整数所满足的格式说明符数量
  direction: output
- name: Value
  summary: 发送 Simulink 数值的内联端口 numeric
  direction: output
  data_types: single | double | int8 | uint8 | uint16 | int16 | int32 | uint32
```

### 输入

### **Data** — 要解析的输入向量 `character vector`

输入向量可以是 8 位或 16 位，并且可以是有符号或无符号的。
如果数据格式为 16 位，该模块会忽略每个条目的高 8 位。

**数据类型：** `int8` | `uint8` | `int16` | `uint16`
### 输出

### **cnt** — 输入整数所满足的格式说明符数量

`cnt` 接收输入字符向量所满足的格式说明符数量。

### **Value** — 发送 Simulink 数值的内联端口 numeric

与 **Format** 中的项对应的输出端口。

该模块为目标计算机生成内联代码。你不能将其用于 Simulink 仿真。

**数据类型：** `single` | `double` | `int8` | `uint8` | `uint16` | `int16` | `int32` | `uint32`
## 参数
```yaml
parameters:
- name: Format
  summary: 用于解析输入向量的格式说明符 '%f\n'（默认）| %c | %d | %i | %o | %u | %x | %e | %g
  group: ''
  block_parameter: format
```

### **Format** — 用于解析输入向量的格式说明符 `'%f\n'`（默认）| `%c` | `%d` | `%i` | `%o` | `%u` | `%x` | `%e` | `%g`

输入一个类似 `scanf` 的格式字符串。每个格式说明符（例如 `%d`）都必须与输入向量中的对应部分匹配。格式中的字面字符串必须与输入向量中的字符匹配。格式说明符遵循 `scanf` 的常规说明。说明符必须用单引号括起来。未包含这些引号会导致仿真失败。

示例格式字符串为：

```
'alpha %d bravo %f\n'
```

在此示例中，从 FIFO 读取的数据为 `'alpha
5'`。在这种情况下，`cnt` 为
`1`，并且第二个输出与上次在字符向量中同时找到二者时相比保持不变。如果模型期望
`2` 个值，而 `cnt` 小于
`2`，则模型会检测到数据中的错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `format` |
## 所属库

Simulink Real-Time / RS232

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

将 ASCII 字符向量解析为 Simulink 值

ASCII Decode 模块解析由以下之一生成的输入向量：

- Serial port Receive 模块
- Serial port FIFO Read 模块
- ASCII Encode 模块

该模块使转换后的值可供实时应用使用。它假定
输入向量是使用类似于
`printf` 的输出格式说明符生成的，并使用类似于
`scanf` 的输入格式说明符。

该模块为 Speedgoat® 目标计算机生成内联代码。你不能将其用于 Simulink® 仿真。

有关详细信息，请参阅 RS-232 Serial Communication 和
RS-232 Legacy Drivers。
