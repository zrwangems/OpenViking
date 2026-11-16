---
type: simulink-block
title: 'VGGish Embeddings'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Applications / Signal Processing, Audio, and Wireless / Audio Processing'
documentation_page: 'vggishembeddingsblock'
documentation_source_path: '../audio/ref/vggishembeddingsblock.html'
language: en
---

# VGGish Embeddings

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

### **Port\_1** — Embeddings row vector of length 128

VGGish feature embeddings, returned as a row vector of length 128. The feature
embeddings are a compact representation of audio data.

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

**Introduced in R2022a**

## Description

Extract VGGish embeddings

The VGGish Embeddings block uses VGGish to extract feature embeddings from audio segments.
The VGGish Embeddings block combines necessary audio preprocessing and VGGish network
inference and returns feature embeddings that are a compact representation of audio
data.
