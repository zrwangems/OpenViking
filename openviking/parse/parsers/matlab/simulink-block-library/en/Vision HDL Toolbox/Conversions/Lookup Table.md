---
type: simulink-block
title: 'Lookup Table'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'lookuptable'
documentation_source_path: 'ref/lookuptable.html'
language: en
---

# Lookup Table

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar | vector
  direction: input
  data_types: uint8 | uint16 | fixdt(0,N,F), N <= 16 | Boolean
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: pixel
  summary: Output pixel stream scalar | vector
  direction: output
  data_types: uint8 | uint16 | int8 | int16 | fixed point | Boolean | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: output
  data_types: bus
```

### Input

### **pixel** — Input pixel stream scalar | vector

For single pixel streaming, specify **pixel** as a
scalar intensity value or a row vector of **Number of
components** values. For multipixel streaming, specify
**pixel** as a column vector of **Number of
pixels** pixel intensity values. **Number of
pixels** can be two, four, or eight. This block does not
support multipixel-multicomponent streaming.

Integer and fixed-point data types larger than 16 bits are not
supported. Signed data types are not supported.

**Data Types:** `uint8` | `uint16` | `fixdt(0,N,F), N <= 16` | `Boolean`

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

The dimensions of the output **pixel** match the
dimensions of the input **pixel**. The block returns
the output **pixel** as a scalar, a row vector of
**Number of components** values, or a column vector
of **Number of pixels** values.

The data type is specified by the **Table data**
parameter.

**Data Types:** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `Boolean` | `double` | `single`

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
- name: Table data
  summary: Map between input pixel and output pixel uint8(0:1:255) (default) | vector
  group: ''
```

### **Table data** — Map between input pixel and output pixel `uint8(0:1:255)` (default) | vector

Map between input pixel and output pixel, specified as a row or column
vector of any data type. The data type of the table data determines the data
type of the output **pixel**. This mapping determines the
one-to-one correspondence between an input **pixel** value
and an output **pixel** value.

- The length of the vector must be
  2*WordLength*,
  where *WordLength* is the size, in bits, of the
  input **pixel**. The Lookup Table
  block does not perform interpolation. Every input value must have a
  corresponding output value in the table.
- The smallest representable value of the input data type maps to
  the first element of the table, the second smallest value maps to
  the second element, and so on. For example, if the input
  **pixel** has a data type of
  `fixdt(0,3,1)`, the input value 0 maps to the
  first element of the table, 0.5 maps to the second element, 1 maps
  to the third element, and so on.

When the input **pixel** is a vector, the block
replicates the lookup table for each element of the vector. In that case,
the tables use
*VectorSize*×2*WordLength*
memory locations.

Since R2025a, the software supports `single`
data type for simulation and HDL code generation. To enable HDL code generation for
`single` data types in your model, open the **HDL
Coder** app, go to the **Floating Point** pane, and
select the **Use Floating Point** checkbox.
`double` data type is supported only for simulation, not for HDL code
generation.

**Example:** `uint8(linspace(255,0,256))`

**Data Types:** `uint8` | `uint16` | `int8` | `int16` | `fixed point` | `Boolean` | `double` | `single`
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

### R2025a: `single` data type supported for HDL code generation

The block now supports HDL code generation with `single` data
type for the **Table data** values.

### R2023a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2020b: Multipixel streaming

The Lookup Table block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel. You cannot use multicomponent
and multipixel together.

For multipixel streaming, the blocks support input and output column vectors of 4
or 8 pixels. The **ctrl** port remains scalar, and the control
signals in the `pixelcontrol` bus apply to all pixels in the
vector.

## Description

Map input pixel to output pixel using custom rule

The Lookup Table block provides a custom one-to-one map between an
input pixel value and an output pixel value.
