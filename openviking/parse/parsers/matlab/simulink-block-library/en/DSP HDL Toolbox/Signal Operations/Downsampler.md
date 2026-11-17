---
type: simulink-block
title: 'Downsampler'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'downsampler'
documentation_source_path: 'ref/downsampler.html'
language: en
---

# Downsampler

## Ports
```yaml
ports:
- name: data
  summary: Input data scalar | column vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: valid
  summary: Valid input data indicator 0 | 1
  direction: input
  data_types: Boolean
- name: reset
  summary: Option to clear internal states 0 | 1
  direction: input
  data_types: Boolean
- name: data
  summary: Downsampled data scalar | column vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: valid
  summary: Valid output data indicator 0 | 1
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data scalar | column vector

Input data, specified as a scalar or a column vector with a length up to 64. The
input data must be an integer or a fixed point with a word length less than or equal
to 128. The **Downsample factor (K)** parameter must be an integer
multiple of the input frame size.

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

### **data** — Downsampled data scalar | column vector

Downsampled data, returned as a scalar or a column vector with a length up to 1 to
64.

For a vector input, if the vector size is less than or equal to
**Downsample factor (K)**, the block outputs scalar output.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — Valid output data indicator `0` | `1`

Control signal that indicates whether data from the **data**
output port is valid. When this value is `1`, the block returns valid
data on the **data** output port. When this value is
`0`, the values on the **data** output port are
not valid.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Downsample factor (K)
  summary: Downsampling factor 2 (default) | integer in the range [1, 2.^16]
  group: Main
- name: Sample offset (0 to K-1)
  summary: Sample offset 0 (default) | integer in the range [0, 2.^16 – 1]
  group: Main
- name: Enable reset input port
  summary: Option to enable reset input port off (default) | on
  group: Control Ports
```

### Main

### **Downsample factor (K)** — Downsampling factor `2` (default) | integer in the range [1, 2.^16]

Specify the downsampling factor at which the block decreases the input sample
rate.

### **Sample offset (0 to K-1)** — Sample offset `0` (default) | integer in the range [0, 2.^16 – 1]

Specify the sample offset in the range [0, **Downsample factor
(K)** – 1].

### Control Ports

### **Enable reset input port** — Option to enable reset input port `off` (default) | `on`

Select this parameter to enable the **reset** input port. The
reset signal implements a local synchronous reset of the data path registers.

For more reset considerations, see Tips.
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

Downsample by removing data samples between input samples

The Downsampler block downsamples an input signal by removing
*K*–1 data samples between input samples. The block supports these
combinations of input and output data.

- Scalar input and scalar output
- Vector input and scalar output
- Vector input and vector output

The block provides an architecture suitable for HDL code generation and hardware
deployment.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
