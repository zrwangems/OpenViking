---
type: simulink-block
title: 'LTE Convolutional Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'lteconvolutionalencoder'
documentation_source_path: 'ref/lteconvolutionalencoder.html'
language: en
---

# LTE Convolutional Encoder

## Ports

### Input

### **data** — Input sample scalar

Input sample, specified as a binary scalar. `double` and
`single` are supported for simulation but not for HDL code
generation.

**Data Types:** `single` | `double` | `Boolean` | `ufix1`

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

### **data** — Encoded sample 3-by-1 column vector

Encoded sample, returned as a 3-by-1 column vector. Each encoded
sample is represented by three bits, one from each encoder
polynomial.

The output data type matches the input data type.

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

Maximum input frame size, specified as a positive integer from 6 to
216. This parameter defines the required
amount of frame memory. If you do not specify a power of two, the block uses
the next largest power of two.

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

Encode binary samples using tail-biting convolutional algorithm

The LTE Convolutional Encoder block implements the encoding polynomials
specified by LTE standard TS 36.212 [1]. The convolutional
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

The message size can change dynamically. The encoded output bits for each input bit
are returned as a 3-by-1 vector, `[G0 G1 G2]`.

The block takes *M* + 5 cycles to encode a frame of
*M* samples. Therefore, you must leave *M* + 5
idle cycles between input frames. Alternatively, you can use the output signal
**ctrl**.`end` to determine when the block is
ready for new input.

This waveform shows an input message of 40 samples, with 45 idle cycles between
frames. The output data is a vector of three encoded bits. The input and output
**ctrl** buses are expanded to show the control signals.
`start` and `end` show the frame boundaries, and
`valid` qualifies the data samples.
