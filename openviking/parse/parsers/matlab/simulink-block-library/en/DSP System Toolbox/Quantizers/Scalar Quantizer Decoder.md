---
type: simulink-block
title: 'Scalar Quantizer Decoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'scalarquantizerdecoder'
documentation_source_path: 'ref/scalarquantizerdecoder.html'
language: en
---

# Scalar Quantizer Decoder

## Ports

### Input

### **I** — Index values vector

Specify the index values in the range, 0 ≤ index < *N*, where *N* is the number of distinct
codeword vectors in the codebook matrix.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **C** — Codebook values vector | matrix

Specify the codebook values as a vector or a matrix.

#### Dependencies

To enable this port, set the **Source of
codebook** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Q(U)** — Quantized output values vector | matrix

Quantized output values, returned as a vector or a matrix of the same
size as the input data.

If the codebook values are input through the **C**
port, the quantized output values have the same data type as the input
codebook values. If the codebook values are specified in the block
dialog box, the **Codebook and output data type**
parameter determines the data type of the quantized output
values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## Parameters

### Main Tab

### **Action for out of range index value** — Action for out of range index value `Clip` (default) | `Clip and warn` | `Error`

Specify one of these actions the block must take when an input index
value is outside the range 0 ≤ index <*N*, where *N* is the length of the
codebook vector. Select `Clip`, when you want
any index values less than 0 to be set to 0 and any index values greater
than or equal to *N* to be set to
*N*−1. Select `Clip and warn`,
when you want to be warned when clipping occurs. Select
`Error`, when you want the simulation to
stop and the block to display an error when the index values are outside
the range.

### **Source of codebook** — Source of codebook `Specify via dialog` (default) | `Input port`

Specify the source of codebook values as one of these:

- `Specify via dialog` –– Enter the
  codebook values in the **Codebook values**
  parameter.
- `Input port` –– Specify the
  codebook values through the input port
  **C**.

### **Codebook values** — Codebook values `[1:10]` (default) | vector | matrix

Enter all possible quantized output values that correspond to each
index value as a vector or a matrix. The data type of the codebook
values is determined by the setting of the **Codebook and output
data type** parameter.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Source of
codebook** parameter to `Specify via
dialog`.

### Data Types Tab

### **Codebook and output data type** — Codebook and output data type `double` (default) | `Same as input` | `single` | `Inherit via back propagation` | numeric type

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

See Control Data Types of Signals (Simulink) for more
information.

#### Dependencies

This parameter is available only when you set the **Source
of codebook** parameter to `Specify via
dialog`. If you set the **Source of
codebook** parameter to `Input
port`, the quantized output values have the same
data type as the input codebook values.

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Convert each index value into quantized output value

The Scalar Quantizer Decoder block transforms the zero-based input index
values into quantized output values. For each input index value, the block outputs the
corresponding quantized output value (or codeword).

The set of all possible quantized output values is defined by the **Codebook
values** parameter.
