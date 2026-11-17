---
type: simulink-block
title: 'Protocol Decoder'
family: 'target-communication'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Target Communication'
documentation_page: 'protocoldecoder'
documentation_source_path: 'ref/protocoldecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Protocol Decoder

## 端口

### 输入

### **Data** — uint8 字节流数据包向量

包含来自多个信号的编码数据的 uint8 字节流数据包，如数据包结构中所指定。

输入数据包可以在多个采样时间上部分接收。Protocol Decoder 模块能够缓冲此类部分数据，直到接收到完整数据包。

**数据类型：** `uint8`

### **Length** — Data 输入端口处数据流数据包的长度，数值标量

用于包含有效数据流精确长度的可选输入端口。当您知道输入数据流中有效数据的精确长度时，请使用此选项。

此选项适用于以下情况：通信信道接收外设输出包含尾随零的部分接收数据。此类外设还会输出所接收有效数据字节实际数量的长度。您可以将外设的长度输出直接连接到 Protocol Decoder 模块的 **Length** 输入端口，这样输入字节流中的尾随零就不会影响解码逻辑。

#### 依赖关系

仅当您选择 **Is input data stream length available** 参数时，此输入端口才会出现。

**数据类型：** `uint16`

### 输出

### **Field1** — 模块解码的第一个字段，标量

模块解码的第一个字段的名称。输出端口的名称使用模块参数 `Field name` 定义。您在定义数据包结构时创建的每个后续字段都会生成一个新的输出端口，其中 `Field name` 值显示为该输出端口的名称。

模块可以有 1 到 `N` 个输出端口。`N` 是您在 **按顺序指定数据包字段** 窗格中指定的数据包结构中的字段数。

**数据类型：** `string`

### **IsNew** — 新数据指示符 `0` | `1`

以逻辑值形式返回的新数据指示符。值 1 表示自模块接收到上一个样本以来有新数据可用。此输出可用于触发子系统，以处理从 Protocol Decoder 模块接收的新数据。

如果 `IsNew` = 0，模块输出其解码的上一个完整数据包中的解码字段。如果没有上一个样本可用，模块输出零。

**数据类型：** `Boolean`

### **IsValid** — 校验和验证指示符 `0` | `1`

以逻辑值形式返回的校验和验证指示符。值 1 表示使用您指定的校验和逻辑验证时，模块接收的输入数据包有效。如果 `IsValid` = 0，模块输出零。

#### 依赖关系

此输出端口仅在您选择 **Specify logic for checksum validation** 参数时出现。

**数据类型：** `Boolean`

### **Variable field length** — 可变大小的最后一个字段的实际数据长度，数值标量

可变大小的最后一个字段的实际数据长度。可变大小字段的最大大小可以使用 **Specify maximum length if last field has variable size** 参数指定。模块将可变大小数据输出为固定大小数据，其大小等于指定的最大长度。输出包含实际数据，后跟尾随零。实际数据的大小可以使用此 **Variable Field Length** 输出确定。

#### 依赖关系

此输出端口仅在您选择 **Specify maximum length if last field has variable size** 参数时出现。有关详细信息，请参阅解码可变大小数据包。

**数据类型：** `double`

### **Variable field lengths** — 逗号分隔变量的实际数据长度数组

从输入流中解码的逗号分隔变量的实际数据长度。

此输出值（1×`N` 数组）对应于数据包中字段的实际数据长度，其中 N 是数据包中逗号分隔变量的数量。

当选择 **Parse comma separated variables** 时，`Output field length` 参数值对应于字段的最大大小。字段的实际大小可作为 **Variable field lengths** 输出获得。

如果第 n 个字段的实际字段长度小于模块上指定的 `Output field length` 参数值，则该字段对应的输出为实际数据后跟尾随零。**Variable field lengths** 输出的第 n 个元素提供该数组中该变量对应的实际长度。

如果第 n 个字段的实际字段长度大于模块上指定的 `Output field length` 参数值，则在数据包实际大小不超过最大数据包大小的前提下，该字段对应的输出会被截断并输出。**Variable field lengths** 输出的第 n 个元素提供该数组中该变量对应的实际长度。

#### 依赖关系

此输出端口仅在您选择 **Parse comma separated variables** 参数时出现。有关详细信息，请参阅解码逗号分隔变量。

**数据类型：** `double`

## 参数

### **Parse comma separated variables** — 解析包含逗号分隔变量的输入数据数组

指定要解析的输入数据包含逗号分隔变量。

**数据类型：** `uint8`

### **Header** — 数据包的 Header，字符数组 | 小于 255 的数值数组

指定指示数据开始的标头。仿真会忽略标头之前出现的数据。标头数据不会发送到输出端口。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

Header 值的几个示例为：‘START’、'$'、36、[36,37]。

#### 按顺序指定数据包字段

### **Field name** — 数据包结构中字段的名称 `Field1`（默认） | string

指定数据包结构中包含的字段的名称。此名称显示为输出端口的名称。

