---
type: simulink-block
title: 'Wavelet Scattering'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Transforms / Cosine and Wavelet Transforms'
documentation_page: 'waveletscattering'
documentation_source_path: 'ref/waveletscattering.html'
language: en
---

# Wavelet Scattering

## Ports

### Input

### **Input** — Input signal vector | matrix

Specify the input signal as a vector or a matrix. The block treats each column in
the matrix as a separate channel. For example, the block treats a
1-by-*Nchann* row vector as *Nchann* separate
channels.

When the input data type is `single`, the block performs internal
operations in single-precision. The input data type determines the precision of the
scattering decomposition in the filter banks.

The input frame length does not have to match the signal length specified in the
block dialog box. The block uses a buffer to feed the wavelet scattering algorithm
with frames of length **Signal length (samples)**. If the input frame
size does not match the signal length, the block runs in multirate mode.

**Data Types:** `single` | `double`
### Output

### **Output** — Output signal matrix | 3-D array

Output signal, returned as a matrix or a 3-D array.

For a column vector input, the output dimensions are
*Npath*-by-*Nscat*, where *Npath*
is the number of scattering paths and *Nscat* is the number of
scattering coefficients in each path, or the resolution of the scattering
coefficients.

For matrix inputs, the output dimensions are
*Npath*-by-*Nscat*-by-*Nchann*,
where *Nchann* is the number of columns in the input.

**Data Types:** `single` | `double`

## Parameters

### **Signal length (samples)** — Signal length in samples `1024` (default) | positive integer ≥ 16

Specify the signal length in samples as a positive integer ≥ 16.

The input frame length does not have to match the signal length. The block uses a
buffer to feed the wavelet scattering algorithm with frames of length **Signal
length**. If the input frame size does not match the signal length, the block
runs in multirate mode.

**Data Types:** `double`

### **Overlap length (Samples)** — Overlap length in samples `0` (default) | positive integer

Specify the overlap (in samples) between consecutive frames of a signal as a
nonnegative integer.

**Data Types:** `double`

### **Specify sample rate** — Specify sample rate off (default) | on

Specify the sample rate on the block dialog using the `Sample rate
(Hz)` parameter. If you do not select this check box, the frequencies are in
cycles/sample and the Nyquist frequency is ½.

**Data Types:** `Boolean`

### **Sample rate (Hz)** — Sample rate `16e3` (default) | positive scalar

Specify the sample rate in Hz as a positive scalar.

#### Dependencies

To enable this parameter, select the **Specify sample rate**
parameter.

**Data Types:** `double`

### **Invariance scale (samples)** — Scattering transform invariance scale in samples `512` (default) | positive integer

Specify the scattering transform invariance scale in samples as a positive integer.
Invariance scale specifies the translation invariance of the scattering transform.

If you do not specify the sample rate, invariance scale is measured in samples. If
you specify the sample rate, invariance scale is measured in seconds.

Invariance scale cannot exceed the signal length. If signal length is 1000 samples
and you do not specify a sample rate, the maximum value of the invariance scale is 1000
samples.

#### Dependencies

To enable this parameter, clear the **Specify sample rate**
parameter.

**Data Types:** `double`

### **Invariance scale (s)** — Scattering transform invariance scale in seconds `0.032` (default) | positive scalar

Specify the scattering transform invariance scale in samples as a positive scalar.
Invariance scale specifies the translation invariance of the scattering transform.

If you do not specify the sample rate, invariance scale is measured in samples. If
you specify the sample rate, invariance scale is measured in seconds. By default,
invariance scale is one-half the signal length.

Invariance scale cannot exceed the signal length. If signal length is 1000 samples
and you specify a sample rate of 200 Hz, then the maximum value of the invariance scale
is 5.

#### Dependencies

This parameter appears only when you select the **Specify sample
rate** parameter.

**Data Types:** `double`

### **Quality factors** — Quality factors for scattering filter banks [`8`,`1`] (default) | positive integer | vector of monotonically decreasing positive integers

