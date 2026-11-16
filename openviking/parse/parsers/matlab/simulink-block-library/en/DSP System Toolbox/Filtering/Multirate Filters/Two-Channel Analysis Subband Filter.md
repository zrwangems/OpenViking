---
type: simulink-block
title: 'Two-Channel Analysis Subband Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'twochannelanalysissubbandfilter'
documentation_source_path: 'ref/twochannelanalysissubbandfilter.html'
language: en
---

# Two-Channel Analysis Subband Filter

## Ports

### Input

### **Input 1** — Data input column vector | matrix

Specify the data input as a column vector or a matrix of size
*M*-by-*N*. The columns in the
input signal represent *N* independent channels.

The block supports variable-size input signals (frame length changes during simulation)
when you set **Input processing** to
`Columns as channels (frame based)` and
**Rate options** to `Enforce
single-rate processing`. When you specify variable-size
input signals, they can be of arbitrary frame length, that is, the input
frame length does not have to be even. When you specify fixed-size
signals, the frame length can be arbitrary under certain conditions. For
more details, see Frame-Based Processing and Sample-Based Processing.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **Hi band** — High-frequency subband column vector | matrix

The block outputs the high-frequency subband as a column vector or a matrix.

When you set **Rate options** to:

- `Enforce single-rate processing`
  –– The block maintains the input sample rate and decimates
  the signal by decreasing the output frame size by a factor
  of 2.

  The output has an upper bound size of
  `ceil`(*M*/2)-by-*N*
  for an input of size
  *M*-by-*N*.
- `Allow multirate processing` ––
  The block decimates the signal such that the output sample
  rate is half the input sample rate.

  The output frame size is the same as the input frame
  size.

For more details, see Frame-Based Processing and Sample-Based Processing.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Lo band** — Low-frequency subband column vector | matrix

The block outputs the low-frequency subband as a column vector or a matrix.

When you set **Rate options** to:

- `Enforce single-rate processing`
  –– The block maintains the input sample rate and decimates
  the signal by decreasing the output frame size by a factor
  of 2.

  The output has an upper bound size of
  `ceil`(*M*/2)-by-*N*
  for an input of size
  *M*-by-*N*.
- `Allow multirate processing` ––
  The block decimates the signal such that the output sample
  rate is half the input sample rate.

  The output frame size is the same as the input frame
  size.

For more details, see Frame-Based Processing and Sample-Based Processing.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## Parameters

### Main Tab

### **Lowpass FIR filter coefficients** — Lowpass FIR filter coefficients `[0.0352 -0.0854 -0.1350 0.4599 0.8069 0.3327]` (default) | row vector

Specify a vector of lowpass FIR filter coefficients, in descending
powers of *z*. The lowpass filter should be a
half-band filter that passes the frequency band stopped by the filter
specified in the **Highpass FIR filter coefficients**
parameter. The default values of this parameter specify a filter based
on a third-order Daubechies wavelet. When you use the Two-Channel Synthesis Subband
Filter block to reconstruct the input to this block, you
need to design perfect reconstruction filters to use in the synthesis
subband filter. For more information, see Specify FIR Filters.

### **Highpass FIR filter coefficients** — Highpass FIR filter coefficients `[-0.3327 0.8069 -0.4599 -0.1350 0.0854 0.0352]` (default) | row vector

Specify a vector of highpass FIR filter coefficients, in descending
powers of *z*. The highpass filter should be a
half-band filter that passes the frequency band stopped by the filter
specified in the **Lowpass FIR filter coefficients**
parameter. The default values of this parameter specify a filter based
on a third-order Daubechies wavelet. When you use the Two-Channel Synthesis Subband
Filter block to reconstruct the input to this block, you
need to design perfect reconstruction filters to use in the synthesis
subband filter. For more information, see Specify FIR Filters.

### **Input processing** — Input processing `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. You can set this
parameter to one of the following options:

- `Columns as channels (frame based)`
  (default) — When you select this option, the block treats each
  column of the input as a separate channel.
- `Elements as channels (sample based)`
  — When you select this option, the block treats each element of
  the input as a separate channel.

For more information, see Frame-Based Processing and Sample-Based Processing.

### **Rate options** — Rate options `Enforce single-rate processing` (default) | `Allow multirate processing`

Specify the rate processing rule for the block. You can set this
parameter to one of the following options:

- `Enforce single-rate processing`
  — When you select this option, the block treats each
  column of the input as an independent channel and decomposes
  each channel over time. The output has the same sample rate as
  the input, but the output frame size is half that of the input
  frame size. To select this option, you must set the
  **Input processing** parameter to
  `Columns as channels (frame
  based)`.
- `Allow multirate processing` —
  When you select this option, the input and output of the block
  are the same size, but the sample rate of the output is half
  that of the input.

