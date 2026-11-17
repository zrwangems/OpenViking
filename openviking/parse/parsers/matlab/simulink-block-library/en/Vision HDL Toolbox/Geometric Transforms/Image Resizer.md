---
type: simulink-block
title: 'Image Resizer'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transforms'
documentation_page: 'imageresizer'
documentation_source_path: 'ref/imageresizer.html'
language: en
---

# Image Resizer

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar
  direction: input
  data_types: uint8 | uint16 | fixdt(0,WL,0), WL between 8 and 16 | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: inputSize
  summary: Dimensions of active frame in input stream [ActiveVideoLines,ActivePixelsPerLine]
  direction: input
  data_types: single | double | uint8 | uint16 | fixdt(0,WL,0), WL up to 16
- name: outputSize
  summary: Dimensions of active frame in output stream [ActiveVideoLines,ActivePixelsPerLine]
  direction: input
  data_types: single | double | uint8 | uint16 | fixdt(0,WL,0), WL up to 16
- name: pixel
  summary: Output pixel stream scalar
  direction: output
  data_types: uint8 | uint16 | fixdt(0,WL,0), WL between 8 and 16 | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: output
  data_types: bus
```

### Input

### **pixel** — Input pixel stream scalar

Single pixel, specified as a scalar value.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint8` | `uint16` | `fixdt(0,WL,0), WL between 8 and 16` | `double` | `single`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`

### **inputSize** — Dimensions of active frame in input stream `[ActiveVideoLines,ActivePixelsPerLine]`

Dimensions of the input frame, specified as a row vector of the form
[*ActiveVideoLines*,*ActivePixelsPerLine*]. The
dimensions must be integers greater than or equal to `[16,16]` and
less than or equal to `[4320,8192]`.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable this port, set the **Input size source** parameter to
`Input port`.

If you enable both **inputSize** and
**outputSize** ports, and those inputs use a fixed point type,
both ports must use the same fixed point type.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `fixdt(0,WL,0), WL up to 16`

### **outputSize** — Dimensions of active frame in output stream `[ActiveVideoLines,ActivePixelsPerLine]`

Dimensions of the output frame, specified as a row vector of the form
[*ActiveVideoLines*,*ActivePixelsPerLine*]. The
dimensions must be integers greater than or equal to `[16,16]` and
less than or equal to `[4320,8192]`.

The output dimensions must be less than or equal to the input
dimensions.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

This port appears when you set the **Output size source**
parameter to `Input port`.

If you enable both **inputSize** and
**outputSize** ports, and those inputs use a fixed point type,
both ports must use the same fixed point type.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `fixdt(0,WL,0), WL up to 16`
### Output

### **pixel** — Output pixel stream scalar

Configure the data type of the output pixel by using the
**Output** parameter on the **Data Type**
tab.

**Data Types:** `uint8` | `uint16` | `fixdt(0,WL,0), WL between 8 and 16` | `double` | `single`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Input height and width
  summary: Dimensions of active frame in input stream [1080,1920] (default) | [ActiveVideoLines,ActivePixelsPerLine]
  group: Main
- name: Input size source
  summary: Source of input active frame size Property (default) | Input port
  group: Main
- name: Maximum input height and width
  summary: Active frame size that accommodates the largest anticipated input size [1080,1920] (default) | [ActiveVideoLines,ActivePixelsPerLine]
  group: Main
- name: Output height and width
  summary: Dimensions of active frame in output stream [720,1280] (default) | [ActiveVideoLines,ActivePixelsPerLine]
  group: Main
- name: Output size source
  summary: Source of input active frame size Property (default) | Input port
  group: Main
- name: Maximum output height and width
  summary: Active frame size that accommodates the largest anticipated output size [720, 1280] (default) | [ActiveVideoLines,ActivePixelsPerLine]
  group: Main
- name: Insert horizontal blanking
  summary: Add invalid cycles between active lines off (default) | on
  group: Main
- name: Minimum output horizontal blanking
  summary: Number of inactive cycles to insert between output lines 370 (default)
  group: Main
- name: Interpolation method
  summary: Method of interpolating pixel values Bilinear (default) | Nearest Neighbor
  group: Main
- name: Perform antialiasing on downscale
  summary: Apply antialiasing filter before resizing on (default) | off
  group: Main
- name: Rounding mode
  summary: Rounding method for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round
    | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow action for internal fixed-point calculations off (default) | on
  group: Data Types
- name: Coefficients
  summary: Interpolation filter coefficients data type fixdt(0,16) (default) | <data type expression>
  group: Data Types
- name: Output
  summary: 'Output data type Inherit: Same as first input (default) | fixdt(0,16,0) | <data type expression>'
  group: Data Types
```

