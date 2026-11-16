---
type: simulink-block
title: 'Yule-Walker Method'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'yulewalkermethod'
documentation_source_path: 'ref/yulewalkermethod.html'
language: en
---

# Yule-Walker Method

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

The block outputs are always nonsingular.

**Data Types:** `single` | `double`

## Parameters

### **Inherit estimation order from input dimensions** — Inherit estimation order from input dimensions `off` (default) | `on`

When you select **Inherit estimation order from input dimensions**
parameter, the block sets the order of the all-pole model (estimation order)
to a value that is one less than the length of the input frame size.
Otherwise, the **Estimation order** parameter value
specifies the order. The block computes the spectrum from the FFT of the
estimated AR model parameters.

### **Estimation order** — Order of AR model `6` (default) | nonnegative integer

Specify the estimation order of the AR model as a nonnegative integer. To
guarantee a valid output, the **Estimation order**
parameter must be less than or equal to 1/2 the input vector length.

#### Dependencies

To enable this parameter, clear the **Inherit estimation order
from input dimensions** parameter.

### **Inherit FFT length from estimation order** — Inherit FFT length from estimation order `off` (default) | `on`

When you select the **Inherit FFT length from estimation order**
parameter, the FFT length *Nfft* is
one greater than the estimation order. To specify the number of points on
which to perform the FFT, clear the **Inherit FFT length from
estimation order** parameter. You can then specify the FFT
length as a power of 2 using the **FFT length** parameter.
The block zero-pads or wraps the input to
*Nfft* before computing the
FFT.

### **FFT length** — FFT length `256` (default) | positive integer greater than or equal to 2

Enter the number of data points *Nfft* on which
to perform the FFT as a positive integer greater than or equal to 2. When
*Nfft* is larger than the
input frame size, the block zero-pads each frame as needed. When
*Nfft* is smaller than the
input frame size, the block wraps each frame as needed.

#### Dependencies

To enable this parameter, clear the **Inherit FFT length from input
dimensions** parameter.

### **Inherit sample time from input** — Inherit sample time from input `on` (default) | `off`

When you select the **Inherit sample time from input** parameter, the
block computes the frequency data from the sample period of the input
signal. For the block to produce a valid output, the following conditions
must hold:

- The input to the block is the original signal with no samples
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

Power spectral density estimate using Yule-Walker method

The Yule-Walker Method block estimates the power spectral density (PSD) of
the input using the Yule-Walker AR method. This method, also called the autocorrelation
method, fits an autoregressive (AR) model to the windowed input data by minimizing the
forward prediction error in the least squares sense. This process leads to the
Yule-Walker equations, which the Levinson-Durbin recursion solves.

The block computes the spectrum from the FFT of the estimated AR model
parameters.
