---
type: simulink-block
title: 'String Concatenate'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringconcatenate'
documentation_source_path: 'slref/stringconcatenate.html'
language: en
---

# String Concatenate

## Ports

### Input

### **Port\_1** — First input string scalar

First input string, specified as a scalar.

**Data Types:** `string`

### **Port\_2** — Second input string scalar

Second input string, specified as a scalar.

**Data Types:** `string`
### Output

### **Port\_1** — Concatenated string scalar

Concatenated string, specified as a scalar.

**Data Types:** `string`

## Parameters

### **Number of Inputs** — Number of input strings scalar

Number of input strings to concatenate, specified as a scalar. You can
specify from 2 to 512 input ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** scalar from `2` to `512` |
| **Default:** `'2'` |

### **Output data type** — Output data type `string` (default) | `<data type expression>` | scalar

Output data type, specified using the string data type to specify a string
with no maximum length.

To specify a string data type with a maximum length, specify
`stringtype(N)`. For
example, `stringtype(128)` creates a string data type with
a maximum length of 128 characters.

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

### **Mode** — Category of data `stringtype(128)` (default) | `scalar`

Use the `stringtype` function, for example,
`stringtype(128)`.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

## Libraries

Simulink / String

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Concatenate input strings to form one output string

The String Concatenate block concatenates multiple input strings, in
order of their input, to form one output string. Use this block if you want to combine
multiple strings into a single string.
