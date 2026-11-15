---
type: simulink-block
title: 'CREPE Preprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Pretrained Models / CREPE'
documentation_page: 'crepepreprocessblock'
documentation_source_path: 'ref/crepepreprocessblock.html'
language: en
---

# CREPE Preprocess

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

### **Port\_1** — Preprocessed audio frames 4-D array

Preprocessed audio frames for the CREPE neural network, returned as a
1024-by-1-by-1-by-*N* array, where
*N* is the number of generated frames specified by
**Number of output frames**.

**Data Types:** `single`

## Parameters

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `16e3` (default) | positive scalar

Sample rate of the input signal in Hz, specified as a positive
scalar.

### **Overlap percentage (%)** — Overlap percentage between consecutive frames `85` (default) | [0, 100)

Specify the overlap percentage between consecutive frames as a scalar in
the range [0, 100).

### **Number of output frames** — Number of generated frames `1` (default) | positive integer

Number of generated frames in the output, specified as a positive integer.

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

**Introduced in R2023a**

## Description

Preprocess audio for CREPE deep pitch estimation

The CREPE Preprocess block generates frames from the input audio signal that
you can feed to a CREPE
pretrained network or to a network that accepts the same inputs as CREPE.
