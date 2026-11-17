---
type: simulink-block
title: 'CIC Decimation'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'cicdecimation'
documentation_source_path: 'ref/cicdecimation.html'
language: en
---

# CIC Decimation

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal vector | matrix
  direction: input
  data_types: int8 | int16 | int32 | int64 | fixed point
- name: Port_1
  summary: CIC decimated output vector | matrix
  direction: output
  data_types: int8 | int16 | int32 | int64 | fixed point
```

### Input

### **Port\_1** — Input signal vector | matrix

Data input, specified as a vector or matrix. The number of input rows must be a
multiple of the decimation factor.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — CIC decimated output vector | matrix

CIC decimated output, returned as a vector or a matrix. The data type of the
output is determined by the settings in the block dialog. The complexity of the output
matches that of the input. The number of output rows is
(1/*R*)✕*Num*, where *R* is the
decimation factor and *Num* is the number of input rows.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Coefficient source
  summary: Source of the filter information Dialog parameters (default) | Filter object
  group: ''
- name: Decimation factor (R)
  summary: Decimation factor 2 (default) | integer
  group: ''
- name: Differential Delay (M)
  summary: Differential delay 1 (default) | positive integer
  group: ''
- name: Number of sections (N)
  summary: Number of filter sections 2 (default) | positive integer
  group: ''
- name: Data type specification mode
  summary: Specify word length and fraction length of filter sections and output Full precision (default) | Minimum section
    word lengths | Specify word lengths | Binary point scaling
  group: ''
- name: Section word lengths
  summary: Word length of filter sections [16 16 16 16] (default) | scalar | row vector
  group: ''
- name: Section fraction lengths
  summary: Fraction lengths of filter sections 0 (default) | integer
  group: ''
- name: Output word length
  summary: Word length of filter output 32 (default) | integer
  group: ''
- name: Output fraction length
  summary: Fraction length of filter output 0 (default) | integer
  group: ''
- name: Rate options
  summary: Rate processing rule Enforce single-rate processing (default) | Allow multirate processing
  group: ''
- name: Filter object
  summary: Multirate filter object dsp.CICDecimator
  group: ''
- name: View Filter Response
  summary: View filter response gui button
  group: ''
```

### **Coefficient source** — Source of the filter information `Dialog parameters` (default) | `Filter object`

Source of the filter information, specified as one of the following:

- `Dialog parameters` — Enter information about
  the filter, such as **Decimation factor (R)**,
  **Differential delay (M)** and **Number of sections
  (N)**, in the block dialog.
- `Filter object` — Specify the filter using a
  `dsp.CICDecimator`
  System object™.

Different items appear on the CIC Decimation block dialog depending
on whether you select `Dialog parameters` or
`Filter object` in the **Coefficient
source** parameter.

### **Decimation factor (R)** — Decimation factor `2` (default) | integer

Decimation factor of the filter, specified as an integer greater than 1.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Dialog parameters`.

### **Differential Delay (M)** — Differential delay `1` (default) | positive integer

Specify the differential delay of the comb part of the filter, *M*,
as a positive integer. For more details, see CIC Decimation Filter.

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
  lengths of the filter sections and outputs are automatically selected for you. All
  word lengths (WL) are set to:

  WL=ceil(N×log2(M×R))+I

  where,

  - *I* –– Input word length
  - *M* –– Differential delay
  - *N* –– Number of sections
  - *R* –– Decimation factor

  All fraction lengths are set to the input fraction length.
- `Minimum section word lengths` — Specify the
  word length of the filter output in the **Output word length**
  parameter. The block automatically selects the word lengths of the filter sections
  and all fraction lengths such that each of the section word lengths is as small as
  possible. The precision of each filter section is less than in `Full
  precision` mode, but the range of each section is preserved.
- `Specify word lengths` — Specify the word
  lengths of the filter sections and output in the **Section word
  lengths** and **Output word length** parameters. The
  block automatically selects fraction lengths for the filter sections and output
  such that the range of each section is preserved when the least significant bits
  are discarded.
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

### **Section fraction lengths** — Fraction lengths of filter sections `0` (default) | integer

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

### **Rate options** — Rate processing rule `Enforce single-rate processing` (default) | `Allow multirate processing`

Specify the rate processing rule for the block:

- `Enforce single-rate processing` — The block
  performs frame-based processing and produces an output that has the same sample rate
  as the input. To decimate the signal while maintaining the input sample rate, the
  block decreases the output frame size. In this mode, the input column size must be a
  multiple of **Decimation Factor (R)**.
- `Allow multirate processing` — In this mode, the
  block produces an output with a sample rate that is `R` times
  slower than the input sample rate.

### **Filter object** — Multirate filter object `dsp.CICDecimator`

Specify the name of the multirate filter object that you want the block to
implement. You must specify the filter as a `dsp.CICDecimator`
System object.

You can define the System object in the block dialog or in a MATLAB® workspace variable.

For information on creating System objects, see Define Basic System Objects.

#### Dependencies

This parameter appears when you set **Coefficient source** to
`Filter object`.

### **View Filter Response** — View filter response `gui button`

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
the CIC Decimator (DSP HDL Toolbox)
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

Decimate signal using cascaded integrator-comb filter

The CIC Decimation block performs a sample rate decrease (decimation) on an input signal
by an integer factor. Cascaded Integrator-Comb (CIC) filters are a class of linear phase FIR
filters comprised of a comb part and an integrator part.

The block supports real and complex fixed-point inputs. In its normal mode of operation,
the CIC Decimation block allows the adder’s numeric values to overflow and wrap around [1]
[3]. The Fixed-Point infrastructure then causes overflow warnings to appear on the command
line. This overflow is of no consequence.

The CIC Decimation block requires a Fixed-Point Designer™ license.
