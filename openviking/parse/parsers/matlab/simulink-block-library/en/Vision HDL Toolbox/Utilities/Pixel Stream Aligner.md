---
type: simulink-block
title: 'Pixel Stream Aligner'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'pixelstreamaligner'
documentation_source_path: 'ref/pixelstreamaligner.html'
language: en
---

# Pixel Stream Aligner

## Ports

### Input

This block uses a streaming pixel interface with a bus for
frame control signals. This interface enables the block to operate independently of image size
and format. The **pixel** ports on this block support single pixel streaming or
multipixel streaming. Single pixel streaming accepts and returns a single pixel value each clock
cycle. Multipixel streaming accepts and returns a vector of *M* pixels per
clock cycle to support high-frame-rate or high-resolution formats. The *M*
value corresponds to the **Number of pixels** parameter of the Frame To
Pixels block. Along with the pixel, the block accepts and returns a
`pixelcontrol` bus that contains five control signals. The control signals
indicate the validity of each pixel and their location in the frame. For multipixel streaming,
one set of control signals applies to all pixels in the vector. To convert a frame (pixel
matrix) into a serial pixel stream and control signals, use the Frame
To Pixels block. For a full description of the interface, see Streaming Pixel Interface.

This block also supports multipixel-multicomponent streams,
where the pixel input is a matrix of *M*-by-*N* values.
*M* is number of pixels and *N* is number of components.
These values correspond to the **Number of pixels** and **Number of
components** parameters of the Frame To Pixels
block.

### **pixel** — Input pixel stream scalar | vector | matrix

For single pixel streams, specify **pixel** as a
scalar or a vector of 1-by-**Number of components**
values. For multipixel streams, specify **pixel** as a
matrix of **Number of pixels**-by-**Number of
components** pixel intensity values. **Number of
pixels** can be two, four, or eight.

Because the block delays this pixel stream to match the control
signals of the reference stream, **refPixel**,
**pixel** must be the earlier of the two
streams.

Since R2025a, the software supports `single`
data type for simulation and HDL code generation. To enable HDL code generation for
`single` data types in your model, open the **HDL
Coder** app, go to the **Floating Point** pane, and
select the **Use Floating Point** checkbox.
`double` data type is supported only for simulation, not for HDL code
generation.

**Data Types:** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

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

### **refPixel** — Reference pixel stream scalar | vector | matrix

Specify **refPixel** as a scalar, a vector of
1-by-**Number of components** values, or a matrix
of **Number of pixels**-by-**Number of
components** pixel intensity values.

The allowed dimensions for **refPixel** depend on the
dimensions of the input **pixel** stream. The
**Number of pixels** must be the same.

| Input pixel Dimensions | Allowed refPixel Dimensions |
| --- | --- |
| 1-by-*N* | 1-by-1, 1-by-3, or 1-by-4 |
| 2-by-*N* | 2-by-1, 2-by-3, or 2-by-4 |
| 4-by-*N* | 4-by-1, 4-by-3, or 4-by-4 |
| 8-by-*N* | 8-by-1, 8-by-3, or 8-by-4 |

Because the block delays the **pixel** input stream
to match the reference control signals, **refPixel**
must be the later of the two streams. The reference data and its control
signals pass through the block with a small delay.

Since R2025a, the software supports `single`
data type for simulation and HDL code generation. To enable HDL code generation for
`single` data types in your model, open the **HDL
Coder** app, go to the **Floating Point** pane, and
select the **Use Floating Point** checkbox.
`double` data type is supported only for simulation, not for HDL code
generation.

**Data Types:** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

### **refCtrl** — Reference pixel stream control signals `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

For multipixel streaming, each vector of pixel values has one set of
control signals. Because the vector has only one
`valid` signal, the pixels in the vector must be
either all valid or all invalid. The `hStart` and
`vStart` signals apply to the pixel with the lowest
index in the vector. The `hEnd` and
`vEnd` signals apply to the pixel with the highest
index in the vector.

The block uses these control signals for the aligned output
stream.

**Data Types:** `bus`
### Output

### **pixel** — Aligned pixel stream scalar | vector | matrix

