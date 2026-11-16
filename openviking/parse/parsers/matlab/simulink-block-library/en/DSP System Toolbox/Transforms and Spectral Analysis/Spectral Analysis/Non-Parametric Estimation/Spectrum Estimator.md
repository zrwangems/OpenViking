---
type: simulink-block
title: 'Spectrum Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Spectral Analysis / Non-Parametric Estimation'
documentation_page: 'spectrumestimator'
documentation_source_path: 'ref/spectrumestimator.html'
language: en
---

# Spectrum Estimator

## Ports

### Input

### **Input** — Input signal vector | matrix

Specify the input signal as a vector or matrix. The block treats each
column of the input as a separate channel. If the input is a
two-dimensional signal, the first dimension represents the channel
length (or frame size) and the second dimension represents the number of
channels. If the input is a one-dimensional signal, then it is
interpreted as a single channel.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **P** — Power spectrum or power-density spectrum vector | matrix

Power spectrum or power-density spectrum that the block estimates,
returned as a vector or a matrix.

**Data Types:** `single` | `double`

### **P\_max** — Max-hold spectrum vector | matrix

Max-hold spectrum, returned as a vector or a matrix. The block
computes the max-hold spectrum by keeping, at each frequency bin, the
maximum value of all the power spectrum estimates.

**Data Types:** `single` | `double`

### **P\_min** — Min-hold spectrum vector | matrix

Min-hold spectrum, returned as a vector or a matrix. The block
computes the min-hold spectrum by keeping, at each frequency bin, the
minimum value of all the power spectrum estimates.

**Data Types:** `single` | `double`

### **F** — Output frequencies column vector

Output frequencies, returned as a column vector.

**Data Types:** `single` | `double`

### **RBW** — Effective resolution bandwidth scalar

Effective resolution bandwidth, returned as a scalar.

**Data Types:** `single` | `double`

## Parameters

### Main Tab

### **Method** — Welch or filter bank `Filter bank` (default) | `Welch`

Specify the spectral estimation method as one of these options.

- `Filter bank` — Analysis
  filter bank splits the broadband input signal into multiple
  narrow subbands. The block computes the power in each narrow
  frequency band, and the computed value is the spectral
  estimate over the respective frequency band.
- `Welch` — The block uses
  the Welch averaged modified periodograms method to compute
  the power spectrum over the narrow subbands.

### **Number of taps per band** — Number of filter taps per frequency band `12` (default) | positive integer

Specify the number of filter coefficients, or taps, for each frequency
band as a positive integer. This value corresponds to the number of
filter coefficients per polyphase branch. The total number of filter
coefficients is equal to **Number of taps per band**
times the FFT length.

#### Dependencies

To enable this parameter, set **Method** to
`Filter bank`.

### **Spectrum type** — Type of spectrum `Power` (default) | `Power density`

Specify the type of spectrum to compute one of these:

- `Power` — Compute the
  power spectrum.
- `Power density` — Compute
  the power spectral density.

### **Frequency resolution method** — Frequency resolution method `Auto` (default) | `RBW` | `Number of frequency bands`

Specify the frequency resolution method as one of these options.

- `Auto` — The
  Spectrum Estimator block computes the
  resolution bandwidth (RBW) so that the frequency span fits
  1024 RBW intervals.

  - Welch method — The window length,
    *winLen*, is calculated using winLen=NENBW×Fs/RBW. *NENBW* is the
    equivalent noise bandwidth of the window and
    *Fs* is the sample rate.
  - Filter bank method — The FFT length is
    the ceiling of the ratio of **Sample rate
    (Hz)** to the computed resolution
    bandwidth.
- `RBW` — Specify the
  resolution bandwidth, which is used to determine the window
  length (Welch method) or the FFT length (filter bank
  method). When the block uses the Welch method, the behavior
  is equivalent to that of the Spectrum Analyzer
  block. The window length is calculated using winLen=NENBW×Fs/RBW. *NENBW* is the
  equivalent noise bandwidth of the window and
  *Fs* is the sample rate. The FFT length
  is equal to the ceiling of the ratio of **Sample
  rate (Hz)** to **RBW
  (Hz)**.
- `Window length` — Specify
  the window or segment length to use in the Welch algorithm.
  This option is available when you set
  **Method** to
  `Welch`.
- `Number of frequency bands`
  — Specify the number of polyphase branches of the
  analysis filter bank. This value corresponds to the FFT
  length that the filter bank uses. To enable this option, set
  **Method** to `Filter
  bank`.

### **RBW (Hz)** — Resolution bandwidth `5` (default) | positive scalar

Specify the resolution bandwidth as a positive scalar in Hz. The
ceiling of the ratio of the frequency span to RBW must be greater than
`2`.

#### Dependencies

To enable this parameter, set **Frequency resolution
method** to `RBW`.

### **Window length source** — Source of window length `Same as input frame length` (default) | `Specify on dialog`

Specify the source of the window length value as one of these:

