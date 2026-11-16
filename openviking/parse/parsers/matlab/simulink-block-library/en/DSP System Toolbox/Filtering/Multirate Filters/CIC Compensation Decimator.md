---
type: simulink-block
title: 'CIC Compensation Decimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'ciccompensationdecimator'
documentation_source_path: 'ref/ciccompensationdecimator.html'
language: en
---

# CIC Compensation Decimator

## Ports

### Input

### **Input** — Data input vector | matrix

Specify the data input as a vector or a matrix.

The block treats a *P*-by-*Q* input
matrix as *Q* independent channels, decimating each
channel over the first dimension.

When you input a variable-size signal (frame length changes during
simulation), the frame length of the signal *P* can be
arbitrary, that is, the input frame length does not have to be a
multiple of the decimation factor. When you input a fixed-size signal
(frame length does not change during simulation), the frame length can
be arbitrary only when you select the **Allow arbitrary frame
length for fixed-size input signals** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### Output

### **Output** — Filtered and downsampled signal vector | matrix

Filtered and downsampled signal, returned as a vector or matrix.

The output signal dimensions depend on the input signal dimensions,
the decimation factor of the compensator, and whether you select the
**Allow arbitrary frame length for fixed-size input
signals** parameter.

When the output is fixed-point, it is signed only.

This table provides more information on the dimensions of the output signal when you
input a fixed-size input signal and a variable-size input signal.

