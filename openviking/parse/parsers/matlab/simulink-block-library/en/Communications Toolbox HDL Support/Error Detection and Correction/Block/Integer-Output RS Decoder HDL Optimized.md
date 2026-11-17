---
type: simulink-block
title: 'Integer-Output RS Decoder HDL Optimized'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'integeroutputrsdecoderhdloptimized'
documentation_source_path: '../comm/ref/integeroutputrsdecoderhdloptimized.html'
language: en
---

# Integer-Output RS Decoder HDL Optimized

## Ports
```yaml
ports:
- name: dataIn
  summary: Input data scalar
  direction: input
  data_types: double | uint8 | uint16 | uint32 | uint64 | fixed point
- name: startIn
  summary: Start of input frame indicator scalar
  direction: input
  data_types: Boolean
- name: endIn
  summary: End of input frame indicator scalar
  direction: input
  data_types: Boolean
- name: validIn
  summary: Valid input data indicator scalar
  direction: input
  data_types: Boolean
- name: dataOut
  summary: Decoded message data scalar
  direction: output
  data_types: double | uint8 | uint16 | uint32 | uint64 | fixed point
- name: startOut
  summary: Start of output frame indicator scalar
  direction: output
  data_types: Boolean
- name: endOut
  summary: End of output frame indicator scalar
  direction: output
  data_types: Boolean
- name: validOut
  summary: Valid output data indicator scalar
  direction: output
  data_types: Boolean
- name: errOut
  summary: Indications of corruption of received data scalar
  direction: output
  data_types: Boolean
- name: numErrors
  summary: Number of corrected errors nonnegative scalar
  direction: output
  data_types: uint8
```

### Input

### **dataIn** — Input data scalar

Input data, specified as a scalar representing one symbol. For binary point
scaling, the input data type must be an unsigned integer or an unsigned fixed point.
The `double` data type is allowed for simulation, but not for HDL
code generation.

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

### **dataOut** — Decoded message data scalar

Decoded message data, returned as a scalar. This output data width is the same as
the input data width.

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

### **errOut** — Indications of corruption of received data scalar

Indications of corruption of the received data, returned as a Boolean
scalar.

When this value is `1` (`true`) , the output
contains at least one error. When this value is `0`
(`false`), the output contains zero errors.

If the number of errors in the input codeword is greater than (**Codeword
length** – **Message length**)/`2`, the
block outputs data without correcting the errors and sets the
**errOut** port to `1` (`true`)
to indicate that errors that cannot be corrected exist in the input codeword.

**Data Types:** `Boolean`

### **numErrors** — Number of corrected errors nonnegative scalar

Number of corrected errors, returned as a nonnegative scalar.

The maximum number of errors an RS code can correct is equal to
(**Codeword length** – **Message length**)/2. If
the number of errors in the input codeword is greater than (**Codeword
length** – **Message length**)/2, the block outputs data
without correcting the errors and sets the **numErrors** port to
`0` to indicate that none of those errors can be corrected.

#### Dependencies

To enable this port, select the **Output number of corrected symbol
errors** parameter.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Codeword length
  summary: Length of codeword 7 (default) | range from 7 to 65, 535
  group: ''
- name: Message length
  summary: Length of message 3 (default) | positive integer
  group: ''
- name: Source of primitive polynomial
  summary: Primitive polynomial source Auto (default) | Property
  group: ''
- name: Primitive polynomial
  summary: Primitive polynomial [ 1 0 1 1 ] (default) | binary row vector
  group: ''
- name: Source of B, the starting power for roots of the primitive polynomial
  summary: Source of starting power for roots of primitive polynomial Auto (default) | Property
  group: ''
- name: B value
  summary: Starting exponent of roots 1 (default) | positive integer
  group: ''
- name: Output number of corrected symbol errors
  summary: Number of corrected symbol errors off (default) | on
  group: ''
```

### **Codeword length** — Length of codeword `7` (default) | range from 7 to 65, 535

Specify the codeword length.

The codeword length `N` must be an integer equal to
2*M* – 1, where *M* is
an integer in the range from 3 to 16. For more information on representing data for RS
codes, see Integer Format (Reed-Solomon Only).

### **Message length** — Length of message `3` (default) | positive integer

Specify the message length.

For more information on representing data for RS codes, see Integer Format (Reed-Solomon Only).

### **Source of primitive polynomial** — Primitive polynomial source `Auto` (default) | `Property`

Specify the source of the primitive polynomial.

- Select `Auto` to specify the primitive polynomial based
  on the **Codeword length** parameter value. The degree of the
  primitive polynomial is calculated as *M* =
  `ceil`(log2(**Codeword
  length**).
- Select `Property` to specify the primitive polynomial
  using the **Primitive polynomial** parameter.

### **Primitive polynomial** — Primitive polynomial `[ 1 0 1 1 ]` (default) | binary row vector

Specify a binary row vector representing the primitive polynomial in descending
order of powers.

For more information on how to specify a primitive polynomial, see Primitive Polynomials and Element Representations.

#### Dependencies

To enable this parameter, set the **Source of primitive
polynomial** parameter to `Property`.

### **Source of B, the starting power for roots of the primitive polynomial** — Source of starting power for roots of primitive polynomial `Auto` (default) | `Property`

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

### **Output number of corrected symbol errors** — Number of corrected symbol errors `off` (default) | `on`

Select this parameter to enable the **numErrors** output port. This
port outputs the number of corrected errors.
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
Integer-Output RS Decoder HDL Optimized block.

## Description

Decode data using Reed-Solomon (RS) decoder

The Integer-Output RS Decoder HDL Optimized block decodes data using RS
decoder. The RS decoding follows the same standards as any other cyclic redundancy code. Use
this block to model communications system forward error correction (FEC) codes. The block
provides an architecture suitable for HDL code generation and hardware deployment.

For more information about the RS decoder, see the Integer-Output RS Decoder block. For more information on representing data for RS
codes, see Integer Format (Reed-Solomon Only).
