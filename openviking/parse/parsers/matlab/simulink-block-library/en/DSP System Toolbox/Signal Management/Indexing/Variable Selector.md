---
type: simulink-block
title: 'Variable Selector'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'variableselector'
documentation_source_path: 'ref/variableselector.html'
language: en
---

# Variable Selector

## Ports

### Input

### **InN** — *N*th input signal scalar | vector | matrix

*N*th input signal, where *N* is the
number of inputs specified in the Number of input signals
parameter.

When the input is an unoriented vector, the Select
parameter is ignored and the output is an unoriented vector of length
*L* containing those elements specified by the
length-*L* indexing vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes

### **Idx** — Index vector scalar | vector

Specify a scalar value or vector containing the indices of the input
rows or columns that appear in the output matrix.

#### Dependencies

This port appears only when you set the Selector mode
to `Variable`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **OutN** — *N*th Output signal scalar | vector | matrix

*N*th output signal, corresponding to the
*N*th input signal, where *N* is
the number of inputs specified in the Number of input signals
parameter. The output is returned as a scalar, vector, or matrix as the
same type, size, and complexity as the corresponding input.

For variable and fixed indexing modes, the row selection operation is
equivalent to

```
y = u(idx,:)						% Equivalent MATLAB code
```

and the column selection operation is equivalent to

```
y = u(:,idx)						% Equivalent MATLAB code
```

where `idx` is the length-*L*
indexing vector. The row selection output size is
*L*-by-*N* and the column
selection output size is *M*-by-*L*.
Input rows or columns can appear any number of times in the output, or
not at all.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Number of input signals** — Number of inputs `1` (default) | positive integer

Specify the number of input signals as a positive integer. An input port
is created on the block for each input signal.

### **Select** — Select dimension `Rows` (default) | `Columns`

Specify the dimension of the input to select,
`Rows` or
`Columns`.

When **Select** is set to:

- `Rows` –– The block extracts rows from
  each input matrix.
- `Columns` –– The block extracts columns
  from each input matrix.

When the input is an unoriented vector, the **Select**
parameter is ignored. The output is an unoriented vector of length
*L* containing those elements specified by the
length-*L* indexing vector.

### **Selector mode** — Indexing mode `Variable` (default) | `Fixed`

Specify the type of indexing operation to perform,
`Variable` or
`Fixed`.

When **Selector mode** is set to:

- `Variable` –– The
  length-*L* vector input to the Idx
  port selects *L* rows or columns of each input to
  pass through to the output. You can update the elements of the
  indexing vector at each sample time, but the vector length must
  remain the same throughout the simulation.
- `Fixed` –– The **Idx**
  port is disabled. The length-*L* vector that you
  specified in the Elements
  parameter selects *L* rows or columns of each input
  to pass through to the output. The **Elements**
  parameter is tunable, so you can change the values of the indexing
  vector elements at any time during the simulation but the vector
  length must remain the same.

### **Elements** — Selected elements `[1 3]` (default) | scalar | vector

Specify a vector containing the indices of the input rows or columns that
appear in the output matrix.

**Tunable:** Yes

#### Dependencies

This parameter appears only when you set the Selector mode to
`Fixed`.

### **Index mode** — Index mode `Zero-based` (default) | `One-based`

When set to `One-based`, an index value of
`1` refers to the first row or column of the input.
When set to `Zero-based`, an index value of
`0` refers to the first row or column of the
input.

### **Invalid index** — Error handling `Clip Index` (default) | `Clip and Warn` | `Generate Error`

Specify how the block handles an invalid index value. You can select one
of these options:

- `Clip index` — Clip the index to
  the nearest valid value and do not issue an alert.

  For example, if the block receives a
  `64`-by-`4` input and the
  Select
  parameter is set to:

  - `Rows` –– The block clips an
    index of `72` to
    `64`.
  - `Columns` –– The block clips
    an index of `72` to
    `4`.

  In both cases, the block clips an index of
  `-2` to `1`.
- `Clip and warn` — Clip the index
  to the nearest valid value and display a warning message at the
  MATLAB® command line.
- `Generate error` — Display an
  error dialog box and terminate the simulation.

**Tunable:** Yes

### **Fill empty spaces in outputs (for logical indexing)** — Fill in empty spaces in outputs `on` (default) | `off`

When the indexing vector elements are of a Boolean data type, the block
performs logical indexing. Logical indexing can cause empty spaces in the
output. Select this parameter to designate values to be appended to the
output in the Fill values
parameter.

### **Fill values** — Fill values `0` (default) | scalar value | integer

Specify the fill values when the block performs logical indexing.

#### Dependencies

This parameter appears only when you select the Fill empty spaces in outputs (for logical indexing)
parameter.

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

Select subset of rows or columns from input

The Variable Selector block extracts a subset of rows or columns from the
*M*-by-*N* input matrix `u` at
each input port. You specify the number of input and output ports in the
**Number of input signals** parameter.

When an element of the indexing vector references a nonexistent row or column of the
input, the block implements the action that you specify by using the **Invalid
index** parameter.

When the indexing vector elements are of the Boolean data type, the block performs
logical indexing. Select **Fill empty spaces in outputs (for logical
indexing)** to access the **Fill values** parameter. These
values are appended to the output to make it as long as the input elements.

**Note**

The Variable Selector block always copies the selected input rows or columns to a
contiguous block of memory (unlike the Simulink® Selector block).
