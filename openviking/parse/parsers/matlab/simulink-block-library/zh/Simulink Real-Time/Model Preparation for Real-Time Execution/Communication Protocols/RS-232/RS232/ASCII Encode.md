---
type: simulink-block
title: 'ASCII Encode'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'asciiencode'
documentation_source_path: 'io_ref/asciiencode.html'
language: zh-CN
chinese_source: official
---

# ASCII Encode

## 端口

### 输入

### **1** — 接收待编码值的编号端口 数值

模块编码为空终止字符向量的值。

**数据类型:** `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **D** — 空终止字符向量 `character vector`

生成包含 NULL 终止字符向量的 `uint8` 输出向量。

## 参数

### **Format string** — 用于将值转换为 ASCII 的格式指定符 `%d\r` (默认) | `%c` | `%i` | `%o` | `%u` | `%x` | `%e` | `%f` | `%g`

输入类似 `printf` 的格式字符串。对于每个格式指定符（如 `%d`），该模块会将格式指定符替换为对应输入变量中的转换值。格式指定符遵循 `printf` 的常规描述。

#### 编程用法

|  |
| --- |
| **模块参数：**`format` |

### **Number of variables** — 模块输入数量 `1` (默认) | 整数

每个端口的数值将按 **Format string** 中指定的格式插入输出字符向量。

#### 编程用法

|  |
| --- |
| **模块参数：**`nvars` |

### **Max output string length** — 转换后字符向量的最大长度（以字节为单位） `128` (默认) | 整数

该模块为输出端口分配了足够的内存以支持此长度。在指定此长度时，请在字符向量中包含 NULL 终止符。

若转换后的字符向量超过此长度，该模块将返回错误且不会将该字符向量写入输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`maxlength` |

### **Variable types** — Simulink® 允许用于输入端口的数据类型 `{'double'}` (默认) | `{'int8'}` | `{'uint8'}` | `{'int16}` | `{'uint16'}` | `{'int32'}` | `{'uint32'}`

与 **Number of variables** 中指定元素数量相同的单元向量，可为每个输入端口指定不同的数据类型。单个元素被复制。例如：

```
nvars=3
```

`{ }` - 这三个输入都是双精度数值。

`{'uint8'}` - 这三个输入是 `uint8`。

`{'uint16', 'double', 'uint8'}` - 第一个输入是 `uint16`，第二个输入是 `double`，第三个输入是 `uint8`。

#### 编程用法

|  |
| --- |
| **模块参数：**`vartypes` |

## 所属库

Simulink Real-Time / RS232

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

将 Simulink 值转换为 uint8 字符向量

ASCII Encode 模块生成一个 `uint8` 输出向量，该向量包含基于类似 `printf` 格式字符串的 NULL 终止字符向量。数据来自输入端口。

有关详细信息，请参阅RS-232 串行通信和RS-232 Legacy Drivers。
