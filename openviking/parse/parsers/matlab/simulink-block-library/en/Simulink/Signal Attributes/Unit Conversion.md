---
type: simulink-block
title: 'Unit Conversion'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Attributes'
documentation_page: 'unitconversion'
documentation_source_path: 'slref/unitconversion.html'
language: en
---

# Unit Conversion

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal with converted units with the same dimensions as the input signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation`

Specify the output data type.

- `Inherit: Inherit via internal rule` —
  Simulink® chooses intermediate and output data types to balance
  numerical accuracy, performance, and generated code size, while
  accounting for the properties of the embedded target hardware. If
  you change the embedded target settings, the data type selected by
  the internal rule might change.
- `Inherit: Inherit via back propagation` —
  Output data type is inherited via back propagation. Internal rules
  determine the intermediate data types and Simulink casts the final results to the output data
  type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputType` |
| **Type:** character vector |
| **Values:** `'Inherit via internal rule' | 'Inherit via back propagation'` |
| **Default:** `'Inherit via internal rule'` |

## Libraries

Simulink / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2016a**

## Description

Convert units

The Unit Conversion block converts the unit of the input signal to the output
signal. The block can perform the conversion if the units are separated by a scaling
factor or offset, or are inverse units, for example:

- *y* = *a*\**U*
- *y* =
  *a*\**U*+*b*, where
  *a* is the scale and *b* is the
  offset
- *y* = *a*/*U*

This block supports normal, accelerator, and rapid accelerator modes and fast restart.
