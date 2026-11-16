---
type: simulink-block
title: 'LPC to/from Cepstral Coefficients'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'lpctofromcepstralcoefficients'
documentation_source_path: 'ref/lpctofromcepstralcoefficients.html'
language: en
---

# LPC to/from Cepstral Coefficients

## Ports

### Input

### **A** — LPC coefficients vector | matrix

Specify the LPC coefficients as a vector or a matrix. The block treats each column of
the matrix as a channel. When you specify an unoriented vector, the
block treats the input as one channel.

This port is unnamed until you set **Specify P** to
`via input port`.

#### Dependencies

To enable this port, set **Type of conversion**
to `LPCs to cepstral coefficients`.

**Data Types:** `single` | `double`

### **CC** — Cepstral coefficients vector | matrix

Specify the cepstral coefficients as a vector or a matrix. The block treats each column
of the matrix as a channel. When you specify an unoriented vector, the
block treats the input as one channel.

#### Dependencies

To enable this port, set **Type of conversion**
to `Cepstral coefficients to LPCs`.

**Data Types:** `single` | `double`

### **P** — Prediction error power scalar | vector

Specify the prediction error power *P* for each
channel as a vector through this port. The length of this vector must
equal the number of channels in the input.

#### Dependencies

To enable this port, set **Specify P** to
`via input port`.

**Data Types:** `single` | `double`
### Output

### **CC** — Cepstral coefficients vector | matrix

Cepstral coefficients, returned as a vector or a matrix.

#### Dependencies

To enable this port, set **Type of conversion**
to `LPCs to cepstral coefficients`.

**Data Types:** `single` | `double`

### **P** — Prediction error power scalar | vector

Prediction error power *P* for each channel, returned
as a scalar or a vector through this port. The length of this vector
must equal the number of channels in the input.

#### Dependencies

To enable this port, select **Output P**.

**Data Types:** `single` | `double`

## Parameters

### **Type of conversion** — Type of conversion `LPCs to cepstral coefficients` (default) | `Cepstral coefficients to LPCs`

Specify the domain for converting the coefficients as one of these:

- `LPCs to cepstral
  coefficients`
- `Cepstral coefficients to
  LPCs`

### **Specify P** — Method of specifying prediction error power *P* `assume P equals 1` (default) | `via input port`

Specify the prediction error power *P* using one of these options:

- `assume P equals 1` –– Specify the
  value of *P* to 1 for all channels.
- `via input port` –– Use the
  **P** port to input the prediction error
  power for each channel. The length of this vector must equal the
  number of channels in the input.

#### Dependencies

To enable this parameter, set **Type of conversion**
to `LPCs to cepstral coefficients`.

### **Output P** — Output prediction error power *P* `off` (default) | `on`

Select this check box to output the prediction error power for each
channel from output port **P**.

#### Dependencies

To enable this parameter, set **Type of conversion**
to `Cepstral coefficients to LPCs`

### **Output size same as input size** — Output size same as input size `off` (default) | `on`

When you select this check box, the length of the input vector of LPCs is
equal to the output vector of CCs. When you do not select this check box,
enter a positive scalar for the **Length of output cepstral
coefficients** parameter.

#### Dependencies

To enable this parameter, set **Type of conversion**
to `LPCs to cepstral coefficients`.

### **Length of output cepstral coefficients vector** — Length of output cepstral coefficients `10` (default) | positive integer

Specify the length of the output cepstral coefficients vector as a
positive integer. This value determines the length of each channel in the
output cepstral coefficients.

#### Dependencies

To enable this parameter, set **Type of conversion**
to `LPCs to cepstral coefficients`

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
  an error stating that the first coefficient of the LPC
  coefficient vector is not 1.

#### Dependencies

To enable this parameter, set **Type of conversion**
to `LPCs to cepstral coefficients`.

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

Convert linear prediction coefficients to cepstral coefficients or cepstral coefficients to linear prediction coefficients

The LPC to/from Cepstral Coefficients block can convert linear prediction
coefficients (LPCs) to cepstral coefficients (CCs) or cepstral coefficients to linear
prediction coefficients. Set the **Type of conversion** parameter to
`LPCs to cepstral coefficients` or `Cepstral
coefficients to LPCs` to select the domain for converting your
coefficients. For more information, see Algorithms.

Consider a signal *x*(*n*) as the input to an FIR
analysis filter represented by LPCs. The output of this analysis filter,
*e*(*n*), is known as the prediction error signal.
The power of this error signal is denoted by *P*, the prediction error
power.
