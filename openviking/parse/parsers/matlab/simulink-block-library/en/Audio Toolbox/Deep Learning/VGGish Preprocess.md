---
type: simulink-block
title: 'VGGish Preprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'vggishpreprocessblock'
documentation_source_path: 'ref/vggishpreprocessblock.html'
language: en
---

# VGGish Preprocess

## Ports

### Input

### **Port\_1** — Sound data column vector

Sound data, specified as a one-channel signal (column vector). If
**Sample rate of input signal (Hz)** is 16e3, there
are no restrictions on the input frame length. If **Sample rate
of input signal (Hz)** is different from 16e3, then the
input frame length must be a multiple of the decimation factor of the
resampling operation that the block performs. If the input frame length
does not satisfy this condition, the block throws an error message with
information on the decimation factor.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Mel spectrogram 96-by-64 matrix

Mel spectrogram generated from the input audio signal, returned as a
96-by-64 matrix, where:

- `96` –– Represents the number of 25 ms frames
  in each mel spectrogram
- `64` –– Represents the number of mel bands
  spanning 125 Hz to 7.5 kHz

The overlap between consecutive 96-by-64 mel spectrograms is
determined by the value of the **Overlap percentage
(%)** parameter. You can provide the mel spectrogram as an
input to the VGGish pretrained network or to a network that accepts the
same inputs as VGGish.

**Data Types:** `single`

## Parameters

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `16e3` (default) | positive scalar

Sample rate of the input signal in Hz, specified as a positive
scalar.

### **Overlap percentage (%)** — Overlap percentage between consecutive mel spectrograms `50` (default) | [0 100)

Specify the overlap percentage between consecutive mel spectrograms as a
scalar in the range [0 100).

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

**Introduced in R2022a**

## Description

Preprocess audio for VGGish feature extraction

The VGGish Preprocess block generates mel spectrograms from an audio input that you can then
feed to the VGGish pretrained network or to a network that accepts the same inputs as
VGGish.
