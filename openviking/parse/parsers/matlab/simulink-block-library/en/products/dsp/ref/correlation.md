---
type: simulink-block
title: 'Correlation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Measurements and Statistics / Stationary Statistics'
documentation_page: 'correlation'
documentation_source_path: 'ref/correlation.html'
language: en
---

# Correlation

## Ports

### Input

### **Port\_1** — First data input signal vector | matrix | *N*-D array

The block accepts real-valued or complex-valued multichannel and
multidimensional inputs. The input can be a fixed-point signal when you
set the **Computation domain** to
`Time`. When one or both of the input
signals are complex, the output signal is also complex.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Port\_2** — Second data input signal vector | matrix | *N*-D array

The block accepts real-valued or complex-valued multichannel and
multidimensional inputs. The input can be a fixed-point signal when you
set the **Computation domain** to
`Time`. When one or both of the input
signals are complex, the output signal is also complex.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Cross-correlated output vector | matrix | *N*-D array

Cross-correlated output of the two input signals.

When the inputs are *N*-D arrays, the object outputs
an *N*-D array, where all the dimensions, except for
the first dimension, match with the input array. For example,

- When the inputs *u* and
  *v* have dimensions
  *Mu*-by-*N*-by-*P*
  and
  *Mv*-by-*N*-by-*P*,
  respectively, the Correlation block outputs
  an (*Mu* +
  *Mv* –
  1)-by-*N*-by-*P*
  array.
- When the inputs *u* and
  *v* have the dimensions
  *Mu*-by-*N*
  and
  *Mv*-by-*N*,
  the block outputs an
  (*Mu* +
  *Mv* –
  1)-by-*N* matrix.

If one input is a column vector and the other input is an
*N*-D array, the Correlation block
computes the cross-correlation of the vector with each column in the
*N*-D array. For example,

- When the input *u* is an
  *Mu*-by-1
  column vector and *v* is an
  *Mv*-by-*N*
  matrix, the block outputs an
  (*Mu* +
  *Mv* –
  1)-by-*N* matrix.
- Similarly, when *u* and
  *v* are column vectors with lengths
  *Mu* and
  *Mv*,
  respectively, the block performs the vector
  cross-correlation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Computation domain** — Domain in which the block computes the cross-correlation `Time` (default) | `Frequency` | `Fastest`

- `Time` — Computes the
  cross-correlation in the time domain, which minimizes the
  memory usage.
- `Frequency` — Computes the
  cross-correlation in the frequency domain. For more
  information, see Algorithms.
- `Fastest` — Computes the
  cross-correlation in the domain that minimizes the number of
  computations.

To cross-correlate fixed-point signals, set this parameter to
`Time`.

### Data Types Tab

**Note**

Fixed-point signals are supported for the time domain only. To use these
parameters, on the **Main** tab, set **Computation
domain** to `Time`.

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

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on
numerical results when all these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.
- **Output** data type is
  `Inherit: Same as
  accumulator`.

With these data type settings, the block operates in
full-precision mode.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

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

With these data type settings, the block operates in
full-precision mode.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Product output** specifies the data type of the
output of a product operation in the Correlation block.
For more information on the product output data type, see Multiplication Data Types and
Fixed-Point Data Types.

- `Inherit: Inherit via internal rule`
  — The block inherits the product output data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- `Inherit: Same as input` — The
  block specifies the product output data type to be the same as
  the input data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Product output**
data type by using the **Data Type Assistant**. To use
the assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Accumulator** specifies the data type of output of
an accumulation operation in the Correlation block. For
illustrations on how to use the accumulator data type in this block, see
Fixed-Point Data Types.

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
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the Correlation block. For more information on the output
data type, see Fixed-Point Data Types.

- `Inherit: Same as input` — The
  block specifies the output data type to be the same as the input
  data type.
- `Inherit: Same as product output`
  — The block specifies the output data type to be the same
  as the product output data type.
- `Inherit: Same as accumulator`
  — The block specifies the output data type to be the same
  as the accumulator data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output Minimum** — Minimum value block can output `[]` (default) | scalar

Specify the minimum value the block can output. Simulink® software uses this minimum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value the block can output `[]` (default) | scalar

Specify the maximum value the block can output. Simulink software uses this maximum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Statistics

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

Cross-correlation of two inputs

The Correlation block computes the cross-correlation of two
*N*-D input arrays along the first-dimension. The computation can
be done in the time domain or frequency domain. You can specify the domain through the
**Computation domain** parameter. In the time domain, the block
convolves the first input signal, *u*, with the time-reversed complex
conjugate of the second input signal, *v*. In the frequency domain, to
compute the cross-correlation, the block:

1. Takes the Fourier transform of both input signals, *U*
   and *V*.
2. Multiplies *U* and
   *V*\*, where \* denotes the
   complex conjugate.
3. Computes the inverse Fourier transform of the product.

If you set **Computation domain** to
`Fastest`, the block chooses the domain that minimizes the
number of computations. For information on these computation methods, see Algorithms.
