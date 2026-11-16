---
type: simulink-block
title: 'Protocol Encoder'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'protocolencoder'
documentation_source_path: 'io_ref/protocolencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Protocol Encoder

## 端口

### 输入

### **Field1** — 由模块编码的第一个字段 scalar

由模块编码的第一个字段。输入端口的名称使用模块参数 `Field name` 定义。在定义数据包结构时创建的每个后续字段都会产生一个新的输入端口，`Field name` 值将作为输入端口的名称出现。

该模块可以有 1 到 `N` 个输入端口。`N` 是你在 **依次指定数据包字段** 窗格中指定的数据包结构中的字段数。

### 输出

### **Packet** — uint8 字节流数据包向量

uint8 字节流数据包，其中包含根据数据包结构指定的来自多个信号的编码数据。

**数据类型：** `uint8`

## 参数

### **Header** — 数据包的包头 character array | array of numeric values less than 255

指定用于指示编码数据开始的包头。编码后的输出数据以该包头开始。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

包头值的几个示例包括：‘START’、'$'、36、[36,37]。

#### 编程用法

|  |
| --- |
| **模块参数：** `Header` |

#### 依次指定数据包字段

### **字段名称** — 数据包结构中字段的名称 `Field1` (default) | string

指定要包含在数据包结构中的字段名称。此名称将作为输入端口的名称显示。

要添加新的数据包字段并指定其属性，请点击 **Add**。添加字段后，点击 **Move Up** 或 **Move Down** 更改其在结构中的顺序。

要删除字段及其属性，请选择该行并点击 **Delete**。

#### 编程用法

|  |
| --- |
| **模块参数：** `FieldNames` |

### **输入字段长度** — 根据数据类型的输入字段长度 `1` (default) | numeric scalar

根据你在下一列（`Input field data type`）中输入的数据类型确定的输入字段长度。例如，如果某字段的 `Input field data type` 为 ‘uint16’ 且长度为 1，则编码器会在输出数据包中将输入转换为两个 `uint8` 字节。

#### 编程用法

|  |
| --- |
| **模块参数：** `FixedSizeFieldLength` |

### **输入字段数据类型** — 字段的数据类型 `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

选择字段的数据类型。

**注意**

`double` 被视为 8 字节。如果你的硬件不支持 8 字节 `double`，选择此数据类型可能会产生不正确的结果。

#### 编程用法

|  |
| --- |
| **模块参数：** `FixedFieldDataTypes` |

### **字节顺序** — 数据包中字段的字节序 `Little endian` (default) | `Big endian`

选择数据包字段的字节序，以描述字节解包的顺序。

#### 编程用法

|  |
| --- |
| **模块参数：** `IsLittleEndian` |

### **指定用于验证的校验和生成逻辑** — 启用校验和验证逻辑并选择逻辑 `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

指定使用标准算法或自定义算法生成用于验证的校验和的逻辑。

如果逻辑选择为 `XOR of bytes`，则模块将校验和计算为单个字节，该字节是除包头、终止符（如果适用）之外所有字节的 XOR。

如果逻辑选择为 `2's complement of sum of bytes`，则模块将校验和计算为单个字节，该字节是除包头和终止符（如果适用）之外所有字节之和的 2's complement。

如果选择 `Custom algorithm`，则会启用附加参数 – **校验和大小** 和 **文件路径** –。在这种情况下，你可以提供自己的自定义逻辑来验证数据包。自定义逻辑返回的校验和字节大小应为 **校验和大小** 字段中指定的大小，这些字节会追加到数据包中。

对于上述三种情况下的编码数据包，校验和字节要么追加在末尾（如果未指定终止符），要么追加在终止符之前（如果指定了终止符）。

#### 编程用法

|  |
| --- |
| **模块参数：** `ChecksumAlgorithm` |

### **校验和大小** — 用于自定义算法的函数中指定的校验和字节大小 numeric scalar

指定用于自定义算法的函数生成的校验和字节大小。

#### 依赖关系

仅当你在 **指定用于验证的校验和生成逻辑** 参数下选择 `Custom algorithm` 选项时，才启用此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `ChecksumSize` |

### **文件路径** — 用于自定义校验和逻辑的函数 (.m) 的路径 MATLAB path

指定你在其中定义用于生成校验和字节的自定义算法的函数 (.m) 的路径。该文件必须保存在 MATLAB path 中的目录中。

#### 依赖关系

仅当你在 **指定用于验证的校验和生成逻辑** 参数下选择 `Custom algorithm` 选项时，才启用此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `ChecksumFilepath` |

### **终止符** — 数据包的终止符 `<none>` (default) | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

指定用于指示编码数据结束的终止符。编码输出中的最后一个字节/字节序列是终止符。

如果选择 `Custom Terminator`，你可以指定自己的终止符值。

#### 编程用法

|  |
| --- |
| **模块参数：** `TerminatorOption` |

### **自定义终止符** — 数据包的自定义终止符 character array | array of numeric values less than 255

指定用于指示编码数据结束的自定义终止符。编码输出中的最后一个字节/字节序列是终止符。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

自定义终止符值的几个示例包括：‘END’、'#'。

#### 编程用法

|  |
| --- |
| **模块参数：** `CustomTerminatorVal` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2023b 中引入**

## 描述

通过指定数据包结构将输入数据编码为 uint8 字节流

Protocol Encoder 模块根据通信协议，按照指定的数据包结构将输入数据编码为 uint8 字节流。你可以使用此模块通过指定包头、终止符、数据包字段的名称（按顺序）及其大小，将各个字段编码为一个数据包。你还可以为数据包生成校验和字节以验证数据包。这些图展示了 Protocol Encoder 和 Protocol Decoder 如何简化串行通信。

**不使用编码器和解码器模块的简单串行通信**

模型 slrt\_ex\_serialasciitest\_protocol\_e\_d 展示了简单串行通信。

**使用编码器和解码器模块的简单串行通信**

模型 slrt\_ex\_serialasciitest\_protocol\_e\_d 经过修改，展示了用于简单串行通信的编码器和解码器模块。
