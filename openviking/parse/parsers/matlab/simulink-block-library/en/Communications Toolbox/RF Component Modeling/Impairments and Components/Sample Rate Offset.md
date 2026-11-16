---
type: simulink-block
title: 'Sample Rate Offset'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'samplerateoffset'
documentation_source_path: 'ref/samplerateoffset.html'
language: en
---

# Sample Rate Offset

## Ports

### Input

### **In** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, an
*N*S element column vector, or an
*N*S-by-*N*C
matrix. *N*S is the number of time samples.
*N*C is the number of channels. For matrix
input signals, the sample rate offset is applied independently to each column.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — Output signal scalar | vector | matrix

Output signal, returned as a scalar, vector, or matrix. This output is the same
data type as the input signal.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Sample rate offset** — Sample rate offset 10 (default) | scalar

Sample rate offset in parts per million (ppm), specified as a scalar greater than
–1e6.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as `Interpreted
execution` or `Code generation`.

- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option requires less startup time, but the
  speed of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / RF Impairments and Components

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Apply sample rate offset to input signal

The Sample Rate Offset block applies a sample rate offset to the input signal. Applying a sample
rate offset is equivalent to changing the ADC clock rate.
