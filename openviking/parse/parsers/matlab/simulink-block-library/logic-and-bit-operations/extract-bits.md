---
type: simulink-block
title: 'Extract Bits'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'extractbits'
---

# Extract Bits

Output selection of contiguous bits from input signal

## 中文

输出从输入信号选择的连续位

### 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

### 描述

Extract Bits 模块允许您从输入信号的存储整数值中输出选择的连续位。使用**提取位**参数定义选择输出位的方法。

- 选择 `Upper half` 输出一半的输入位，其中包含最高有效位。如果输入信号中有奇数数量的位，则按以下方程计算输出位数

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- 选择 `Lower half` 输出一半的输入位，其中包含最低有效位。如果输入信号中有奇数数量的位，则按以下方程计算输出位数

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- 选择 `Range starting with most significant bit` 以输出一定数量的输入信号最高有效位。在**位数**参数中指定要输出的最高有效位数。
- 选择 `Range ending with least significant bit` 以输出一定数量的输入信号最低有效位。在**位数**参数中指定要输出的最低有效位数。
- 选择 `Range of bits` 以在**位索引**参数中指定要输出的输入信号的一系列连续位。您需要以 `[start end]` 格式指明范围，而输入位的索引将从 0（最低有效位）开始连续标记。

仿真期间，此模块不会报告溢出绕回警告。要报告这些警告，请参阅 `Simulink.restoreDiagnostic` 参考页。但此模块会报告由于溢出绕回而导致的错误。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。浮点输入通过模块时保持不变。`boolean` 输入被视为 `uint8` 信号。

**注意**

对有符号整数执行位运算非常困难。要解决这个难题，您可以将输入的数据类型转换为无符号整数类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 提取位 标量 | 向量 | 矩阵 | N 维数组

提取的连续选择的位，指定为标量、向量、矩阵或 N 维数组。浮点输入通过模块时保持不变。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **提取位** — 提取位的方法 **上半部** (默认) | **下半部** | **以最高有效位开始的范围** | **以最低有效位结束的范围** | **位范围**

选择用于从输入信号中提取位的方法。

假定有一个输入信号以二进制格式表示为 `110111001`：

- 如果您为**提取位**参数选择 `Upper half`，则输出为二进制 `11011`。
- 如果您为**提取位**参数选择 `Lower half`，则输出为二进制 `11001`。
- 如果您为**提取位**参数选择 `Range starting with most significant bit`，并为**位数**参数指定 `3`，则输出为二进制 `110`。
- 如果您为**提取位**参数选择 `Range ending with least significant bit`，并为**位数**参数指定 `8`，则输出为二进制 `10111001`。
- 如果您为**提取位**参数选择 `Range of bits`，并为**位索引**参数指定 `[4 7]`，则输出为二进制 `1011`。

##### 编程用法

|  |
| --- |
| **模块参数**：`bitsToExtract` |
| **类型：**字符向量 |
| **值：**`'Upper half' | 'Lower half' | 'Range starting with most significant bit' | 'Range ending with least significant bit' | 'Range of bits'` |
| **默认值：**`'Upper half'` |

#### **位数** — 要输出的位数 `8` (默认) | 正整数标量

将输入信号输出的位数指定为正整数标量。

##### 依赖关系

要启用此参数，请将**提取位**设置为 `Range starting with most significant bit` 或 `Range ending with least significant bit`。

##### 编程用法

|  |
| --- |
| **模块参数**：`numBits` |
| **类型：**字符向量 |
| **值：**正整数标量 |
| **默认值：**`'8'` |

#### **位索引** — 要输出的位数的连续范围 [0 7] (默认) | 二元素向量 | 正整数标量

将要输出的输入信号位的二元素向量指定为正整数标量。以 `[start end]` 格式指定范围。

##### 依赖关系

要启用此参数，请将**提取位**设置为 `Range of bits`。

##### 编程用法

|  |
| --- |
| **模块参数**：`bitIdxRange` |
| **类型：**字符向量 |
| **值：**二元素向量 | 正整数标量 |
| **默认值：**`'[0 7]'` |

#### **输出定标模式** — 输出定标模式 **保留定点定标** (默认) | **将位域视为整数**

选择要对输出位选项使用的定标模式：

