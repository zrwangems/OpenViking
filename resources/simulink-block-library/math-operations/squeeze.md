---
type: simulink-block
title: 'Squeeze'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'squeeze'
---

# Squeeze

Remove singleton dimensions from multidimensional signal

## Libraries

Simulink / Math Operations

## Description

The Squeeze block removes singleton dimensions from its
multidimensional input signal. A singleton dimension is any dimension whose size is one.
The Squeeze block operates only on signals whose number of dimensions is
greater than two. Scalar, vector, and matrix signals pass through the
Squeeze block unchanged.

## Ports

### Input

### **Port\_1** — Multidimensional input signal multidimensional signal

Input signal that has any singleton dimensions removed in the output.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal with no singleton dimensions multidimensional signal

Output signal with no singleton dimensions. For example, a
multidimensional array of size 3-by-1-by-2 changes into a 3-by-2 signal.
If there are no singleton dimensions in the input, then the input signal
is passed through unchanged to the output.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2007b**
