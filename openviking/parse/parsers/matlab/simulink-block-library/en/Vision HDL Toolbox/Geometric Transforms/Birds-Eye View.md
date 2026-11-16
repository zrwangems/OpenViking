---
type: simulink-block
title: 'Birds-Eye View'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transforms'
documentation_page: 'birdseyeview'
documentation_source_path: 'ref/birdseyeview.html'
language: en
---

# Birds-Eye View

## Ports

### Input

### **pixel** — Input pixel stream scalar

Single image pixel in a pixel stream, specified as a scalar that
represents grayscale intensity.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`
### Output

### **pixel** — Output pixel stream scalar

Single image pixel in the pixel stream, returned as a scalar
representing grayscale intensity. The output pixel data type is the same
as the input pixel data type.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`

## Parameters

### **Homography matrix** — Transfer function derived from camera parameters `[0.000100990123328 0 0;0.000412396945637 0.001302203393162 1.293171994e-06;-0.103019798961327 -0.255811259450009 -0.000222053779501]` (default) | 3-by-3 matrix

Transfer function derived from camera parameters, specified as a 3-by-3
matrix.

The homography matrix, *h*, is derived from four
intrinsic parameters of the physical camera setup: the focal length, pitch,
height, and principal point (from a pinhole camera model). The default value
is the matrix for the camera setup used in the Lane Detection example.

This matrix can be calculated from physical camera properties, or
empirically derived by analyzing an image of a grid test pattern taken by
the camera. See `estimateGeometricTransform` (Computer Vision Toolbox) or
Using the Single Camera Calibrator App (Computer Vision Toolbox).

### **Maximum buffer size, in pixels** — Number of input pixels to buffer `40000` (default) | integer

Number of input pixels to buffer, specified as an integer. Compute this
value from **Number of input lines to
buffer**\**ActivePixelsPerLine*. The block uses
a memory of this size to store the input pixels. If you specify a value that
is not a power of two, the block uses the next largest power of two.

### **Number of input lines to buffer** — Number of lines to transform `54` (default) | integer

Number of lines to transform, specified as an integer. The block stores
and transforms this number of lines into the output bird's-eye view image,
starting at the vanishing point as determined by the **Homography
matrix**.

Storing the full input frame uses too much memory to implement the
algorithm without off-chip storage. Therefore, for a hardware
implementation, choose a smaller region to store and transform, one that
generates an acceptable output frame size.

For example, using the default **Homography matrix** with
an input image of 640-by-480 pixels, the full-sized transform results in a
900-by-640 output image. Analysis of the input-to-output
*x*-coordinate mapping shows that around 50 lines of
the input image are required to generate the top 700 lines of the bird's-eye
view output image. This number of input lines can be stored using on-chip
memory. The vanishing point for the default camera setup is around line 200,
and lines above that point do not contribute to the resulting bird's-eye
view. Therefore, the block can store only input lines 200–250 for
transformation.

### **Output active pixels** — Horizontal size of output frame `640` (default) | integer

Horizontal size of output frame, specified as an integer. This parameter
is the number of active pixels in each output line.

### **Output active lines** — Vertical size of output frame `700` (default) | integer

Vertical size of output frame, specified as an integer. This parameter is
the number of active lines in each output frame.

## Libraries

Vision HDL Toolbox / Geometric Transforms

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

## Version History

**Introduced in R2017b**

## Description

Transform front-facing camera image into top-down view

The Birds-Eye View block warps a front-facing camera image into a
top-down view. It uses a hardware-efficient architecture that supports HDL code
generation.

You must provide the homography matrix that describes the transform. This matrix can
be calculated from physical camera properties, or empirically derived by analyzing an
image of a grid pattern taken by the camera. The block uses the matrix to compute the
transformed coordinates of each pixel. The transform does not interpolate between pixel
locations. Instead it rounds the result to the nearest coordinate.

The block operates on a trapezoidal region of the input image below the vanishing
point. These images show the input region selected for transformation and the resulting
top-down view.

You can specify the number of lines in the transformed region and the size of the
output frame. If the specified homography matrix cannot map from the requested number of
lines to the requested output size, the block returns a warning.

Because the block replicates lines from the input region to create the larger output
frame, it cannot complete the transform of one frame before the next frame arrives. The
block ignores any new input frames while it is still transforming the previous frame.
Therefore, depending on the stored lines and output size, the block can drop input
frames. This timing also enables the block to maintain the blanking intervals of the
input pixel stream.