- 如果您选择 `Preserve fixed-point scaling`，则在数据类型转换过程中，将使用输入的定点定标来确定输出缩放。
- 如果您选择 `Treat bit field as an integer`，将忽略输入的定点定标，只使用存储的整数来计算输出数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`outScalingMode` |
| **类型：**字符向量 |
| **值：**`'Preserve fixed-point scaling' | 'Treat bit field as an integer'` |
| **默认值：**`'Preserve fixed-point scaling'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Description

The Extract Bits block allows you to output a contiguous selection of
bits from the stored integer value of the input signal. Use the **Bits to
extract** parameter to define the method for selecting the output
bits.

- Select `Upper half` to output the half of the input bits that
  contain the most significant bit. If there is an odd number of bits in the input
  signal, the number of output bits is given by the equation

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- Select `Lower half` to output the half of the input bits that
  contain the least significant bit. If there is an odd number of bits in the
  input signal, the number of output bits is given by the equation

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- Select `Range starting with most significant bit` to output a
  certain number of the most significant bits of the input signal. Specify the
  number of most significant bits to output in the **Number of
  bits** parameter.
- Select `Range ending with least significant bit` to output a
  certain number of the least significant bits of the input signal. Specify the
  number of least significant bits to output in the **Number of
  bits** parameter.
- Select `Range of bits` to indicate a series of contiguous
  bits of the input to output in the **Bit indices** parameter.
  You indicate the range in `[start end]` format, and the indices
  of the input bits are labeled contiguously starting at 0 for the least
  significant bit.

This block does not report wrap on overflow warnings during simulation. To report
these warnings, see the `Simulink.restoreDiagnostic` reference
page. The block does report errors due to wrap on overflow.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array.
Floating-point inputs are passed through the block unchanged.
`boolean` inputs are treated as
`uint8` signals.

**Note**

Performing bit operations on a signed integer is difficult. You
can avoid difficulty by converting the data type of your input
signals to unsigned integer types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Extracted bits scalar | vector | matrix | N-D array

Contiguous selection of extracted bits, specified as a scalar, vector,
matrix, or N-D array. Floating-point inputs are passed through the block
unchanged.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Bits to extract** — Method for extracting bits `Upper half` (default) | `Lower half` | `Range starting with most significant bit` | `Range ending with least significant big` | `Range of bits`

Select the method for extracting bits from the input signal.

Consider an input signal that is represented in binary by
`110111001`:

- If you select `Upper half` for the **Bits
  to extract** parameter, the output is
  `11011` in binary.
- If you select `Lower half` for the **Bits
  to extract** parameter, the output is
  `11001` in binary.
- If you select `Range starting with most significant
  bit` for the **Bits to extract**
  parameter, and specify `3` for the **Number
  of bits** parameter, the output is
  `110` in binary.
- If you select `Range ending with least significant
  bit` for the **Bits to extract**
  parameter, and specify `8` for the **Number
  of bits** parameter, the output is
  `10111001` in binary.
- If you select `Range of bits` for the
  **Bits to extract** parameter, and specify
  `[4 7]` for the **Bit indices**parameter, the output is `1011` in
  binary.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `bitsToExtract` |
| **Type:** character vector |
| **Values:** `'Upper half' | 'Lower half' | 'Range starting with most significant bit' | 'Range ending with least significant bit' | 'Range of bits'` |
| **Default:** `'Upper half'` |

### **Number of bits** — Number of bits to output `8` (default) | scalar positive integer

Specify the number of bits to output from the input signal as a scalar
positive integer.

#### Dependencies

To enable this parameter, set **Bits to extract** to
`Range starting with most significant bit` or
`Range ending with least significant bit`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numBits` |
| **Type:** character vector |
| **Values:** scalar positive integer |
| **Default:** `'8'` |

### **Bit indices** — Contiguous range of bits to output [0 7] (default) | two-element vector | scalar positive integer

Specify a two-element vector of bits of the input signal to output as
scalar positive integers. Specify the range in `[start
end]` format.

#### Dependencies

To enable this parameter, set **Bits to extract** to
`Range of bits`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `bitIdxRange` |
| **Type:** character vector |
| **Values:** two-element vector | scalar positive integer |
| **Default:** `'[0 7]'` |

### **Output scaling mode** — Output scaling mode `Preserve fixed-point scaling` (default) | `Treat bit field as an integer`

Select the scaling mode to use on the output bit selection:

- When you select `Preserve fixed-point
  scaling`, the fixed-point scaling of the input is
  used to determine the output scaling during the data type
  conversion.
- When you select `Treat bit field as an
  integer`, the fixed-point scaling of the input is
  ignored, and only the stored integer is used to compute the
  output data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outScalingMode` |
| **Type:** character vector |
| **Values:** `'Preserve fixed-point scaling' | 'Treat bit field as an integer'` |
| **Default:** `'Preserve fixed-point scaling'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
