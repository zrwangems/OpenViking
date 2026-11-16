---
type: simulink-block
title: 'Multiband Parametric EQ'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'multibandparametriceq'
documentation_source_path: 'ref/multibandparametriceq.html'
language: en
---

# Multiband Parametric EQ

## Ports

### Input

### **Port\_1** — Audio input to equalizer matrix | vector

Audio input to the equalizer, specified as one of the following:

- Matrix input –– The block treats each column of the input as an independent
  channel.
- Vector input –– The block treats the input as having a single
  channel.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Audio output from equalizer matrix

Audio output from the equalizer, returned as a matrix. If you specify the input as
a matrix, the block returns the output with the same size as matrix input. If you
specify the input as a vector then the output is N-by-1 matrix.

**Data Types:** `single` | `double`

## Parameters

### Main

### **EQ order** — Order of individual equalizer bands `2` (default) | even positive integer

Order of individual equalizer bands, specified as an even positive integer. All
equalizer bands have the same order.

### **Number of bands** — Number of equalizer bands `3` (default) | integer in the range `[1,10]`

Number of equalizer bands, specified as an integer in the range
`[1,10]`. The number of equalizer bands does not include shelving
filters, highpass filters, or lowpass filters.

### **Specify frequencies from input port** — Specify frequencies from input port `off` (default) | `on`

Select this parameter to specify frequencies from the input port.

### **Frequencies (Hz)** — Center frequencies of equalizer bands `[100,181,325]` (default) | row vector of length equal to Number of bands

Center frequencies of equalizer bands in Hz, specified as a row vector of length
equal to **Number of
bands**. The vector consists of real scalars in the range
`0` to **Input sample rate
(Hz)**/2.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Specify input
frequencies from input port** to `off`.

### **Specify peak gains from input port** — Specify peak gains from input port `off` (default) | `on`

Select this parameter to specify peak gains from input port.

### **Peak Gains (dB)** — Peak or dip filter gains `[0,0,0]` (default) | row vector of length equal to Number of bands

Peak or dip filter gains, specified as a row vector of length equal to
**Number of
bands** in dB. The vector consists of real scalars in the range
`[–inf,20]`.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Specify peak gains
from input port** to `off`.

### **Specify quality factors from input port** — Specify quality factors from input port `off` (default) | `on`

Select this parameter to specify quality factors from the input port.

### **Quality factors** — Quality factors of equalizer bands `[1.6,1.6,1.6]` (default) | row vector

Quality factors of equalizer bands, specified as a row vector of length equal to
**Number of bands**.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Specify quality
factor from input port** to `off`.

### **Inherit sample rate from input** — Specify sample rate from input port `off` (default) | `on`

Select this parameter to specify sample rate from the input port.

### **Input sample rate (Hz)** — Input sample rate `44100` (default) | positive scalar

Input sample rate, specified as a positive scalar in Hz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Inherit sample rate
from input port** to `off`.

### **Visualize filter response** — Visualize magnitude response of equalizer button

This button plots the filter responses of low-shelf, high-shelf, highpass
(low-cut), and lowpass (high-cut) filters in a magnitude (dB) vs. frequencies (Hz) plot.

**Note**

The block does not support filter visualization if any parameters are
specified from input ports or the sample rate is inherited.

### **Variable name** — Variable name of exported filter `myFilt` (default) | valid variable name

Name of the variable in the base workspace to contain the filter when it is
exported. The name must be a valid MATLAB® variable name.

### **Overwrite variable if it already exists** — Overwrite variable if it already exists `on` (default) | `off`

When you select this parameter, exporting the filter overwrites the variable
specified by the **Variable name** parameter if it already exists in
the base workspace. If you do not select this parameter and the specified variable
already exists in the workspace, exporting the filter creates a new variable with an
underscore and a number appended to the variable name. For example, if the variable
name is `var` and it already exists, the exported variable will be
named `var_1`.

