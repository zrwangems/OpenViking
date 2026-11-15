---
type: simulink-block
title: 'Deep Pitch Estimator'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Applications / Signal Processing, Audio, and Wireless / Audio Processing'
documentation_page: 'deeppitchestimator'
documentation_source_path: '../audio/ref/deeppitchestimator.html'
language: en
---

# Deep Pitch Estimator

## Ports

### Input

### **Port\_1** — Audio input vector

Audio input, specified as a one-channel signal (vector). If **Sample rate of input signal (Hz)** is 16e3, there are
no restrictions on the input frame length. If **Sample rate of
input signal (Hz)** is different from 16e3, then the input
frame length must be a multiple of the decimation factor of the
resampling operation that the block performs. If the input frame length
does not satisfy this condition, the block generates an error message
with information on the decimation factor.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Estimated fundamental frequency column vector

Estimated fundamental frequency in Hz, returned as an
*N*-by-1 vector, where *N* is the
number of pitch estimations specified by **Number of buffered pitch estimations**.

**Data Types:** `single`

## Parameters

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `16e3` (default) | positive scalar

Sample rate of the input signal in Hz, specified as a positive
scalar.

### **Overlap percentage (%)** — Overlap percentage between consecutive frames `85` (default) | [0, 100)

Specify the overlap percentage between consecutive input frames as a
scalar in the range [0, 100).

### **Number of buffered pitch estimations** — Number of pitch estimations in output `1` (default) | positive integer

Number of pitch estimations in output, specified as a positive
integer.

A higher value allows the block to improve computational efficiency by
operating on multiple audio frames in parallel. However, it also increases
latency because the block buffers the specified number of pitch estimations
before returning them.

### **Confidence threshold** — Pitch confidence threshold `0.5` (default) | scalar in the range [0, 1)

Pitch confidence threshold, specified as a scalar in the range [0, 1). In
postprocessing, the block suppresses fundamental frequencies where the
network confidence is below the threshold.

**Note**

If the maximum value of the network output is less than the
confidence threshold, the block returns
`NaN`.

### **Model capacity** — Size of trained neural network `Full` (default) | `Large` | `Medium` | `Small` | `Tiny`

Model capacity, specified as `Full`,
`Large`, `Medium`,
`Small`, or `Tiny`.
The smaller sizes correspond to fewer parameters in the model, leading to
faster computation but lower accuracy.

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

Estimate pitch with CREPE deep learning neural network

The Deep Pitch Estimator block uses a CREPE pretrained neural network to
estimate the pitch from audio signals. The block combines necessary audio preprocessing,
network inference, and postprocessing of network output to return pitch estimations in
Hz. This block requires Deep Learning Toolbox™.
