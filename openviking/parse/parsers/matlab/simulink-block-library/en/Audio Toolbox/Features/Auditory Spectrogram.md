---
type: simulink-block
title: 'Auditory Spectrogram'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'auditoryspectrogramblock'
documentation_source_path: 'ref/auditoryspectrogramblock.html'
language: en
---

# Auditory Spectrogram

## Ports
```yaml
ports:
- name: Port_1
  summary: Audio input column vector | matrix
  direction: input
  data_types: single | double
- name: spec
  summary: Spectrogram matrix | 3-D array
  direction: output
  data_types: single | double
- name: fvec
  summary: Center frequencies row vector
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — Audio input column vector | matrix

Audio input signal, specified as a column vector or a matrix. When you specify a matrix,
the block treats columns as independent audio channels.

**Data Types:** `single` | `double`
### Output

### **spec** — Spectrogram matrix | 3-D array

Spectrogram, returned as a matrix or 3-D array. The dimensions of
**spec** are
*L*-by-*M*-by-*N*, where:

- *L* is the number of spectra, which is
  determined by the **Number of spectra**
  parameter.
- *M* is the number of bands, which is
  determined by the **Auto-determine number of
  bands** and **Number of
  bands** parameters.
- *N* is the number of channels in the
  input audio signal.

Trailing singleton dimensions are removed from the output.

This port is unnamed until you select the **Output center
frequencies** parameter.

**Data Types:** `single` | `double`

### **fvec** — Center frequencies row vector

Center frequencies of the bandpass filters in Hz, returned as a row vector with number
of elements equal to the number of bands.

#### Dependencies

To enable this port, select the **Output center
frequencies** parameter.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Frequency scale
  summary: Frequency scale of filter bank mel (default) | bark | erb
  group: ''
- name: Mel style
  summary: Mel style oshaughnessy (default) | slaney
  group: ''
- name: Auto-determine number of bands
  summary: Automatically determine number of bandpass filters on (default) | off
  group: ''
- name: Number of bands
  summary: Number of bandpass filters 32 (default) | positive integer
  group: ''
- name: Auto-determine frequency range
  summary: Automatically determine frequency range on (default) | off
  group: ''
- name: Frequency range (Hz)
  summary: Frequency range over which to design auditory filter bank [0,22050] (default) | two-element row vector
  group: ''
- name: Filter bank design domain
  summary: Domain to design filter bank linear (default) | warped
  group: ''
- name: Filter bank normalization
  summary: Normalization technique for filter bank bandwidth (default) | area | none
  group: ''
- name: Output center frequencies
  summary: Specify additional output port for center frequencies off (default) | on
  group: ''
- name: Visualize filter bank
  summary: Open plot to visualize filter bank button
  group: ''
- name: Window
  summary: Analysis window hamming(1024,'periodic') (default) | real vector
  group: ''
- name: Normalize window
  summary: Normalize analysis window on (default) | off
  group: ''
- name: Overlap length
  summary: Overlap length of adjacent analysis windows 512 (default) | integer in the range [0, windowLength)
  group: ''
- name: Auto-determine FFT length
  summary: Automatically determine FFT length on (default) | off
  group: ''
- name: FFT length
  summary: Number of DFT points 1024 (default) | positive integer
  group: ''
- name: Spectrum type
  summary: Type of spectrum magnitude (default) | power
  group: ''
- name: Number of spectra
  summary: Number of spectra 1 (default) | positive integer
  group: ''
- name: Number of spectra overlap
  summary: Number of overlapped spectra 0 (default) | integer in the range [0, Number of spectra)
  group: ''
- name: Apply logarithm
  summary: Apply logarithm off (default) | on
  group: ''
- name: Inherit sample rate from input
  summary: Specify source of input sample rate off (default) | on
  group: ''
- name: Input sample rate (Hz)
  summary: Sample rate of input 44.1e3 (default) | positive scalar
  group: ''
```

#### Filter Bank Parameters

### **Frequency scale** — Frequency scale of filter bank `mel` (default) | `bark` | `erb`

Frequency scale used to design the auditory filter bank, specified as
`mel`, `bark`, or
`erb`.

- `mel` –– Design the filter bank as
  half-overlapped triangles equally spaced on the mel
  scale.
- `bark` –– Design the filter bank as
  half-overlapped triangles equally spaced on the Bark
  scale.
- `erb` –– Design the filter bank as
  gammatone filters whose center frequencies are equally spaced on
  the ERB scale.

### **Mel style** — Mel style `oshaughnessy` (default) | `slaney`

Style of the mel scale, specified as `oshaughnessy` or
`slaney`.

#### Dependencies

To enable this parameter, set the **Frequency scale**
parameter to `mel`.

### **Auto-determine number of bands** — Automatically determine number of bandpass filters `on` (default) | `off`

When you select this parameter, the block automatically determines the number of bandpass
filters based on the **Frequency scale** parameter.

- If you set **Frequency scale** to
  `mel` or
  `bark`, then the number of bands is
  `32`.