- `Same as input frame length`
  — Window length is equal to the frame size of the
  input. Specify this option to obtain behavior equivalent to
  that of the Periodogram
  block.
- `Specify on dialog` —
  Window length is the value you specify in the
  **Window length** parameter.

#### Dependencies

To enable this parameter, set

- **Method** to
  `Welch`.
- **Frequency resolution method** to
  `Window length`.

### **Window length** — Window length `1024` (default) | positive integer

Specify the length of the window used to compute the spectrum estimate
as a positive integer scalar greater than `2`.

#### Dependencies

To enable this parameter, set

- **Method** to
  `Welch`.
- **Frequency resolution method** to
  `Window length`.
- **Window length source** to
  `Specify on dialog`.

### **Number of bands source** — Source of number of frequency bands `Same as input frame size` (default) | `Specify on dialog`

Specify the source of the number of frequency bands as one of these:

- `Same as input frame length`
  — The FFT length is equal to the frame size of the
  input.
- `Specify on dialog` — The
  FFT length is the value you specify in **Number of
  bands**.

#### Dependencies

To enable this parameter, set

- **Method** to `Filter
  bank`.
- **Frequency resolution method** to
  `Number of frequency
  bands`.

### **Number of bands** — Number of frequency bands `1024` (default) | positive scalar

Specify the number of frequency bands or the FFT length the filter bank uses to compute
the power spectral estimate as a positive scalar.

#### Dependencies

To enable this parameter, set

- **Method** to `Filter
  bank`.
- **Frequency resolution method** to
  `Number of frequency
  bands`.
- **Number of bands source** to
  `Specify on dialog`.

### **FFT length source** — Source of FFT length value `Auto` (default) | `Property`

Specify the source of the FFT length value as one of these:

- `Auto` — The block sets
  the FFT length to the frame size of the input.
- `Property` — The block
  sets the FFT length to the value you specify in
  **FFT length**.

#### Dependencies

To enable this parameter, set

- **Method** to
  `Welch`.
- **Frequency resolution method** to
  `Window length`.

### **FFT length** — FFT length `1024` (default) | positive integer

Specify the FFT length as a positive integer. The block uses this to compute the
spectrum estimates.

#### Dependencies

To enable this parameter, set

- **Method** to
  `Welch`.
- **Frequency resolution method** to
  `Window length`.
- **FFT length source** to
  `Property`.

### **Inherit sample rate from input** — Inherit sample rate from input `on` (default) | `off`

