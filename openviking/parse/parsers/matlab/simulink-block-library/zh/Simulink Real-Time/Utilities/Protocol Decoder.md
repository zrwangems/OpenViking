---
type: simulink-block
title: 'Protocol Decoder'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'protocoldecoder'
documentation_source_path: 'io_ref/protocoldecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Protocol Decoder

## 端口

### 输入

### **Data** — uint8 字节流数据包向量

包含来自多个信号的编码数据的 uint8 字节流数据包，其结构由数据包结构指定。

输入数据包可以在多个采样时间上部分接收。Protocol Decoder 模块能够缓冲此类部分数据，直到接收到完整的数据包。

**数据类型：** `uint8`

### **Length** — Data 输入端口处数据流数据包的长度 数值标量

可选输入端口，用于指定有效数据流的精确长度。当您知道输入数据流中有效数据的精确长度时，使用此选项。

当您的通信信道接收外设输出包含尾部零的部分接收数据时，此选项非常有用。此类外设还会输出实际接收到的有效数据字节数的长度。您可以将外设的长度输出直接连接到 Protocol Decoder 模块的 **Length** 输入端口，这样输入字节流中的尾部零就不会影响解码逻辑。

#### 依赖关系

此输入端口仅在您选择 **Is input data stream length available** 参数时出现。

**数据类型：** `uint16`

### 输出

### **Field1** — 模块解码的第一个字段 标量

模块解码的第一个字段的名称。输出端口的名称使用模块参数 `Field name` 定义。您在定义数据包结构时创建的每个后续字段都会产生一个新的输出端口，其中 `Field name` 值作为输出端口的名称出现。

该模块可以有 1 到 `N` 个输出端口。`N` 是您在 **Specify packet fields sequentially** 窗格中指定的数据包结构中的字段数。

**数据类型：** `string`

### **IsNew** — 新数据指示符 `0` | `1`

新数据指示符，以逻辑值形式返回。值为 1 表示自模块上次接收到采样以来有新数据可用。此输出可用于触发子系统处理从 Protocol Decoder 模块接收到的新数据。

如果 `IsNew` = 0，模块输出模块上次解码的完整数据包中的解码字段。如果没有可用的上次采样，模块输出零。

**数据类型：** `Boolean`

### **IsValid** — 校验和验证指示符 `0` | `1`

校验和验证指示符，以逻辑值形式返回。值为 1 表示当使用您指定的校验和逻辑进行验证时，模块接收到的输入数据包是有效的。如果 `IsValid` = 0，模块输出零。

#### 依赖关系

此输出端口仅在您选择 **Specify logic for checksum validation** 参数时出现。

**数据类型：** `Boolean`

### **Variable field length** — 最后一个可变大小字段的实际数据长度 数值标量

最后一个可变大小字段的实际数据长度。可变大小字段的最大大小可以使用 **Specify maximum length if last field has variable size** 参数指定。模块将可变大小数据输出为固定大小数据，其大小等于指定的最大长度。输出包含实际数据后跟尾部零。实际数据的大小可以使用此 **Variable Field Length** 输出确定。

#### 依赖关系

此输出端口仅在您选择 **Specify maximum length if last field has variable size** 参数时出现。

**数据类型：** `double`

### **Variable field lengths** — 逗号分隔变量数组的实际数据长度

从输入流中解码得到的逗号分隔变量的实际数据长度。

此输出值（1×`N` 数组）对应于数据包中字段的实际数据长度，其中 N 是数据包中逗号分隔变量的数量。

当选中 **Parse comma separated variables** 时，`Output field length` 参数值对应于字段的最大大小。字段的实际大小可通过 **Variable field lengths** 输出获得。

如果第 n 个字段的实际字段长度小于模块上指定的 `Output field length` 参数值，则该字段对应的输出为实际数据后跟尾随零。**Variable field lengths** 输出的第 n 个元素提供该数组中该变量对应的实际长度。

如果第 n 个字段的实际字段长度大于模块上指定的 `Output field length` 参数值，则在给定实际数据包大小不超过最大数据包大小的情况下，该字段对应的输出被截断并输出。**Variable field lengths** 输出的第 n 个元素提供该数组中该变量对应的实际长度。

#### 依赖关系

此输出端口仅在选中 **Parse comma separated variables** 参数时出现。

**Data Types:** `double`

## 参数

### **Parse comma separated variables** — 解析包含逗号分隔变量数组的输入数据

指定要解析的输入数据包含逗号分隔变量。

#### 编程使用

|  |
| --- |
| **模块参数**：`Header` |

#### 编程使用

|  |
| --- |
| **模块参数**：`IsParseCSV` |

### **Header** — 数据包字符数组的包头 | 小于 255 的数值数组

指定指示数据开始位置的包头。仿真会忽略包头之前出现的数据。包头数据不会发送到输出端口。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

包头值的几个示例：'START'、'$'、36、[36,37]。

#### 编程使用

|  |
| --- |
| **模块参数**：`Header` |

#### Specify packet fields sequentially

### **Field name** — 数据包结构中的字段名称 `Field1`（默认）| 字符串

指定数据包结构中包含的字段名称。此名称显示为输出端口的名称。

