---
type: simulink-block
title: 'Complex Bandpass Decimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'complexbandpassdecimator'
documentation_source_path: 'ref/complexbandpassdecimator.html'
language: en
---

# Complex Bandpass Decimator

## Ports
```yaml
ports:
- name: x
  summary: Input data vector | matrix
  direction: input
  data_types: single | double
- name: Fc
  summary: Center frequency real scalar
  direction: input
  data_types: single | double
- name: Port_1
  summary: Filtered output vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **x** — Input data vector | matrix

Specify the input data as a vector or a matrix.

The block treats each column of the input signal as a separate
channel. If the input is a two-dimensional signal, the first dimension
represents the channel length (or frame size) and the second dimension
represents the number of channels. If the input is a one-dimensional
signal, then the block interprets it as a single-channel signal.

When you input a variable-size signal (frame length changes during
simulation), the frame length of the signal can be arbitrary, that is,
the input frame length does not have to be a multiple of the decimation
factor. When you input a fixed-size signal (frame length does not change
during simulation), the frame length can be arbitrary only when you
select the **Allow arbitrary frame length for
fixed-size input signals** parameter.

To determine the decimation factor, click the **View Info** button.

This port is unnamed until you select the **Specify center
frequency from input port** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Fc** — Center frequency real scalar

Specify the center frequency of the desired band as a real, finite
numeric scalar in the range [–*Fs*/2,
*Fs*/2], where *Fs* is the sample
rate of the input signal. If you set **Sample rate
mode** to `Inherit from input
port` or `Specify on dialog`,
the block inherits *Fs* from the input signal or uses
the value of the **Input sample rate (Hz)** parameter,
respectively. If you set **Sample
rate mode** to `Use normalized frequency (0
to 1)`, the block sets *Fs* to
2 *(since R2024b)*.

#### Dependencies

To enable this port, select the **Specify center frequency
from input port** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Filtered output vector | matrix

Output of the complex bandpass decimator, returned as a vector or a
matrix. The output contains the subband of frequencies specified by the
parameters in the block dialog box.

The output signal dimensions depend on the input signal dimensions,
the overall decimation factor of the Complex Bandpass
Decimator block, and whether you select the **Allow
arbitrary frame length for fixed-size input signals**
parameter. You can determine the overall decimator factor
*D* by clicking the **View
Info** button in the block dialog box.

This table provides more details on the dimensions of the output
signal when you input a fixed-size input signal.

**Fixed-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-1 column vector, where *P* is a multiple of the decimation factor *D* | (*P*/*D*)-by-1 |
| *P*-by-1 column vector, where *P* is not a multiple of the decimation factor *D* | `ceil`(*P*/*D*)-by-1 when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |
| *P*-by-*Q* matrix, where *P* is a multiple of the decimation factor *D* | (*P*/*D*)-by-*Q* |
| *P*-by-*Q* matrix, where *P* is not a multiple of the decimation factor *D* | `ceil`(*P*/*D*)-by-*Q* when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |

This table gives more details on the dimensions of the output signal
when you input a variable-size input signal. When you input a
variable-size signal (frame length changes during simulation), the
**Allow arbitrary frame length for fixed-size
input signals** parameter is visible in the block dialog
box but does not have any impact on the input frame length. You can
input a variable-size signal of any frame length even if you do not
select the **Allow arbitrary frame length for
fixed-size input signals** parameter.

**Variable-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-*Q* | `ceil`(*P*/*D*)-by-*Q* |

The data type of the output is same as the data type of the input. The
output signal is always complex.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Filter specification
  summary: Filter design parameters Decimation factor (default) | Bandwidth | Decimation factor and bandwidth
  group: ''
- name: Decimation factor
  summary: Decimation factor 2 (default) | positive integer
  group: ''
- name: Bandwidth
  summary: Width of frequency band of interest 0.2268 (default) | real positive scalar
  group: ''
- name: Specify center frequency from input port
  summary: Specify source of center frequency off (default) | on
  group: ''
- name: Center frequency
  summary: Center frequency of desired band 0 (default) | real scalar
  group: ''
- name: Stopband attenuation (dB)
  summary: Stopband attenuation in dB 80 (default) | positive scalar
  group: ''
- name: Passband ripple (dB)
  summary: Passband ripple in dB 1 (default) | positive scalar
  group: ''
- name: Transition width
  summary: Transition width 0.0045 (default) | positive scalar
  group: ''
- name: Reduce number of complex coefficients
  summary: Minimize number of complex coefficients on (default) | off
  group: ''
- name: Mix signal to baseband
  summary: Mix signal to baseband on (default) | off
  group: ''
- name: Sample rate mode
  summary: Mode to specify the input sample rate Use normalized frequency (0 to 1) (default) | Specify on dialog | Inherit
    from input port
  group: ''
- name: Input sample rate (Hz)
  summary: Input sample rate in Hz 44100 (default) | real positive scalar
  group: ''
- name: Allow arbitrary frame length for fixed-size input signals
  summary: Allow arbitrary frame length for fixed-size input signals off (default) | on
  group: ''
- name: View Filter Response
  summary: Visualize frequency response button
  group: ''
- name: View Info
  summary: View filter information button
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Filter specification** — Filter design parameters `Decimation factor` (default) | `Bandwidth` | `Decimation factor and bandwidth`

Specify the filter design parameters as one of the following:

- `Decimation factor` –– Specify the
  decimation factor through the **Decimation
  factor** parameter. The block computes the
  bandwidth of interest (*BW*) using the
  following equation:

  BW=Fs/D

  where

  - *Fs* –– Sample rate of input
    signal
  - *D* –– Decimation factor
- `Bandwidth` –– Specify the bandwidth
  through the **Bandwidth** parameter. The block
  computes the decimation factor (*D*) using the
  following equation:

  D=floor(FsBW+TW)

  where

  - *Fs* –– Sample rate of input
    signal
  - *BW* –– Bandwidth of
    interest
  - *TW* –– Transition width
    specified through the **Transition
    width** parameter
- `Decimation factor and bandwidth` ––
  Specify the decimation factor and the bandwidth of interest
  through the **Decimation factor** and
  **Bandwidth** parameters,
  respectively.

### **Decimation factor** — Decimation factor `2` (default) | positive integer

Specify the factor by which to reduce the bandwidth of the input signal as
a positive integer. The frame size (number of rows) of the input signal must
be a multiple of the decimation factor.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Decimation
factor` or `Decimation factor and
bandwidth`.