When you select this check box, the block algorithm computes the block sample rate as
*N*/*Ts*,
where *N* is the frame size of the input signal and
*Ts* is the sample time
of the input signal. By default, the block inherits its sample rate from
the input signal. When you clear this check box, the block sample rate
is the value you specify in **Sample rate
(Hz)**.

#### Dependencies

To enable this parameter, do one of the following:

- Set **Method** to
  `Welch` and
  **Frequency resolution method** to
  `Window length`.
- Set **Method** to `Filter
  bank` and **Frequency
  resolution method** to `Number
  of frequency bands`.

### **Sample rate (Hz)** — Sample rate of input `44100` (default) | scalar

Specify the sample rate of the input signal as a positive
scalar.

#### Dependencies

To enable this parameter, do one of the following:

- Set **Frequency resolution method**
  to `Auto` or
  `RBW`.
- Set **Method** to
  `Welch`,
  **Frequency resolution method** to
  `Window length`, and clear
  the **Inherit sample rate from input**
  check box.
- Set **Method** to `Filter
  bank`, **Frequency resolution
  method** to `Number of
  frequency bands`, and clear the
  **Inherit sample rate from input**
  check box.

### **Window function** — Window function `Hann` (default) | `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

Specify the window function used by the Welch algorithm as
`Chebyshev`, `Flat
Top`, `Hamming`,
`Hann`, `Kaiser`,
or `Rectangular`. The default value is
`Hann`.

#### Dependencies

To enable this parameter, set **Method** to
`Welch`.

### **Sidelobe attenuation of window (dB)** — Sidelobe attenuation of window `60` (default) | positive scalar

Specify the sidelobe attenuation of the window in dB as a positive scalar greater than
or equal to `45`.

#### Dependencies

To enable this parameter, set **Method** to
`Welch` and **Window
function** to `Chebyshev` or
`Kaiser`.

### **Averaging method** — Averaging method `Exponential` (default) | `Running`

Specify the averaging method as `Exponential`
(default) or `Running`. In the exponential
method, the block computes the average over samples weighted by an
exponentially decaying forgetting factor. In the running averaging
method, the block computes an equally weighted average of specified
number of spectrum estimates defined by **Number of spectral
averages** parameter.

### **Number of spectral averages** — Number of spectral averages `1` (default) | positive integer

Specify the number of spectral averages as a positive integer. The
spectrum estimator computes the current power spectrum estimate by
averaging the last *N* power spectrum estimates, where
*N* is the number of spectral averages defined in
**Number of spectral averages**.

#### Dependencies

To enable this parameter, set **Averaging
method** to `Running`.

### **Specify forgetting factor from input port** — Specify forgetting factor from input port `off` (default) | `on`

Select this check box to specify the forgetting factor from an input port. When you do
not select this check box, you must specify the forgetting factor
through the **Forgetting factor** parameter.

#### Dependencies

To enable this parameter, set **Averaging
method** to
`Exponential`.

### **Forgetting factor** — Forgetting factor `0.9` (default) | scalar in the range (`0,1`]

Specify the exponential weighting forgetting factor as a scalar value greater than 0 and
smaller than or equal to 1.

#### Dependencies

To enable this parameter, set **Averaging
method** to `Exponential` and
clear the **Specify forgetting factor from input
port** parameter.

### Advanced Tab

### **Window overlap (%)** — Percentage of overlap between windows `0` (default)

Specify the percentage of overlap between successive data windows as a
scalar from `0` and `100`.

#### Dependencies

To enable this parameter, on the **Main Tab**,
set **Method** to
`Welch`.

### **Reference load (ohms)** — Reference load `1` (default) | positive scalar

Specify the load used as a reference to compute the power values as a
real positive scalar expressed in ohms.

### **Frequency range** — Frequency range of spectrum estimator `Centered` (default) | `One-sided` | `Two-sided`

Specify the frequency range of the spectrum estimator as one of these:

- `Centered` — The spectrum
  estimator computes the centered two-sided spectrum of a
  complex or real input signal. The length of the spectrum
  estimate is equal to the FFT length. The spectrum estimate
  is computed over the frequency range
  (`-SampleRate/2 SampleRate/2`]
  when the FFT length is even and
  `(-SampleRate/2 SampleRate/2)`
  when the FFT length is odd.
- `One-sided` — The spectrum
  estimator computes the one-sided spectrum of a real input
  signal. When the FFT length, `NFFT`, is
  even, the spectrum estimate has length
  (`NFFT`/`2`) + `1`
  and is computed over the frequency range
  `[0 SampleRate/2]`.
  `SampleRate` is the sample rate of the
  input signal. When `NFFT` is odd, the
  spectrum estimate has length
  (`NFFT` + 1)/`2`
  and is computed over the frequency range
  [`0 SampleRate/2`).
- `Two-sided` — The spectrum
  estimator computes the two-sided spectrum of a complex or
  real input signal. The length of the spectrum estimate is
  equal to the FFT length. The spectrum estimate is computed
  over the frequency range
  [`0 SampleRate`), where
  `SampleRate` is the sample rate of the
  input signal.

### **Power units** — Power units `dBm` (default) | `Watts` | `dBW`

Specify the units used to measure power as one of these:

- `dBm` — The spectrum
  estimator measures power in decibel-milliwatts.
- `Watts` — The spectrum
  estimator measures power in watts.
- `dBW` — The spectrum
  estimator measures power in decibel-watts.

### **Output max-hold spectrum** — Output max-hold spectrum `off` (default) | `on`

When you select this check box, the block outputs the max-hold
spectrum of the input signal through the **P\_max**
port. The block computes the max-hold spectrum by keeping, at each
frequency bin, the maximum value of all the power spectrum estimates. By
default, this check box is not selected.

### **Output min-hold spectrum** — Output min-hold spectrum `off` (default) | `on`

When you select this check box, the block outputs the min-hold
spectrum of the input signal through the **P\_min**
port. The block computes the min-hold spectrum by keeping, at each
frequency bin, the minimum value of all the power spectrum estimates. By
default, this check box is not selected.

### **Output frequency vector** — Output frequency vector `off` (default) | `on`

When you select this check box, the block outputs the frequency vector
through the **F** port. By default, this check box is
not selected.

### **Output effective RBW** — Output effective RBW `off` (default) | `on`

When you select this check box, the block computes and outputs the
effective resolution bandwidth through the **RBW**
port. By default, this check box is not selected.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run as one of these:

- `Interpreted execution` —
  Simulate model using the MATLAB®  interpreter. This option shortens
  startup time.
- `Code generation` —
  Simulate model using generated C code. The first time you
  run a simulation, Simulink® generates C code for the block. The C code is
  reused for subsequent simulations, as long as the model does
  not change. This option requires additional startup time but
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

**Introduced in R2015b**

## Description

Estimate power spectrum or power-density spectrum

The Spectrum Estimator block outputs the power spectrum or
power-density spectrum of a real or complex input signal, using the Welch method of
averaged modified periodograms and the filter bank approach.

When you choose the filter bank approach, the block uses an analysis filter bank to
estimate the power spectrum. The filter bank approach produces a spectral estimate with
a higher resolution, a more accurate noise floor, and more precise peaks than the Welch
method, with low or no spectral leakage. They come at the expense of increased
computation and slower tracking.

When you choose the Welch method, the block computes the averaged modified
periodograms to compute the spectral estimate. The block buffers the input data into
overlapping segments. Use the block parameters to set the length of the data segments,
the amount of data overlap between consecutive segments, and other features of the power
spectrum.

For more information on the Welch method and the filter bank method, see Algorithms.
