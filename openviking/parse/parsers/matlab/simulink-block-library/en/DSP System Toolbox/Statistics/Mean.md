---
type: simulink-block
title: 'Mean'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'mean'
documentation_source_path: 'ref/mean.html'
language: en
---

# Mean

## Ports
```yaml
ports:
- name: I
  summary: Data input vector | matrix | *N*-D array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Rst
  summary: Reset port scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Port_1
  summary: Mean value along the specified dimension scalar | vector | matrix | *N*-D array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **I** — Data input vector | matrix | *N*-D array

The block accepts real-valued or complex-valued multichannel and
multidimensional inputs. The input data type must be double precision,
single precision, integer, or fixed point with power-of-two slope and
zero bias.

This port is unnamed until you select the **Running
mean** parameter and set the **Reset
port** parameter to any option other than
`None`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Rst** — Reset port scalar

Specify the reset event that causes the block to reset the running
mean. The sample time of the **Rst** input must be a
positive integer multiple of the input sample time.

#### Dependencies

To enable this port, select the **Running mean**
parameter and set the **Reset port** parameter to
any option other than `None`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Port\_1** — Mean value along the specified dimension scalar | vector | matrix | *N*-D array

The data type of the output matches the data type of the input.

When you do not select the **Running mean**
parameter, the block computes the mean value in each row or column of
the input, or along vectors of a specified dimension of the input. It
can also compute the mean of the entire input at each individual sample
time. Each element in the output array `y` is the mean
value of the corresponding column, row, or entire input. The output
array `y` depends on the setting of the **Find
the mean value over** parameter. Consider a
three-dimensional input signal of size
*M*-by-*N*-by-*P*.
When you set **Find the mean value over** to:

- `Entire input` — The output at
  each sample time is a scalar that contains the mean value of the
  *M*-by-*N*-by-*P*
  input matrix.
- `Each row` — The output at
  each sample time consists of an
  *M*-by-1-by-*P* array,
  where each element contains the mean value of each vector over
  the second dimension of the input. For an
  *M*-by-*N* matrix input,
  the output at each sample time is an *M*-by-1
  column vector.
- `Each column` — The output at
  each sample time consists of a
  1-by-*N*-by-*P* array,
  where each element contains the mean value of each vector over
  the first dimension of the input. For an
  *M*-by-*N* matrix input,
  the output at each sample time is a 1-by-*N*
  row vector.

  In this mode, the block treats length-*M*
  unoriented vector inputs as *M*-by-1 column
  vectors.
- `Specified dimension` — The
  output at each sample time depends on the value of the
  **Dimension** parameter. If you set the
  **Dimension** to `1`, the
  output is the same as when you select `Each
  column`. If you set the
  **Dimension** to `2`, the
  output is the same as when you select `Each
  row`. If you set the
  **Dimension** to `3`, the
  output at each sample time is an
  *M*-by-*N* matrix
  containing the mean value of each vector over the third
  dimension of the input.

When you select **Running mean**, the block tracks
the mean value of each channel in a time sequence of inputs. In this
mode, you must also specify a value for the **Input
processing** parameter.

- `Elements as channels (sample based)`
  — The block treats each element of the input as a
  separate channel. For a three-dimensional input signal of size
  *M*-by-*N*-by-*P*,
  the block outputs an
  *M*-by-*N*-by-*P*
  array. Each element
  *yijk* of the output
  contains the mean value of the element
  *uijk* for all
  inputs since the last reset.

  When a reset event occurs, the running mean
  *yijk* in the
  current frame is reset to the element
  *uijk*.
- `Columns as channels (frame based)`
  — The block treats each column of the input as a separate
  channel. This option does not support an N-dimensional input
  signal, where N > 2. For a two-dimensional input signal of
  size *M*-by-*N*, the block
  outputs an *M*-by-*N* matrix.
  Each element *yij* of
  the output contains the mean of the values in the
  *j*th column of all inputs since the last
  reset, up to and including the element
  *uij* of the
  current input.

  When a reset event occurs, the running mean for each channel
  becomes the mean value of all the samples in the current input
  frame, up to and including the current input sample.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Running mean
  summary: Option to select running mean off (default) | on
  group: Main Tab
- name: Find the mean value over
  summary: Dimension over which the block computes the mean value Each column (default) | Entire input | Each row | Specified
    dimension
  group: Main Tab
- name: Dimension
  summary: Custom dimension 1 (default) | scalar
  group: Main Tab
- name: Input processing
  summary: Method to process the input in running mode Columns as channels (frame based) (default) | Elements as channels
    (sample based)
  group: Main Tab
- name: Reset port
  summary: Reset event None (default) | Rising edge | Falling edge | Either edge | Non-zero sample
  group: Main Tab
- name: Rounding mode
  summary: Method of rounding operation Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator data type Inherit: Same as input (default) | fixdt([],16,0)'
  group: Data Types Tab
- name: Output
  summary: 'Output data type Inherit: Same as accumulator (default) | fixdt([],16,0)'
  group: Data Types Tab
- name: Output Minimum
  summary: Minimum value the block can output [] (default) | scalar
  group: Data Types Tab
- name: Output Maximum
  summary: Maximum value the block can output [] (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Running mean** — Option to select running mean off (default) | on

When you select the **Running mean** parameter, the
block tracks the mean value of each channel in a time sequence of
inputs.

### **Find the mean value over** — Dimension over which the block computes the mean value `Each column` (default) | `Entire input` | `Each row` | `Specified dimension`

- `Each column` — The block
  outputs the mean value over each column.
- `Each row` — The block
  outputs the mean value over each row.
- `Entire input` — The block
  outputs the mean value over the entire input.
- `Specified dimension` —
  The block outputs the mean value over the dimension,
  specified in the **Dimension**
  parameter.

#### Dependencies

To enable this parameter, clear the **Running
mean** parameter.

### **Dimension** — Custom dimension `1` (default) | scalar

Specify the dimension (one-based value) of the input signal over which
the mean is computed. The value of this parameter must be greater than 0
and less than the number of dimensions in the input signal.

#### Dependencies

To enable this parameter, set **Find the mean value
over** to `Specified
dimension`.

### **Input processing** — Method to process the input in running mode `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

