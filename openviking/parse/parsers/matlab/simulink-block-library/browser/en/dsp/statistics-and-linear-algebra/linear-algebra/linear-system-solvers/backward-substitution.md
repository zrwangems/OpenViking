---
type: simulink-block
title: 'Backward Substitution'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Linear System Solvers'
documentation_page: 'backwardsubstitution'
documentation_source_path: 'ref/backwardsubstitution.html'
language: en
---

# Backward Substitution

## Ports

### Input

### **U** — Input upper triangular matrix *M*-by-*M* matrix

Specify the input upper triangular
*M*-by-*M* matrix
*U* through this port. Inputs *U*
and *B* must have the same number of rows.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **B** — *B* matrix *M*-by-*N* matrix | *M*-by-1 vector

Specify the *B* matrix in the
*U**X* = *B*
equation as an *M*-by-*N* matrix or an
*M*-by-1 vector.

When you specify an *M*-by-1 vector, the block treats
the length-*M* vector input at port
**B** as an *M*-by-1 matrix.
Inputs *U* and *B* must have the same
number of rows.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **X** — Solution of system of equations *M*-by-*N* matrix | *M*-by-1 matrix

The block returns the output as an
*M*-by-*N* matrix or an
*M*-by-1 vector. The size of the
*X* matrix is same as the size of the
*B* matrix.

When the inputs are fixed-point, the output matrix
*X* is signed only fixed-point.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Input U is unit-upper triangular** — Diagonal elements of input matrix have a value of 1 `off` (default) | `on`

Select this check box only when all elements on the diagonal of
*U* have a value of `1`. When you
do so, the block optimizes its behavior by skipping an unnecessary
division operation.

Do not select this check box if any elements on the diagonal of
*U* do not have a value of `1`.
When you clear the **Input U is unit-upper triangular**
check box, the block always performs the division operation.

### **Diagonal of complex input U is real** — Diagonal elements of complex input are real `off` (default) | `on`

Select to optimize simulation speed when the diagonal elements of
complex input *U* are real.

**Note**

When U is a complex fixed-point signal, you must select either
**Input U is unit-upper triangular** or
**Diagonal of complex input U is real**. When
either of these options are selected, the block ignores any
imaginary part of the diagonal of *U*.

#### Dependencies

This parameter is visible only when **Input U is
unit-upper triangular** is not selected.

### Data Types Tab

**Note**

Floating-point inheritance takes precedence over the data type settings
defined on this pane. When inputs are floating point, the block ignores these
settings, and all internal data types are floating point.

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as one of the following:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see rounding
mode.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `fixdt(1,16,0)`

**Product output** specifies the data type of the
output of a product operation in the Backward
Substitution block. For more information on the product
output data type, see Fixed-Point Data Types and
Multiplication Data Types.

- `Inherit: Inherit via internal rule`
  — The block inherits the product output data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- `Inherit: Same as first input`
  — The block specifies the product output data type to be
  the same as the first input data type.
- `fixdt(1,16,0)` — The block
  specifies a signed, binary-point, scaled, fixed-point data type
  with a word length of 16 bits and a fraction length of 0.

Alternatively, you can set the **Product output**
data type by using the **Data Type Assistant**. To use
the assistant, click the **Show data type assistant**
button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as product output` | `Inherit: Same as first input` | `fixdt(1,16,0)`

**Accumulator** specifies the data type of the output
of an accumulation operation in the Backward Substitution
block. For illustrations on how to use the accumulator data type in this
block, see Fixed-Point Data Types.

- `Inherit: Inherit via internal rule`
  — The block inherits the accumulator data type based on
  an internal rule. For more information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as product output`
  — The block specifies the accumulator data type to be the
  same as the product output data type.
- `Inherit: Same as first input`
  — The block specifies the accumulator data type to be the
  same as the first input data type.
- `fixdt(1,16,0)` — The block
  specifies a signed, binary-point scaled, fixed-point data type
  with a word length of 16 bits and a fraction length of 0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button .

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Output data type `Inherit: Same as first input` (default) | `fixdt(1,16,0)`

**Output** specifies the data type of the output of
the Backward Substitution block. For more information on
the output data type, see Fixed-Point Data Types.

- `Inherit: Same as first input`
  — The block specifies the output data type to be the same
  as the first input data type.
- `fixdt(1,16,0)` — The block
  specifies a signed, binary-point scaled, fixed-point data type
  with a word length of 16 bits and a fraction length of 0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output Minimum** — Minimum value the block can output `[]` (default) | scalar

Specify the minimum value the block can output. Simulink® software uses this minimum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value block can output `[]` (default) | scalar

Specify the maximum value the block can output. Simulink software uses this maximum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Solve U X = B for X when U is upper triangular matrix

The Backward Substitution block solves the linear system
*U**X* = *B* by simple backward
substitution of variables, where:

- *U* is the upper triangular
  *M*-by-*M* matrix input to the
  **U** port.
- *B* is the *M*-by-*N*
  matrix input to the **B** port.
- *X* is the *M*-by-*N*
  output matrix and is the solution of the system of equations.

The block does not check the rank of the inputs. The block uses only the elements in
the *upper triangle* of input *U* and ignores the
lower elements. When you select the **Input U is unit-upper
triangular** check box, the block assumes the elements on the diagonal of
*U* are 1s. This is useful when matrix *U* is the
result of another operation, such as an LDL decomposition, that uses the diagonal
elements to represent the *D* matrix.
