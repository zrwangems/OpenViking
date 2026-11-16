---
type: simulink-block
title: 'Weighting Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'weightingfilter'
documentation_source_path: 'ref/weightingfilter.html'
language: en
---

# Weighting Filter

## Ports

### Input

### **Port\_1** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an independent channel.
- 1-D vector input –– The input is treated as a single channel.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal matrix

The Weighting Filter block outputs a signal with
the same data type as the input signal. The size of the output depends
on the size of the input:

- Matrix input –– The block outputs a matrix the same size and data type as the input
  signal.
- 1-D vector input –– The block outputs an *N*-by-1 matrix (column vector),
  where *N* is the number of elements in the 1-D
  vector.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Weighting method** — Type of frequency weighting `A-weighting` (default) | `C-weighting` | `K-weighting`

See A-Weighting, C-Weighting, and K-Weighting for the definition of the weighting
curves.

**Tunable:** No

### **Inherit sample rate from input** — Specify source of input sample rate `off` (default) | `on`

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, you specify the sample rate
in **Input sample rate (Hz)**.

**Tunable:** No

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | `positive scalar`

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time but the speed of the
  subsequent simulations is faster than `Interpreted
  execution`.
- `Interpreted execution` –– Simulate model
  using the MATLAB® interpreter. This option shortens startup time but has
  a slower simulation speed compared to `Code
  generation`. In this mode, you can debug the source
  code of the block.

**Tunable:** No

### **Mask for attenuation limits** — Creates a mask for filter response visualization `No mask` (default) | `Class 1` | `Class 2`

The mask attenuation limits are defined in the IEC 61672-1:2002
standard.

- If the mask is green, the design is compliant.
- If the mask is red, the design breaks compliance.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Weighting method** to
`A-weighting` or
`C-weighting`.

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

You cannot export the filter if you have enabled the **Inherit
sample rate from input** parameter and the model is not
running.

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

Weighted frequency response filter

The Weighting Filter block performs frequency-weighted
filtering independently across each input channel.
