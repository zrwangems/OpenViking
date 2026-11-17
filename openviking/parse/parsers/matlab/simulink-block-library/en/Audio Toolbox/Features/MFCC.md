---
type: simulink-block
title: 'MFCC'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'mfccblock'
documentation_source_path: 'ref/mfccblock.html'
language: en
---

# MFCC

## Ports
```yaml
ports:
- name: Port_1
  summary: Audio input column vector | matrix
  direction: input
  data_types: single | double
- name: Port_1
  summary: MFCC features matrix | 3-D array
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — Audio input column vector | matrix

Audio input signal, specified as a column vector or a matrix. When you specify a
matrix, the block treats columns as independent audio channels.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — MFCC features matrix | 3-D array

MFCC features returned as a matrix or 3-D array. The features include the MFCCs
themselves and optionally include the delta and delta-delta features of the MFCCs. The
dimensions of the output are
*L*-by-*M*-by-*N*, where:

- *L* is the number of feature vectors, which is specified by
  the **Number of
  feature vectors** parameter.
- *M* is the number of features in each feature vector, which
  is determined by the **Number of
  cepstral coefficients**, **Append
  delta**, and **Append
  delta-delta** parameters.
- *N* is the number of channels in the input audio
  signal.

Trailing dimensions of size 1 are removed from the output.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Window
  summary: Analysis window hamming(1024,'periodic') (default) | real vector
  group: ''
- name: Overlap length
  summary: Number of overlapping samples between adjacent windows 512 (default) | integer in the range [0, windowLength)
  group: ''
- name: Number of cepstral coefficients
  summary: Number of cepstral coefficients in each feature vector 13 (default) | positive integer greater than 1
  group: ''
- name: Rectification
  summary: Type of nonlinear rectification Logarithm (default) | Cubic root
  group: ''
- name: Append delta
  summary: Append delta of MFCCs to feature vectors on (default) | off
  group: ''
- name: Append delta-delta
  summary: Append delta-delta of MFCCs to feature vectors on (default) | off
  group: ''
- name: Delta window length
  summary: Number of coefficients for calculating delta and delta-delta 9 (default) | odd integer greater than 2
  group: ''
- name: Number of feature vectors
  summary: Number of MFCC feature vectors in output 1 (default) | positive integer
  group: ''
- name: Number of overlapped feature vectors
  summary: Number of feature vectors overlapped in output 0 (default) | nonnegative integer
  group: ''
- name: Inherit sample rate from input
  summary: Specify source of input sample rate off (default) | on
  group: ''
- name: Input sample rate (Hz)
  summary: Sample rate of input 44.1e3 (default) | positive scalar
  group: ''
- name: Number of bands
  summary: Number of bands in mel filter bank 32 (default) | positive integer
  group: ''
- name: Auto-determine frequency range
  summary: Automatically determine frequency range on (default) | off
  group: ''
- name: Frequency range (Hz)
  summary: Frequency range of mel filter bank [0,22050] (default) | two-element row vector
  group: ''
- name: Filter bank design domain
  summary: Design domain of mel filter bank linear (default) | warped
  group: ''
- name: Filter bank normalization
  summary: Normalization technique for filter bank bandwidth (default) | area | none
  group: ''
- name: Mel style
  summary: Mel style oshaughnessy (default) | slaney
  group: ''
- name: Normalize window
  summary: Normalize analysis window on (default) | off
  group: ''
- name: Spectrum type
  summary: Type of spectrum power (default) | magnitude
  group: ''
- name: Auto-determine FFT length
  summary: Automatically determine FFT length on (default) | off
  group: ''
- name: FFT length
  summary: Number of DFT points 1024 (default) | positive integer
  group: ''
```

#### Mel-Frequency Cepstral Coefficients

### **Window** — Analysis window `hamming(1024,'periodic')` (default) | real vector

Analysis window applied to the input signal in the time domain, specified as a real
vector.

### **Overlap length** — Number of overlapping samples between adjacent windows `512` (default) | integer in the range [0, `windowLength`)

Number of overlapping samples between adjacent windows, specified as an integer in
the range [0, `windowLength`), where `windowLength` is
the length of the analysis window and is specified by the **Window**
parameter.

### **Number of cepstral coefficients** — Number of cepstral coefficients in each feature vector `13` (default) | positive integer greater than 1

Number of cepstral coefficients in each feature vector, specified as a positive
integer greater than 1.

### **Rectification** — Type of nonlinear rectification `Logarithm` (default) | `Cubic root`

Type of nonlinear rectification applied to the spectrum prior to the discrete cosine
transform, specified as `Logarithm` or `Cubic
root`.

### **Append delta** — Append delta of MFCCs to feature vectors `on` (default) | `off`

