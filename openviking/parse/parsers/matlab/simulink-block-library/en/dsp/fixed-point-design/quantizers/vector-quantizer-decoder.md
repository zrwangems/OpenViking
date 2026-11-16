---
type: simulink-block
title: 'Vector Quantizer Decoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Fixed-Point Design / Quantizers'
documentation_page: 'vectorquantizerdecoder'
documentation_source_path: 'ref/vectorquantizerdecoder.html'
language: en
---

# Vector Quantizer Decoder

## Ports

### Input

### **I** — Index values scalar | row vector

Specify the index values to be a scalar or a row vector in the range 0
≤ *index* < *N*, where
*N* is the number of columns of the codebook
matrix.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **C** — Codebook values vector | matrix

Specify the codebook values as a vector or a matrix,

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Q(U)** — Quantized output values row vector | matrix

Quantized output values, returned as a vector or a matrix.

These quantized output values always have the same data type as the codebook values.
When you specify the codebook values via an input port, the block
assigns the same data type to the **Q(U)** output port.
When you specify the codebook values via the dialog box, use the
**Codebook and output data type** parameter to
specify the data type of the **Q(U)** output
port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## Parameters

### Main Tab

### **Action for out of range index value** — Action for out of range index value `Clip` (default) | `Clip and warn` | `Error`

Specify the action to take when an input index value is out of range,
where 0 ≤ *index* <
*N* and *N* is the length of the codebook
vector (or the number of columns in the codebook matrix).

Select `Clip` when you want any index values less than 0 to be
set to 0 and any index values greater than or equal to
*N* to be set to *N*−1. Select
`Clip and warn` to be warned when the block
sets any index values less than 0 to 0 and any index values greater than
or equal to *N* to *N*−1. Select
`Error` for the simulation to stop and
display an error when the index values are out of range.

### **Source of codebook** — Source of codebook `Specify via dialog` (default) | `Input port`

Specify the source of the codebook values as one of these options:

- `Specify via dialog` –– Specify
  codebook values in the **Codebook values**
  parameter.
- `Input port` –– Specify codebook
  values through the input port **C**.

### **Codebook values** — Codebook values `[1.5 13.3 136.4 6.8; 2.5 14.3 137.4 7.8; 3.5 15.3 138.4 8.8]` (default)

Specify the codebook values as a
*k*-by-*N* matrix of quantized
output values, where *k* ≥ 1 and *N* ≥ 1. Each column of this matrix is a codeword vector, and
each codeword vector corresponds to an index value. The index values are
zero based. The first codeword vector corresponds to an index value of
0, the second codeword vector corresponds to an index value of 1, and so
on.

#### Dependencies

To enable this parameter, set the **Source of
codebook** parameter to `Specify via
dialog`.

### Data Types Tab

### **Codebook and output data type** — Codebook and output data type `double` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `single` | `fixdt(1,16)` | `fixdt(1,16,0)`

Specify the data type of the codebook and quantized output values. You
can select one of the following:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`.
- A built in data type, such as `double`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Output data
type** parameter.

See Control Data Types of Signals (Simulink) for more information.

#### Dependencies

To enable this parameter, set the **Source of
codebook** parameter to `Specify via
dialog`. If you set the **Source of
codebook** parameter to `Input
port`, the output values have the same data type as
the input codebook values.

## Libraries

DSP System Toolbox / Quantizers

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `fixed point` | `integer` |
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

Find vector quantizer codeword that corresponds to zero-based index value

The Vector Quantizer Decoder block associates each input index value with a
codeword, expressed as a column vector of quantized output values defined in the
**Codebook values** parameter. When you input multiple index values
into this block, the block outputs a matrix of quantized output vectors. The block
creates this matrix by horizontally concatenating the codeword vectors that correspond
to each index value.
