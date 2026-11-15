---
type: simulink-block
title: 'Integer to Bit Converter'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'integertobitconverter'
---

# Integer to Bit Converter

Map vector of integers to vector of bits

## 中文

将整数向量映射为位向量

### 库

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

### 描述

Integer to Bit Converter 模块将输入向量中的每个整数（或定点值）映射到输出向量中的一组位。

此模块是单速率和单通道的。该模块将每个整数值（或使用定点输入时的存储整数）映射到一组 *M* 个位，并使用 **输出位顺序** 的选择确定最高有效位。生成的输出向量长度是输入向量长度的 *M* 倍。

### 端口

#### 输入

#### **In** — 输入信号 整数 | 整数列向量

输入信号，指定为整数或长度为 *N* 的整数列向量。

如果 *M* 由 **每个整数的位数(M)** 参数指定：

- 当 **每个整数的位数** 参数设置为 `Unsigned` 时，输入值必须是范围 [0, (2*M* – 1)] 内的整数。
- 当 **每个整数的位数** 参数设置为 `Signed` 时，输入值必须是范围 [(–2*M*-1), (2*M* – 1 – 1)] 内的整数。

在仿真期间，此模块执行运行时检查，如果任何输入值超出相应范围，则会发出错误。当此模块生成代码时，它不会执行此运行时检查。

**数据类型：** `double`
#### 输出

#### **Out** — 输出信号 位标量 | 位列向量

输出信号，返回为标量或长度为 *M·N* 的位列向量。

### 参数

#### **每个整数的位数(M)** — 每个整数的位数 `3`（默认） | 范围 [1, 32] 内的整数

映射到输入中每个整数的输入位数，指定为范围 [1, 32] 内的整数。

#### 编程使用

|  |
| --- |
| **模块参数**：`nbits` |
| **类型**：字符向量 |
| **值**：范围 [1, 32] 内的整数 |
| **默认值**：`'3'` |

#### **将输入值视为** — 将输入值视为 `Unsigned`（默认） | `Signed`

指示是否应将整数值输入范围视为有符号或无符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`signedInputValues` |
| **类型**：字符向量 |
| **值**：`'Unsigned'` | `'Signed'` |
| **默认值**：`'Unsigned'` |

#### **输出位顺序** — 输出位顺序 `MSB first`（默认） | `LSB first`

定义输出信号的第一位是最高有效位 (MSB) 还是最低有效位 (LSB)。

#### 编程使用

|  |
| --- |
| **模块参数**：`bitOrder` |
| **类型**：字符向量 |
| **值**：`'MSB first'` | `'LSB first'` |
| **默认值**：`'MSB first'` |

#### **输出数据类型** — 输出数据类型 `Inherit via internal rule`（默认） | `Smallest unsigned integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定输出位的数据类型。您可以选择以下 **输出数据类型** 选项之一：

- `Inherit via internal rule` –– 此模块根据输入数据类型确定输出数据类型。

  - 如果输入信号为浮点型（`single` 或 `double`），则输出数据类型与输入数据类型相同。
  - 如果输入数据类型不是浮点型，则输出数据类型的确定方式如同该参数设置为 `Smallest integer`。
- `Smallest integer` ––此模块根据 Configuration Parameters 对话框的 Hardware Implementation Pane 中使用的设置选择输出数据类型。

  - 如果为设备供应商选择 `ASIC/FPGA`，则输出数据类型为理想的一位大小 (ufix1)。
  - 对于所有其他设备供应商选择，输出数据类型为具有最小可用字长的无符号整数，如 Hardware Implementation 设置中所定义（例如 uint8）
- `Same as input`
- `double`
- `single`
- `uint8`
- `uint16`
- `uint32`

#### 编程使用

