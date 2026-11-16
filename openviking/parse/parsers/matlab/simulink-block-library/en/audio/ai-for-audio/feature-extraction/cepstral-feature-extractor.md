---
type: simulink-block
title: 'Cepstral Feature Extractor'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Feature Extraction'
documentation_page: 'cepstralfeatureextractor'
documentation_source_path: 'ref/cepstralfeatureextractor.html'
language: en
---

# Cepstral Feature Extractor

## Ports

### Input

### **Port\_1** — Audio input to cepstral feature extractor column vector | matrix

Audio input to the cepstral feature extractor, specified as a column
vector or a matrix. If specified as a matrix, the columns are treated as
independent audio channels.

**Data Types:** `single` | `double`
### Output

### **coeffs** — Cepstral coefficients column vector | matrix

Cepstral coefficients, returned as a column vector or a matrix. If the
coefficients matrix is an *N*-by-*M*
matrix, *N* is determined by the values you specify in
the **Number of coefficients to return** and
**Log energy usage** parameters.
*M* equals the number of input audio
channels.

When the **Log energy usage** parameter is set to:

- `Append` –– The block prepends
  the log energy value to the coefficients vector. The length
  of the coefficients vector is 1 +
  *NumCoeffs*, where
  *NumCoeffs* is the value specified in
  the **Number of coefficients to return**
  parameter.
- `Replace` –– The block replaces
  the first coefficient with the log energy of the signal. The
  length of the coefficients vector is
  *NumCoeffs*.
- `Ignore` –– The block does not
  calculate or return the log energy.

This port is unnamed until you select **Output
delta** parameter, the **Output
delta-delta** parameter, or both.

**Data Types:** `single` | `double`

### **delta** — Change in coefficients column vector | matrix

Change in coefficients over consecutive calls to the algorithm,
returned as a column vector or a matrix. The **delta**
array is of the same size and data type as the
**coeffs** array.

#### Dependencies

To enable this port, select the **Output delta**
parameter.

**Data Types:** `single` | `double`

### **deltaDelta** — Change in delta values column vector | matrix

Change in **delta** values over consecutive calls to
the algorithm, returned as a column vector or a matrix. The
**deltaDelta** array is the same size and data type
as the **coeffs** and **delta**
arrays.

#### Dependencies

To enable this port, select the **Output
delta-delta** parameter.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Filter bank type** — Type of filter bank `Mel` (default) | `Gammatone`

Type of filter bank, specified as either `Mel` or
`Gammatone`:

- `Mel` –– The block computes the mel
  frequency cepstral coefficients (MFCC).
- `Gammatone` –– The block computes the
  gammatone cepstral coefficients (GTCC).

**Tunable:** No

### **Domain of the input signal** — Input signal domain `Time` (default) | `Frequency`

Input signal domain, specified as either `Time`
or `Frequency`.

**Tunable:** No

### **Number of coefficients to return** — Number of coefficients to return `13` (default) | positive integer

Number of coefficients to return, specified as an integer in the range [2,
*v*], where *v* is the number of valid
passbands. The number of valid passbands depends on the type of filter bank:

- `Mel` –– The number of valid
  passbands is defined as `sum(κ <=
  floor(fs/2))-2`, where `κ` is the
  number of band edges in the mel filter bank and
  `fs` is the sample rate.
- `Gammatone` –– The number of valid
  passbands is defined as `ceil(hz2erb(R(2))-hz2erb(R(1)))`,
  where `R` is the frequency range of the
  gammatone filter bank.

**Tunable:** No

**Data Types:** `single` | `double`

### **Nonlinear rectification** — Type of nonlinear rectification `Log` (default) | `Cubic-Root`

Type of nonlinear rectification applied prior to the discrete cosine
transform.

**Tunable:** No

### **Inherit FFT length from input dimensions** — Inherit FFT length from input `on` (default) | `off`

When you select this parameter, the FFT length is equal to the number of
rows in the input signal.

**Tunable:** No

#### Dependencies

To enable this parameter, set **Domain of the input
signal** to `Time`.

### **FFTLength** — FFT length `[]` (default) | positive integer

FFT length, specified as a positive integer. The default,
`[]`, means that the FFT length is equal to the number
of rows in the input signal.

**Tunable:** No

#### Dependencies

To enable this parameter, set **Domain of the input
signal** to `Time` and select the
**Inherit FFT length from input dimensions**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Log energy usage** — Specify how the log energy is shown `Append` (default) | `Replace` | `Ignore`

Specify how the log energy is shown in the coefficients vector output,
specified as:

- `Append` –– The block prepends the
  log energy to the coefficients vector. The length of the
  coefficients vector is 1 + *NumCoeffs*, where
  *NumCoeffs* is the value specified in the
  **Number of coefficients to return**
  parameter.