### Main

### **Input height and width** — Dimensions of active frame in input stream `[1080,1920]` (default) | `[ActiveVideoLines,ActivePixelsPerLine]`

Dimensions of the input frame, specified as a row vector of the form
[*ActiveVideoLines*,*ActivePixelsPerLine*]. The
dimensions must be integers greater than or equal to `[16,16]` and
less than or equal to `[4320,8192]`.

#### Dependencies

This parameter appears when you set the **Input size source**
parameter to `Property`.

### **Input size source** — Source of input active frame size `Property` (default) | `Input port`

Source of the input active frame size, specified as one of these options:

- `Property` — Specify the input size by using the
  **Input height and width** parameter.
- `Input port` — Specify the input size by using the
  **inputSize** input port. The block samples the
  **inputSize** and **outputSize** ports when
  `vStart` is `true` in the input control
  bus.

### **Maximum input height and width** — Active frame size that accommodates the largest anticipated input size `[1080,1920]` (default) | `[ActiveVideoLines,ActivePixelsPerLine]`

Dimensions of the largest anticipated input frame, specified as a row vector of
the form [*ActiveVideoLines*,*ActivePixelsPerLine*].
The dimensions must be integers greater than or equal to `[16,16]`
and less than or equal to `[4320,8192]`.

#### Dependencies

This parameter appears when you set the **Input size source**
parameter to `Input port`.

### **Output height and width** — Dimensions of active frame in output stream `[720,1280]` (default) | `[ActiveVideoLines,ActivePixelsPerLine]`

Dimensions of the output frame, specified as a matrix of the form
[*ActiveVideoLines*,*ActivePixelsPerLine*]. The
dimensions must be integers greater than or equal to `[16,16]` and
less than or equal to `[4320,8192]`.

The output dimensions must be less than or equal to the input
dimensions.

#### Dependencies

This parameter appears when you set the **Output size source**
parameter to `Property`.

### **Output size source** — Source of input active frame size `Property` (default) | `Input port`

Source of the output active frame size, specified as one of these options:

- `Property` — Specify the output size by using the
  **Output height and width** parameter.
- `Input port` — Specify the output size by using the
  **outputSize** input port. The block samples the
  **inputSize** and **outputSize** ports when
  `vStart` is `true` in the input control
  bus.

### **Maximum output height and width** — Active frame size that accommodates the largest anticipated output size `[720, 1280]` (default) | `[ActiveVideoLines,ActivePixelsPerLine]`

Dimensions of the largest anticipated output frame, specified as a row vector of
the form [*ActiveVideoLines*,*ActivePixelsPerLine*].
The dimensions must be integers greater than or equal to `[16,16]`
and less than or equal to `[4320,8192]`.

#### Dependencies

This parameter appears when you set the **Output size source**
parameter to `Input port`.

### **Insert horizontal blanking** — Add invalid cycles between active lines off (default) | on

The horizontal blanking interval is the period of inactive cycles between the end
of one line and the beginning of the next line. When you select this option, the block
includes a buffer to store the output pixels while inserting extra horizontal blanking
cycles between the active lines of the output video stream. Set the number of blanking
cycles in the **Minimum output horizontal blanking** parameter. For
information on when to use horizontal blanking, see Configure Blanking Intervals.

