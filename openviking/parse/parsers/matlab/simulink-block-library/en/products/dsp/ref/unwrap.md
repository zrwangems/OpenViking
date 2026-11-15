---
type: simulink-block
title: 'Unwrap'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Operations / Signal Operations'
documentation_page: 'unwrap'
documentation_source_path: 'ref/unwrap.html'
language: en
---

# Unwrap

## Ports

### Input

### **Port\_1** — Signal input scalar | vector | matrix

Signal input to unwrap, specified as a scalar, vector, or matrix. The
input must have radian phase entries.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Signal output scalar | vector | matrix

Unwrapped signal output, returned as a scalar, vector, or matrix.

The block preserves the input size and dimension, and the output port
rate equals the input port rate.

**Data Types:** `single` | `double`

## Parameters

### **Tolerance (radians)** — Jump size `pi` (default) | scalar value

The jump size that the block recognizes as a true phase discontinuity. The
default is set to *π* (rather than a smaller value) to
avoid altering legitimate signal features. To increase the block's
sensitivity, set the **Tolerance** to a value slightly less
than π.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Input processing** — Method to process the input `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. You can set this parameter
to one of these options:

- `Columns as channels (frame based)`
  (default) — When you select this option, the block treats
  each column of the input as a separate channel.
- `Elements as channels (sample based)`
  — When you select this option, the block treats each element
  of the input as a separate channel.

### **Reset initial phase to zero for each input frame** — Checking successive frames `off` (default) | `on`

When you clear this parameter, the block ignores boundaries between input
frames and does not reset the initial phase value to zero each time a new
input is received. In this mode, the block continuously unwraps the data in
each column of the input.

This figure illustrates how the block unwraps data when you clear this
parameter.

When you select this parameter, the block treats each frame of input data
independently and resets the initial phase value for each new input
frame.

This figure illustrates how the block unwraps data when you select this
parameter.

For more information, see Frame-Based Processing.

#### Dependencies

To enable this parameter, set the **Input
processing** parameter to `Columns as channels
(frame based)`. In sample-based processing mode, the
block does not reset the initial phase value to zero for each new input.
See Sample-Based Processing for more information.

## Libraries

DSP System Toolbox / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Unwrap signal phase

The Unwrap block unwraps each channel of the input by adding or
subtracting appropriate multiples of 2π to each channel element. The block recognizes
phase discontinuities larger than the value of the **Tolerance**
parameter. For more information on phase unwrapping, see Definition of Phase Unwrap.
