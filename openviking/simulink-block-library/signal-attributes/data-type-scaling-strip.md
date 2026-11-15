---
type: simulink-block
title: 'Data Type Scaling Strip'
family: signal-attributes
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypescalingstrip'
---

# Data Type Scaling Strip

Remove scaling and map to built in integer

## Libraries

Simulink / Signal Attributes

## Description

The Data Type Scaling Strip block strips the scaling off a fixed-point
signal. It maps the input data type to the smallest built-in data type that has enough
data bits to hold the input. The stored integer value of the input is the value of the
output. The output always has nominal scaling (slope = 1.0 and bias = 0.0), so the
output does not distinguish between real world value and stored integer value.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix. The block
strips the scaling off a fixed-point input signal, and outputs the
stored integer value with the smallest possible built-in data
type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Input signal mapped to built-in data type scalar | vector | matrix

Stored integer value of the input signal with the smallest possible
built-in data type, and the same dimensions as the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
