---
type: simulink-block
title: 'Inverse Short-Time FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'inverseshorttimefft'
documentation_source_path: 'ref/inverseshorttimefft.html'
language: en
---

# Inverse Short-Time FFT

## Ports
```yaml
ports:
- name: X[nL,k]
  summary: Frequency-domain input signal unoriented vector | column vector | matrix
  direction: input
  data_types: single | double
- name: w[n]
  summary: Analysis window vector
  direction: input
  data_types: single | double
- name: x[n]
  summary: Inverse short-time FFT output vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **X[nL,k]** — Frequency-domain input signal unoriented vector | column vector | matrix

Specify the frequency-domain input signal as a vector or a matrix. The FFT length is
equal to the number of rows in the input at the
**x[nL,k]** port. Hence the number of input rows
must be greater than or equal to the window length.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **w[n]** — Analysis window vector

Specify the analysis window at the **w[n]**
port.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **x[n]** — Inverse short-time FFT output vector | matrix

The block outputs the inverse short-time FFT output at the port
**x[n]**.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Analysis window length
  summary: Length of analysis window 512 (default) | positive integer greater than 1
  group: ''
- name: Overlap between consecutive STFFT frames (in samples)
  summary: Overlap length 384 (default) | nonnegative integer
  group: ''
- name: Samples per output frame
  summary: Number of samples per output frame 512 (default) | positive integer
  group: ''
- name: Input is conjugate symmetric
  summary: Input to the block is conjugate symmetric on (default) | off
  group: ''
- name: Assert if analysis window does not support perfect signal reconstruction
  summary: Error if analysis window does not support perfect signal reconstruction off (default) | on
  group: ''
- name: Reconstruction error tolerance
  summary: Reconstruction error tolerance of original signal 1e-4 (default) | real scalar
  group: ''
```

### **Analysis window length** — Length of analysis window `512` (default) | positive integer greater than 1

Enter the length of the analysis window as a positive integer greater than
1.

### **Overlap between consecutive STFFT frames (in samples)** — Overlap length `384` (default) | nonnegative integer

Enter the number of samples of overlap for each frame of the input signal as a
nonnegative integer. This value should be the same as the **Overlap
between consecutive windows (in samples)** parameter in the
dialog box of the Short-Time FFT block.

### **Samples per output frame** — Number of samples per output frame `512` (default) | positive integer

Enter the desired frame size of the output signal as a positive
integer.

### **Input is conjugate symmetric** — Input to the block is conjugate symmetric `on` (default) | `off`

Select this check box when the input to the block is both floating point and conjugate
symmetric and you want real-valued outputs. If you select this check box
when the input is not conjugate symmetric, the output of the block is
invalid. This parameter cannot be used for fixed-point signals.

### **Assert if analysis window does not support perfect signal reconstruction** — Error if analysis window does not support perfect signal reconstruction `off` (default) | `on`

Select this check box to display an error when the analysis window used by
the Short-Time FFT block does not support perfect signal
reconstruction.

A time-domain signal input to the Short-time FFT block
cannot be perfectly reconstructed.

To determine if the signal can be perfectly reconstructed, the
Inverse Short-time FFT block uses the values you enter in
the **Analysis window length** and **Reconstruction
error tolerance** parameters.

### **Reconstruction error tolerance** — Reconstruction error tolerance of original signal `1e-4` (default) | real scalar

Enter the amount of acceptable error in the reconstruction of the original
signal as a real scalar.

#### Dependency

To enable this parameter, select the **Assert if analysis
window does not support perfect signal reconstruction**
check box.
## Libraries

DSP System Toolbox / Transforms / Matrix Operations

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

Usage notes and limitations:

- Generated code relies on the `memcpy` or
  `memset` function (`string.h`) under certain
  conditions.
- When the input length is not a power of 2, the executable generated from
  this block relies on prebuilt dynamic library files (`.dll`
  files) included with MATLAB®. Use the `packNGo` function to package the
  code generated from this block and all the relevant files in a compressed
  zip file. Using this zip file, you can relocate, unpack, and rebuild your
  project in another development environment where MATLAB is not installed. For more details, see How To Run a Generated Executable Outside MATLAB.

  When the input length is a power of 2, you can generate standalone C and
  C++ code from this block.

## Version History

**Introduced before R2006a**

## Description

Recover time-domain signals by performing inverse short-time fast Fourier transform (FFT)

The Inverse Short-Time FFT block reconstructs the time-domain signal from the
frequency-domain output of the Short-Time FFT block using a two-step
process. First, the block implements the overlap-add algorithm.

x[n]=LW(0)∑p=−∞∞[1N∑k=0N−1X[pL,k]ej2πkn/N]

Then, the block rebuffers the signal in order to reconstruct the time-domain signal.
Depending on the analysis window used by the Short-Time FFT block, the Inverse Short-Time FFT block might
or might not achieve perfect reconstruction of the time-domain signal.
