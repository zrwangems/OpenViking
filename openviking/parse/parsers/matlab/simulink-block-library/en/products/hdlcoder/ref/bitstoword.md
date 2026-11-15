---
type: simulink-block
title: 'Bits to Word'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / Logic and Bit Operations'
documentation_page: 'bitstoword'
documentation_source_path: 'ref/bitstoword.html'
language: en
---

# Bits to Word

## Ports

### Input

### **In** — Input signal binary-valued scalar | binary-valued vector

Input signal to the block, specified as binary-valued scalar or vector. You can
specify a vector containing up to 128 elements.

**Example:**
`[0 1 1 0 0 1 1 1]`

**Data Types:** `fixdt(0,1,0)`
### Output

### **Out** — Output signal scalar

*N*-bit integer, where *N* is the size of the
input vector, returned as a nonnegative scalar. For example, when you specify a 1-by-8
input signal, then the output signal is an unsigned integer with the
`ufix8` data type.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Input bit order** — Input bit order `LSB first` (default) | `MSB first`

Input bit order, specified as `'MSB first'` or `'LSB
first'`.

- `'MSB first'` –– First bit of the input signal is the most
  significant bit (MSB).
- `'LSB first'` –– First bit of the input signal is the least
  significant bit (LSB).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `bitOrder` |
| **Type**: character vector |
| **Values**: `'LSB first'` | `'MSB first'` |
| **Default**: `'LSB first'` |

### **After bit packing, treat resulting integer values as** — Flag for signed integer values after bit packing `Unsigned` (default) | `Signed`

Specify whether the resulting integer values are treated as signed or unsigned after
bit packing.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `signedOutputValues` |
| **Type**: character vector |
| **Values**: `'Unsigned'` | `'Signed'` |
| **Default**: `'Unsigned'` |

## Libraries

HDL Coder / Logic and Bit Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

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

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector | `ufix1` | No | No | No | No | No |

**Restrictions**

- Matrix input is not supported.

## Version History

**Introduced in R2023a**

## Description

Convert vector of bits to integer

The Bits to Word block converts a length-*N* input vector of bits to an
*N*-bit integer. The output of the block is an unsigned integer that has
word length *N*.

The block treats the first element of the input vector as the least significant bit (LSB)
of the output and treats subsequent bits as the next significant bits in ascending order. This
figure shows the conversion of the bit vector `[1 0 1 1 0]` to the integer
value `13`.

Bit to Integer Conversion
