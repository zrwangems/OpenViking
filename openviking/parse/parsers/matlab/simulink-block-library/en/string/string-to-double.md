---
type: simulink-block
title: 'String to Double'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringtodouble'
language: en
---

# String to Double

## Ports

### Input

### **Port\_1** — Input string scalar

Input string, specified as a scalar.

**Data Types:** `string`
### Output

### **d** — Output data whose format matches `%d` format scalar

Output data whose format matches specified format, defined as a
scalar. Total maximum number of outputs is 128.

If the block cannot match an input string to a format operator
specified in **Format**, it returns a warning and
outputs an appropriate value (`0` or
`""`) for each unmatched format operator.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **f** — Output data whose format matches %f format scalar

Output data whose format matches the `%f` format,
specified as a scalar. Total maximum number of outputs is 128.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — Output data whose format matches N format scalar

Output data whose format matches *`N`* format,
specified as a scalar. Total maximum number of outputs is 128.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Format** — Format operator for input `"%lf"` (default) | format string | character vector

Format operator for input, specified as a scalar. If the block cannot
match the input string with the specified format, it returns
`0`. The return of `0` differs from
the `sscanf` function return, which
is an empty matrix if the function cannot match the input with the specified
format.

- For the String to Double block, this parameter has
  a default value of `%lf`.
- For the String to Single block, this parameter has
  a default value of `%f`.

For more information about acceptable format operators, see the Algorithms
section.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character vector |
| **Values:** `'<filename>'` |
| **Default:** `'"%lf"'` if the block is String to Double, `'"%f"'` if the block is String to Single |

## Libraries

Simulink / String

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Convert string signal to double signal

Scan String scans an input string and converts it to signals per the
format specified by the **Format** parameter. The block converts values
to their decimal (base 10) representation and outputs the results as numeric or string
signals. For example, if the **Format** parameter is set to
`"%s is %f."`, the block outputs two parts, a string signal and a
single signal. If the input is the string `"Pi is 3.14"`, the two
outputs are `"Pi"` and `"3.14"`.

The Scan String, String to Double, and String to
Single blocks are identical blocks. When configured for String to
Double, the block converts the input string signal to a double numerical
output. When configured for String to Single, the block converts the
input string signal to a single numerical output.

For code generation, configure models that contain this block for non-finite number
support by selecting the **Configuration Parameters** > **Code Generation** > **Interface** > **Support non-finite numbers** check box.
