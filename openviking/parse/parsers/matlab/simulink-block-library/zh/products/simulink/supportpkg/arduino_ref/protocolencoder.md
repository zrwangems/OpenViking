---
type: simulink-block
title: 'Protocol Encoder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Target Communication'
documentation_page: 'protocolencoder'
documentation_source_path: 'supportpkg/arduino_ref/protocolencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Protocol Encoder

## 端口

### 输入

### **Field1** — 要由模块编码的第一个字段 scalar

第一个要由模块编码的字段。输入端口的名称使用模块参数 `Field name` 定义。在定义包结构时创建的每个后续字段都会产生一个新的输入端口，其中 `Field name` 值显示为输入端口的名称。

该模块可以有 1 到 `N` 个输入端口。
`N` 是你在 **按顺序指定包字段** 窗格中指定的包结构中的字段数。

### 输出

### **Packet** — uint8 byte stream 包向量

包含来自多个信号的编码数据的 uint8 byte stream 包，这些编码数据如包结构中所指定。

**数据类型：** `uint8`

## 参数

### **Header** — 包的 Header character array | array of numeric values less than 255

指定表示编码数据开始的 Header。编码输出数据将以该 Header 开始。

在此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示形式。

Header 值的几个示例为：‘START’、'$'、36、[36,37]。

#### 按顺序指定包字段

### **Field name** — 包结构中字段的名称 `Field1`（默认） | string

指定要包含在包结构中的字段的名称。此名称显示为输入端口的名称。

要添加新的包字段并指定其属性，请点击 **添加**。添加字段后，点击 **上移** 或 **下移** 以更改其在结构中的顺序。

要删除字段及其属性，请选择该行并点击 **删除**。

### **Input field length** — 根据数据类型的输入字段长度 `1`（默认） | numeric scalar

根据你在下一列（`Input field data type`）中输入的数据类型确定的输入字段长度。例如，如果某个字段的 `Input field data type` 为 ‘uint16’，长度为 1，则编码器会在输出包中将输入转换为两个 `uint8` bytes。

### **Input field data type** — 字段的数据类型 `uint8`（默认） | `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

选择字段的数据类型。

**注意**

`double` 被视为 8 bytes。如果你的硬件不支持 8 bytes `double`，选择此数据类型可能会给出不正确的结果。

### **Byte order** — 包中字段的字节序 `Little endian`（默认） | `Big endian`

选择包字段的字节序，以描述字节解包的顺序。

### **Specify logic to generate checksum for validation** — 启用校验和验证逻辑并选择逻辑 `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

指定使用标准算法或自定义算法生成用于验证的校验和的逻辑。

如果逻辑选择为 `XOR of bytes`，则该模块计算校验和为单个 byte，该 byte 是除 Header、Terminator（如果适用）之外所有 bytes 的 XOR。

如果逻辑选择为 `2's complement of sum of bytes`，则该模块计算校验和为单个 byte，该 byte 是除 Header 和 Terminator（如果适用）之外所有 bytes 之和的 2's complement。

如果选择 `Custom algorithm`，则附加参数 – **Checksum size** 和 **File path** – 将启用。在这种情况下，你可以提供自己的自定义逻辑来验证包。自定义逻辑返回的校验和 bytes 的大小应为 **Checksum size** 字段中指定的大小，并且这些 bytes 将追加到包中。有关更多信息，请参阅 Protocol Encoder 模块中自定义校验和逻辑的函数模板。

对于上述三种情况中的编码包，校验和 bytes 要么追加在末尾（如果 Terminator 不可用），要么追加在 Terminator 之前（如果指定了 Terminator）。

### **Checksum size** — 用于自定义算法的函数中指定的校验和 bytes 大小 numeric scalar

指定用于自定义算法的函数生成的校验和 bytes 的大小。有关更多详细信息，请参阅 Protocol Encoder 模块中自定义校验和逻辑的函数模板。

#### 依赖项

仅当你在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才会启用。

**数据类型：** `uint8`

### **File path** — 用于自定义校验和逻辑的函数 (.m) 的路径 MATLAB path

指定你在其中定义了用于生成校验和 bytes 的自定义算法的函数 (.m) 的路径。该文件必须保存在 MATLAB 路径中的某个目录下。

#### 依赖项

仅当你在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才会启用。

**数据类型：** `uint8`

### **Terminator** — 包的 Terminator `<none>`（默认） | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

指定表示编码数据结束的 Terminator。编码输出中的最后一个/最后几个 byte/bytes 将是 Terminator。

如果选择 `Custom Terminator`，你可以指定自己的 Terminator 值。

### **Custom terminator** — 包的自定义 Terminator character array | array of numeric values less than 255

指定表示编码数据结束的自定义 Terminator。编码输出中的最后一个/最后几个 byte/bytes 将是 Terminator。

在此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示形式。

自定义 Terminator 值的几个示例为：‘END’、'#'。

**数据类型：** `uint8`

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Utilities Simulink Support Package for Arduino Hardware / Common C2000 Microcontroller Blockset / Target Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

通过指定包结构，将输入数据编码为 uint8 byte stream

Protocol Encoder 根据通信协议，按照指定的包结构将输入数据编码为 uint8 byte stream。通过按顺序指定 Header、Terminator、包字段的名称及其大小，你可以使用此模块将各个字段编码为一个包。你还可以为该包生成校验和 bytes，以验证该包。
