---
type: simulink-block
title: 'Pixel Stream FIFO'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'pixelstreamfifo'
documentation_source_path: 'ref/pixelstreamfifo.html'
language: en
---

# Pixel Stream FIFO

## Ports

### Input

### **pixel** — Input pixel stream scalar | vector | matrix

For single pixel streams, specify **pixel** as a
scalar or a vector of 1-by-**Number of components**
values that represent a single pixel. For multipixel streams, specify
**pixel** as a matrix of **Number of
pixels**-by-**Number of components** pixel
intensity values. **Number of pixels** can be two,
four, or eight.

Since R2025a, the software supports `single`
data type for simulation and HDL code generation. To enable HDL code generation for
`single` data types in your model, open the **HDL
Coder** app, go to the **Floating Point** pane, and
select the **Use Floating Point** checkbox.
`double` data type is supported only for simulation, not for HDL code
generation.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

For multipixel streaming, each vector of pixel values has one set of control signals.
Because the vector has only one `valid` signal, the pixels in the
vector must be either all valid or all invalid. The `hStart` and
`vStart` signals apply to the pixel with the lowest index in the
vector. The `hEnd` and `vEnd` signals apply to the
pixel with the highest index in the vector.

**Data Types:** `bus`
### Output

### **pixel** — Output pixel stream scalar | vector | matrix

Each line of the output stream has contiguous valid pixels. The
dimensions and data type of the output **pixel** stream
match those of the input **pixel** stream. The block
returns the output pixel stream as a scalar, a vector of
1-by-**Number of components** values, or a matrix
of **Number of pixels**-by-**Number of
components** values.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **ctrl** — Control signals accompanying pixel stream `pixelcontrol` bus

Control signals accompanying pixel stream, returned as a
`pixelcontrol` bus containing five signals. The
signals indicate the validity of the pixel and its location in the
frame. For more information on the signal protocol, see Pixel Control Bus.

The Pixel Stream FIFO block returns each line of pixels
with the **ctrl**.`valid` signal
continuously `true` between
**ctrl**.`hStart` and
**ctrl**.`hEnd`. The block buffers
the entire input line before it returns the modified line.

**Data Types:** `bus`

## Parameters

### **Line buffer size** — Size of line memory buffer `2048` (default) | positive integer

Specify a power of two that accommodates the number of active pixels in a
single horizontal line. If you specify a value that is not a power of two,
the block uses the next largest power of two.

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

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

**Restrictions**

You cannot generate HDL for this block inside an Enabled Subsystem (Simulink), Resettable Synchronous
Subsystem (HDL Coder), or a Triggered Subsystem (Simulink).

## Version History

**Introduced in R2018a**

### R2025a: `single` data type supported for HDL code generation

The block now supports HDL code generation with `single` data
type pixel input.

### R2022a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021a: Multipixel-multicomponent streaming

The block now supports streams that are both multipixel and multicomponent. The
HDL implementation replicates the algorithm for each pixel and component in
parallel.

The block supports input and output matrices of
*NumPixels*-by-*NumComponents* pixels. The
**ctrl** ports remain scalar, and the control signals in the
`pixelcontrol` bus apply to all pixels in the matrix.

## Description

Buffer input stream to create image lines that have contiguous valid pixels

The Pixel Stream FIFO block stores incoming valid pixels and
accompanying control signals and returns the same pixel stream without gaps between the
valid pixels of each line. The block preserves the total line size and total frame size
of the video stream, including invalid cycles.

Use the Pixel Stream FIFO block to buffer video sources. The waveform
shows a direct memory access (DMA) video source, where pixels are read in bursts, and a
Camera Link® video source, where pixels are valid every second clock cycle. To create
contiguous video lines, a Pixel Stream FIFO block buffers the input
pixels and control signals of each source.

Logic Analyzer waveform of the input and output signals of the Pixel Stream FIFO block for a DMA video source and a Camera Link video source
