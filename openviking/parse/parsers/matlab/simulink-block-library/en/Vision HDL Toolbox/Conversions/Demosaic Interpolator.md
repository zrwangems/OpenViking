---
type: simulink-block
title: 'Demosaic Interpolator'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'demosaicinterpolator'
documentation_source_path: 'ref/demosaicinterpolator.html'
language: en
---

# Demosaic Interpolator

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar | vector
  direction: input
  data_types: uint | fixdt(0,W,F) | single | double
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: pixel
  summary: Output pixel stream vector | matrix
  direction: output
  data_types: uint | fixdt(0,W,F) | single | double
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: output
  data_types: bus
```

### Input

### **pixel** — Input pixel stream scalar | vector

For single pixel streams, specify **pixel** as a
scalar. For multipixel streams, specify **pixel** as a
vector of **Number of pixels**-by-1 pixel values.
**Number of pixels** can be two, four, or eight.
Images in the Bayer format have one color component for each pixel
location. Select the sequence of R, G, and B pixels by using the
**Sensor alignment** parameter.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `fixdt(0,W,F)` | `single` | `double`

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

### **pixel** — Output pixel stream vector | matrix

For single pixel streams, the output **pixel** is a
three-element vector of RGB values. For multipixel streams, the output
**pixel** is a matrix of **Number of
pixels**-by-3 RGB values. The block calculates the values
of the missing color components for each pixel, using the method you
specify in the **Interpolation algorithm**
parameter.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `fixdt(0,W,F)` | `single` | `double`

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
- name: Interpolation algorithm
  summary: Algorithm used to calculate missing pixel values Gradient-corrected linear (default) | Bilinear
  group: ''
- name: Sensor alignment
  summary: Color sequence of the pixels in the input stream RGGB (default) | GBRG | GRBG | BGGR
  group: ''
- name: Line buffer size
  summary: Size of line memory buffer 2048 (default) | integer
  group: ''
```

### **Interpolation algorithm** — Algorithm used to calculate missing pixel values `Gradient-corrected linear` (default) | `Bilinear`

Algorithm used to calculate missing pixel values, specified as one of the
following:

- `Gradient-corrected linear` —
  Bilinear average, corrected for intensity gradient
- `Bilinear` — Average of the
  pixel values in the surrounding 3-by-3 neighborhood

### **Sensor alignment** — Color sequence of the pixels in the input stream `RGGB` (default) | `GBRG` | `GRBG` | `BGGR`

Select the sequence of R, G, and B pixels that correspond to the 2-by-2
block of pixels in the top-left corner of the input image. Specify the
sequence in left-to-right, top-to-bottom order. For instance, the default
sequence of `RGGB` represents an image with this pattern.

Two-by-two grid with R and G across the top and G and B across the bottom

### **Line buffer size** — Size of line memory buffer `2048` (default) | integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

When you use multipixel input, this value must accommodate (**Active pixels per line**)/(**Number of pixels**) + 2.

The total memory size allocated depends on your selection of
**Interpolation algorithm**:

- `Bilinear`: 2-by-**Line
  buffer size** memory locations
- `Gradient-corrected linear`:
  4-by-**Line buffer size** memory
  locations
## Libraries

Vision HDL Toolbox / Conversions

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

### R2022a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021b: Multipixel streaming

The Demosaic Interpolator block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel.

The block accepts an input vector of *NumPixels*-by-1 values and
returns an output matrix of *NumPixels*-by-3 values. The
**ctrl** ports remain scalar, and the control signals in the
`pixelcontrol` bus apply to all pixels in the matrix.

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

Construct RGB pixel data from Bayer pattern pixel stream

The Demosaic Interpolator block provides a Bayer pattern interpolation
filter for streaming video data. The block implements the calculations using
hardware-efficient, multiplier-free algorithms for HDL code generation. You can select a
low-complexity bilinear interpolation, or a moderate-complexity gradient-corrected
bilinear interpolation.

- When you select bilinear interpolation, the block operates on a 3-by-3 pixel
  window using only additions and bit shifts.
- When you select gradient correction, the block operates on a 5-by-5 pixel
  window. The calculation is performed using bit shift, addition, and low-order
  canonical signed digit (CSD) multiplication.
