---
type: simulink-block
title: 'Cross-Spectrum Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Spectral Analysis / Non-Parametric Estimation'
documentation_page: 'crossspectrumestimator'
documentation_source_path: 'ref/crossspectrumestimator.html'
language: en
---

# Cross-Spectrum Estimator

## Ports

### Input

### **x** — First data input vector | matrix

Specify the first data input as a vector or a matrix. The block treats each column of
the input signal as a separate channel. If the input is a
two-dimensional signal, the first dimension represents the channel
length (or frame size) and the second dimension represents the number of
channels. If the input is a one-dimensional signal, then the block
interprets it as a single-channel signal.

The inputs, *x* and *y*, must have the same size and
data type.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **y** — Second data input vector | matrix

Specify the second data input as a vector or a matrix. The block treats each column of
the input signal as a separate channel. If the input is a
two-dimensional signal, the first dimension represents the channel
length (or frame size) and the second dimension represents the number of
channels. If the input is a one-dimensional signal, then the block
interprets it as a single-channel signal.

The inputs, *x* and *y*, must have the same size and
data type.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Output** — Cross-power spectrum density vector | matrix

Cross-power spectrum density estimated by the block, returned as a
vector or a matrix. The output has the same size and data type as the
input signals.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

## Parameters

### **Window length source** — Window length source `Same as input frame length` (default) | `Specify on dialog`

Specify the source of the window length value as one of these:

- `Same as input frame length`
  (default) — Window length is equal to the frame size of
  the input.
- `Specify on dialog` — Window
  length is the value specified in **Window
  length**.

### **Window length** — Length of window in samples `1024` (default) | positive integer

Specify the length of the window in samples that the block uses to compute
the spectrum estimate as a positive integer greater than
`2`.

#### Dependencies

To enable this parameter, set **Window length
source** to `Specify on
dialog`.

### **Window overlap (%)** — Percentage of overlap between windows `0` (default) | scalar in the range [`0`,`100`)

Specify the percentage of overlap between successive data windows as a
scalar in the range [`0`,`100`).

### **Averaging method** — Averaging method `Running` (default) | `Exponential`

Specify the averaging method as:

- `Running` –– In the running averaging
  method, the block computes an equally weighted average of a
  specified number of spectrum estimates defined by the
  **Number of spectral averages**
  parameter.
- `Exponential` –– In the exponential
  method, the block computes the average over samples weighted by
  an exponentially decaying forgetting factor.

### **Specify forgetting factor from input port** — Specify forgetting factor from input port `off` (default) | `on`

Select this check box to specify the forgetting factor from an input port. When you do
not select this check box, you must specify the forgetting factor through
the **Forgetting factor** parameter in the block dialog
box.

#### Dependencies

To enable this parameter, set **Averaging method** to
`Exponential`.

### **Forgetting factor** — Exponential weighting forgetting factor `0.9` (default) | scalar in the range (`0`,`1`]

Specify the exponential weighting forgetting factor as a scalar in the
range (`0`,`1`].

#### Dependencies

To enable this parameter, set **Averaging method** to
`Exponential` and clear the
**Specify forgetting factor from input port**
parameter.

### **Number of spectral averages** — Number of spectral averages `1` (default) | positive integer

Specify the number of spectral averages as a positive integer. The
spectrum estimator computes the current power spectrum estimate by averaging
the last *N* power spectrum estimates, where
*N* is the number of spectral averages defined in
**Number of spectral averages**.

#### Dependencies

To enable this parameter, set **Averaging method** to
`Running`.

### **FFT length source** — Source of FFT length value `Auto` (default) | `Property`

Specify the source of the FFT length value as one of these:

- `Auto` — FFT length is equal
  to the frame size of the input.
- `Property` — FFT length is the
  value you specify in the **FFT length**
  parameter.

### **FFT length** — FFT length `128` (default) | positive integer

Specify the FFT length the block uses to compute the spectral estimates as
a positive integer.

#### Dependencies

To enable this parameter, set **FFT length source**
to `Property`.

### **Window function** — Window function `Hann` (default) | `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

Specify the window function for the cross-spectrum estimator as
`Chebyshev`, `Flat
Top`, `Hamming`,
`Hann`, `Kaiser`, or
`Rectangular`. The default value is
`Hann`.

### **Sidelobe attenuation of window (dB)** — Sidelobe attenuation of window in dB `60` (default) | positive scalar

Specify the sidelobe attenuation of the window as a positive scalar in
dB.

#### Dependencies

To enable this parameter, set **Window function** to
`Chebyshev` or
`Kaiser`.

### **Frequency range** — Frequency range of the cross-spectrum estimate `Centered` (default) | `One-sided` | `Two-sided`

Specify the frequency range of the cross-spectrum estimator as one of these:

- `Centered` — The
  cross-spectrum estimator computes the centered two-sided
  spectrum of complex or real input signals, *x*
  and *y*. The length of the cross-spectrum
  estimate is equal to the FFT length. The block computes the
  spectrum estimate over the frequency range
  [`-SampleRate/2 SampleRate/2`], where
  `SampleRate` is the sample rate of the
  input signal.
- `One-sided` — The
  cross-spectrum estimator computes the one-sided spectrum of real
  input signals, *x* and *y*.
  When the FFT length, *NFFT* is even, length of
  the cross-spectrum estimate is (*NFFT*/
  `2`) + `1`, and is
  computed over the frequency range [`0
  SampleRate/2`]. When the FFT length,
  *NFFT* is odd, length of the cross-spectrum
  estimate is (*NFFT* + 1)/ `2`,
  and is computed over the frequency range [`0
  SampleRate/2`].
- `Two-sided` — The
  cross-spectrum estimator computes the two-sided spectrum of
  complex or real input signals, *x* and
  *y*. The length of the cross-spectrum
  estimate is equal to the FFT length. The spectrum estimate is
  computed over the frequency range [`0
  SampleRate`].

### **Inherit sample rate from input** — Inherit sample rate from input `on` (default) | `off`

When you select this check box, the block computes the sample rate as
*N*/*Ts*, where *N*
is the frame size of the input signal, and *Ts* is the
sample time of the input signal. When you clear this check box, the block
uses the value you specify in **Sample rate (Hz)**. By
default, this check box is selected.

### **Sample rate (Hz)** — Sample rate of input `44100` (default) | positive scalar

Specify the sample rate of the input signal as a positive scalar.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** check box.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run as one of these:

- `Interpreted execution` —
  Simulate model using the MATLAB® interpreter. This option shortens startup
  time.
- `Code generation` — Simulate
  model using generated C code. The first time you run a
  simulation, Simulink® generates C code for the block. The C code is
  reused for subsequent simulations, as long as the model does not
  change. This option requires additional startup time but
  provides faster subsequent simulations.

## Libraries

DSP System Toolbox / Estimation / Power Spectrum Estimation

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

## Description

Estimate cross-power spectrum density

The Cross-Spectrum Estimator block estimates the cross-power spectrum density
of two input signals, *x* and *y*, using Welch’s
method of averaged modified periodograms. The block buffers the input data into
overlapping segments. You can set the length of the data segment and the amount of data
overlap between segments through the parameters in the block dialog box. The block
computes the current power spectrum estimate by averaging the previous power spectrum
estimates using the method you specify in the **Averaging method**
parameter.
