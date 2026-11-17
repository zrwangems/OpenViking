---
type: simulink-block
title: 'Levinson-Durbin'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'levinsondurbin'
documentation_source_path: 'ref/levinsondurbin.html'
language: en
---

# Levinson-Durbin

## Ports
```yaml
ports:
- name: Input
  summary: Input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: A
  summary: Model coefficients vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: K
  summary: Reflection coefficients vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: P
  summary: Output prediction error power vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### Input

### **Input** — Input vector | matrix

Specify the input to the block, `r =``[r(1)
r(2) ...
r(n+1)]` as a
vector or a matrix. If the input is a matrix, the block treats each
column as an independent channel and solves it separately. Each channel
of the input contains lags *0* through
*n* of an autocorrelation sequence, which appear in
the matrix *R*.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **A** — Model coefficients vector | matrix

Model coefficients *A*, returned as a vector or a
matrix. *A* has the same dimension as the input.

For each channel, port **A** outputs
`A =` `[1
a(2) a(3) ...
a(n+1)]`, the
solution to the Levinson-Durbin equation. You can also view the elements
of each output channel as the coefficients of an
*n*th-order autoregressive (AR) process.

#### Dependencies

To enable this port, set **Output(s)** to
`A and K` or
`A`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **K** — Reflection coefficients vector | matrix

Reflection coefficients *K*, returned as a vector or
a matrix. *K* has the same dimension as the input, less
one element.

For each channel, port **K** outputs
`K =``[k(1)
k(2) ...
k(n)]`, which
contains *n* reflection coefficients.

A scalar input channel causes an error when you select
`K`. You can use reflection coefficients to realize
a lattice representation of the AR process. For more details, see Applications.

#### Dependencies

To enable this port, set **Output(s)** to
`A and K` or
`K`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **P** — Output prediction error power vector

Output prediction error power *P*, returned as vector
of length equal to the number of input channels. Each element in the
vector is the prediction error power for each channel.

For each channel, *P* represents the power of the
output of an FIR filter with taps *A* and input
autocorrelation described by *r*, where
*A* represents a prediction error filter and
*r* is the input to the block. In this case,
*A* is a whitening filter. *P* has
one element per input channel.

#### Dependencies

To enable this port, select the **Output prediction error
power (P)** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
## Parameters
```yaml
parameters:
- name: Output(s)
  summary: Output(s) K (default) | A and K | A
  group: Main Tab
- name: Output prediction error power (P)
  summary: Output prediction error power off (default) | on
  group: Main Tab
- name: If the value of lag 0 is zero, A=[1 zeros], K=[zeros], P=0
  summary: If the value of lag 0 is zero, A=[1 zeros], K=[zeros], P=0 on (default) | off
  group: Main Tab
- name: Rounding mode
  summary: Rounding mode Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Saturate on integer overflow off (default) | on
  group: Data Types Tab
- name: Product output
  summary: 'Product output Inherit: Same as input (default) | numeric type'
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator Inherit: Same as input (default) | Inherit: Same as product output | numeric type'
  group: Data Types Tab
- name: Polynomial coefficients (A)
  summary: Polynomial coefficients data type fixdt(1,16,0) (default) | numeric type
  group: Data Types Tab
- name: Reflection coefficients (K)
  summary: Reflection coefficients data type fixdt(1,16,0) (default) | numeric type
  group: Data Types Tab
- name: Prediction error power (P)
  summary: 'Prediction error power data type Inherit: Same as input (default) | numeric type'
  group: Data Types Tab
- name: Minimum
  summary: Minimum values of polynomial coefficients, reflection coefficients, or prediction error power [] (default) | scalar
  group: Data Types Tab