- If you set **Frequency scale** to
  `erb`, then the number of bands is
  equal to `ceil(hz2erb(fr(2))-hz2erb(fr(1)))`, where
  `fr` is specified using **Frequency
  range (Hz)**.

### **Number of bands** — Number of bandpass filters `32` (default) | positive integer

Number of bandpass filters, specified as a positive integer.

#### Dependencies

To enable this parameter, clear the **Auto-determine number of
bands** parameter.

### **Auto-determine frequency range** — Automatically determine frequency range `on` (default) | `off`

When you select this parameter, the block sets the **Frequency range**
to `[0,fs/2]`, where `fs` is the sample
rate. The sample rate is determined by the **Inherit sample rate
from input** and **Input sample rate (Hz)**
parameters.

### **Frequency range (Hz)** — Frequency range over which to design auditory filter bank `[0,22050]` (default) | two-element row vector

Frequency range in Hz over which to design the auditory filter bank, specified as a
two-element row vector.

#### Dependencies

To enable this parameter, clear the **Auto-determine frequency
range** parameter.

### **Filter bank design domain** — Domain to design filter bank `linear` (default) | `warped`

Domain in which the block designs the filter bank, specified as
`linear` or `warped`.
Set the filter bank design domain to `linear` to
design the bandpass filters in the linear (Hz) domain. Set the filter bank
design domain to `warped` to design the bandpass
filters in the warped (mel or Bark) domain.

#### Dependencies

To enable this parameter, set **Frequency scale** to
`mel` or
`bark`.

### **Filter bank normalization** — Normalization technique for filter bank `bandwidth` (default) | `area` | `none`

Normalization technique used for the filter bank weights, specified as
`bandwidth`, `area`,
or `none`.

- `bandwidth` –– Normalize the weights
  of each bandpass filter by the corresponding bandwidth of the
  filter.
- `area` –– Normalize the weights of
  each bandpass filter by the corresponding area of the bandpass
  filter.
- `none` –– The block does not
  normalize the weights of the filters.

### **Output center frequencies** — Specify additional output port for center frequencies `off` (default) | `on`

When you select this parameter, the block displays an additional output
port, **fvec**. This port outputs the center frequencies of
the bandpass filters.

### **Visualize filter bank** — Open plot to visualize filter bank button

Open plot to visualize the filters in the frequency domain.

#### Spectrogram Parameters

### **Window** — Analysis window `hamming(1024,'periodic')` (default) | real vector

Analysis window applied in the time domain, specified as a real
vector.

### **Normalize window** — Normalize analysis window `on` (default) | `off`

When you select this parameter, the block applies window
normalization.

### **Overlap length** — Overlap length of adjacent analysis windows `512` (default) | integer in the range [0, `windowLength`)

Overlap length of adjacent analysis windows, specified as an integer in
the range [0, `windowLength`), where
`windowLength` is the length of the analysis window,
which is specified by **Window**.

### **Auto-determine FFT length** — Automatically determine FFT length `on` (default) | `off`

When you select this parameter, the block automatically sets the FFT length to the window
length `numel(Window)`.

### **FFT length** — Number of DFT points `1024` (default) | positive integer

Number of points used to calculate the DFT, specified as a positive
integer.

#### Dependencies

To enable this parameter, clear the **Auto-determine FFT
length** parameter.

### **Spectrum type** — Type of spectrum `magnitude` (default) | `power`

Type of spectrum, specified as `magnitude` or
`power`.

### **Number of spectra** — Number of spectra `1` (default) | positive integer

Number of spectra in the spectrogram, specified as a positive
integer.

### **Number of spectra overlap** — Number of overlapped spectra `0` (default) | integer in the range [0, **Number of spectra**)

Number of spectra overlapped across consecutive spectrograms, specified as
an integer in the range [0, **Number of spectra**).

### **Apply logarithm** — Apply logarithm `off` (default) | `on`

When you select this parameter, the block applies a base 10 logarithm to
the spectrogram.

#### Simulation Parameters

### **Inherit sample rate from input** — Specify source of input sample rate `off` (default) | `on`

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, you specify the sample rate
in the **Input sample rate (Hz)** parameter.

### **Input sample rate (Hz)** — Sample rate of input `44.1e3` (default) | positive scalar

Input sample rate in Hz, specified as a real positive scalar.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.
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

The Auditory Spectrogram block supports optimized code generation
using single instruction, multiple data (SIMD) instructions. For more information
about SIMD code generation, see Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder).

## Version History

**Introduced in R2022a**

### R2024a: Apply logarithm to spectrogram

Select the **Apply logarithm** parameter to apply a base 10
logarithm to the spectrogram.

### R2023b: Support for Slaney-style mel scale

Set the **Mel style** parameter to
`slaney` to use the Slaney-style mel scale.

### R2023a: Generate optimized C/C++ code for computing auditory spectrogram

The Auditory Spectrogram block supports optimized C/C++ code
generation using single instruction, multiple data (SIMD) instructions.

## Description

Extract mel, Bark, or ERB spectrogram from audio

The Auditory Spectrogram block extracts a spectrogram from the audio input signal. A
spectrogram contains an estimate of the short-term, time-localized frequency content of
the input signal.
