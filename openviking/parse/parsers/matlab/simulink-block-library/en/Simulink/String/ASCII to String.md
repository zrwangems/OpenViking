---
type: simulink-block
title: 'ASCII to String'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'asciitostring'
documentation_source_path: 'slref/asciitostring.html'
language: en
---

# ASCII to String

## Ports

### Input

### **Port\_1** — ASCII signal vector

ASCII signal, specified as a vector.

While using dynamic strings, if the length of the input vector exceeds
the number of characters specified in the configuration parameter
**Buffer size of dynamically-sized string (bytes)**
(`256` by default), the ASCII to
String block truncates the string output to the buffer
size-1 (for example, `255`), for generated code. To
avoid truncation, increase the value of the **Buffer size of
dynamically-sized string (bytes)** configuration
parameter.

**Example:**  [088 099]

**Data Types:** `uint8`
### Output

### **Port\_1** — Converted string signal scalar

Converted string signal from input ASCII signal, specified as a
scalar. The block converts each ASCII element in the vector into its
alphanumeric equivalent and outputs all elements concatenated into one
string.

**Data Types:** `string`

## Parameters

Not documented in R2025b.

## Libraries

Simulink / String

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Uint8 vector signal to string signal

The ASCII to String block converts uint8 vector signals to string
signals. The block treats each element in the input vector as an ASCII value during the
conversion. For example, the block converts an input vector of `[72 101 108 108
111]` to the string `"Hello"`.
