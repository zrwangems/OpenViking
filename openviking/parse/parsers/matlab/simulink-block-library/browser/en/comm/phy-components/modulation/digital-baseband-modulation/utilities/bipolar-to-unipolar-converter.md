---
type: simulink-block
title: 'Bipolar to Unipolar Converter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Utilities'
documentation_page: 'bipolartounipolarconverter'
documentation_source_path: 'ref/bipolartounipolarconverter.html'
language: en
---

# Bipolar to Unipolar Converter

## Ports

### Input

### **In** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix. The block
expects a signal of integers in the set {–*M*+1,
–*M*+3, –*M*+5,...,
*M* – 1}, where *M* is the
**M-ary
number** parameter value.

The input signal is unnamed on the block mask.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Out** — Output signal scalar | vector | matrix

Output signal, returned as a signal of integers in the range [0,
(*M* – 1)] with the same dimensions as the input
signal, **In**. *M* is the **M-ary
number** parameter value. The **Output
data type** parameter specifies the desired data
type.

The output signal is unnamed on the block mask.

**Note**

The output might not be valid for input signal values outside the
set {–*M*+1, –*M*+3,
–*M*+5,..., *M* – 1}.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **M-ary number** — Number of symbols `4` (default) | positive integer

Number of symbols in the bipolar or unipolar alphabet, specified as a
positive integer.

### **Polarity** — Relative ordering of symbols `Positive` (default) | `Negative`

Relative ordering of symbols, specified as
`Positive` or
`Negative`.

- `Positive` causes the block to
  maintain the relative ordering of symbols in the
  alphabets.
- `Negative` causes the block to
  reverse the relative ordering of symbols in the
  alphabets.

The value of this parameter determines the output for input value
*k* and **M-ary
number** parameter value *M*.

|  | Output |
| --- | --- |
| `Positive` | (*M* – 1 + *k*)/2 |
| `Negative` | (*M* – 1 – *k*)/2 |

### **Output data type** — Output data type of unipolar signal `Inherit via internal rule` (default) | `Same as input` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `boolean`

Output data type of the unipolar signal, specified as `Inherit
via internal rule`, `Same as
input`, `double`,
`int8`, `int16`,
`int32`, `uint8`,
`uint16`, `uint32`, or
`boolean`.

When you set this parameter to `Inherit via internal
rule`, the block determines the output data type based on
the input data type as follows:

- If the input data type is either
  `single` or
  `double`, the output data type is
  the same as the input data type.
- If the input data type is not
  `single` or
  `double`:

  - For the **M-ary number** parameter value,
    *M*, the block computes the ideal
    signed integer output word length,
    *ideal\_word\_length*, required to
    contain the range [0, *M* – 1]
    as:

    `ideal_word_length =
    ceil(log2(M))`.
  - The block sets the output data type to be an
    unsigned integer, based on the smallest word length
    (in bits) that can best fit the computed ideal word
    length.

**Note**

Selections in the Hardware Implementation Pane (Simulink) that constrain word length do not affect how this block
determines output data types.

## Libraries

Communications Toolbox / Utility Blocks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
|  |  |
| --- | --- |
| a Signed only. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Map bipolar signal to unipolar signal in range [0, M – 1]

The Bipolar to Unipolar Converter block maps the bipolar input signal to a unipolar
output signal.