- `Columns as channels (frame based)`
  — The block treats each column of the input as a separate
  channel. This option does not support an N-dimensional input
  signal, where N > 2. For a two-dimensional input signal of
  size *M*-by-*N*, the block
  outputs an *M*-by-*N* matrix.
  Each element *yij* of
  the output contains the mean of the values in the
  *j*th column of all inputs since the last
  reset, up to and including the element
  *uij* of the
  current input.

  When a reset event occurs, the running mean for each channel
  becomes the mean value of all the samples in the current input
  frame, up to and including the current input sample.
- `Elements as channels (sample based)`
  — The block treats each element of the input as a
  separate channel. For a three-dimensional input signal of size
  *M*-by-*N*-by-*P*,
  the block outputs an
  *M*-by-*N*-by-*P*
  array. Each element
  *yijk* of the output
  contains the mean value of the element
  *uijk* for all
  inputs since the last reset.

  When a reset event occurs, the running mean
  *yijk* in the
  current frame is reset to the element
  *uijk*.

  **Variable-Size Inputs**

  When your inputs are of variable size, and you select the
  **Running mean** parameter, then:

  - If you set the **Input
    processing** parameter to
    `Elements as channels (sample
    based)`, the state is reset.
  - If you set the **Input
    processing** parameter to
    `Columns as channels (frame
    based)`, then:

    - When the input size difference is in the
      number of channels (number of columns), the state
      is reset.
    - When the input size difference is in the
      length of channels (number of rows), there is no
      reset and the running operation is carried out as
      usual.

#### Dependencies

To enable this parameter, select the **Running
mean** parameter.

### **Reset port** — Reset event `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

The block resets the running mean whenever a reset event is detected
at the optional **Rst** port. The reset sample time
must be a positive integer multiple of the input sample time.

