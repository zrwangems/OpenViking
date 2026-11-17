---
type: simulink-block
title: 'Inherit Complexity'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'inheritcomplexity'
documentation_source_path: '../dsp/ref/inheritcomplexity.html'
language: en
---

# Inherit Complexity

## Ports
```yaml
ports:
- name: Data
  summary: Data input scalar | vector | *N*-D array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Ref
  summary: Reference input scalar | vector | *N*-D array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Output
  summary: Output scalar | vector | *N*-D array
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### Input

### **Data** — Data input scalar | vector | *N*-D array

Specify the data input as a scalar, vector, or an
*N*-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Ref** — Reference input scalar | vector | *N*-D array

Specify the reference input as a scalar, vector, or an
*N*-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Output scalar | vector | *N*-D array

Output of the Inherit Complexity block, returned as a
scalar, vector, or an *N*-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

DSP System Toolbox / Signal Management / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized
logic.

The Inherit Complexity block supports HDL code generation for these input types:

- Input complexities, such as real or complex, at the data and reference
  port
- Vector, matrix, and bus inputs

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Limitations**

The block has these HDL code generation limitations:

- Half-precision data type is not supported.
- Non-virtual bus input is not supported.

## Version History

**Introduced before R2006a**

## Description

Change complexity of input to match reference signal

The Inherit Complexity block copies data at the **Data**
input port with the complexity of the reference signal at the **Ref**
port. When the data input is real and the reference input is complex, the block appends
a zero-valued imaginary component, `0i`, to each element of the data at
the **Data** input port.

When the data input is complex and the reference input is real, the block outputs the real
component of the data input.

When both the data input and reference input are real or when both the data input and
reference input are complex, the block propagates the data input with no changes.