|  |
| --- |
| **模块参数**：`outDtype` |
| **类型**：字符向量 |
| **值**：`'Inherit via internal rule'` | `'Smallest unsigned integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'`| `'boolean'` |
| **默认值**：`'Inherit via internal rule'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 仅当在 Hardware Implementation Pane 中选择 ASIC/FPGA 时，输出才为 ufix(1)。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点类型的 `MAX`、`MIN`、`CUSTOM` 或 `ZERO` 延迟。请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。请参阅 NFPCustomLatency (HDL Coder)。 |

**数据类型支持**

此模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | Boolean | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量 | Yes | Single  Double | Yes | Yes | Yes | No |

**延迟详细信息**

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

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

#### R2022a: Integer to Bit Converter 模块已添加到 Simulink Logic and Bit Operations 库

Integer to Bit Converter 模块已从 **Communications Toolbox** > **Utility Blocks** 库添加到 **Simulink** > **Logic and Bit Operations** 库。所有现有模型继续正常工作。

## Libraries

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

## Description

The Integer to Bit Converter block maps each integer (or fixed-point value)
in the input vector to a group of bits in the output vector.

This block is single-rate and single-channel. The block maps each integer value (or stored
integer when you use a fixed point input) to a group of *M* bits, using the
selection for the **Output bit order** to determine the most significant bit.
The resulting output vector length is *M* times the input vector length.

## Ports

### Input

### **In** — Input signal integer | column vector of integers

Input signal, specified as an integer or a length *N* column vector of
integers.

If *M* is specified by the **Number of bits per
integer(M)** parameter:

- When the **Number of bits per integer** parameter is set to
  `Unsigned`, input values must be integers in the range [0,
  (2*M* – 1)].
- When the **Number of bits per integer** parameter is set to
  `Signed`, input values must be integers in the range
  [(–2*M*-1),
  (2*M* – 1 – 1)].

During simulation, the block performs a run-time check and issues an error if any input
value is outside of the appropriate range. When the block generates code, it does not perform
this run-time check.

**Data Types:** `double`
### Output

### **Out** — Output signal bit scalar | column vector of bits

Output signal, returned as a scalar or column vector of bits of length
*M·N*.

## Parameters

### **Number of bits per integer(M)** — Number of bits per integer `3` (default) | integer in the range [1, 32]

Number of input bits mapped to each integer in the input, specified as an integer in the
range [1, 32].

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `nbits` |
| **Type**: character vector |
| **Values**: integer in the range [1, 32] |
| **Default**: `'3'` |

### **Treat input values as** — Treat input values as `Unsigned` (default) | `Signed`

Indicate if the integer value input ranges should be treated as signed or
unsigned.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `signedInputValues` |
| **Type**: character vector |
| **Values**: `'Unsigned'` | `'Signed'` |
| **Default**: `'Unsigned'` |

### **Output bit order** — Output bit order `MSB first` (default) | `LSB first`

Define whether the first bit of the output signal is the most significant bit (MSB) or
the least significant bit (LSB).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `bitOrder` |
| **Type**: character vector |
| **Values**: `'MSB first'` | `'LSB first'` |
| **Default**: `'MSB first'` |

### **Output data type** — Output data type `Inherit via internal rule` (default) | `Smallest unsigned integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify the data type of the output bits. You can choose one of the following
**Output data type** options:

- `Inherit via internal rule` –– The block determines the
  output data type based on the input data type.

  - If the input signal is floating-point (either `single` or
    `double`), the output data type is the same as the input data
    type.
  - If the input data type is not floating-point, the output data type is determined as
    if the parameter is set to `Smallest integer`.
- `Smallest integer` ––The block selects the output data type
  based on settings used in the Hardware Implementation Pane of the Configuration
  Parameters dialog box.

  - If you select `ASIC/FPGA` for the device vendor, the
    output data type is the ideal one-bit size (ufix1).
  - For all other device vendor selections, the output data type is an unsigned integer
    with the smallest available word length, as defined in the Hardware Implementation
    settings (for example, uint8)
- `Same as input`
- `double`
- `single`
- `uint8`
- `uint16`
- `uint32`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `outDtype` |
| **Type**: character vector |
| **Values**: `'Inherit via internal rule'` | `'Smallest unsigned integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'`| `'boolean'` |
| **Default**: `'Inherit via internal rule'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a ufix(1) only at the output when ASIC/FPGA is selected in the Hardware Implementation Pane. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized logic.

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

### R2022a: Integer to Bit Converter Block Added to Simulink Logic and Bit Operations Library

The Integer to Bit Converter block has been added from the **Communications Toolbox** > **Utility Blocks** library to the **Simulink** > **Logic and Bit Operations** library. All existing models continue to work.
