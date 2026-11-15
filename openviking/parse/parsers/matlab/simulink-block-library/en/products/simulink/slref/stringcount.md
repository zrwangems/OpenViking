---
type: simulink-block
title: 'String Count'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / String'
documentation_page: 'stringcount'
documentation_source_path: 'slref/stringcount.html'
language: en
---

# String Count

## Ports

### Input

### **str** — String to search scalar

String to search for the pattern in, specified as a scalar.

**Data Types:** `string`

### **sub** — String pattern to search for scalar

String pattern to search for in string, specified as a scalar.

**Data Types:** `string`
### Output

### **n** — Number of times pattern was found in string scalar

Number of times the string pattern was found in the string,
`str`, returned as a scalar.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## Parameters

### **Case sensitive** — Case sensitivity on (default) | off

Case sensitivity for the string count:

on
:   Consider string case when counting found strings.

off
:   Do not consider string case when counting found strings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CaseSensitive` |
| **Type**: character vector |
| **Values:** `'on'` | `'off'` |
| **Default**: `'on'` |

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `<data type expression>`

Output data type. The type can be inherited, specified directly, or expressed as a
data type object such as `Simulink.NumericType`.

When you select an inherited option, the block exhibits these behaviors:

- `Inherit: Inherit via internal rule` — Simulink® chooses a data type to balance numerical accuracy, performance, and
  generated code size, while taking into account the properties of the embedded target
  hardware.
- `Inherit: Inherit via back propagation` — Use data type
  of the driving block.

Click the Show data type assistant button  to display the **Data Type
Assistant**, which helps you set the data type attributes. See Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | *`<data type expression>`* |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Mode** — Category of data type `Inherit` (default) | `Built in` | `Expression`

Category of data type, specified as `Inherit`, `Built
in`, or `Expression`. For more information on using this
parameter, see Specify Data Types Using Data Type Assistant.

#### Dependency

Clicking the **Show data type assistant** button enables this
parameter.

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

**Introduced in R2020a**

## Description

Count occurrences of pattern in string

The String Count block counts the occurrences of the pattern
(**sub**) in a string (**str**). If the input at
**sub** matches part or all of the input at **str**, the
block counts the occurrence as 1.
