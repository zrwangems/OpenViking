---
type: simulink-block
title: 'FIR Halfband Decimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'firhalfbanddecimator'
documentation_source_path: 'ref/firhalfbanddecimator.html'
language: en
---

# FIR Halfband Decimator

## Ports

### Input

### **Input** — Input signal column vector | matrix

Specify the input signal as a column vector or a matrix of size
*P*-by-*Q*.

The block treats each column of the input signal as a separate
channel. If the input is a two-dimensional signal, the first dimension
represents the channel length (or frame size) and the second dimension
represents the number of channels. If the input is a one-dimensional
signal, then the block interprets it as a single-channel signal.

This block supports variable-size input signals (frame length changes
during simulation).

When you input a variable-size
signal, the frame length of the signal can be arbitrary, that is, the
input frame length does not have to be a multiple of the decimation
factor 2. When you input a fixed-size signal (frame length does not
change during simulation), the frame length can be arbitrary only when
you select the **Allow arbitrary frame length for
fixed-size input signals** parameter. *(since R2023b)*

This block supports variable-size input signals.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **LP** — Lowpass subband of decimator output column vector | matrix

Lowpass subband of the decimator output, returned as a column vector or a matrix. As the
filter is a halfband filter, the downsampling factor is always 2.

The dimensions of the output signal depend on the
dimensions of the input signal and on whether you select the
**Allow arbitrary frame length for fixed-size input
signals** parameter. *(since R2023b)*

This table provides more details on the dimensions of the lowpass
subband output signal when you input a fixed-size input signal.

**Fixed-Size Input Signal**

| Input Signal | Output Signal |
| --- | --- |
| *P*-by-*Q*, where *P* is a multiple of the decimation factor 2 | Fixed-size signal of size (*P*/2)-by-*Q* |
| *P*-by-*Q*, where *P* is not a multiple of the decimation factor 2 *(since R2023b)* | Variable-size signal with an upper bound of size `ceil`(*P*/2)-by-*Q* when you select **Allow arbitrary frame length for fixed-size input signals** *(since R2023b)*  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. *(since R2023b)* |

This table gives more details on
the dimensions of the lowpass subband output signal when you input a
variable-size input signal. When you input a variable-size signal (frame
length changes during simulation), the **Allow
arbitrary frame length for fixed-size input signals**
parameter is visible in the block dialog box but does not have any
impact on the input frame length. You can input a variable-size signal
of any frame length even if you do not select the **Allow arbitrary frame length for fixed-size input
signals** parameter. *(since R2023b)*

**Variable-Size Input Signal**

| Input Signal | Output Signal |
| --- | --- |
| *P*-by-*Q* | Variable-size signal with an upper bound of size `ceil`(*P*/2)-by-*Q* *(since R2023b)* |

When the output is of fixed-point data type, it is signed only.

This port is unnamed until you select the **Output highpass
subband** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes

### **HP** — Highpass subband of decimator output column vector | matrix

Highpass subband of the decimator output, returned as a column vector or a matrix. As
the filter is a halfband filter, the downsampling factor is always
2.

The dimensions of the output signal depend on the
dimensions of the input signal and on whether you select the
**Allow arbitrary frame length for fixed-size input
signals** parameter. *(since R2023b)*

This table provides more details on the dimensions of the highpass
subband output signal when you input a fixed-size input signal.

**Fixed-Size Input Signal**

| Input Signal | Output Signal |
| --- | --- |
| *P*-by-*Q*, where *P* is a multiple of the decimation factor 2 | Fixed-size signal of size (*P*/2)-by-*Q* |
| *P*-by-*Q*, where *P* is not a multiple of the decimation factor 2 *(since R2023b)* | Variable-size signal with an upper bound of size `ceil`(*P*/2)-by-*Q* when you select **Allow arbitrary frame length for fixed-size input signals** *(since R2023b)*  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. *(since R2023b)* |

This table gives more details on
the dimensions of the highpass subband output signal when you input a
variable-size input signal. When you input a variable-size signal (frame
length changes during simulation), the **Allow
arbitrary frame length for fixed-size input signals**
parameter is visible in the block dialog box but does not have any
impact on the input frame length. You can input a variable-size signal
of any frame length even if you do not select the **Allow arbitrary frame length for fixed-size input
signals** parameter. *(since R2023b)*

**Variable-Size Input Signal**

