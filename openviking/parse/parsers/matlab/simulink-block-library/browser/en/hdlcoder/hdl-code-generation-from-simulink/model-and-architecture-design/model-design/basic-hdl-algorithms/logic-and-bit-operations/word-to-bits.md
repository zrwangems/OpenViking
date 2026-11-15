---
type: simulink-block
title: 'Word to Bits'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / Logic and Bit Operations'
documentation_page: 'wordtobits'
documentation_source_path: 'ref/wordtobits.html'
language: en
---

# Word to Bits

## Ports

### Input

### **In** — Input signal scalar

Input signal, specified as a scalar. The word-length must be less than or equal to
the **Maximum Word Length** parameter.

**Example:** `72`

**Example:** `5.5`

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Out** — Output signal binary-valued scalar | binary-valued vector

Output signal, returned as a binary-valued scalar or vector. Set the length of
this vector in the **Maximum Word Length** parameter. The block
treats the first element of the output vector as the LSB and treats subsequent bits as
the next significant bits in ascending order.

**Data Types:** `ufix1`

## Parameters

### **Maximum Word Length** — Maximum output word length `64` (default) | integer in the range [1, 65535]

Maximum output word length, specified as an integer in the range [1, 65535]. The
parameter value must be greater than or equal to the input signal word-length.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `maxWordLength` |
| **Type:** character vector |
| **Value:** Integer in the range [1, 65535] |
| **Default:** `'64'` |

### **Output bit order** — Output bit order `LSB first` (default) | `MSB first`

Define whether the first bit of the output signal is the most significant bit (MSB)
or the least significant bit (LSB).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `bitOrder` |
| **Type**: character vector |
| **Values**: `'LSB first'` | `'MSB first'` |
| **Default**: `'LSB first'` |

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
| **In** | Scalar | Yes | No | Yes | No | No | No |

**Restrictions**

- Matrix input is not supported.

## Version History

**Introduced in R2023a**

### R2024b: Maximum word length is 65535 bits

The **Maximum Word Length** block parameter supports maximum word
length of 65535 bits. Prior to R2024b, the maximum word length was 128 bits.

## Description

Converts real numbers to vector of bits

The Word to Bits block converts a real number of word length *N* to a
vector of bits. The output of the block is a vector whose length you specify in the
**Maximum Word Length** parameter.

The block treats the first element of the output vector as the least significant bit (LSB)
and treats subsequent bits as the next significant bits in ascending order.

This figure shows the conversion of the unsigned integer 72 to its binary representation
when you specify a maximum word length of 8. You can also convert a signed integer value to
its corresponding binary vector.

Word to Bits Conversion

This figure shows the conversion of the non-integer value 5.5 to its binary
representation. The output is a binary representation of the stored integer value of 5.5. To
determine stored integer value of a fixed-point real number, use `storedInteger` function.

Convert Real Numbers to Bit Vector
