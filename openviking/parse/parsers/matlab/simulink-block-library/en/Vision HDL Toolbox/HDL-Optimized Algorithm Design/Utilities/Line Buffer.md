---
type: simulink-block
title: 'Line Buffer'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Algorithm Design / Utilities'
documentation_page: 'linebuffer'
documentation_source_path: 'ref/linebuffer.html'
language: en
---

# Line Buffer

## Ports

### Input

### **pixel** — Input pixel stream scalar | vector

This block supports single pixel streaming or multipixel streaming.
For single pixel streaming, specify a single input pixel as a scalar
intensity value. For multipixel streaming, specify a vector of two,
four, or eight pixel intensity values. For details of how to set up your
model for multipixel streaming, see Filter Multipixel Video Streams.

This block does not support multicomponent streaming. To process
multicomponent streams, replicate the block for each component. The
`pixelcontrol` bus for all components is identical,
so you can connect a single bus to multiple replicated blocks.

Since R2025a, the software supports `single`
data type for simulation and HDL code generation. To enable HDL code generation for
`single` data types in your model, open the **HDL
Coder** app, go to the **Floating Point** pane, and
select the **Use Floating Point** checkbox.
`double` data type is supported only for simulation, not for HDL code
generation.

**Data Types:** `int` | `uint` | `fixed point` | `Boolean` | `double` | `single`

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

### **pixel** — Column of neighborhood column vector | matrix

Column of neighborhood pixel values, returned as a of
1-by-*H* vector, where *H* is the
vertical neighborhood dimension. When using multipixel streaming, the
block returns a *M*-by-*H* matrix,
where *M* is the number of pixels in the input vector.
The output pixel data type is the same as the data type of the input
pixels.

To compose a neighborhood for further processing, use the
**shiftEnable** signal to store the output columns
for each kernel region, including padding, in a shift register. For
multipixel streaming, use shift registers to construct
*M* regions, each of
*W*-by-*H* pixels, where
*W* is the horizontal kernel dimension. Then,
perform the kernel operation *M* times in parallel.

**Note**

HDL code generation is supported for small matrices, but
matrix operations can impact hardware performance and resource
usage. Therefore, minimize how much your design operates on an
*W*-by-*H* neighborhood
directly. You can :

- Separate a filter into vertical and horizontal
  components.
- Concatenate the neighborhood pixels into an
  (*W*\**H*)-by-1
  vector.
- Use a For Each subsystem to store
  and operate on each pixel row.

These design suggestions provide opportunities to add
pipelining around each adder or multiplier to increase
synthesized clock speed and fit the design to DSP blocks on an
FPGA.

**Data Types:** `int` | `uint` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — Control signals accompanying output column `pixelcontrol` bus

Control signals accompanying the output column, returned as a
`pixelcontrol` bus containing five signals. The
signals describe the validity of the center pixel of the column, and the
location of that pixel within the frame. See Pixel Control Bus.

Columns that contain only padding pixels do not assert
**ctrl**.`valid`. The
**shiftEnable** signal is asserted for both padding
and active columns.

**Note**

For most of the frame, the block returns the input control signals
that arrived with the bottom pixel of the column. However, for the
final `floor(H/2)` lines of each
frame, the bottom pixel of the column is a padding pixel, so the
block generates output control signals. The block generates a
contiguously asserted
**ctrl**.`valid` signal for
the valid pixels in each line.

For multipixel streaming, there is one set of control signals for each
vector of pixel values. Since there is only one `valid`
signal for the vector, the pixels in the vector are either all valid or
all invalid. The `hStart` and `vStart`
signals apply to the pixel with the lowest index in the vector. The
`hEnd` and `vEnd` signals apply to
the pixel with the highest index in the vector.

**Data Types:** `bus`

### **shiftEnable** — Valid signal for neighborhood column scalar

Valid signal for neighborhood columns, returned as a
`Boolean` scalar. Use this signal to control a
shift register that composes a neighborhood from the output columns.
This signal is `true` (1) for any neighborhood column,
indicating that the column contains valid image pixels or that the
column was added for edge padding.

**Data Types:** `Boolean`

## Parameters

### **Neighborhood size** — Size of output neighborhood `[3 3]` (default) | 2-element row vector of integer dimensions

Size of output neighborhood to be formed, specified as a 2-element row
vector of integer dimensions [*H*
*W*], where *H* is the vertical dimension
and *W* is the horizontal dimension. The block returns a
column vector of *H* elements. The *W*
dimension is used to determine padding.

