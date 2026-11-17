---
type: simulink-block
title: 'Convert 1-D to 2-D'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2023b
official_category: 'Signal Management'
documentation_page: 'convert1dto2d'
documentation_source_path: '../dsp/ref/convert1dto2d.html'
language: en
---

# Convert 1-D to 2-D

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Output signal matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — Input signal vector | matrix

Input signal, specified as a 1-D vector or 2-D matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal matrix

Output signal, returned as a 2-D matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of output rows
  summary: Number of rows in output matrix 1 (default) | positive integer
  group: ''
- name: Number of output columns
  summary: Number of columns in output matrix 1 (default) | positive integer
  group: ''
- name: Frame-based output
  summary: Option to enable frame-based output off (default) | on
  group: ''
```

### **Number of output rows** — Number of rows in output matrix `1` (default) | positive integer

Number of rows *Mo* in the output matrix,
specified as a positive integer.

### **Number of output columns** — Number of columns in output matrix `1` (default) | positive integer

Number of columns *No* in the output matrix,
specified as a positive integer.

### **Frame-based output** — Option to enable frame-based output `off` (default) | `on`

Select this parameter to create a frame-based output.
## Libraries

DSP System Toolbox / Signal Management / Signal Attributes DSP System Toolbox HDL Support / Signal Management

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has a pass-through implementation.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023b: Convert 1-D to 2-D block will be removed

The Convert 1-D to 2-D block will be removed in a future release. Use the
Reshape (Simulink) block instead. When the block is
removed, existing instances of this block will be automatically replaced with the
Reshape block.

## Description

(To be removed) Reshape 1-D or 2-D input to 2-D matrix with specified dimensions

The Convert 1-D to 2-D block reshapes a
length-*Mi* 1-D vector or an
*Mi*-by-*Ni*
matrix to an
*Mo*-by-*No*
matrix, where *Mo* is specified by the
**Number of output rows** parameter and
*No* is specified by the **Number of output
columns** parameter.

```
y = reshape(u,Mo,No)					% Equivalent MATLAB code
```

The input is reshaped *column-wise*, as shown in the two cases below.
The length-6 vector and the 2-by-3 matrix are both reshaped to the same 3-by-2 output
matrix.

The Convert 1-D to 2-D block reshapes the length-6 1-D vector and 2-by-3 matrix to the 3-by-2 output matrix.

An error is generated when
(*Mo*\**No*)≠(*Mi*\**Ni*).
In other words, the total number of input elements must be conserved in the output.

The output is frame based when you select the **Frame-based output**
check box; otherwise, the output is sample based.
