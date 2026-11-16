---
type: simulink-block
title: 'Variable Fractional Delay'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Operations / Delay'
documentation_page: 'variablefractionaldelay'
documentation_source_path: 'ref/variablefractionaldelay.html'
language: en
---

# Variable Fractional Delay

## Ports

### Input

### **In** — Data input vector | matrix

Specify the data input as a vector or matrix. The data input must have
the same data type as the delay input.

This block supports variable-size input signal. That is, you can
change the number of input rows during the simulation. However, the
number of channels must remain constant.

**Example:** [1 2 3 4;5 1 4 2;2 6 2 3;1 2 3 2;3 4 5 6;1 2 3
1]

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Delay** — Delay input scalar | vector | matrix | *N*-D array

Specify the delay input in samples as a scalar, vector, matrix, or
*N*-D array. The delay can be an integer or a
fractional value. The block interpolates the signal to obtain new
samples at noninteger sampling intervals. The delay input must have the
same data type as the data input.

The block dialog box displays the valid delay range in samples. The
block determines this range based on the settings in the block dialog
box. If you specify a delay value that is less than the minimum
acceptable value, the block performs the action you choose in the
**For small input delay values** parameter. If you
set the **Interpolation mode** to
`Linear`, the minimum acceptable value is
0.

If you specify a delay value that is greater than the maximum
acceptable value, the block clips the delay value to the maximum
value.

This block supports variable-size delay signal. That is, you can
change one or both of the dimensions of the delay signal during
simulation. However, the block must make sure that the resulting number
of output channels remains constant throughout the simulation.

When the **Input processing** parameter is set to
`Columns as channels (frame based)`, the
table below shows the effect of the dimension of the delay input on the
data input. For an example, see Delay Signal Using Multitap Fractional Delay.

| Data Input | Delay Input | Output | Effect of Delay Input on Data Input |
| --- | --- | --- | --- |
| *N* (unoriented, one channel) | scalar | Unoriented (N) | One delay value applied to the input channel |
| *N* (unoriented, one channel) | Unoriented (N) | Unoriented (N) | Delay value varies within the frame from sample to sample |
| *N* (unoriented, one channel) | 1-by-*P* | *N*-by-*P* | *P* taps. Each column in the output is a delayed version of the input. The delay value is specified by the corresponding element in the delay input vector. |
| *N* (unoriented, one channel) | *N*-by-*P* | *N*-by-*P* | *P* taps. In addition, delay varies within each frame from sample to sample. |
| *N*-by-1 (one channel with frame size equal to *N*) | scalar | *N*-by-1 | One delay value applied to the input channel |
| *N*-by-1 (one channel with frame size equal to *N*) | Unoriented (N) | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | *N*-by-1 | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | 1-by-*P* | *N*-by-*P* | *P* taps. Each column in the output is a delayed version of the input. The delay value is specified by the corresponding element in the delay input vector. |
| *N*-by-1 (one channel with frame size equal to *N*) | *N*-by-*P* | *N*-by-*P* | *P* taps. In addition, delay varies within each frame from sample to sample. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | scalar | *N*-by-*L* | One delay value applied to all input channels |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | 1-by-*L* | *N*-by-*L* | Unique delay value for each input channel |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-1 | *N*-by-*L* | Delay value varies within the frame from sample to sample. Same set of delay values for all channels. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-*L* | *N*-by-*L* | Delay value varies within the frame from sample to sample. Different delay values for each input channel. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | 1-by-1-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Same delay for all channels. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | 1-by-*L*-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Taps vary across channels. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-1-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Delay varies within the frame from sample to sample. Same set of delay values for each channel. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-*L*-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Delay varies within the frame from sample to sample. Different set of delay values for each channel. |

When the **Input processing** parameter is set to
`Elements as channels (sample based)`, the
table below shows the effect of the dimension of the delay input on the
data input.

