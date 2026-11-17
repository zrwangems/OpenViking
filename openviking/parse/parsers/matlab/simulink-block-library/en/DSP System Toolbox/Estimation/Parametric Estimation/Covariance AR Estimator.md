---
type: simulink-block
title: 'Covariance AR Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Parametric Estimation'
documentation_page: 'covariancearestimator'
documentation_source_path: 'ref/covariancearestimator.html'
language: en
---

# Covariance AR Estimator

## Ports
```yaml
ports:
- name: Input
  summary: Input column vector | unoriented vector
  direction: input
  data_types: single | double
- name: A
  summary: Normalized estimate of the AR model polynomial coefficients column vector
  direction: output
  data_types: single | double
- name: G
  summary: Model gain scalar
  direction: output
  data_types: single | double
```

### Input

### **Input** — Input column vector | unoriented vector

Specify the input data as a column vector or an unoriented vector. The block assumes
that the input data is the output of an AR system driven by white noise
and represents a frame of consecutive time samples from a single-channel
signal.

**Data Types:** `single` | `double`
### Output

### **A** — Normalized estimate of the AR model polynomial coefficients column vector

Normalized estimate of the AR model polynomial coefficients
*A*(*z*), returned as a column
vector of length *p*+1 in descending powers of
*z*.

The block computes the estimate of these coefficients independently
for each successive input frame.

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

where,

- *H*(*z*) –– Transfer
  function of the estimated AR model
- *G* –– Scalar gain
- *A*(*z*) –– Polynomial
  coefficients of the AR model

**Data Types:** `single` | `double`

### **G** — Model gain scalar

Gain of the estimated AR model, returned as a scalar.

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

where,

- *H*(*z*) –– Transfer
  function of the estimated AR model
- *G* –– Scalar gain
- *A*(*z*) –– Polynomial
  coefficients of the AR model

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Estimation order
  summary: Order of AR model 4 (default) | positive integer
  group: ''
```

### **Estimation order** — Order of AR model `4` (default) | positive integer

Specify the estimation order *p* of the all-pole AR model as a positive
integer. To guarantee a nonsingular output, you must set
*p* to be less than or equal to half the input vector
length. Otherwise, the output can be singular.
## Libraries

DSP System Toolbox / Estimation / Parametric Estimation

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Compute estimate of autoregressive (AR) model parameters using covariance method

The Covariance AR Estimator block uses the covariance method to fit an
autoregressive (AR) model to the input data. This method minimizes the forward
prediction error in the least squares sense.
