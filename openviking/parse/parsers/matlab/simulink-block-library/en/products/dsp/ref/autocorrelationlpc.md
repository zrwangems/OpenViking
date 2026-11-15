---
type: simulink-block
title: 'Autocorrelation LPC'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Linear Prediction'
documentation_page: 'autocorrelationlpc'
documentation_source_path: 'ref/autocorrelationlpc.html'
language: en
---

# Autocorrelation LPC

## Ports

### Input

### **Input 1** — Input array unoriented vector | column vector | matrix

Specify the input *u* as an unoriented vector, column
vector, or a matrix. Row vectors are not valid inputs. The block treats
all *M*-by-*N* matrix inputs as
*N* channels of length *M*.

**Data Types:** `single` | `double`
### Output

### **A** — Polynomial coefficients column vector | matrix

Polynomial coefficients generated when you set the **Output(s)**
parameter to `A` or `A and
K`. For each input channel, port A outputs an
(*N*+1)-by-1 column vector *a* =
[1
*a2**a3*
...
*aN+1*]T,
containing the coefficients of an
*N*th-order moving
average (MA) linear process that predicts the next value,*ûM+1*, in the input
time-series.

u^M+1=−(a2uM)−(a3uM−1)−...−(aN+1uM−N+1)

#### Dependencies

To enable port A, set **Output(s)** to
`A` or `A and
K`.

**Data Types:** `single` | `double`

### **K** — Reflection coefficients column vector | matrix

Reflection coefficients generated when **Output(s)**
is set to `K` or `A and
K`. For each input channel, port K outputs a
length-*N* column vector whose elements are the
prediction error reflection coefficients.

#### Dependencies

To enable port K, set **Output(s)** to
`A` or `A and
K`.

**Data Types:** `single` | `double`

### **P** — Prediction error power vector

Prediction error power output at port P as a vector whose length is
the number of input channels.

#### Dependencies

To enable port P, select the **Output prediction error
power (P)** parameter.

**Data Types:** `single` | `double`

## Parameters

### **Output(s)** — Type of prediction coefficients `A` (default) | `A and K` | `K`

Specify the type of prediction coefficients output by the block. The block
can output polynomial coefficients (`A`), reflection
coefficients (`K`), or both (`A and
K`).

When you set **Output(s)** to `A and
K`, the block enables port A and K and each port outputs
its respective set of prediction coefficients for each channel.

### **Output prediction error power (P)** — Output prediction error power `off` (default) | `on`

Select this parameter to enable the output port `P`,
which outputs the output prediction error power.

### **Inherit prediction order from input dimensions** — Inherit prediction order from input dimensions `off` (default) | `on`

Select this parameter to inherit the prediction order *N*
from the input dimensions.

### **Prediction order (N)** — Prediction order `1` (default) | scalar

Specify the prediction order *N*. Note that
*N* must be a scalar with a value less than the length
of the input channels or the block produces an error.

#### Dependencies

This parameter appears only when you do not select the
**Inherit prediction order from input dimensions**
parameter.

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

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Determine coefficients of Nth-order forward linear predictors

The Autocorrelation LPC block determines the coefficients of an
*N-step forward linear predictor* for the time-series in each
length-*M* input channel, *u*, by minimizing the
prediction error in the least squares sense. A linear predictor is an FIR filter that
predicts the next value in a sequence from the present and past inputs. This technique
has applications in filter design, speech coding, spectral analysis, and system
identification.

The Autocorrelation LPC block can output the prediction error for each channel as polynomial
coefficients, reflection coefficients, or both. The block can also output the prediction
error power for each channel.
