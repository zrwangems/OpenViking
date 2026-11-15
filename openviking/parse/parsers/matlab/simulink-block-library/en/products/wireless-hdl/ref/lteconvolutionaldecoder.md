---
type: simulink-block
title: 'LTE Convolutional Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Convolutional Coding'
documentation_page: 'lteconvolutionaldecoder'
documentation_source_path: 'ref/lteconvolutionaldecoder.html'
language: en
---

# LTE Convolutional Decoder

## Ports

### Input

### **data** — Input sample 3-by-1 column vector

Input sample, specified as a 3-by-1 column vector. The block performs
soft-decision decoding when the input type is signed fixed point or
signed integer, or performs hard-decision decoding when the input type
is `Boolean` or `fixdt(0,1,0)`. The
block performs unquantized soft-decision decoding for
`single` and `double` types, but
this mode is not supported for HDL code generation.

For a hardware soft-decision implementation, an integer or fixed-point
type that is three or four bits wide is recommended. This input word
length achieves decode performance while optimizing timing and resource
use when the design is synthesized to an FPGA. The input data type must
be less than 16 bits wide. Internal data types are derived from this
data type and lower precision types can result in loss of decoding
performance.

Values less than zero are most likely a logical `0`,
while values greater than zero are most likely a logical
`1`. The absolute value determines the level of
confidence. For example, the table shows the confidence levels used if
the input is `sfix4` (*WL*=4,
*FL*=0).

|  |  |  |  |
| --- | --- | --- | --- |
| **Soft Value** | –8, –7, –6, –5, –4, –3, –2, –1 | 0 | 1, 2, 3, 4, 5, 6, 7 |
| **Logic Level** | logical `0` | unknown | logical `1` |
| **Confidence** | high → low | none | low → high |

**Data Types:** `Boolean` | `fixdt(0,1,0)` | `fixdt(1,WL,FL)` | `int8` | `int16` | `single` | `double`

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

### **data** — Output sample scalar

Output sample, returned as a binary scalar value.

`double` and `single` are supported
for simulation but not for HDL code generation.

**Data Types:** `single` | `double` | `Boolean` | `ufix1`

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

## Parameters

### **Maximum message length** — Maximum input frame size 1024 (default) | positive integer

Maximum input frame size, specified as a positive integer from 6 to 2048.
The block uses this parameter to determine the amount of RAM required to
store intermediate decisions. If you do not specify a power of two, the
block uses the next largest power of two.

If an input frame is larger than the specified maximum message length, the
block returns a warning.

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

This block does not have any HDL Block
Properties.

## Version History

**Introduced in R2017b**

## Description

Decode convolutional-encoded samples using Viterbi algorithm

The LTE Convolutional Decoder block implements a wrap-around Viterbi
algorithm (WAVA) to decode samples encoded with the tail-biting polynomials specified by
LTE standard TS 36.212 [1]. The convolutional
code has constraint length 7 and is tail biting with coding rate 1/3 and octal
polynomials **G0**=133, **G1**=171 and **G2**=165. The block provides a
hardware-optimized architecture and interface.

This block uses a
streaming sample interface with a bus for related control signals. This interface enables the
block to operate independently of frame size, and to connect easily with other Wireless HDL Toolbox™ blocks. The block accepts and returns a value representing a single sample, and a
bus containing three control signals. These signals indicate the validity of each sample and the
boundaries of the frame. To convert a matrix into a sample stream and these control signals, use
the Frame To Samples block
or the `whdlFramesToSamples`
function. For a full description of the interface, see Streaming Sample Interface.

The block accepts input samples representing soft or hard decisions. Each sample is a
3-by-1 vector, where the three values represent the bits encoded by the three
polynomials, `[G0 G1 G2]`.

Decoding of a message of *M* samples requires
2\**M*+140 cycles, assuming contiguous valid input. Therefore, you must
leave at least that many idle cycles between input frames. Alternatively, you can use
the output signal **ctrl**.`end` to determine when the
block is ready for new input.

This waveform shows an input message of 100 samples, with 340 idle cycles between
frames. The input data is a vector of three encoded bits. The input and output
**ctrl** buses are expanded to show the control signals.
`start` and `end` show the frame boundaries, and
`valid` qualifies the data samples.
