---
type: simulink-block
title: 'To String'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'tostring'
language: en
---

# To String

Convert input signal to string signal

## Libraries

Simulink / String

## Description

The To String block creates a string signal from an input signal. For
example, consider using this signal to convert a logical value `1` or
`0` to its string equivalent `"false"` or
`"true"`.

The To String block generates efficient code for enumerations by generating a shared
function for each enumeration type. For more information on enumerations, see Simulink Enumerations.

When a MinGW® compiler compiles code generated from the block, running the compiled code
may produce nonstandard results for floating-point inputs. For example, a numeric input
of `501.987` returns the string `"5.019870e+002"`
instead of the expected string `"5.019870e+02"`.

## Ports

### Input

### **Port\_1** — Input signal scalar

Input signal, specified as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Output string scalar

Output string, specified as a scalar. This block returns the output as
a string, surrounded by double quotes.

- If the input is a Boolean, the output is a logical value
  (`1` or `0`) and the block
  returns its textual equivalent (`true` or
  `false`).

- If the input is a numeric data type, such as an integer,
  single, double, or fixed point, the block returns the number as
  a string. For example, an input of `1` converts
  to `"1"` and an input of `0`
  converts to `"0"`.

  **Note**

  The output string might not contain all the digits of the
  numeric value from the input port.

**Data Types:** `string`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2018a**

### R2024b: To String block generates more efficient code

The To String block now generates more efficient code for enumerations by
generating a shared function for each enumeration type. Prior to R2024b, this block
generated inlined code for enumerations.
