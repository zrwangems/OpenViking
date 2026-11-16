---
type: simulink-block
title: 'Modified Covariance Method'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Spectral Analysis / Non-Parametric Estimation'
documentation_page: 'modifiedcovariancemethod'
documentation_source_path: 'ref/modifiedcovariancemethod.html'
language: en
---

# Modified Covariance Method

## Ports

### Input

### **Input** — Input column vector | unoriented vector

Specify the input as a column vector or an unoriented vector. This
input represents a frame of consecutive time samples from a
single-channel signal.

**Data Types:** `single` | `double`
### Output

### **Output** — Power spectral density estimate column vector

Power spectral density estimate of the signal at
*Nfft* equally spaced
frequency points, returned as a column vector. The frequency points are
in the range [0,*Fs*), where
*Fs* is the sampling
rate of the signal.

**Data Types:** `single` | `double`

## Parameters

### **Estimation order** — Order of AR model `6` (default) | positive integer

Specify the estimation order of the AR model (all-pole model) as a
positive integer. The block computes the spectrum from the FFT of the
estimated AR model parameters. To guarantee a nonsingular output, the value
of the **Estimation order** parameter must be less than or
equal to 2/3 of the input vector length.

### **Inherit FFT length from estimation order** — Inherit FFT length from estimation order `off` (default) | `on`

When you select the **Inherit FFT length from estimation
order** parameter, the FFT length
*Nfft* is one greater than
the estimation order. To specify the number of points on which to perform
the FFT, clear the **Inherit FFT length from estimation
order** parameter. You can then specify a power-of-two FFT
length using the **FFT length** parameter. The block
zero-pads or wraps the input to
*Nfft* before computing the
FFT.

### **FFT length** — FFT length `256` (default) | positive integer greater than or equal to 2

Enter the number of data points
*Nfft* on which to perform the
FFT as a positive integer greater than or equal to 2. When
*Nfft* is larger than the
input frame size, the block zero-pads each frame as needed. When
*Nfft* is smaller than the
input frame size, the block wraps each frame as needed.

#### Dependencies

To enable this parameter, clear the **Inherit FFT length from estimation
order** parameter.

### **Inherit sample time from input** — Inherit sample time from input `on` (default) | `off`

When you select the **Inherit sample time from input** parameter, the
block computes the frequency data from the sample period of the input
signal. For the block to produce valid output, the following conditions must hold:

- The input to the block is the original signal, with no samples
  added or deleted (by insertion of zeros, for example).
- The sample period of the time-domain signal in the simulation
  equals the sample period of the original time series.

If these conditions do not hold, clear the **Inherit sample time
from input** check box. You can then specify a sample time
using the **Sample time of original time series**
parameter.

### **Sample time of original time series** — Sample time of original time-domain signal `1` (default) | positive scalar

Specify the sample time of the original time-domain signal as a positive
scalar.

#### Dependencies

To enable this parameter, clear the **Inherit sample time from
input** parameter.

## Libraries

DSP System Toolbox / Estimation / Power Spectrum Estimation

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

Power spectral density estimate using modified covariance method

The Modified Covariance Method block estimates the power spectral density
(PSD) of the input using the modified covariance method. This method fits an
autoregressive (AR) model to the signal by minimizing the forward and backward
prediction errors in the least squares sense.

The block computes the spectrum from the FFT of the estimated AR model
parameters.
