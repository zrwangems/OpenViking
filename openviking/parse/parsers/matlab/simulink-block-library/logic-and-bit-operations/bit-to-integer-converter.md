---
type: simulink-block
title: 'Bit to Integer Converter'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bittointegerconverter'
---

# Bit to Integer Converter

Map vector of bits to corresponding vector of integers

## 中文

将位向量映射为对应的整数向量

### 库

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

### 描述

Bit to Integer Converter 模块将输入向量中的位组映射为输出向量中的整数。

如果 *M* 由 **每个整数的位数(M)** 参数指定：

- 对于无符号整数，该模块将每组 *M* 位映射为范围 [0, (2*M* – 1)] 内的整数。因此，输出向量长度是输入向量长度的 1/*M* 倍。
- 对于有符号整数，该模块将每组 *M* 位映射为范围 [(–2*M*-1), (2*M* – 1 – 1)] 内的整数。

### 端口

#### 输入

#### **In** — 输入信号 位标量 | 位列向量

输入信号，指定为标量或位列向量，其长度是 **每个整数的位数(M)** 参数中所指定值的倍数。输入必须是值为 0 或 1 的位。

**数据类型:** `double`
#### 输出

#### **Out** — 输出信号 整数 | 整数列向量

输出信号，以整数或整数列向量形式返回。**位打包后，将结果整数值视为** 参数指定输入位被视为无符号还是有符号。

- 当输入位被视为无符号时，每个整数输出都在范围 [0, (2*M* – 1)] 内。
- 当输入位被视为有符号时，每个整数输出都在范围 [(–2*M*-1), (2*M* – 1 – 1)] 内。

### 参数

#### **每个整数的位数(M)** — 每个整数的位数 `3` (default) | [1, 32] 范围内的整数

映射到输出中每个整数的输入位数，指定为 [1, 32] 范围内的整数。

#### 程序化使用

|  |
| --- |
| **模块参数**: `nbits` |
| **类型**: character vector |
| **值**: [1, 32] 范围内的整数 |
| **默认值**: `'3'` |

#### **输入位顺序** — 输入位顺序 `MSB first` (default) | `LSB first`

输入位顺序，指定为 `'MSB first'` 或 `'LSB first'`。

- `'MSB first'` –– 输入信号的第一位是最高有效位 (MSB)。
- `'LSB first'` –– 输入信号的第一位是最低有效位 (LSB)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `bitOrder` |
| **类型**: character vector |
| **值**: `'MSB first'` | `'LSB first'` |
| **默认值**: `'MSB first'` |

#### **位打包后，将结果整数值视为** — 位打包后结果整数值的符号标志 `Unsigned` (default) | `Signed`

指定位打包后结果整数值被视为有符号还是无符号。此参数设置确定哪些 **输出数据类型** 选项可用。

**提示**

当此参数设置为 `Unsigned` 且模块发生溢出时，模块的行为如同 **位打包后，将结果整数值视为** 设置为 `Signed`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `signedOutputValues` |
| **类型**: character vector |
| **值**: `'Unsigned'` | `'Signed'` |
| **默认值**: `'Unsigned'` |

#### **输出数据类型** — 输出数据类型 `Inherit via internal rule` (default) | `Smallest integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

**输出数据类型** 选项会根据输出的所需符号性而变化。

如果输出整数为 `Signed`，可以从以下 **输出数据类型** 选项中选择：

- `Inherit via internal rule`
- `Smallest integer`
- `double`
- `single`
- `int8`
- `int16`
- `int32`

如果输出整数为 `Unsigned`，除了 `Signed` 选项外，还可以从以下选项中选择：

- `Same as input`
- `uint8`
- `uint16`
- `uint32`

当您将参数设置为 `Inherit via internal rule` 时，模块根据输入数据类型确定输出数据类型。

- 如果输入信号是浮点（`double` 或 `single`），则输出数据类型与输入数据类型相同。
- 如果输入数据类型不是浮点，则输出数据类型的确定方式如同参数设置为 `Smallest integer`。

当您将参数设置为 `Smallest integer` 时，模块根据 Configuration Parameters 对话框的 Hardware Implementation Pane 中使用的设置选择输出数据类型。

- 如果为设备供应商选择 `ASIC/FPGA`，则输出数据类型是基于 **每个整数的位数(M)** 参数的设置得到的最小理想整数或定点数据类型。
- 对于所有其他设备供应商选择，输出数据类型是足以容纳理想最小位大小的最小可用（有符号或无符号）整数字长。

#### 程序化使用

|  |
| --- |
| **模块参数**: `outDtype` |
| **类型**: character vector |
| **值**: `'Inherit via internal rule'` | `'Smallest integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` |
| **默认值**: `'Inherit via internal rule'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `no` |
|  |  |
| --- | --- |
| a 定点输入必须为 ufix(1)。  b 当在 Hardware Implementation Pane 中选择 ASIC/FPGA 且输出数据类型设置为 (a) Smallest integer 或 (b) Inherit via internal rule，并且同时输入为非浮点时，为 ufix(N) 或 sfix(N)。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点类型的 `MAX`、`MIN`、`CUSTOM` 或 `ZERO` 延迟。请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。请参阅 NFPCustomLatency (HDL Coder)。 |

**数据类型支持**

此模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | Boolean | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量 | Yes | Single  Double | Yes | Yes | Yes | No |

**延迟详情**

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看添加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**浮点延迟**

| 架构 | 浮点类型 | 延迟策略 | 延迟（以 cycles 计） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| `default` | Single | Min | 6 | Yes |
| Max | 6 |
| Double | Min | 3 |
| Max | 6 |

**限制**

- 不支持矩阵输入。

### 版本历史

**在 R2006a 之前引入**

#### R2022a：Bit to Integer Converter 模块已添加至 Simulink Logic and Bit Operations 库

Bit to Integer Converter 模块已从 **Communications Toolbox** > **Utility Blocks** 库添加到 **Simulink** > **Logic and Bit Operations** 库。所有现有模型继续正常工作。

## Libraries

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

## Description

The Bit to Integer Converter block maps groups of bits in the input
vector to integers in the output vector.

If *M* is specified by the **Number of bits per
integer(M)** parameter:

- For unsigned integers, the block maps each group of *M*
  bits to an integer in the range [0,
  (2*M* – 1)]. As a result,
  the output vector length is 1/*M* times the input vector
  length.
- For signed integers, the block maps each group of *M*
  bits to an integer in the range
  [(–2*M*-1),
  (2*M* – 1 – 1)].

## Ports

### Input

### **In** — Input signal bit scalar | column vector of bits

Input signal, specified as a scalar or column vector of bits with a
length that is a multiple of the value specified in the **Number
of bits per integer(M)** parameter. The input must be bits
with values of 0 or 1.

**Data Types:** `double`
### Output

### **Out** — Output signal integer | column vector of integers

Output signal, returned as an integer or column vector of integers.
The **After bit packing, treat resulting integer values
as** parameter specifies whether input bits are treated as
unsigned or signed.

- When the input bits are treated as unsigned, each integer
  output is in the range [0,
  (2*M* – 1)].
- When the input bits are treated as signed, each integer output
  is in the range
  [(–2*M*-1),
  (2*M* – 1 –
  1)].

## Parameters

### **Number of bits per integer(M)** — Number of bits per integer `3` (default) | integer in the range [1, 32]

Number of input bits mapped to each integer in the output, specified as an
integer in the range [1, 32].

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `nbits` |
| **Type**: character vector |
| **Values**: integer in the range [1, 32] |
| **Default**: `'3'` |

### **Input bit order** — Input bit order `MSB first` (default) | `LSB first`

Input bit order, specified as `'MSB first'` or
`'LSB first'`.

- `'MSB first'` –– First bit of the input
  signal is the most significant bit (MSB).
- `'LSB first'` –– First bit of the input
  signal is the least significant bit (LSB).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `bitOrder` |
| **Type**: character vector |
| **Values**: `'MSB first'` | `'LSB first'` |
| **Default**: `'MSB first'` |

### **After bit packing, treat resulting integer values as** — Flag for signed integer values after bit packing `Unsigned` (default) | `Signed`

Specify whether the resulting integer values are treated as signed or
unsigned after bit packing. This parameter setting determines which
**Output data type** selections are available.

**Tip**

When this parameter is set to `Unsigned` and
the block has an overflow, the block behaves as though **After
bit packing, treat resulting integer values as** is set to
`Signed`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `signedOutputValues` |
| **Type**: character vector |
| **Values**: `'Unsigned'` | `'Signed'` |
| **Default**: `'Unsigned'` |

### **Output data type** — Output data type `Inherit via internal rule` (default) | `Smallest integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

The **Output data type** options change depending on the
desired signedness of the output.

If the output integers are `Signed`, you can
choose from the following **Output data type** options:

- `Inherit via internal rule`
- `Smallest integer`
- `double`
- `single`
- `int8`
- `int16`
- `int32`

If the output integers are `Unsigned`, you can
choose from the following options in addition to the
`Signed` options:

- `Same as input`
- `uint8`
- `uint16`
- `uint32`

When you set the parameter to `Inherit via internal
rule`, the block determines the output data type based on
the input data type.

- If the input signal is floating-point (either
  `double` or
  `single`), the output data type is
  the same as the input data type.
- If the input data type is not floating-point, the output data
  type is determined as if the parameter is set to
  `Smallest integer`.

When you set the parameter to `Smallest
integer`, the block selects the output data type based on
the settings used in the Hardware Implementation Pane of
the Configuration Parameters dialog box.

- If you select `ASIC/FPGA` for the
  device vendor, the output data type is the smallest ideal
  integer or fixed-point data type, based on the setting for the
  **Number of bits per integer(M)**
  parameter.
- For all other device vendor selections, the output data type
  is the smallest available (signed or unsigned) integer word
  length that is large enough to fit the ideal minimum bit
  size.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `outDtype` |
| **Type**: character vector |
| **Values**: `'Inherit via internal rule'` | `'Smallest integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` |
| **Default**: `'Inherit via internal rule'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Fixed-point inputs must be ufix(1).  b ufix(N) or sfix(N) when ASIC/FPGA is selected in the Hardware Implementation Pane and output data-type is set to either (a) Smallest integer or, (b) Inherit via internal rule and at the same time input is non floating-point. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized
logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `MAX`, `MIN`, `CUSTOM`, or `ZERO` latency for floating-point types. See LatencyStrategy (HDL Coder). |
| **CustomLatency** | When **LatencyStrategy** is set to `CUSTOM` and use this property to specify a custom latency value between `ZERO` and `MAX`. See NFPCustomLatency (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector | Yes | Single  Double | Yes | Yes | Yes | No |

**Latency Details**

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

**Floating-Point Latency**

| Architecture | Floating-Point Type | Latency Strategy | Latency (in cycles) | Custom Latency Support |
| --- | --- | --- | --- | --- |
| `default` | Single | Min | 6 | Yes |
| Max | 6 |
| Double | Min | 3 |
| Max | 6 |

**Restrictions**

- Matrix input is not supported.

## Version History

**Introduced before R2006a**

### R2022a: Bit to Integer Converter Block Added to Simulink Logic and Bit Operations Library

The Bit to Integer Converter block has been added from the **Communications Toolbox** > **Utility Blocks** library to the **Simulink** > **Logic and Bit Operations** library. All existing models continue to work.
