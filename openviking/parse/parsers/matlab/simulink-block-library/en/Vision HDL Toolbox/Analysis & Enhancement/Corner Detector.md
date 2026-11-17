---
type: simulink-block
title: 'Corner Detector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'cornerdetector'
documentation_source_path: 'ref/cornerdetector.html'
language: en
---

# Corner Detector

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar
  direction: input
  data_types: uint | int | fixed point | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: minC
  summary: Threshold that indicates corner for FAST algorithm nonnegative integer
  direction: input
  data_types: single | double | uint | fixed point
- name: thresh
  summary: Threshold that indicates corner for Harris algorithm nonnegative integer
  direction: input
  data_types: single | double | uint | fixed point
- name: corner
  summary: Metric that indicates whether pixel is a corner scalar
  direction: output
  data_types: uint | int | fixed point | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: output
  data_types: bus
```

### Input

### **pixel** — Input pixel stream scalar

Single image pixel in a pixel stream, specified as a scalar that
represents grayscale intensity.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`

### **minC** — Threshold that indicates corner for FAST algorithm nonnegative integer

Threshold that indicates a corner for the FAST algorithm, specified as
a nonnegative integer. Each pixel in the circle is subtracted from the
center pixel value, and only those differences that exceed this
threshold are used to determine if the center pixel is a corner and to
calculate the output metric. This value is cast to the same data type as
the input **pixel**.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable this port, set the **Method** parameter
to one of the FAST options and set the **Source of minimum
contrast value** parameter to `Input
port`.

**Data Types:** `single` | `double` | `uint` | `fixed point`

### **thresh** — Threshold that indicates corner for Harris algorithm nonnegative integer

Threshold that indicates a corner for the Harris algorithm, specified
as a nonnegative integer. This value represents an approximation of the
eigenvalues of the Harris matrix calculated from the gradient results.
The block returns a corner for pixels where the eigenvalue metric
exceeds this threshold. This value is cast to the same data type as the
output **pixel**. The corner metrics are in the range
of a fourth power of the input pixel values. For example, for an 8-bit
input pixel, the full-precision output size is 44 bits.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable this port, set the **Method** parameter
to `Harris` and set the **Source of
threshold value** parameter to `Input
port`.

**Data Types:** `single` | `double` | `uint` | `fixed point`
### Output

### **corner** — Metric that indicates whether pixel is a corner scalar

Metric that indicates whether the pixel is a corner, returned as a
scalar of the numeric type specified by the **Output**
data type parameter. When the pixel is not a corner, the block returns
zero for this value.

For corners detected with the FAST algorithm, this value is a contrast
metric computed by using the sum-of-absolute-difference (SAD) of the
pixels around the circle with the center pixel value. The metric
includes only those differences that exceed the threshold.

For corners detected with the Harris algorithm, this value is the
approximation of the eigenvalues of the Harris matrix calculated from
the gradient results.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `int` | `fixed point` | `double` | `single`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Method
  summary: Detection method FAST 5 of 8 (default) | FAST 7 of 12 | FAST 9 of 16 | Harris
  group: Main
- name: Source of minimum contrast value
  summary: Source for threshold that indicates corner for FAST algorithm Property (default) | Input port
  group: Main
- name: MinContrast value
  summary: Threshold that indicates corner for FAST algorithm 20 (default) | nonnegative integer
  group: Main
- name: Source of threshold value
  summary: Source for threshold that indicates corner for Harris algorithm Property (default) | Input port
  group: Main
- name: Threshold value
  summary: Threshold that indicates corner for Harris algorithm 2000 (default) | nonnegative integer
  group: Main
- name: Line buffer size
  summary: Size of line buffer 2048 (default) | integer
  group: Main
- name: Padding method
  summary: Method for padding Symmetric (default) | Replicate | Reflection | None
  group: Main
- name: Rounding mode
  summary: Rounding method for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round
    | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow action for internal fixed-point calculations off (default) | on
  group: Data Types
- name: Output
  summary: Data type for corner output port Inherit same as first input (default) | data type expression | Inherit via internal
    rule
  group: Data Types
