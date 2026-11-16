---
type: simulink-block
title: 'Matrix 1-Norm'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'matrix1norm'
documentation_source_path: 'ref/matrix1norm.html'
language: en
---

# Matrix 1-Norm

## Ports

### Input

### **Port\_1** — Input signal vector | matrix

Input signal, specified as a vector or matrix.

The block treats length-*M* unoriented vector input
as an *M*-by-1 matrix.

The Matrix 1-Norm block supports real and complex floating-point
inputs and real fixed-point inputs.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal scalar

Matrix 1-norm or maximum column-sum of the input, returned as a
scalar. The output *y* is always a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## Parameters

### Main

There are no parameters on the **Main Tab**.

### Data Types

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as one of the following:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see Rounding
Modes.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on
numerical results when all these conditions are met:

- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.
- **Output** data type is
  `Inherit: Same as
  accumulator`.

With these data-type settings, the block operates in a
full-precision mode.

### **Saturate on integer overflow** — Overflow handling method off (default) | on

Select this parameter to saturate the result of the fixed-point
operation. Clear this parameter to wrap the result of the fixed-point
operation. For details on *saturate* and
*wrap*, see Overflow
Handling for fixed-point operations.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on numeric
results when all these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.

With these data-type settings, the block operates in a
full-precision mode.

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Accumulator** specifies the data type of the output
of an accumulation operation in the Matrix 1-Norm
block.

- `Inherit: Inherit via internal rule`
  — The block inherits the accumulator data type based on
  an internal rule. For more information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as input` — The
  block specifies the accumulator data type to be the same as the
  input data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

For illustrations on how to use the accumulator data type in this
block, see Fixed-Point Data Types.

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the Matrix 1-Norm block.

- `Inherit: Same as input` — The
  block specifies the output data type to be the same as the input
  data type.
- `Inherit: Same as accumulator`
  — The block specifies the output data type to be the same
  as the accumulator data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

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

Floating-point inheritance takes precedence over the data type settings
defined on this tab. When inputs are floating point, the block ignores these
settings and all internal data types are floating point.

## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Compute 1-norm of matrix

The Matrix 1-Norm block computes the 1-norm or maximum column-sum of an
*M*-by-*N* input matrix
*A*.

y=‖A‖1=max1≤j≤N∑i=1M|aij|

Equivalent MATLAB® code is given by:

```
y = max(sum(abs(A)))
```