When a reset event occurs while the **Input
processing** parameter is set to `Elements as
channels (sample based)`, the running mean for each
channel is initialized to the value in the corresponding channel of the
current input. Similarly, when the **Input processing**
parameter is set to `Columns as channels (frame
based)`, the running mean for each channel becomes the
mean value of all the samples in the current input frame, up to and
including the current input sample.

Use this parameter to specify the reset event.

- `None` — Disables the
  **Rst** port.
- `Rising edge` — Triggers a
  reset operation when the **Rst** input does one
  of the following:

  - Rises from a negative value to either a positive value
    or zero.
  - Rises from zero to a positive value, where the rise is
    not a continuation of a rise from a negative value to
    zero.
- `Falling edge` — Triggers a
  reset operation when the **Rst** input does one
  of the following:

  - Falls from a positive value to a negative value or
    zero.
  - Falls from zero to a negative value, where the fall is
    not a continuation of a fall from a positive value to
    zero.
- `Either edge` — Triggers a
  reset operation when the **Rst** input is a
  `Rising edge` or
  `Falling edge`.
- `Non-zero sample` — Triggers a
  reset operation at each sample time, when the
  **Rst** input is not zero.

**Note**

When running simulations in the Simulink multitasking mode, reset signals have a one-sample
latency. Therefore, when the block detects a reset event, there is a
one-sample delay at the reset port rate before the block applies the
reset. For more information on latency and the Simulink tasking modes, see Excess Algorithmic Delay (Tasking Latency) and Time-Based Scheduling and Code Generation (Simulink Coder).

#### Dependencies

To enable this parameter, select the **Running
mean** parameter.

### Data Types Tab

**Note**

To use these parameters, the data input must be fixed-point. For all other
inputs, the parameters on the **Data Types** tab are
ignored.

### **Rounding mode** — Method of rounding operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

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

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Accumulator** — Accumulator data type `Inherit: Same as input` (default) | `fixdt([],16,0)`

**Accumulator** specifies the data type of the output
of an accumulation operation in the Mean block. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this
block. You can set this parameter to:

- `Inherit: Same as input` — The
  block specifies the accumulator data type to be the same as the
  input data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Accumulator** data
type by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `fixdt([],16,0)`

**Output** specifies the data type of the output of
the Mean block. See Fixed-Point Data Types for
illustrations depicting the use of the output data type in this block.
You can set it to:

- `Inherit: Same as accumulator`
  — The block specifies the output data type to be the same
  as the accumulator data type.
- `fixdt([],16,0)` — The block
  specifies an autosigned, binary-point, scaled, fixed-point data
  type with a word length of 16 bits and a fraction length of
  0.

Alternatively, you can set the **Output** data type
by using the **Data Type Assistant**. To use the
assistant, click the **Show data type assistant**
button.

For more information on the data type assistant, see Specify Data Types Using Data Type Assistant (Simulink).

### **Output Minimum** — Minimum value the block can output `[]` (default) | scalar

Specify the minimum value that the block can output. The default value
is `[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Output Maximum** — Maximum value the block can output `[]` (default) | scalar

Specify the maximum value that the block can output. The default value
is `[]` (unspecified). Simulink uses this value to perform:

- Simulation range checking. See Specify Signal Ranges (Simulink).
- Automatic scaling of fixed-point data types.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types off (default) | on

Select this parameter to prevent the fixed-point tools from overriding
the data types you specify on the block.
## Libraries

DSP System Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Find mean value of input or sequence of inputs

The Mean block computes the mean of each row or column of the input, or
along vectors of a specified dimension of the input. It can also compute the mean of the
entire input. You can specify the dimension using the **Find the mean value
over** parameter. The Mean block can also track the mean
value in a sequence of inputs over a period of time. To track the mean value in a
sequence of inputs, select the **Running mean** parameter.

**Note**

The **Running** mode in the Mean block
will be removed in a future release. To compute the running mean in Simulink®, use the Moving Average block instead.
