---
type: simulink-block
title: 'ASCII Encode'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'asciiencode'
documentation_source_path: 'io_ref/asciiencode.html'
language: zh-CN
chinese_source: worker-translation
---

# ASCII Encode

## 端口

### 输入

### **1** — 接收用于编码为数值的带编号端口

模块将其编码为以 NULL 结尾的字符向量的值。

**数据类型：** `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **D** — 以 NULL 结尾的字符向量 `字符向量`

生成的 `uint8` 输出向量，包含以 NULL 结尾的字符向量。

## 参数

### **Format string** — 用于将值转换为 ASCII 的格式说明符 `%d\r`（默认）| `%c` | `%i` | `%o` | `%u` | `%x` | `%e` | `%f` | `%g`

输入一个类似 `printf` 的格式字符串。对于每个格式说明符（如 `%d`），模块将格式说明符替换为对应输入变量中的转换值。格式说明符遵循 `printf` 的常规描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`format` |

### **Number of variables** — 模块输入的数量 `1`（默认）| 整数

每个端口上的值按照 **Format string** 中指定的格式插入到输出字符向量中。

#### 编程使用

|  |
| --- |
| **模块参数**：`nvars` |

### **Max output string length** — 转换后字符向量的最大长度，以字节为单位 `128`（默认）| 整数

模块分配足够的内存以支持输出端口的此长度。指定此长度时，请包含字符向量上的 NULL 终止符。

如果转换后的字符向量超过此长度，模块将返回错误，并且不会将该字符向量写入输出端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`maxlength` |

### **Variable types** — 输入端口允许的 Simulink® 数据类型 `{'double'}`（默认）| `{'int8'}` | `{'uint8'}` | `{'int16}` | `{'uint16'}` | `{'int32'}` | `{'uint32'}`

一个元胞向量，其元素数量与 **Number of variables** 中指定的数量相同，可以为每个输入端口指定不同的数据类型。单个元素会被复制。例如：

```
nvars=3
```

`{ }` — 三个输入均为 double。

`{'uint8'}` — 三个输入均为 `uint8`。

`{'uint16', 'double', 'uint8'}` — 第一个输入为 `uint16`，第二个输入为 `double`，第三个输入为 `uint8`。

#### 编程使用

|  |
| --- |
| **模块参数**：`vartypes` |

## 所属库

Simulink Real-Time / RS232

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

将 Simulink 值转换为 uint8 字符向量

ASCII Encode 模块生成一个 `uint8` 输出向量，其中包含基于类似 `printf` 格式字符串的以 NULL 结尾的字符向量。数据来自输入端口。

有关详细信息，请参阅 RS-232 Serial Communication 和 RS-232 Legacy Drivers。
