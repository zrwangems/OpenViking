---
type: simulink-block
title: 'Gamma Corrector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Algorithm Design / Conversions'
documentation_page: 'gammacorrector'
documentation_source_path: 'ref/gammacorrector.html'
language: en
---

# Gamma Corrector

## Ports

### Input

### **pixel** — Input pixel stream scalar | vector

For single pixel streams, specify **pixel** as a
scalar intensity value. For multipixel streams, specify
**pixel** as a vector of **Number of
pixels**-by-1 pixel intensity values. **Number of
pixels** can be two, four, or eight. Integer and
fixed-point data types larger than 16 bits are not supported.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `double` | `single`

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

Image pixel, returned as a scalar value or vector of values. The data
type and dimension of the output **pixel** stream match
those of the input **pixel** stream.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `double` | `single`

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

### **Operation** — Direction of pixel value adjustment `Gamma` (default) | `De-gamma`

Direction of pixel value adjustment, specified as one of these options:

- `Gamma` — Apply gamma
  correction.
- `De-gamma` — Remove gamma
  correction.

### **Gamma** — Target gamma value `2.2` (default) | scalar greater than or equal to 1

Target gamma value, specified as a scalar greater than or equal to
1.

- When you set **Operation** to
  `Gamma`, **Gamma** is
  the target gamma value of the output video stream.
- When you set **Operation** to
  `De-gamma`, **Gamma**
  is the gamma value of the input video stream.

### **Linear segment** — Include a linear segment in the gamma curve on (default) | off

Option to include a linear segment in the gamma curve. When you select
this check box, the gamma curve has a linear portion near the origin.

### **Break point** — Point where gamma curve and linear segment meet `0.018` (default) | scalar between 0 and 1

Pixel value that corresponds to the point where the gamma curve and linear
segment meet, specified as a scalar value between 0 and 1, exclusive.

#### Dependencies

This parameter applies only when you select the **Linear
segment** check box.

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
| **LUTRegisterResetType** | The reset type of the lookup table output register. Select `none` to synthesize the lookup table to a ROM when your target is an FPGA. See also LUTRegisterResetType (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2015a**

### R2022b: Multipixel streaming

The block now supports multipixel streams. The HDL implementation replicates the
algorithm for each pixel in parallel.

For multipixel streaming, the block supports input and output column vectors of 2,
4, or 8 pixels. The **ctrl** port remains scalar, and the control
signals in the `pixelcontrol` bus apply to all pixels in the
vector.

## Description

Apply or remove gamma correction of pixel stream

Gamma Corrector applies or removes gamma correction on a stream of
pixels. Gamma correction adjusts linear pixel values so that the modified values fit a
curve. The de-gamma operation performs the opposite operation to obtain linear pixel
values.
