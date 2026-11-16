---
type: simulink-block
title: 'NR CRC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrcrcdecoder'
documentation_source_path: 'ref/nrcrcdecoder.html'
language: en
---

# NR CRC Decoder

## Ports

### Input

### **data** — CRC-encoded data binary scalar | binary vector | unsigned integer scalar

CRC-encoded data, specified as a binary scalar, binary vector, or unsigned integer
scalar.

You can specify the input data with one of these options:

- Scalar – Specify an integer representing several bits. For this case, the
  block supports unsigned integer (`uint8`,
  `uint16`, or `ufixN`) and
  `Boolean` data types.
- Vector – Specify a vector of binary values of size *N*. For
  this case, the block supports `Boolean` and
  `ufix1` data types.

*N* is the input data width, and it must be less than or equal to
the length of the CRC polynomial and a factor of the specified CRC polynomial
length.

`double` and `single` data types are supported for
simulation, but not for HDL code generation.

**Example:** For the CRC type `CRC24A`, the valid data widths
are 24, 12, 8, 6, 4, 3, 2, and 1. An integer input is interpreted as a binary word.
For example, when you specify a `uint8` input of
`19`, it is equivalent to a vector input `[0 0 0 1 0 0 1
1]`.

**Data Types:** `double` | `single` | `ufix1` | `uint8` | `uint16` | `Boolean` | `ufixN`

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

### **CRCMask** — CRC checksum mask nonnegative integer

CRC checksum mask, specified as a nonnegative integer representing a binary word
from 0 to 2*CRCLength* – 1, where
*CRCLength* is the length of the CRC polynomial.

This mask is typically a radio network temporary identifier (RNTI). The RNTI is
used to XOR the CRC checksum.

#### Dependencies

To enable this port, set the **CRC type** parameter to
`CRC24C port` and select the **Enable CRC mask
input port** parameter.

**Data Types:** `ufix24`
### Output

### **data** — CRC-decoded data scalar | vector

CRC-decoded data, returned as a scalar or vector. The output data type and size
are the same as the input data.

**Data Types:** `double` | `single` | `ufix1` | `uint8` | `uint16` | `Boolean` | `ufixN`

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

### **err** — Indication of corruption of received data binary or integer scalar

Indication of corruption of the received data, returned as a binary or integer
scalar.

When this value is `1`, the message contains at least one error.
When this value is `0`, the message contains zero errors. This value
is valid when **ctrl.end** is set 1 `true`.

If you select the **Full checksum mismatch**
parameter, this port returns the integer XOR result of the checksum mismatch. This
value is the result of the logical CRC difference between the CRC checksum comprised
in the input and the CRC checksum recalculated across the data part of the input. If
you specify a CRC mask, the block XORs the checksum with the specified CRC
mask.

**Data Types:** `Boolean` | `ufix24`

## Parameters

### **CRC type** — Type of CRC `CRC16` (default) | `CRC6` | `CRC11` | `CRC24A` | `CRC24B` | `CRC24C`

Select the CRC type. Each CRC type indicates a polynomial, as shown in this
table.

| CRC Type | Polynomial |
| --- | --- |
| `CRC6` | [1 1 0 0 0 0 1] |
| `CRC11` | [1 1 1 0 0 0 1 0 0 0 0 1] |
| `CRC16` | [1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1] |
| `CRC24A` | [1 1 0 0 0 0 1 1 0 0 1 0 0 1 1 0 0 1 1 1 1 1 0 1 1] |
| `CRC24B` | [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1] |
| `CRC24C` | [1 1 0 1 1 0 0 1 0 1 0 1 1 0 0 0 1 0 0 0 1 0 1 1 1] |

These CRC polynomials are specified according to 5G new radio (NR) standard 3GPP TS
38.212 [1].

### **Full checksum mismatch** — Enable full checksum `off` (default) | `on`

Select this parameter to enable full checksum.

When you select this parameter, the **err** port
returns an integer that represents the locations of bit mismatches in the CRC checksum
bits. When you clear this parameter, the **err** port
returns a Boolean value indicating whether any CRC checksum bits are mismatched.

### **Enable CRC mask input port** — Enable CRC checksum mask input port `off` (default) | `on`

Select this parameter to enable the **CRCMask** input port.

#### Dependencies

To enable this parameter, set the **CRC type** parameter to
`CRC24C`.

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

**Introduced in R2021a**

## Description

Detect errors in input data using CRC

The NR CRC Decoder block calculates the cyclic redundancy check (CRC)
checksum and compares it with the appended CRC checksum for each frame of streaming data
samples. If the two CRC checksums do not match, the block reports an error. The block accepts
and returns a data sample stream with accompanying control signals. The control signals
indicate the validity of the samples and the boundaries of the frame.

The block supports scalar and vector inputs and outputs data as either a scalar or vector
based on the input data. To achieve higher throughput, the block accepts a binary vector or
unsigned integer scalar input and implements a parallel architecture. The input data width
must be less than or equal to the length of the CRC polynomial, and the length of the CRC
polynomial must be divisible by the input data width. The block supports all CRC polynomials
specified according to the 5G new radio (NR) standard 3GPP TS 38.212 [1]. When you select the CRC24C
polynomial, the block supports dynamic CRC mask.

The block provides an interface and hardware-optimized architecture suitable for HDL code
generation and hardware deployment.
