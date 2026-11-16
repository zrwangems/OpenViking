---
type: simulink-block
title: 'ASCII Decode V2'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'asciidecodev2'
documentation_source_path: 'io_ref/asciidecodev2.html'
language: zh-CN
chinese_source: official
---

# ASCII Decode V2

## 端口

### 输入

### **Data** — 待解析的输入向量 `character vector`

输入向量可以是 8 位或 16 位，且可以是有符号或无符号的。如果数据格式为 16 位，则该模块会忽略每个条目的高 8 位。

**数据类型:** `int8` | `uint8` | `int16` | `uint16`
### 输出

### **cnt** — 输入满足的格式指定符数量 整数

`cnt` 接收由输入字符向量满足的格式指定符数量。

### **Value** — 内联端口发送 Simulink 值 数值

与 **Format** 中的项目相对应的输出端口。

此模块为目标计算机生成内联代码。您无法将其用于 Simulink 仿真。

**数据类型:** `single` | `double` | `int8` | `uint8` | `uint16` | `int16` | `int32` | `uint32`

## 参数

### **Format** — 用于解析输入向量的格式指定符 `'%f\n'` (默认) | `%c` | `%d` | `%i` | `%o` | `%u` | `%x` | `%e` | `%g`

输入类似 `scanf` 的格式字符串。每个格式指定符（如 `%d`）都必须与输入向量的对应部分匹配。格式中的字符串必须与输入向量中的字符完全匹配。格式指定符遵循 `scanf` 的常规描述。限定符必须用单引号括起来。未包含这些引号将导致仿真失败。

格式字符串示例如下：

```
'alpha %d bravo %f\n'
```

在此示例中，FIFO 读取的数据为 `'alpha 5'`。在此情况下，`cnt` 即为 `1`，且第二次输出结果与上次两者均出现在字符向量中的情况保持不变。如果模型预期值为 `2`，而 `cnt` 小于 `2`，则模型会检测到数据中的错误。

#### 编程用法

|  |
| --- |
| **模块参数：**`format` |

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

ASCII Decode 模块解析由以下任一方式生成的输入向量：

- 串行端口 Receive 模块
- 串行端口 FIFO Read 模块
- ASCII Encode 模块

该模块使转换后的值可供实时应用程序使用。它假定输入向量是使用类似于 `printf` 的输出格式指定符准备的，并使用类似于 `scanf` 的输入格式指定符。

此模块为 Speedgoat® 目标计算机生成内联代码。您无法将其用于 Simulink® 仿真。

有关详细信息，请参阅RS-232 串行通信和RS-232 Legacy Drivers。
