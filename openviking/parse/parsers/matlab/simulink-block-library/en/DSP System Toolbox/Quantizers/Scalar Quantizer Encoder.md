---
type: simulink-block
title: 'Scalar Quantizer Encoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'scalarquantizerencoder'
documentation_source_path: 'ref/scalarquantizerencoder.html'
language: en
---

# Scalar Quantizer Encoder

## Ports
```yaml
ports:
- name: U
  summary: Input data values vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: B
  summary: Boundary points vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: C
  summary: Codebook values vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: I
  summary: Index values vector | matrix
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Q(U)
  summary: Quantized output values vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Err
  summary: Quantization error vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: S
  summary: Clipping status vector | matrix
  direction: output
  data_types: Boolean
```

### Input

### **U** — Input data values vector | matrix

Specify the input data values as a vector or a matrix.

The input data, boundary points, codebook values, quantized output
values, and the quantization error must have the same data type whenever
they are present.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **B** — Boundary points vector

Specify the boundary points as a vector of length
*N*. You must enter the boundary points in ascending
order.

The input data, boundary points, codebook values, quantized output
values, and the quantization error must have the same data type whenever
they are present.

#### Dependencies

To enable this port, select `Input port`
from the **Source of quantizer parameters**
list.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **C** — Codebook values vector

Enter a vector of quantized output values that correspond to each
index value. The length of the codebook vector must be
*N*−1, where *N* is the length of
the boundary points vector.

The input data, boundary points, codebook values, quantized output
values, and the quantization error must have the same data type whenever
they are present.

#### Dependencies

To enable this port, select `Input port`
from the **Source of quantizer parameters** list
and you select either the **Output codeword** or
**Output quantization error** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **I** — Index values vector | matrix

Index values, returned as a vector or a matrix of the same size as the
input data.

The data type of this port depends on the setting of the
**Index output data type** parameter.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Q(U)** — Quantized output values vector | matrix

Quantized output values, returned as a vector or a matrix of the same
size as the input data. These are the codeword values that correspond to
each index value.

The input data, boundary points, codebook values, quantized output
values, and the quantization error must have the same data type whenever
they are present.

#### Dependencies

To enable this port, select the **Output
codeword** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Err** — Quantization error vector | matrix

Quantization error, returned as a vector or a matrix of the same size
as the input data. The quantization error is the difference between the
input value and the quantized output value.

The input data, boundary points, codebook values, quantized output
values, and the quantization error must have the same data type whenever
they are present.

#### Dependencies

To enable this port, select the **Output quantization
error** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **S** — Clipping status vector | matrix

Clipping status values, returned as a vector or a matrix of boolean
values of the same size as the input data. Any time an input value is
outside the range defined by the **Boundary points**
parameter, the block outputs a 1 at the **S** port.
When the value is inside the range, the blocks outputs a 0.

#### Dependencies

To enable this port, select the **Output clipping
status** check box.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Source of quantizer parameters
  summary: Source of quantizer parameters Specify via dialog (default) | Input port
  group: Main Tab
- name: Partitioning
  summary: Partitioning method Bounded (default) | Unbounded
  group: Main Tab
- name: Boundary points
  summary: Boundary points [1:10] (default) | vector
  group: Main Tab
- name: Searching method
  summary: Searching method Linear (default) | Binary
  group: Main Tab
- name: Tie-breaking rule
  summary: Action when input value is same as boundary point Choose the lower index (default) | Choose the higher index
  group: Main Tab
- name: Output codeword
  summary: Output codeword off (default) | on
  group: Main Tab
- name: Output quantization error
  summary: Output quantization error off (default) | on
  group: Main Tab
- name: Codebook
  summary: Quantized output values [1.5:9.5] (default) | vector
  group: Main Tab
- name: Output clipping status
  summary: Output clipping status off (default) | on
  group: Main Tab
- name: Action for out of range input
  summary: Action for out of range input Clip | Clip and warn | Error
  group: Main Tab
- name: Index output data type
  summary: Index output data type int32 (default) | int8 | uint8 | int16 | uint16 | int32 | uint32 | Inherit via back propagation
  group: Main Tab
- name: Rounding mode
  summary: Rounding mode Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Saturate on integer overflow off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Source of quantizer parameters** — Source of quantizer parameters `Specify via dialog` (default) | `Input port`

Specify the source of quantizer parameters as one of these:

- `Specify via dialog` –– Enter the
  boundary points and the codebook values using the parameters
  in the dialog box.
- `Input port` –– Specify the
  parameters using the block input ports. Input the boundary
  points and the codebook values using ports
  **B** and **C**,
  respectively.

### **Partitioning** — Partitioning method `Bounded` (default) | `Unbounded`

Specify one of these partitioning methods to interpret the boundary
points you enter:

- `Bounded` –– Select this option
  to create a bounded quantizer.

  For example, when you enter these boundary
  points:

  ```
  [0 0.5 3.7 5.8 6.0 11]
  ```

  The block assigns any input values between 0 and 0.5 to
  index 0, input values between 0.5 and 3.7 to index 1, and so
  on. The block assigns any values that are less than 0 to
  index 0, the lowest index value. The block assigns any
  values that are greater than 11 to index 4, the highest
  index value.