- `Replace` –– The block replaces the
  first coefficient with the log energy of the signal. The length
  of the coefficients vector is
  *NumCoeffs*.
- `Ignore` –– The block does not
  calculate or return the log energy.

**Tunable:** No

### **Output delta** — Output delta values `off` (default) | `on`

When you select this parameter, an additional output port,
**delta**, is added to the block. This port outputs the
change in coefficients over consecutive calls to the algorithm.

**Tunable:** No

### **Output delta-delta** — Output delta-delta values `off` (default) | `on`

When you select this parameter, an additional output port,
**deltaDelta**, is added to the block. This port
outputs the change in delta values over consecutive calls to the
algorithm.

**Tunable:** No

### **Inherit sample rate from input** — Specify source of input sample rate `off` (default) | `on`

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, you specify the sample rate
in **Input sample rate (Hz)** parameter.

**Tunable:** No

### **Input sample rate (Hz)** — Sample rate of input `16000` (default) | positive scalar

Input sample rate in Hz, specified as a real positive scalar.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.
- `Interpreted execution` –– Simulate model
  using the MATLAB® interpreter. This option shortens startup time but has
  a slower simulation speed than `Code
  generation`. In this mode, you can debug the source
  code of the block.

**Tunable:** No

#### Advanced Tab

### **Gammatone frequency range (Hz)** — Frequency range of gammatone filter bank (Hz) `[50 8000]` (default) | two-element row vector

Frequency range of the gammatone filter bank in Hz, specified as a
positive, monotonically increasing two-element row vector. The maximum
frequency range can be any finite number. The center frequencies of the
filter bank are equally spaced across the frequency range on the ERB
scale.

**Tunable:** No

#### Dependencies

To enable this parameter, set **Filter bank type** to
`Gammatone`.

### **Band edges of Mel filter bank (Hz)** — Band edges of mel filter bank row vector

Band edges of the filter bank in Hz, specified as a nonnegative
monotonically increasing row vector in the range [0, ∞). The maximum
bandedge frequency can be any finite number. The number of bandedges must be
in the range [4, 80].

The default band edges are spaced linearly for the first ten and then
logarithmically thereafter. The default band edges are set as recommended by
[1].

**Tunable:** No

#### Dependencies

To enable this parameter, set **Filter bank type** to
`Mel`.

### **Domain for Mel filter bank design** — Mel filter bank design domain `Hz` (default) | `Bin`

Mel filter bank design domain, specified as either
`Hz` or `Bin`. The
filter bank is designed as overlapped triangles with band edges specified by
the **Band edges of filter bank (Hz)** parameter.

The band edges are specified in Hz. When you set the design domain
to:

- `Hz` –– Filter bank triangles are drawn
  in Hz and are mapped onto bins. For details, see [1].
- `Bin` –– The band edge frequencies in
  `Hz` are converted to bins. The filter
  bank triangles are drawn symmetrically in bins. For details, see
  [2].

**Tunable:** No

#### Dependencies

To enable this parameter, set **Filter bank type** to
`Mel`.

### **Filter bank normalization** — Normalize filter bank `Bandwidth` (default) | `Area` | `None`

Normalization technique used to normalize the weights of the filter bank,
specified as:

- `Bandwidth` –– The weights of each
  bandpass filter are normalized by the corresponding bandwidth of
  the filter.
- `Area` –– The weights of each
  bandpass filter are normalized by the corresponding area of the
  bandpass filter.
- `None` –– The weights of the filter
  are not normalized.

**Tunable:** No

## Libraries

Audio Toolbox / Measurements

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2022b: To be removed

The Cepstral Feature Extractor block will be removed in a future
release. Use the MFCC
block or a combination of the Auditory
Spectrogram, Cepstral
Coefficients, and Audio
Delta blocks instead.

| Cepstral Feature Extractor Configuration | Recommended Replacement |
| --- | --- |
| **Filter bank type** parameter set to `Mel` | Use the MFCC block. |
| **Filter bank type** parameter set to `Gammatone` | Use the Auditory Spectrogram block combined with the Cepstral Coefficients block. See Extract GTCC from Audio in Simulink for an example. |
| **Output delta** or **Output delta-delta** parameters selected | If using the MFCC block, select the **Append delta** or **Append delta-delta** parameters. If using the Cepstral Coefficients block instead, use the Audio Delta block to extract delta features. |
| **Log energy usage** parameter set to `Append` or `Replace` | No replacement |
| **Band edges of Mel filter bank (Hz)** parameter specified | No replacement |
| **Domain for Mel filter bank design** parameter set to `Bin` | No replacement |

## Description

(To be removed) Extract cepstral features from audio segment

The Cepstral Feature Extractor block extracts cepstral features from an
audio segment. Cepstral features are commonly used to characterize speech and music
signals.
