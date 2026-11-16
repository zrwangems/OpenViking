---
type: simulink-block
title: 'IIR Halfband Interpolator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Multirate and Multistage Filters / Single Stage Multirate Filters'
documentation_page: 'iirhalfbandinterpolator'
documentation_source_path: 'ref/iirhalfbandinterpolator.html'
language: en
---

# IIR Halfband Interpolator

## Ports

### Input

### **LP** — Data input column vector | matrix

Specify the data input as a vector or a matrix. If the input signal is
a matrix, the block treats each column of the matrix as an independent
channel.

When you select the **Input highpass subband**
parameter, this block acts as a halfband synthesis filter bank. The
input at this port is then the lowpass subband output of a halfband
analysis filter bank.

This port is unnamed until you select the **Input highpass
subband** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **HP** — Second input to the synthesis filter bank column vector | matrix

Specify the second input to the synthesis filter bank as a column
vector or a matrix. This signal is the highpass subband output of a
halfband analysis filter bank. If the input signal is a matrix, the
block treats each column of the matrix as an independent channel.

The size, data type, and complexity of both the inputs must be the
same.

#### Dependency

To enable this port, select the **Input highpass
subband** parameter.

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

**Data Types:** `single` | `double`

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

**Data Types:** `single` | `double`
### Output

### **Output** — Output of interpolator column vector | matrix

Output of the interpolator, returned as a column vector or a matrix.
The number of rows in the interpolator output is twice the number of
rows in the input signal.

**Data Types:** `single` | `double`

## Parameters

### **Filter specification** — Filter design parameters `Transition width and stopband attenuation` (default) | `Filter order and stopband attenuation` | `Filter order and transition width` | `Coefficients`

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

### **Transition width (Hz)** — Transition width `4.1e3` (default) | positive scalar

Specify the transition width of the IIR halfband filter as a positive scalar in Hz
or in normalized frequency
units *(since R2023b)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the transition width is in Hz and must be less than
  half the value of the output sample rate (2 × input sample
  rate).
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

Specify the filter order as a positive integer. If you set
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

- `Elliptic` (default) — The
  filter has a nonlinear phase and uses few coefficients.
- `Quasi-linear phase` — The
  first branch of the polyphase filter structure is a pure delay,
  which results in an approximately linear phase response.

#### Dependencies

To enable this parameter, set **Filter
specification** to any option except
`Coefficients`.

### **Internal allpass structure** — Filter structure in coefficient mode `Minimum multiplier` (default) | `Wave Digital Filter`

Specify the internal allpass filter implementation structure as
`Minimum multiplier` or `Wave
Digital Filter`. Each structure uses a different
coefficients set, independently stored in the corresponding coefficients
property. The default is `Minimum
multiplier`.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Make the first branch a pure delay** — Make the first branch a pure delay `off` (default) | `on`

When you select this check box, the first branch of the polyphase filter
structure becomes a pure delay, and the **Branch 1 allpass
polynomial coefficients** and **Branch 1 Wave Digital
coefficients** parameters do not apply.

By default, this check box is not selected.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Delay length in samples for branch 1** — Length of the delay `1` (default) | finite positive scalar

Specify the length of the first branch delay as a finite positive scalar.
The default is `1`.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to
  `Coefficients`
- Select the **Make the first branch a pure
  delay** parameter

### **Specify coefficients from input port** — Specify coefficients from input port `off` (default) | `on`

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

### **Last section of branch 2 is first order** — Make the last section of the second branch as first order `off` (default) | `on`

When you select this check box, the block treats the last section of the
second branch as a first order section. When the coefficients of the second
branch are in an *N*-by-`2` matrix, the
block ignores the second element of the last row of the matrix. The last
section of the second branch then becomes a first-order section.

When you clear this check box, the block treats the last section of the
second branch as a second-order section. When the coefficients of the second
branch are in an *N*-by-`1` matrix, the
block ignores this parameter.

By default, this check box is cleared.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Input highpass subband** — Input highpass subband `off` (default) | `on`

When you select this check box, the block acts as a synthesis filter bank.
The block accepts two inputs to synthesize: lowpass and highpass subbands.
When you clear this check box, the block acts as an IIR halfband
interpolator and accepts a single vector or matrix as input. By default,
this check box is cleared.

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

### **Input sample rate (Hz)** — Sample rate of input signal 22050 (default) | positive real scalar

Specify the sample rate of the input signal as a scalar in Hz.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to any value
  other than `Coefficients`.
- **Sample rate mode** to
  `Specify on dialog`.

*(since R2023b)*

### **View Filter Response** — View Filter Response button

Click this button to open the Filter Visualization Tool (FVTool) and
display the magnitude and phase response of the IIR Halfband
Interpolator. The response is based on the values you specify in
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

## Description

Interpolate signal using polyphase IIR halfband filter

The IIR Halfband Interpolator block performs efficient polyphase
interpolation of the input signal by a factor of 2. To design the halfband filter, you
can use an elliptic design or a quasi-linear phase design. The block uses these design
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

You can also use the block to implement the synthesis portion of a two-band filter
bank to synthesize a signal from lowpass and highpass subbands.
