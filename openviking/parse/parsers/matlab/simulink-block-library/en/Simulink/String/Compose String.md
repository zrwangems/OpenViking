---
type: simulink-block
title: 'Compose String'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'composestring'
documentation_source_path: 'slref/composestring.html'
language: en
---

# Compose String

## Ports

### Input

### **d** — Data for first part of string scalar

Data for the first part of string, specified as a scalar. The
**Format** parameter determines the port label and
the format of the input data. For example, if the first item in the
**Format** parameter is `%d`, the
port label is d.

The data type of the input signal must be compatible with the format
specifier in the **Format** parameter. For more
information, see the **Format** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **f** — Data for second part of string scalar

Data for the second part of string, specified as a scalar. The
**Format** parameter determines the port label and
the format of the input data. For example, if the first item in the
**Format** parameter is `%f`, the
port label is f.

The data type of the input signal must be compatible with the format
specifier specified in the **Format** parameter. For
more information, see the **Format** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — Data for N parts of string scalar (default)

Data for *`N`* parts of string, specified as a
scalar. The **Format** parameter determines the port
label and the format of the input data. For example, if the
corresponding item in the **Format** parameter is
`%f`, the port label is f.

The data type of the input signal must be compatible with the format
specifier in the **Format** parameter. For more
information, see the **Format** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **str** — Output string scalar

Output string composed of inputs, specified as a scalar.

**Data Types:** `string`

## Parameters

### **Format** — Format input data "%d %f" (default) | format string | character vector

Format of input data, specified as a format string.

For more information about acceptable format specifiers, see Algorithms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character vector |
| **Values:** `'<filename>'` |
| **Default:** `'"%d %f"'` |

### **Output data type** — Output data type `string` (default) | `<data type expression>`

Output data type, specified using the string data type to specify a string
with no maximum length.

To specify a string data type with a maximum length, specify
`stringtype(N)`. For
example, `stringtype(31)` creates a string data type with a
maximum length of 31 characters.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'string'` | *`<data type expression>`* |
| **Default:** `'string'` |

### **Mode** — Category of data `string` (default) | `scalar`

Use the `stringtype` function, for example,
`stringtype(255)`.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

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

Compose output string signal based on specified format and input signals

The Compose String block composes output string signal based on the
format specifier listed in the **Format** parameter. The
**Format** parameter determines the number of input signals. If
there are multiple inputs, the block constructs the string by combining these multiple
inputs in order, and applying the associated format specifier, one format specifier for
each input. Each format specifier starts with a percent sign, `%`,
followed by the conversion character. For example, `%f` formats the
input as a floating point output. To supplement the string output, you can also add a
character to the format specification. Use this block to compose and format an output
string signal from a multiple inputs.

For example, if the **Format** parameter contains `"%s is
%f"`, the block expects two inputs, a string signal and a single or double
signal. If the first input is the string `"Pi"` and the second input is
a double value `3.14`, the output is `"Pi is
3.14"`.

When a MinGW® compiler compiles code generated from the block, running the compiled code
may produce nonstandard results for floating-point inputs. For example, a numeric input
of `501.987` returns the string `"5.019870e+002"`
instead of the expected string `"5.019870e+02"`.
