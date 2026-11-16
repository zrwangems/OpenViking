---
type: simulink-block
title: 'Audio Delta'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'audiodeltablock'
documentation_source_path: 'ref/audiodeltablock.html'
language: en
---

# Audio Delta

## Ports

### Input

### **Port\_1** — Audio features scalar | vector | matrix | 3-D array

Audio features, specified as a scalar, vector, matrix, or 3-D array. The delta
computation operates along the first dimension. All other dimensions are treated as
independent channels.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Delta of audio features scalar | vector | matrix | array

Delta of audio features, returned as an array that is the same size and data type
as the input.

**Data Types:** `single` | `double`

## Parameters

### **Delta window length** — Window length over which to calculate delta `9` (default) | odd integer greater than 2

Window length over which to calculate delta, specified as an odd integer greater
than 2.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` –– Simulate model using the
  MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode,
  you can debug the source code of the block.
- `Code generation` –– Simulate model using generated C
  code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

## Libraries

Audio Toolbox / Features

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Compute delta features

The Audio Delta block computes the delta of the input audio features. The
delta is an approximation of the first derivative of the audio features with respect to
time.
