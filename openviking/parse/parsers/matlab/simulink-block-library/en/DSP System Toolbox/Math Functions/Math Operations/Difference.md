---
type: simulink-block
title: 'Difference'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'difference'
documentation_source_path: 'ref/difference.html'
language: en
---

# Difference

## Ports

### Input

### **Port\_1** — Input signal vector | matrix | *N*-D array

Input signal, specified as a vector, matrix, or an *N*-D
array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal vector | matrix | *N*-D array

The difference between adjacent rows, columns, or a specified dimension of the
input, returned as a vector, matrix, or an *N*-D array.

The output is the same data type and complexity as the input, but the dimension
that the difference was calculated on is one less. The length of the other dimensions
is unchanged.

For more details on how the output is computed, see the Difference along parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Running difference** — Running difference `No` (default) | `Yes`

Specify whether the block computes a running difference.

- `No` –– The block computes the difference between
  adjacent elements in the specified dimension of the current input. In this mode,
  the block can compute the difference along the columns, rows, or a specified
  dimension of the input depending on the Difference along parameter.
- `Yes` –– The block computes the running difference
  along the columns of the input. See Running Operation
  for more information.

### **Difference along** — Difference dimension `Columns` (default) | `Rows` | `Specified dimension`

Specify whether the block computes the difference along the columns, rows, or a
specified dimension of the input.

- `Columns` –– The block computes differences between
  adjacent elements in each column of the input. Equivalent MATLAB® code is given by:

  ```
  y = diff(u)
  ```

  For *M*-by-*N* inputs, the output is an
  (*M* – 1)-by-*N* matrix whose
  *j*th column has these elements:

  yi,j=ui+1,j−ui,j     1≤i≤(M−1)
- `Rows` –– The block computes differences between
  adjacent elements in each row of the input. Equivalent MATLAB code is given by:

  ```
  y = diff(u,[],2)
  ```

  The output is an *M*-by-(*N*-1) matrix whose
  *i*th row has the following elements:

  yi,j=ui,j+1−ui,j     1≤j≤(N−1)
- `Specified dimension` –– The behavior of the block is
  an extension of the row-wise differencing described earlier. The block computes
  differences between adjacent elements along the dimension you specify in the
  **Dimension** parameter. Equivalent MATLAB code is given by:

  ```
  y = diff(u,[],d)
  ```

  where *d* is the dimension.

  The output is an array whose length in the specified dimension is one less
  than that of the input, and whose lengths in other dimensions are unchanged. For
  example, consider an
  *M*-by-*N*-by-*P*-by-*R*
  input array with elements *u(i,j,k,l)* and assume that the value
  of the **Dimension** parameter is `3`. The
  output of the block is an
  *M*-by-*N*-by-(*P*–1)-by-*R*
  array with the following elements:

  yi,j,k,l=ui,j,k+1,l−ui,j,k,l     1≤k≤(P−1)

### **Dimension** — One-based dimension `1` (default) | `2` | `3`

Specify the one-based dimension along which to compute element-to-element
differences.

#### Dependencies

To enable this parameter, select `Specified dimension`
for the **Difference along** parameter.

### Data Types Tab

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as one of the following:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see Rounding Modes.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its fixed-point
operation. When you clear this parameter, the block wraps the result of its
fixed-point operation. For details on `saturate` and
`wrap`, see overflow mode for
fixed-point operations.

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Accumulator** specifies the data type of the output of an
accumulation operation in the Difference block.

- `Inherit: Inherit via internal rule` — The
  block inherits the accumulator data type based on an internal rule. For more
  information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as input` — The block specifies
  the accumulator data type to be the same as the input data type.
- `fixdt([],16,0)` — The block specifies an
  autosigned, binary-point, scaled, fixed-point data type with a word length of 16
  bits and a fraction length of 0.

Alternatively, you can set the **Accumulator** data type by using
the **Data Type Assistant**. To use the assistant, click the
**Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

For illustrations on how to use the accumulator data type in this block, see Fixed-Point Data Types.

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Output** specifies the data type of the output of the
Difference block.

- `Inherit: Same as input` — The block specifies
  the output data type to be the same as the input data type.
- `Inherit: Same as accumulator` — The block
  specifies the output data type to be the same as the accumulator data type.
- `fixdt([],16,0)` — The block specifies an
  autosigned, binary-point, scaled, fixed-point data type with a word length of 16
  bits and a fraction length of 0.

Alternatively, you can set the **Output** data type by using the
**Data Type Assistant**. To use the assistant, click the
**Show data type assistant**
button.

For more information, see Control Data Types of Signals (Simulink).

For more information on the output data type, see Fixed-Point Data Types.

### **Output Minimum** — Minimum value that block can output `[]` (default) | scalar

Specify the minimum value the block can output. Simulink uses this minimum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value that block can output `[]` (default) | scalar

Specify the maximum value the block can output. Simulink uses this maximum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

**Note**

Floating-point inheritance takes precedence over the data type settings defined on
this pane. When inputs are floating point, the block ignores these settings, and all
internal data types are floating point.

## Libraries

DSP System Toolbox / Math Functions / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Compute element-to-element difference along specified dimension of input

The Difference block computes the difference between adjacent elements in
rows, columns, or a specified dimension of the input array *u*. You can
configure the block to compute the difference only within the current input, or across
consecutive inputs (running difference).
