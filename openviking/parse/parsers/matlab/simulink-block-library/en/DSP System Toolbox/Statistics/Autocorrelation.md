---
type: simulink-block
title: 'Autocorrelation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'autocorrelation'
documentation_source_path: 'ref/autocorrelation.html'
language: en
---

# Autocorrelation

## Ports
```yaml
ports:
- name: Port_1
  summary: Data input vector | matrix | *N*-D array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Autocorrelated output vector | matrix | *N*-D array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Data input vector | matrix | *N*-D array

Data input. The block accepts real-valued or complex-valued
multichannel and multidimensional inputs. The input can be a fixed-point
signal when you set the **Computation domain** to
`Time`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Autocorrelated output vector | matrix | *N*-D array

Autocorrelated output of the data input.

- When the input is an
  *M*-by-*N* matrix,
  *u*, the output, *y*,
  is an (*l*+1)-by-*N*
  matrix. *l* is the maximum positive lag for
  autocorrelation.
- When the input is an *N*-D array, the
  block outputs an *N*-D array. The size of
  the first dimension is *l*+1, and the sizes
  of all other dimensions match those of the input array. For
  example, when the input is an
  *M*-by-*N*-by-*P*
  array, the block outputs an
  (*l*+1)-by-*N*-by-*P*
  array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Compute all non-negative lags
  summary: Compute autocorrelation over all nonnegative lags on (default) | off
  group: Main Tab
- name: Maximum non-negative lag (less than input length)
  summary: Maximum positive lag 1 (default) | integer greater than or equal to 0 and less than input length
  group: Main Tab
- name: Scaling
  summary: Scaling of the output None (default) | Biased | Unbiased | Unity at zero-lag
  group: Main Tab
- name: Computation domain
  summary: Domain in which the block computes the autocorrelation Time (default) | Frequency
  group: Main Tab
- name: Rounding mode
  summary: Method of rounding operation Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types Tab
- name: Product output
  summary: 'Product output data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | fixdt([],16,0)'
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | Inherit: Same as
    product output | fixdt([],16,0)'
  group: Data Types Tab
- name: Output
  summary: 'Output data type Inherit: Same as accumulator (default) | Inherit: Same as input | Inherit: Same as product output
    | fixdt([],16,0)'
  group: Data Types Tab
- name: Output Minimum
  summary: Minimum value the block can output [] (default) | scalar
  group: Data Types Tab
- name: Output Maximum
  summary: Maximum value block can output [] (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Compute all non-negative lags** — Compute autocorrelation over all nonnegative lags on (default) | off

When you select this parameter, the Autocorrelation
block computes the autocorrelation over all nonnegative lags in the
range [0, `length(input)` – 1]. When you clear this
parameter, the block computes the autocorrelation using the lags in the
range [0, *l*], where *l* is the value
you specify in **Maximum non-negative lag (less than input
length)**.

### **Maximum non-negative lag (less than input length)** — Maximum positive lag `1` (default) | integer greater than or equal to 0 and less than input length

Maximum positive lag for autocorrelation, specified as an integer that
is greater than or equal to 0 and less than the input length.

#### Dependencies

To enable this parameter, clear the **Compute all
non-negative lags** parameter.

### **Scaling** — Scaling of the output `None` (default) | `Biased` | `Unbiased` | `Unity at zero-lag`

Scaling applied to the output.

- `None` — Generates the raw
  autocorrelation *yi,j*
  without normalization.
- `Biased` — Generates the
  biased estimate of the autocorrelation.

  yi,jbiased=yi,jM
- `Unbiased` — Generates the
  unbiased estimate of the autocorrelation.

  yi,junbiased=yi,jM−i
- `Unity at zero-lag` —
  Normalizes the estimate of the autocorrelation for each channel
  so that the zero-lag sum, the first element in each column, is
  identically 1.

  y0,j=1

### **Computation domain** — Domain in which the block computes the autocorrelation `Time` (default) | `Frequency`

- `Time` — Computes the
  convolutions in the time domain, which minimizes the memory
  usage.
- `Frequency` — Computes the
  autocorrelation in frequency domain. For more information,
  see Algorithms.

To autocorrelate fixed-point signals, set this parameter to
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
output of a product operation in the Autocorrelation
block. For more information on the product output data type, see Multiplication Data Types and
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
the assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Accumulator** specifies the data type of the output
of an accumulation operation in the Autocorrelation
block. For illustrations on how to use the accumulator data type in this
block, see Fixed-Point Data Types.

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
assistant, click the **Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the Autocorrelation block. For more information on the
output data type, see Fixed-Point Data Types.

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
assistant, click the **Show data type assistant** button.

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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Autocorrelation of N -D array

The Autocorrelation block computes the autocorrelation along the first
dimension of an *N*-D input array. The computation can be done in the
time domain or frequency domain. You can specify the domain through the
**Computation domain** parameter. In the time domain, the input
signal is convolved with its time-reversed complex conjugate. In the frequency domain,
the block computes the autocorrelation by taking the Fourier transform of the input
signal, multiplying the Fourier transform with its conjugate, and computing the inverse
Fourier transform of the product. In this domain, depending on the input length, the
block can require fewer computations. For information on these two computation methods,
see Algorithms.

You can specify the maximum lag for autocorrelation using the **Compute all
non-negative lags** and **Maximum non-negative lag (less than input
length)** parameters.

The block accepts fixed-point signals when you set the **Computation
domain** to `Time`.
