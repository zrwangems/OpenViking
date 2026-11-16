---
type: simulink-block
title: 'Design Auditory Filter Bank'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Feature Extraction'
documentation_page: 'designauditoryfilterbankblock'
documentation_source_path: 'ref/designauditoryfilterbankblock.html'
language: en
---

# Design Auditory Filter Bank

## Ports

### Output

### **fb** — Filter bank column vector | matrix

Auditory filter bank, returned as an
*M*-by-*N* matrix, where:

- *M* is the number of bands, which is
  determined by the **Auto-determine number of
  bands** and **Number of
  bands** parameters.
- *N* is the number of points in the
  spectrum. If you select **Design one-sided filter
  bank**, then *N* is equal to
  `ceil(NFFT/2)`,
  where `NFFT` is the **FFT
  length**. If you do not select **Design
  one-sided filter bank**, then
  *N* is equal to the **FFT
  length**.

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

### **FFT length** — Number of DFT points `1024` (default) | positive integer

Number of points used to calculate the DFT, specified as a positive
integer.

### **Design one-sided filter bank** — Design one-sided or two-sided filter bank `on` (default) | `off`

When you select this parameter, the block designs a one-sided filter bank. Otherwise, the
filter bank is two sided.

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
to `[0,fs/2]`, where `fs` is specified
using **Sample rate (Hz)**.

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

### **Output data type** — Data type of output `double` (default) | `single`

Data type of output, specified as `double` or
`single`.

### **Sample rate (Hz)** — Sample rate `44.1e3` (default) | positive scalar

Sample rate in Hz of the filter design, specified as a positive scalar.

### **Visualize filter bank** — Open plot to visualize filter bank button

Open plot to visualize the filters in the frequency domain.

### **Output center frequencies** — Specify additional output port for center frequencies `off` (default) | `on`

When you select this parameter, the block displays an additional output port,
**fvec**. This port outputs the center frequencies of
the bandpass filters.

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

## Version History

**Introduced in R2022a**

### R2023b: Support for Slaney-style mel scale

Set the **Mel style** parameter to
`slaney` to use the Slaney-style mel scale.

## Description

Design frequency-domain auditory filter bank

The Design Auditory Filter Bank block outputs a frequency-domain auditory filter bank. You
can use an auditory filter bank to decompose an audio signal into separate frequency
bands for feature extraction.
