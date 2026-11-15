---
type: simulink-block
title: 'Median Filter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Algorithm Design / Filtering'
documentation_page: 'medianfilter'
documentation_source_path: 'ref/medianfilter.html'
language: en
---

# Median Filter

## Ports

### Input

### **pixel** — Input pixel stream scalar | vector

This block supports single pixel streaming or multipixel streaming. For single
pixel streaming, specify a single input pixel as a scalar intensity value. For
multipixel streaming, specify a vector of two, four, or eight pixel intensity values.
For details of how to set up your model for multipixel streaming, see Filter Multipixel Video Streams.

This block does not support multicomponent streaming. To process multicomponent
streams, replicate the block for each component. The `pixelcontrol`
bus for all components is identical, so you can connect a single bus to multiple
replicated blocks.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

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

### **pixel** — Output pixel stream scalar | vector

This block supports single pixel streaming or multipixel streaming. When using
single pixel streaming, the block returns a single pixel as a scalar intensity value.
When using multipixel streaming, the block returns a vector of intensity values. This
vector is the same size as the input **pixel** vector. For details of
how to set up your model for multipixel streaming, see Filter Multipixel Video Streams.

The output pixel data type is the same as the data type of the input
pixels.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

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

## Parameters

### **Neighborhood size** — Size of image region used to compute median `3×3` (default) | `5×5` | `7×7`

Select the neighborhood size, in pixels, as `3×3`,
`5×5`, or `7×7`.

You cannot use a neighborhood size of `7×7` when you
use multipixel streaming and set **Padding method** to
`None`.

### **Padding method** — Method for padding boundary of input image `Symmetric` (default) | `Constant` | `Replicate` | `Reflection` | `None`

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

You cannot use a neighborhood size of `7×7` when you
set **Padding method** to `None`.

### **Padding value** — Value used to pad boundary of input image `0` (default) | integer

Specify an integer to pad the boundary of the input image. The block casts this value
to the same data type as the input pixel.

#### Dependencies

To enable this parameter, set the **Padding method** parameter to
`Constant`.

### **Line buffer size** — Size of line buffer `2048` (default) | integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

The block allocates (*N*— 1) -by-**Line buffer
size** memory locations to store the pixels used to compute the median value.
*N* is the dimension of the square region specified by the
**Neighborhood size** parameter.

## Libraries

Vision HDL Toolbox / Analysis & Enhancement Vision HDL Toolbox / Filtering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

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

**Restrictions**

You cannot generate HDL code for this block if it is inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2015a**

### R2023a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021b: Reflection padding

Pad the edge of a frame by reflecting around the edge-pixel value. This padding method
helps reduce edge contrast effects and can improve results for machine learning while
maintaining the original frame size.

### R2020a: Option to omit padding

You can now configure the block to not add padding around the boundaries of the active
frame. This option reduces the hardware resources used by the block and the blanking
required between frames but affects the accuracy of the output pixels at the edges of the
frame. To use this option, set the **Padding method** parameter to
`None`. For an example, see Increase Throughput by Omitting Padding.

### R2019b: Multipixel streaming

The Median Filter block now supports multipixel streams. The HDL implementation replicates
the algorithm for each pixel in parallel.

For multipixel streaming, the block supports input and output column vectors of 4 or 8
pixels. The **ctrl** port remains scalar, and the control signals in the
`pixelcontrol` bus apply to all pixels in the vector.

### R2018b: Improved line buffer

The internal line buffer in this block now handles bursty data, that is, noncontiguous
valid signals within a pixel line. This implementation uses fewer hardware resources due to
improved padding logic and native support for kernel sizes with an even number of lines.
This change affects the Line Buffer block and blocks that use an internal
line buffer.

The latency of the line buffer is now reduced by a few cycles for some configurations.
You might need to rebalance parallel path delays in your models. A best practice is to
synchronize parallel paths in your models by using the pixel stream control signals rather than
by inserting a specific number of delays.

## Description

2-D median filtering

The Median Filter block replaces each input pixel with the median value of
a specified surrounding *N*-by-*N* neighborhood. The median
is less sensitive to extreme values than the mean. You can use this block to remove
salt-and-pepper noise from an image without significantly reducing the sharpness of the image.
You can specify the neighborhood size and padding values for edges of the input image.
