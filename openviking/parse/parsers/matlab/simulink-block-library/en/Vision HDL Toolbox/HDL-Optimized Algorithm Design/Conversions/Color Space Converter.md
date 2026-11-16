---
type: simulink-block
title: 'Color Space Converter'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Algorithm Design / Conversions'
documentation_page: 'colorspaceconverter'
documentation_source_path: 'ref/colorspaceconverter.html'
language: en
---

# Color Space Converter

## Ports

### Input

### **pixel** — Input pixel stream vector | matrix

For scalar pixel streams, specify **pixel** as a
vector of 1-by-3 values. For multipixel streams, specify
**pixel** as a matrix of **Number of
pixels**-by-3 pixel intensity values. **Number of
pixels** can be two, four, or eight.

The pixel stream must be in Y'CbCr or R'G'B' color space. Integer and
fixed-point data types must be between 8 and 16 bits. The values must be
unsigned.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint8` | `uint16` | `fi(0,N,0), where N = 8,9,...,16` | `single` | `double`

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

### **pixel** — Output pixel stream in new colorspace scalar | vector | matrix

Output pixel stream in intensity, Y'CbCr, or R'G'B' color space,
returned as a single pixel stream or multipixel stream. The data type
and **Number of pixels** of the output stream is the
same as the input pixel stream. If the output is intensity values, each
pixel has one component. If the output is Y'CbCr or R'G'B', each pixel
has three components.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `fixed point`

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

### **Conversion** — Type of color space conversion `RGB to YCbCr` (default) | `YCbCr to RGB` | `RGB to intensity`

The block accepts input pixels as vectors of three values that represent a
single pixel. If you choose `RGB to intensity`,
each output pixel is a scalar. Otherwise, each output pixel is a vector of
three values.

### **Use conversion specified by** — Conversion equation `Rec. 601 (SDTV)` (default) | `Rec. 709 (HDTV)`

Conversion equation used between R'G'B' and Y'CbCr color spaces.

#### Dependencies

This parameter applies only when you set
**Conversion** to `RGB to YCbCr`
or `YCbCr to RGB`.

### **Scanning standard** — HDTV scanning standard `1250/50/2:1` (default) | `1125/60/2:1`

Scanning standard used to convert between R'G'B' and Y'CbCr color spaces
in HDTV format.

#### Dependencies

This parameter applies when you set **Use conversion specified
by** to `Rec. 709 (HDTV)`.

## Libraries

Vision HDL Toolbox / Conversions

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

**Introduced in R2015a**

### R2022a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021b: Multipixel streaming

The Color Space Converter block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel.

The block supports input matrices of *NumPixels*-by-3 values, and
output matrices of *NumPixels*-by-*NumComponents*
values, where *NumComponents* is 3 or 1. The
**ctrl** ports remain scalar, and the control signals in the
`pixelcontrol` bus apply to all pixels in the matrix.

## Description

Convert color information between color spaces

The Color Space Converter block converts between R'G'B' and Y'CbCr
color spaces, and also converts R'G'B' to intensity.

**Note**

The Color Space Converter block operates on gamma-corrected color
spaces, usually indicated with prime notation ('). However, for simplicity, the
block and mask labels do not include the prime notation.
