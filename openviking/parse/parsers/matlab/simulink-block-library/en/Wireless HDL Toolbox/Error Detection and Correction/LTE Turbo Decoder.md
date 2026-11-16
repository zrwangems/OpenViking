---
type: simulink-block
title: 'LTE Turbo Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'lteturbodecoder'
documentation_source_path: 'ref/lteturbodecoder.html'
language: en
---

# LTE Turbo Decoder

## Ports

### Input

### **data** — Input sample three-element vector

Input sample, specified as a three-element integer vector. The values
represent soft-coded probabilities. If the value is negative, the bit is
more likely to be 0. If the value is positive, the bit is more likely to
be
1.
The first element is the sequential bit, and the other two elements are
parity bits. The block expects input frames of
*BlockSize* + 12 samples. This frame size includes
the tail bits, in the order specified by LTE standard TS 36.212 [1].

For a hardware implementation, use a fixed-point type with two or
three integer bits and one to four fractional bits. Internal data types
are derived from this data type, and lower precision types can result in
loss of decoding precision. If the input data type has zero fractional
bits or less than two integer bits, the block returns a warning.
`double` and `single` are
supported for simulation but not for HDL code generation.

**Data Types:** `fixdt(1,WL,FL)` | `single` | `double`

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

### **blockSize** — Turbo code block size integer

Turbo code block size, specified as an integer. This value must be one of the 188 values
specified in the LTE standard, from 40 to 6144 in these intervals: `[40:8:512
528:16:1024 1056:32:2048 2112:64:6144]`.

#### Dependencies

This port appears when you set **Block size source** to `Input port`.

**Data Types:** `single` | `double` | `uint16` | `fixdt(0,13,0)`
### Output

### **data** — Output sample scalar

Output sample, returned as a binary scalar. `double`
and `single` are supported for simulation but not for
HDL code generation.

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

### **Block size source** — How to specify the block size `Input port` (default) | `Property`

Select whether you specify the block size with an input port or enter a fixed value as
a parameter. If you select `Property`, the **Block
size** parameter appears. If you select `Input
port`, the **blockSize** port appears.

### **Block size** — Turbo code block size `6144` (default)

Turbo code block size, specified as an integer. This value must be one of the
188 values specified in the LTE standard, from 40 through 6144 in these
intervals: `[40:8:512 528:16:1024 1056:32:2048
2112:64:6144]`. This value is registered for each frame,
when **ctrl**.`start` = 1
(`true`).

#### Dependencies

This parameter appears when you set **Block size
source** to
`Property`.

### **Number of decoding iterations** — How many MAX decoding iterations to perform `6` (default) | positive integer

How many MAX decoding iterations to perform, specified as a positive
integer. The decoder implementation uses a single MAX decoder, with the
output data of each half-iteration routed back to the input. A higher
iteration count increases accuracy and adds latency. After about 15
iterations, the algorithm does not provide further accuracy.

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

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder)
or an Enabled Synchronous
Subsystem (HDL Coder).

## Version History

**Introduced in R2017b**

## Description

Decode turbo-encoded samples

The LTE Turbo Decoder block implements the turbo decoder required by
LTE standard TS 36.212 [1] and provides an
interface and architecture optimized for HDL code generation and hardware deployment.
The block iterates over two MAX decoders. You can specify the number of iterations. The
coding rate is 1/3. The block accepts encoded bits as a 3-by-1 vector of soft-coded
values, `[S P1 P2]`. In this vector, `S` is the
systematic bit, and `P1` and `P2` are the parity bits
from the two encoders.

This block uses a
streaming sample interface with a bus for related control signals. This interface enables the
block to operate independently of frame size, and to connect easily with other Wireless HDL Toolbox™ blocks. The block accepts and returns a value representing a single sample, and a
bus containing three control signals. These signals indicate the validity of each sample and the
boundaries of the frame. To convert a matrix into a sample stream and these control signals, use
the Frame To Samples block
or the `whdlFramesToSamples`
function. For a full description of the interface, see Streaming Sample Interface.

The block can accept the next frame only after it has completed decoding the previous
frame. You must leave
*Iterations*\*2\**HalfIterationLatency*+*BlockSize*+4
idle cycles between input frames. The half-iteration latency is described in the Algorithms section.
Alternatively, you can use the output signal
**ctrl**.`end` to determine when the block is
ready for new input.

This waveform shows an input frame of 120 samples (+ 4 tail bits), and 2632 idle
cycles between frames. Each input sample is a vector of three fixed-point soft-decision
values. The input and output **ctrl** buses are expanded to show the
control signals. `start` and `end` show the frame
boundaries, and `valid` qualifies the data samples.

Logic Analyzer waveform of LTE Turbo Decoder block input and output signals
