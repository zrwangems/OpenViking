---
type: simulink-block
title: 'YAMNet Preprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'yamnetpreprocessblock'
documentation_source_path: 'ref/yamnetpreprocessblock.html'
language: en
---

# YAMNet Preprocess

## Ports
```yaml
ports:
- name: audioIn
  summary: Sound data column vector
  direction: input
  data_types: single | double
- name: features
  summary: Mel spectrograms that can be fed to YAMNet pretrained network 96-by-64 matrix
  direction: output
  data_types: single
```

### Input

### **audioIn** — Sound data column vector

Sound data to classify, specified as a one-channel signal (column vector). If
**Sample rate of input signal (Hz)** is 16e3, there are no
restrictions on the input frame length. If **Sample rate of input signal
(Hz)** is different from 16e3, then the input frame length must be a
multiple of the decimation factor of the resampling operation that the block performs.
If the input frame length does not satisfy this condition, the block throws an error
message with information on the decimation factor.

**Data Types:** `single` | `double`
### Output

### **features** — Mel spectrograms that can be fed to YAMNet pretrained network 96-by-64 matrix

Mel spectrograms generated from **audioIn**, returned as a
96-by-64 matrix, where:

- `96` –– Represents the number of 25 ms frames in each mel
  spectrogram
- `64` –– Represents the number of mel bands spanning 125 Hz to
  7.5 kHz

The overlap between consecutive 96-by-64 mel spectrograms is determined by the
value of the **Overlap percentage (%)** parameter.

Each 96-by-64 matrix represents a single mel spectrogram. For more details on how
this block generates mel spectrograms, see Algorithms.

**Data Types:** `single`
## Parameters
```yaml
parameters:
- name: Sample rate of input signal (Hz)
  summary: Sample rate of input signal in Hz 16e3 (default) | positive scalar
  group: ''
- name: Overlap percentage (%)
  summary: Overlap percentage between consecutive mel spectrograms 50 (default) | [0 100)
  group: ''
```

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `16e3` (default) | positive scalar

Sample rate of the input signal in Hz, specified as a positive scalar.

**Data Types:** `single` | `double`

### **Overlap percentage (%)** — Overlap percentage between consecutive mel spectrograms `50` (default) | [0 100)

Specify the overlap percentage between consecutive mel spectrograms as a scalar in
the range [0 100).

**Data Types:** `single` | `double`
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

**Introduced in R2021b**

## Description

Preprocess audio for YAMNet classification

The YAMNet Preprocess block generates mel spectrograms from audio input
that can be fed to the YAMNet pretrained network or to a network that accepts the same inputs
as YAMNet.
