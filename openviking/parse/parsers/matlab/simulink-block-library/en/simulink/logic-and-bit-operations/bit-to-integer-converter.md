---
type: simulink-block
title: 'Bit to Integer Converter'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Logic and Bit Operations'
documentation_page: 'bittointegerconverter'
documentation_source_path: 'slref/bittointegerconverter.html'
language: en
---

# Bit to Integer Converter

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

## Libraries

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

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

## Description

Map vector of bits to corresponding vector of integers

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
