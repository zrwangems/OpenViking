---
type: simulink-block
title: 'RS Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Block Coding'
documentation_page: 'rsencoder'
documentation_source_path: 'ref/rsencoder.html'
language: en
---

# RS Encoder

## Ports

### Input

### **data** — Input message data scalar

Input message data, specified as a scalar representing one symbol.

The input word length must be an unsigned integer equal to
`ceil`(log2(**Codeword length
(N)**)). For an input data word length of `3`, the
codeword length parameter, **Codeword length (N)**, must be
`7`.

`double` and `single` data types are allowed for
simulation, but not for HDL code generation.

**Data Types:** `double` | `single` | `uint8` | `uint16` | `fixed point`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, specified as a
`samplecontrol` bus. The bus includes the `start`,
`end`, and `valid` control signals, which indicate the
boundaries of the frame and the validity of the samples.

- `start` — Indicates the start of the input frame
- `end` — Indicates the end of the input frame
- `valid` — Indicates that the data on the input
  **data** port is valid

For more details, see Sample Control Bus.

**Data Types:** `bus`
### Output

### **data** — Encoded codeword data scalar

Encoded codeword data, returned as a scalar. This output data width is same as the
input data width.

**Data Types:** `double` | `single` | `uint8` | `uint16` | `fixed point`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, returned as a `samplecontrol`
bus. The bus includes the `start`, `end`, and
`valid` control signals, which indicate the boundaries of the frame
and the validity of the samples.

- `start` — Indicates the start of the output
  frame
- `end` — Indicates the end of the output frame
- `valid` — Indicates that the data on the output
  **data** port is valid

For more details, see Sample Control Bus.

**Data Types:** `bus`

### **nextFrame** — Block ready indicator scalar

Block ready indicator, returned as a scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`

## Parameters

### **Codeword length (N)** — Length of codeword `7` (default) | integer in the range from 7 to 65,535

Specify the codeword length.

The codeword length must be an integer equal to
2*M* – 1, where *M* is an
integer in the range from 3 to 16. For more information on representing data for RS
codes, see Integer Format (Reed-Solomon Only).

### **Message length (K)** — Length of message `3` (default) | integer in the range from 3 to (**Codeword length (N)** – `2`)

Specify the message length.

For more information on representing data for RS codes, see Integer Format (Reed-Solomon Only).

### **Source of primitive polynomial** — Primitive polynomial source `Auto` (default) | `Property`

Specify the source of the primitive polynomial.

- Select `Auto` to specify the primitive polynomial based
  on the **Codeword length (N)** parameter value. The degree of the
  primitive polynomial is calculated as *M* =
  `ceil`(log2(**Codeword length
  (N)**)).
- Select `Property` to specify the primitive polynomial
  using the **Primitive polynomial** parameter.

### **Primitive polynomial** — Primitive polynomial `[1 0 1 1]` (default) | binary row vector

Specify a binary row vector representing the primitive polynomial in descending
order of powers.

For more information on how to specify a primitive polynomial, see Primitive Polynomials and Element Representations.

#### Dependencies

To enable this parameter, set the **Source of primitive
polynomial** parameter to `Property`.

### **Source of B, the starting power for roots of the primitive polynomial** — Source of starting power for roots of primitive polynomial `Auto` (default) | `Property`

Specify the source of the starting power for roots of the primitive
polynomial.

- Select `Auto` to use the default **B
  value** parameter value, `1`.
- Select `Property` to enable the **B
  value** parameter.

### **B value** — Starting power for roots of primitive polynomial `1` (default) | positive integer

Specify the starting power for roots of the primitive polynomial.

#### Dependencies

To enable this parameter, set the **Source of B, the starting power for
roots of the primitive polynomial** parameter to
`Property`.

### **Enable puncturing** — Puncture pattern source `off` (default) | `on`

Select this parameter to enable the **Puncture pattern vector**
parameter.

### **Puncture pattern vector** — Puncture vector `[1; 1; 0; 0]` (default) | binary column vector

Specify a binary column vector of length **Codeword length (N)** –
**Message length (N)**. A value of `1` indicates
that the block data symbol is not punctured, and remained unchanged from the data
stream. A value of `0` indicates that the data symbol is punctured, or
removed, from the data stream.

#### Dependencies

To enable this parameter, select the **Enable puncturing**
parameter.

## Libraries

Wireless HDL Toolbox / Error Detection and Correction

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

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

## Version History

**Introduced in R2020b**

## Description

Encode message to RS codeword

The RS Encoder block encodes message data to a Reed-Solomon (RS) codeword.
The block accepts message data and a `samplecontrol` bus and outputs codeword
data symbols and a `samplecontrol` bus.

Because the latency of the block varies, the block provides output port
**nextFrame** that indicates when the block is ready to accept new input
message data. The block provides an architecture suitable for HDL code generation and hardware
deployment and supports shortened message lengths.

You can use this block to model many communication system forward error correcting (FEC)
codes. The block supports digital subscriber line (DSL), WiMAX (802.16 m and e), digital video
broadcast handheld (DVB-H) terminals, digital video broadcast satellite (DVB-S) services, and
digital video broadcast satellite services to handheld (DVB-SH) devices below 3 MHz.
