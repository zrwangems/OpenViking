---
type: simulink-block
title: 'OpenL3 Embeddings'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Pretrained Models / OpenL3'
documentation_page: 'openl3embeddingsblock'
documentation_source_path: 'ref/openl3embeddingsblock.html'
language: en
---

# OpenL3 Embeddings

## Ports

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

### **Port\_1** — Embedding row vector

Output embedding, returned as a row vector whose length is specified by the
**Embedding length** parameter.

**Data Types:** `single`

## Parameters

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `48e3` (default) | positive scalar

Sample rate of the input signal in Hz, specified as a positive scalar.

### **Overlap percentage (%)** — Overlap percentage between consecutive spectrograms `90` (default) | [0 100)

Specify the overlap percentage between consecutive spectrograms as a scalar in the
range [0 100).

### **Spectrum type** — Type of spectrum `Mel (128 bands)` (default) | `Mel (256 bands)` | `Linear`

Type of spectrum generated from audio and used as input to the neural network,
specified as `Mel (128 bands)`, `Mel (256
bands)`, or `Linear`.

- `Mel (128 bands)` –– The neural network accepts mel
  spectrograms generated from the input audio with 128 mel bands.
- `Mel (256 bands)` –– The neural network accepts mel
  spectrograms generated from the input audio with 256 mel bands.
- `Linear` –– The neural network accepts positive
  one-sided spectrograms generated from the input audio with an FFT length of
  257.

### **Content type** — Type of audio content `Environmental sounds` (default) | `Musical sounds`

Type of audio content the neural network was trained on, specified as
`Environmental sounds` or `Musical
sounds`. Set this parameter to `Environmental
sounds` to use a neural network pretrained on environmental audio data,
and set it to `Musical sounds` to use a network pretrained on
musical data.

### **Embedding length** — Output embedding length `512` (default) | `6144`

Length of output embedding, specified as `512` or
`6144`.

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

Usage notes and limitations:

- To generate generic C code that does not depend on third-party libraries, in the
  **Configuration Parameters** > **Code
  Generation** general category, set the **Language**
  parameter to `C`.
- To generate C++ code, in the **Configuration Parameters** >
  **Code Generation** general category, set the
  **Language** parameter to `C++`. To
  specify the target library for code generation, in the **Code
  Generation** > **Interface** category, set the
  **Target Library** parameter. Setting this parameter to
  `None` generates generic C++ code that does not depend
  on third-party libraries.
- For a list of networks and layers supported for code generation, see Networks and Layers Supported for Code Generation (MATLAB Coder).

## Version History

**Introduced in R2022b**

## Description

Extract OpenL3 embeddings

The OpenL3 Embeddings block uses OpenL3 to extract feature embeddings from
audio signals. The OpenL3 Embeddings block combines necessary audio
preprocessing and OpenL3 network inference and returns feature embeddings that are a compact
representation of audio data. This block requires Deep Learning Toolbox™.