| Data Input | Delay Input | Output | Effect of Delay Input on Data Input |
| --- | --- | --- | --- |
| *N* (unoriented, one channel) | scalar | Unoriented (N) | One delay value applied to the input channel |
| *N* (unoriented, one channel) | Unoriented (N) | Unoriented (N) | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | scalar | *N*-by-1 | One delay value applied to the input channel |
| *N*-by-1 (one channel with frame size equal to *N*) | Unoriented (N) | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | *N*-by-1 | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | scalar | *N*-by-*L* | One delay value applied to all input channels |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | 1-by-*L* | *N*-by-*L* | Unique delay value for each input channel |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | *N*-by-1 | *N*-by-*L* | Delay value varies within the frame from sample to sample. Same set of delay values for all channels. |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | *N*-by-*L* | *N*-by-*L* | Delay value varies within the frame from sample to sample. Different delay values for each input channel. |

**Example:** [2 3 4 5]

**Example:** [2.5]

**Example:** [5.6]

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Delayed output vector | matrix

Delayed output, returned as a vector or matrix. The data type and
complexity of the output match the data type and complexity of the data
input.

When the **Input processing** parameter is set to
`Columns as channels (frame based)`, the
table below shows the effect of the dimension of the delay input on the
data input.

| Data Input | Delay Input | Output | Effect of Delay Input on Data Input |
| --- | --- | --- | --- |
| *N* (unoriented, one channel) | scalar | Unoriented (N) | One delay value applied to the input channel |
| *N* (unoriented, one channel) | Unoriented (N) | Unoriented (N) | Delay value varies within the frame from sample to sample |
| *N* (unoriented, one channel) | 1-by-*P* | *N*-by-*P* | *P* taps. Each column in the output is a delayed version of the input. The delay value is specified by the corresponding element in the delay input vector. |
| *N* (unoriented, one channel) | *N*-by-*P* | *N*-by-*P* | *P* taps. In addition, delay varies within each frame from sample to sample. |
| *N*-by-1 (one channel with frame size equal to *N*) | scalar | *N*-by-1 | One delay value applied to the input channel |
| *N*-by-1 (one channel with frame size equal to *N*) | Unoriented (N) | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | *N*-by-1 | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | 1-by-*P* | *N*-by-*P* | *P* taps. Each column in the output is a delayed version of the input. The delay value is specified by the corresponding element in the delay input vector. |
| *N*-by-1 (one channel with frame size equal to *N*) | *N*-by-*P* | *N*-by-*P* | *P* taps. In addition, delay varies within each frame from sample to sample. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | scalar | *N*-by-*L* | One delay value applied to all input channels |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | 1-by-*L* | *N*-by-*L* | Unique delay value for each input channel |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-1 | *N*-by-*L* | Delay value varies within the frame from sample to sample. Same set of delay values for all channels. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-*L* | *N*-by-*L* | Delay value varies within the frame from sample to sample. Different delay values for each input channel. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | 1-by-1-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Same delay for all channels. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | 1-by-*L*-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Taps vary across channels. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-1-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Delay varies within the frame from sample to sample. Same set of delay values for each channel. |
| *N*-by-*L* (*L* channels with frame size equal to *N*) | *N*-by-*L*-by-*P* | *N*-by-*L*-by-*P* | *L* channels. *P* taps per channel. Delay varies within the frame from sample to sample. Different set of delay values for each channel. |

When the **Input processing** parameter is set to
`Elements as channels (sample based)`, the
table below shows the effect of the dimension of the delay input on the
data input.

| Data Input | Delay Input | Output | Effect of Delay Input on Data Input |
| --- | --- | --- | --- |
| *N* (unoriented, one channel) | scalar | Unoriented (N) | One delay value applied to the input channel |
| *N* (unoriented, one channel) | Unoriented (N) | Unoriented (N) | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | scalar | *N*-by-1 | One delay value applied to the input channel |
| *N*-by-1 (one channel with frame size equal to *N*) | Unoriented (N) | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-1 (one channel with frame size equal to *N*) | *N*-by-1 | *N*-by-1 | Delay value varies within the frame from sample to sample |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | scalar | *N*-by-*L* | One delay value applied to all input channels |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | 1-by-*L* | *N*-by-*L* | Unique delay value for each input channel |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | *N*-by-1 | *N*-by-*L* | Delay value varies within the frame from sample to sample. Same set of delay values for all channels. |
| *N*-by-*L* (*L* channels with *N* samples in each channel) | *N*-by-*L* | *N*-by-*L* | Delay value varies within the frame from sample to sample. Different delay values for each input channel. |