The timing of the output **pixel** stream matches the
timing of the output **refPixel** stream. The
dimensions and data type of the output **pixel** stream
match those of the input **pixel** stream.

**Data Types:** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

### **refPixel** — Reference pixel stream scalar | vector | matrix

The dimensions and data type of the output **refPixel** stream match those of
the input **refPixel** stream. The block passes this
stream through the block unchanged.

**Data Types:** `fixed point` | `uint` | `int` | `Boolean` | `double` | `single`

### **refCtrl** — Reference control signals `pixelcontrol` bus

The block passes the input **refCtrl** signals through the block with a small
delay.

**Data Types:** `bus`

## Parameters

### **Line buffer size** — Size of the line memory buffer `2048` (default) | positive integer

Choose a power of two that accommodates the number of active pixels in a horizontal line. If
you specify a value that is not a power of two, the block uses the next
largest power of two. The block implements a circular buffer of
2*m* pixels, where
*m* is **Maximum number of lines** +
log2(**Line buffer
size**).

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

### **Maximum number of lines** — Buffer depth that accommodates the timing offset between input streams `10` (default) | positive integer

The block implements a circular buffer of 2*m*
pixels, where *m* is **Maximum number of
lines** + log2(**Line buffer
size**), and a line address buffer of **Maximum number
of lines** locations. The circular memory stores the earlier
input lines until the reference control signals arrive. The line address
buffer stores the address of the start of each line. When the reference
control signals arrive, the block uses the stored address to read and send
the delayed line. This parameter must accommodate the difference in timing
between the two input streams, including the internal latency before the
block reads the first line. During simulation, the block warns when an
overflow occurs. To avoid the overflow condition, increase **Maximum
number of lines**. The delay between streams cannot exceed an
entire frame.

When the input **pixel** is a vector or a matrix, the
block replicates the circular buffer for each element. For multipixel
streaming, the block adjusts the line buffer size to store
1/**Number of pixels** pixels. For instance, with a
4-by-3 input stream, each buffer stores ¼ of the pixels for a line, and the
buffer is 12×2*m-2* locations.
The line address buffer remains the same size.

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

You cannot generate HDL for this block inside a Resettable Synchronous
Subsystem (HDL Coder).

## Version History

**Introduced in R2017a**

### R2025a: `single` data type supported for HDL code generation

The block now supports HDL code generation with `single` data
type pixel input.

### R2022b: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021a: Multipixel-multicomponent streaming

The block now supports streams that are both multipixel and multicomponent. The
HDL implementation replicates the algorithm for each pixel and component in
parallel.

The block supports input and output matrices of
*NumPixels*-by-*NumComponents* pixels, where
*NumPixels* is 4 or 8. The **ctrl** ports
remain scalar, and the control signals in the `pixelcontrol` bus
apply to all pixels in the matrix.

### R2020b: Multipixel streaming

The Pixel Stream Aligner block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel. You cannot use multicomponent
and multipixel together.

For multipixel streaming, the block supports input and output column vectors of 4
or 8 pixels. The **ctrl** port remains scalar, and the control
signals in the `pixelcontrol` bus apply to all pixels in the
vector.

## Description

Align two streams of pixel data

The Pixel Stream Aligner block synchronizes two
pixel streams by delaying one stream to match the timing of a reference
stream. Many Vision HDL Toolbox™ algorithms delay the pixel stream,
and the amount of delay can change as you adjust algorithm parameters.
You can use this block to align streams for overlaying, comparing,
or combining two streams such as in a Gaussian blur operation. Connect
the delayed stream to the **refPixel** and **refCtrl** input
ports, and the earlier stream to the **pixel** and **ctrl** input
ports.

This waveform diagram shows the input streams, `pixelIn` and
`refPixelIn`, and their associated control signals. The reference
input frame starts later than the `pixelIn` frame. The output signals
show that the block delays `pixelIn` to match the reference stream, and
that both output streams share control signals. The waveform shows the short latency
between the input `refCtrl` and the output `refCtrl`.
In this simulation, to accommodate the delay of four lines between the input streams,
the **Maximum number of lines** parameter must be set to at least
4.