### **Export filter to workspace** — Export filter to workspace button

Export the filter to the base workspace in the variable specified by the
**Variable name** parameter.

#### Tips

- You cannot export the filter if you have enabled the **Inherit
  sample rate from input** parameter and the model is not
  running.
- You cannot export the filter if you are specifying filter characteristics
  from input ports.

### Advanced

### **Add low-shelf filter** — Add low-shelf filter to equalizer `off` (default) | `on`

Select this parameter to add a low-shelf filter to your equalizer.

### **Specify low-shelf cutoff from input port** — Specify low-shelf cutoff frequency from input port `off` (default) | `on`

Select this parameter to specify the cutoff frequency of the low-shelf filter from
the input port.

#### Dependencies

To enable this parameter, set **Add low-shelf
filter** to `on`.

### **Low-shelf cutoff frequency (Hz)** — Low-shelf cutoff frequency `200` (default) | scalar

The cutoff frequency of the low-shelf filter, specified as a scalar greater than
or equal to `0` in Hz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add low-shelf
filter** to `on` and **Specify low-shelf
cutoff from input port** to `off`.

### **Specify low-shelf slope from input port** — Specify low-shelf slope `off` (default) | `on`

Select this parameter to specify low-shelf slope from the input port.

#### Dependencies

To enable this parameter, set **Add low-shelf
filter** to `on`.

### **Low-shelf filter slope** — Low-shelf slope `1.5` (default) | positive scalar

The slope of the low-shelf filter, specified as a positive scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add low-shelf
filter** to `on` and **Specify low-shelf
slope from input port** to `off`.

### **Specify low-shelf gain from input port** — Specify low-shelf gain from input port `off` (default) | `on`

Select this parameter to specify the gain of the low-shelf filter from the input
port.

#### Dependencies

To enable this parameter, set **Add low-shelf
filter** to `on`.

### **Low-shelf filter gain (dB)** — Low-shelf gain `0` (default) | real scalar

The gain of the low-shelf filter, specified as a real scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add low-shelf
filter** to `on` and **Specify low-shelf
gain from input port** to `off`.

### **Add high-shelf filter** — Add high-shelf filter to equalizer `off` (default) | `on`

Select this parameter to add a high-shelf filter to your equalizer.

### **Specify high-shelf cutoff from input port** — Specify high-shelf cutoff frequency from input port `off` (default) | `on`

Select this parameter to specify the cutoff frequency of the high-shelf filter
from the input port.

#### Dependencies

To enable this parameter, set **Add high-shelf
filter** to `on`.

### **High-shelf cutoff frequency (Hz)** — High-shelf cutoff frequency `15e3` (default) | scalar

The cutoff frequency of the high-shelf filter, specified as a scalar greater than
or equal to `0` in Hz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add high-shelf
filter** to `on` and **Specify high-shelf
cutoff from input port** to `off`.

### **Specify high-shelf slope from input port** — Specify high-shelf slope from input port `off` (default) | `on`

Select this parameter to specify the slope of the high-shelf filter from the input
port.

#### Dependencies

To enable this parameter, set **Add high-shelf
filter** to `on`.

### **High-shelf filter slope** — High-shelf slope `1.5` (default) | positive scalar

The slope of the high-shelf filter, specified as a positive scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add high-shelf
filter** to `on` and **Specify high-shelf
slope from input port** to `off`.

### **Specify high-shelf gain from input port** — Specify high-shelf gain from input port `off` (default) | `on`

Select this parameter to specify the gain of the high-shelf filter from the input
port.

#### Dependencies

To enable this parameter, set **Add high-shelf
filter** to `on`.

### **High-shelf filter gain (dB)** — High-shelf gain `0` (default) | real scalar

The gain of the high-shelf filter, specified as a real scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add high-shelf
filter** to `on` and **Specify high-shelf
gain from input port** to `off`.