| Input Signal Size | Input Signal Dimensions | Output Signal Dimensions |
| --- | --- | --- |
| Fixed | *P*-by-1 column vector, where *P* is a multiple of the decimation factor *M* | (*P*/*M*)-by-1 |
| Fixed | *P*-by-1 column vector, where *P* is not a multiple of the decimation factor *M* | `ceil`(*P*/*M*)-by-1 when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |
| Fixed | *P*-by-*Q* matrix, where *P* is a multiple of the decimation factor *M* | (*P*/*M*)-by-*Q* |
| Fixed | *P*-by-*Q* matrix, where *P* is not a multiple of the decimation factor *M* | `ceil`(*P*/*M*)-by-*Q* when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |
| Variable | *P*-by-*Q* | `ceil`(*P*/*M*)-by-*Q*  **Allow arbitrary frame length for fixed-size input signals** parameter appears in the block dialog box but does not have any impact on the input frame length. You can input a variable-size signal of any frame length even if you do not select the **Allow arbitrary frame length for fixed-size input signals** parameter. |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

## Parameters

### Main Tab

### **Rate change factor** — Rate-change factor of the CIC filter `2` (default) | positive integer

Specify the rate-change factor of the CIC filter as a positive
integer. The block compensates the CIC filter using an FIR polyphase
decimator as the compensation filter.

### **Number of sections** — Number of sections in the CIC filter `2` (default) | positive integer

Specify the number of decimator and comb sections in the CIC filter as
a positive integer. The block compensates the CIC filter using an FIR
polyphase decimator as the compensation filter.

### **Differential delay** — Differential delay of the CIC filter `1` (default) | positive integer

Specify the delay value used in each comb section of the CIC filter as
a positive integer. The block compensates the CIC filter using an FIR
polyphase decimator as the compensation filter.

### **Decimation factor** — Decimation factor of compensation filter `2` (default) | positive integer scalar

Specify the decimation factor *M* of the compensation
filter as a positive integer. The number of input rows must be a
multiple of the decimation factor.

### **Minimum order filter design** — Design compensation filter of minimum order or of specified order `on` (default) | `off`

When you select this check box, the block designs filter with the
minimum order that meets the passband frequency, stopband frequency,
passband ripple, and stopband attenuation specifications. When you clear
this check box, the block designs filter with the order that you specify
in the **Filter order** parameter.

By default, this check box is selected.

### **Filter order** — Order of compensation filter `12` (default) | positive integer

Specify the order of the compensation filter as a positive
integer.

#### Dependency

To enable this parameter, clear the **Minimum order filter
design** parameter.

### **Passband edge frequency (Hz)** — Passband edge frequency of compensation filter `100000` (default) | positive scalar

Specify the passband edge frequency of the compensation filter as a positive scalar in
Hz or in normalized frequency
units *(since R2024a)*.

If you set the **Sample
rate mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` ––
  The value of the passband edge frequency is in Hz and must
  be in the range *Fpass* <
  *Fstop* < *Fs*/2,
  where *Fstop* is the stopband edge
  frequency and *Fs* is the input sample rate
  that you specify through the **Input sample rate
  (Hz)** parameter.
- `Use normalized frequency (0 to
  1)` –– The value of the passband edge
  frequency is in normalized frequency units and must be in
  the range *Fpass* <
  *Fstop* <
  `1.0`.

*(since R2024a)*

### **Stopband edge frequency (Hz)** — Stopband edge frequency of compensation filter `400000` (default) | positive scalar

Specify the stopband edge frequency of the compensation filter as a positive scalar in
Hz or in normalized frequency
units *(since R2024a)*.

If you set the **Sample
rate mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` ––
  The value of the stopband edge frequency is in Hz and must
  be in the range *Fpass* <
  *Fstop* < *Fs*/2,
  where *Fpass* is the passband edge
  frequency and *Fs* is the input sample rate
  that you specify through the **Input sample rate
  (Hz)** parameter.
- `Use normalized frequency (0 to
  1)` –– The value of the stopband edge
  frequency is in normalized frequency units and must be in
  the range *Fpass* <
  *Fstop* <
  `1.0`.

*(since R2024a)*

#### Dependency

To enable this parameter, select the **Minimum order
filter design** parameter.

### **Passband ripple (dB)** — Passband ripple of compensation filter `0.1` (default) | positive real scalar

Specify the passband ripple of the compensation filter as a positive
real scalar in dB.

### **Stopband attenuation (dB)** — Stopband attenuation of compensation filter `60` (default) | positive real scalar

Specify the stopband attenuation of the compensation filter as a
positive real scalar in dB.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2024a*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to
  1)` –– Specify the passband edge and the
  stopband edge frequencies in normalized frequency units (0
  to 1).
- `Specify on dialog` –– Specify
  the input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal.

### **Input sample rate (Hz)** — Sample rate of input signal `1200000` (default) | positive real scalar

Specify the sample rate of the input signal as a positive real scalar
in Hz.

#### Dependencies

To enable this parameter,
set the **Sample rate mode** parameter to
`Specify on dialog`. *(since R2024a)*

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals off (default) | on

*Since R2023a*

Specify whether fixed-size input signals (whose size does not change
during simulation) can have an arbitrary frame length, where the frame
length does not have to be a multiple of the decimation factor. The
block uses this parameter setting only for fixed-size input signals and
ignores this parameter if the input has a variable-size.

When the input signal is a variable-size signal, the signal can have
arbitrary frame length, that is, the frame length does not have to be a
multiple of the decimation factor.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor. If the input is not a multiple of the
  decimation factor, then the output is generally a
  variable-size signal. Therefore, to support arbitrary input
  size, the block must also support variable-size operations,
  which you can enable by selecting the **Allow
  arbitrary frame length for fixed-size input
  signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation
  factor.

### **View Filter Response** — View Filter Response button (default)

Click this button to open the Filter Visualization Tool FVTool and
display the magnitude and phase response of the CIC Compensation
Decimator. The response is based on the values you specify in the block
parameters dialog box. Changes made to these parameters update
FVTool.

To view the magnitude response and phase response simultaneously,
click the **Magnitude and Phase responses** button on
the toolbar.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

### Data Types Tab

### **Rounding mode** — Rounding mode for output fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode for fixed-point operations. The default is
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
  ]`,`16`,
  `15`)). Specify the sign mode of this data
  type as `[ ]` or true.
- `Refresh Data Type` — Refresh to
  the default data type.

Click the **Show data type assistant**
button  to display the data type assistant,
which helps you set the coefficients data type.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

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

### R2024a: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the passband edge and stopband edge frequencies in normalized frequency units (0 to
1).

### R2023a: Support for arbitrary input frame length

This block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and you select the **Allow arbitrary frame
  length for fixed-size input signals** parameter
- Input signal is a variable-size signal (frame length changes during
  simulation)

When this block supports an input signal with an arbitrary frame length, the input
frame length does not have to be a multiple of the decimation factor.

## Description

Compensate for CIC filter using FIR decimator

The CIC Compensation Decimator block uses an FIR polyphase decimator as
the compensation filter. CIC compensation decimators are multirate FIR filters that you
cascade with CIC decimators to mitigate the drawbacks of the CIC filters.

CIC decimation filters are used in areas that require high decimation. These filters
are popular in ASICs and FPGAs, since they do not have any multipliers. CIC filters have
two drawbacks:

- CIC filters have a magnitude response that causes a droop in the passband
  region. This magnitude response is:

  abs(sin(Mω2)sin(ω2))n

  - *M* — Differential delay
  - *n* — Number of stages
  - *ω* — Normalized angular
    frequency
- CIC filters have a wide transition region.

The compensation decimator filters have an inverse passband response to
correct for the CIC droop, and they have a narrow transition width.

This block brings the capabilities of the `dsp.CICCompensationDecimator`
System object™ to the Simulink® environment.
