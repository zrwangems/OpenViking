---
type: simulink-block
title: 'Phase Extractor'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'phaseextractor'
documentation_source_path: 'ref/phaseextractor.html'
language: en
---

# Phase Extractor

## Ports

### Input

### **Input 1** — Input signal vector | matrix

Specify the input signal as a vector or a matrix. When the input is a
matrix, the block treats each column of the signal as an independent
channel. The first dimension is the length of the channel. The second
dimension is the number of channels. The block treats one dimensional
inputs as one channel.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output 1** — Unwrapped phase vector | matrix

The block returns the unwrapped phase of the signal.

The block preserves the input size and dimension, and the output port
rate equals the input port rate.

**Data Types:** `single` | `double`

## Parameters

### **Unwrap phase only within the frame** — Unwrap phase only within the frame `off` (default) | `on`

When you clear this check box, the block ignores boundaries between the
input frames. When you select this check box, the block treats each frame of
input data independently, and resets the initial phase value for each new
input frame.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Signal Operations

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

**Introduced in R2014b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Extract the unwrapped phase of a complex input

The Phase Extractor block extracts the unwrapped phase of a complex
input.
