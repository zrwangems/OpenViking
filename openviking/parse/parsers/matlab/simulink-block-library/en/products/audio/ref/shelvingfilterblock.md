---
type: simulink-block
title: 'Shelving Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Filters'
documentation_page: 'shelvingfilterblock'
documentation_source_path: 'ref/shelvingfilterblock.html'
language: en
---

# Shelving Filter

## Ports

### Input

### **x** — Input signal column vector | matrix

Input signal to be filtered, specified as a column vector or a matrix. If the
input is a matrix, each column is treated as an independent channel.

**Data Types:** `single` | `double`

### **G** — Peak gain (dB) real scalar

This port specifies the value of the **Gain
(dB)** parameter.

#### Dependencies

To enable this port, select the **Specify gain from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **S** — Slope positive scalar

This port specifies the value of the **Slope**
parameter.

#### Dependencies

To enable this port, select the **Specify slope from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **F** — Cutoff frequency nonnegative scalar

This port specifies the value of the **Cutoff frequency
(Hz)** parameter.

#### Dependencies

To enable this port, select the **Specify cutoff frequency from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Port\_1** — Output signal column vector | matrix

Filtered output signal, returned as a column vector or matrix that is the same
size and data type as the input signal.

**Data Types:** `single` | `double`

## Parameters

### **Specify gain from input port** — Use additional input port to specify gain `off` (default) | `on`

When you select this parameter, an additional input port, **G**, is
added to the block. This port specifies the gain of the filter.

### **Gain (dB)** — Peak gain (dB) `0` (default) | real scalar

Peak gain of the filter in dB, specified as a real scalar. The gain specifies how
much the filter will boost (if the gain is positive) or cut (if the gain is negative)
the frequency spectrum of the input signal.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify gain from input
port** parameter.

### **Specify slope from input port** — Use additional input port to specify slope `off` (default) | `on`

When you select this parameter, an additional input port, **S**, is
added to the block. This port specifies the slope of the filter.

### **Slope** — Filter slope `1.5` (default) | positive scalar

Slope of the filter specified as a positive scalar. The slope controls the width of
the transition band in the filter response.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify slope from input
port** parameter.

### **Specify cutoff frequency from input port** — Use additional input port to specify cutoff frequency `off` (default) | `on`

When you select this parameter, an additional input port, **F**, is
added to the block. This port specifies the cutoff frequency of the filter.

### **Cutoff frequency (Hz)** — Filter cutoff frequency `200` (default) | nonnegative scalar

Cutoff frequency of the filter in Hz, specified as a nonnegative scalar in the range [0,`Fs`/2], where `Fs` is the sample rate specified by the
**Input sample rate (Hz)** and **Inherit sample rate from
input** parameters. The cutoff frequency specifies the frequency at half of
the peak gain of the filter,
`G`/2 dB, where `G` is the peak gain.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify cutoff frequency from input
port** parameter.

### **Type** — Type of filter `lowpass` (default) | `highpass`

Type of shelving filter, specified as `lowpass` or
`highpass`.

- `lowpass` — Boost or cut the frequency spectrum below
  the cutoff frequency.
- `highpass` — Boost or cut the frequency spectrum above
  the cutoff frequency.

### **Inherit sample rate from input** — Specify source of input sample rate `off` (default) | `on`

When you select this parameter, the block inherits its sample rate from the input
signal. When you clear this parameter, you specify the sample rate in **Input
sample rate (Hz)**.

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | positive scalar

Sample rate of the input, specified as a positive scalar.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Visualize filter response** — Open plot to visualize filter response button

Open plot to visualize the magnitude response of the filter.

### **Variable name** — Variable name of exported filter `myFilt` (default) | valid variable name

Name of the variable in the base workspace to contain the filter when it is
exported. The name must be a valid MATLAB® variable name.

### **Overwrite variable if it already exists** — Overwrite variable if it already exists `on` (default) | `off`

When you select this parameter, exporting the filter overwrites the variable
specified by the **Variable name** parameter if it already exists in
the base workspace. If you do not select this parameter and the specified variable
already exists in the workspace, exporting the filter creates a new variable with an
underscore and a number appended to the variable name. For example, if the variable name
is `var` and it already exists, the exported variable will be named
`var_1`.

### **Export filter to workspace** — Export filter to workspace button

Export the filter to the base workspace in the variable specified by the
**Variable name** parameter.

#### Tips

- You cannot export the filter if you have enabled the **Inherit sample
  rate from input** parameter and the model is not running.
- You cannot export the filter if you are specifying filter characteristics from
  input ports.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate model using the
  MATLAB interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode,
  you can debug the source code of the block.
- `Code generation` — Simulate model using generated C
  code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

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

**Introduced in R2022a**

## Description

Second-order IIR shelving filter

The Shelving Filter block applies a shelving filter to the input signal. A shelving filter
boosts or cuts the frequency spectrum of the input signal above or below a given cutoff
frequency.
