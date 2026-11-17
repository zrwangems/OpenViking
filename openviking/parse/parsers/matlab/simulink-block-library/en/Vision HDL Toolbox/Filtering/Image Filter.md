---
type: simulink-block
title: 'Image Filter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'imagefilter'
documentation_source_path: 'ref/imagefilter.html'
language: en
---

# Image Filter

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
- name: coeff
  summary: Filter coefficients matrix
  direction: input
  data_types: int | uint | fixed point | single | double
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

### **coeff** — Filter coefficients matrix

Specify the filter coefficients as a 2-D matrix of numeric values. Each dimension
of the matrix must have at least 2 elements, but no more than 64 elements.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

The block samples the values from the **coeff** port only at the
start of a frame and ignores any changes within a frame.

#### Dependencies

To enable this port, set the **Filter coefficients source**
parameter to `Input port`.

**Data Types:** `int` | `uint` | `fixed point` | `single` | `double`
### Output

### **pixel** — Output pixel stream scalar | vector

Output pixel stream, returned as a scalar value representing intensity, or as a
vector of two, four, or eight pixel intensity values. The dimensions and data type of
the output **pixel** port match the dimensions and data type of the
input **pixel** port.

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
- name: Filter coefficients source
  summary: Source to provide filter coefficients Property (default) | Input port
  group: Main
- name: Filter coefficients
  summary: Coefficients of filter [ 1, 0; 0, -1 ] (default) | matrix
  group: Main
- name: Padding method
  summary: Method for padding Constant (default) | Replicate | Symmetric | Reflection | None
  group: Main
- name: Padding value
  summary: Value used to pad boundary of input image 0 (default) | integer
  group: Main
- name: Line buffer size
  summary: Size of line buffer 2048 (default) | integer
  group: Main
- name: Rounding mode
  summary: Rounding method for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round
    | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow action for internal fixed-point calculations off (default) | on
  group: Data Types
- name: Coefficients
  summary: 'Filter coefficients data type Inherit: Same as first input (default) | fixdt(1,16,0) | <data type expression>'
  group: Data Types
- name: Output
  summary: 'Output data type Inherit: Same as first input (default) | Inherit: Inherit via internal rule | fixdt(1,16,0) |
    <data type expression>'
  group: Data Types
- name: Lock data type settings against changes by the fixed-point tools
  summary: Lock data type settings off (default) | on
  group: Data Types
```

### Main

### **Filter coefficients source** — Source to provide filter coefficients `Property` (default) | `Input port`

Select the source for specifying the filter coefficients.

- `Property` (default) — Use this value to
  specify filter coefficients using the **Filter coefficients**
  parameter.
- `Input port` — Use this value to specify
  filter coefficients through the **coeff** input port.

### **Filter coefficients** — Coefficients of filter `[ 1, 0; 0, -1 ]` (default) | matrix

Specify the filter coefficients as a matrix. Each dimension of the matrix must
have at least 2 elements, but no more than 64 elements.

#### Dependencies

To enable this parameter, set the **Filter coefficients
source** parameter to `Property`.

### **Padding method** — Method for padding `Constant` (default) | `Replicate` | `Symmetric` | `Reflection` | `None`

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

### **Line buffer size** — Size of line buffer `2048` (default) | integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

The block allocates (*N* – 1)-by-**Line buffer
size** memory locations to store the pixels. *N*
represents the rows of the coefficient matrix.

### Data Types

### **Rounding mode** — Rounding method for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Specify a rounding method for internal fixed-point calculations.

### **Saturate on integer overflow** — Overflow action for internal fixed-point calculations `off` (default) | `on`

When you clear this parameter, fixed-point and integer values wrap around to zero when
the value overflows what is representable with that data type. When you select this
parameter, the value saturates at the maximum representable value.

### **Coefficients** — Filter coefficients data type `Inherit: Same as first input` (default) | `fixdt(1,16,0)` | `<data type expression>`

Select the method for determining the data type of the filter coefficients.

Click the Show data type assistant button to display the **Data Type
Assistant**, which helps you set the data type of the
**Coefficients** parameter. For details, see Specify Data Types Using Data Type Assistant (Simulink).

When converting the coefficients to the specified data type, the block rounds to
the nearest representable value and saturates to the maximum value if the value
exceeds the maximum value representable with the data type.

#### Dependencies

To enable this parameter, set the **Filter coefficients
source** parameter to `Property`.

### **Output** — Output data type `Inherit: Same as first input` (default) | `Inherit: Inherit via internal rule` | `fixdt(1,16,0)` | `<data type expression>`

Select the method for determining the data type of the output pixel.

Click the Show data type assistant button to display the **Data Type
Assistant**, which helps you to set the data type of the
**Output** parameter. For details, see Specify Data Types Using Data Type Assistant (Simulink).

### **Lock data type settings against changes by the fixed-point tools** — Lock data type settings `off` (default) | `on`

Select this parameter to lock all data type settings of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).
## Libraries

Vision HDL Toolbox / Filtering

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
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

You cannot generate HDL code for this block if it is inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2015a**

### R2025a: Display algorithm latency on block mask

The block now shows its latency on the block mask. The latency displays as a number of
lines and pixels. The exact number of clock cycles depends on the number of pixels in a line
of your image frame and the input pixel valid pattern. Use the displayed latency information
along with the `pixelcontrol` bus signals to align parallel data paths in
your design.

### R2022a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021b: Reflection padding

Pad the edge of a frame by reflecting around the edge-pixel value. This padding method
helps reduce edge contrast effects and can improve results for machine learning while
maintaining the original frame size.

### R2020a: Option to omit padding

You can now configure the block to not add padding around the boundaries of the active
frame. This option reduces the hardware resources used by the block and reduces the blanking
interval required between frames but affects the accuracy of the output pixels at the edges
of the frame. To use this option, set the **Padding method** parameter to
`None`. For an example, see Increase Throughput by Omitting Padding.

### R2019b: Multipixel streaming

The block now supports multipixel streams. The HDL implementation replicates the
algorithm for each pixel in parallel.

For multipixel streaming, the block supports input and output column vectors of 4 or 8
pixels. The **ctrl** port remains scalar, and the control signals in the
`pixelcontrol` bus apply to all pixels in the vector.

### R2019a: Increased kernel size limits

The block now allows for a coefficient kernel with up to 64-by-64 elements.

### R2018b: Programmable coefficients

The block now accepts coefficients from an input port. Each dimension of the matrix must
have at least 2 and no more than 16 elements. The block samples the values from the
**coeff** port at the start of a frame only and ignores any changes
within a frame.

In previous releases, you could specify a row vector of coefficients, that is, a matrix
of 1-by-N elements. Now, the coefficient matrix must have at least 2 elements in each
dimension.

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

2-D FIR filtering

The Image Filter block performs two-dimensional finite impulse response
(FIR) filtering on a pixel stream and supports the use of programmable filter
coefficients.
