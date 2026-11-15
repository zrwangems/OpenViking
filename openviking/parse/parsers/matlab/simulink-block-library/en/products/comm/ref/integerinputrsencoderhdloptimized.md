---
type: simulink-block
title: 'Integer-Input RS Encoder HDL Optimized'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / Reed-Solomon Codes'
documentation_page: 'integerinputrsencoderhdloptimized'
documentation_source_path: 'ref/integerinputrsencoderhdloptimized.html'
language: en
---

# Integer-Input RS Encoder HDL Optimized

## Ports

### Input

### **dataIn** — Input data scalar

Input data, specified as a scalar representing one symbol. For binary point
scaling, the input data type must be an unsigned integer or an unsigned fixed point.
The word length of each symbol must be equal to
`ceil`(log2(**Codeword
length**) + 1. The `double` data type is allowed for
simulation, but not for HDL code generation.

**Data Types:** `double` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **startIn** — Start of input frame indicator scalar

Start of input frame indicator, specified as a Boolean scalar.

**Data Types:** `Boolean`

### **endIn** — End of input frame indicator scalar

End of input frame indicator, specified as a Boolean scalar.

**Data Types:** `Boolean`

### **validIn** — Valid input data indicator scalar

Valid input data indicator, specified as a Boolean scalar.

This is a control signal that indicates if the data on the **dataIn** port is valid.

**Data Types:** `Boolean`
### Output

### **dataOut** — Output data scalar

Output data, returned as a scalar. This output data width is the same as the input
data width.

**Data Types:** `double` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **startOut** — Start of output frame indicator scalar

Start of output frame indicator, returned as a Boolean scalar.

**Data Types:** `Boolean`

### **endOut** — End of output frame indicator scalar

End of output frame indicator, returned as a Boolean scalar.

**Data Types:** `Boolean`

### **validOut** — Valid output data indicator scalar

Valid output data indicator, returned as a Boolean scalar.

This is a control signal that indicates if the data on the **dataOut** port is valid.

**Data Types:** `Boolean`

## Parameters

### **Codeword length** — Length of codeword `7` (default) | range from 7 to 65, 535

Specify the codeword length.

The codeword length `N` must be an integer equal to
2*M* – 1, where *M* is
an integer in the range from 3 to 16. For more information on representing data for RS
codes, see Integer Format (Reed-Solomon Only).

### **Message length** — Length of message `3` (default) | positive integer

Specify the length of the message.

For more information on representing data for RS codes, see Integer Format (Reed-Solomon Only).

Each input frame, that is, the number of valid data samples between
**startIn** and **endIn** port values, must contain
more than *N*– *K* symbols and less than or equal to
*K* symbols. A shortened code is inferred anytime the number of input
data samples in a frame is less than *K*.

### **Source of primitive polynomial** — Primitive polynomial source `Auto` (default) | `Property`

Specify the source of the primitive polynomial.

- Select `Auto` to specify the primitive polynomial based
  on the **Codeword length** parameter value. The degree of the
  primitive polynomial is calculated as *M* =
  `ceil`(log2(**Codeword
  length**).
- Select `Property` to specify the primitive polynomial
  using the **Primitive polynomial** parameter.

### **Primitive polynomial** — Primitive polynomial provider `[ 1 0 1 1 ]` (default) | binary row vector

Specify a binary row vector representing the primitive polynomial in descending
order of powers.

For more information on how to specify a primitive polynomial, see Primitive Polynomials and Element Representations.

#### Dependencies

To enable this parameter, set the **Source of primitive
polynomial** parameter to `Property`.

### **Source of puncture pattern** — Puncture pattern source `None` (default) | `Property`

Select `Property` to enable the **Puncture pattern
vector** parameter.

### **Puncture pattern vector** — Puncture vector `[ones(2,1); zeros(2,1)]` (default) | binary column vector

Specify a column vector of length *N*–*K*. In a
puncture vector, a value of `1` represents that the data symbol passes
unaltered. A value of `0` represents that the data symbol is punctured,
or removed, from the data stream.

#### Dependencies

To enable this parameter, set the **Source of puncture pattern**
parameter to `Property`.

### **Source of B, the starting power for roots of the primitive polynomial** — Starting power for roots of primitive polynomial `Auto` (default) | `Property`

Specify the source of the starting power for roots of the primitive
polynomial.

- Select `Property` to enable the **B
  value** parameter.
- Select `Auto`, to use the **B value**
  parameter default value of `1`.

### **B value** — Starting exponent of roots `1` (default) | positive integer

The starting exponent of the roots.

#### Dependencies

To enable this parameter, set the **Source of B, the starting power for
roots of the primitive polynomial** parameter to
`Property`.

## Libraries

Communications Toolbox HDL Support / Error Detection and Correction / Block

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Not recommended for production code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2012b**

### R2023b: Added resource and performance data synthesis results

Added a new section with resource and performance data synthesis results for the
Integer-Input RS Encoder HDL Optimized block.

## Description

Encode data using a Reed-Solomon (RS) encoder

The Integer-Input RS Encoder HDL Optimized block encodes data using the RS
encoder. The RS encoding follows the same standards as any other cyclic redundancy code. Use
this block to model communications system forward error correction (FEC) codes. The block
provides an architecture suitable for HDL code generation and hardware deployment.

For more information about the RS encoder, see the Integer-Input RS Encoder block. For more information on representing data for RS
codes, see Integer Format (Reed-Solomon Only).