```

### Main

### **Method** — Detection method `FAST 5 of 8` (default) | `FAST 7 of 12` | `FAST 9 of 16` | `Harris`

Select the Harris algorithm, or the size of the circle for the FAST
algorithm. The three FAST options specify how many contiguous pixels on
the circle must exceed the threshold for the center pixel to be marked
as a corner. For the circles of 8, 12, and 16 pixels shown in these
figures, the block detects a corner when 5, 7, or 9 contiguous
pixels,respectively, are above the threshold. The block checks for this
number of contiguous pixels anywhere on the circle. The block uses a
kernel of size 3-by-3 for `FAST 5 of 8`, 5-by-5
for `FAST 7 of 12`, and 7-by-7 for
`FAST 9 of 16`.

Diagrams of the three sizes of kernels with the circle of pixels around the center pixel.

### **Source of minimum contrast value** — Source for threshold that indicates corner for FAST algorithm `Property` (default) | `Input port`

Specify `Property` to set the threshold by
using the **MinContrast value** parameter. Specify
`Input port` to enable the
**minC** port.

#### Dependencies

To enable this parameter, set the **Method**
parameter to one of the FAST options.

### **MinContrast value** — Threshold that indicates corner for FAST algorithm `20` (default) | nonnegative integer

Each pixel in the circle is subtracted from the center pixel value,
and only those differences that exceed this threshold are used to
determine if the center pixel is a corner and to calculate the output
metric. This value is cast to the same data type as the input
**pixel**.

#### Dependencies

To enable this parameter, set the **Method**
parameter to one of the FAST options and set the **Source of
minimum contrast value** parameter to
`Property`.

### **Source of threshold value** — Source for threshold that indicates corner for Harris algorithm `Property` (default) | `Input port`

Specify `Property` to set the threshold by
using the **Threshold value** parameter. Specify
`Input port` to enable the
**thresh** port.

#### Dependencies

To enable this parameter, set the **Method**
parameter to `Harris`.

### **Threshold value** — Threshold that indicates corner for Harris algorithm `2000` (default) | nonnegative integer

This value represents an approximation of the eigenvalues of the
Harris matrix calculated from the gradient results. The block returns a
corner for pixels where the metric exceeds this threshold. For details,
see the Harris Corner Detection example. This value
is cast to the same data type as the output **corner**.
The corner metric is in the range of a fourth power of the input pixel
values. For example, for an 8-bit input pixel, the full-precision output
size is 44 bits.

#### Dependencies

To enable this parameter, set the **Method**
parameter to `Harris` and set the
**Source of threshold value** parameter to
`Property`.

### **Line buffer size** — Size of line buffer `2048` (default) | integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

The block allocates (*N*  – 1)-by-**Line
buffer size** memory locations to store the pixels.
*N* is the size of the kernel.

The block uses a kernel of size 3-by-3 when the
**Method** parameter is `FAST 5 of
8`, 5-by-5 when **Method** is
`FAST 7 of 12`, and 7-by-7 when
**Method** is `FAST 9 of
16`.

When you set **Method** to
`Harris`, the block uses one 1-by-3 kernel
and one 3-by-1 kernel for the gradient calculation and three 5-by-5
kernels for the circular window filter on the three gradient
components.

### **Padding method** — Method for padding `Symmetric` (default) | `Replicate` | `Reflection` | `None`

Select one of these methods for padding the boundary of the input
image. For more information about these methods, see Edge Padding.

- `Replicate` — Repeat the value of
  pixels at the edge of the image.
- `Symmetric` — Set the value of
  the padding pixels to mirror the edge of the image. This
  option prevents edges from being detected at the boundaries
  of the active frame.
- `Reflection` — Set the value of
  the padding pixels to reflect around the pixel at the edge
  of the image.
- `None` — Exclude padding logic. The block does not set the pixels
  outside the image frame to any particular value. This option reduces the hardware resources
  used by the block and the blanking required between frames but affects the accuracy of the
  output pixels at the edges of the frame. To maintain pixel stream timing, the output frame
  is the same size as the input frame. However, to avoid using pixels calculated from
  undefined padding values, mask off the *KernelSize*/2 pixels around the
  edge of the frame for downstream operations. For details, see Increase Throughput by Omitting Padding.

The circular window filters used in the Harris algorithm pad the edges
of the frame using `Replicate` padding.

### Data Types

### **Rounding mode** — Rounding method for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Specify a rounding method for internal fixed-point calculations.

### **Saturate on integer overflow** — Overflow action for internal fixed-point calculations `off` (default) | `on`

When you clear this parameter, fixed-point and integer values wrap around to zero when
the value overflows what is representable with that data type. When you select this
parameter, the value saturates at the maximum representable value.

### **Output** — Data type for **corner** output port `Inherit same as first input` (default) | data type expression | `Inherit via internal rule`

Specify a data type for the output **corner** port.
By default, the block returns the corner metric using the same data type
as the input **pixel** port.
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

## Version History

**Introduced in R2020a**

### R2021b: Reflection padding

Pad the edge of a frame by reflecting around the edge-pixel value. This padding
method helps reduce edge contrast effects and can improve results for machine
learning while maintaining the original frame size.

### R2020b: Harris corner detection

The block now provides a choice between the FAST algorithm and the Harris and
Stephens interconnecting edges algorithm. See Harris Corner Detection.

### R2020a: Option to omit padding

You can now configure the block to not add padding around the boundaries of the
active frame. This option reduces the hardware resources used by the block and the
blanking required between frames but affects the accuracy of the output pixels at
the edges of the frame. To use this option, set the **Padding
method** parameter to `None`. For an example,
see Increase Throughput by Omitting Padding.

## Description

Find corners using FAST or Harris algorithm

The Corner Detector block detects corners by using the
features-from-accelerated-segment test (FAST) algorithm or by the intersecting edges
(Harris) algorithm. For each pixel, if the pixel is a corner, the block returns the
corner metric. If the pixel is not a corner, the block returns a pixel value of
zero.

The FAST algorithm tests a circular area around the potential center of the corner.
The test detects a corner if a contiguous section of pixels are either brighter than the
center plus a threshold or darker than the center minus a threshold. You can specify a
minimum contrast threshold as a parameter or port and select from three rules to define
a corner. These rules specify how many pixels in a circle of pixels must exceed the
minimum contrast for the center pixel to be considered a corner. The block performs
parallel tests of all combinations of contiguous pixels around the circle. FAST uses
very little hardware resources

The Harris algorithm computes horizontal and vertical gradients, filters the gradient
components with a circular 5-by-5 Gaussian filter, and computes a metric that represents
the strength of the corner. You can specify a threshold that determines the level at
which corners are detected. The block returns a corner for pixels where the metric
exceeds this threshold. The Harris algorithm uses more hardware resources than the FAST
algorithm but can detect corners that the FAST algorithm might not find.
