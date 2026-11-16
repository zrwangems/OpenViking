---
type: simulink-block
title: 'VGGish'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Applications / Signal Processing, Audio, and Wireless / Audio Processing'
documentation_page: 'vggishblock'
documentation_source_path: '../audio/ref/vggishblock.html'
language: en
---

# VGGish

## Ports

### Input

### **Port\_1** — Mel spectrograms 96-by-64 matrix | 96-by-64-by-1-by-*N* array

Mel spectrograms, specified as a 96-by-64 matrix or a
96-by-64-by-1-by-*N* array, where:

- `96` –– Represents the number of 25 ms frames
  in each mel spectrogram
- `64` –– Represents the number of mel bands
  spanning 125 Hz to 7.5 kHz
- *N* –– Represents the number of mel
  spectrograms.

You can use the VGGish Preprocess block to generate mel spectrograms. All
spectrograms are of the dimension 96-by-64.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Embeddings *N*-by-128 matrix

VGGish feature embeddings, returned as an *N*-by-128 matrix, where
*N* is the number of mel spectrograms in the input.
The feature embeddings are a compact representation of audio
data.

**Data Types:** `single`

## Parameters

### **Mini-batch size** — Size of mini-batches `128` (default) | positive integer

Size of mini-batches to use for prediction specified as a positive integer. Larger
mini-batch sizes require more memory but can lead to faster
predictions.

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

VGGish embeddings extraction network

The VGGish block leverages a pretrained convolutional neural network that is trained on the
AudioSet data set to extract feature embeddings from audio signals.
