---
type: simulink-block
title: 'Bit Shift'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / Logic and Bit Operations'
documentation_page: 'bitshift'
documentation_source_path: 'ref/bitshift.html'
language: en
---

# Bit Shift

## Ports

### Input

### **Port\_1** — Input Signal scalar | vector

Input signal on which the logical or arithmetic shift is performed.

- Minimum bit width: 2
- Maximum bit width: 128

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output Signal scalar | vector

Output signal that is logically or arithmetically shifted. The output
signal has the same data type and bit width as the input signal.

- Minimum bit width: 2
- Maximum bit width: 65535

## Parameters

### **Shift Mode** — Type and direction of shift `Shift Left Logical` (default) | `Shift Right Logical` | `Shift Right Arithmetic`

Specifies the type and direction of shift.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `mode` |
| **Type:** string scalar | character vector |
| **Value:** `"Shift Left Logical"` | `"Shift Right Logical"` | `"Shift Right Arithmetic"` |
| **Default:** `'Shift Left Logical'` |

### **Shift Length** — Number of bits to be shifted `0` (default)

Specifies the number of bits to be shifted. Specify a value greater than
or equal to zero.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `N` |
| **Type:** string scalar | character vector |
| **Value:** A value greater than or equal to zero |
| **Default:** `'0'` |

## Libraries

HDL Coder / Logic and Bit Operations

## Block Characteristics

Not documented in R2025b.

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
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |

## Version History

**Introduced in R2014a**

### R2024b: Maximum bit width is 65535 bits

The maximum bit width of the output signal is 65535 bits. Prior to R2024b, the
maximum bit width was 128 bits.

## Description

Logical or arithmetic shift of input signal

The Bit Shift block performs a logical or arithmetic shift on the input
signal.

This block is different from the Shift Arithmetic block in terms of
simulation and HDL code generation behavior. The Bit Shift block can
perform logical shifting of a signed number without having to perform a `reinterpretcast` operation. This
block uses a MATLAB Function block based implementation and might be
slower in operation.

The Shift Arithmetic block shifts the bits or binary point of the input
number. This block has additional block options for HDL code generation in comparison to
the Bit Shift block. When you want to perform a variable shift operation,
use the Shift Arithmetic block instead of the Bit Shift
block. If you have a signed number as input, the block performs a sign extension of the
number. The Shift Arithmetic block requires using additional Data Type Conversion blocks that have the `Stored Integer
(SI)` option selected.
