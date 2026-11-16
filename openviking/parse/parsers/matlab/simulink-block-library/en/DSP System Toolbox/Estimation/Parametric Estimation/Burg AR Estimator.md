---
type: simulink-block
title: 'Burg AR Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Parametric Estimation'
documentation_page: 'burgarestimator'
documentation_source_path: 'ref/burgarestimator.html'
language: en
---

# Burg AR Estimator

## Ports

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

The block computes the estimate of these coefficients independently for each successive
input frame.

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

where,

- *H*(*z*) –– Transfer
  function of the estimated AR model
- *G* –– Scalar gain
- *A*(*z*) –– Polynomial
  coefficients of the AR model

#### Dependency

To enable this port, set the **Output(s)**
parameter to `A` or `A and
K`.

**Data Types:** `single` | `double`

### **K** — Reflection coefficients column vector

Reflection coefficients (which are a secondary result of the Levinson
recursion), returned as a column vector of length
*p*.

#### Dependency

To enable this port, set the **Output(s)**
parameter to `K` or `A and
K`.

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

### **Output(s)** — Output `A` (default) | `A and K` | `K`

Specify whether the block outputs model coefficients (`A`),
reflection coefficients (`K`), or both
(`A and K`).

### **Inherit estimation order from input dimensions** — Inherit estimation order from input dimensions `on` (default) | `off`

When you select the **Inherit estimation order from input dimensions**
parameter, the block sets the order *p* of the all-pole
model to a value that is one less than the length of the input vector.
Otherwise, the order is the value you specify in the **Estimation
order** parameter.

### **Estimation order** — Order of AR model `4` (default) | nonnegative integer

Specify the order of the AR model *p* as a nonnegative
integer.

#### Dependency

To enable this parameter, clear the **Inherit estimation order
from input dimensions** parameter.

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

## Version History

**Introduced before R2006a**

## Description

Compute estimate of autoregressive (AR) model parameters using Burg method

The Burg AR Estimator block uses the Burg method to fit an autoregressive
(AR) model to the input data by minimizing (least squares) the forward and backward
prediction errors while constraining the AR parameters to satisfy the Levinson-Durbin
recursion.
