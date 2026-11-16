---
type: simulink-block
title: 'dB Gain'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Array Operations'
documentation_page: 'dbgain'
documentation_source_path: 'ref/dbgain.html'
language: en
---

# dB Gain

## Ports

### Input

### **Input** — Input signal scalar | vector | matrix

Specify the input signal as a scalar, vector, or a matrix of size
*M*-by-*N*.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Output after applying the decibel gain scalar | vector | matrix

Output after applying the decibel gain, returned as a scalar, vector,
or a matrix of the same size, data type, and complexity as the input
signal.

For more information on how the block applies the decibel gain, see
Algorithms.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

**Note**

This block does not support tunability in generated code.

### **Gain, dB** — Gain `-40` (default) | scalar | matrix

Specify the dB gain to apply to the input as a scalar or a real matrix of
the same size as the input matrix.

**Tunable:** Yes

### **Input signal** — Input signal `Amplitude` (default) | `Power`

Specify the type of input signal as one of these:

- `Power` –– The block treats the
  signal as the power signal.
- `Amplitude` –– The block treats the
  signal as the voltage signal.

**Tunable:** Yes

## Libraries

DSP System Toolbox / Math Functions / Math Operations

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

This block does not support tunability in generated code.

## Version History

**Introduced before R2006a**

## Description

Apply decibel gain

The dB Gain block multiplies the input by the decibel values specified
in the **Gain** parameter. You can specify the input to be a power
signal or a voltage signal.

For more information on how the block applies the decibel gain, see Algorithms.
