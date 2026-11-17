---
type: simulink-block
title: 'Cumulative Sum'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'cumulativesum'
documentation_source_path: 'ref/cumulativesum.html'
language: en
---

# Cumulative Sum

## Ports
```yaml
ports:
- name: In
  summary: Input signal vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Rst
  summary: Reset port scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
- name: Out
  summary: Cumulative sum vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **In** — Input signal vector | matrix

Input, specified as a vector or as matrix inputs containing real or
complex values.

This port is unnamed until you select a
non-`None` value for the `Reset
port` parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Rst** — Reset port scalar

The optional reset port, **Rst**, accepts scalar
values, which can be any built-in Simulink® data type including `boolean`. The rate
of the input to the **Rst** port must be the same or
slower than that of the input data signal. The sample time of the input
to the **Rst** port must be a positive integer multiple
of the input sample time.

This port is unnamed until you select a
non-`None` value for the `Reset
port` parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### Output

### **Out** — Cumulative sum vector | matrix

Cumulative sum of input, specified as a vector or a matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Sum input along
  summary: Dimension to sum along Channels (running sum) (default) | Columns | Rows
  group: Main
- name: Input processing
  summary: Method to process the input Columns as channels (frame based) (default) | Elements as channels (sample based)
  group: Main
- name: Reset port
  summary: Reset type None (default) | Rising edge | Falling edge | Either edge | Non-zero sample
  group: Main
- name: Rounding mode
  summary: Rounding mode Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Saturate for fixed-point operation off (default) | on
  group: Data Types
- name: Accumulator
  summary: 'Data type of accumulator Inherit: Same as first input (default) | fixdt([],16,0)'
  group: Data Types
- name: Output
  summary: 'Data type of output Inherit: Same as accumulator (default) | Inherit: Same as input | fixdt([],16,0)'
  group: Data Types
- name: Output Minimum
  summary: Minimum value the block can output [] (default) | scalar
  group: Data Types
- name: Output Maximum
  summary: Maximum value block can output [] (default) | scalar
  group: Data Types
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types
```

### Main

### **Sum input along** — Dimension to sum along `Channels (running sum)` (default) | `Columns` | `Rows`

Specify the dimension along which to compute the cumulative
summations. You can choose to sum along `Channels (running
sum)`, `Columns`, or
`Rows`. For more information, see these
sections:

- Computing the Running Sum Along Channels of the Input
- Summing Along Columns
- Summing Along Rows

### **Input processing** — Method to process the input `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block processes the input when computing the running
sum along the channels of the input. You can set this parameter to one
of these options:

- `Columns as channels (frame based)`
  — The block treats each column of the input as a separate
  channel.
- `Elements as channels (sample based)`
  — The block treats each element of the input as a
  separate channel.

#### Dependencies

This parameter is available only when you set the `Sum
input along` parameter to `Channels
(running sum)`.

### **Reset port** — Reset type `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

Determines the reset event that causes the block to reset the sum
along channels. The rate of the input to the `Rst` port must be the same or slower than that of the
input data signal. The sample time of the input to the
**Rst** port must be a positive integer multiple of
the input sample time. For more information, see Resetting the Running Sum.

#### Dependencies

This parameter is available only when you set the `Sum
input along` parameter to `Channels
(running sum)`.

### Data Types

**Note**

Floating-point inheritance takes precedence over the data type settings
defined on this pane. When inputs are floating point, the block ignores these
settings. All internal data types are floating point.

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as one of the following:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see rounding
mode.

### **Saturate on integer overflow** — Saturate for fixed-point operation `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Accumulator** — Data type of accumulator `Inherit: Same as first input` (default) | `fixdt([],16,0)`

**Accumulator** specifies the data type of the output
of an accumulation operation in the Cumulative Sum block.
For illustrations on how to use the accumulator data type in this block,
see Fixed-Point Data Types.

- `Inherit: Same as input` — The
  block specifies the accumulator data type to be the same as the
  input data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. Click the
**Show data type assistant** button.

For more information, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Data type of output `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the Cumulative Sum block. For more information on the
output data type, see Fixed-Point Data Types.

- `Inherit: Same as input` — The
  block specifies the output data type to be the same as the input
  data type.
- `Inherit: Same as accumulator`
  — The block specifies the output data type to be the same
  as the accumulator data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. Click the
**Show data type assistant** button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output Minimum** — Minimum value the block can output `[]` (default) | scalar

Specify the minimum value the block can output. Simulink software uses this minimum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value block can output `[]` (default) | scalar

Specify the maximum value the block can output. Simulink software uses this maximum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.
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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Cumulative sum of channel, column, or row elements

The Cumulative Sum block computes the cumulative sum along the specified dimension of
the input or across time (running sum).