**Example:** [0 0 0 0;0 0 0 0;1 0 0 0;5 2 0 0;2 1 3 0;1 6 4
4]

**Example:** [0 0 0 0;0 0 0 0;0.5 1.0 1.5 2.0;3 1.5 3.5 3.0;3.5 3.5 3.0
2.5;1.5 4.0 2.5 2.5]

**Example:** [0 0 0 0;0 0 0 0;0 0 0 0;0 0 0 0;0 0 0 0;0.4 0.8 1.2
1.6]

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Interpolation mode** — Method of interpolation `Linear` (default) | `FIR` | `Farrow`

Specify the method of interpolation. Using this method, the block
interpolates the signal to obtain new samples at noninteger sampling
intervals.

- `Linear` –– Linear interpolation. In
  this mode, the block stores the
  **Dmax**+1 most
  recent samples the **In** port receives for
  each channel. **Dmax**
  is the value you specify in the **Maximum delay (Dmax)
  in samples** parameter.
- `FIR` –– Polyphase FIR interpolation.
  In this mode, the block stores the
  **Dmax**+**P**+1
  most recent samples the **In** port receives
  for each channel. **P** is the value you
  specify in the **Interpolation filter half-length
  (P)** parameter.
- `Farrow` –– LaGrange method. In this
  mode, the block stores the
  **Dmax**+N2+1 most recent samples the
  **In** port receives for each channel.
  **N** is the value you specify in the
  **Farrow filter length (N)**
  parameter.

For more details on these methods, see Algorithms.

### **Interpolation filter half-length (P)** — Half length of interpolation filter `4` (default) | positive integer in the range [1 65535]

Half-length of the FIR interpolation filter. For periodic signals, a
larger value of this property, which indicates a higher order filter, yields
a better estimate of the delayed output sample. A property value of 4 to 6,
which corresponds to a 7th-order to 11th-order filter, is usually
adequate.

**Example:** `6`

**Example:** `10`

#### Dependencies

This parameter applies only when you set **Interpolation
mode** to `FIR`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Interpolation points per input sample** — Number of interpolation points per input sample `10` (default) | positive integer in the range [2, 65,535]

Number of interpolation points per input sample at which a unique FIR
interpolation filter is computed.

**Example:** `20`

**Example:** `5`

#### Dependencies

This parameter applies only when you set **Interpolation
mode** to `FIR`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Normalized input bandwidth (0 to 1)** — Normalized input bandwidth `1` (default) | real scalar in the range (0, 1]

Normalized input bandwidth at which to constrain the interpolated output
samples. A value of `1` equals the Nyquist frequency, or
half the sampling frequency, *Fs*. Use this property to
take advantage of the bandlimited frequency content of the input. For
example, if the input signal does not have frequency content above
*Fs*/4, you can specify a value of
`0.5`.

**Example:** `0.5`

**Example:** `0.8`

#### Dependencies

This parameter applies only when you set **Interpolation
mode** to `FIR`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Farrow filter length (N)** — Length of Farrow filter `4` (default) | integer greater than or equal to 2

Length of the FIR filter implemented using the Farrow structure. If the
length equals 2, the filter performs linear interpolation.

**Example:** `4`

**Example:** `10`

#### Dependencies

This parameter applies only when you set **Interpolation
mode** to `Farrow`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Maximum delay (Dmax) in samples** — Maximum delay `100` (default) | integer in the range [0 65535]

Maximum delay the block can produce,
**Dmax**. Input delay values
exceeding this maximum are clipped to
**Dmax**.

**Example:** 200