要添加新的数据包字段并指定其属性，请点击 **添加**。添加字段后，点击 **上移** 或 **下移** 以更改其在结构中的顺序。

要删除字段及其属性，请选择该行并点击 **删除**。

### **Output field length** — 根据数据类型的字段在数据包结构中的长度 `1`（默认） | 数值标量

根据您在下一列（`Output field data type`）中输入的数据类型，字段在数据包结构中的长度。例如，如果某个字段的 `Output field data type` 为 `uint16` 且长度为 1，则解码器根据数据包结构从数据包中读取两个字节，并将这些字节组合以输出一个 `uint16` 值。

如果您选择 **Parse comma separated variables** 参数，则 `Output field length` 值对应于该字段可以具有的最大长度。

**数据类型：** `double`

### **Output field data type** — 字段的数据类型 `uint8`（默认） | `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

选择字段的输出数据类型。

**注意**

`double` 被视为 8 字节。如果您的硬件不支持 8 字节 `double`，选择此数据类型可能会得到错误结果。

**注意**

如果您选择 **Parse comma separated variables** 参数，则无法编辑此参数（**Output field data type** 始终设置为 `uint8`）。

### **Byte order** — 数据包中字段的字节序 `Little endian`（默认） | `Big endian`

选择数据包字段的字节序，以描述字节传输的顺序。

**注意**

如果您选择 **Parse comma separated variables** 参数，则无法编辑此参数（**Byte order** 始终设置为 `Little endian`）。

### **Specify maximum length if last field has variable size** — 启用最后一个字段输出可变大小数据并指定字段的最大长度，数值标量

启用数据包的最后一个字段输出可变大小数据，并指定可变长度字段的最大长度，该字段作为数据包中的最后一个字段存在。有关详细信息，请参阅 Protocol Decoder 模块中自定义校验和逻辑的函数模板。

### **Specify logic for checksum validation** — 启用校验和验证逻辑并选择逻辑 `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

指定用于生成校验和以进行验证的逻辑，可使用标准算法或自定义算法。

如果选择 `Custom algorithm`，则会启用附加参数 – **Checksum size** 和 **File path**。

校验和字节预期位于数据包中的最后位置（如果存在终止符，则在终止符之前）。

如果选择逻辑为 `XOR of bytes`，则校验和字节预期为终止符之前的最后一个字节。该逻辑计算除标头、终止符和校验和字节之外所有字节的 XOR，并将其与校验和字节进行比较。

如果选择逻辑为 `2's complement of sum of bytes`，则校验和字节预期为终止符之前的最后一个字节。该逻辑计算除标头、终止符和校验和字节之外所有字节之和的 2 的补码，并将其与校验和字节进行比较。

如果选择 `Custom algorithm`，您可以提供自己的自定义逻辑来验证数据包。在这种情况下，校验和字节按 **Checksum size** 字段中指定的大小提取。有关详细信息，请参阅 Protocol Decoder 模块中自定义校验和逻辑的函数模板。

### **Checksum size** — 校验和数据的字节数，数值标量

指定校验和数据的字节数。模块按指定大小提取校验和字节，并将其传递给用于自定义算法的函数，以验证数据包。有关详细信息，请参阅 Protocol Decoder 模块中自定义校验和逻辑的函数模板。校验和字节预期位于数据包中的最后位置（如果存在终止符，则在终止符之前）。

#### 依赖关系

仅当您在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才会启用。

**数据类型：** `uint8`

### **File path** — 用于自定义校验和逻辑的函数的路径（.m），MATLAB 路径

指定您在其中为校验和逻辑定义自定义算法的函数（.m）的路径。该文件必须保存在 MATLAB 路径中的目录中。有关详细信息，请参阅 Protocol Decoder 模块中自定义校验和逻辑的函数模板。

#### 依赖关系

仅当您在 **Specify logic for checksum validation** 参数下选择 `Custom algorithm` 选项时，此参数才会启用。

**数据类型：** `uint8`

### **Terminator** — 数据包的终止符 `<none>`（默认） | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

指定指示数据结束的终止符。终止符数据不会发送到输出端口。

如果选择 `Custom Terminator`，您可以指定自己的终止符值。

**数据类型：** `uint8`

### **Custom terminator** — 数据包的自定义终止符，字符数组

指示数据结束的自定义终止符。终止符数据不会发送到输出端口。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。

自定义终止符值的几个示例为：‘END’、'#'。

### **Is input data stream length available** — 启用数据流长度的附加输入 `off`（默认） | `on`

启用可选输入端口，以包含有效数据流的精确长度。

## 所属库

C2000 Microcontroller Blockset / Target Communication Simulink Support Package for Raspberry Pi Hardware / Utilities Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

通过指定数据包结构来解码 uint8 字节流

Protocol Decoder 模块根据基于通信协议指定的数据包结构解码 uint8 字节流。您可以使用此模块，通过按顺序指定标头、终止符、数据包字段名称及其大小，将数据包解码为单独的字段。您还可以使用指定的校验和逻辑验证数据包。
