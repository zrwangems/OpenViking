---
type: simulink-block
title: 'String to Enum'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringtoenum'
language: en
---

# String to Enum

Input string signal to enumerated signal

## Libraries

Simulink / String

## Description

The String To Enum block converts the input string signal to an enumerated
signal. To use this block, create an enumeration class in the current folder and use
that class name in the **Output data type** parameter.

The String to Enum block generates efficient code for enumerations by generating a shared
function for each enumeration type. For more information on enumerations, see Simulink Enumerations.

## Ports

### Input

### **Port\_1** — Input string signal scalar

Input string signal, specified as a scalar.

**Data Types:** `string`
### Output

### **Output 1** — Enumerated number scalar

Enumerated number associated with the input string, specified as a
scalar.

**Data Types:** `enumerated`

## Parameters

### **Output data type** — Output data type `SlDemoSign` (default) | `<data type expression>`

Use a data type object, for example,
`Simulink.IntEnumType`.

Click the **Show data type assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Enum: SlDemoSign'` | *`<data type expression>`* |
| **Default:** `'Enum: SlDemoSign'` |

### **Mode** — Category of data `Enumerated` (default) | `<data type expression>`

Use a data type object, for example,
`Simulink.IntEnumType`.

- `Enumerated` — Enumerated data class
  object.
- `<data type expression>` —
  Expressions that evaluate to data types. Selecting
  `Expression` enables a second menu/text box to
  the right, where you can enter the expression.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `enumerated` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: String to Enum block generates more efficient code

The String to Enum block now generates more efficient code for enumerations by
generating a shared function for each enumeration type. Prior to R2025a, this block
generated inlined code for enumerations.