**Example:** 500

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Input processing** — Method to process the input `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input. You can set this parameter
to one of the following options:

- `Columns as channels (frame based)`
  (default) — When you select this option, the block treats
  each column of the input as a separate channel. The block treats
  each of the *R* input columns as independent
  channels containing *Mi*
  sequential time samples.

  The input to the **Delay** port,
  *v*, contains floating-point values that
  specify the number of sample intervals to delay the current
  input.

  The input to the **Delay** port can be a scalar
  value to uniformly delay every sample in every channel. It can also
  be a length-*M* column vector, containing one delay
  for each sample in the input frame. The block applies the set of
  delays contained in the vector identically to every channel of a
  multichannel input. The **Delay** port entry can
  also be a length-*R* row vector, containing one
  delay for each channel. Finally, the **Delay** port
  entry can be an *M*-by-*R* matrix,
  containing a different delay for each corresponding element of the
  input.

  For example, if *v* is the
  *Mi*-by-1 matrix
  `[v(1) v(2) ... v(Mi)]'`, the earliest sample
  in the current frame is delayed by `v(1)`
  fractional sample intervals, the following sample in the frame is
  delayed by `v(2)` fractional sample intervals, and
  so on. The block applies the set of fractional delays contained in
  *v* identically to every channel of a
  multichannel input.
- `Elements as channels (sample based)` ––
  When you select this option, the block treats each element of the
  input as a separate channel. The block treats each element of the
  N-D input array, *u*, as an independent channel.
  The input to the **Delay** port,
  *v*, must either be an N-D array of the same
  size and dimension as the input *u*, or be a scalar
  value, such that *Dmin* ≤
  *v* ≤
  *Dmax*.

  For example, consider an
  *M*-by-*R* input matrix. The
  block treats each of the *M*\**R*
  matrix elements as independent channels. The input to the
  **Delay** port can be an
  *M*-by-*R* matrix of
  floating-point values in the range *Dmin* ≤
  *v* ≤
  *Dmax* that specifies the number of sample intervals to
  delay each channel of the input, or it can be a scalar
  floating-point value, *Dmin* ≤
  *v* ≤
  *Dmax*, by which to equally delay all channels.

  In sample-based processing mode, the block treats an unoriented
  vector input as an *M*-by-1 matrix. In this mode,
  the output is also an unoriented vector.

### **InitialConditions** — Initial values in the memory `0` (default) | scalar | 1-by-*R*-by-*D* array | 1-by-*R*-by-(*D+L*) array

Specify the values with in the block's memory at the start of the
simulation. The dimensions of this parameter can vary depending on whether
you want fixed or time-varying initial conditions. The block treats each of
the *R* input columns as a frame containing
*M* sequential time samples from an independent
channel.

For an *M*-by-*R* input matrix,
*u*, you can set this parameter as follows:

- To specify fixed initial conditions, set this parameter to a
  scalar value. The block initializes every sample of every
  channel in memory using the value you specify.
- The dimensions you specify for time-varying initial
  conditions depend on the interpolation method. To specify
  different time-varying initial conditions for each channel, set
  this parameter as follows:

  - If you set the **Interpolation mode**
    to `Linear`, set the
    **Initial conditions** to an array
    of size
    `1`-by-*R*-by-*D*,
    where *D* is the value in
    **Maximum delay (Dmax) in samples**
    parameter.
  - If you set the **Interpolation mode**
    to `FIR` or
    `Farrow`, set the
    **Initial conditions** to an array
    of size
    1-by-*R*-by-(*D*+*L*),
    where *D* is the value of the maximum
    delay. For FIR interpolation, `L` is
    the value of the interpolation filter half length. For
    Farrow interpolation, `L` equals
    `floor` of half the value of the
    farrow filter length (`floor( farrow filter
    length/2)`).

**Example:** `1`

**Example:** randn(1,3,104)

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Disable direct feedthrough by increasing minimum possible delay by one** — Disable direct feedthrough `off` (default) | `on`

Select this box to disable direct feedthrough by increasing the minimum
possible delay value. When you set the **Input processing**
parameter to `Columns as channels (frame based)`,
the block increases the minimum possible delay value by *`frame
size`*  – 1. Similarly, when you set the
**Input processing** parameter to `Elements
as channels (sample based)`, the block increases the
minimum possible delay value by one sample.

Checking this box allows you to use the Variable Fractional
Delay block in feedback loops.

