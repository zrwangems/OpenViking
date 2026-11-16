---
type: simulink-block
title: 'IIR Halfband Decimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Multirate and Multistage Filters / Single Stage Multirate Filters'
documentation_page: 'iirhalfbanddecimator'
documentation_source_path: 'ref/iirhalfbanddecimator.html'
language: en
---

# IIR Halfband Decimator

## Ports

### Input

### **x** — Input signal column vector | matrix

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

This port is unnamed until you select the **Specify
coefficients from input port** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **coeffs1** — Branch 1 allpass polynomial coefficients *N*-by-`1` vector | *N*-by-`2` matrix

Specify the allpass polynomial filter coefficients of the first branch
as an *N*-by-`1` vector or
*N*-by-`2` matrix of
*N* first-order or second-order allpass
sections.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- **Internal allpass structure** to
  `Minimum multiplier`
- Clear the **Make the first branch a pure
  delay** parameter
- Select the **Specify coefficients from input
  port** parameter

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **coeffs2** — Branch 2 allpass polynomial coefficients *N*-by-`1` vector | *N*-by-`2` matrix

Specify the allpass polynomial filter coefficients of the second
branch as an *N*-by-`1` vector or
*N*-by-`2` matrix of
*N* first-order or second-order allpass
sections.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- **Internal allpass structure** to
  `Minimum multiplier`
- Select the **Specify coefficients from input
  port** parameter

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
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

This port is unnamed until you select the **Output highpass
subband** parameter.

**Data Types:** `single` | `double`
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

This port is unnamed until you select the **Output highpass
subband** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Filter specification** — Filter design parameters `Transition width and stopband attenuation` (default) | `Filter order and transition width` | `Filter order and stopband attenuation` | `Coefficients`

Select the parameters that the block uses to design the IIR halfband
filter. Because the filter design has only two degrees of freedom, you can
specify only two of the three parameters:

- `Transition width and stopband
  attenuation` (default) — Design the
  filter using **Transition width (Hz)** and
  **Stopband attenuation (dB)**. This design
  is the minimum order design.
- `Filter order and transition width`
  — Design the filter using **Filter
  order** and **Transition width
  (Hz)**.
- `Filter order and stopband
  attenuation` — Design the filter using
  **Filter order** and **Stopband
  attenuation (dB)**.
- `Coefficients`— Specify the
  filter coefficients directly using the enabled
  parameters.

### **Transition width (Hz)** — Transition width in Hz `4.1e3` (default) | positive real scalar

Specify the transition width of the IIR halfband filter as a real positive
scalar in Hz or in normalized frequency
units *(since R2023b)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the transition width is in Hz and must be less than
  half the value of the input sample rate.
- `Use normalized frequency (0 to 1)`
  –– The value of the transition width is in normalized frequency
  units. The value must be a positive scalar less than
  `1.0`.

*(since R2023b)*

#### Dependencies

To enable this parameter, set **Filter
specification** to `Filter order and transition
width` or `Transition width and stopband
attenuation`.

### **Filter order** — Order of the IIR halfband filter 9 (default) | positive integer

Specify the filter order as a finite positive integer. If you set
**Design method** to
`Elliptic`, then **Filter
order** must be an odd integer greater than one. If you set
**Design method** to `Quasi-linear
phase`, then **Filter order** must be a
multiple of four.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Filter order and transition
width` or `Filter order and stopband
attenuation`.

### **Stopband attenuation (dB)** — Minimum attenuation needed in stopband 80 (default) | positive real scalar

Specify the minimum attenuation needed in the stopband of the IIR halfband
filter as a real positive scalar in dB.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Filter order and stopband
attenuation` or `Transition width and
stopband attenuation`.

### **Design method** — Design method `Elliptic` (default) | `Quasi-linear phase`

Specify the design method for the IIR halfband filter.

- `Elliptic` — The filter has a
  nonlinear phase and uses few coefficients.
- `Quasi-linear phase` — The
  first branch of the polyphase filter structure is a pure delay,
  which results in an approximately linear phase response.

#### Dependencies

To enable this parameter, set **Filter
specification** to any option except
`Coefficients`.

### **Internal allpass structure** — Internal allpass filter implementation structure `Minimum multiplier` (default) | `Wave Digital Filter`

Specify the internal allpass filter implementation structure as
`Minimum multiplier` or `Wave
Digital Filter`. Each structure uses a different
coefficients set, independently stored in the corresponding coefficients
property.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Make the first branch a pure delay** — Make first branch a pure delay off (default) | on

When you select this check box, the first branch of the polyphase filter
structure becomes a pure delay, and the **Branch 1 allpass
polynomial coefficients** and **Branch 1 Wave Digital
coefficients** parameters do not apply.

By default, this check box is not selected.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Delay length in samples for branch 1** — Length of delay `1` (default) | positive scalar

Specify the length of the first branch delay as a positive scalar.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- Select the **Make the first branch a pure
  delay** parameter

### **Specify coefficients from input port** — Specify coefficients from input port off (default) | on

When you select this check box, you can input the branch 1 allpass
polynomial coefficients and branch 2 allpass polynomial coefficients through
the input ports **coeffs1** and
**coeffs2**. When you clear this check box, you specify
the coefficients in the block dialog box through the **Branch 1
allpass polynomial coefficients** and **Branch 2
allpass polynomial coefficients** parameters.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- **Internal allpass structure** to
  `Minimum multiplier`

### **Branch 1 allpass polynomial coefficients** — Allpass polynomial filter coefficients of first branch `[0.1284563; 0.7906755]` (default) | *N*-by-`1` | *N*-by-`2`

