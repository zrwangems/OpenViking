---
type: simulink-block
title: 'String Find'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringfind'
language: en
---

# String Find

## Ports

### Input

### **str** — String in which to find pattern scalar

String in which to find pattern (`sub`), specified as
a scalar.

**Data Types:** `string`

### **sub** — Pattern scalar

Pattern to be found in string (`str`), specified as a
scalar.

**Data Types:** `string`
### Output

### **idx** — Position index of found pattern scalar

Position index of the found pattern, specified as a positive integer
scalar.

- If the block does not find the pattern, it returns
  `-1`.
- If the **sub** parameter is empty
  (`""`), the block returns
  `1`, indicating that it matched the
  beginning of the searched string.

**Data Types:** `int8` | `int16` | `int32`

## Parameters

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `int8` | `int16` | `int32` | `<data type expression>`

Output data type. The type can be inherited, specified directly, or
expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block exhibits these
behaviors:

- `Inherit: Inherit via internal rule` —
  Simulink® chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account the
  properties of the embedded target hardware.
- `Inherit: Inherit via back propagation` —
  Use data type of the driving block.

Click the **Show data type assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'int16'` | `'int32'` | *`<data type expression>`* |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Mode** — Category of data type `Inherit` (default) | `Built in` | `Expression`

Category of data type, specified as `Inherit`,
`Built in`, or `Expression`. For more
information on using this parameter, see Specify Data Types Using Data Type Assistant.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

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

Return index of first occurrence of pattern string

The String Find block returns the index of the first occurrence of the
pattern string **sub** in the text string **str**.