When you select this parameter, the block appends the delta of the MFCCs to the
coefficients in each feature vector. The delta is an approximation of the first
derivative of the MFCCs with respect to time. The number of delta features is equal to
the number of MFCCs, which is specified by **Number of cepstral
coefficients**.

### **Append delta-delta** — Append delta-delta of MFCCs to feature vectors `on` (default) | `off`

When you select this parameter, the block appends the delta-delta of the MFCCs to
each output feature vector. The delta-delta is an approximation of the second derivative
of the MFCCs with respect to time. The number of delta-delta features is equal to the
number of MFCCs, which is specified by **Number of cepstral
coefficients**.

The block appends the delta-delta after the delta in the feature vectors if you also
select the **Append delta** parameter.

### **Delta window length** — Number of coefficients for calculating delta and delta-delta `9` (default) | odd integer greater than 2

Number of coefficients for calculating delta and delta-delta, specified as an odd
integer greater than 2.

#### Output Buffering

### **Number of feature vectors** — Number of MFCC feature vectors in output `1` (default) | positive integer

Number of MFCC feature vectors in output, specified as a positive integer. The block
buffers the output to return the specified number of feature vectors.

### **Number of overlapped feature vectors** — Number of feature vectors overlapped in output `0` (default) | nonnegative integer

Number of feature vectors the block overlaps in the output, specified as a
nonnegative integer less than **Number of feature vectors**.

#### Simulation Parameters

### **Inherit sample rate from input** — Specify source of input sample rate `off` (default) | `on`

When you select this parameter, the block inherits its sample rate from the input
signal. When you clear this parameter, you specify the sample rate in the
**Input sample rate (Hz)** parameter.

### **Input sample rate (Hz)** — Sample rate of input `44.1e3` (default) | positive scalar

Input sample rate in Hz, specified as a positive scalar.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

#### Mel Filter Bank Design

### **Number of bands** — Number of bands in mel filter bank `32` (default) | positive integer

Number of bands in mel filter bank, specified as a positive integer.

### **Auto-determine frequency range** — Automatically determine frequency range `on` (default) | `off`

When you select this parameter, the block sets the **Frequency
range** to `[0,fs/2]`, where `fs` is the
sample rate. The block determines the sample rate using the **Inherit sample
rate from input** and **Input sample rate (Hz)**
parameters.

### **Frequency range (Hz)** — Frequency range of mel filter bank `[0,22050]` (default) | two-element row vector

Frequency range in Hz of mel filter bank, specified as a two-element row
vector.

#### Dependencies

To enable this parameter, clear the **Auto-determine frequency
range** parameter.

### **Filter bank design domain** — Design domain of mel filter bank `linear` (default) | `warped`

Design domain of mel filter bank, specified as `linear` or
`warped`.

### **Filter bank normalization** — Normalization technique for filter bank `bandwidth` (default) | `area` | `none`

Normalization technique that the block uses for the filter bank weights, specified
as `bandwidth`, `area`, or
`none`.

- `bandwidth` –– Normalize the weights of each bandpass
  filter by the corresponding bandwidth of the filter.
- `area` –– Normalize the weights of each bandpass
  filter by the corresponding area of the bandpass filter.
- `none` –– The block does not normalize the weights of
  the filters.

### **Mel style** — Mel style `oshaughnessy` (default) | `slaney`

Style of the mel scale, specified as `oshaughnessy` or
`slaney`.

#### Spectrogram

### **Normalize window** — Normalize analysis window `on` (default) | `off`

When you select this parameter, the block applies window normalization.

### **Spectrum type** — Type of spectrum `power` (default) | `magnitude`

Type of spectrum, specified as `power` or
`magnitude`.

### **Auto-determine FFT length** — Automatically determine FFT length `on` (default) | `off`

When you select this parameter, the block automatically sets the FFT length to the
window length. The window length is determined by the **Window**
parameter.

### **FFT length** — Number of DFT points `1024` (default) | positive integer

Number of points used to calculate the DFT, specified as a positive integer.

#### Dependencies

To enable this parameter, clear the **Auto-determine FFT length**
parameter.
## Libraries

Audio Toolbox / Features

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

The MFCC block supports optimized code generation using single
instruction, multiple data (SIMD) instructions. For more information about SIMD code
generation, see Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder).

## Version History

**Introduced in R2022b**

### R2023b: Support for Slaney-style mel scale

Set the **Mel style** parameter to `slaney` to
use the Slaney-style mel scale.

### R2023a: Generate optimized C/C++ code for computing MFCCs

The MFCC block supports optimized C/C++ code generation using single
instruction, multiple data (SIMD) instructions.

## Description

Extract mel-frequency cepstral coefficients from audio

The MFCC block extracts feature vectors containing the mel-frequency
cepstral coefficients (MFCCs), as well as their delta and delta-delta features, from the audio
input signal. MFCCs are popular features extracted from speech signals for use in
classification tasks.
