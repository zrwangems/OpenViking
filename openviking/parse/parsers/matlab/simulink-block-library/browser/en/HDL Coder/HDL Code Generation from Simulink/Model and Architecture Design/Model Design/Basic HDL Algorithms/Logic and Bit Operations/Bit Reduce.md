---
type: simulink-block
title: 'Bit Reduce'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / Logic and Bit Operations'
documentation_page: 'bitreduce'
documentation_source_path: 'ref/bitreduce.html'
language: en
---

# Bit Reduce

## Ports

### Input

### **Port\_1** — Input Signal scalar | vector

Input signal on which the bit-reduction operation is performed.

- Minimum bit width: 2
- Maximum bit width: 128

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output Signal scalar | vector

Output signal that is bit-reduced.

**Data Types:** `ufix1`

## Parameters

### **Reduction Mode** — Reduction operation on input `AND` (default) | `OR` | `XOR`

Specifies the reduction operation:

- `AND` (default): Perform a bitwise AND reduction of
  the input signal.
- `OR`: Perform a bitwise OR reduction of the input
  signal.
- `XOR`: Perform a bitwise XOR reduction of the input
  signal.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `mode` |
| **Type:** string scalar | character vector |
| **Value:** `"AND"` | `"OR"` | `"XOR"` |
| **Default:** `'AND'` |

## Libraries

HDL Coder / Logic and Bit Operations

## Block Characteristics

Not documented in R2025b.

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
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |

## Version History

**Introduced in R2014a**

## Description

AND, OR, or XOR bit reduction on all input signal bits to single bit

The Bit Reduce block performs a selected bit-reduction operation (AND, OR,
or XOR) on all the bits of the input signal, for a single-bit
result.
