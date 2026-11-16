---
type: simulink-block
title: 'LDL Factorization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'ldlfactorization'
documentation_source_path: 'ref/ldlfactorization.html'
language: en
---

# LDL Factorization

## Ports

### Input

### **Port\_1** — Input signal matrix

Input signal, specified as a square matrix.

The algorithm requires that the input be square and Hermitian positive
definite. When the input is not positive definite, the block reacts as
specified by the **Non-positive definite input**
parameter.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Port\_1** — Output signal matrix

The output is a composite matrix with lower triangle elements
*lij* from
*L*, diagonal elements
*dij* from
*D* and upper triangle elements
*uij* from
*L\**, where
*L* is a lower triangular square matrix that has
unity diagonal elements, *D* is a diagonal matrix, and
*L\** is the
Hermitian (complex conjugate) transpose of *L*.

The output format is shown below for a 5-by-5 matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## Parameters

### Main Tab

### **Non-positive definite input** — Non-positive definite input action `Warning` (default) | `Ignore` | `Error`

Specify the action when nonpositive definite matrix inputs occur:

- `Ignore` — Proceed with
  the computation and do not issue an alert. The output is not
  a valid factorization. A partial factorization is present in
  the upper-left corner of the output.
- `Warning` — Display a
  warning message in the MATLAB® Command Window and continue the simulation.
  The output is not a valid factorization. A partial
  factorization is present in the upper-left corner of the
  output.
- `Error` — Display an error
  dialog box and terminate the simulation.

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

For more details, see rounding
mode.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Intermediate product** — Intermediate product data type `Inherit: Same as input` (default) | `fixdt(1,16,0)`

Specify the intermediate product data type. As shown in Fixed-Point Data Types, the
output of the multiplier is cast to the intermediate product data type
before the next element of the input is multiplied into it. You can set
the data type to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Alternatively, you can set the **Intermediate
product** data type by using the **Data Type
Assistant**. To use the assistant, click the
**Show data type assistant**
button.

For more information, see Specify Data Types Using Data Type Assistant (Simulink).

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Product output** specifies the data type of the
output of a product operation in the LDL Factorization
block.

- `Inherit: Inherit via internal rule`
  — The block inherits the product output data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- `Inherit: Same as input` — The
  block specifies the product output data type to be the same as
  the input data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type that has a word length of 16 bits and a fraction length of
  0.

For more information, see Multiplication Data Types and
Fixed-Point Data Types.

Alternatively, you can set the **Product output**
data type by using the **Data Type Assistant**. To use
the assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Accumulator** specifies the data type of the output
of an accumulation operation in the LDL Factorization
block.

- `Inherit: Inherit via internal rule`
  — The block inherits the accumulator data type based on
  an internal rule. For more information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as input` — The
  block specifies the accumulator data type to be the same as the
  input data type.
- `Inherit: Same as product output`
  — The block specifies the accumulator data type to be the
  same as the product output data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type that has a word length of 16 bits and a fraction length of
  0.

For illustrations on how to use the accumulator data type in this
block, see Fixed-Point Data Types.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Output data type `Inherit: Same as input` (default) | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the LDL Factorization block. For more information on the
output data type, see Fixed-Point Data Types.

- `Inherit: Same as input` — The
  block specifies the output data type to be the same as the input
  data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type that has a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output Minimum** — Minimum value that block can output `[]` (default) | scalar

Specify the minimum value that the block can output. Simulink software uses this minimum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value that block can output `[]` (default) | scalar

Specify the maximum value that the block can output. Simulink software uses this maximum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Factorizations

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

Factor square Hermitian positive definite matrices into lower, upper, and diagonal components

The LDL Factorization block uniquely factors the square Hermitian positive definite
input matrix S as

S=LDL\*

where *L* is a lower triangular square matrix with unity diagonal
elements, *D* is a diagonal matrix, and
*L\** is the Hermitian (complex
conjugate) transpose of *L*. Only the diagonal and lower triangle of
the input matrix are used. Any imaginary component of the diagonal entries is
disregarded.

LDL factorization requires half the computation of Gaussian elimination (LU
decomposition), and is always stable. It is more efficient than Cholesky factorization
because it avoids computing the square roots of the diagonal elements.
