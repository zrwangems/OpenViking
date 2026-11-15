---
type: simulink-block
title: 'Closing'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Algorithm Design / Morphology'
documentation_page: 'closing'
documentation_source_path: 'ref/closing.html'
language: en
---

# Closing

## Ports

### Input

### **pixel** — Boolean input pixel or multipixel vector scalar | vector

This block supports single pixel streaming or multipixel streaming. For
single pixel streaming, specify a single input pixel as a scalar Boolean
value. For multipixel streaming, specify a vector of four or eight Boolean
values. For details of how to set up your model for multipixel streaming,
see Filter Multipixel Video Streams.

**Data Types:** `Boolean`

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

### **pixel** — Boolean output pixel or multipixel vector scalar | vector

This block supports single pixel streaming or multipixel streaming. When
using single pixel streaming, the block returns a single pixel as a scalar
Boolean value. When using multipixel streaming, the block returns a vector
of Boolean values. This vector is the same size as the input
**pixel** vector. For details of how to set up your
model for multipixel streaming, see Filter Multipixel Video Streams.

**Data Types:** `Boolean`

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

### **Neighborhood** — Pixel neighborhood `[0,1,0; 1,1,1; 0,1,0]` (default) | vector or matrix of `1`s and `0`s

Pixel neighborhood, specified as a vector or matrix of binary
values.

The block supports neighborhoods of up to 32-by-32 pixels. To
use a structuring element, set the **Neighborhood** parameter to
`getnhood (Image Processing Toolbox)(strel (Image Processing Toolbox)(shape))`, where
*`shape`* is specified by the input arguments to the `strel` (Image Processing Toolbox) function..

When you use multipixel vector input, the neighborhood must be at least two pixels
in each dimension.

### **Line buffer size** — Size of line memory buffer `2048` (default) | positive integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

The block allocates (*n* –
1)-by-**Line buffer size** memory locations to store the pixels,
where *n* is the number of lines in the
**Neighborhood** parameter value.

### **Padding method** — Method for padding `Constant` (default) | `None`

Select one of these methods for padding the boundary of the input image. For more
information about these methods, see Edge Padding.

- `Constant` — The block pads the image with zeros for
  the dilation operation and with ones for the erosion operation. These values
  prevent closing at the boundaries of the active frame.
- `None` — Exclude padding logic. The block does not set the pixels
  outside the image frame to any particular value. This option reduces the hardware resources
  used by the block and the blanking required between frames but affects the accuracy of the
  output pixels at the edges of the frame. To maintain pixel stream timing, the output frame
  is the same size as the input frame. However, to avoid using pixels calculated from
  undefined padding values, mask off the *KernelSize*/2 pixels around the
  edge of the frame for downstream operations. For details, see Increase Throughput by Omitting Padding.

## Libraries

Vision HDL Toolbox / Morphological Operations

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

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous
Subsystem (HDL Coder).

## Version History

**Introduced in R2015a**

### R2020a: Option to omit padding

You can now configure the block to not add padding around the boundaries of the active
frame. This option reduces the hardware resources used by the block and the blanking
required between frames but affects the accuracy of the output pixels at the edges of the
frame. To use this option, set the **Padding method** parameter to
`None`. For an example, see Increase Throughput by Omitting Padding.

### R2020a: Multipixel streaming

The Closing block now supports multipixel streams. The HDL implementation replicates
the algorithm for each pixel in parallel.

For multipixel streaming, the blocks support input and output column vectors of 4 or 8
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
synchronize parallel paths in your models by using the pixel stream control signals rather
than by inserting a specific number of delays.

## Description

Morphological closing of binary pixel data

The Closing block performs morphological dilation followed by morphological
erosion by using the same neighborhood for both calculations. The block operates on a stream
of binary intensity values. You can specify a neighborhood, or structuring element, of up to
32-by-32 pixels.

**Note**

This block matches the behavior of the Closing (Computer Vision Toolbox) block in Computer Vision Toolbox™ and of the combination of `imerode(imdilate())` in
Image Processing Toolbox™. However, it does not match the edge behavior of the
`imclose` function in Image Processing Toolbox. `imclose` assumes that white is the foreground color of a
binary image, which can result in differences in edge behavior.

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
