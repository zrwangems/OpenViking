---
type: simulink-block
title: 'LSF/LSP to LPC Conversion'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'lsflsptolpcconversion'
documentation_source_path: 'ref/lsflsptolpcconversion.html'
language: en
---

# LSF/LSP to LPC Conversion

## Ports
```yaml
ports:
- name: LSP
  summary: Line spectral pairs vector | matrix
  direction: input
  data_types: single | double
- name: LSFn
  summary: Line spectral frequencies normalized in range (0 0.5) vector | matrix
  direction: input
  data_types: single | double
- name: LSFr
  summary: Line spectral frequencies in range (0 π) vector | matrix
  direction: input
  data_types: single | double
- name: A
  summary: Linear prediction coefficients vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **LSP** — Line spectral pairs vector | matrix

Specify the line spectral pairs as a vector of values in the range (−1 1) in decreasing
order. If you specify a matrix, the block treats each column of the
matrix as a separate channel. When you specify an unoriented vector, the
block treats the input as one channel. These values equal the cosine of
the LSF values between 0 and π radians. Do not include the guaranteed
LSP values, −1 and 1.

**Data Types:** `single` | `double`

### **LSFn** — Line spectral frequencies normalized in range (0 0.5) vector | matrix

Specify the line spectral frequencies normalized in the range (0 0.5) as a vector or a
matrix in increasing order. If you specify a matrix, the block treats
each column of the matrix as a separate channel. When you specify an
unoriented vector, the block treats the input as one channel. You can
obtain these values by dividing the LSF values between 0 and π radians
by 2π. Do not include the guaranteed LSF values, 0 and 0.5.

**Data Types:** `single` | `double`

### **LSFr** — Line spectral frequencies in range (0 π) vector | matrix

Specify the line spectral frequencies in the range (0 π) as a vector or a matrix in
increasing order. If you specify a matrix, the block treats each column
of the matrix as a separate channel. When you specify an unoriented
vector, the block treats the input as one channel. Do not include the
guaranteed LSF values, 0 and π.

**Data Types:** `single` | `double`
### Output

### **A** — Linear prediction coefficients vector | matrix

Linear prediction coefficients, returned as a vector or a
matrix.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Input
  summary: Line spectral pairs or line spectral frequencies LSP in range (-1 1) (default) | LSF normalized in range (0 0.5)
    | LSF in range (0 pi)
  group: ''
```

### **Input** — Line spectral pairs or line spectral frequencies `LSP in range (-1 1)` (default) | `LSF normalized in range (0 0.5)` | `LSF in range (0 pi)`

When you select this parameter to:

- `LSP in range (-1 1)` –– The block
  converts the line spectral pairs in the range (−1 1) to linear
  prediction coefficients.
- `LSF in range (0 pi)` –– The block
  converts the line spectral frequencies in the range (0 π) to
  linear prediction coefficients.
- `LSF normalized in range (0 0.5)` ––
  The block converts the line spectral frequencies normalized in
  the range (0 0.5) to linear prediction coefficients.
## Libraries

DSP System Toolbox / Estimation / Linear Prediction

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

**Introduced before R2006a**

## Description

Convert line spectral frequencies or line spectral pairs to linear prediction coefficients

The LSF/LSP to LPC Conversion block converts line spectral pairs (LSPs) or
line spectral frequencies (LSFs) to linear prediction polynomial coefficients (LPCs).
When converting LSFs to LPCs, the block outputs match those of the
`lsf2poly` function.