| Input Signal | Output Signal |
| --- | --- |
| *P*-by-*Q* | Variable-size signal with an upper bound of size `ceil`(*P*/2)-by-*Q* *(since R2023b)* |

When the output is of fixed-point data type, it is signed only.

#### Dependency

To enable this port, select the **Output highpass
subband** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main Tab

### **Filter specification** — Filter design parameters `Transition width and stopband attenuation` (default) | `Filter order and transition width` | `Filter order and stopband attenuation` | `Coefficients`

Select the parameters that the block uses to design the FIR halfband filter.

- `Transition width and stopband
  attenuation` (default) — Design the
  filter using **Transition width (Hz)** and
  **Stopband attenuation (dB)**. This
  design is the minimum-order design.
- `Filter order and transition
  width` — Design the filter using
  **Filter order** and
  **Transition width (Hz)**.
- `Filter order and stopband
  attenuation` — Design the filter
  using **Filter order** and
  **Stopband attenuation (dB)**.
- `Coefficients` — Specify
  the filter coefficients directly through the
  **Numerator** parameter.

### **Filter order** — Filter order `52` (default) | even positive integer

Specify the filter order as an even positive integer.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Filter order and
transition width` or `Filter order and
stopband attenuation`.

### **Transition width (Hz)** — Transition width `4.1e3` (default) | positive scalar

Specify the transition width as a positive scalar in Hz or
in normalized frequency units *(since R2023b)*.

If you set the **Sample
rate mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` ––
  The value of the transition width is in Hz and must be less
  than half the value of the input sample rate.
- `Use normalized frequency (0 to
  1)` –– The value of the transition width is
  in normalized frequency units. The value must be a positive
  scalar less than `1.0`.

*(since R2023b)*

#### Dependencies

To enable this parameter, set **Filter
specification** to `Filter order and
transition width` or `Transition width
and stopband attenuation`.

### **Stopband attenuation (dB)** — Stopband attenuation `80` (default) | positive real scalar

Specify the stopband attenuation as a real positive scalar in
dB.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Filter order and
stopband attenuation` or `Transition
width and stopband attenuation`.

### **Numerator** — FIR halfband filter coefficients `designHalfbandFIR('TransitionWidth',0.186, 'StopbandAttenuation',80, 'Structure','decim')` (default) | row vector

Specify the FIR halfband filter coefficients directly as a row vector.
The coefficients must comply with the FIR halfband impulse response
format. If (`length`(`Numerator`)
− 1)/2 is even, where
(`length`(`Numerator`) − 1) is
the filter order, every other coefficient starting with the first
coefficient must be 0 except the center coefficient which must be 0.5.
If (`length`(`Numerator`) − 1)/2
is odd, the sequence of alternating zeros with 0.5 at the center starts
at the second coefficient.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Design method** — Filter design method `Auto` (default) | `Equiripple` | `Kaiser`

Specify the filter design method as one of the following:

- `Auto` –– The algorithm
  automatically chooses the filter design method depending on
  the filter design parameters. The algorithm uses the
  equiripple or the Kaiser window method to design the
  filter.

  If the design constraints are very tight, such as very
  high stopband attenuation or very narrow transition width,
  then the algorithm automatically chooses the Kaiser method,
  as this method is optimal for designing filters with very
  tight specifications. However, if the design constraints are
  not tight, then the algorithm chooses the equiripple
  method.

  When you set the **Design method**
  parameter to `Auto`, you can
  determine the method used by the algorithm by examining the
  passband and stopband ripple characteristics of the designed
  filter. If the block used the equiripple method, the
  passband and stopband ripples of the designed filter have a
  constant amplitude in the frequency response. If the filter
  design method the block chooses in the
  `Auto` mode is not suitable for
  your application, manually specify the **Design
  method** as
  `Equiripple` or
  `Kaiser`.
- `Equiripple` –– The algorithm
  uses the equiripple method.
- `Kaiser` –– The algorithm uses
  the Kaiser window method.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Filter order and
stopband attenuation`, `Filter order
and transition width`, or `Transition
width and stopband attenuation`.

### **Output highpass subband** — Output highpass subband `off` (default) | `on`

