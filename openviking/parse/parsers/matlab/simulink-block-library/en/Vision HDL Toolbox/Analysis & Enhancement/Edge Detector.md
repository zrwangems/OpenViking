---
type: simulink-block
title: 'Edge Detector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'edgedetector'
documentation_source_path: 'ref/edgedetector.html'
language: en
---

# Edge Detector

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar | vector
  direction: input
  data_types: uint | int | fixed point | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: Th
  summary: Threshold value scalar
  direction: input
  data_types: single | double | int | uint | fixed point
- name: Edge
  summary: Boolean pixel value, indicating whether pixel is an edge scalar | vector
  direction: output
  data_types: Boolean
- name: Gv,Gh
  summary: Vertical and horizontal gradient scalar | vector
  direction: output
  data_types: single | double | int | uint | fixed point
- name: G45,G135
  summary: Orthogonal gradient scalar | vector
  direction: output
  data_types: single | double | int | uint | fixed point
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: output
  data_types: bus
```

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

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `int` | `fixed point` | `double` | `single`

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

### **Th** — Threshold value scalar

Threshold value that defines an edge, specified as a scalar. The block
compares the square of this value to the sum of the squares of the
gradients.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int` | `uint` | `fixed point`
### Output

### **Edge** — Boolean pixel value, indicating whether pixel is an edge scalar | vector

For single pixel streaming, **Edge** is a Boolean
scalar. For multipixel streaming, **Edge** is a vector
of *M*-by-1 Boolean values. Each pixel value indicates
whether the pixel is an edge.

**Data Types:** `Boolean`

### **Gv,Gh** — Vertical and horizontal gradient scalar | vector

Vertical and horizontal gradient values calculated over the kernel
centered at a pixel location.

For single pixel streaming, the block returns **Gv**
and **Gh** as scalar values. For multipixel streaming,
the block returns **Gv** and **Gh** as
vectors of *M*-by-1 values.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable these ports, set **Method** to
`Sobel` or
`Prewitt`.

**Data Types:** `single` | `double` | `int` | `uint` | `fixed point`

### **G45,G135** — Orthogonal gradient scalar | vector

Orthogonal gradient values calculated over the kernel centered at a
pixel location.

For single pixel streaming, the block returns **G45**
and **G135** as scalar values. For multipixel
streaming, the block returns **G45** and
**G135** as vectors of *M*-by-1
values.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable these ports set **Method** to
`Roberts`.

**Data Types:** `single` | `double` | `int` | `uint` | `fixed point`

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
```yaml
parameters:
- name: Method
  summary: Edge detection algorithm Sobel (default) | Prewitt | Roberts
  group: Main
- name: Output the binary image
  summary: Enable edge output port on (default) | off
  group: Main
- name: Output the gradient components
  summary: Enable gradient output ports off (default) | on
  group: Main
- name: Source of threshold value
  summary: Source for gradient threshold that indicates an edge Property (default) | Input port
  group: Main
- name: Threshold value
  summary: Gradient threshold value that indicates an edge 20 (default) | scalar
  group: Main
- name: Line buffer size
  summary: Size of the line memory buffer 2048 (default) | integer
  group: Main
- name: Padding method
  summary: Method for padding Symmetric (default) | None
  group: Main
- name: Rounding mode
  summary: Rounding method for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round
    | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow action for internal fixed-point calculations off (default) | on
  group: Data Types
- name: Gradient Data Type
  summary: Data type for gradient output ports Inherit via internal rule (default) | data type expression
  group: Data Types
```

### Main

### **Method** — Edge detection algorithm `Sobel` (default) | `Prewitt` | `Roberts`

When you select `Sobel` or
`Prewitt`, the block calculates horizontal
and vertical gradients, `Gv` and `Gh`.
When you select `Roberts`, the block calculates
orthogonal gradients, `G45` and
`G135`. For details of each method, see Algorithms.

**Note**

If you select `Prewitt`, the
full-precision internal data type is large due to the 1/6
coefficient. Consider selecting **Output the gradient
components**, so that you can customize the data
type to a smaller size.

### **Output the binary image** — Enable edge output port on (default) | off

When this parameter is selected, the block returns a stream of binary
pixels representing the edges detected in the input frame.

You must select at least one of **Output the binary
image** and **Output the gradient
components**.

### **Output the gradient components** — Enable gradient output ports off (default) | on

