---
type: simulink-block
title: 'LPC/RC to Autocorrelation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'lpcrctoautocorrelation'
documentation_source_path: 'ref/lpcrctoautocorrelation.html'
language: en
---

# LPC/RC to Autocorrelation

## Ports

### Input

### **A** — LPC coefficients vector | matrix

Specify the LPC coefficients as a vector or a matrix. The block treats each column of
the matrix as a separate channel. When you specify an unoriented vector,
the block treats the input as one channel.

#### Dependencies

To enable this port, set **Type of conversion**
to `LPC to autocorrelation`.

**Data Types:** `single` | `double`

### **K** — RC coefficients vector | matrix

Specify the RC coefficients as a vector or a matrix. The block treats each column of the
matrix as a separate channel. When you specify an unoriented vector, the
block treats the input as one channel.

#### Dependencies

To enable this port, set **Type of conversion**
to `RC to autocorrelation`.

**Data Types:** `single` | `double`

### **P** — Prediction error power scalar | vector

Specify the non-unity prediction error power *P* for
each channel as a vector through this port. The length of this vector
must equal the number of channels in the input.

#### Dependencies

To enable this port, set **Specify P** to
`Via input port`.

**Data Types:** `single` | `double`
### Output

### **AC** — Autocorrelation coefficients vector | matrix

Autocorrelation coefficients, returned as a vector or a matrix.

**Data Types:** `single` | `double`

## Parameters

### **Type of conversion** — Type of conversion `LPC to autocorrelation` (default) | `RC to autocorrelation`

Specify the domain for converting the coefficients as one of these:

- `LPC to autocorrelation`
- `RC to autocorrelation`

### **Specify P** — Method of specifying prediction error power *P* `Assume P = 1` (default) | `Via input port`

Specify the prediction error power *P* using one of these options:

- `Assume P=1` –– Specify the value of
  *P* to 1.
- `Via input port` –– Use the
  **P** port to input the value of the actual
  non-unity prediction error power for each channel. The length of
  this vector must equal the number of channels in the
  input.

### **If first input value is not 1** — Action to take if first input value is not 1 `Replace it with 1` (default) | `Normalize` | `Normalize and warn` | `Error`

Specify the action to take if the first coefficient of the LPC coefficient
vector is not 1. You can set this parameter to one of these options:

- `Replace it with 1` — The
  block changes the first value of the coefficient vector to 1.
  The rest of the coefficient values are unchanged.
- `Normalize` — The block
  divides the entire vector of coefficients by the first
  coefficient so that the first coefficient of the LPC coefficient
  vector is 1.
- `Normalize and Warn` — The
  block divides the entire vector of coefficients by the first
  coefficient so that the first coefficient of the LPC coefficient
  vector is 1. The block displays a warning message stating that
  the vector of coefficients has been normalized.
- `Error` — The block displays
  an error telling you that the first coefficient of the LPC
  coefficient vector is not 1.

#### Dependencies

To enable this parameter, set **Type of conversion**
to `LPC to autocorrelation`.

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

Convert linear prediction coefficients or reflection coefficients to autocorrelation coefficients

The LPC/RC to Autocorrelation block can convert linear prediction
coefficients (LPCs) to autocorrelation coefficients (ACs) or reflection coefficients
(RCs) to autocorrelation coefficients (ACs). Set the **Type of
conversion** parameter to `LPC to autocorrelation`
or `RC to autocorrelation` to select the domain for converting
your coefficients.