### **For small input delay values** — Action to take for small input delay values `Clip to the minimum value necessary for centered kernel` (default) | `Use off-centered kernel` | `Switch to linear interpolation if kernel cannot be centered`

Specify the block's behavior when the input delay values are too small to
center the kernel.

You can specify how the block handles input delay values that are too
small for the kernel to be centered using one of the following
choices:

- In both `FIR` and
  `Farrow` interpolation modes, you can
  select `Clip to the minimum value necessary for centered
  kernel`. This option forces the block to increase
  *Dmin* to the
  smallest value necessary to keep the kernel centered.
- In `FIR` interpolation mode, you can
  select `Switch to linear interpolation if kernel cannot
  be centered`. This option forces the block to
  preserve the value of *Dmin*
  and compute all interpolated values using
  `Linear` interpolation.
- In `Farrow` interpolation mode, you can
  select `Use off-centered kernel`. This
  option forces the block to preserve the value of
  *Dmin* and compute
  the interpolated values using a farrow filter with an off-centered
  kernel.

#### Dependencies

This parameter applies only when **Interpolation
mode** is set to `FIR` or
`Farrow`.

### **Valid delay range (in samples)** — Range of valid delay values Read-only: [0 100] (default) | [*Dmin* *Dmax*]

This parameter is read-only.

The delay range values [*Dmin*
*Dmax*] are calculated (in samples)
by the block based on the current parameter settings.
*Dmin* is the smallest
possible valid delay value (in samples). The block clips all input delay
values less than *Dmin* to
*Dmin*.
*Dmax* is the maximum valid
delay value (in samples). The block clips all input delay values greater
than *Dmax* to
*Dmax*.

When the **Interpolation mode** is set to one of the following:

- `Linear` ––
  *Dmin* equal 0.
  *Dmax* equals
  the value you specify in the **Maximum delay (Dmax) in
  samples** parameter.
- `FIR` ––
  *Dmin* equals
  *P* – 1, where *P* is the
  value you specify in **Interpolation filter half-length
  (P)**.
  *Dmax* equals the
  value you specify in the **Maximum delay (Dmax) in
  samples** parameter.
- `Farrow` ––
  *Dmin* equals
  *N/2* – 1, where *N* is
  the value you specify in **Farrow filter length
  (N)**.
  *Dmax* equals the
  value you specify in the **Maximum delay (Dmax) in
  samples** parameter.

**Example:** [1 100]

**Example:** [2 100]

**Example:** [3 100]

### Fixed-Point Properties

#### Fixed-Point Properties

### **Rounding mode** — Rounding method for fixed-point operations `Zero` (default) | `Ceiling` | `Convergent` | `Floor` | `Nearest` | `Round` | `Simplest`

Specify the rounding mode for fixed-point operations as one of the following:

- `Zero`
- `Ceiling`
- `Convergent`
- `Floor`
- `Nearest`
- `Round`
- `Simplest`

For more details, see rounding
mode.

### **Saturate on integer overflow** — Method of overflow action off (default) | on

When you select this parameter, the block saturates the result of its
fixed-point operation. When you clear this parameter, the block wraps
the result of its fixed-point operation. For details on
`saturate` and `wrap`, see overflow
mode for fixed-point operations.

### **Coefficients** — Data type of the coefficients `Same word length as input` (default) | `Specify word length`

Specify the data type of the filter coefficients as one of the
following:

- `Same word length as input` –– The
  word length of the filter coefficients matches that of the input
  to the block. The fraction length of the coefficients is
  automatically set to the binary-point only scaling that provides
  you with the best precision possible given the value and word
  length of the coefficients.
- `Specify word length` –– Specify the
  word length of the coefficients, in bits. In this mode, the
  fraction length of the coefficients is automatically set to the
  binary-point only scaling that provides you with the best
  precision possible given the value and word length of the
  coefficients.

For more information on the coefficients data type this block uses,
see the Fixed-Point Data Types
section.

### **Product output** — Data type of the product output `Same as first input` (default) | `Binary point scaling`

Specify the data type of the product output as one of the following:

- `Same as first input` –– The
  block specifies the product output data type to be the same
  as that of the data input.
