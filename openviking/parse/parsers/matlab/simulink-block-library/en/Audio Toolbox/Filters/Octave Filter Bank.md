---
type: simulink-block
title: 'Octave Filter Bank'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'octavefilterbank'
documentation_source_path: 'ref/octavefilterbank.html'
language: en
---

# Octave Filter Bank

## Ports

### Input

### **Port\_1** — Input signal vector | matrix

- Vector input –– The block treats the input as a single channel.
- Matrix input –– The block treats each column of the input as an independent
  channel.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal matrix | 3-D array

The Octave Filter Bank block outputs a signal with the same data
type as the input signal. The shape of the output depends on the shape of the input,
the number of filters in the bank, and whether or not you enable the
**Bands as separate output ports** parameter.

If *F* is the number of filters in the bank, and the input
signal is an *L*-by-*C* matrix, then the block
returns an *L*-by-*F*-by-*C* array.
If *C* is 1, then the block outputs a matrix.

- Vector input –– When you provide a vector input, the block outputs an
  *L*-by-*F* matrix, where *L*
  is the number of elements in the vector and *F* is the number of
  filters in the bank.
- Matrix input –– When you provide a matrix input, the block outputs a 3-D array
  with size *L*-by-*F*-by-*C*,
  where *C* is the number of channels in the matrix input.

**Note**

When you enable the **Bands as separate output ports**
parameter, each output is the same size as the input.

**Data Types:** `single` | `double`

## Parameters

### **Bandwidth (octaves)** — Bandwidth of filters specified in octaves `1 octave` (default) | `2/3 octave` | `1/2 octave` | `1/3 octave` | `1/6 octave` | `1/12 octave` | `1/24 octave` | `1/48 octave`

Filter bandwidth in octaves, specified as `1 octave`, `2/3
octave`, `1/2 octave`, `1/3 octave`,
`1/6 octave`, `1/12 octave`, `1/24
octave`, `1/48 octave`.

### **Frequency range (Hz)** — Frequency range of filter bank (Hz) `[22 22050]` (default) | two-element row vector of positive monotonically increasing values

Frequency range of the filter bank in Hz, specified as a two-element row vector of
positive monotonically increasing values. The block places filter bank center
frequencies according to the **Bandwidth (octaves)**,
**Reference frequency (Hz)**, and **Octave ratio
base** parameters. Filters that have a center frequency outside of
**Frequency range (Hz)** are ignored.

### **Reference frequency (Hz)** — Reference frequency of filter bank (Hz) `1000` (default) | positive integer scalar

Reference frequency of the filter bank in Hz, specified as a positive integer
scalar. The ANSI S1.11-2004 standard defines the center frequencies of the octave
filters relative to the reference frequency. For more information, see Center Frequencies and Band Edges.

### **Filter order** — Order of octave filters `12` (default) | positive even integer

Order of the octave filters, specified as a positive even integer. The filter order
applies to each individual filter in the bank.

**Note**

The default filter order for the `octaveFilterBank` object is `2`.

### **Octave ratio** — Distance between filters `Base ten (ANSI S1.11 preferred)` (default) | `Base two (musical scale)`

Octave ratio base, specified as `Base ten (ANSI S1.11
preferred)` or `Base two (musical scale)`. The
octave ratio base determines the distribution of the center frequencies of the octave
filters. The ANSI S1.11 standard recommends base 10. Base 2 is popular for music
applications. **Base two (musical scale)** defines an octave as a
factor of 2, and **Base ten (ANSI S1.11 preferred)** defines an octave
as a factor of 10 0.3.

### **Inherit sample rate from input** — Allow sample rate to be set by input signal `off` (default) | `on`

When you select this parameter, the block inherits its sample rate from the input
signal. When you clear this parameter, you specify the sample rate in the
**Input sample rate (Hz)** parameter.

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | positive scalar

When you select this parameter, the block accepts the sample rate from the
user.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Bands as separate output ports** — One output port per filter band `off` (default) | `on`

When you select this parameter, the block provides an output port for each filter in
the bank. Each output port is labeled with the center frequency of the filter and has a
size identical to the input signal.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Code generation` –– Simulate the model using generated
  C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time.
- `Interpreted execution` –– Simulate the model using the
  MATLAB® interpreter. In this mode, you can debug the source code of the
  block.

### **View filter response** — Open plot to visualize magnitude response button

Octave filters are best understood when viewed on a logarithmic scale, which models
how the human ear weights the spectrum. The block uses a 2048-point FFT to calculate the
magnitude response. The filter bank's response is displayed on a log-frequency scale
with a legend to indicate the center frequency of each filter.

### **Variable name** — Variable name of exported filter bank `myFilt` (default) | valid variable name

Name of the variable in the base workspace to contain the filter bank when it is
exported. The name must be a valid MATLAB variable name.

### **Overwrite variable if it already exists** — Overwrite variable if it already exists `on` (default) | `off`

When you select this parameter, exporting the filter bank overwrites the variable
specified by the **Variable name** parameter if it already exists in
the base workspace. If you do not select this parameter and the specified variable
already exists in the workspace, exporting the filter bank creates a new variable with
an underscore and a number appended to the variable name. For example, if the variable
name is `var` and it already exists, the exported variable will be
named `var_1`.

### **Export filter to workspace** — Export filter bank to workspace button

Export the filter bank to the base workspace in the variable specified by the
**Variable name** parameter.

#### Tips

You cannot export the filter bank if you have enabled the **Inherit sample
rate from input** parameter and the model is not running.

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

**Introduced in R2021a**

## Description

Octave-band and fractional octave-band filter bank

The Octave Filter Bank block decomposes a signal into octave or
fractional-octave subbands. An octave-band is a frequency band where the highest frequency is
twice the lowest frequency. Octave-band and fractional octave-band filters are commonly used
to mimic how humans perceive loudness.
