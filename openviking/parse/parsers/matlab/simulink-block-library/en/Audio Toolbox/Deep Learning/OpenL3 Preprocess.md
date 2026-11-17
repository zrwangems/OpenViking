---
type: simulink-block
title: 'OpenL3 Preprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'openl3preprocessblock'
documentation_source_path: 'ref/openl3preprocessblock.html'
language: en
---

# OpenL3 Preprocess

## Ports
```yaml
ports:
- name: Port_1
  summary: Sound data column vector
  direction: input
  data_types: single | double
- name: Port_1
  summary: Spectrogram matrix
  direction: output
  data_types: single
```

### Input

### **Port\_1** — Sound data column vector

Sound data, specified as a one-channel signal (column vector). If **Sample
rate of input signal (Hz)** is 48e3, there are no restrictions on the input
frame length. If **Sample rate of input signal (Hz)** is different
from 48e3, then the input frame length must be a multiple of the decimation factor of
the resampling operation that the block performs. If the input frame length does not
satisfy this condition, the block throws an error message with information on the
decimation factor.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Spectrogram matrix

Spectrogram generated from input audio, returned as a matrix whose size depends on
the value of the **Spectrum type** parameter.

- `Mel (128 bands)` –– The block returns a mel
  spectrogram of size 128-by-199, where 128 is the number of mel bands, and 199 is
  the number of time hops.
- `Mel (256 bands)` –– The block returns a mel
  spectrogram of size 256-by-199, where 256 is the number of mel bands, and 199 is
  the number of time hops.
- `Linear` –– The block returns a positive one-sided
  spectrogram of size 257-by-197, where 257 is the FFT length and 197 is the number
  of time hops.

You can use this spectrogram as input to an OpenL3 block
that has the same **Spectrum type**.

**Data Types:** `single`
## Parameters
```yaml
parameters:
- name: Sample rate of input signal (Hz)
  summary: Sample rate of input signal in Hz 48e3 (default) | positive scalar
  group: ''
- name: Overlap percentage (%)
  summary: Overlap percentage between consecutive spectrograms 90 (default) | [0 100)
  group: ''
- name: Spectrum type
  summary: Type of spectrum Mel (128 bands) (default) | Mel (256 bands) | Linear
  group: ''
```

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `48e3` (default) | positive scalar

Sample rate of the input signal in Hz, specified as a positive scalar.

### **Overlap percentage (%)** — Overlap percentage between consecutive spectrograms `90` (default) | [0 100)

Specify the overlap percentage between consecutive spectrograms as a scalar in the
range [0 100).

### **Spectrum type** — Type of spectrum `Mel (128 bands)` (default) | `Mel (256 bands)` | `Linear`

Type of spectrum generated from input audio, specified as `Mel (128
bands)`, `Mel (256 bands)`, or
`Linear`.
## Libraries

Audio Toolbox / Deep Learning

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

**Introduced in R2022b**

## Description

Preprocess audio for OpenL3 embeddings extraction

The OpenL3 Preprocess block generates spectrograms from an audio input. You
can then feed these spectrograms to an OpenL3 pretrained network or to a network that accepts
the same inputs as OpenL3.