- `Binary point scaling` –– Specify
  the word length and the fraction length of the product
  output, in bits.

For more information on the product output data type, see Multiplication Data Types and
the Fixed-Point Data Types
section.

### **Accumulator** — Data type of accumulation operation `Same as product output` (default) | `Same as first input` | `Binary point scaling`

Specify the data type of an accumulation operation as one of the following:

- `Same as product output` –– The
  block specifies the accumulator data type to be the same as
  that of the product output data type.
- `Same as first input` –– The
  block specifies the accumulator data type to be the same as
  that of the data input.
- `Binary point scaling` –– Specify
  the word length and the fraction length of the accumulator
  output, in bits.

For more information on the accumulator data type this block uses, see
the Fixed-Point Data Types
section.

### **Product output polyval** — Data type of the product polynomial value `Same as first input` (default) | `Binary point scaling`

Specify the data type of the product polynomial value as one of the following:

- `Same as first input` –– The
  block specifies the product polynomial value data type to be
  the same as that of the data input.
- `Binary point scaling` –– Specify
  the word length and the fraction length of the product
  output polynomial, in bits.

For more information on the product polynomial value data type this
block uses, see the Fixed-Point Data Types
section.

#### Dependencies

This property applies when you set **Interpolation
mode** to `Farrow`.

### **Accumulator polyval** — Data type of the accumulator polynomial value `Same as first input` (default) | `Binary point scaling`

Specify the data type of the accumulator polynomial value as one of
the following:

- `Same as first input` –– The
  block specifies the accumulator polynomial value data type
  to be the same as that of the data input.
- `Binary point scaling` –– Specify
  the word length and the fraction length of the accumulator
  polynomial value, in bits.

For more information on the accumulator polynomial value data type
that this block uses, see the Fixed-Point Data Types
section.

#### Dependencies

This property applies when you set **Interpolation
mode** to `Farrow`.

### **Multiplicand polyval** — Data type of multiplicand polynomial value `Same as first input` (default) | `Binary point scaling`

Specify the data type of the multiplicand polynomial value as one of
the following:

- `Same as first input` –– The
  block specifies the multiplicand polynomial value data type
  to be the same as that of the data input.
- `Binary point scaling` –– Specify
  the word length and the fraction length of the multiplicand
  polynomial value, in bits.

For more information on the multiplicand polynomial value data type
this block uses, see the Fixed-Point Data Types
section.

#### Dependencies

This property applies when you set **Interpolation
mode** to `Farrow`.

### **Output** — Data type of block output `Same as accumulator` (default) | `Same as first input` | `Binary point scaling`

Specify the data type of the block output as one of the following:

- `Same as accumulator` –– The
  block specifies the output data type to be the same as that
  of the accumulator output data type.
- `Same as first input` –– The
  block specifies the output data type to be the same as that
  of the data input.
- `Binary point scaling` –– Specify
  the word length and the fraction length of the block output,
  in bits.

For more information on the output data type this block uses, see the
Fixed-Point Data Types
section.

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
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Delay input by time-varying fractional number of sample periods

The Variable Fractional Delay block delays the input signal by a
specified number of fractional samples along each channel of the input. The block can
also concurrently compute multiple delayed versions (taps) of the same signal. For an
example, see Delay Signal Using Multitap Fractional Delay.

When the delay has a fractional value, the block interpolates the input signal to
obtain new samples at noninteger sampling intervals. You can set **Interpolation
mode** parameter to one of `Linear`,
`FIR`, or `Farrow`. The block
supports time-varying delay values. That is, the delay value can vary within a frame
from sample to sample.

The block assumes that the input values at the **Delay** port are
between *Dmin* and
*Dmax*, where
*Dmin* appears in the `Valid
delay range` section on the **Main** tab of the block
dialog, and *Dmax* is the value of the
**Maximum delay (Dmax) in samples** parameter. The block clips
delay values less than *Dmin* to
*Dmin* and delay values greater than
*Dmax* to
*Dmax*.

You must consider additional factors when selecting valid
`Delay` values for the `FIR` and
`Farrow` interpolation modes. For details, see Algorithms.
