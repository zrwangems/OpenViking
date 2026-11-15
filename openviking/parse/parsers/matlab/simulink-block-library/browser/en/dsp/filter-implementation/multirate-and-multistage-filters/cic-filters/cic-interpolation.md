---
type: simulink-block
title: 'CIC Interpolation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Multirate and Multistage Filters / CIC Filters'
documentation_page: 'cicinterpolation'
documentation_source_path: 'ref/cicinterpolation.html'
language: en
---

# CIC Interpolation

## Ports

### Input

### **Port\_1** — Input signal vector | matrix

Specify the data input as a vector or a matrix.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — CIC interpolated output vector | matrix

CIC interpolated output, returned as a vector or a matrix. The data type of the
output is determined by the settings in the block dialog. The complexity of the output
matches that of the input. The number of output rows is
*R*✕*Num*, where *R* is the
interpolation factor and *Num* is the number of input rows.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Coefficient source** — Source of filter information `Dialog parameters` (default) | `Filter object`

Source of the filter information, specified as one of the following:

- `Dialog parameters` — Enter information about
  the filter, such as **Interpolation factor (R)**,
  **Differential delay (M)** and **Number of sections
  (N)**, in the block dialog.
- `Filter object` — Specify the filter using a
  `dsp.CICInterpolator`
  System object™.

### **Interpolation factor (R)** — Interpolation factor `2` (default) | integer

Interpolation factor of the filter, specified as an integer greater than 1.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters`.

### **Differential Delay (M)** — Differential delay `1` (default) | positive integer

Specify the differential delay of the comb part of the filter, *M*,
as a positive integer. For more details, see CIC Interpolation Filter.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters`.

### **Number of sections (N)** — Number of filter sections `2` (default) | positive integer

Specify the number of filter sections. The number you specify determines the number
of sections in either the comb part of the filter or the integrator part of the filter.
This value does not represent the total number of sections in the comb and integrator
parts combined.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters`.

### **Data type specification mode** — Specify word length and fraction length of filter sections and output `Full precision` (default) | `Minimum section word lengths` | `Specify word lengths` | `Binary point scaling`

Choose how you specify the fixed-point word length and fraction length of the filter
sections and/or output:

- `Full precision` — The word and fraction
  lengths of the filter sections and outputs are automatically selected for you. The
  output and last section word lengths (WL) are set to:

  WL=ceil(log2((RM)NR))+I

  where,

  - *I* –– Input word length
  - *M* –– Differential delay
  - *N* –– Number of sections
  - *R* –– Interpolation factor

  The other section word lengths are set to accommodate the bit growth, as
  described in Hogenauer's paper [1]. All fraction lengths are set to the input fraction length.
- `Minimum section word lengths` — Specify the
  word length of the filter output in the **Output word length**
  parameter. The word lengths of the filter sections are set in the same way as in
  `Full precision` mode.

  The section fraction lengths are set to the input fraction length. The output
  fraction length is set to the input fraction length minus the difference between
  the last section word length and the output word length.
- `Specify word lengths` — Specify the word
  lengths of the filter sections and output in the **Section word
  lengths** and **Output word length** parameters. The
  fraction lengths of the filter sections are set such that the spread between word
  length and fraction length is the same as in full-precision mode. The output
  fraction length is set to the input fraction length minus the difference between
  the last section word length and the output word length.
- `Binary point scaling` — Specify the word and
  fraction lengths of the filter sections and output in the **Section word
  lengths**, **Section fraction lengths**,
  **Output word length**, and **Output fraction
  length** parameters.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters`.

### **Section word lengths** — Word length of filter sections [`16 16 16 16`] (default) | scalar | row vector

Word lengths of filter sections, specified as a scalar or a vector of length equal
to 2*N*, where *N* is the number of filter sections.
The section word length must be in the range [2, 128].

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters` and **Data type specification
mode** to either `Specify word lengths` or
`Binary point scaling`.

### **Section fraction lengths** — Fraction length of filter sections `0` (default) | integer

Fraction lengths of filter sections, specified as an integer.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters` and **Data type specification
mode** to `Binary point scaling`.