Specify the allpass polynomial filter coefficients of the first branch as
an *N*-by-`1` vector or
*N*-by-`2` matrix of
*N* first-order or second-order allpass
sections.

This parameter is tunable, that is, you can change its value during
simulation.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- **Internal allpass structure** to
  `Minimum multiplier`
- Clear the **Make the first branch a pure
  delay** parameter
- Clear the **Specify coefficients from input
  port** parameter

### **Branch 2 allpass polynomial coefficients** — Allpass polynomial filter coefficients of second branch `[0.4295667]` (default) | *N*-by-`1` | *N*-by-`2`

Specify the allpass polynomial filter coefficients of the second branch as
an *N*-by-`1` vector or
*N*-by-`2` matrix of
*N* first-order or second-order allpass
sections.

This parameter is tunable, that is, you can change its value during
simulation.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- **Internal allpass structure** to
  `Minimum multiplier`
- Clear the **Specify coefficients from input
  port** parameter

### **Branch 1 Wave Digital coefficients** — Allpass filter coefficients of first branch in wave digital filter form `[0.1284563; 0.7906755]` (default) | *N*-by-`1` | *N*-by-`2`

Specify the allpass filter coefficients of the first branch in wave
digital filter (WDF) form as an *N*-by-`1`
vector or *N*-by-`2` matrix of
*N* first-order or second-order allpass
sections.

The magnitude of each WDF coefficient must not be greater than 1.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- **Internal allpass structure** to
  `Wave Digital Filter`
- Clear the **Make the first branch a pure
  delay** parameter

### **Branch 2 Wave Digital coefficients** — Allpass filter coefficients of second branch in wave digital filter form `[0.4295667]` (default) | *N*-by-`1` | *N*-by-`2`

Specify the allpass filter coefficients of the second branch in wave
digital filter form as an *N*-by-`1`
vector or *N*-by-`2` matrix of
*N* first-order or second-order allpass
sections.

The magnitude of each WDF coefficient must not be greater than 1.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- **Internal allpass structure** to
  `Wave Digital Filter`

### **Last section of branch 2 is first order** — Last section of branch 2 is first order off (default) | on

When you select this check box, the block treats the last section of the
second branch as a first order section. When the coefficients of the second
branch are in an *N*-by-`2` matrix, the
block ignores the second element of the last row of the matrix. The last
section of the second branch then becomes a first-order section.

When you clear this check box, the block treats the last section of the
second branch as a second-order section. When the coefficients of the second
branch are in an *N*-by-`1` matrix, the
block ignores this parameter.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Output highpass subband** — Output highpass subband off (default) | on

When you select this check box, the block acts as an analysis filter bank,
producing two power-complementary outputs. When you clear this check box,
the block acts as an IIR halfband decimator and accepts a single vector or
matrix as input.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2023b*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to 1)`
  –– Specify the passband-edge and the stopband-edge frequencies
  in normalized frequency units (0 to 1).
- `Specify on dialog` –– Specify the
  input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal.

#### Dependencies

To enable this parameter, set **Filter
specification** to any value other than
`Coefficients`.

### **Input sample rate (Hz)** — Sample rate of input signal 44100 (default) | positive real scalar

Specify the sample rate of the input signal as a scalar in Hz.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to any value
  other than `Coefficients`.
- **Sample rate mode** to
  `Specify on dialog`.

*(since R2023b)*

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals `off` (default) | `on`

*Since R2023b*

Specify whether a fixed-size input signal (whose size does not change during simulation)
can have an arbitrary frame length, where the frame length does not have to
be a multiple of the decimation factor 2. The block uses this parameter only
for a fixed-size input signal and ignores it if the input data varies in
size during simulation.

When the input signal is a variable-size signal, the signal can have an
arbitrary frame length, that is, the frame length does not have to be a
multiple of the decimation factor 2.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor 2. If the input is not a multiple of the
  decimation factor, then the output is generally a variable-size
  signal. Therefore, to support arbitrary input size, the block
  must also support variable-size operations, which you can enable
  by selecting the **Allow arbitrary frame length for
  fixed-size input signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation factor
  2.

### **View Filter Response** — View Filter Response button

Click this button to open the Filter Visualization Tool (FVTool) and
display the magnitude and phase response of the IIR Halfband
Decimator. The response is based on the values you specify in
the block parameters dialog box. Changes made to these parameters update
FVTool.

To update the magnitude response while FVTool is running, modify the
dialog box parameters and click **Apply**.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Filtering / Multirate Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
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

Decimate signal using polyphase IIR halfband filter

The IIR Halfband Decimator  block performs polyphase decimation of the
input signal by a factor of 2. To design the halfband filter, you can specify the block
to use an elliptic design or a quasi-linear phase design. The block uses these design
methods to compute the filter coefficients. To filter the inputs, the block uses a
polyphase structure. The allpass filters in the polyphase structure are in a minimum
multiplier form.

Elliptic design introduces nonlinear phase and creates the filter using fewer
coefficients than the quasi-linear design. Quasi-linear phase design overcomes phase
nonlinearity at the cost of additional coefficients.

Alternatively, instead of designing the halfband filter using a design method, you can
specify the filter coefficients directly. When you choose this option, the allpass
filters in the two branches of the polyphase implementation can be in a minimum
multiplier form or a wave digital form.

You can also use the block to implement the analysis portion of a two-band filter bank
to filter a signal into lowpass and highpass subbands. For more details, see Algorithms.