### **Padding method** — Method for padding the boundary of input image `Symmetric` (default) | `Constant` | `Replicate` | `Reflection` | `None`

Select one of these methods for padding the boundary of the input image. For more information
about these methods, see Edge Padding.

- `Constant` — Interpret pixels outside the image frame
  as having a constant value.
- `Replicate` — Repeat the value of pixels at the edge
  of the image.
- `Symmetric` — Set the value of the padding pixels to
  mirror the edge of the image.
- `Reflection` — Set the value of the padding pixels to
  reflect around the pixel at the edge of the image.
- `None` — Exclude padding logic. The block does not set the pixels
  outside the image frame to any particular value. This option reduces the hardware resources
  used by the block and the blanking required between frames but affects the accuracy of the
  output pixels at the edges of the frame. To maintain pixel stream timing, the output frame
  is the same size as the input frame. However, to avoid using pixels calculated from
  undefined padding values, mask off the *KernelSize*/2 pixels around the
  edge of the frame for downstream operations. For details, see Increase Throughput by Omitting Padding.

### **Padding value** — Value used to pad boundary of input image `0` (default) | integer

Specify an integer to pad the boundary of the input image. The block casts this value
to the same data type as the input pixel.

#### Dependencies

To enable this parameter, set the **Padding method** parameter to
`Constant`.

### **Line buffer size** — Size of line memory buffer `2048` (default) | positive integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

## Libraries

Vision HDL Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

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

### R2025a: `single` data type supported for HDL code generation

The block now supports HDL code generation with `single` data
type pixel input.

### R2025a: Display algorithm latency on block mask

The block now shows its latency on the block mask. The latency displays as a number
of lines and pixels. The exact number of clock cycles depends on the number of
pixels in a line of your image frame and the input pixel valid pattern. Use the
displayed latency information along with the `pixelcontrol` bus
signals to align parallel data paths in your design.

### R2022a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021b: Reflection padding

Pad the edge of a frame by reflecting around the edge-pixel value. This padding
method helps reduce edge contrast effects and can improve results for machine
learning while maintaining the original frame size.

### R2020a: Option to omit padding

You can now configure the block to not add padding around the boundaries of the
active frame. This option reduces the hardware resources used by the block and the
blanking required between frames but affects the accuracy of the output pixels at
the edges of the frame. To use this option, set the **Padding
method** parameter to `None`. For an example,
see Increase Throughput by Omitting Padding.

### R2019b: Multipixel streaming

The Line Buffer block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel.

For multipixel streaming, the block accepts an input vector of 4 or 8 pixels and
returns a *KernelHeight*-by-*NumberOfPixels*
matrix. The **ctrl** port remains scalar, and the control signals
in the `pixelcontrol` bus apply to all pixels in the vector.

### R2018b: Improved line buffer

The line buffer now handles bursty data, that is, noncontiguous valid signals
within a pixel line. This implementation uses fewer hardware resources due to
improved padding logic and native support for kernel sizes with an even number of
lines. This change affects the Line Buffer block and blocks that use
an internal line buffer.

The latency of the line buffer is now reduced by a few cycles for some
configurations. You might need to rebalance parallel path delays in your models. A
best practice is to synchronize parallel paths in your models by using the pixel stream
control signals rather than by inserting a specific number of delays.

## Description

Store video lines and return neighborhood pixels

The Line Buffer block selects neighborhood pixels from streaming image
data. It handles video control signals and edge padding, and is pipelined for high-speed
video designs. The block outputs one column of the neighborhood at a time. To
compose a neighborhood for further processing, use the **shiftEnable**
signal to store the output columns, including padding, in a shift register. This block
allows you to share the line buffer resources when your design performs multiple
operations on the same neighborhood.

The following waveform shows the Line
Buffer block returning 5-by-1 pixel columns that make up a 5-by-5
neighborhood. The time frame shown is at the beginning (top-left corner) of an input
frame. The output starts after the block has stored two (`floor(M/2)`)
lines and is receiving the start of the third line. The **shiftEnable**
signal is asserted two cycles earlier than the output
**ctrl**.`valid` signal, which indicates that the
first two (`floor(M/2)`) columns are exclusively padding pixels.
Similarly, **shiftEnable** stays high for two extra cycles at the end
of the line.
