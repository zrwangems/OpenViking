---
type: simulink-block
title: 'CCSDS RS Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ccsdsrsencoder'
documentation_source_path: 'ref/ccsdsrsencoder.html'
language: en
---

# CCSDS RS Encoder

## Ports
```yaml
ports:
- name: data
  summary: Input message symbols integer in the range 0 to 255
  direction: input
  data_types: double | single | uint8 | fixdt(0,8,0)
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: data
  summary: Encoded codeword symbols integer in the range 0 to 255
  direction: output
  data_types: double | single | uint8 | fixdt(0,8,0)
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: nextFrame
  summary: Block ready indicator Boolean scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input message symbols integer in the range 0 to 255

Input message symbols, specified as an integer in the range 0 to 255. Every
integer represents a symbol.

The number of input message symbols per frame must be equal to
*p* × *I*, where *p* can be any
integer in the range from 1 to *k*. *k* is the
message length and *I* is the interleaving depth specified on the
block mask.

To provide proper outputs, the block requires a minimum frame gap of (255 –
*k*) × *I* clock cycles between the input
frames.

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

### **data** — Encoded codeword symbols integer in the range 0 to 255

Encoded codeword symbols, returned as an integer in the range 0 to 255. The output
data type is the same as the input data type.

The block outputs *N* + (255 – *k*) ×
*I* number of codeword symbols per frame, where
*N* is the number of input message symbols. *k* is
the message length specified using the **Message length (k)**
parameter and *I* is the interleaving depth specified using the
**Interleaving depth (I)** parameter.

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

### **nextFrame** — Block ready indicator Boolean scalar

Block ready indicator, returned as a Boolean scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Message length (k)
  summary: Length of message 223 (default) | 239
  group: ''
- name: Interleaving depth (I)
  summary: Depth of interleaving 1 (default) | 2 | 3 | 4 | 5 | 8
  group: ''
```

### **Message length (k)** — Length of message `223` (default) | `239`

Select the message length.

### **Interleaving depth (I)** — Depth of interleaving `1` (default) | `2` | `3` | `4` | `5` | `8`

Select the interleaving depth.
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

**Introduced in R2022a**

## Description

Encode message into RS codeword according to CCSDS standard

The CCSDS RS Encoder block encodes message symbols into a Reed-Solomon (RS)
codeword according to the Consultative Committee for Space Data Systems (CCSDS) standard [1]. The block accepts message
symbols and a `samplecontrol` bus and outputs encoded codeword data, a
`samplecontrol` bus, and a **nextFrame** signal that
indicates when the block is ready to accept new input message symbols.

The block also supports shortened message lengths. You can use this block in a CCSDS
transmitter for satellite communication. The block provides an architecture suitable for HDL
code generation and hardware deployment.
