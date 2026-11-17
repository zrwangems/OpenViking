---
type: simulink-block
title: 'CIC Compensation Interpolator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'ciccompensationinterpolator'
documentation_source_path: 'ref/ciccompensationinterpolator.html'
language: en
---

# CIC Compensation Interpolator

## Ports
```yaml
ports:
- name: Input
  summary: Data input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
- name: Output
  summary: Upsampled and filtered signal vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
```

### Input

### **Input** — Data input vector | matrix

Specify the data input as a vector or a matrix.

The block treats a *P*-by-*Q* input
matrix as *Q* independent channels, interpolating each
channel over the first dimension.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### Output

### **Output** — Upsampled and filtered signal vector | matrix

Upsampled and filtered signal, returned as a vector or matrix. For a
*P*-by-*Q* input matrix, the
output is an *LP*-by-*Q* matrix, where
*L* is the interpolation
factor.

When the output is fixed-point, it is signed only.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Rate change factor
  summary: Rate-change factor of the CIC filter 2 (default) | positive integer
  group: Main Tab
- name: Number of sections
  summary: Number of sections in the CIC filter being compensated 2 (default) | positive integer
  group: Main Tab
- name: Differential delay
  summary: Differential delay of the CIC filter 1 (default) | positive integer
  group: Main Tab
- name: Interpolation factor
  summary: Interpolation factor of compensation filter 2 (default) | positive integer
  group: Main Tab
- name: Minimum order filter design
  summary: Design compensation filter of minimum order or of specified order on (default) | off
  group: Main Tab
- name: Filter order
  summary: Order of compensation filter 12 (default) | positive integer
  group: Main Tab
- name: Passband edge frequency (Hz)
  summary: Passband edge frequency of compensation filter 100000 (default) | positive scalar
  group: Main Tab
- name: Stopband edge frequency (Hz)
  summary: Stopband edge frequency of compensation filter 400000 (default) | positive scalar
  group: Main Tab
- name: Passband ripple (dB)
  summary: Passband ripple of compensation filter 0.1 (default) | positive scalar
  group: Main Tab
- name: Stopband attenuation (dB)
  summary: Stopband attenuation of compensation filter 60 (default) | positive scalar
  group: Main Tab
- name: Sample rate mode
  summary: Mode to specify the input sample rate Use normalized frequency (0 to 1) (default) | Specify on dialog | Inherit
    from input port
  group: Main Tab
- name: Input sample rate (Hz)
  summary: Sample rate of input signal 600000 (default) | positive scalar
  group: Main Tab
- name: View Filter Response
  summary: View Filter Response button
  group: Main Tab
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: Main Tab
- name: Rounding mode
  summary: Rounding mode for output fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest
    | Zero
  group: Data Types Tab
- name: Coefficients
  summary: Word and fraction lengths of coefficients fixdt(1,16) (default) | fixdt(1,16,0)
  group: Data Types Tab
```

### Main Tab

### **Rate change factor** — Rate-change factor of the CIC filter `2` (default) | positive integer

Specify the rate-change factor of the CIC filter as a positive
integer. The block compensates the CIC filter using an FIR polyphase
interpolator as the compensation filter.

### **Number of sections** — Number of sections in the CIC filter being compensated `2` (default) | positive integer

Specify the number of sections in the CIC filter as a positive
integer. The block compensates the CIC filter using an FIR polyphase
interpolator as the compensation filter.

### **Differential delay** — Differential delay of the CIC filter `1` (default) | positive integer

Specify the differential delay value used in each comb section of the
CIC filter as a positive integer. The block compensates the CIC filter
using an FIR polyphase interpolator as the compensation filter.

### **Interpolation factor** — Interpolation factor of compensation filter `2` (default) | positive integer

Specify the interpolation factor *L* of the
compensation filter as a positive integer.

### **Minimum order filter design** — Design compensation filter of minimum order or of specified order `on` (default) | `off`

When you select this check box, the block designs filter with the
minimum order that meets the passband frequency, stopband frequency,
passband ripple, and stopband attenuation specifications. When you clear
this check box, the block designs filter with the order that you specify
in the **Filter order** parameter.

### **Filter order** — Order of compensation filter `12` (default) | positive integer

Specify the order of the compensator filter as a positive
integer.

#### Dependencies

To enable this parameter, clear the **Minimum order filter
design** parameter.

### **Passband edge frequency (Hz)** — Passband edge frequency of compensation filter `100000` (default) | positive scalar

Specify the passband edge frequency *Fpass* of the compensation filter
as a positive scalar in Hz or in normalized
frequency units *(since R2024a)*.

If you set the **Sample
rate mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` ––
  The value of the passband edge frequency is in Hz and must
  be in the range *Fpass* <
  *Fstop* < (*Fs*/2)
  × *L*, where *Fstop* is
  the stopband edge frequency, *Fs* is the
  input sample rate that you specify through the
  **Input sample rate (Hz)** parameter,
  and *L* is the interpolation factor that
  you specify through the **Interpolation
  factor** parameter.