Specify the quality factors for the scattering filter banks as a positive integer or
a vector of monotonically decreasing positive integers. A filter bank quality factor is
the number of wavelet filters per octave. Quality factors cannot exceed 32 and must be
greater than or equal to 1.

By default, the wavelet scattering network the block creates has two filter banks.
The first filter bank has a quality factor of eight wavelets per octave and the second
filter bank has a quality factor of 1 wavelet per octave.

**Data Types:** `double`

### **Reduce the number of scattering paths** — Optimize scattering transform off (default) | on

Specify whether to optimize the scattering transform and reduce the number of
scattering paths.

When you select this parameter, the algorithm reduces the number of scattering paths
to compute based on a bandwidth consideration. The scattering transform excludes
scattering paths of order 2 and greater that do not satisfy this criterion:

The center frequency minus ½ the 3-dB bandwidth of the wavelet filter in the
(*i*+1)th filter bank must overlap 0 (DC)
plus ½ the 3-dB bandwidth of the wavelet filter in the
*i*th filter bank.

If this criterion is not satisfied, the higher-order path is excluded. Selecting the
**Reduce the number of scattering paths** parameter can significantly
reduce the number of scattering paths and computational complexity of the scattering
transform for most networks.

**Data Types:** `Boolean`

### **Oversampling factor** — Oversampling factor `0` (default) | nonnegative integer | `Inf`

Specify the oversampling factor as a nonnegative integer or `Inf`.

The oversampling factor specifies the factor by which the number of scattering
coefficients per signal increase on a log2 scale. By default, the
**Oversampling factor** is set to `0`, which
corresponds to critically downsampling the coefficients. To obtain a fully undecimated
scattering transform, set **Oversampling factor** to
`Inf`.

Setting **Oversampling factor** to a value that results in more
coefficients than samples is equivalent to setting **Oversampling
factor** to `Inf`. Increasing the **Oversampling
factor** significantly increases the computational complexity and memory
requirements of the scattering transform.

If you set **Oversampling factor** to 2, the scattering transform
returns `22` times as many coefficients for
each scattering path with respect to the critically sampled number.

**Data Types:** `double`

### **Boundary signal extension** — Signal extension method `periodic` (default) | `reflection`

Specify the signal extension method to apply at the boundary as:

- `periodic` — Extend signal periodically to length
  `2^ceil(log2(N))`, where *N* is the signal
  length.
- `reflection` — Extend signal by reflection to length
  `2^ceil(log2(2N))`, where *N* is the signal
  length.

The signal is extended to match the length of the wavelet filters. The
length of the filters are powers of two.

The signal extension method is for internal operations. Results are downsampled back
onto the scale of the original signal before being returned.

### Scattering coefficients

### **Include zeroth-order coefficients** — Include zeroth-order coefficients off (default) | on

Specify whether to include the zeroth-order coefficients.

**Data Types:** `Boolean`

### **Normalization** — Coefficient normalization `none` (default) | `parent`

Specify the type of normalization to apply to the scattering coefficients as
`none` or `parent`. If specified
as `parent`, scattering coefficients of order greater than 0
are normalized by their parents along the scattering path.

### **Transform** — Transformation on coefficients `none` (default) | `log`

Specify the type of transformation to apply to the scattering coefficients as
`none` or `log`.

## Libraries

DSP System Toolbox / Feature Extractors

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

This block does not support code generation if the dynamic memory allocation is off. To
turn on the dynamic memory allocation, run this command in the MATLAB command
prompt.

```
set_param(gcs,'MATLABDynamicMemAlloc','on')
```

## Version History

**Introduced in R2022b**

## Description

Model wavelet scattering network in Simulink

The Wavelet Scattering block creates a framework for wavelet time
scattering in the Simulink® environment. Use this block to derive low-variance features from real-valued
data and then use those features in machine learning and deep learning applications. The block
uses predefined wavelet filters to compute the scalogram and applies an averaging filter to
the scalogram for feature extraction. For more information, see Wavelet Scattering (Wavelet Toolbox). To perform wavelet
scattering in MATLAB®, use the `waveletScattering` (Wavelet Toolbox) function.

The Wavelet Scattering block requires Wavelet Toolbox™.
