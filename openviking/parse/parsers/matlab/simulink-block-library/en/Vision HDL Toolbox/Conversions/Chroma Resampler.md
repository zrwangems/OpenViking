---
type: simulink-block
title: 'Chroma Resampler'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'chromaresampler'
documentation_source_path: 'ref/chromaresampler.html'
language: en
---

# Chroma Resampler

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream in Y'CbCr color space vector | matrix
  direction: input
  data_types: uint8 | uint16 | fi(0,N,0) , where N = 8,9,...,16 | single | double
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: pixel
  summary: Output pixel stream in Y'CbCr color space vector | matrix
  direction: output
  data_types: single | double | uint8 | uint16 | fixed point
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: output
  data_types: bus
```

### Input

### **pixel** — Input pixel stream in Y'CbCr color space vector | matrix

For scalar pixel streams, specify **pixel** as a
vector of 1-by-3 values. For multipixel streams, specify
**pixel** as a matrix of **Number of
pixels**-by-3 pixel intensity values. **Number of
pixels** can be two, four, or eight.

The pixel stream must be in Y'CbCr color space. Integer and
fixed-point data types must be between 8 and 16 bits. The values must be
unsigned.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint8` | `uint16` | `fi(0,N,0) , where N = 8,9,...,16` | `single` | `double`

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

### **pixel** — Output pixel stream in Y'CbCr color space vector | matrix

Output pixel stream in Y'CbCr color space, returned as a single pixel
stream or multipixel stream. The data type and **Number of
pixels** of the output stream is the same as the input
pixel stream.

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
```yaml
parameters:
- name: Resampling
  summary: Type of resampling 4:4:4 to 4:2:2 (default) | 4:2:2 to 4:4:4
  group: Main
- name: Antialiasing filter
  summary: Lowpass filter to follow downsample operation Auto (default) | Property | None
  group: Main
- name: Horizontal filter coefficients
  summary: Coefficients for the antialiasing filter [0.2 0.6 0.2] (default) | vector
  group: Main
- name: Interpolation
  summary: Interpolation method for an upsample operation Linear (default) | Pixel replication
  group: Main
- name: Rounding mode
  summary: Rounding method for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round
    | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow action for internal fixed-point calculations off (default) | on
  group: Data Types
- name: Filter coefficients
  summary: Data type for antialiasing filter coefficients fixdt(1,16,15) (default) | data type expression
  group: Data Types
```

### Main

### **Resampling** — Type of resampling `4:4:4 to 4:2:2` (default) | `4:2:2 to 4:4:4`

If you select `4:4:4 to 4:2:2`, the block
performs a downsampling operation. If you select `4:2:2 to
4:4:4`, the block performs an upsampling
operation.

### **Antialiasing filter** — Lowpass filter to follow downsample operation `Auto` (default) | `Property` | `None`

If you select `Auto`, the block uses a
built-in lowpass filter. If you select
`Property`, the **Horizontal filter
coefficients** parameter appears on the dialog box. If you
select `None`, the block does not filter the
input signal.

#### Dependencies

This parameter is visible when you set
**Resampling** to `4:4:4 to
4:2:2`.

### **Horizontal filter coefficients** — Coefficients for the antialiasing filter `[0.2 0.6 0.2]` (default) | vector

Coefficients for the antialiasing filter, specified as a
vector.

#### Dependencies

This parameter is visible if you set
**Resampling** to `4:4:4 to
4:2:2` and **Antialiasing filter**
to `Property`.

### **Interpolation** — Interpolation method for an upsample operation `Linear` (default) | `Pixel replication`

If you select `Linear`, the block uses linear
interpolation to calculate the missing values. If you select
`Pixel replication`, the block repeats the
chrominance values of the preceding pixel to create the missing pixel.

#### Dependencies

This parameter is visible if you set
**Resampling** to `4:2:2 to
4:4:4`.

### Data Types

The parameters on this tab appear only when they are relevant. If you configure
the block so that no filter coefficients are needed, or no rounding or overflow is
possible, the irrelevant parameter is hidden.

### **Rounding mode** — Rounding method for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Specify a rounding method for internal fixed-point calculations.

### **Saturate on integer overflow** — Overflow action for internal fixed-point calculations `off` (default) | `on`

When you clear this parameter, fixed-point and integer values wrap around to zero when
the value overflows what is representable with that data type. When you select this
parameter, the value saturates at the maximum representable value.

### **Filter coefficients** — Data type for antialiasing filter coefficients `fixdt(1,16,15)` (default) | data type expression

This parameter applies when you set **Antialiasing
filter** to `Auto` or
`Property`.
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

## Version History

**Introduced in R2015a**

### R2025a: Multipixel-multicomponent streaming

The Chroma Resampler block now supports multipixel-multicomponent streams. The block
accepts and returns matrices of *NumPixels*-by-3 values. The
**ctrl** ports remain scalar, and the control signals in the
`pixelcontrol` bus apply to all pixels in the matrix. The HDL
implementation replicates the algorithm for each pixel in parallel.

## Description

Downsample or upsample chrominance component

The Chroma Resampler block downsamples or upsamples a pixel stream.

- Downsampling reduces bandwidth and storage requirements in a video system
  by combining pixel chrominance components over multiple pixels. You can
  specify a filter to prevent aliasing by selecting the default filter or by
  entering coefficients.
- Upsampling restores a signal to its original rate. To calculate the extra
  sample, you can use interpolation or replication.

The block accepts luma and chrominance components. The block does not modify the luma
component, and applies delay to align it with the resampled chrominance outputs. The
rate of the output luma component is the same as the rate of the input.
