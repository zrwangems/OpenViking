---
type: simulink-block
title: 'CREPE Postprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'crepepostprocessblock'
documentation_source_path: 'ref/crepepostprocessblock.html'
language: en
---

# CREPE Postprocess

## Ports
```yaml
ports:
- name: Port_1
  summary: CREPE network activations matrix
  direction: input
  data_types: single | double
- name: Port_1
  summary: Estimated fundamental frequency column vector
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — CREPE network activations matrix

CREPE network activations, specified as an *N*-by-360
matrix, where *N* is the number of frames output by the
CREPE neural network.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Estimated fundamental frequency column vector

Estimated fundamental frequency in Hz, returned as an
*N*-by-1 vector, where *N* is the
number of frames in the input.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Confidence threshold
  summary: Pitch confidence threshold 0.5 (default) | scalar in the range [0, 1)
  group: ''
```

### **Confidence threshold** — Pitch confidence threshold `0.5` (default) | scalar in the range [0, 1)

Pitch confidence threshold, specified as a scalar in the range [0, 1). In
postprocessing, the block suppresses fundamental frequencies where the
network confidence is below the threshold.

**Note**

If the maximum value of the network output is less than the
confidence threshold, the block returns
`NaN`.

**Tunable:** Yes
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

Postprocess output of CREPE pitch estimation network

The CREPE Postprocess block converts the output of a CREPE
pretrained network to pitch estimates in Hz.
