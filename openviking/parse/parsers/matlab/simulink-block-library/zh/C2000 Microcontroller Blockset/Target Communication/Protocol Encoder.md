---
type: simulink-block
title: 'Protocol Encoder'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Target Communication'
documentation_page: 'protocolencoder'
documentation_source_path: 'ref/protocolencoder.html'
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

模块要编码的第一个字段。输入端口的名称使用模块参数 `Field name` 定义。在定义数据包结构时创建的每个后续字段都会产生一个新的输入端口，`Field name` 值会显示为输入端口的名称。

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
- name: Field name
  summary: 数据包结构中的字段名称 Field1（默认）| 字符串
  group: ''
- name: Input field length
  summary: 根据数据类型的输入字段长度 1（默认）| 数值标量
  group: ''
- name: Input field data type
  summary: 字段的数据类型 uint8（默认）| int8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | single | double
  group: ''
- name: Byte order
  summary: 数据包中字段的字节序 Little endian（默认）| Big endian
  group: ''
- name: Specify logic to generate checksum for validation
  summary: 启用校验和验证逻辑并选择逻辑 XOR of bytes | 2's complement of sum of bytes | Custom algorithm
  group: ''
- name: Checksum size
  summary: 用于自定义算法的函数中指定的校验和字节大小 数值标量
  group: ''
- name: File path
  summary: 用于自定义校验和逻辑的函数 (.m) 的路径 MATLAB 路径
  group: ''
- name: Terminator
  summary: 数据包的终止符 <none>（默认）| CR ('\r') | LF ('\n') | CR/LF ('\r\n') | NULL ('\0') | Custom Terminator
  group: ''
- name: Custom terminator
  summary: 数据包的自定义终止符 字符数组 | 小于 255 的数值数组
  group: ''
```

### **Header** — 数据包的头部 字符数组 | 小于 255 的数值数组

指定指示编码数据开始的头部。编码输出数据以该头部开始。

此参数中指定的数值数组是相应 ASCII 字符的 `uint8` 整数表示。

头部值的一些示例包括：‘START’、'$'、36、[36,37]。

#### 按顺序指定数据包字段

### **Field name** — 数据包结构中的字段名称 `Field1`（默认）| 字符串

指定要包含在数据包结构中的字段名称。此名称会显示为输入端口的名称。

要添加新的数据包字段并指定其属性，请点击 **Add**。添加字段后，点击 **Move Up** 或 **Move Down** 可更改其在结构中的顺序。

要删除字段及其属性，请选择该行并点击 **Delete**。

### **Input field length** — 根据数据类型的输入字段长度 `1`（默认）| 数值标量

根据您在下一列（`Input field data type`）中输入的数据类型确定的输入字段长度。例如，如果某个字段的 `Input field data type` 为 ‘uint16’ 且长度为 1，则编码器会将输入转换为输出数据包中的两个 `uint8` 字节。

### **Input field data type** — 字段的数据类型 `uint8`（默认）| `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

选择字段的数据类型。

**注意**

`double` 被视为 8 字节。如果您的硬件不支持 8 字节 `double`，选择此数据类型可能会产生不正确的结果。

### **Byte order** — 数据包中字段的字节序 `Little endian`（默认）| `Big endian`

选择数据包字段的字节序，以描述字节解包的顺序。

### **Specify logic to generate checksum for validation** — 启用校验和验证逻辑并选择逻辑 `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

指定使用标准算法或自定义算法生成用于验证的校验和的逻辑。

如果逻辑选择为 `XOR of bytes`，模块会将校验和计算为单个字节，即除头部、终止符（如适用）之外所有字节的 XOR。

如果逻辑选择为 `2's complement of sum of bytes`，模块会将校验和计算为单个字节，即除头部和终止符（如适用）之外所有字节之和的 2 的补码。

如果选择 `Custom algorithm`，则会启用附加参数 – **Checksum size** 和 **File path**。在这种情况下，您可以提供自己的自定义逻辑来验证数据包。自定义逻辑返回的校验和字节大小应与 **Checksum size** 字段中指定的大小一致，并且这些字节会追加到数据包中。有关详细信息，请参阅 Function Template for Custom Checksum Logic in Protocol Encoder Block。

对于上述三种情况下的编码数据包，校验和字节要么追加在末尾（如果不存在终止符），要么追加在终止符之前（如果指定了终止符）。

### **Checksum size** — 用于自定义算法的函数中指定的校验和字节大小 数值标量

指定用于自定义算法的函数所生成的校验和字节大小。有关详细信息，请参阅 Protocol Encoder 模块中自定义校验和逻辑的函数模板。

#### 依赖关系

仅当在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才会启用。

**数据类型：** `uint8`

### **File path** — 用于自定义校验和逻辑的函数 (.m) 的路径 MATLAB 路径

指定用于定义生成校验和字节的自定义算法的函数 (.m) 的路径。该文件必须保存在 MATLAB 路径中的某个目录下。

#### 依赖关系

仅当在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才会启用。

**数据类型：** `uint8`

### **Terminator** — 数据包的终止符 `<none>`（默认）| `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

指定用于指示编码数据结束的终止符。编码输出中的最后一个字节/字节序列即为终止符。

如果选择 `Custom Terminator`，则可以指定自己的终止符值。

### **Custom terminator** — 数据包的自定义终止符 字符数组 | 小于 255 的数值数组

指定用于指示编码数据结束的自定义终止符。编码输出中的最后一个字节/字节序列即为终止符。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

自定义终止符值的几个示例包括：‘END’、‘#’。

**数据类型：** `uint8`
## 所属库

C2000 Microcontroller Blockset / Target Communication Simulink Support Package for Raspberry Pi Hardware / Utilities Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

通过指定数据包结构将输入数据编码为 uint8 字节流

Protocol Encoder 根据基于通信协议指定的数据包结构，将输入数据编码为 uint8 字节流。您可以使用此模块，通过按顺序指定报头、终止符、数据包字段名称及其大小，将各个字段编码为一个数据包。您还可以为数据包生成校验和字节，以验证数据包。
