---
type: simulink-block
title: 'Burg Method'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'burgmethod'
documentation_source_path: 'ref/burgmethod.html'
language: en
---

# Burg Method

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

### **Inherit estimation order from input dimensions** — Inherit estimation order from input dimensions `off` (default) | `on`

When you select the **Inherit estimation order from input dimensions**
parameter, the order of the all-pole model (estimation order) is one less
than the input frame size. Otherwise, the **Estimation
order** parameter determines the model order. The block
computes the spectrum from the FFT of the estimated AR model parameters.

### **Estimation order** — Order of AR model `6` (default) | nonnegative integer

Specify the estimation order of the AR model as a nonnegative integer.

#### Dependencies

To enable this parameter, clear the **Inherit estimation order from input
dimensions** parameter.

### **Inherit FFT length from estimation order** — Inherit FFT length from estimation order `off` (default) | `on`

When you select this parameter, the FFT length
*Nfft* is one greater than the
estimation order. To specify the number of points on which to perform the
FFT, clear the **Inherit FFT length from estimation order**
parameter. You can then specify the FFT length as a power of 2 using the
**FFT length** parameter. The block zero-pads or wraps
the input to *Nfft* before computing
the FFT.

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

- The input to the block is an original signal with no samples
  added or deleted (by insertion of zeros, for example).
- The sample period of the time-domain signal in the simulation
  equals the sample period of the original time series.

If these conditions do not hold, clear the **Inherit sample time
from input** parameter. You can then specify a sample time
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

Usage notes and limitations:

- When the FFT length is not a power of 2, the executable generated from
  this block relies on prebuilt dynamic library files (`.dll`
  files) included with MATLAB®. Use the `packNGo` function to package the
  code generated from this block and all the relevant files in a compressed
  zip file. Using this zip file, you can relocate, unpack, and rebuild your
  project in another development environment where MATLAB is not installed. For more details, see How To Run a Generated Executable Outside MATLAB.
- When the FFT length is a power of 2, you can generate standalone C and C++
  code from this block.

## Version History

**Introduced before R2006a**

## Description

Power spectral density estimate using Burg method

The Burg Method block estimates the power spectral density (PSD) of the input
frame using the Burg method. This method fits an autoregressive (AR) model to the signal
by minimizing (least squares) the forward and backward prediction errors. The block
minimizes the errors by constraining the AR parameters to satisfy the Levinson-Durbin
recursion.

The block computes the spectrum from the FFT of the estimated AR model parameters.
