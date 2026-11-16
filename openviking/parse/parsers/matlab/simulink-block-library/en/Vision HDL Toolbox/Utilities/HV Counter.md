---
type: simulink-block
title: 'HV Counter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'hvcounter'
documentation_source_path: 'ref/hvcounter.html'
language: en
---

# HV Counter

## Ports

### Input

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`
### Output

### **hCount** — Pixel location in line positive integer

Pixel location within a line, returned as a positive integer. The
block clears the pixel count at the start of each line. If the input
pixels per line exceeds the size of the counter, the block returns a
saturated value until the start of the next line.

**Data Types:** `fixdt(0,ceil(log2(ActiveVideoLines)),0)`

### **vCount** — Line location in frame positive integer

Line location within the frame or region of interest, returned as a
positive integer. The block clears the line count at the start of each
frame. If the input lines per frame exceeds the size of the counter, the
block returns a saturated value until the start of the next frame.

**Data Types:** `fixdt(0,ceil(log2(ActiveVideoLines)),0)`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`

## Parameters

### **Active pixels per line** — Maximum pixels per line `320` (default) | positive integer

Maximum pixels per line, specified as a positive integer. The block
implements a pixel counter that has
`ceil(log2(ActivePixelsPerLine))`
bits. For example, for a frame with 320 pixels per line, the counter has 9
bits. For a frame with 1024 pixels per line, the counter has 11 bits.

### **Active video lines** — Maximum lines per frame `240` (default) | positive integer

Maximum lines per frame, specified as a positive integer. The block
implements a line counter that has
`ceil(log2(ActiveVideoLines))`
bits. For example, for a frame with 240 pixels per line, the counter has 8
bits. For a frame with 1080 pixels per line, the counter has 11 bits.

## Libraries

Vision HDL Toolbox / Utilities

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

**Introduced in R2019a**

## Description

Count active dimensions of pixel stream

The HV Counter block analyzes a video stream and returns the current
count of lines per frame and pixels per line. The block also delays control signals of
the pixel stream to correspond with the count result. Use this block for algorithms that
use the location of a pixel within a frame or region of interest.

This waveform shows the pixel-stream control signals and resulting counter outputs for
the first two lines of a video frame that has 10 pixels per line. The HV
Counter block has a latency of two cycles to return the current counter
values.

Logic Analyzer waveforms of the input and output signals of the HV Counter block
