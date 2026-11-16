---
type: simulink-block
title: 'LPC to/from RC'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Linear Prediction'
documentation_page: 'lpctofromrc'
documentation_source_path: 'ref/lpctofromrc.html'
language: en
---

# LPC to/from RC

## Ports

### Input

### **K** — RC coefficients vector | matrix

Specify the RC coefficients as a vector or a matrix. The block treats each column of the
matrix as a channel. When you specify an unoriented vector, the block
treats the input as one channel.

#### Dependencies

To enable this input port, set **Type of
conversion** to `RC to
LPC`.

**Data Types:** `single` | `double`

### **A** — LPC coefficients vector | matrix

Specify the LPC coefficients as a vector or a matrix. The block treats each column of
the matrix as a channel. When you specify an unoriented vector, the
block treats the input as one channel.

#### Dependencies

To enable this input port, set **Type of
conversion** to `LPC to
RC`.

**Data Types:** `single` | `double`
### Output

### **K** — RC coefficients vector | matrix

RC coefficients, returned as a vector or a matrix.

#### Dependencies

To enable this output port, set **Type of
conversion** to `LPC to
RC`.

**Data Types:** `single` | `double`

### **A** — LPC coefficients vector | matrix

LPC coefficients, returned as a vector or a matrix. Each channel of
the input must have at least two samples.

#### Dependencies

To enable this output port, set **Type of
conversion** to `RC to
LPC`.

**Data Types:** `single` | `double`

### **P** — Normalized prediction error power vector

Normalized prediction error power, returned as a vector with one element per input
channel. Each element varies between 0 and 1.

#### Dependencies

To enable this port, select the **Output normalized
prediction error power** check box.

**Data Types:** `single` | `double`

### **S** — Filter stability output vector

Filter stability output, returned as a vector with one element per
input channel. The filter is represented by the LPCs or RCs.

The synthesis filter represented by the LPCs is stable when the absolute value of each
of the roots of the LPC polynomial is less than 1. The lattice filter
represented by the RCs is stable when the absolute value of each
reflection coefficient is less than 1. When the filter is stable, the
block outputs a Boolean value of `1` for each input
channel. When the filter is unstable, the block outputs a Boolean value
of `0` for each input channel.

#### Dependencies

To enable this port, select the **Output LPC filter
stability** check box.

**Data Types:** `Boolean`

## Parameters

### **Type of conversion** — Type of conversion `RC to LPC` (default) | `LPC to RC`

Select `LPC to RC` or `RC to LPC` to
select the domain for converting your coefficients.

### **Output normalized prediction error power** — Output normalized prediction error power `on` (default) | `off`

Select this check box to output the normalized prediction error power on
port **P**.

### **Output LPC filter stability** — Output LPC filter stability `off` (default) | `on`

Select this check box to output the stability of the filter.

The synthesis filter represented by the LPCs is stable when the absolute value of each of
the roots of the LPC polynomial is less than 1. The lattice filter
represented by the RCs is stable when the absolute value of each reflection
coefficient is less than 1. When the filter is stable, the block outputs a
Boolean value of `1` for each input channel at the
**S** port. When the filter is unstable, the block
outputs a Boolean value of `0` for each input channel at
the **S** port.

### **If first input value is not 1** — Action to take if first input value is not 1 `Replace it with 1` (default) | `Normalize` | `Normalize and warn` | `Error`

Specify the action to take if the first coefficient of the LPC coefficient
vector in any channel is not a 1. You can set this parameter to one of the following:

- `Replace it with 1` — Changes
  the first value of the coefficient channel to 1. The other
  coefficient values are unchanged.
- `Normalize` — Divides the
  entire channel of coefficients by the first coefficient so that
  the first coefficient of the LPC coefficient vector is 1.
- `Normalize and Warn` — Divides
  the entire channel of coefficients by the first coefficient so
  that the first coefficient of the LPC coefficient vector is 1.
  The block displays a warning message telling you that your
  vector of coefficients has been normalized.
- `Error` — Displays an error
  telling you that the first coefficient of the LPC coefficient
  channel is not 1.

#### Dependencies

To enable this parameter, set **Type of conversion**
to `LPC to RC`.

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

Convert linear prediction coefficients to reflection coefficients or reflection coefficients to linear prediction coefficients

The LPC to/from RC block can convert linear prediction coefficients (LPCs) to
reflection coefficients (RCs) or reflection coefficients to linear prediction
coefficients. Set the **Type of conversion** parameter to
`LPC to RC` or `RC to LPC` to
select the domain for converting your coefficients. For more information, see Algorithm.

Consider a signal, *x* (*n*), as the input to an FIR
analysis filter represented by LPC coefficients. The output of the analysis filter,
*e* (*n*), is known as the prediction error
signal. The power of this error signal is denoted by *P*. When the zero
lag autocorrelation coefficient of *x* (*n*) is 1, the
autocorrelation sequence and prediction error power are said to be normalized.
