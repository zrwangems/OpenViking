---
type: simulink-block
title: 'Convolution'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'convolution'
documentation_source_path: 'ref/convolution.html'
language: en
---

# Convolution

## Ports
```yaml
ports:
- name: Port_1
  summary: First input signal scalar | vector | matrix | *N*-*D* array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_2
  summary: Second input signal scalar | vector | matrix | *N*-D array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Output signal scalar | vector | matrix | *N*-*D* array
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **Port\_1** — First input signal scalar | vector | matrix | *N*-*D* array

First input *u* specified as a scalar, vector,
matrix, or *N*-*D* array. When both
inputs are real, the output is real. When one or both inputs are
complex, the output is complex. All the input port dimensions for both
the inputs, except the first dimension, must have the same value.

Inputs *u* and *v* are zero when
indexed outside their valid ranges.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

### **Port\_2** — Second input signal scalar | vector | matrix | *N*-D array

Second input *v* specified as a scalar, vector,
matrix, or *N*-D array. When both inputs are real, the
output is real. When one or both inputs are complex, the output is
complex. All the input port dimensions for both the inputs, except the
first dimension, must have the same value.

Inputs *u* and *v* are zero when
indexed outside their valid ranges.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal scalar | vector | matrix | *N*-*D* array

Convolved signal, returned as a scalar, vector, matrix, or
*N*-*D* array depending on the
input signals. When both inputs are real, the output is real. When one
or both inputs are complex, the output is complex. Inputs
*u* and *v* are zero when indexed
outside of their valid ranges. For more details on how the convolved
signal changes based on the inputs, see More About.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Computation domain
  summary: Computation domain Time (default) | Frequency | Fastest
  group: Main Tab
- name: Rounding mode
  summary: Method of rounding operation Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types Tab
- name: Product output
  summary: 'Product output data type Inherit: Inherit via internal rule (default) | Inherit: Same as first input | fixdt([],16,0)'
  group: Data Types Tab
- name: Accumulator
  summary: 'Data type of accumulator Inherit: Inherit via internal rule (default) | Inherit: Same as first input | Inherit:
    Same as product output | fixdt([],16,0)'
  group: Data Types Tab
- name: Output
  summary: 'Data type of output Inherit: Same as accumulator (default) | Inherit: Same as input | Inherit: Same as product
    output | fixdt([],16,0)'
  group: Data Types Tab
- name: Output Minimum
  summary: Minimum value that block can output [] (default) | scalar
  group: Data Types Tab
- name: Output Maximum
  summary: Maximum value that block can output [] (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Computation domain** — Computation domain `Time` (default) | `Frequency` | `Fastest`

Set the domain in which the block computes convolutions:

- `Time` — The block computes in
  the time domain, which minimizes memory use.
- `Frequency` — The block
  computes in the frequency domain, which might require fewer
  computations than computing in the time domain, depending on the
  input length.
- `Fastest` — The block computes
  in the domain that minimizes the number of computations.

Fixed-point signals are only supported in the time domain. When
inputting fixed-point signals, make sure you set the
**Computation domain** parameter to
`Time`.

### Data Types Tab

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as one of the following:

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

For more details, see Rounding
Modes.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on
numerical results when all these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.
- **Output** data type is
  `Inherit: Same as
  accumulator`.

With these data-type settings, the block operates in a
full-precision mode.

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
*saturate* and *wrap*, see
Overflow
Handing for fixed-point operations.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on
numerical results when all these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.
- **Output** data type is
  `Inherit: Same as
  accumulator`.

With these data-type settings, the block operates in a
full-precision mode.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `fixdt([],16,0)`

**Product output** specifies the data type of the
output of a product operation in the Convolution
block.

- `Inherit: Inherit via internal rule`
  — The block inherits the product output data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- `Inherit: Same as first input`
  — The block specifies the product output data type to be
  the same as the first input data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Product output**
data type by using the **Data Type Assistant**. To use
the assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

For more information on the product output data type, see Multiplication Data Types and
Fixed-Point Data Types.

### **Accumulator** — Data type of accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Accumulator** specifies the data type of the output
of an accumulation operation in the Convolution block.

- `Inherit: Inherit via internal rule`
  — The block inherits the accumulator data type based on
  an internal rule. For more information on this rule, see Inherit via Internal Rule.
- `Inherit: Same as first input`
  — The block specifies the accumulator data type to be the
  same as the first input data type.
- `Inherit: Same as product output`
  — The block specifies the accumulator data type to be the
  same as the product output data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

For a diagrammatic representation on how to use the accumulator data
type in this block, see Fixed-Point Data Types.

### **Output** — Data type of output `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the Convolution block.

- `Inherit: Same as accumulator`
  — The block specifies the output data type to be the same
  as the accumulator data type.
- `Inherit: Same as first input`
  — The block specifies the output data type to be the same
  as the first input data type.
- `Inherit: Same as product output`
  — The block specifies the output data type to be the same
  as the product output data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information, see Control Data Types of Signals (Simulink).

For more information on the output data type, see Fixed-Point Data Types.

### **Output Minimum** — Minimum value that block can output `[]` (default) | scalar

Specify the minimum value the block can output. Simulink uses this minimum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value that block can output `[]` (default) | scalar

Specify the maximum value the block can output. Simulink uses this maximum value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.
## Libraries

DSP System Toolbox / Signal Operations

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

## Description

Convolution of two inputs

The Convolution block convolves the first dimension of an
*N*-D input array *u* with the first dimension of
an N-D input array *v*. The block can also convolve a column vector
with the first-dimension of an N-D input array.

The general equation for convolution is:

y(k)=∑nu(n−k)v(k)

Two DSP System Toolbox™ blocks can be used for convolving two input signals:

- Convolution
- Discrete FIR Filter (Simulink)

The Convolution block assumes that all elements of *u*
and *v* are available at each Simulink® time step and computes the entire convolution at every step.

The Discrete FIR Filter block can be used for convolving signals in situations where
all elements of *v* is available at each time step, but
*u* is a sequence that comes in over the life of the simulation.
When you use the Discrete FIR Filter block, the convolution is computed only
once.

To determine which block best fits your needs, see Selecting the Appropriate Convolution Block.