### **Minimum output horizontal blanking** — Number of inactive cycles to insert between output lines `370` (default)

The horizontal blanking interval is the period of inactive cycles between the end
of one line and the beginning of the next line. If your downstream processing requires
a certain blanking interval, specify that interval in this parameter. This parameter
value must be an integer between `1` and `1195`. The
block includes a buffer that stores the output pixels until the minimum number of
blanking cycles is reached.

The recommended minimum horizontal blanking interval for Vision HDL Toolbox library blocks that use a line buffer is 2×*Kw* when
using padding or 12 cycles when you set the **Padding method**
parameter to `None`. For more information on blanking
requirements for image processing systems, see Configure Blanking Intervals.

#### Dependencies

To enable this parameter, select **Insert horizontal
blanking**.

### **Interpolation method** — Method of interpolating pixel values `Bilinear` (default) | `Nearest Neighbor`

Method of interpolating pixel values in horizontal and vertical directions,
specified as one of these types:

- `Bilinear` — The block implements a two-tap filter
  in each direction, where the taps are the current and previous pixel values.
- `Nearest Neighbor` — The object implements muxes to
  select the closest of the current pixel value or the previous pixel value. This
  interpolation method uses the fewest hardware resources, at the tradeoff of
  coarser interpolation accuracy.

For more information about interpolation methods, see the Change Image Size example.

Comparison of interpolation accuracy

### **Perform antialiasing on downscale** — Apply antialiasing filter before resizing on (default) | off

When you set this property to `true`,
the object applies an antialiasing filter to the
input image before the resize operation. The antialiasing filter is a separable 5-by-5
filter. The coefficients are `[1 4 6 4
1]/16`.

### Data Types

### **Rounding mode** — Rounding method for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Specify a rounding method for internal fixed-point calculations.

### **Saturate on integer overflow** — Overflow action for internal fixed-point calculations `off` (default) | `on`

When you clear this parameter, fixed-point and integer values wrap around to zero when
the value overflows what is representable with that data type. When you select this
parameter, the value saturates at the maximum representable value.

### **Coefficients** — Interpolation filter coefficients data type `fixdt(0,16)` (default) | `<data type expression>`

Specify the data type of the filter coefficients as a data type expression in the
form `fixdt(0,WL)`, where the type is unsigned and
*WL* is a word length in the range 2 to 17. The block computes the
binary point scaling to accommodate the interpolation coefficients. When converting
the coefficients to the specified data type, the block uses the settings of the
**Rounding method** and **Overflow action**
parameters.

The interpolation filter also limits the internal pixel data types to 24 bits wide
so that the filter maps to DSP blocks on your FPGA.

### **Output** — Output data type `Inherit: Same as first input` (default) | `fixdt(0,16,0)` | `<data type expression>`

Specify the data type of the output pixels as `Inherit: Same as first
input` or as a data type expression in the form
`fixdt(0,WL,0)`, where the type is unsigned, and
*WL* is a word length in the range 8 to 16.

- `Inherit: Same as first input` — Sets the data
  type of the output pixels to match the data type of the input
  **pixel** port.
- `<data type expression>` — Sets the data
  type of the output pixels to this data type.

When converting the pixel values to the specified data type, the block uses the
settings of the **Rounding method** and **Overflow
action** parameters.
## Libraries

Vision HDL Toolbox / Geometric Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

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

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2023a**

## Description

Change dimensions of image in pixel stream

The Image Resizer block downscales grayscale input images.
The horizontal and vertical scale factors are independent
and you can optionally specify input and output sizes in real time.
The block provides an optional antialiasing filter, and
you can choose nearest-neighbor or bilinear
interpolation.

You can use this block for image resize operations such as:

- Converting images to a uniform size for input to deep learning algorithms
- Modifying disparate source videos for processing, resource, or display
  requirements
