---
type: simulink-block
title: 'Cepstral Coefficients'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'cepstralcoefficientsblock'
documentation_source_path: 'ref/cepstralcoefficientsblock.html'
language: en
---

# Cepstral Coefficients

## Ports
```yaml
ports:
- name: Port_1
  summary: Spectrogram or auditory spectrogram matrix | 3-D array
  direction: input
  data_types: single | double
- name: Port_1
  summary: Cepstral Coefficients matrix | 3-D array
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — Spectrogram or auditory spectrogram matrix | 3-D array

Spectrogram or auditory spectrogram, specified as an
*L*-by-*M* matrix or
*L*-by-*M*-by-*N* array, where:

- *L* is the number of frequency bands.
- *M* is the number of frames.
- *N* is the number of channels.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Cepstral Coefficients matrix | 3-D array

Cepstral coefficients, returned as an *M*-by-*B*
matrix or *M*-by-*B*-by-*N* array, where:

- *M* is the number of frames in the input
  spectrogram.
- *B* is the number of coefficients returned per frame, which
  is specified by the **Number of cepstral coefficients**
  parameter.
- *N* is the number of channels in the input
  spectrogram.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Number of cepstral coefficients
  summary: Number of cepstral coefficients returned 13 (default) | positive integer greater than 1
  group: ''
- name: Rectification
  summary: Type of nonlinear rectification Logarithm (default) | Cubic root | None
  group: ''
- name: Simulate using
  summary: Specify type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Number of cepstral coefficients** — Number of cepstral coefficients returned 13 (default) | positive integer greater than 1

Number of cepstral coefficients, specified as a positive integer greater than
1.

### **Rectification** — Type of nonlinear rectification `Logarithm` (default) | `Cubic root` | `None`

Type of nonlinear rectification applied to the spectrum prior to the discrete cosine
transform, specified as `Logarithm`, `Cubic
root`, or `None`.

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
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Extract cepstral coefficients from spectrogram

The Cepstral Coefficients block extracts the cepstral coefficients from a
real-valued spectrogram or auditory spectrogram. Cepstral coefficients are commonly used as
compact representations of audio signals.