- name: Maximum
  summary: Maximum values of polynomial coefficients, reflection coefficients, or prediction error power [] (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Output(s)** — Output(s) `K` (default) | `A and K` | `A`

Specify the solution representation of
*R**a* = *b* to output:

- Polynomial coefficients (`A`) –– For each
  channel, port **A** outputs
  `A =``[1 a(2)
  a(3) ...
  a(n+1)]`,
  the solution to the Levinson-Durbin equation.
  *A* has the same dimension as the
  input. You can also view the elements of each output channel
  as the coefficients of an *n*th-order
  autoregressive (AR) process.
- Reflection coefficients (`K`) –– For each
  channel, port **K** outputs
  `K =``[k(1)
  k(2) ...
  k(n)]`,
  which contains *n* reflection coefficients
  and has the same dimension as the input, less one element. A
  scalar input channel causes an error when you select
  `K`. You can use reflection
  coefficients to realize a lattice representation of the AR
  process described later in this page.
- Both model coefficients and reflection coefficients
  (`A and K`) –– The block outputs both
  representations at their respective ports. A scalar input
  channel causes an error when you select `A and
  K`.

When the input is a scalar or row vector, you must set this parameter
to `A`.

### **Output prediction error power (P)** — Output prediction error power `off` (default) | `on`

Select this parameter to output the prediction error power for each
channel at port **P**.

### **If the value of lag 0 is zero, A=[1 zeros], K=[zeros], P=0** — If the value of lag 0 is zero, A=[1 zeros], K=[zeros], P=0 `on` (default) | `off`

When you select this check box and the first element of the input,
`r(1)`, is zero, the block outputs the following
vectors, as appropriate:

- `A = [1 zeros(1,n)]`
- `K = [zeros(1,n)]`
- `P = 0`

When you clear this check box, the block outputs a vector of `NaN`s for each channel
whose `r`(1) element is zero. In general, an input with
*r*(1) = `0` is invalid because it
does not construct a positive-definite matrix *R*.
Often, however, blocks receive zero-valued inputs at the start of a
simulation. The check box allows you to avoid propagating
`NaN`s during this period.

### Data Types Tab

**Note**

Floating-point inheritance takes precedence over the data type settings
defined on this pane. When inputs are floating point, the block ignores these
settings, and all internal data types are floating point.

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

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

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Product output** — Product output `Inherit: Same as input` (default) | numeric type

Specify the product output data type as `Inherit: Same as
input` or a numeric type. See Fixed-Point Data Types and Multiplication Data Types for illustrations depicting the
use of the product output data type in this block. You can set it
to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Accumulator** — Accumulator `Inherit: Same as input` (default) | `Inherit: Same as product output` | numeric type

Specify the accumulator data type as `Inherit: Same as
input`, `Inherit: Same as product
output`, or a numeric type. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this
block. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- A rule that inherits a data type, for example,
  `Inherit: Same as product
  output`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Polynomial coefficients (A)** — Polynomial coefficients data type `fixdt(1,16,0)` (default) | numeric type

Specify the polynomial coefficients (*A*) data type
as a numeric type. See Fixed-Point Data Types for
illustrations depicting the use of the A data type in this block. You
can set it to an expression that evaluates to a valid data type, for
example, `fixdt(1,16,10)`.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **A**
parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Reflection coefficients (K)** — Reflection coefficients data type `fixdt(1,16,0)` (default) | numeric type

Specify the reflection coefficients (*K*) data type
as a numeric type. See Fixed-Point Data Types for
illustrations depicting the use of the K data type in this block. You
can set it to an expression that evaluates to a valid data type, for
example, `fixdt(1,16,10)`.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **K**
parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Prediction error power (P)** — Prediction error power data type `Inherit: Same as input` (default) | numeric type

Specify the prediction error power (*P*) data type as
`Inherit: Same as input` or a numeric type.
See Fixed-Point Data Types for
illustrations depicting the use of the P data type in this block. You
can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **P**
parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Minimum** — Minimum values of polynomial coefficients, reflection coefficients, or prediction error power `[]` (default) | scalar

Specify the minimum values that the polynomial coefficients,
reflection coefficients, or prediction error power should have. The
default value is `[]` (unspecified). Simulink® uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink))
- Automatic scaling of fixed-point data types

### **Maximum** — Maximum values of polynomial coefficients, reflection coefficients, or prediction error power `[]` (default) | scalar

Specify the maximum values that the polynomial coefficients,
reflection coefficients, or prediction error power should have. The
default value is `[]` (unspecified). Simulink uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink))
- Automatic scaling of fixed-point data types

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.
## Libraries

DSP System Toolbox / Estimation / Linear Prediction / Linear System Solvers DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

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

## Version History

**Introduced before R2006a**

## Description

Solve linear system of equations using Levinson-Durbin recursion

The Levinson-Durbin block solves the *n*th-order
system of linear equations

*Ra* = *b*

in the cases where:

- *R* is a Hermitian, positive-definite, Toeplitz
  matrix.
- *b* is identical to the first column of *R*
  shifted by one element and with the opposite sign.

[r(1)r\*(2)⋯r\*(n)r(2)r(1)⋯r\*(n−1)⋮⋮⋱⋮r(n)r(n−1)⋯r(1)] [a(2)a(3)⋮a(n+1)]=[−r(2)−r(3)⋮−r(n+1)]