### **Bandwidth** — Width of frequency band of interest `0.2268` (default) | real positive scalar

Specify the width of the frequency band of interest as a real positive
scalar in Hz or in normalized frequency
units *(since R2024b)*.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Bandwidth` or
`Decimation factor and bandwidth`.

**Data Types:** `single` | `double`

### **Specify center frequency from input port** — Specify source of center frequency `off` (default) | `on`

When you select this check box, the center frequency is input through the
**Fc** port. When you clear this check box, you can
specify the center frequency in the block dialog box through the
**Center frequency** parameter.

When you select this check box, the block does not compute the filter
response. To view the filter response, clear this check box, specify the
center frequency in the block dialog box, and click the **View
Filter Response** button.

### **Center frequency** — Center frequency of desired band `0` (default) | real scalar

Specify the center frequency of the desired band as a real scalar in Hz
or in normalized frequency units *(since R2024b)*.
The center frequency must be in the range [–*Fs*/2,
*Fs*/2], where *Fs* is the sample rate
of the input signal. If you set **Sample rate mode** to
`Inherit from input port` or
`Specify on dialog`, the block inherits
*Fs* from the input signal or uses the value of the
**Input sample rate (Hz)** parameter, respectively.
If you set **Sample rate
mode** to `Use normalized frequency (0 to
1)`, the block sets *Fs* to
2 *(since R2024b)*.

**Tunable:** Yes

**Data Types:** `single` | `double`

### **Stopband attenuation (dB)** — Stopband attenuation in dB `80` (default) | positive scalar

Specify the stopband attenuation of the filter as a finite positive scalar
in dB.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Passband ripple (dB)** — Passband ripple in dB `1` (default) | positive scalar

Specify the passband ripple of the filter as a positive scalar in
dB.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Bandwidth` or
`Decimation factor and bandwidth`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Transition width** — Transition width `0.0045` (default) | positive scalar

Specify the transition width of the filter as a positive scalar in Hz
or in normalized frequency
units *(since R2024b)*.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Reduce number of complex coefficients** — Minimize number of complex coefficients `on` (default) | `off`

