---
type: simulink-block
title: 'Octave Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Filters'
documentation_page: 'octavefilter'
documentation_source_path: 'ref/octavefilter.html'
language: en
---

# Octave Filter

## Ports

### Input

### **x** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an
  independent channel.
- 1-D vector input –– The input is treated as a single
  channel.

This port is unnamed unless you specify additional input ports.

**Data Types:** `single` | `double`

### **CF** — Center frequency (Hz) scalar in the range `3` to `22,000` inclusive

#### Dependencies

To enable this port, select **Specify from input
port** for the Center frequency (Hz)
parameter.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal matrix

The Octave Filter block outputs a signal with the same
data type as the input signal. The size of the output depends on the
size of the input:

- Matrix input –– The block outputs a matrix the same size and
  data type as the input signal.
- 1-D vector input –– The block outputs an
  *N*-by-1 matrix (column vector), where
  *N* is the number of elements in the 1-D
  vector.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Filter order** — Order of octave filter `6` (default) | even integer

**Tunable:** No

### **Center frequency (Hz)** — Center frequency of octave filter `1000` (default) | scalar in the range `3` to `22,000` inclusive

- The maximum center frequency is the value that causes the upper
  band edge to be equal to the Nyquist frequency,
  *Fs*/2. Frequencies above this value are
  saturated.
- The minimum center frequency is the value that causes the lower
  band edge to be equal to 1 Hz. Frequencies below this value are
  quantized to 1 Hz.

To specify **Center frequency (Hz)** from an input port,
select **Specify from input port** for the
parameter.

**Tunable:** Yes

### **Bandwidth** — Filter bandwidth in octaves `1 octave` (default) | `2/3 octave` | `1/2 octave` | `1/3 octave` | `1/6 octave` | `1/12 octave` | `1/24 octave` | `1/48 octave`

**Tunable:** Yes

### **Oversample the input by 2 for this filter** — Oversample toggle off (default) | on

- off –– The Octave Filter block runs at the
  input sample rate.
- on –– The Octave Filter block runs at two times
  the input sample rate. Oversampling minimizes the frequency
  warping effects introduced by the bilinear transformation. An
  FIR halfband interpolator implements oversampling before octave
  filtering. A halfband decimator reduces the sample rate back the
  input sampling rate after octave filtering.

**Tunable:** No

### **Inherit sample rate from input** — Specify source of input sample rate off (default) | on

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, you specify the sample rate
in **Input sample rate (Hz)**.

**Tunable:** No

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | scalar

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` –– Simulate the model
  using generated C code. The first time you run a simulation,
  Simulink® generates C code for the block. The C code is reused
  for subsequent simulations as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.
- `Interpreted execution` –– Simulate the
  model using the MATLAB® interpreter. This option shortens startup time but has
  a slower simulation speed than `Code
  generation`. In this mode, you can debug the source
  code of the block.

**Tunable:** No

### **Mask for attenuation limits** — Create a mask for filter response visualization `No mask` (default) | `Class 0` | `Class 1` | `Class 2`

The mask attenuation limits are defined in the ANSI S1.11-2004
standard.

- If the mask is green, the design is compliant.
- If the mask is red, the design breaks compliance.

**Tunable:** Yes

### **Visualize filter response** — Open plot to visualize magnitude response and compliance mask button

A 2048-point FFT is used to calculate the magnitude response.

**Tunable:** Yes

### **Variable name** — Variable name of exported filter `myFilt` (default) | valid variable name

Name of the variable in the base workspace to contain the filter when it
is exported. The name must be a valid MATLAB variable name.

### **Overwrite variable if it already exists** — Overwrite variable if it already exists `on` (default) | `off`

When you select this parameter, exporting the filter overwrites the
variable specified by the **Variable name** parameter if it
already exists in the base workspace. If you do not select this parameter
and the specified variable already exists in the workspace, exporting the
filter creates a new variable with an underscore and a number appended to
the variable name. For example, if the variable name is
`var` and it already exists, the exported variable will
be named `var_1`.

### **Export filter to workspace** — Export filter to workspace button

Export the filter to the base workspace in the variable specified by the
**Variable name** parameter.

#### Tips

- You cannot export the filter if you have enabled the
  **Inherit sample rate from input**
  parameter and the model is not running.
- You cannot export the filter if you are specifying filter
  characteristics from input ports.

## Libraries

Audio Toolbox / Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Octave-band and fractional octave-band filter

The Octave Filter block performs octave-band or fractional octave-band
filtering independently across each input channel. An octave-band is a frequency band
where the highest frequency is twice the lowest frequency. Octave-band and fractional
octave-band filters are commonly used to mimic how humans perceive loudness. Octave
filters are best understood when viewed on a logarithmic scale, which models how the
human ear weights the spectrum.
