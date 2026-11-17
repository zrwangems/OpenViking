---
type: simulink-block
title: 'Vector Quantizer Encoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'vectorquantizerencoder'
documentation_source_path: 'ref/vectorquantizerencoder.html'
language: en
---

# Vector Quantizer Encoder

## Ports
```yaml
ports:
- name: U
  summary: Input data values vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: C
  summary: Codebook values vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: W
  summary: Weighting factor vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: I
  summary: Index values scalar | row vector
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Q(U)
  summary: Output codeword vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: D
  summary: Quantization error scalar | row vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### Input

### **U** — Input data values vector | matrix

Specify the input data values as a vector or a matrix.

The data, codebook values, and weighting factor inputs must have the same data type
whenever they are present.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **C** — Codebook values vector | matrix

Specify the codebook values as a
*k*-by-*N* matrix, where *k* ≥ 1 and *N* ≥ 1. Each input column vector is compared to this
codebook. Each column of the codebook matrix is a codeword, and each
codeword has an index value. The first codeword vector corresponds to an
index value of 0, the second codeword vector corresponds to an index
value of 1, and so on.

The input data, codebook values, and weighting factor must be of the
same data type.

If the codebook values are fixed-point, they must be signed values only.

#### Dependencies

To enable this port, set the **Source of
codebook** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **W** — Weighting factor vector

Use the **Weighting factor** parameter to emphasize
or deemphasize certain input values when calculating the distortion
measure. For more information, see **Weighting
factor**.

The input data, codebook values, and weighting factor must be of the
same data type.

If the weighting factor is fixed-point, it must be signed values only.

#### Dependencies

To enable this port, set the **Distortion measure** parameter to
`Weighted squared error` and the
**Source of weighting factor** parameter to
`Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **I** — Index values scalar | row vector

Index values of the nearest codeword based on Euclidean or weighted
Euclidean distance measure, returned as a scalar or a row vector.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Q(U)** — Output codeword vector | matrix

Output codeword, returned as a vector or a matrix.

The block assigns the data type of the output codewords based on the data type of the
input data. If the output codeword is fixed-point, it must be signed
values only.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **D** — Quantization error scalar | row vector

Quantization error, returned as a scalar or a row vector.

The block assigns the data type of the quantization error based on the data type of the
input data. If the quantization error is fixed-point, it must be signed
values only.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
## Parameters
```yaml
parameters:
- name: Source of codebook
  summary: Source of codebook Specify via dialog (default) | Input port
  group: Main Tab
- name: Codebook
  summary: Codebook values [1.5 13.3 136.4 6.8 ; 2.5 14.3 137.4 7.8; 3.5 15.3 138.4 8.8] (default)
  group: Main Tab
- name: Distortion measure
  summary: Measure of distortion Squared error (default) | Weighted squared error
  group: Main Tab
- name: Source of weighting factor
  summary: Source of weighting factor Specify via dialog (default) | Input port
  group: Main Tab
- name: Weighting factor
  summary: Weighting factor [1 1 1] (default) | vector
  group: Main Tab
- name: Tie-breaking rule
  summary: Tie-breaking rule Choose the lower index (default) | Choose the higher index
  group: Main Tab
- name: Output codeword
  summary: Output codeword off (default) | on
  group: Main Tab
- name: Output quantization error
  summary: Output quantization error off (default) | on
  group: Main Tab
- name: Index output data type
  summary: Index output data type int32 (default) | int8 | uint8 | int16 | uint16 | uint32 | Inherit via back propagation
  group: Main Tab
- name: Rounding mode
  summary: Rounding mode Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Saturate on integer overflow off (default) | on
  group: Data Types Tab
- name: Product output
  summary: Product output data type Same as input (default) | Binary point scaling
  group: Data Types Tab
- name: Word length
  summary: Product output word length 16 (default) | positive integer in range [2,128]
  group: Data Types Tab
- name: Fraction length
  summary: Product output fraction length 15 (default) | integer
  group: Data Types Tab
- name: Accumulator
  summary: Accumulator data type Same as product output (default) | Same as input | Binary point scaling
  group: Data Types Tab
- name: Word length
  summary: Accumulator word length 16 (default) | positive integer in range [2,128]
  group: Data Types Tab
- name: Fraction length
  summary: Accumulator fraction length 15 (default) | integer
  group: Data Types Tab
```

### Main Tab

### **Source of codebook** — Source of codebook `Specify via dialog` (default) | `Input port`

Specify the source of codebook as one of these options:

- `Specify via dialog` –– Specify
  codebook values in the **Codebook**
  parameter.
- `Input port` –– Specify codebook
  values through the input port **C**.

### **Codebook** — Codebook values `[1.5 13.3 136.4 6.8 ; 2.5 14.3 137.4 7.8; 3.5 15.3 138.4 8.8]` (default)

Specify the codebook values as a
*k*-by-*N* matrix, where *k* ≥ 1 and *N* ≥ 1. Each input column vector is compared to this
codebook. Each column of the codebook matrix is a codeword, and each
codeword has an index value. The first codeword vector corresponds to an
index value of 0, the second codeword vector corresponds to an index
value of 1, and so on. The codeword vectors must have the same number of
rows as the input, **U**.

#### Dependencies

To enable this parameter, set the **Source of
codebook** parameter to `Specify via
dialog`.

### **Distortion measure** — Measure of distortion `Squared error` (default) | `Weighted squared error`

Specify the measure of distortion as one of these:

