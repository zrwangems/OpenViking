---
type: simulink-block
title: 'LTE CRC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ltecrcdecoder'
documentation_source_path: 'ref/ltecrcdecoder.html'
language: en
---

# LTE CRC Decoder

## Ports

### Input

### **data** — Input sample binary scalar | unsigned integer scalar | binary vector

Input sample, specified as a binary scalar, unsigned integer scalar,
or binary vector. The vector size must be less than or equal to the
length of the polynomial. The CRC length also must be divisible by the
vector size. For example, for polynomial type
`CRC24A`, the valid vector sizes are 24,
12, 8, 6, 4, 3, 2, and 1. An integer input is interpreted as a binary
word. For example, vector input `[0 0 0 1 0 0 1 1]` is
equivalent to `uint8` input
`19`.

`double` and `single` are supported
for simulation but not for HDL code generation.

**Data Types:** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32`

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

### **data** — Output sample binary scalar | integer scalar | binary vector

Output sample, returned a binary scalar, unsigned integer scalar, or
binary vector of the same data type and size as the input samples. The
checksum is removed from the end of the frame.

`double` and `single` binary values
are supported for simulation but not for HDL code generation.

**Data Types:** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32` | `ufixN`

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

### **err** — Indicator of checksum mismatch binary scalar | integer scalar

Indicator of checksum mismatch, returned as a binary scalar or an
integer scalar. If you select **Full checksum
mismatch**, this port returns the integer XOR result of the
calculated checksum against the appended checksum. The
**err** value is valid when
**ctrl**.`end` is 1
(`true`). The data type of this port matches the
data type of the input samples.

**Data Types:** `single` | `double` | `Boolean` | `ufix1` | `uint8` | `uint16` | `uint32` | `ufixN`

## Parameters

### **CRC Type** — Encode polynomial `CRC16` (default) | `CRC8` | `CRC24A` | `CRC24B`

The encode polynomial options are the four CRC types described in the LTE
standard TS 36.212 [1], Section
5.1.1.

### **Full checksum mismatch** — Return bit-by-bit mismatch information off (default) | on

When this parameter is not selected, the **err** port
returns a Boolean value indicating whether any checksum bits are mismatched,
after applying **CRC Mask**. When this parameter is
selected, the **err** port returns an integer that
represents the locations of bit mismatches in the checksum.

### **CRC Mask** — Mask applied to checksum 0 (default) | integer from 0 to 2*CRCLength* – 1

Mask applied to checksum, specified as an integer representing a binary
word from 0 to 2*CRCLength* – 1.
This mask is typically a Radio Network Temporary Identifier (RNTI).

#### Dependencies

This parameter appears when **Full checksum
mismatch** is cleared.

## Libraries

Wireless HDL Toolbox / Error Detection and Correction

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2017b**

## Description

Detect errors in input samples using checksum

The LTE CRC Decoder block calculates a cyclic redundancy check (CRC)
and compares it with the appended checksum, for each frame of streaming data samples.
You can select from the polynomials specified by LTE standard TS 36.212 [1]. The block
provides a hardware-optimized architecture and interface.

This block uses a
streaming sample interface with a bus for related control signals. This interface enables the
block to operate independently of frame size, and to connect easily with other Wireless HDL Toolbox™ blocks. The block accepts and returns a value representing a single sample, and a
bus containing three control signals. These signals indicate the validity of each sample and the
boundaries of the frame. To convert a matrix into a sample stream and these control signals, use
the Frame To Samples block
or the `whdlFramesToSamples`
function. For a full description of the interface, see Streaming Sample Interface.
