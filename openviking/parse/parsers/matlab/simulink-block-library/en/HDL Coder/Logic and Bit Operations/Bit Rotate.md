---
type: simulink-block
title: 'Bit Rotate'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitrotate'
documentation_source_path: 'ref/bitrotate.html'
language: en
---

# Bit Rotate

## Ports

### Input

### **Port\_1** — Input Signal scalar | vector

Input signal on which the bit-rotation is performed.

- Minimum bit width: 2
- Maximum bit width: 128

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output Signal scalar | vector

Output signal that is bit-rotated. The output signal has the same data type as the
input signal.

## Parameters

### **Rotate Mode** — Specifies direction of rotation, left or right `Rotate Left` (default) | `Rotate Right`

Specifies direction of rotation, left or right.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `mode` |
| **Type:** string scalar | character vector |
| **Value:** `"Rotate Left"` | `"Rotate Right"` |
| **Default:** `'Rotate Left'` |

### **Rotate Length** — Specifies the number of bits to rotate `0` (default) | integer greater than or equal to zero

Specifies the number of bits to rotate.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `N` |
| **Type:** string scalar | character vector |
| **Value:** integer greater than or equal to zero |
| **Default:** `'0'` |

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

Rotate input signal by bit positions

The Bit Rotate block rotates the input signal left or right by the
specified number of bit positions.