When you select this check box, the block acts as an analysis filter
bank and analyzes the input signal into highpass and lowpass subbands.
When you clear this check box, the block acts as an FIR halfband
decimator.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2023b*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to
  1)` –– Specify the transition width in
  normalized frequency units (0 to 1).
- `Specify on dialog` –– Specify
  the input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal.

#### Dependencies

To enable this parameter, set **Filter
specification** to any value other than
`Coefficients`.

### **Input sample rate (Hz)** — Sample rate of input signal `44100` (default) | positive real scalar

Specify the sample rate of the input signal as a positive scalar in
Hz.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to any value
  other than
  `Coefficients`.
- **Sample rate mode** to
  `Specify on dialog`.

*(since R2023b)*

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals `off` (default) | `on`

*Since R2023b*

Specify whether a fixed-size input signal (whose size does not change during simulation)
can have an arbitrary frame length, where the frame length does not have
to be a multiple of the decimation factor 2. The block uses this
parameter only for fixed-size input signals and ignores it if the input
data varies in size during simulation.

When the input signal is a variable-size signal, the signal can have
an arbitrary frame length, that is, the frame length does not have to be
a multiple of the decimation factor 2.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor 2. If the input is not a multiple of the
  decimation factor, then the output is generally a
  variable-size signal. Therefore, to support arbitrary input
  size, the block must also support variable-size operations,
  which you can enable by selecting the **Allow
  arbitrary frame length for fixed-size input
  signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation factor
  2.

### **View Filter Response** — View Filter Response button

Click this button to open the Filter Visualization Tool (FVTool) and
display the magnitude and phase response of the FIR Halfband
Decimator. The response is based on the values you specify
in the block parameters dialog box. Changes made to these parameters
update FVTool.

To update the magnitude response while FVTool is running, modify the
dialog box parameters and click **Apply**.

Magnitude response in dB

To view the magnitude response and phase response simultaneously,
click the **Magnitude and Phase responses** button on
the toolbar.

#### Dependencies

To visualize the filter response, set **Sample rate
mode** to `Specify on dialog`
or `Use normalized frequency (0 to
1)`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

### Data Types Tab

### **Rounding mode** — Rounding mode for output fixed-point operations `Floor` (default) | `Ceiling` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode for output fixed-point operations. The default is
`Floor`.

### **Coefficients** — Word and fraction lengths of coefficients `fixdt(1,16)` (default) | `fixdt(1,16,0)`

Specify the fixed-point data type of the coefficients as one of the
following:

- `fixdt(1,16)` (default) —
  Signed fixed-point data type of word length
  `16` with binary point scaling. The
  block determines the fraction length automatically from the
  coefficient values in such a way that the coefficients
  occupy maximum representable range without
  overflowing.
- `fixdt(1,16,0)` — Signed
  fixed-point data type of word length `16`
  and fraction length `0`. You can change the
  fraction length to any other integer value.
- `<data type expression>`
  — Specify the coefficients data type by using an
  expression that evaluates to a data type object. For
  example,
  `numerictype`(`fixdt`(`[
  ]`,`18`,
  `15`)). Specify the sign mode of this data
  type as `[ ]` or true.
- `Refresh Data Type` — Refresh to
  the default data type.

Click the **Show data type assistant**
button  to display the data type assistant,
which helps you set the coefficients data type.

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

## Version History

**Introduced in R2015b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2023b: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the transition width in normalized frequency units (0 to 1).

### R2023b: Support for arbitrary input frame length

This block supports an input signal with an arbitrary frame length when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and you select the **Allow arbitrary frame
  length for fixed-size input signals** parameter.
- Input signal is a variable-size signal (frame length changes during
  simulation).

When this block supports an input signal with an arbitrary frame length, the input frame
length does not have to be a multiple of the decimation factor 2 and the output
signal is a variable-size signal.

## Description

Decimate signal using polyphase FIR halfband filter

The FIR Halfband Decimator block performs polyphase decimation of the
input signal by a factor of 2. The block uses an FIR equiripple design or a Kaiser
window design to construct the halfband filters. The implementation takes advantage of
the zero-valued coefficients of the FIR halfband filter, making one of the polyphase
branches a delay. You can use the block to implement the analysis portion of a two-band
filter bank to separate a signal into lowpass and highpass subbands. For more
information, see Algorithms.

The block supports fixed-point operations and ARM®
Cortex® code generation. For more information on ARM
Cortex code generation, see Code Generation for ARM Cortex-M and ARM Cortex-A Processors.