When this parameter is selected, the block returns a stream of values
representing the gradients calculated in the two orthogonal directions
at each pixel. When you set **Method** to
`Sobel` or
`Prewitt`, the output ports
**Gv** and **Gh** appear on the
block. When you set **Method** to
`Roberts`, the output ports
**G45** and **G135** appear on the
block.

You must select at least one of **Output the binary
image** and **Output the gradient
components**.

### **Source of threshold value** — Source for gradient threshold that indicates an edge `Property` (default) | `Input port`

You can set the threshold from an input port or from the dialog box.
The default value is `Property`. Selecting
`Input port` enables the
**Th** port.

### **Threshold value** — Gradient threshold value that indicates an edge `20` (default) | scalar

The block compares the square of this value to the sum of the squares
of the gradients. The block casts this value to the data type of the
gradients.

#### Dependencies

This option is visible when you set **Source of threshold
value** to `Property`.

### **Line buffer size** — Size of the line memory buffer `2048` (default) | integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

The block allocates (*N – 1*)-by-**Line
buffer size** memory locations to store the pixels, where
*N* is the number of lines in the differential
approximation matrix. If you set **Method** to
`Sobel` or
`Prewitt`, then *N* is 3.
If you set **Method** to
`Roberts`, then *N* is
2.

### **Padding method** — Method for padding `Symmetric` (default) | `None`

Select one of these methods for padding the boundary of the input
image. For more information about these methods, see Edge Padding.

- `Symmetric` — Set the value of
  the padding pixels to mirror the edge of the image. This
  option prevents edges from being detected at the boundaries
  of the active frame.
- `None` — Exclude padding logic. The block does not set the pixels
  outside the image frame to any particular value. This option reduces the hardware resources
  used by the block and the blanking required between frames but affects the accuracy of the
  output pixels at the edges of the frame. To maintain pixel stream timing, the output frame
  is the same size as the input frame. However, to avoid using pixels calculated from
  undefined padding values, mask off the *KernelSize*/2 pixels around the
  edge of the frame for downstream operations. For details, see Increase Throughput by Omitting Padding.

### Data Types

### **Rounding mode** — Rounding method for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Specify a rounding method for internal fixed-point calculations.

### **Saturate on integer overflow** — Overflow action for internal fixed-point calculations `off` (default) | `on`

When you clear this parameter, fixed-point and integer values wrap around to zero when
the value overflows what is representable with that data type. When you select this
parameter, the value saturates at the maximum representable value.

### **Gradient Data Type** — Data type for gradient output ports `Inherit via internal rule` (default) | data type expression

Data type for the two gradient output ports. By default, the block
automatically chooses full-precision data types.

#### Dependencies

To enable this parameter, on the **Main** tab,
select **Output the gradient components**.
## Libraries

Vision HDL Toolbox / Analysis & Enhancement

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

### R2023a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2020a: Option to omit padding

You can now configure the block to not add padding around the boundaries of the
active frame. This option reduces the hardware resources used by the block and the
blanking required between frames but affects the accuracy of the output pixels at
the edges of the frame. To use this option, set the **Padding
method** parameter to `None`. For an example,
see Increase Throughput by Omitting Padding.

### R2019b: Multipixel streaming

The Edge Detector block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel.

For multipixel streaming, the block supports input and output column vectors of 4
or 8 pixels. The **ctrl** port remains scalar, and the control
signals in the `pixelcontrol` bus apply to all pixels in the
vector.

### R2018b: Improved line buffer

The internal line buffer in this block now handles bursty data, that is,
noncontiguous valid signals within a pixel line. This implementation uses fewer
hardware resources due to improved padding logic and native support for kernel sizes
with an even number of lines. This change affects the Line Buffer
block and blocks that use an internal line buffer.

The latency of the line buffer is now reduced by a few cycles for some
configurations. You might need to rebalance parallel path delays in your model. A
best practice is to synchronize parallel paths in your model by using the pixel
stream control signals rather than by inserting a specific number of delays.

## Description

Find edges of objects in grayscale pixel stream

The Edge Detector block finds the edges in a grayscale pixel stream by
using the Sobel, Prewitt, or Roberts method. The block convolves the input pixels with
derivative approximation matrices to find the gradient of pixel magnitude along two
orthogonal directions. It then compares the sum of the squares of the gradients to the
square of a configurable threshold to determine if the gradients represent an
edge.

By default, the block returns a binary image as a stream of pixel values. A pixel
value of 1 indicates that the pixel is an edge. You can disable the edge output. You can
also enable output of the gradient values in the two orthogonal directions at each
pixel.
