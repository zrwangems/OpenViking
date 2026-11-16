---
type: simulink-block
title: 'Two-Channel Synthesis Subband Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Multirate and Multistage Filters / Filter Bank'
documentation_page: 'twochannelsynthesissubbandfilter'
documentation_source_path: 'ref/twochannelsynthesissubbandfilter.html'
language: en
---

# Two-Channel Synthesis Subband Filter

## Ports

### Input

### **Hi band** — High-frequency subband vector | matrix

Specify the high-frequency subband as a vector or a matrix. Both the high-frequency
subband and the low-frequency subbands must have the same size and data
type.

When the input is fixed-point, it must be signed
only.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **Lo band** — Low-frequency subband vector | matrix

Specify the low-frequency subband as a vector or a matrix. Both the high-frequency
subband and the low-frequency subbands must have the same size and data
type.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output 1** — Synthesized output vector | matrix

The block returns the synthesized output as a vector or a matrix. The number of rows in
the output is the sum of the number of rows of the input signals.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Lowpass FIR filter coefficients** — Lowpass FIR filter coefficients `[0.3327 0.8069 0.4599 -0.1350 -0.0854 0.0352]` (default)

A vector of lowpass FIR filter coefficients, in descending powers of
*z*. The lowpass filter should be a half-band
filter that passes the frequency band stopped by the filter specified in
the **Highpass FIR filter coefficients** parameter. To
use this block to reconstruct the output of a Two-Channel Analysis Subband
Filter block, you must design the filters in this block to
perfectly reconstruct the outputs of the analysis filters. For more
information, see Specify FIR Filters.

### **Highpass FIR filter coefficients** — Highpass FIR filter coefficients `[0.0352 0.0854 -0.1350 -0.4599 0.8069 -0.3327]` (default)

A vector of highpass FIR filter coefficients, in descending powers of
*z*. The highpass filter should be a half-band
filter that passes the frequency band stopped by the filter specified in
the **Lowpass FIR filter coefficients** parameter. To
use this block to reconstruct the output of a Two-Channel Analysis Subband
Filter block, you must design the filters in this block to
perfectly reconstruct the outputs of the analysis filters. For more
information, see Specify FIR Filters.

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
  column of the input as an independent channel and reconstructs
  each channel over time. The output has the same sample rate as
  the input, but the output frame size is twice that of the input
  frame size. To select this option, you must set the
  **Input processing** parameter to
  `Columns as channels (frame
  based)`.
- `Allow multirate processing` —
  When you select this option, the input and output of the block
  are the same size, but the sample rate of the output is twice
  that of the input.

Some settings of this parameter cause the block to have nonzero
latency. See Latency for more information.

### Data Types Tab

### **Rounding mode** — Rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode for fixed-point operations. The filter coefficients do
not obey this parameter; they always round to
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

See Control Data Types of Signals (Simulink) for more
information.

### **Output Minimum** — Output Minimum `[]` (default) | scalar

Specify the minimum value that the block should output. The default
value is `[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Output Maximum** — Output Maximum `[]` (default) | scalar

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

## Description

Reconstruct signal from high-frequency and low-frequency subbands

The Two-Channel Synthesis Subband Filter block reconstructs a signal from its
high-frequency and low-frequency subbands, each with half the bandwidth and half the
sample rate of the original signal. Use this block to reconstruct signals decomposed by
the Two-Channel Analysis Subband Filter
block.

The block upsamples the high- and low-frequency subbands by 2, and then filters the results
with a pair of highpass and lowpass FIR filters, as shown in this figure.

The block implements the FIR filtering and downsampling steps together using a polyphase
filter structure, which is more efficient than the interpolate-then-filter algorithm
shown in the preceding figure. You can implement a multilevel dyadic synthesis filter
bank by connecting multiple copies of this block or by using the Dyadic Synthesis Filter Bank block. For more information, see Creating Multilevel Dyadic Synthesis Filter Banks.

You must provide a vector of filter coefficients for the lowpass and highpass FIR filters.
Each filter should be a half-band filter that passes the frequency band that the other filter
stops. You can use this block to reconstruct the output of a Two-Channel Analysis Subband Filter block. To do so, you must design the filters in this block such that they perfectly reconstruct the outputs of the analysis filters.
