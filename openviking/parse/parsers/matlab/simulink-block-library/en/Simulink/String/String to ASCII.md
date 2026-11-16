---
type: simulink-block
title: 'String to ASCII'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / String'
documentation_page: 'stringtoascii'
documentation_source_path: 'slref/stringtoascii.html'
language: en
---

# String to ASCII

## Ports

### Input

### **Port\_1** — Input string signal scalar

Input string signal, specified as a scalar.

**Data Types:** `string`
### Output

### **Port\_1** — Converted uint8 vector signal vector | 1D vector of *N* elements

Converted `uint8` vector signal of ASCII characters from input string
signal, specified as a vector. The block converts each element in the
string into its ASCII character equivalent and outputs the ASCII
equivalents as a vector. If there are fewer characters than the maximum
length, the block fills the remaining space with zeros at simulation. At
code generation, the block fills the remaining space with null
characters.

**Data Types:** `uint8`

## Parameters

### **Output vector size** — Size of output vector 31 (default) | scalar

Size of output string vector, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputVectorSize` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'31'` |

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

### R2024b: String to ASCII block output dimension change

The String to
ASCII block output dimension has changed from a 2D row vector, such as a
2-by-*N* vector, to a 1D vector, *N*.
*N* is the number of elements.

## Description

Convert string signal to uint8 vector

The String To ASCII block converts a string signal to a uint8 vector. The
block converts each character in the string to its corresponding ASCII value. For
example, the block converts the input string `"Hello"` to `[72
101 108 108 111]`.