### **Output word length** — Word length of filter output `32` (default) | integer

Word length of the filter output, specified as an integer in the range [2,
128].

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters` and **Data type specification
mode** to any option other than `Full
precision`.

### **Output fraction length** — Fraction length of filter output `0` (default) | integer

Fraction length of the filter output, specified as an integer.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters` and **Data type specification
mode** to `Binary point scaling`.

### **Input processing** — Method of processing input `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. You can set this parameter to one of
the following options:

- `Columns as channels (frame based)` — The block
  treats each column of the input as a separate channel. In this mode, the block
  always performs single-rate processing.
- `Elements as channels (sample based)` — The
  block treats each element of the input as a separate channel. In this mode, the
  input to the block must be a scalar or a vector. You can use the **Rate
  options** parameter to specify whether the block performs single-rate or
  multirate processing.

### **Rate options** — Rate processing rule `Enforce single-rate processing` (default) | `Allow multirate processing`

Specify the rate processing rule for the block. You can select one of the following
options:

- `Enforce single-rate processing` — The block
  maintains the sample rate of the input.
- `Allow multirate processing` — The block
  produces an output with a sample rate that is *R* times faster than
  the input sample rate. To select this option, you must set the **Input
  processing** parameter to `Elements as channels (sample
  based)`.

### **Filter object** — Multirate filter object `dsp.CICInterpolator System object`

Specify the name of the multirate filter object that you want the block to
implement. You must specify the filter as a `dsp.CICInterpolator`
System object.

You can define the System object in the block dialog or in a MATLAB® workspace variable.

For information on creating System objects, see Define Basic System Objects.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Filter object`.

### **View Filter Response** — View filter response button

This button opens the Filter Visualization Tool (FVTool) from the Signal Processing Toolbox™ product and displays the filter response of the filter defined in the
block. For more information on FVTool, see the Signal Processing Toolbox documentation.

**Note**

If you specify a filter in the **Filter object** parameter, you
must apply the filter by clicking the **Apply** button before using
the **View Filter Response** button.

## Libraries

DSP System Toolbox / Filtering / Multirate Filters DSP System Toolbox HDL Support / Filtering

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `fixed point` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**Note**

For an HDL-optimized filter architecture with hardware-friendly control signals, use
the CIC Interpolator (DSP HDL Toolbox)
block. The DSP HDL Toolbox™ block simulates the latency of the HDL algorithm in Simulink®.

**HDL Architecture**

The block has `HDLDataPath` as a default architecture. This
architecture provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Block Properties**

| HDL Block Properties | Description |
| --- | --- |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **AddPipelineRegisters** | Insert a pipeline register between stages of computation in a filter. See also AddPipelineRegisters (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Enumerated | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar | Yes | Half  Single  Double | Yes | No | Yes | Yes | Yes |

**Block Parameter Configuration**

These block parameter configurations are incompatible with HDL code generation.

| Block Parameter | Limitations |
| --- | --- |
| **Rate options** | Parameter value `Enforce single-rate processing` is not supported. |
| **Input processing** | Parameter value `Columns as channels (frame based)` is not supported. |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**Limitations and Considerations**

- Vector and frame inputs are not supported for HDL code generation.

When you use **AddPipelineRegisters**, registers
are placed based on the filter structure. The pipeline register placement
determines the latency.

| Pipeline Register Placement | Latency (clock cycles) |
| --- | --- |
| A pipeline register is added between the comb stages of the differentiators. | `NS-1`, where `NS` is number of sections (at the output side). |

## Version History

**Introduced before R2006a**

## Description

Interpolate signal using cascaded integrator-comb filter

The CIC Interpolation block performs a sample rate increase (interpolation) on an input
signal by an integer factor. Cascaded integrator-comb (CIC) filters are a class of linear
phase FIR filters that consist of a comb part and an integrator part.

The CIC Interpolation block requires a Fixed-Point Designer™ license.
