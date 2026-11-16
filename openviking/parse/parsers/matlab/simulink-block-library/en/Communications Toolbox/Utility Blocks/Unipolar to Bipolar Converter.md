---
type: simulink-block
title: 'Unipolar to Bipolar Converter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'unipolartobipolarconverter'
documentation_source_path: 'ref/unipolartobipolarconverter.html'
language: en
---

# Unipolar to Bipolar Converter

## Ports

### Input

### **In** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix. The block
expects input integers in the range [0, (*M* – 1)],
where *M* is the **M-ary
number** parameter.

The input signal is unnamed on the block mask.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32`
### Output

### **Out** — Output signal scalar | vector | matrix

Output signal, returned as a signal of integers in the range
[–(*M* – 1), (*M* – 1)] with the
same dimensions as the input signal, **In**. *M* is the **M-ary
number** parameter value. The **Output
data type** parameter specifies the desired data type.

- When you set *M* to an even integer, the
  block outputs odd integer values.
- When you set *M* to an odd integer, the
  block outputs even integer values.

The output signal is unnamed on the block mask.

**Note**

The output might not be valid for unsigned integer input values,
noninteger input values, or integer input values outside the range
[0, (*M* – 1)].

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

This value of this parameter determines the output for input value
*k* and **M-ary
number** parameter value *M*.

|  | Output |
| --- | --- |
| `Positive` | 2*k* – (*M* – 1) |
| `Negative` | –2*k* + (*M* – 1) |

### **Output data type** — Output data type of bipolar signal `Inherit via internal rule` (default) | `Same as input` | `double` | `int8` | `int16` | `int32`

Output data type of the bipolar signal, specified as `Inherit
via internal rule`, `Same as
input`, `double`,
`int8`, `int16`, or
`int32`.

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
    contain the range [–(*M* – 1),
    (*M* – 1)] as:

    `ideal_word_length = ceil(log2(M)) +
    1`, where `+ 1` fulfills
    the need for the sign bit.
  - The block sets the output data type to be a signed
    integer, based on the smallest word length (in bits)
    that can best fit the computed ideal word
    length.

**Note**

Selections in the Hardware Implementation Pane (Simulink) that constrain word length do not affect how this block
determines output data types.

## Libraries

Communications Toolbox / Utility Blocks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Map unipolar signal in range [0, M – 1] to bipolar signal

The Unipolar to Bipolar Converter block maps the unipolar input signal to a bipolar
output signal.
