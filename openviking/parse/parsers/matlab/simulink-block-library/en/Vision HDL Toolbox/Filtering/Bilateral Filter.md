---
type: simulink-block
title: 'Bilateral Filter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'bilateralfilter'
documentation_source_path: 'ref/bilateralfilter.html'
language: en
---

# Bilateral Filter

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
- name: pixel
  summary: Output pixel stream scalar | vector
  direction: output
  data_types: uint | int | fixed point | double | single
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
### Output

### **pixel** — Output pixel stream scalar | vector

Output pixel stream, returned as a scalar value representing
intensity, or as a vector of two, four, or eight pixel intensity values.
The dimensions and data type of the output **pixel**
port match the dimensions and data type of the input
**pixel** port.

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
## Parameters
```yaml
parameters:
- name: Neighborhood size
  summary: Size of image region to average 3×3 (default) | 5×5 | 7×7 | 9×9 | 11×11 | 13×13 | 15×15
  group: Main
- name: Spatial standard deviation
  summary: Spatial standard deviation target 0.5 (default) | positive real number
  group: Main
- name: Intensity standard deviation
  summary: Intensity standard deviation target 0.5 (default) | positive real number
  group: Main
- name: Padding method
  summary: Method for padding boundary of input image Constant (default) | Replicate | Symmetric | Reflection | None
  group: Main
- name: Padding value
  summary: Value used to pad boundary of input image 0 (default) | integer
  group: Main
- name: Line buffer size
  summary: Size of line memory buffer 2048 (default) | positive integer
  group: Main
- name: Rounding mode
  summary: Rounding method for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round
    | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow mode for internal fixed-point calculations on (default) | off
  group: Data Types
- name: Coefficients
  summary: 'Method to determine data type of filter coefficients Inherit: Same as first input (default) | fixdt(1,16,0) |
    data type expression'
  group: Data Types
- name: Output
  summary: 'Method to determine data type of output pixels Inherit: Same as first input (default) | fixdt(1,16,0) | data type
    expression'
  group: Data Types
```

### Main

### **Neighborhood size** — Size of image region to average `3×3` (default) | `5×5` | `7×7` | `9×9` | `11×11` | `13×13` | `15×15`

Size of the image region used to compute the average, specified as an
*N*-by-*N* pixel square.

### **Spatial standard deviation** — Spatial standard deviation target `0.5` (default) | positive real number

Spatial standard deviation target used to compute coefficients for the
spatial Gaussian filter, specified as a positive real number. This
parameter has no limits, but recommended values are from 0.1 to 10. At
the high end, the distribution becomes flat and the coefficients are
small. At the low end, the distribution peaks in the center and has
small coefficients in the rest of the neighborhood. These boundary
values also depend on the neighborhood size and the data type used for
the coefficients.

### **Intensity standard deviation** — Intensity standard deviation target `0.5` (default) | positive real number

Intensity standard deviation target used to compute coefficients for
the intensity Gaussian filter, specified as a positive real number. This
parameter has no limits, but recommended values are from 0.1 to 10. At
the high end, the distribution becomes flat and the coefficients are
small. At the low end, the distribution peaks in the center and has
small coefficients in the rest of the neighborhood. These boundary
values also depend on the neighborhood size and the data type used for
the coefficients.

When the intensity standard deviation is large, the bilateral filter
acts more like a Gaussian blur filter, because the intensity Gaussian
has a lower peak. Conversely, when the intensity standard deviation is
smaller, edges in the intensity are preserved or enhanced.

### **Padding method** — Method for padding boundary of input image `Constant` (default) | `Replicate` | `Symmetric` | `Reflection` | `None`

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

### Data Types

### **Rounding mode** — Rounding method for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Specify a rounding method for internal fixed-point calculations.

### **Saturate on integer overflow** — Overflow mode for internal fixed-point calculations on (default) | off

When the input is any integer or fixed-point data type, the algorithm
uses fixed-point arithmetic for internal calculations. By default,
fixed-point values saturate on overflow. This option does not apply when
the input data type is `single` or
`double`.

### **Coefficients** — Method to determine data type of filter coefficients `Inherit: Same as first input` (default) | `fixdt(1,16,0)` | data type expression

Specify an unsigned data type that can represent values less than 1.
The coefficients usually require a data type with more precision than
the input data type. The block calculates the coefficients based on the
neighborhood size and the values of **Intensity standard
deviation** and **Spatial standard
deviation**. Larger neighborhoods spread the Gaussian
function such that each coefficient value is smaller. A larger standard
deviation flattens the Gaussian so that the coefficients are more
uniform in nature, and a smaller standard deviation produces a peaked
response.

**Note**

If you try a data type and after quantization, more than half of
the coefficients become zero, the block issues a warning. If all the
coefficients are zero after quantization, the block issues an error.
These messages mean that the block was unable to express the
requested filter by using the data type specified. To avoid this
issue, choose a higher-precision coefficient data type or adjust the
standard deviation targets.

### **Output** — Method to determine data type of output pixels `Inherit: Same as first input` (default) | `fixdt(1,16,0)` | data type expression

The filtered pixel values are cast to this data type.
## Libraries

Vision HDL Toolbox / Filtering

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

### R2022a: Multipixel streaming

The Bilateral Filter block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel.

The block supports input column vectors of *NumPixels* values,
where *NumPixels* can be 2, 4, or 8. The **ctrl**
ports remain scalar, and the control signals in the `pixelcontrol`
bus apply to all pixels in the matrix. The block returns an output vector of the
same size as the input vector.

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

### R2018b: Improved line buffer

The internal line buffer in this block now handles bursty data, that is,
noncontiguous valid signals within a pixel line. This implementation uses fewer
hardware resources due to improved padding logic and native support for kernel sizes
with an even number of lines. This change affects the Line Buffer
block and blocks that use an internal line buffer.

The latency of the line buffer is now reduced by a few cycles for some
configurations. You might need to rebalance parallel path delays in your models. A
best practice is to synchronize parallel paths in your models by using the pixel stream
control signals rather than by inserting a specific number of delays.

## Description

2-D bilateral filtering

The Bilateral Filter block filters images while preserving edges. Some
applications of bilateral filtering are denoising while preserving edges, separating
texture from illumination, and cartooning to enhance edges. The filter replaces each
pixel at the center of a neighborhood by an average that is calculated using spatial and
intensity Gaussian filters. The block determines the filter coefficients from:

- Spatial location in the neighborhood (similar to a Gaussian blur
  filter)
- Intensity difference from the neighborhood center value

The block provides two standard deviation parameters for independent
control of the spatial and intensity coefficients.
