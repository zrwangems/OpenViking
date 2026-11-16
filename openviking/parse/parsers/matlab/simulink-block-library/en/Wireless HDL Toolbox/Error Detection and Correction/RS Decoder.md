---
type: simulink-block
title: 'RS Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'rsdecoder'
documentation_source_path: 'ref/rsdecoder.html'
language: en
---

# RS Decoder

## Ports

### Input

### **data** — Input codeword data scalar

Input codeword data, specified as a scalar representing one symbol.

The length of the codeword in symbols specified by the **Codeword length
(N)** parameter must be an integer equal to
2*M* – 1, where *M*
is an integer in the range from 3 to 16.

The input data word length must be an unsigned integer equal to
`ceil`(log2(**Codeword length
(N)**)). For a codeword length of `7`, the input data word
length must be 3.

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

### **erasure** — Erasure location scalar

*Since R2024b*

Erasure location, specified as a `Boolean` scalar.

When erasure is `1` it indicates the location where the symbol
is erased in the codeword. When erasure is `0` it indicates the
location where there is no erasure.

#### Dependencies

To enable this port, select the **Enable erasure input port**
parameter.

**Data Types:** `Boolean`
### Output

### **data** — Decoded message data scalar

Decoded message data, returned as a scalar. This output data width is the same as
the input data width.

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

### **err** — Indication of corruption of received data scalar

Indication of corruption of the received data, returned as a scalar.

When this value is `1` (`true`), the output
contains errors. When this value is `0` (`false`),
the output contains zero errors.

If the number of errors in the input codeword is greater than (**Codeword
length (N)** – **Message length (K)**)/2, the block
outputs data without correcting the errors and sets the **err** port
to `1` (`true`) to indicate that errors that cannot
be corrected exist in the input codeword.

**Data Types:**  `Boolean`

### **nextFrame** — Block ready indicator scalar

Block ready indicator, returned as a scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`

### **numErrors** — Number of corrected errors nonnegative scalar

Number of corrected errors, returned as a nonnegative scalar.

The maximum number of errors an RS code can correct is equal to
(**Codeword length (N)** – **Message length
(K)**)/2. If the number of errors in the input codeword is greater than
(**Codeword length (N)** – **Message length
(K)**)/2, the block outputs data without correcting the errors and sets the
**numErrors** port to `0` to indicate that none of
those errors can be corrected.

#### Dependencies

To enable this port, select the **Output number of corrected symbol
errors** parameter.

**Data Types:** `uint8`

## Parameters

### **Codeword length (N)** — Length of codeword `7` (default) | range from 7 to 65,535

Specify the codeword length.

The codeword length `N` must be an integer equal to
2*M* – 1, where *M* is
an integer in the range from 3 to 16. For more information on representing data for RS
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

- Select `Auto`, to use the default **B
  value** parameter value, `1`.
- Select `Property` to enable the **B
  value** parameter.

### **B value** — Starting power of roots `1` (default) | positive integer

Specify the starting power for roots of the primitive polynomial.

#### Dependencies

To enable this parameter, set the **Source of B, the starting power for
roots of the primitive polynomial** parameter to
`Property`.

### **Output number of corrected symbol errors** — Number of corrected symbol errors `off` (default) | `on`

Select this parameter to enable the **numErrors** output port. This
port outputs the number of corrected errors.

### **Enable erasure input port** — Enable erasure input port `off` (default) | `on`

*Since R2024b*

Select this parameter to enable the **erasure** input port.

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

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2020a**

### R2024b: Enable erasure through input port

The RS Decoder block now offers a new parameter that you can use to
enable erasure through an input port. To enable the port, select the **Enable
erasure input port** parameter.

## Description

Decode and recover message from RS codeword

The RS Decoder block decodes and recovers a message from a Reed-Solomon
(RS) codeword. The block accepts codeword data and a `samplecontrol` bus and
(optionally) erasure and outputs a decoded message data, a `samplecontrol`
bus, whether the received data is corrupted, a block ready indicator, and (optionally) the
number of corrected errors. The block provides an architecture suitable for HDL code
generation and hardware deployment and supports shortened message lengths.

Because, the latency of the block varies, the block provides output port
**nextFrame** that indicates when the block is ready to accept new input
codeword data. For more details about latency, see the Algorithms section.

You can use this block to model many communication system forward error correcting (FEC)
codes. The block supports digital subscriber line (DSL), WiMAX (802.16 m and e), digital video
broadcast handheld (DVB-H) terminals, digital video broadcast satellite (DVB-S) services, and
digital video broadcast satellite services to handheld (DVB-SH) devices below 3 MHz.
