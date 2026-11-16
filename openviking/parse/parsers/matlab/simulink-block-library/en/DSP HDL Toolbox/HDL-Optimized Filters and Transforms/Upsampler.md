---
type: simulink-block
title: 'Upsampler'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'upsampler'
documentation_source_path: 'ref/upsampler.html'
language: en
---

# Upsampler

## Ports

### Input

### **data** — Input data scalar | column vector

Input data, specified as a scalar or a column vector with a length up to 64. The
input data must be an integer or a fixed-point value with a word length less than or
equal to 128.

The `double` and
`single` data types are supported for simulation, but not for HDL
code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — Valid input data indicator `0` | `1`

Control signal that indicates whether the input data is valid. When this value is
`1`, the block accepts the values on the **data**
input port. When this value is `0`, the block ignores the values on
the **data** input port.

**Data Types:** `Boolean`

### **reset** — Option to clear internal states `0` | `1`

Control signal that clears the internal states. When this value is
`1`, the block stops the current calculation and clears its
internal states. When this value is `0` and
**valid** is `1`, the block captures data for
processing.

For more reset considerations, see the Reset Signal section on the
Hardware Control Signals page.

#### Dependencies

To enable this port, on the **Control Ports** tab, select the
**Enable reset input port** parameter.

**Data Types:** `Boolean`
### Output

### **data** — Upsampled data scalar | column vector

Upsampled data, returned as a scalar or a column vector with a length up to 1 to
128.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — Valid output data indicator `0` | `1`

Control signal that indicates whether data from the **data**
output port is valid. When this value is `1`, the block returns valid
data on the **data** output port. When this value is
`0`, the values on the **data** output port are
not valid.

**Data Types:** `Boolean`

### **ready** — Block ready indicator `0` | `1`

Control signal that indicates whether the block is ready for new input data on the
next cycle. When this value is `1`, you can specify the **data** and **valid**  inputs for
the next time step. When this value is `0`, the block ignores any
input data in the next time step.

#### Dependencies

To enable this port, on the **Control Ports** tab, select the
**Enable ready output port** parameter.

**Data Types:** `Boolean`

## Parameters

### Main

### **Upsample factor (L)** — Upsampling factor `3` (default) | integer in the range [1, 2.^16]

Specify the upsampling factor by which the block increases the input sampling
rate.

### **Sample offset (0 to L-1)** — Sample offset `0` (default) | integer in the range [0, 2.^16 – 1]

Specify the sample offset as an integer in the range [0, **Upsample factor
(L)** – 1].

### **Minimum number of cycles between valid input samples** — Minimum number of cycles between valid input samples `1` (default) | factor or multiple of **Upsample factor (L)** | integer in the range [1, Inf]

Specify the minimum number of cycles between the valid input samples as a factor
or multiple of **Upsample factor (L)** or an integer in the range [1,
Inf] based on the type of input and output data.

| Input Data | Output Data | Minimum Number of Cycles Between Valid Input Samples |
| --- | --- | --- |
| Scalar | Scalar | Greater than or equal to **Upsample factor (L)** |
| Scalar | Vector | Factor of **Upsample factor (L)** |
| Vector | Vector | Integer in the range [1, Inf] |

### Control Ports

### **Enable reset input port** — Option to enable reset input port `off` (default) | `on`

Select this parameter to enable the **reset** input port. The
reset signal implements a local synchronous reset of the data path registers.

For more reset considerations, see Tips.

### **Enable ready output port** — Option to enable ready output port off (default) | on

Select this parameter to enable the **ready** output port. This
port indicates whether the block is ready for new input data.

## Libraries

DSP HDL Toolbox / Signal Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

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

## Version History

**Introduced in R2022b**

## Description

Upsample by adding zeros between input samples

The Upsampler block upsamples an input signal by adding
*L*–1 zeros between input samples, where *L* is the
upsampling factor. The block supports these combinations of input and output data.­­­

- Scalar input and scalar output
- Scalar input and vector output
- Vector input and vector output

The block provides an architecture suitable for HDL code generation and hardware
deployment.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
