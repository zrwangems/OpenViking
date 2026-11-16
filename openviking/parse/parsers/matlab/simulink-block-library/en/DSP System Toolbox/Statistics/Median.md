---
type: simulink-block
title: 'Median'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'median'
documentation_source_path: 'ref/median.html'
language: en
---

# Median

## Ports

### Input

### **Port\_1** — Data input vector | matrix | *N*-D array

The block accepts real-valued or complex-valued multichannel and
multidimensional inputs. The input data type must be double precision,
single precision, integer, or fixed point, with power-of-two slope and
zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Median value along specified dimension vector | matrix | *N*-D array

The block computes the median value in each row or column of the
input, or along vectors of a specified dimension of the input. It can
also compute the median of the entire input. Each element in the output
array `y` is the median value of the corresponding
column, row, or entire input. The output array `y`
depends on the setting of the **Find the median value
over** parameter.

Consider a three-dimensional input signal of size
*M*-by-*N*-by-*P*.
When you set **Find the median value over** to:

- `Entire input` — The output at
  each sample time is a scalar that contains the median value of
  the
  *M*-by-*N*-by-*P*
  input matrix.
- `Each row` — The output at
  each sample time consists of an
  *M*-by-1-by-*P* array,
  where each element contains the median value of each vector over
  the second dimension of the input. For an
  *M*-by-*N* matrix input,
  the output is an *M*-by-1 column vector.
- `Each column` — The output at
  each sample time consists of a
  1-by-*N*-by-*P* array,
  where each element contains the median value of each vector over
  the first dimension of the input. For an
  *M*-by-*N* matrix input,
  the output at each sample time is a 1-by-*N*
  row vector.

  In this mode, the block treats length-*M*
  unoriented vector inputs as *M*-by-1 column
  vectors.
- `Specified dimension` — The
  output at each sample time depends on the value of the
  **Dimension** parameter. If you set the
  **Dimension** to `1`, the
  output is the same as when you select `Each
  column`. If you set the
  **Dimension** to `2`, the
  output is the same as when you select `Each
  row`. If you set the
  **Dimension** to `3`, the
  output at each sample time is an
  *M*-by-*N* matrix
  containing the median value of each vector over the third
  dimension of the input.

  The data type of the output matches the data type of the
  input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Sort algorithm** — Sort method `Quick sort` (default) | `Insertion sort`

Specify the sorting algorithm as either `Quick
sort` or `Insertion
sort`.

### **Find the median value over** — Dimension over which the median is computed `Each column` (default) | `Entire input` | `Each row` | `Specified dimension`

- `Each column` — The block
  outputs the median value over each column.
- `Each row` — The block
  outputs the median value over each row.
- `Entire input` — The block
  outputs the median value over the entire input.
- `Specified dimension` —
  The block outputs the median value over the dimension
  specified in the **Dimension**
  parameter.

### **Dimension** — Custom dimension `1` (default) | scalar

Specify the dimension (one-based value) of the input signal over which
the block computes the median. The value of this parameter must be
greater than 0 and less than or equal to the number of dimensions in the
input signal.

#### Dependencies

To enable this parameter, set **Find the median value
over** to `Specified
dimension`.

### Data Types Tab

**Note**

To use these parameters, the data input must be fixed point. For all other
inputs, the parameters on the **Data Types** tab are
ignored.

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more
details, see rounding
mode.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Product output** — Product output data type `Inherit: Same as input` (default) | `fixdt([],16,0)`

Specify the data type of the output of a product operation in the
Median block. For more information, see Fixed-Point Data Types and
Multiplication Data Types.

You can set this parameter to:

- `Inherit: Same as input` — The
  product output data type is the same as the input data
  type.
- `fixdt([],16,0)` — The product
  output data type is an autosigned, binary-point, scaled,
  fixed-point data type with a word length of 16 bits and a
  fraction length of 0.

Alternatively, you can set the **Product output**
data type by using the **Data Type Assistant**. To use
the assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Accumulator** — Accumulator data type `Inherit: Same as product output` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

Specify the data type of the output of an accumulation operation in
the Median block. For more details, see Fixed-Point Data Types.

You can set this parameter to:

- `Inherit: Same as product output`
  — The accumulator data type is the same as the product
  output data type.
- `Inherit: Same as input` — The
  accumulator data type is the same as the input data type.
- `fixdt([],16,0)` — The
  accumulator data type is an autosigned, binary-point, scaled,
  fixed-point data type with a word length of 16 bits and a
  fraction length of 0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the Median block. For more details, see Fixed-Point Data Types.

You can set this parameter to:

- `Inherit: Same as accumulator`
  — The output data type is the same as the accumulator
  data type.
- `Inherit: Same as input` — The
  output data type is the same as the input data type.
- `Inherit: Same as product output`
  — The output data type is the same as the product output
  data type.
- `fixdt([],16,0)` — The output
  data type is an autosigned, binary-point, scaled, fixed-point
  data type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output Minimum** — Minimum output value `[]` (default) | scalar

Specify the minimum value that the block can output. The default value
is `[]` (unspecified). Simulink® uses this value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum output value `[]` (default) | scalar

Specify the maximum value that the block can output. The default value
is `[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types off (default) | on

Select this parameter to prevent the fixed-point tools from overriding
the data types you specify on the block.

## Libraries

DSP System Toolbox / Statistics

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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Median value of input

The Median block computes the median of each row or column of the
input, or along vectors of a specified dimension of the input. It can also compute the
median of the entire input. You can specify the dimension using the **Find the
median value over** parameter. While computing the median, the block first
sorts the input values. If the number of values is odd, the median is the middle value.
If the number of values is even, the median is the average of the two middle values. To
sort the data, you can specify the **Sort algorithm** parameter as
either `Quick sort` or `Insertion
sort`. The block sorts complex inputs according to their
magnitude.
