---
type: simulink-block
title: 'Edge Detector'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Switches and Counters'
documentation_page: 'edgedetector'
documentation_source_path: 'ref/edgedetector.html'
language: en
---

# Edge Detector

## Ports
```yaml
ports:
- name: Input
  summary: Input signal vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
- name: Output
  summary: Output of edge detector vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated
```

### Input

### **Input** — Input signal vector | matrix

Specify the input signal as a vector or a matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Output** — Output of edge detector vector | matrix

The block returns the output of the edge detector as a vector or a
matrix.

The block might output Boolean values depending on the input data
type, and whether Boolean support is enabled or disabled.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
## Parameters
```yaml
parameters:
- name: Input processing
  summary: Input processing Columns as channels (frame based) (default) | Elements as channels (sample based)
  group: ''
```

### **Input processing** — Input processing `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. You can set this parameter to one of
the following options:

- `Columns as channels (frame based)` (default) — When
  you select this option, the block treats each column of the input as a separate
  channel.
- `Elements as channels (sample based)` — When you
  select this option, the block treats each element of the input as a separate
  channel.
## Libraries

DSP System Toolbox / Signal Management / Switches and Counters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
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

Detect transition from zero to nonzero value

The Edge Detector block generates an impulse (the value 1) in a given
output channel when the corresponding channel of the input transitions from zero to a
nonzero value. When the input does not transition from zero to a nonzero value, the
block generates a zero in the corresponding output channel.

This block supports only discrete-time fixed-step signals. Continuous signals are not
supported.

The output has the same dimension and sample rate as the input. When you set the
**Input processing** parameter to `Columns as channels
(frame based)`, the block counts an edge that is split across two
consecutive frames in the frame that contains the nonzero value. For example, if there
is a zero at the bottom of the first frame and a nonzero value at the top of the second
frame, the block counts the edge in the second frame.
