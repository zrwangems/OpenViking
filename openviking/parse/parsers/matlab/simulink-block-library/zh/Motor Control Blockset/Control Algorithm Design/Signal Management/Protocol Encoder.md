---
type: simulink-block
title: 'Protocol Encoder'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Signal Management'
documentation_page: 'protocolencoder'
documentation_source_path: 'ref/protocolencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Protocol Encoder

## 端口

### 输入

### **Field1** — 模块要编码的第一个字段 scalar

模块要编码的第一个字段。输入端口的名称使用模块参数 `Field name` 定义。您在定义数据包结构时创建的每个后续字段都会产生一个新的输入端口，其中 `Field name` 值会显示为输入端口的名称。

该模块可以有 1 到 `N` 个输入端口。`N` 是您在 **依次指定数据包字段** 窗格中指定的数据包结构中的字段数。

### 输出

### **Packet** — uint8 字节流数据包向量

uint8 字节流数据包，其中包含按数据包结构指定的来自多个信号的编码数据。

**数据类型：** `uint8`

## 参数

### **Header** — 数据包的包头 character array | array of numeric values less than 255

指定指示编码数据开始位置的包头。编码输出数据以包头开始。

此参数中指定的数值数组是相应 ASCII 字符的 `uint8` 整数表示。

包头值的几个示例包括：‘START’、'$'、36、[36,37]。

#### 依次指定数据包字段

### **Field name** — 数据包结构中字段的名称 `Field1` (default) | string

指定要包含在数据包结构中的字段名称。此名称会显示为输入端口名称。

要添加新的数据包字段并指定其属性，请点击 **添加**。添加字段后，点击 **上移** 或 **下移** 以更改其在结构中的顺序。

要删除字段及其属性，请选择该行并点击 **删除**。

### **Input field length** — 根据数据类型的输入字段长度 `1` (default) | numeric scalar

输入字段的长度取决于您在下一列（`Input field data type`）中输入的数据类型。例如，如果某个字段的 `Input field data type` 为 ‘uint16’，长度为 1，则编码器会在输出数据包中将输入转换为两个 `uint8` 字节。

### **Input field data type** — 字段的数据类型 `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

选择字段的数据类型。

**注意**

`double` 被视为 8 字节。如果您的硬件不支持 8 字节 `double`，选择此数据类型可能会得到不正确的结果。

### **Byte order** — 数据包中字段的字节序 `Little endian` (default) | `Big endian`

选择数据包字段的字节序，以描述字节的解包顺序。

### **Specify logic to generate checksum for validation** — 启用校验和验证逻辑并选择逻辑 `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

指定使用标准算法或自定义算法生成校验和以进行验证的逻辑。

如果逻辑选择为 `XOR of bytes`，模块会将校验和计算为一个单字节，该字节是除包头、终止符（如果适用）之外所有字节的 XOR。

如果逻辑选择为 `2's complement of sum of bytes`，模块会将校验和计算为一个单字节，该字节是除包头和终止符（如果适用）之外所有字节之和的 2 的补码。

如果选择 `Custom algorithm`，则会启用附加参数 – **Checksum size** 和 **File path**。在这种情况下，您可以提供自己的自定义逻辑来验证数据包。自定义逻辑返回的校验和字节大小应与 **Checksum size** 字段中指定的大小一致，并且这些字节会附加到数据包中。有关详细信息，请参阅 C2000 Microcontroller Blockset 中 Protocol Decoder Block 的自定义校验和逻辑函数模板。

对于上述三种情况下的编码数据包，校验和字节要么附加在末尾（如果终止符不可用），要么附加在终止符之前（如果指定了终止符）。

### **Checksum size** — 用于自定义算法的函数中指定的校验和字节大小 numeric scalar

指定用于自定义算法的函数生成的校验和字节大小。有关更多详细信息，请参阅 C2000 Microcontroller Blockset 中 Protocol Decoder Block 的自定义校验和逻辑函数模板。

#### 依赖项

仅当您在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，才会启用此参数。

**数据类型：** `uint8`

### **File path** — 用于自定义校验和逻辑的函数 (.m) 的路径 MATLAB® path

指定您在其中定义了用于生成校验和字节的自定义算法的函数 (.m) 的路径。该文件必须保存在 MATLAB path 中的某个目录下。

#### 依赖项

仅当您在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，才会启用此参数。

**数据类型：** `uint8`

### **Terminator** — 数据包的终止符 `<none>` (default) | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

指定指示编码数据结束的终止符。编码输出中的最后一个/最后几个字节是终止符。

如果选择 `Custom Terminator`，您可以指定自己的终止符值。

### **Custom terminator** — 数据包的自定义终止符 character array | array of numeric values less than 255

指定指示编码数据结束的自定义终止符。编码输出中的最后一个/最后几个字节是终止符。

此参数中指定的数值数组是相应 ASCII 字符的 `uint8` 整数表示。

自定义终止符值的几个示例包括：‘END’、'#'。

**数据类型：** `uint8`

## 所属库

Motor Control Blockset / Signal Management C2000 Microcontroller Blockset / Target Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

通过指定数据包结构，将输入数据编码为 uint8 字节流

Protocol Encoder 根据通信协议，按照指定的数据包结构将输入数据编码为 uint8 字节流。您可以使用此模块，通过按顺序指定包头、终止符、数据包字段名称及其大小，将各个字段编码为一个数据包。您还可以为数据包生成校验和字节，以验证数据包。