Some settings of this parameter cause the block to have nonzero
latency. See Latency for more information.

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals `off` (default) | `on`

*Since R2023a*

Specify whether fixed-size input signals (whose size does not change during simulation)
can have an arbitrary frame length, where the frame length does not have
to be even. The block uses this parameter only for fixed-size input
signals and ignores it if the input has a variable-size.

When the input signal is a variable-size signal, the signal can have an arbitrary frame
length, that is, the frame length does not have to be an even
number.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be even. The output is
  a variable-size signal.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be even.

#### Dependency

To enable this parameter, set **Input
processing** to `Columns as channels (frame
based)` and **Rate options** to
`Enforce single-rate
processing`.

### Data Types Tab

### **Rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode for fixed-point operations. The filter coefficients do
not obey this parameter; they are always rounded to
`Nearest`.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** settings have no effect on numerical
results when all the following conditions exist:

- **Product output** is
  `Inherit: Inherit via internal
  rule`
- **Accumulator** is
  `Inherit: Inherit via internal
  rule`
- **Output** is `Inherit:
  Same as accumulator`

With these data type settings, the block effectively operates in
full-precision mode.

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

**Note**

The **Rounding mode** and **Saturate on
integer overflow** parameters have no effect on numeric
results when all these conditions are met:

- **Product output** data type is
  `Inherit: Inherit via internal
  rule`.
- **Accumulator** data type is
  `Inherit: Inherit via internal
  rule`.

With these data type settings, the block operates in
full-precision mode.

### **Coefficients** — Data type of the coefficients `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `fixdt(1,16,0)`

Specify the coefficients data type. See Fixed-Point Data Types and Multiplication Data Types for
illustrations depicting the use of the coefficients data type in this
block. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same word length as
  input`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Coefficients** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Coefficients Minimum** — Minimum value of filter coefficients `[]` (default) | scalar

Specify the minimum value of the filter coefficients. The default value is
`[]` (unspecified). Simulink® software uses this value to perform automatic scaling of
fixed-point data types.

### **Coefficients Maximum** — Maximum value of filter coefficients `[]` (default) | scalar

Specify the maximum value of the filter coefficients. The default value is
`[]` (unspecified). Simulink software uses this value to perform automatic scaling of
fixed-point data types.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

Specify the product output data type. See Fixed-Point Data Types and Multiplication Data Types for
illustrations depicting the use of the product output data type in this
block. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.

  **Note**

  The actual product output word length can be equal to or
  greater than the calculated ideal product output word
  length, depending on the settings on the
  **Hardware Implementation** pane
  of the Configuration Parameters dialog box.
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Accumulator** — Data type of accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the accumulator data type. See Fixed-Point Data Types for
illustrations depicting the use of the accumulator data type in this
block. You can set this parameter to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Output** — Data type of output `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the output data type. See Fixed-Point Data Types for
illustrations depicting the use of the output data type in this block.
You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Output** parameter.

See Control Data Types of Signals (Simulink) for more information.

### **Output Minimum** — Output minimum `[]` (default) | scalar

Specify the minimum value that the block should output. The default
value is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Output Maximum** — Output maximum `[]` (default) | scalar

Specify the maximum value that the block should output. The default
value is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

## Libraries

DSP System Toolbox / Filtering / Multirate Filters

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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023a: Support for arbitrary input frame length

This block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and the block allows for multirate processing.
- Input signal is a fixed-size signal, the block enforces single-rate
  processing, and you select the **Allow arbitrary frame length
  for fixed-size input signals** parameter.
- Input signal is a variable-size signal (frame length changes during
  simulation).

When this block supports an input signal with an arbitrary frame length, the input frame
length does not have to be even.

For more details, see Frame-Based Processing and Sample-Based Processing.

## Description

Decompose signal into high-frequency and low-frequency subbands

The Two-Channel Analysis Subband Filter block decomposes the input into
high-frequency and low-frequency subbands, each with half the bandwidth and half the
sample rate of the input.

The block filters the input with a pair of highpass and lowpass FIR filters, and then
downsamples the results by 2, as shown in this figure.

The block implements the FIR filtering and downsampling steps together using a polyphase
filter structure, which is more efficient than the filter-then-decimate algorithm shown
in the preceding figure. Each subband is the first phase of the respective polyphase
filter. You can implement a multilevel dyadic analysis filter bank by connecting
multiple copies of this block or by using the Dyadic Analysis Filter Bank block. See Creating Multilevel Dyadic Analysis Filter Banks for more
information.

You must provide a vector of filter coefficients for the lowpass and highpass FIR filters. Each filter should be a half-band filter that passes the frequency band that the other filter stops.
