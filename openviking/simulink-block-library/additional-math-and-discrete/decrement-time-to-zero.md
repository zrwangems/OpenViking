---
type: simulink-block
title: 'Decrement Time To Zero'
family: additional-math-and-discrete
documentation_release: R2025b
official_category: 'Additional Math and Discrete'
documentation_page: 'decrementtimetozero'
---

# Decrement Time To Zero

Decrease real-world value of signal by sample time, but only to zero

## Libraries

Simulink / Additional Math & Discrete / Additional Math: Increment - Decrement

## Description

The Decrement Time To Zero block decreases the real-world value of the
signal by the sample time, `Ts`. The output never goes below
zero.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output is the real-world value of the input signal decreased by the
sample time, `Ts`. The output never goes below zero.
The output has the same data type and dimensions as the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
