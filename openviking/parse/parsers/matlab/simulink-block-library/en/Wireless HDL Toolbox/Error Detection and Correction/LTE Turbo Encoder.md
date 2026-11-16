---
type: simulink-block
title: 'LTE Turbo Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'lteturboencoder'
documentation_source_path: 'ref/lteturboencoder.html'
language: en
---

# LTE Turbo Encoder

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

### **blockSize** — Turbo code block size integer

Turbo code block size, specified as an integer. This value must be one of the 188 values
specified in the LTE standard, from 40 to 6144 in these intervals: `[40:8:512
528:16:1024 1056:32:2048 2112:64:6144]`.

#### Dependencies

This port appears when you set **Block size source** to `Input port`.

**Data Types:** `single` | `double` | `uint16` | `fixdt(0,13,0)`
### Output

### **data** — Encoded sample stream 3-by-1 column vector

Encoded sample stream, returned as a 3-by-1 column vector. Each
encoded sample is represented by one systematic bit and two parity bits.

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

### **tail1, tail2** — Indicate trellis termination cycles scalar

Use the optional **tail1** and
**tail2** output ports to indicate the location of
the tail bits in the output data stream. These signals are 1
(`true`) for the cycles that correspond to the tail
bits for each encoder.

The block returns the tail bits in the order specified by the LTE
standard TS 36.212 [1].
Each encoder returns two cycles of encoded tail bits.

| Cycle | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| **tail1** | 1 | 1 | 0 | 0 |
| **tail2** | 0 | 0 | 1 | 1 |
| **data** | [E1inK E1outK E1inK+1] | [E1outK+1 E1inK+2 E1outK+2] | [E2inK E2outK E2inK+1] | [E2outK+1 E2inK+2 E2outK+2] |

#### Dependencies

Enable these ports by selecting **Enable trellis
termination valid ports**.

**Data Types:** `Boolean`

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

### **Enable trellis termination valid ports** — Enable ports that indicate the tail bit output samples off (default) | on

When you select this parameter, the **tail1** and
**tail2** ports appear on the block. These ports return
control signals that indicate the cycles when the output samples are the
tail bits for each encoder.

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

Encode binary samples using turbo algorithm

The LTE Turbo Encoder block implements the turbo encoder described by
LTE standard TS 36.212 [1] using an interface
and architecture optimized for HDL code generation and hardware deployment. The encoder
is a parallel concatenated convolutional code (PCCC) with two 8-state constituent
encoders and an internal interleaver. The first encoder operates on the input data
stream, and the second encoder operates on an interleaved version of the input data. The
block terminates each encoder output with independent tail bits. The coding rate is 1/3.
The encoded output bits for each input bit are returned as a 3-by-1 vector, `[S
P1 P2]`. In this vector, `S` is the systematic bit, and
`P1` and `P2` are the parity bits from the two
encoders.

This block uses a
streaming sample interface with a bus for related control signals. This interface enables the
block to operate independently of frame size, and to connect easily with other Wireless HDL Toolbox™ blocks. The block accepts and returns a value representing a single sample, and a
bus containing three control signals. These signals indicate the validity of each sample and the
boundaries of the frame. To convert a matrix into a sample stream and these control signals, use
the Frame To Samples block
or the `whdlFramesToSamples`
function. For a full description of the interface, see Streaming Sample Interface.

The block can accept new input data after the previous frame is complete. Apply input
frames with at least *BlockSize* + 16 idle cycles between them. The 16
cycles consists of 12 cycles for pipeline delays in the algorithm, and 4 cycles of tail
bits. This latency does not vary with block size. Or, you can use the output signal
**ctrl**.`end` to determine when the block is
ready for new input.

This waveform shows an input frame of 40 samples, with 57 idle cycles between frames.
The input and output **ctrl** buses are expanded to show the control
signals. `start` and `end` show the frame boundaries,
and `valid` qualifies the data samples. The optional
**tail1** and **tail2** signals indicate the
cycles when the tail bits from each encoder are valid.

Logic Analyzer waveform of LTE Turbo Encoder block input and output signals
