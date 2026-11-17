---
type: simulink-block
title: 'IDCT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'idct'
documentation_source_path: 'ref/idct.html'
language: en
---

# IDCT

## Ports
```yaml
ports:
- name: Input 1
  summary: Input signal vector | matrix | *N*-D array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point | bus
- name: Output 1
  summary: IDCT output vector | matrix | *N*-D array
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point | bus
```

### Input

### **Input 1** — Input signal vector | matrix | *N*-D array

Specify the input signal as a vector, matrix, or an
*N*-D array.

For all *N*-D input arrays, the block computes the IDCT across the
first dimension. The size of the first dimension (frame size) must be a
power of two. To work with other frame sizes, use the Pad block to pad or truncate
the frame size to a power-of-two length.

When the input is an *M*-by-*N* matrix, the block
treats each input column as an independent channel containing
*M* consecutive samples.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point` | `bus`
**Complex Number Support:** Yes
### Output

### **Output 1** — IDCT output vector | matrix | *N*-D array

The block outputs the IDCT of the input signal as a vector, matrix, or
an *N*-D array.

When the block outputs an *M*-by-*N*
matrix, the *l*th column
contains the length-*M* IDCT of the corresponding input
column.

y(m,l)=∑k=1Mw(k)u(k,l)cosπ(2m−1)(k−1)2M,m=1,...,M

where

w(k)={1M2M,,k=12≤k≤M

When the input is fixed-point (signed and unsigned), the output is
signed fixed-point.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point` | `bus`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Sine and cosine computation
  summary: Sine and cosine computation Table lookup (default) | Trigonometric fcn
  group: Main Tab
- name: Rounding mode
  summary: Rounding mode Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Saturate on integer overflow off (default) | on
  group: Data Types Tab
- name: Sine table
  summary: 'Sine table Inherit: Same word length as input (default) | fixdt(1,16)'
  group: Data Types Tab
- name: Product output
  summary: 'Product output Inherit: Inherit via internal rule (default) | Inherit: Same as input | fixdt(1,16,0)'
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator Inherit: Inherit via internal rule (default) | Inherit: Same as input | Inherit: Same as product output
    | fixdt(1,16,0)'
  group: Data Types Tab
- name: Output
  summary: 'Output data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | fixdt(1,16,0)'
  group: Data Types Tab
- name: Output Minimum
  summary: Output minimum [] (default) | scalar
  group: Data Types Tab
- name: Output Maximum
  summary: Output Maximum [] (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Sine and cosine computation** — Sine and cosine computation `Table lookup` (default) | `Trigonometric fcn`

Set the block to compute sines and cosines by either looking up sine and cosine values
in a speed-optimized table (`Table lookup`), or
by making sine and cosine function calls (`Trigonometric
fcn`).

To compute sines and cosines, set the parameter to one of these values:

- `Table lookup` –– The block
  computes and stores the trigonometric values before the
  simulation starts, and retrieves them during the simulation.
  When you generate code from the block, the processor running
  the generated code stores the trigonometric values computed
  by the block in a speed-optimized table, and retrieves the
  values during code execution.

  The block runs much more quickly, but requires extra
  memory for storing the precomputed trigonometric
  values.
- `Trigonometric fcn` –– The block
  computes sine and cosine values during the simulation. When
  you generate code from the block, the processor running the
  generated code computes the sine and cosine values while the
  code runs.

  The block runs more slowly, but does not need extra data
  memory. For code generation, the block requires a support
  library to emulate the trigonometric functions, increasing
  the size of the generated code.

### Data Types Tab

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode for fixed-point operations. The sine table values do not
obey this parameter; they always round to
`Nearest`.

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

**Note**

The **Rounding mode** and **Saturate on integer
overflow** parameters have no effect on numeric results
when these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.

With these data type settings, the block operates in
full-precision mode.

### **Sine table** — Sine table `Inherit: Same word length as input` (default) | `fixdt(1,16)`

Choose how you specify the word length of the values of the sine
table. The fraction length of the sine table values always equals the
word length minus one. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Same word length as
  input`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16)`

The sine table values do not obey the **Rounding mode** and
**Saturate on integer overflow** parameters. The
block always saturates and rounds off the sine table values to
`Nearest`.

### **Product output** — Product output `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

Specify the product output data type. See Fixed-Point Data Types and Multiplication Data Types for
illustrations depicting the use of the product output data type in this
block. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Accumulator** — Accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the accumulator data type. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this
block. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Output** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

Specify the output data type. See Fixed-Point Data Types for
illustrations depicting the use of the output data type in this block.
You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`.

  When you select `Inherit: Inherit via internal
  rule`, the block calculates the output word
  length and fraction length automatically. The internal rule
  first calculates an ideal output word length and fraction length
  using the following equations:

  WLideal output=WLinput+floor(log2(DCT length−1))+1

  FLideal output=FLinput

  Using these ideal results, the internal rule then selects word
  lengths and fraction lengths that are appropriate for your
  hardware. For more information, see Inherit via Internal Rule.
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Output** parameter.

See Control Data Types of Signals (Simulink) for more
information.

### **Output Minimum** — Output minimum `[]` (default) | scalar

Specify the minimum value that the block should output. The default
value is `[]` (unspecified). Simulink® software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Output Maximum** — Output Maximum `[]` (default) | scalar

Specify the maximum value that the block should output. The default
value is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.
## Libraries

DSP System Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `bus` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

To comply with the embedded systems coding standards, generated code is
non-recursive.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Inverse discrete cosine transform (IDCT) of input

The IDCT block computes the inverse discrete cosine transform (IDCT) of the
input signal *u*. When the input is an
*M*-by-*N* matrix, the block computes the IDCT of
each channel in the matrix.

Here is the equivalent MATLAB® code.

```
y = idct(u)
```
