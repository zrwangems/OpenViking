---
type: simulink-block
title: 'Gammatone Filter Bank'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'gammatonefilterbank'
documentation_source_path: 'ref/gammatonefilterbank.html'
language: en
---

# Gammatone Filter Bank

## Ports

### Input

### **Port\_1** — Audio input to filter bank scalar | vector | matrix

Audio input to the filter bank, specified as a scalar, vector, or matrix. If you
specify the input as a matrix, the block treats the columns as independent audio
channels. If you specify the input as a vector, the block treats the input as
containing a single channel.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Audio output from filter bank scalar | vector | matrix | 3-D array

Audio output from the filter bank, returned as a scalar, vector, matrix, or 3-D
array. The shape of output signal depends on the shape of input signal and
**Number of
filters**. If input is an *M*-by-*N*
matrix, then output is an *M*-by-Number of
filters-by-*N* array. If *N* is
`1`, then output is a matrix.

**Data Types:** `single` | `double`

## Parameters

### **Frequency range (Hz)** — Frequency range of filter bank `[50 8000]` (default) | two-element row vector of monotonically increasing values

Frequency range of the filter bank, specified as a two-element row vector of
monotonically increasing values in Hz.

**Tunable:** No

### **Number of filters** — Number of filters `32` (default) | positive integer

Number of filters in the filter bank, specified as a positive integer.

**Tunable:** No

### **Inherit sample rate from input** — Specify sample rate from input port `off` (default) | `on`

Select this parameter to specify the sample rate from the input port.

### **Input sample rate (Hz)** — Input sample rate `16000` (default) | positive integer

Input sample rate, specified as a positive integer in Hz.

**Tunable:** No

#### Dependencies

To enable this parameter, set **Inherit sample rate
from input port** to `off`.

### **Bands as separate output port** — Separate ports for each filter output `off` (default) | `on`

Select this parameter to separate ports for each filter output.

**Tunable:** No

### **View Filter Response** — Visualize filter bank responses button

This button visualizes gammatone filter bank responses.

### **Variable name** — Variable name of exported filter bank `myFilt` (default) | valid variable name

Name of the variable in the base workspace to contain the filter bank when it is
exported. The name must be a valid MATLAB® variable name.

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

You cannot export the filter if you have enabled the **Inherit sample rate
from input** parameter and the model is not running.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

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

Gammatone filter bank

The Gammatone Filter Bank block decomposes a signal by passing it through a
bank of gammatone filters equally spaced on the equivalent rectangular bandwidth (ERB) scale.
Gammatone filter banks are designed to model the human auditory system.
