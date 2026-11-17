---
type: simulink-block
title: 'Grayscale Erosion'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'grayscaleerosion'
documentation_source_path: 'ref/grayscaleerosion.html'
language: en
---

# Grayscale Erosion

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar
  direction: input
  data_types: uint8 | uint16 | uint32 | uint64 | double | single | fi(0,N,0)
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: pixel
  summary: Output pixel stream scalar
  direction: output
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: output
  data_types: bus
```

### Input

### **pixel** — Input pixel stream scalar

Single image pixel in a pixel stream, specified as an unsigned integer
scalar that represents grayscale intensity.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `double` | `single` | `fi(0,N,0)`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`
### Output

### **pixel** — Output pixel stream scalar

Single output pixel transformed by a morphological operation, returned as
a scalar value.

The data type of this output **pixel** is the same as the
data type of the input **pixel**.

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Neighborhood
  summary: Pixel neighborhood ones(3,3) (default) | vector or matrix of 1s and 0s
  group: ''
- name: Line buffer size
  summary: Size of line memory buffer 2048 (default) | positive integer
  group: ''
```

### **Neighborhood** — Pixel neighborhood `ones(3,3)` (default) | vector or matrix of `1`s and `0`s

Pixel neighborhood, specified as a vector or matrix of binary
values.

The block supports flat neighborhoods of up to 32-by-32
pixels. To use a structuring element, set the **Neighborhood** parameter to
`getnhood (Image Processing Toolbox)(strel (Image Processing Toolbox)(shape))`, where
*`shape`* is specified by the input arguments to the
`strel` (Image Processing Toolbox) function. The minimum
neighborhood size is a 2-by-2 matrix, or a 2-by-1 column vector. If the neighborhood is a
row vector, it must be at least 8 columns wide and contain no zeros.

### **Line buffer size** — Size of line memory buffer `2048` (default) | positive integer

Size of the line memory buffer, specified as a positive
integer. Choose a power of two that accommodates the number of active pixels in a horizontal
line. If you specify a value that is not a power of two, the buffer uses the next largest power
of two.

The block allocates (*n* –
1)-by-**Line buffer size** memory locations to store the pixels,
where *n* is the number of lines in the
**Neighborhood** parameter value.
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

You cannot generate HDL code for this block if it is inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2016a**

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

Morphological erosion of grayscale pixel data

The Grayscale Erosion block performs morphological erosion on a stream
of pixel intensity values. You can specify a neighborhood or structuring element of up
to 32-by-32 pixels. For line, square, or rectangle structuring elements more than 8
pixels wide, the block uses the Van Herk algorithm to find the minimum pixel value. This
algorithm uses only three comparators to find the minimum pixel values of all the rows,
then uses a comparison tree to find the minimum pixel value of the row results.

For structuring elements less than 8 pixels wide, or that contain zero elements, the
block implements a pipelined comparison tree for each row of the neighborhood. An
additional comparison tree finds the minimum pixel value of the row results. If the
structuring element contains zeros that mask off pixels, the algorithm saves hardware
resources by not implementing comparators for those pixel locations.
