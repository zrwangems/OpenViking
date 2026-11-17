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
```yaml
ports:
- name: Field1
  summary: 模块要编码的第一个字段 标量
  direction: input
- name: Packet
  summary: uint8 字节流数据包向量
  direction: output
  data_types: uint8
```

### 输入

### **Field1** — 模块要编码的第一个字段 标量

模块要编码的第一个字段。输入端口的名称使用模块参数 `Field name` 定义。在定义数据包结构时创建的每个后续字段都会产生一个新的输入端口，`Field name` 值将作为输入端口的名称显示。

该模块可以有 1 到 `N` 个输入端口。
`N` 是您在 **Specify packet fields sequentially** 窗格中指定的数据包结构中的字段数。
### 输出

### **Packet** — uint8 字节流数据包向量

包含来自多个信号的编码数据的 uint8 字节流数据包，如数据包结构中所指定。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Header
  summary: 数据包的头部 字符数组 | 小于 255 的数值数组
  group: ''
  block_parameter: Header
- name: Field name
  summary: 数据包结构中字段的名称 Field1（默认）| 字符串
  group: ''
  block_parameter: FieldNames
- name: Input field length
  summary: 根据数据类型确定的输入字段长度 1（默认）| 数值标量
  group: ''
  block_parameter: FixedSizeFieldLength
- name: Input field data type
  summary: 字段的数据类型 uint8（默认）| int8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | single | double
  group: ''
  block_parameter: FixedFieldDataTypes
- name: Byte order
  summary: 数据包中字段的字节序 Little endian（默认）| Big endian
  group: ''
  block_parameter: IsLittleEndian
- name: Specify logic to generate checksum for validation
  summary: 启用校验和验证逻辑，并选择逻辑 XOR of bytes | 2's complement of sum of bytes | Custom algorithm
  group: ''
  block_parameter: ChecksumAlgorithm
- name: Checksum size
  summary: 自定义算法所用函数中指定的校验和字节大小 numeric scalar
  group: ''
  block_parameter: ChecksumSize
- name: File path
  summary: 用于自定义校验和逻辑的函数 (.m) 路径 MATLAB path
  group: ''
  block_parameter: ChecksumFilepath
- name: Terminator
  summary: 数据包的终止符 <none> (default) | CR ('\r') | LF ('\n') | CR/LF ('\r\n') | NULL ('\0') | Custom Terminator
  group: ''
  block_parameter: TerminatorOption
- name: Custom terminator
  summary: 数据包的自定义终止符 character array | array of numeric values less than 255
  group: ''
  block_parameter: CustomTerminatorVal
```

### **Header** — 数据包的头部 字符数组 | 小于 255 的数值数组

指定指示编码数据开始的头部。编码输出数据以该头部开始。

此参数中指定的数值数组是相应 ASCII 字符的 `uint8` 整数表示。

头部值的几个示例包括：‘START’、'$'、36、[36,37]。

#### 编程使用

|  |
| --- |
| **模块参数**：`Header` |

#### Specify packet fields sequentially

### **Field name** — 数据包结构中字段的名称 `Field1`（默认）| 字符串

指定要包含在数据包结构中的字段名称。此名称将作为输入端口的名称显示。

要添加新的数据包字段并指定其属性，请点击 **Add**。添加字段后，点击 **Move Up** 或 **Move Down** 可更改其在结构中的顺序。

要删除字段及其属性，请选择该行并点击 **Delete**。

#### 编程使用

|  |
| --- |
| **模块参数**：`FieldNames` |

### **Input field length** — 根据数据类型确定的输入字段长度 `1`（默认）| 数值标量

根据您在下一列（`Input field data type`）中输入的数据类型确定的输入字段长度。例如，如果某个字段的 `Input field data type` 为 ‘uint16’ 且长度为 1，则编码器会将输入转换为输出数据包中的两个 `uint8` 字节。

#### 编程使用

|  |
| --- |
| **模块参数**：`FixedSizeFieldLength` |

### **Input field data type** — 字段的数据类型 `uint8`（默认）| `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

选择字段的数据类型。

**注意**

`double` 被视为 8 字节。如果您的硬件不支持 8 字节 `double`，选择此数据类型可能会产生不正确的结果。

#### 编程使用

|  |
| --- |
| **模块参数**：`FixedFieldDataTypes` |

### **Byte order** — 数据包中字段的字节序 `Little endian`（默认）| `Big endian`

选择数据包字段的字节序，以描述字节解包的顺序。

#### 编程使用

|  |
| --- |
| **模块参数**：`IsLittleEndian` |

### **Specify logic to generate checksum for validation** — 启用校验和验证逻辑，并选择逻辑 `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

使用标准算法或自定义算法指定用于验证的校验和生成逻辑。

如果逻辑选择为 `XOR of bytes`，模块将校验和计算为一个单字节，该字节是除头部、终止符（如适用）之外所有字节的 XOR。

如果逻辑选择为 `2's complement of sum of bytes`，模块将校验和计算为一个单字节，该字节是除头部和终止符（如适用）之外所有字节之和的 2 的补码。

如果选择 `Custom algorithm`，则启用附加参数 – **Checksum size** 和 **File path**。在这种情况下，您可以提供自己的自定义逻辑来验证数据包。自定义逻辑返回的校验和字节大小应与 **Checksum size** 字段中指定的大小一致，并且这些字节会追加到数据包中。

对于上述三种情况下的编码数据包，校验和字节要么追加在末尾（如果终止符不可用），要么追加在终止符之前（如果指定了终止符）。

#### 编程使用

|  |
| --- |
| **模块参数**：`ChecksumAlgorithm` |

### **Checksum size** — 自定义算法所用函数中指定的校验和字节大小 numeric scalar

指定用于自定义算法的函数所生成的校验和字节大小。

#### 依赖关系

仅当在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，才启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ChecksumSize` |

### **File path** — 用于自定义校验和逻辑的函数 (.m) 路径 MATLAB path

指定其中定义了用于生成校验和字节的自定义算法的函数 (.m) 的路径。该文件必须保存在 MATLAB path 中的某个目录下。

#### 依赖关系

仅当在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，才启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ChecksumFilepath` |

### **Terminator** — 数据包的终止符 `<none>` (default) | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

指定表示编码数据结束的终止符。编码输出中的最后一个字节/字节组是终止符。

如果选择 `Custom Terminator`，则可以指定自己的终止符值。

#### 编程使用

|  |
| --- |
| **模块参数**：`TerminatorOption` |

### **Custom terminator** — 数据包的自定义终止符 character array | array of numeric values less than 255

指定表示编码数据结束的自定义终止符。编码输出中的最后一个字节/字节组是终止符。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

自定义终止符值的一些示例包括：‘END’、'#'。

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomTerminatorVal` |
## 所属库

Simulink Real-Time / Utilities

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

通过指定数据包结构，将输入数据编码为 uint8 字节流

协议编码器模块根据基于通信协议的指定数据包结构，将输入数据编码为 uint8 字节流。您可以使用此模块，通过按顺序指定数据包头、终止符、数据包字段名称及其大小，将各个字段编码为一个数据包。您还可以为数据包生成校验和字节以验证数据包。这些图展示了协议编码器和协议解码器如何简化串行通信。

**不使用编码器和解码器模块的简单串行通信**

模型 slrt\_ex\_serialasciitest\_protocol\_e\_d 展示了简单串行通信。

**使用编码器和解码器模块的简单串行通信**

模型 slrt\_ex\_serialasciitest\_protocol\_e\_d 经过修改，展示了用于简单串行通信的编码器和解码器模块。