- `Squared error` –– Block
  calculates the distortion by evaluating the Euclidean
  distance between the input column vector and each codeword
  in the codebook.
- `Weighted squared error` –– Block
  calculates the distortion by evaluating a weighted Euclidean
  distance using a weighting factor to emphasize or
  deemphasize certain input values.

### **Source of weighting factor** — Source of weighting factor `Specify via dialog` (default) | `Input port`

Specify the source of weighting factor as one of these options:

- `Specify via dialog` –– Specify
  the weighting factor in the **Weighting
  factor** parameter of the block dialog
  box.
- `Input port` –– Specify the
  weighting factor through the input port
  **W**.

#### Dependencies

To enable this parameter, set the **Distortion
measure** parameter to `Weighted squared
error`.

### **Weighting factor** — Weighting factor `[1 1 1]` (default) | vector

Specify weighting factor as a vector of values. The length of this vector must equal the
number of rows of the input, **U**.

Use the **Weighting factor** parameter to emphasize
or deemphasize certain input values when calculating the distortion
measure. For example, consider the *p*-th input column
vector, Up=[u1pu2p...ukp]′. When you want to neglect the effect of the first
element of this vector, enter `[0 1 1 ... 1]` as the
**Weighting factor** parameter. This weighting
factor is used to calculate the weighted squared error using the
equation:

D=∑j=1kwj(aji−ujp)2

Because of the weighting factor used in this example,
the weighted squared error is not affected by the first element of the
input matrix. Therefore, the first element of the input column vector no
longer impacts the choice of index value output by the Vector
Quantizer Encoder block.

#### Dependencies

To enable this parameter, set the **Source of weighting
factor** parameter to `Specify via
dialog`.

### **Tie-breaking rule** — Tie-breaking rule `Choose the lower index` (default) | `Choose the higher index`

Set this parameter to determine the behavior of the block when an
input column vector is equidistant from two codewords. When you want the
input column vector to be represented by the lower index valued
codeword, select `Choose the lower index`. To
represent the input column vector by the higher index valued codeword,
select `Choose the higher index`.

### **Output codeword** — Output codeword `off` (default) | `on`

Select the **Output codeword** check box to output at
port **Q(U)** the codeword vectors that correspond to
each index value. When the input is a matrix, the corresponding codeword
vectors are horizontally concatenated into a matrix.

### **Output quantization error** — Output quantization error `off` (default) | `on`

Select the **Output quantization error** check box to
output at port **D** the quantization error that
results when the block represents the input column vector by its nearest
codeword. When the input is a matrix, the quantization error values are
horizontally concatenated.

### **Index output data type** — Index output data type `int32` (default) | `int8` | `uint8` | `int16` | `uint16` | `uint32` | `Inherit via back propagation`

Specify the data type of the index output from the block at port
**I** as one of the following:

- `int8`
- `uint8`
- `int16`
- `uint16`
- `int32`
- `uint32`

To inherit the index output data type, select `Inherit via
back propagation`.

### Data Types Tab

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
the result of its fixed-point operation. For details, see overflow
mode for fixed-point operations.

### **Product output** — Product output data type `Same as input` (default) | `Binary point scaling`

As depicted above, the output of the multiplier is placed into the
product output data type and scaling. Use this parameter to specify how
you would like to designate this product output word and fraction lengths.

- When you select `Same as input`,
  these characteristics match those of the input to the
  block.
- When you select `Binary point
  scaling`, you can enter the word length and
  the fraction length of the product output in bits.

### **Word length** — Product output word length `16` (default) | positive integer in range [2,128]

Specify the product output word length as a positive integer in the
range [2,128].

#### Dependencies

To enable this parameter, set the **Product
output** parameter to `Binary point
scaling`.

### **Fraction length** — Product output fraction length `15` (default) | integer

Specify the product output fraction length as an integer.

#### Dependencies

To enable this parameter, set the **Product
output** parameter to `Binary point
scaling`.

### **Accumulator** — Accumulator data type `Same as product output` (default) | `Same as input` | `Binary point scaling`

As depicted in this diagram, inputs to the accumulator are cast to the accumulator data
type. The output of the adder remains in the accumulator data type as
each element of the input is added to it. Use this parameter to specify
how you would like to designate the accumulator word and fraction lengths.

- When you select `Same as product
  output`, these characteristics match those
  of the product output.
- When you select `Same as input`,
  these characteristics match those of the input to the
  block.
- When you select `Binary point
  scaling`, you can enter the word length and
  the fraction length of the accumulator in bits.

### **Word length** — Accumulator word length `16` (default) | positive integer in range [2,128]

Specify the accumulator word length as a positive integer in the range
[2,128].

#### Dependencies

To enable this parameter, set the **Accumulator**
parameter to `Binary point scaling`.

### **Fraction length** — Accumulator fraction length `15` (default) | integer

Specify the accumulator fraction length as an integer.

#### Dependencies

To enable this parameter, set the **Accumulator**
parameter to `Binary point scaling`.
## Libraries

DSP System Toolbox / Quantizers

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

Index of nearest codeword based on Euclidean or weighted Euclidean distance measure

The Vector Quantizer Encoder block compares each input column vector to
the codeword vectors in the codebook matrix. Each column of this codebook matrix is a
codeword. The block finds the codeword vector nearest to the input column vector and
returns its zero-based index. This block supports real floating-point and fixed-point
signals on all input ports.

The Vector Quantizer Encoder block accepts real floating-point and
fixed-point inputs. For more information, see the **Ports**
section.