要添加新的数据包字段并指定其属性，请点击 **Add**。添加字段后，点击 **Move Up** 或 **Move Down** 可更改其在结构中的顺序。

要删除字段及其属性，请选择该行并点击 **Delete**。

#### 编程使用

|  |
| --- |
| **模块参数**：`FieldNames` |

### **Output field length** — 数据包结构中字段的长度（根据数据类型） `1`（默认）| 数值标量

数据包结构中字段的长度，根据您在下一列（`Output field data type`）中输入的数据类型确定。例如，如果某个字段的 `Output field data type` 为 `uint16` 且长度为 1，则解码器根据数据包结构从数据包中读取两个字节，并将这些字节组合以输出一个 `uint16` 值。

如果选中 **Parse comma separated variables** 参数，则 `Output field length` 值对应于该字段可以具有的最大长度。

#### 编程使用

|  |
| --- |
| **模块参数**：`FixedSizeFieldLength` |

### **Output field data type** — 字段的数据类型 `uint8`（默认）| `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

选择字段的输出数据类型。

**注意**

`double` 被视为 8 字节。如果您的硬件不支持 8 字节 `double`，选择此数据类型可能会产生错误结果。

**注意**

如果您选择 **Parse comma separated variables** 参数，则无法编辑此参数（**Output field data type** 始终设置为 `uint8`）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FixedFieldDataTypes` |

### **Byte order** — 数据包中字段的字节序 `Little endian`（默认）| `Big endian`

选择数据包字段的字节序，以描述字节的传输顺序。

**注意**

如果您选择 **Parse comma separated variables** 参数，则无法编辑此参数（**Byte order** 始终设置为 `Little endian`）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IsLittleEndian` |

### **Specify maximum length if last field has variable size** — 使最后一个字段能够输出可变大小的数据并指定字段的最大长度 数值标量

使数据包的最后一个字段能够输出可变大小的数据，并指定可变长度字段的最大长度，该字段作为数据包中的最后一个字段存在。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxVariableSizeFieldLength` |

### **Specify logic for checksum validation** — 启用校验和验证逻辑并选择逻辑 `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

指定使用标准算法或自定义算法生成用于验证的校验和的逻辑。

如果您选择 `Custom algorithm`，则启用附加参数 – **Checksum size** 和 **File path**。

校验和字节预期位于数据包中的最后位置（如果存在终止符，则在终止符之前）。

如果您选择逻辑为 `XOR of bytes`，则校验和字节预期为终止符之前的最后一个字节。该逻辑计算除报头、终止符和校验和字节之外的所有字节的 XOR，并将其与校验和字节进行比较。

如果您选择逻辑为 `2's complement of sum of bytes`，则校验和字节预期为终止符之前的最后一个字节。该逻辑计算除报头、终止符和校验和字节之外的所有字节之和的 2 的补码，并将其与校验和字节进行比较。

如果您选择 `Custom algorithm`，您可以提供自己的自定义逻辑来验证数据包。在这种情况下，校验和字节将按照 **Checksum size** 字段中指定的大小提取。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ChecksumAlgorithm` |

### **Checksum size** — 校验和数据的字节数 数值标量

指定校验和数据的字节数。模块按照指定的大小提取校验和字节，并将其传递给用于自定义算法的函数，以验证数据包。校验和字节预期位于数据包中的最后位置（如果存在终止符，则在终止符之前）。

#### 依赖关系

仅当您在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ChecksumSize` |

### **File path** — 用于自定义校验和逻辑的函数 (.m) 的路径 MATLAB 路径

指定您在其中定义校验和逻辑自定义算法的函数 (.m) 的路径。该文件必须保存在 MATLAB 路径中的某个目录下。

#### 依赖关系

仅当您在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才启用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ChecksumFilepath` |

### **Terminator** — 数据包终止符 `<none>`（默认）| `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

指定指示数据结束的终止符。终止符数据不会发送到输出端口。

如果选择 `Custom Terminator`，可以指定自己的终止符值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TerminatorOption` |

### **Custom terminator** — 数据包的自定义终止符 字符数组

指示数据结束的自定义终止符。终止符数据不会发送到输出端口。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

自定义终止符值的几个示例：'END'、'#'

#### 程序化使用

|  |
| --- |
| **模块参数：** `CustomTerminatorVal` |

### **Is input data stream length available** — 为数据流长度启用额外输入 `off`（默认）| `on`

启用可选输入端口以包含有效数据流的确切长度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IsInputLengthAvailable` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

通过指定数据包结构解码 uint8 字节流

Protocol Decoder 模块根据通信协议，按照指定的数据包结构解码 uint8 字节流。通过按顺序指定包头、终止符、数据包字段名称及其大小，可以使用此模块将数据包解码为单独的字段。还可以使用指定的校验和逻辑验证数据包。这些图展示了 Protocol Encoder 和 Protocol Decoder 如何简化串行通信。

**不使用 Encoder 和 Decoder 模块的简单串行通信**

模型 slrt\_ex\_serialasciitest\_protocol\_e\_d 展示简单串行通信。

**使用 Encoder 和 Decoder 模块的简单串行通信**

模型 slrt\_ex\_serialasciitest\_protocol\_e\_d 经过修改，展示了用于简单串行通信的编码器和解码器模块。