Select this parameter to minimize the number of complex coefficients. When
you select this parameter, the first stage of the multistage filter is
bandpass (with complex coefficients) centered at the specified center
frequency. The first stage is followed by a mixing stage that heterodynes
the signal to DC. The remaining filter stages, all with real coefficients,
follow.

When you clear the parameter, the input signal is first passed through the
different stages of the multistage filter. All stages are bandpass (complex
coefficients). The signal is then heterodyned to DC if **Mix signal
to baseband** parameter is selected and the frequency offset
resulting from the decimation is nonzero.

### **Mix signal to baseband** — Mix signal to baseband `on` (default) | `off`

Select this parameter to mix the signal to baseband. When you select this
parameter, the block heterodynes the filtered, decimated signal to DC. This
mixing stage runs at the output sample rate of the filter. When you clear
this parameter, the block skips the mixing stage.

#### Dependencies

This parameter applies when you clear the **Reduce number of
complex coefficients** parameter.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2024b*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to 1)`
  –– Specify the center frequency, transition width, and bandwidth
  in normalized frequency units (0 to 1).
- `Specify on dialog` –– Specify the
  input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal. The block
  calculates the sample rate based on the sample time of the input
  port.

### **Input sample rate (Hz)** — Input sample rate in Hz `44100` (default) | real positive scalar

Specify the sampling rate of the input signal *Fs* in Hz
as a real positive scalar.

#### Dependencies

To enable this parameter, set
the **Sample rate mode** parameter to
`Specify on dialog`. *(since R2024b)*

**Data Types:** `single` | `double`

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals `off` (default) | `on`

*Since R2023a*

Specify whether fixed-size input signals (whose size does not change
during simulation) can have an arbitrary frame length, where the frame
length does not have to be a multiple of the decimation factor. The block
uses this parameter only for fixed-size input signals and ignores it if the
input data varies in size during simulation.

When the input signal is a variable-size signal, the signal can have an
arbitrary frame length, that is, the frame length does not have to be a
multiple of the decimation factor.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor. If the input is not a multiple of the
  decimation factor, then the output is generally a variable-size
  signal. Therefore, to support arbitrary input size, the block
  must also support variable-size operations, which you can enable
  by selecting the **Allow arbitrary frame length for
  fixed-size input signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation factor.

### **View Filter Response** — Visualize frequency response button

Click this button to open the filter visualizer and display the magnitude
response of the complex bandpass decimator. The response is based on the
parameters you select in the block dialog box. To update the response while
the visualizer is running, modify the parameters in the dialog box and click
**Apply**.

You can configure the plot settings and the frequency response measurements
from the interface of the visualizer.

On the **Scope** tab, you can enable the legend, specify
to plot both magnitude and phase responses of the filter, modify the plot
settings, generate a script to re-create the plot, and even save or share
the settings. On the **Measurements** tab, you can enable
data cursors, and display the peak values of the filter response.

For more details on the filter visualizer interface and its tools, see
Configure Filter Visualizer.

#### Dependencies

To enable this button, do not specify any filter specifications from
the input port.

### **View Info** — View filter information button

Display filter information of the Complex Bandpass
Decimator block.

This button brings the functionality of the `info`
analysis method into the Simulink® environment.

#### Dependencies

To enable this button, do not specify any filter specifications from
the input port.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.
## Libraries

DSP System Toolbox / Filtering / Multirate Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `Yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Complex Bandpass Decimator block supports SIMD code generation
using Intel AVX2 code replacement library under these conditions:

- Input signal is complex-valued.
- Input signal has a data type of `single` or
  `double`.

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

## Version History

**Introduced in R2018a**

### R2024b: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the center frequency, transition width, and bandwidth in normalized frequency units
(0 to 1).

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2023a: Support for arbitrary input frame length

This block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and you select the **Allow arbitrary frame
  length for fixed-size input signals** parameter.
- Input signal is a variable-size signal (frame length changes during
  simulation).

When this block supports an input signal with an arbitrary frame length, the input
frame length does not have to be a multiple of the decimation factor and the output
signal is a variable-size signal.

## Description

Extract a frequency subband using a one-sided (complex) bandpass decimator

The Complex Bandpass Decimator block extracts a specific subband of
frequencies using a one-sided, multistage, complex bandpass decimator. The block
determines the bandwidth of interest using the specified center frequency, decimator
factor, and bandwidth values.

This block supports C/C++ code generation and SIMD code generation. For details, see
Code Generation.