### **Add lowpass filter** — Add lowpass filter to equalizer `off` (default) | `on`

Select this parameter to add a lowpass filter to your equalizer.

### **Specify lowpass cutoff from input port** — Specify lowpass cutoff frequency from input port `off` (default) | `on`

Select this parameter to specify the cutoff frequency of the lowpass filter from
the input port.

#### Dependencies

To enable this parameter, set **Add lowpass
filter** to `on`.

### **Lowpass cutoff frequency (Hz)** — Lowpass cutoff frequency `18e3` (default) | scalar

The cutoff frequency of the lowpass filter, specified as a scalar greater than or
equal to `0` in Hz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add lowpass
filter** to `on` and **Specify lowpass
cutoff from input port** to `off`.

### **Specify lowpass slope from input port** — Specify lowpass slope from input port `off` (default) | `on`

Select this parameter to specify the slope of the lowpass filter from the input
port.

#### Dependencies

To enable this parameter, set **Add lowpass
filter** to `on`.

### **Lowpass filter slope** — Lowpass slope `12` (default) | real scalar in the range `[0:6:48]`

The slope of the lowpass filter, specified as a real scalar in the range
`[0:6:48]` in dB/octave. Values that are not multiples of 6 are
rounded to the nearest multiple of 6.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add lowpass
filter** to `on` and **Specify lowpass
slope from input port** to `off`.

### **Add highpass filter** — Add highpass filter to equalizer `off` (default) | `on`

Select this parameter to add a highpass filter to your equalizer.

### **Specify highpass cutoff from input port** — Specify highpass cutoff frequency from input port `off` (default) | `on`

Select this parameter to specify the cutoff frequency of the highpass filter
cutoff from the input port.

#### Dependencies

To enable this parameter, set **Add highpass
filter** to `on`.

### **Highpass cutoff frequency (Hz)** — Highpass cutoff frequency `20` (default) | nonnegative real scalar

The cutoff frequency of the highpass filter, specified as a real scalar greater
than or equal to `0` in Hz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add highpass
filter** to `on` and **Specify highpass
cutoff from input port** to `off`.

### **Specify highpass slope from input port** — Specify highpass slope from input port `off` (default) | `on`

Select this parameter to specify the slope of the highpass filter from the input
port.

#### Dependencies

To enable this parameter, set **Add highpass
filter** to `on`.

### **Highpass filter slope** — Highpass slope `30` (default) | real scalar in the range `[0:6:48]`

The slope of the highpass filter, specified as a real scalar in the range
`[0:6:48]` in dB/octave. Values that are not multiples of 6 are
rounded to the nearest multiple of 6.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Add highpass
filter** to `on` and **Specify highpass
slope from input port** to `off`.

### **Oversample** — Oversample toggle `off` (default) | `on`

Oversample toggle, specified as one of the following:

- `off` –– Run the multiband parametric equalizer at the
  input sample rate.
- `on` –– Run the multiband parametric equalizer at two times
  the input sample rate. Oversampling minimizes the frequency-warping effects
  introduced by the bilinear transformation.

A halfband interpolator implements oversampling before equalization. A
halfband decimator reduces the sample rate back to the input sampling rate after
equalization.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as one of the following:

- `Interpreted execution` –– Simulate model using the
  MATLAB interpreter. This option shortens startup time and has simulation
  speed comparable to `Code generation`. In this mode, you
  can debug the source code of the block.
- `Code generation` –– Simulate model using generated C
  code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time but the speed of the subsequent simulations is faster than
  `Interpreted execution`.

**Tunable:** No

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

**Introduced in R2021b**

## Description

Multiband parametric equalizer

The Multiband Parametric EQ block performs multiband parametric
equalization independently across each channel of input using specified center frequencies,
gains, and quality factors. You can configure this block with up to 10 bands. You can add
low-shelf and high-shelf filters as well as highpass (low-cut) and lowpass (high-cut)
filters.