- `Unbounded` –– Select this option
  to create an unbounded quantizer.

  For example, when you enter these boundary
  points:

  ```
  [0 0.5 3.7 5.8 6.0 11]
  ```

  The block assigns any input values between 0 and 0.5 to
  index 1, input values between 0.5 and 3.7 to index 2, and so
  on. The block assigns any input values less than 0 to index
  0 and any values greater than 11 to index 6.

### **Boundary points** — Boundary points `[1:10]` (default) | vector

Enter a vector of values in ascending order that represent the
boundary points of the quantizer regions. These values are used to break
up the set of input numbers into regions. Each region is specified by an
index number.

Let *N* be the number of quantization regions. When
the codebook is defined as `[c1 c2 c3 ... cN]`, and the
**Boundary points** parameter is defined as
`[p0 p1 p2 p3 ... pN]`, then
`p0<c1<p1<c2 ... p(N-1)<cN<pN` for a
regular quantizer. When your quantizer is bounded, from the
**Partitioning** list, select
`Bounded`. You need to specify
*N*+1 boundary points, or `[p0 p1 p2 p3 ...
pN]`. When your quantizer is unbounded, from the
**Partitioning** list, select
`Unbounded`. You need to specify
*N*−1 boundary points, or`[p1 p2 p3 ...
p(N-1)]`. The block sets `p0` equal to
−`inf` and `pN` equal to
`inf`.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select `Specify via
dialog` from the **Source of quantizer
parameters** list.

### **Searching method** — Searching method `Linear` (default) | `Binary`

Specify the searching method the block uses to determine the region in
which the input value is located (quantizer index):

- `Linear` –– The block compares
  the input value to the first region defined by the first two
  boundary points. When the input value does not fall within
  this region, the block then compares the input value to the
  next region. This process continues until the input value is
  determined to be within a region and is associated with the
  appropriate index value. The computational cost of this
  process is of the order *P*, where
  *P* is the number of boundary
  points.
- `Binary` –– The block compares
  the input value to the middle value of the boundary points
  vector. When the input value is larger than this boundary
  point, the block discards the boundary points that are lower
  than this middle value. The block then compares the input
  value to the middle boundary point of the new range, defined
  by the remaining boundary points. This process continues
  until the input value is associated with the appropriate
  index value. The computational cost of this process is of
  the order log2*P*, where *P* is the number
  of boundary points. In most cases, the
  `Binary` option is faster than
  the `Linear` option.

### **Tie-breaking rule** — Action when input value is same as boundary point `Choose the lower index` (default) | `Choose the higher index`

Specify one of these actions to take when the input value is the same
as the boundary point. This parameter determines the region to which the
value is assigned.

- `Choose the lower index` –– The
  block assigns the input value to the lower indexed
  region.
- `Choose the higher index` –– The
  block assigns the input value to the higher indexed
  region.

### **Output codeword** — Output codeword `off` (default) | `on`

Select this check box to output the codeword values that correspond to
each index value at port **Q(U)**.

### **Output quantization error** — Output quantization error `off` (default) | `on`

Select this check box to output the quantization error for each input
value at port **Err**. The quantization error is the
difference between the input value and the quantized output
value.

### **Codebook** — Quantized output values `[1.5:9.5]` (default) | vector

Enter a vector of quantized output values that correspond to each
index value.

If you set the **Partitioning** parameter to
`Bounded` and your boundary points vector
has a length of *N*, then you must specify a codebook
of length *N*−1. If you set the
**Partitioning** parameter to
`Unbounded` and your boundary points vector
has a length of *N*, then you must specify a codebook
of length *N*+1.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select `Specify via dialog` from the
**Source of quantizer parameters** list and
select either the **Output codeword** or
**Output quantization error** check box.

### **Output clipping status** — Output clipping status `off` (default) | `on`

Specify the output clipping status on the port **S**.
Any time an input value is outside the range defined by the
**Boundary points** parameter, the block outputs a
1 at this port. When the value is inside the range, the block outputs a
0.

#### Dependencies

To enable this parameter, set the
**Partitioning** parameter to
`Bounded`.

### **Action for out of range input** — Action for out of range input `Clip` | `Clip and warn` | `Error`

Specify one of these actions the block must take when an input value
is outside the range defined by the **Boundary points** parameter:

- `Clip`
- `Clip and warn`
- `Error`

Suppose the boundary points for a bounded quantizer are defined as
`[p0 p1 p2 p3 ... pN]` and the possible index
values are defined as `[i0 i1 i2 ... i(N-1)]`, where
`i0=0` and
`i0<i1<i2<...<i(N-1)`. When you want
any input value less than `p0` to be assigned to index
value `i0` and any input values greater than
`pN` to be assigned to index value
`i(N-1)`, select `Clip`. When you
want to be warned when clipping occurs, select `Clip and
warn`. When you want the simulation to stop and the
block to display an error when the index values are out of range, select
`Error`.

#### Dependencies

To enable this parameter, set the
**Partitioning** parameter to
`Bounded`.

### **Index output data type** — Index output data type `int32` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Inherit via back propagation`

Specify the data type of the index output from the block at port
**I** as one of these:

- `int8`
- `uint8`
- `int16`
- `uint16`
- `int32`
- `uint32`
- `Inherit via back
  propagation`

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
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.
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

## Version History

**Introduced before R2006a**

## Description

Encode each input value by associating it with index value of quantization region

The Scalar Quantizer Encoder block maps each input value to a
quantization region by comparing the input value to the quantizer boundary points
defined in the **Boundary points** parameter. The block outputs the
zero-based index of the associated region.
