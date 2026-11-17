---
type: simulink-block
title: 'Uniform Encoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'uniformencoder'
documentation_source_path: 'ref/uniformencoder.html'
language: en
---

# Uniform Encoder

## Ports
```yaml
ports:
- name: Input
  summary: Input signal vector | matrix
  direction: input
  data_types: single | double
- name: Output
  summary: Encoder output vector | matrix
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
```

### Input

### **Input** — Input signal vector | matrix

Specify the floating-point input signal as a vector or a matrix.
Inputs greater than
(1−21−*B*)*V*
or less than −*V* saturate at those respective values.
The real and imaginary components of complex inputs saturate
independently.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output** — Encoder output vector | matrix

Encoder output, returned as a vector or a matrix. The block quantizes
each sample in the floating-point input and encodes the quantized
floating-point value to an integer value. For more information on how
the block computes the output, see Algorithms.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Peak
  summary: Largest input amplitude to encode 1 (default) | nonnegative scalar
  group: ''
- name: Bits
  summary: Number of bits 8 (default) | integer in the range [2, 32]
  group: ''
- name: Output type
  summary: Data type of block output Unsigned integer (default) | Signed integer
  group: ''
```

### **Peak** — Largest input amplitude to encode `1` (default) | nonnegative scalar

Specify the largest input amplitude to encode *V* as a
nonnegative scalar. Real or imaginary input values greater than
(1−21−*B*)*V*
or less than −*V* saturate (independently for complex
inputs) at those limits.

### **Bits** — Number of bits `8` (default) | integer in the range [`2`, `32`]

Specify the number of bits *B* that the block needs to
represent the integer output. The number of bits *B* can be
any integer value between 2 and 32, inclusive. The number of levels at which
the block quantizes the floating-point input is 2*B*.

### **Output type** — Data type of block output `Unsigned integer` (default) | `Signed integer`

Specify the data type of the block output as one of these:

- `Unsigned integer` –– The block maps
  the smallest quantized floating-point value
  −*V* to the integer 0 and the largest
  quantized floating-point value
  (1−21−*B*)*V*
  to the integer
  2*B*−1. It linearly
  (uniformly) maps the intermediate quantized floating-point
  values to the intermediate integers in the range [0,
  2*B*−1]. For
  efficiency, the block automatically selects an
  *unsigned* output data type
  (`uint8`,
  `uint16`, or
  `uint32`) with the minimum number
  of bits equal to or greater than *B*.
- `Signed integer` –– The block maps
  the smallest quantized floating-point value
  −*V* to the integer
  −2*B*−1, and
  the largest quantized floating-point value
  (1−21−*B*)*V*
  to the integer
  2*B*−1−1. It
  linearly maps the intermediate quantized floating-point values
  to the intermediate integers in the range
  [−2*B*−1,
  2*B*−1−1].
  The block automatically selects a *signed*
  output data type (`int8`,
  `int16`, or
  `int32`) with the minimum number of
  bits equal to or greater than *B*.

This table shows the output data types that the block uses.

| Bits | Unsigned Integer | Signed Integer |
| --- | --- | --- |
| `2` to `8` | `uint8` | `int8` |
| `9` to `16` | `uint16` | `int16` |
| `17` to `32` | `uint32` | `int32` |
## Libraries

DSP System Toolbox / Quantizers

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Quantize and encode floating-point input into integer output

The Uniform Encoder block performs these two operations on each
floating-point sample in the input vector or matrix:

1. Quantizes the value using the same precision
2. Encodes the quantized floating-point value to an integer
   value

For more information on how the block computes the output, see Algorithms.

The Uniform Encoder block operations adhere to the definition for
uniform encoding specified in ITU-T Recommendation G.701.
