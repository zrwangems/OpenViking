---
type: simulink-block
title: 'CREPE'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Pretrained Models / CREPE'
documentation_page: 'crepeblock'
documentation_source_path: 'ref/crepeblock.html'
language: en
---

# CREPE

## Ports

### Input

### **Port\_1** — Preprocessed audio input vector | 4-D array

Preprocessed input to the network, specified as a 1024-by-1-by-1-by-*N*
array, where *N* is the number of audio frames. If the
input has only one frame, the block accepts a vector.

The CREPE
Preprocess block takes in an audio signal and outputs the
preprocessed frames.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Network activations matrix

Network activations output by the CREPE network, returned as an
*N*-by-360 matrix, where *N* is the
number of input frames.

The CREPE
Postprocess block converts these network activations to
pitch estimates in Hz.

**Data Types:** `single`

## Parameters

### **Model capacity** — Size of trained neural network `Full` (default) | `Large` | `Medium` | `Small` | `Tiny`

Model capacity, specified as `Full`,
`Large`, `Medium`,
`Small`, or `Tiny`.
The smaller sizes correspond to fewer parameters in the model, leading to
faster computation but lower accuracy.

### **Mini-batch size** — Size of mini-batches `128` (default) | positive integer

Size of mini-batches to use for prediction, specified as a positive
integer. Larger mini-batch sizes require more memory but can lead to faster
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

**Introduced in R2023a**

## Description

CREPE deep pitch estimation neural network

The CREPE block leverages a pretrained convolutional neural model to estimate
pitch from an audio signal. This block requires Deep Learning Toolbox™.
