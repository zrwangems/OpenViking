---
type: simulink-block
title: 'OpenL3'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Pretrained Models / OpenL3'
documentation_page: 'openl3block'
documentation_source_path: 'ref/openl3block.html'
language: en
---

# OpenL3

## Ports

### Input

### **Port\_1** — Spectrograms matrix | 4-D array

Spectrograms generated from audio, specified as an
*N*-by-*M* matrix or an
*N*-by-*M*-by-1-by-*K* array.
*K* represents the number of spectrograms, and
*N*-by-*M* is the size of the spectrograms and
depends on the value of the **Spectrum type** parameter.

- `Mel (128 bands)` –– The network accepts mel
  spectrograms of size 128-by-199, where 128 is the number of mel bands, and 199
  is the number of time hops.
- `Mel (256 bands)` –– The network accepts mel
  spectrograms of size 256-by-199, where 256 is the number of mel bands, and 199
  is the number of time hops.
- `Linear` –– The network accepts positive one-sided
  spectrograms of size 257-by-197, where 257 is the FFT length and 197 is the
  number of time hops.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Embeddings matrix

Output embeddings, returned as a *K*-by-*L*
matrix, where *K* is the number of input spectrograms, and
*L* is specified by the **Embedding length**
parameter.

**Data Types:** `single`

## Parameters

### **Spectrum type** — Type of spectrum `Mel (128 bands)` (default) | `Mel (256 bands)` | `Linear`

Type of spectrum generated from audio and used as input to the neural network,
specified as `Mel (128 bands)`, `Mel (256
bands)`, or `Linear`. This parameter specifies
the size of the network input Port\_1.

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

### **Mini-batch size** — Size of mini-batches `128` (default) | positive integer

Size of mini-batches to use for prediction, specified as a positive integer. Larger
mini-batch sizes require more memory but can lead to faster predictions.

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

OpenL3 embeddings extraction network

The OpenL3 block leverages a pretrained convolutional neural network that
extracts feature embeddings from audio signals. These embeddings are powerful audio
representations that can be used for tasks such as classification. This block requires
Deep Learning Toolbox™.
