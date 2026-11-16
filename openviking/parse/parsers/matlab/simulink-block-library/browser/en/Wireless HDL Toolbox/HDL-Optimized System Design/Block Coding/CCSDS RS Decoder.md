---
type: simulink-block
title: 'CCSDS RS Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Block Coding'
documentation_page: 'ccsdsrsdecoder'
documentation_source_path: 'ref/ccsdsrsdecoder.html'
language: en
---

# CCSDS RS Decoder

## Ports

### Input

### **data** — Input codeword data integer in the range from 0 to 255

Input codeword data, specified as an integer in the range from 0 to 255. This
integer represents a symbol.

The block accepts a maximum value of 255 x *I* and a minimum
value of (255 – *k* + 1) x *I* for the number of
input codeword symbols per frame. *k* is the message length specified
by the **Message length (k)** parameter. *I* is the
interleaving depth specified by the **Interleaving depth (I)**
parameter. The number of input codeword symbols must be an integral multiple of
*I*.

The block supports back-to-back input frames for:

- Full-length codes when you set **Message length (k)** to
  `223` and **Interleaving depth (I)**
  to `3`, `4`,
  `5`, or `8`
- Full-length codes when you set **Message length (k)** to
  `239` and **Interleaving depth (I)**
  to `1`, `2`,
  `3`, `4`,
  `5`, or `8`

The block does not support back-to-back input frames for:

- Shortened codes for any of the **Message length (k)** and
  **Interleaving depth (I)** values
- Full-length codes when you set **Message length (k)** to
  `223` and **Interleaving depth (I)**
  to `1` or `2`

`double` and `single` data types are allowed for
simulation, but not for HDL code generation. For HDL code generation, specify this
value in `fixdt(0,8,0)` or `uint8` format.

**Data Types:** `double` | `single` | `uint8` | `fixdt(0,8,0)`

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

### **data** — Decoded message data integer in the range from 0 to 255

Decoded message data, returned as an integer in the range from 0 to 255. The
output data type is the same as the input data type.

The block outputs *N* – (255 – *k*) x
*I* number of decoded message symbols for *N*
number of input codeword symbols. *k* is the message length specified
by the **Message length (k)** parameter and *I* is
the interleaving depth specified by the **Interleaving depth (I)**
parameter.

**Data Types:** `double` | `single` | `uint8` | `fixdt(0,8,0)`

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

### **err** — Indication of corruption in output data Boolean scalar

Indication of corruption in the output data, returned as a Boolean scalar.

When this value is `1`, the output contains errors. When this
value is `0`, the output contains zero errors.

If the number of symbol errors in the input codeword data is greater than (255 -
*k*) x *I* / 2, the block outputs data without
correcting the errors and sets the **err** port to
`1` to indicate that errors that cannot be corrected exist in the
input codeword data. *k* is the message length specified by
**Message length (k)** parameter.

**Data Types:** `Boolean`

### **nextFrame** — Block ready indicator Boolean scalar

Block ready indicator, returned as a Boolean scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`

### **numCorrErr** — Number of corrected errors nonnegative scalar

Number of corrected errors, returned as a nonnegative scalar.

The maximum number of errors that the block can correct is equal to (255 –
*k*) x *I* / 2. If the number of errors in the
input codeword data is greater than (255 – *k*) x
*I* / 2, the block outputs data without correcting the errors and
sets the **numCorrErr** port to `0` to indicate that
none of those errors can be corrected.

The block sets the **numCorrErr** port to `0`
when the **err** port is `1`.

#### Dependencies

To enable this port, select the **Output number of corrected symbol
errors** parameter.

**Data Types:** `uint8`

## Parameters

### **Message length (k)** — Length of message `223` (default) | `239`

Select the message length.

### **Interleaving depth (I)** — Depth of interleaving `1` (default) | `2` | `3` | `4` | `5` | `8`

Select the interleaving depth.

### **Output number of corrected symbol errors** — Number of corrected symbol errors `off` (default) | `on`

Select this parameter to enable the **numCorrErr** output port.
This port outputs the number of corrected errors.

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

**Introduced in R2021b**

## Description

Decode and recover message from RS codeword according to CCSDS standard

The CCSDS RS Decoder block decodes and recovers a message from a
Reed-Solomon (RS) codeword according to the Consultative Committee for Space Data Systems
(CCSDS) standard [1]. The block accepts codeword
data and a `samplecontrol` bus and outputs a decoded message data, a
`samplecontrol` bus, control signals that indicate whether the decoded data
is corrupted and whether the block is ready to accept data, and an optional signal to provide
the number of corrected errors. The block provides an architecture suitable for HDL code
generation and hardware deployment.

Because the latency of the block varies, the block provides the output port
**nextFrame** that indicates when the block is ready to accept new input
codeword data. For more details about the latency of the block, see the Algorithm section.

The block also supports shortened message lengths. You can use this block in a CCSDS
receiver for satellite communication.
