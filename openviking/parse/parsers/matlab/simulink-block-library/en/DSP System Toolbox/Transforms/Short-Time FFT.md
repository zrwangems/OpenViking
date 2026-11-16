---
type: simulink-block
title: 'Short-Time FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'shorttimefft'
documentation_source_path: 'ref/shorttimefft.html'
language: en
---

# Short-Time FFT

## Ports

### Input

### **x[n]** — Input signal vector | matrix

Specify the time-domain input signal as a vector or a matrix. If the input is a matrix,
the block treats each column as an independent channel. The input can be
a variable-size signal. That is, the frame size of the signal can change
while the simulation is running. The number of channels must remain the
same.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **w[n]** — Analysis window vector vector

Connect your single-channel analysis window to the **w[n]** port. For
the **Analysis window length** parameter, enter the
length of the analysis window *W*. The block buffers
the input signal such that it has a frame length of
*W*.

If the window vector is fixed point, it must be a
signed integer or signed fixed point with a power-of-two slope and zero
bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### Output

### **X[nL,k]** — Short-time FFT output vector | matrix

The block outputs the complex-valued single-channel or multichannel short-time FFT at
this port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Analysis window length** — Length of analysis window `512` (default) | positive integer greater than 1

Specify the frame length of the analysis window as a positive integer greater than 1. The
block buffers the input into overlapping window segments using the specified
window length and overlap length, and then multiplies each overlapped
segment by the window.

### **Overlap between consecutive windows (in samples)** — Overlap length `384` (default) | nonnegative integer

Specify the number of samples by which consecutive windows overlap in each frame of the
input signal as a nonnegative integer. The window overlap reduces artifacts
at the data boundaries.

### **FFT length** — FFT length `1024` (default) | positive integer greater than or equal to 2

Enter the length up to which the block pads the input signal as a positive integer
greater than or equal to 2. After the block buffers and windows the signal,
it zero-pads the signal before computing the FFT. This parameter determines
the length of the short-time fast Fourier transform output (number of rows).
The FFT length must be greater than or equal to the window length.

## Libraries

DSP System Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Generated code relies on the `memcpy` or
  `memset` function (`string.h`) under certain
  conditions.
- When the FFT length is not a power of two, the executable generated from
  this block relies on prebuilt dynamic library files (`.dll`
  files) included with MATLAB®. Use the `packNGo` function to package the
  code generated from this block and all the relevant files in a compressed
  zip file. Using this zip file, you can relocate, unpack, and rebuild your
  project in another development environment where MATLAB is not installed. For more details, see How To Run a Generated Executable Outside MATLAB.

  When the FFT length is a power of two, you can generate standalone C and
  C++ code from this block.

## Version History

**Introduced before R2006a**

## Description

Nonparametric estimate of spectrum using short-time fast Fourier transform (STFT) method

The Short-Time FFT block computes a nonparametric estimate of the spectrum. The block
buffers, applies a window, and zero pads the input signal. The block then takes the FFT
of the signal, transforming it into the frequency domain.
