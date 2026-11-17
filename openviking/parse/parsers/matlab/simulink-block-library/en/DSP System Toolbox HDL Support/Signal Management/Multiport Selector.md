---
type: simulink-block
title: 'Multiport Selector'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'multiportselector'
documentation_source_path: '../dsp/ref/multiportselector.html'
language: en
---

# Multiport Selector

## Ports
```yaml
ports:
- name: Input
  summary: Input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
- name: Output(s)
  summary: Row- or column-subsets of input vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
```

### Input

### **Input** — Input vector | matrix

Specify the input *u* as a vector or a matrix of size
*M*-by-*N*. The block treats an
unoriented length-*M* vector input as an
*M*-by-1 matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Output(s)** — Row- or column-subsets of input vector | matrix

Row- or column-subsets of input, propagated to each output port. Each
cell in the **Indices to output** array determines the
subset of input rows or columns to be propagated to the respective
output port. The total number of cells in the **Indices to
output** array determines the number of output ports on the
block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
## Parameters
```yaml
parameters:
- name: Select
  summary: Select input dimension Rows (default) | Columns
  group: ''
- name: Indices to output
  summary: Indices to output { 4, [1:2 5], [7; 8], 10:-1:6 } (default) | cell array
  group: ''
- name: Invalid index
  summary: Action to take for invalid index Clip Index (default) | Clip and Warn | Generate Error
  group: ''
```

### **Select** — Select input dimension `Rows` (default) | `Columns`

Select the input dimension as:

- `Rows` –– The block uses the
  one-dimensional indices you specify to select matrix rows, and
  all elements on the chosen rows are included.
- `Columns` –– The block uses the
  one-dimensional indices you specify to select matrix columns,
  and all elements on the chosen columns are included.

A given input row or column can appear any number of times in any of the
outputs, or not at all.

When an index references a nonexistent row or column of the input, the
block reacts with the action you specify using the **Invalid index** parameter.

### **Indices to output** — Indices to output `{ 4, [1:2 5], [7; 8], 10:-1:6 }` (default) | cell array

Specify the row- or column-subsets to propagate to each of the output
ports as a cell array. The *k*th cell contains a
one-dimensional indexing expression specifying the subset of input rows or
columns to be propagated to the *k*th output port. The
total number of cells in the array determines the number of output ports on
the block.

Consider the following **Indices to output** cell array.
This is a four-cell array which requires the block to generate four
independent outputs (each at a distinct port).

```
{4,[1:2 5],[7;8],10:-1:6}
```

The following table shows the dimensions of these outputs when
**Select** = `Rows` and the
input dimension is *M*-by-*N*.

| Cell | Expression | Description | Output Size |
| --- | --- | --- | --- |
| 1 | `4` | Row 4 of input | 1-by-*N* |
| 2 | `[1:2 5]` | Rows 1, 2, and 5 of input | 3-by-*N* |
| 3 | `[7;8]` | Rows 7 and 8 of input | 2-by-*N* |
| 4 | `10:-1:6` | Rows 10, 9, 8, 7, and 6 of input | 5-by-*N* |

### **Invalid index** — Action to take for invalid index `Clip Index` (default) | `Clip and Warn` | `Generate Error`

Specify the action to take when there is an invalid index value. You can
select one of the following options:

- `Clip index` — The block clips the
  index to the nearest valid value, and does not issue an
  alert.

  For example, if the block receives a
  `64`-by-`4` input and the
  **Select** parameter is set to
  `Rows`, the block clips an index of
  `72` to `64`. For the same
  input, if the **Select** parameter is set to
  `Columns`, the block clips an index of
  `72` to `4`. In both cases,
  the block clips an index of `-2` to
  `1`.
- `Clip and warn` — The block clips
  the index to the nearest valid value and displays a warning message
  at the MATLAB® command line.
- `Generate error` — The block
  displays an error dialog box and terminates the simulation.
## Libraries

DSP System Toolbox / Signal Management / Indexing DSP System Toolbox HDL Support / Signal Management

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
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

**Complex Data Support**

This block supports code generation for complex signals.

## Version History

**Introduced before R2006a**

## Description

Distribute arbitrary subsets of input rows or columns to multiple output ports

The Multiport Selector block extracts multiple subsets of rows or
columns from *M*-by-*N* input matrix
*u*, and propagates each new submatrix to a distinct output port.
For more details, see the description of the **Select** and
**Indices to output** parameters.