- `Use normalized frequency (0 to
  1)` –– The value of the passband edge
  frequency is in normalized frequency units and must be in
  the range *Fpass* <
  *Fstop* <
  `1.0`.

*(since R2024a)*

### **Stopband edge frequency (Hz)** — Stopband edge frequency of compensation filter `400000` (default) | positive scalar

Specify the stopband edge frequency *Fstop* of the compensation filter
as a positive scalar in Hz or in normalized
frequency units *(since R2024a)*.

If you set the **Sample
rate mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` ––
  The value of the stopband edge frequency is in Hz and must
  be in the range *Fpass* <
  *Fstop* < (*Fs*/2)
  × *L*, where *Fpass* is
  the passband edge frequency, *Fs* is the
  input sample rate that you specify through the
  **Input sample rate (Hz)** parameter,
  and *L* is the interpolation factor that
  you specify through the **Interpolation
  factor** parameter.
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

### **Passband ripple (dB)** — Passband ripple of compensation filter `0.1` (default) | positive scalar

Specify the filter passband ripple of the compensation filter as a
positive scalar in dB.

### **Stopband attenuation (dB)** — Stopband attenuation of compensation filter `60` (default) | positive scalar

Specify the stopband attenuation of the compensation filter as a
positive scalar in dB.

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

### **Input sample rate (Hz)** — Sample rate of input signal `600000` (default) | positive scalar

Specify the sample rate of input signal as a positive scalar in
Hz.

#### Dependencies

To enable this parameter,
set the **Sample rate mode** parameter to
`Specify on dialog`. *(since R2024a)*

### **View Filter Response** — View Filter Response button

Click this button to open the Filter Visualization Tool (FVTool) and
display the magnitude and phase response of the CIC Compensation
Interpolator. The response is based on the values you
specify in the block parameters dialog box. Changes made to these
parameters update FVTool.

To update the magnitude response while FVTool is running, modify the
dialog box parameters and click **Apply**.

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

- `fixdt(1,16)` — Signed
  fixed-point data type of word length `16`
  with binary point scaling. The block determines the fraction
  length automatically from the coefficient values in such a
  way that the coefficients occupy maximum representable range
  without overflowing.
- `fixdt(1,16,0)` — Signed
  fixed-point data type of word length `16`
  with fraction length `0`. You can change
  the fraction length to any other integer value.
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

## Description

Compensate for CIC filter using FIR interpolator

The CIC Compensation Interpolator block uses an FIR polyphase
interpolator as the compensation filter. CIC compensation interpolators are multirate
FIR filters that you cascade with CIC interpolators to mitigate the drawbacks of the CIC
filters.

CIC interpolation filters are used in areas that require high interpolation. These
filters are popular in ASICs and FPGAs, since they do not have any multipliers. CIC
filters have two drawbacks:

- CIC filters have a magnitude response that causes a droop in the passband
  region. This magnitude response is:

  abs(sin(Mω2)sin(ω2))n

  - *M* — Differential delay
  - *n* — Number of stages
  - *ω* — Normalized angular
    frequency
- CIC filters have a wide transition region.

The compensation interpolator filters have an inverse sinc passband
response to correct for the CIC droop, and they have a narrow transition width.

This block brings the capabilities of the `dsp.CICCompensationInterpolator`
System object™ to the Simulink® environment.
